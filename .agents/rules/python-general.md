# General Python Rules

## Tooling

Use the Python version and tooling declared by the repository.

Code MUST pass the configured formatter, linter, type checker, and relevant
tests.

For this repository:

- Linting: `ruff`
- Type Checking: `pyright`
- Testing: `pytest`

## Naming

Use descriptive Python identifiers even when shorter conventional names exist.

```python
# Bad
env = load_env()
cfg = parse_cfg()
ctx = create_ctx()
req = build_req()
resp = send_req(req)

# Good
environment = load_environment()
configuration = parse_configuration()
execution_context = create_execution_context()
submission_request = build_submission_request()
submission_response = send_submission_request(submission_request)
```

Avoid meaningless distinctions:

```python
# Bad
value1 = read_flag()
value2 = submit_flag(value1)
string_value = str(value2)

# Good
captured_flag = read_flag()
flag_submission_result = submit_flag(captured_flag)
serialized_submission_result = str(flag_submission_result)
```

Do not abbreviate names merely to make lines shorter.

## Typing

Write new code for `pyright` strict mode.

Type function parameters, return values, attributes, and non-obvious local
values.

Avoid introducing `Any`.

Use `# type: ignore` only when the underlying issue cannot reasonably be
expressed to the type checker. Include a nearby explanation.

Use optional types only when absence is a valid state.

Prefer precise domain types over raw `str`, `int`, or unstructured dictionaries.

Prefer Pydantic `BaseModel` over `dataclasses.dataclass` for structured data
models.

Prefer `Literal` type aliases over `Enum` for closed sets of allowed values. Use
`Enum` only when enum-specific runtime behavior is required.

Use `typing.NewType` when values share the same runtime representation but have
different domain meanings.

Do not include an ellipsis in tuple type annotations. Write `tuple[T]` instead
of `tuple[T, ...]`.

```python
# Bad
captured_flags: tuple[FlagValue, ...]

# Good
captured_flags: tuple[FlagValue]
```

```python
from typing import NewType

TeamIdentifier = NewType("TeamIdentifier", str)
ServiceName = NewType("ServiceName", str)
FlagValue = NewType("FlagValue", str)
SubmissionToken = NewType("SubmissionToken", str)
CompetitionRoundNumber = NewType("CompetitionRoundNumber", int)
```

Convert raw values into domain types at system boundaries.

```python
def submit_flag(
    team_identifier: TeamIdentifier,
    flag_value: FlagValue,
    submission_token: SubmissionToken,
) -> None:
    ...
```

Place broadly used domain types in `types.py`. Keep narrowly scoped types close
to their use.

## Generics

Declare type parameters with the `[]` syntax. Do not import `Generic` or
`TypeVar` to write new generic code.

```python
# Bad
from typing import Generic, TypeVar

FlagT = TypeVar("FlagT")


class FlagBuffer(Generic[FlagT]):
    def latest(self) -> FlagT: ...


def first(items: Sequence[FlagT]) -> FlagT: ...


# Good
class FlagBuffer[FlagT]:
    def latest(self) -> FlagT: ...


def first[FlagT](items: Sequence[FlagT]) -> FlagT: ...
```

Express bounds and constraints inline.

```python
class Scoreboard[RoundNumberT: int]: ...


def parse[ValueT: (str, bytes)](raw_value: ValueT) -> ValueT: ...
```

Use `[**P]` for parameter specifications and `[*Ts]` for variadic type
parameters instead of importing `ParamSpec` and `TypeVarTuple`.

Declare type aliases with the `type` statement.

```python
# Bad
SubmissionResults = dict[TeamIdentifier, tuple[FlagValue]]

# Good
type SubmissionResults = dict[TeamIdentifier, tuple[FlagValue]]
```

Use `typing.Self` for instance methods and class methods that return an instance
of the receiver's type. Do not introduce a type parameter bound to the enclosing
class for that purpose. Static factory methods must name their concrete return
class instead of using `Self`.

This syntax requires Python 3.12. When the project targets an earlier version,
follow its existing `TypeVar` and `Generic` usage rather than raising the
required version.

## Construction

