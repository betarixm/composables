# Clean Code Rules

## Central Dogma

Implement the rules that generate cases, not the cases themselves.

Before writing code, identify the shared invariants, canonical representation,
state transitions, and independent axes of variation.

Normalize inputs early and express each policy from a single source of truth.
Keep examples and case enumeration in tests or data instead of production
branches.

A new case within the existing semantic model should not require another
production branch. If it does, redesign the model around the shared rule.

Do not stop at the first implementation that passes the current tests or rely
on a later refactor to reveal the intended design. The first delivered
implementation should already express the coherent model.

Do not force semantically distinct behavior into one abstraction or
generalize for hypothetical requirements.

## Naming

Prefer long, descriptive names. Names should explain their role without
requiring surrounding context.

Do not shorten names merely for convenience. Autocomplete makes brevity
unnecessary.

Avoid abbreviations such as:

* `env` → `environment`
* `cfg` → `configuration`
* `ctx` → `context`
* `req` → `request`
* `resp` → `response`
* `repo` → `repository`
* `dep` → `dependency`
* `msg` → `message`
* `exc` → `exception`
* `fn` → `function`
* `tmp` → `temporary`
* `id` → `identifier`

Preserve externally defined names when changing them would break compatibility,
including protocol fields, external APIs, file formats, CLI options, and
environment variables.

Avoid vague names such as `data`, `info`, `value`, `item`, and `object` when a
more specific role is known.

Do not encode type information into names unless it conveys domain meaning.

Avoid numbered names such as `result1`, `result2`, or `handler3`. Name the
semantic difference instead.

```text
Bad:
value1
value2

Good:
captured_flag
flag_submission_result
```

## Explicitness

Make dependencies, state transitions, failures, and side effects explicit.

Prefer code whose behavior can be understood locally. Avoid hidden global
state, implicit configuration, and surprising side effects.

Pass configuration and dependencies explicitly where practical.

Prefer dependency injection for external collaborators and infrastructure
dependencies. Supply them through constructors, function parameters, or
factories rather than constructing them inside consumers or retrieving them
from global state or service locators.

Do not use primitive values as substitutes for distinct domain concepts when
the language provides a practical way to distinguish them.

## Construction

Keep constructors minimal: assign prepared properties and dependencies, and
perform only simple checks needed to establish valid instance state.

Move complex preparation, registration, parsing, and external I/O into named
factory methods on the class. Have each factory prepare the required values
and return a fully initialized instance through the minimal constructor.

Do not hide complex setup in helpers called by the constructor or require a
separate initialization call after construction.

## Error Handling

Represent failures explicitly.

Do not hide failures behind sentinel values such as `null`, `None`, `False`,
empty strings, or empty collections unless absence is an expected part of the
domain.

Errors should identify what failed and include enough context to diagnose the
problem.

Preserve the original cause when translating low-level failures into
domain-specific errors.

Never include secrets, credentials, tokens, flags, cookies, or other sensitive
values in logs or error messages.

## Assertions

Use assertions for states that should be impossible if the program is correct.

Good uses include:

* internal invariants
* postconditions after parsing or validation
* assumptions required by internal algorithms
* unreachable states

Do not use assertions for expected runtime failures such as invalid external
input, unavailable files, network failures, or missing configuration. Handle
those explicitly.

Include a useful assertion message whenever practical.

## Immutability

Treat values as immutable by default.

Prefer constructing complete values over creating partially initialized values
and mutating them afterward.

Avoid reassigning variables when a new name can represent the transformed value
more clearly.

Prefer immutable collections and data structures when mutation is unnecessary.

Prefer pure functions over functions with hidden side effects.

When mutation is required for performance or interoperability, keep it local
and isolate it behind a small interface.

## Boundaries

Keep components independent.

Do not reach into another component's internal implementation. Exchange
explicit domain values or serializable models across boundaries.

Do not create shared abstractions prematurely. Move code into shared
infrastructure only after multiple real consumers require the same behavior.

Prefer duplication over a poorly defined shared abstraction.

## Configuration and Secrets

Keep configuration explicit and secrets external to source code.

Never:

* hardcode production secrets
* bake secrets into build artifacts
* expose secrets through logs or exceptions
* rely on undocumented machine state

External operations should have explicit failure behavior and reasonable
timeouts.

Prefer failing closed when security-sensitive behavior cannot be completed
safely.

## Review

Before completing a change, verify that:

* production code expresses shared rules instead of enumerating known cases
* policies have a single source of truth
* names describe intent rather than implementation details
* unnecessary abbreviations are absent
* numbered or vague names are absent
* dependencies and side effects are explicit
* constructors are minimal, with complex creation logic in named factories
* failures are represented explicitly
* internal invariants are asserted where useful
* unnecessary mutation and reassignment are absent
* secrets cannot appear in logs or errors
* component boundaries remain intact
