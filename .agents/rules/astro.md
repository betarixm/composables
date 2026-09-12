# Astro Rules

## Rendering

Prefer static HTML and server rendering by default.

Client-side JavaScript should be opt-in.

Use Astro components for non-interactive UI whenever practical.

Do not hydrate a component unless browser-side interactivity is actually required.

Prefer:

1. static Astro components
2. server-rendered components
3. server islands when appropriate
4. small client islands

over shipping a large client-rendered application.

Avoid turning an Astro page into a SPA unless the application's requirements genuinely justify it.

## Client Islands

Use `client:*` directives only when a component requires browser-side execution.

Keep client islands small and focused.

Do not hydrate a large component merely because one nested element is interactive. Extract the interactive element into its own island.

Choose the least eager hydration strategy that satisfies the user experience.

Prefer deferred hydration such as `client:idle`, `client:visible`, or another appropriate directive when immediate hydration is unnecessary.

Use eager hydration only when the interaction must be available immediately.

Do not use `client:only` when server-rendered HTML can provide a useful initial representation.

## Interactivity

Prefer native HTML and CSS over JavaScript when they provide the required behavior.

Use client-side JavaScript when it materially improves:

* responsiveness
* direct manipulation
* local interactive state
* browser-specific behavior
* real-time updates
* accessibility

Accessibility takes precedence over reducing JavaScript.

However, do not replace semantic HTML with JavaScript-driven widgets when the platform already provides accessible behavior.

## Server Islands

Use server islands for independently dynamic or personalized server-rendered regions when they improve caching or prevent slow dynamic content from blocking the rest of the page.

Do not move logic to the client merely because part of a page is dynamic.

Prefer keeping personalization, data access, and privileged operations on the server whenever browser execution is unnecessary.

## JavaScript Budget

Treat every client-side dependency and hydrated component as a cost.

Before adding browser JavaScript, ask whether the same user experience can be implemented with:

* static HTML
* server rendering
* semantic HTML
* CSS
* a smaller isolated client island

Do not ship JavaScript for content that is purely presentational.

Before choosing hydration or rendering behavior, check the current official Astro documentation and prefer the latest recommended approach.