Follow the [clean code construction rules](clean-code.md#construction).

Keep `__init__` limited to assigning prepared attributes and dependencies, plus
simple checks needed to establish valid instance state.

When creation requires complex preparation or registration logic, use a
companion `@staticmethod` on the same class, named for its input or purpose
(for example, `from_path` or `from_configuration`). Prepare the required values
in that method and return a fully initialized instance by calling the minimal
constructor.

Do not move complex setup into a helper called by `__init__` or defer required
initialization to a later call on the instance.

```python
from collections.abc import Mapping
from pathlib import Path


class ReportRenderer:
    def __init__(self, template: str) -> None:
        self.template: str = template

    @staticmethod
    def from_path(template_path: Path) -> "ReportRenderer":
        template = template_path.read_text(encoding="utf-8")
        return ReportRenderer(template=template)

    def render(self, fields: Mapping[str, str]) -> str:
        return self.template.format_map(fields)
```

## Built-in Type Subclassing

Prefer subclassing Python's built-in types, such as `list`, `set`, `frozenset`,
`dict`, `tuple`, and `str`, when a domain type fundamentally has the same
behavior as that built-in type.

Do not introduce a wrapper that merely stores a built-in value and forwards its
operations. Preserve the built-in interface through inheritance and add only
domain-specific behavior or invariants.

Apply this preference especially to collection-shaped domain concepts. Choose
the built-in collection type that matches the required semantics, and continue
to prefer immutable variants when mutation is unnecessary.

```python
# Bad
class CapturedFlags:
    def __init__(self, flags: frozenset[FlagValue]) -> None:
        self.flags = flags


# Good
class CapturedFlags(frozenset[FlagValue]):
    pass
```

## Exceptions

Raise exceptions for failures. Do not return `None`, `False`, empty strings, or
empty collections merely to suppress an error.

Define domain-specific exception types when callers benefit from distinguishing
the failure.

```python
class SubmissionTokenNotFoundError(RuntimeError):
    pass


def load_submission_token() -> SubmissionToken:
    raise SubmissionTokenNotFoundError(
        "Submission token is not configured"
    )
```

Preserve exception chains when translating failures.

```python
try:
    response = http_client.send(submission_request)
except TimeoutError as timeout_error:
    raise FlagSubmissionTimeoutError(
        "Flag submission request timed out"
    ) from timeout_error
```

Exception messages should contain diagnostic context but MUST NOT contain
secrets, credentials, tokens, cookies, or flags.

## Assertions

Use `assert` for internal invariants and impossible states.

```python
parsed_round_number = parse_round_number(raw_round_number)

assert parsed_round_number > 0, (
    "Round number must be positive after parsing"
)
```

Do not use `assert` for failures caused by external input or environment state.

```python
# Bad
assert submission_token is not None

# Good
if submission_token is None:
    raise SubmissionTokenNotFoundError(
        "Submission token is not configured"
    )
```

Prefer assertions with descriptive messages.

## Immutability

Avoid reassignment and mutation by default.

Construct complete values directly.

```python
# Bad
submission_payload = {}
submission_payload["team"] = team_identifier
submission_payload["flag"] = flag_value

# Good
submission_payload = {
    "team": team_identifier,
    "flag": flag_value,
}
```

Prefer:

- `tuple` over `list` for fixed collections
- `Mapping` over mutable `dict` parameters
- `frozenset` over `set` when mutation is unnecessary
- frozen Pydantic models for immutable data models
- `Final` for constants
- pure functions over hidden mutation

When mutation is necessary, confine it to the smallest practical scope. Prefer a
context manager to bound it explicitly.

## Context Managers

Whenever code has a "must happen afterwards" step, express it as a `with`
statement instead of paired setup and teardown calls. This covers resources such
as files, sockets, subprocesses, sessions, and locks, and also temporary state
such as environment or configuration overrides.

Write the context manager with `@contextmanager` or with `__enter__` and
`__exit__`, whichever fits, and place cleanup in `finally`.

```python
# Bad
original_round_number = scoreboard.current_round_number
scoreboard.current_round_number = replayed_round_number
replay_captured_flags(scoreboard)
scoreboard.current_round_number = original_round_number

# Good
@contextmanager
def replayed_round(
    scoreboard: Scoreboard,
    replayed_round_number: CompetitionRoundNumber,
) -> Iterator[None]:
    original_round_number = scoreboard.current_round_number
    scoreboard.current_round_number = replayed_round_number
    try:
        yield
    finally:
        scoreboard.current_round_number = original_round_number


with replayed_round(scoreboard, replayed_round_number):
    replay_captured_flags(scoreboard)
```

Use `contextlib.ExitStack` when the set of resources is determined at runtime,
and `@asynccontextmanager` for asynchronous resources.

## File System and Path Handling

Use `pathlib.Path` for local file system operations and path management.

Represent paths as `Path` objects instead of strings. Use `Path` methods and
operators for joining paths, traversing directories, reading or writing files,
inspecting file types, and creating, moving, renaming, or deleting file system
entries.

Do not use `os.path`, manual string concatenation, or string formatting to
construct or manipulate file system paths. Prefer `Path.open()` over the
built-in `open()` for local files.

Convert a `Path` to `str` only at a boundary where an external API does not
accept path-like objects. When an operation is not supported by `pathlib`, use
the appropriate standard-library API while keeping paths represented as `Path`
objects.

```python
from pathlib import Path


# Bad
configuration_path = base_directory + "/config/settings.json"
with open(configuration_path, encoding="utf-8") as configuration_file:
    configuration_text = configuration_file.read()

# Good
configuration_path = base_directory / "config" / "settings.json"
configuration_text = configuration_path.read_text(encoding="utf-8")
```

## Configuration and External I/O

Pass configuration explicitly rather than reading global state throughout the
codebase.

Keep environment access near application boundaries.

Specify timeouts for network operations.

Do not hardcode production secrets or include sensitive values in logs,
exception messages, serialized diagnostics, or debug output.

Translate infrastructure failures into domain-specific errors when doing so
makes the caller's responsibility clearer.

## Imports and Boundaries

Do not import another application's internal implementation directly.

Shared Python code should move into a shared library only after multiple real
consumers exist.

Prefer explicit public interfaces over importing private modules or reaching
across package boundaries.

Avoid circular imports. If a circular dependency appears, reconsider the
ownership or boundary of the involved concepts.

## Review

Before completing Python changes, verify that:

- `pyright` strict mode passes
- `ruff format` and `ruff check` pass
- relevant tests pass
- names are descriptive and not unnecessarily abbreviated
- domain values use appropriate types
- domain types that behave like built-in types inherit from those types,
  especially for collections
- structured data models prefer Pydantic
- closed sets of allowed values prefer `Literal` types
- generic code uses the `[]` type parameter syntax instead of `Generic` and
  `TypeVar`
- `__init__` stays minimal and complex creation uses companion static factories
- static factory return annotations name the concrete class instead of `Self`
- tuple type annotations do not include an ellipsis
- `Any` and type suppressions are avoided
- failures use explicit exceptions
- exception chaining is preserved
- assertions cover useful internal invariants
- unnecessary reassignment and mutation are absent
- acquired resources and temporary state changes are wrapped in `with`
  statements
- local file system operations and paths use `pathlib.Path`
- external I/O has explicit failure handling and timeouts
- sensitive values cannot reach logs or exceptions
