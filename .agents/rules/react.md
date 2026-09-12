# React Rules

## Current Guidance

Before implementing or refactoring React code, check the current official React documentation for recommended APIs and patterns.

Prefer `react.dev` over memory, old examples, blog posts, or legacy conventions.

Do not introduce legacy React APIs when a current recommended alternative exists.

Follow framework-specific React guidance when using frameworks such as Next.js or React Router.

## Components

Use function components only. Do not introduce class components.

Prefer small, focused components with a single clear responsibility.

Split a component when a meaningful part of its UI or behavior can be named independently.

Prefer one React component per file.

Do not keep multiple components in one file merely because they are currently small. Colocation of non-component helpers, types, and constants is acceptable when they are specific to that component.

Keep components pure. Rendering MUST NOT mutate existing values or perform side effects.

Never call component functions directly. Render components through JSX.

## Props

Keep component interfaces explicit and narrow.

Pass only the values a component needs.

Do not pass large objects merely to avoid defining a proper component interface.

Do not mutate props.

Prefer composition over configuration-heavy components with large numbers of behavioral flags.

Avoid boolean props that create many unrelated component modes. Split substantially different behavior into separate components when practical.

## State

Choose state management according to the scope and requirements of the state. Do not mandate a single state-management mechanism for the entire application.

Keep state local when only one component or subtree needs it.

Lift state to the closest common owner when multiple components must coordinate.

Use Context, reducers, external state libraries, URL state, or framework-provided state mechanisms when their use is justified by the problem.

Do not introduce a state-management library by default.

Each piece of state SHOULD have a single source of truth.

Avoid:

* redundant state that can be derived during rendering
* duplicated state
* contradictory state
* unnecessarily deeply nested state
* copying props into state without a specific reason

Prefer deriving values from existing props and state over synchronizing duplicate values.

## Effects

Treat Effects as an escape hatch for synchronization with systems outside React.

Do not use `useEffect` merely to:

* derive values for rendering
* synchronize one piece of React state with another
* respond to a user interaction that can be handled directly by an event handler
* perform transformations that can happen during rendering

Prefer event handlers for interaction-driven side effects.

Prefer direct derivation during rendering for computed values.

Effects MUST declare correct dependencies and clean up external subscriptions or resources when necessary.

## Hooks

Follow the Rules of Hooks.

Call Hooks only at the top level of React components or custom Hooks.

Do not call Hooks conditionally, inside loops, or inside nested functions.

Extract reusable stateful behavior into custom Hooks when doing so creates a meaningful abstraction.

Do not create custom Hooks that merely rename or mechanically wrap another Hook without adding useful semantics.

## Immutability

Treat props, state, Context values, and Hook arguments as immutable snapshots.

Do not mutate state directly.

Create new values when updating objects or collections used by React.

Do not mutate values after passing them to JSX.

## Memoization

Do not add `useMemo`, `useCallback`, or `React.memo` reflexively.

When React Compiler is available and supported by the project, prefer relying on the compiler for routine memoization.

Use manual memoization only when there is a concrete reason, such as required reference stability, explicit control over an Effect dependency, or a demonstrated performance problem.

Do not sacrifice code clarity for speculative render optimization.

Before introducing manual memoization, check the current React guidance because recommended practices may change with React Compiler.

## Review

Before completing React changes, verify that:

* current official React guidance was considered
* only function components are used
* components are small and focused
* each component normally has its own file
* rendering remains pure
* props and state are not mutated
* state has a clear owner and single source of truth
* redundant state is not stored
* Effects are used only when synchronization is actually required
* Hooks follow the Rules of Hooks
* state-management dependencies were introduced only when justified
* manual memoization has a concrete reason
