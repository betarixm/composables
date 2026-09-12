# TypeScript Rules

## Type Safety

Use TypeScript in strict mode.

Prefer precise types. Do not weaken the type system merely to make code compile.

Avoid `any`. Use `unknown` for values whose type is genuinely unknown, then narrow them explicitly before use.

Avoid type assertions (`as`) unless the type cannot reasonably be expressed or inferred otherwise.

Do not use non-null assertions (`!`) merely to silence the type checker. Prove or validate that the value exists.

Prefer discriminated unions and exhaustive narrowing over loosely structured objects or optional fields representing multiple states.

```typescript
type SubmissionState =
  | { readonly status: "pending" }
  | { readonly status: "succeeded"; readonly identifier: string }
  | { readonly status: "failed"; readonly error: Error };
```

Handle impossible states explicitly. Prefer exhaustive checks when working with unions.

## Types

Prefer `type` aliases over `interface`.

```typescript
type User = {
  readonly identifier: string;
  readonly name: string;
};
```

Use `interface` only when its specific semantics are required, such as declaration merging or compatibility with an API that explicitly benefits from interfaces.

Prefer composing types with unions, intersections, mapped types, and utility types rather than inheritance-heavy type hierarchies.

Avoid overly broad types such as `object`, `Function`, `{}`, or unstructured dictionaries when a precise type can be defined.

## Variables

Use `const` by default.

Use `let` only when reassignment is inherently required by the algorithm.

Never use `var`.

Prefer creating a new value over repeatedly reassigning an existing variable.

```typescript
// Bad
let endpoint = configuration.host;
endpoint += "/submit";

// Good
const submissionEndpoint = `${configuration.host}/submit`;
```

## Functions

Prefer arrow functions.

```typescript
const submitFlag = async (
  submissionRequest: SubmissionRequest,
): Promise<SubmissionResponse> => {
  // ...
};
```

Use function declarations only when their semantics or surrounding conventions provide a concrete benefit.

Prefer small functions with explicit inputs and outputs.

Avoid hidden mutation and implicit dependencies.

Specify return types for exported functions and other public boundaries. Prefer explicit return types when they improve readability or prevent accidental API changes.

## Immutability

Treat values as immutable by default.

Use `readonly` aggressively for object properties, parameters, collections, tuples, and public data structures.

```typescript
type Team = {
  readonly identifier: TeamIdentifier;
  readonly name: string;
  readonly services: readonly Service[];
};
```

Prefer:

* `readonly T[]` or `ReadonlyArray<T>` over mutable arrays when mutation is unnecessary
* `Readonly<T>` where appropriate
* `as const` for immutable literals and literal type preservation
* immutable transformations such as `map`, `filter`, and object spread over in-place mutation

Do not mutate function arguments.

Do not expose mutable internal collections through public APIs.

## Enums and Literals

Use `enum` only when it provides a concrete benefit.

For simple finite sets of values, prefer literal unions.

```typescript
type DeploymentState = "pending" | "running" | "failed";
```

Prefer `as const` objects when runtime values and corresponding literal types are both useful.

```typescript
const deploymentStates = {
  pending: "pending",
  running: "running",
  failed: "failed",
} as const;

type DeploymentState =
  (typeof deploymentStates)[keyof typeof deploymentStates];
```

Do not introduce an `enum` merely because a value has several possible variants.

## Nullability

Represent absence intentionally.

Do not make fields optional merely for convenience.

Distinguish between a property that may be absent and a property whose value may explicitly be `undefined` or `null`.

Avoid propagating nullable values through the codebase. Validate or narrow them near system boundaries whenever practical.

Use optional chaining and nullish coalescing only when the underlying absence is semantically valid.

## External Data

Treat data entering the program from outside the type system as untrusted.

Examples include:

* HTTP responses
* JSON
* environment variables
* local storage
* user input
* message queues
* third-party JavaScript

Do not use type assertions to pretend external data is valid.

Parse or validate external data at the boundary and convert it into trusted domain types before further use.

## Imports

Use `import type` for type-only imports when appropriate.

```typescript
import type { SubmissionRequest } from "./submission-request";
```

Keep runtime dependencies distinguishable from type-only dependencies.

Follow the project's configured module system and import conventions.

## Review

Before completing TypeScript changes, verify that:

* strict type checking passes
* `any` is absent unless unavoidable and justified
* `unknown` values are narrowed before use
* unnecessary type and non-null assertions are absent
* `type` is preferred over `interface`
* variables use `const` unless reassignment is required
* functions use arrow syntax by default
* objects and collections are `readonly` where practical
* arguments are not mutated
* literal unions are preferred over unnecessary enums
* nullable and optional values represent real domain states
* external data is validated before being treated as trusted
* exported APIs have precise and stable types
