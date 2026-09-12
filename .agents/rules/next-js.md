# Next.js Rules

## Rendering

Prefer server rendering and Server Components by default.

Minimize client-side JavaScript.

Use Client Components only when browser-side execution provides a concrete benefit, such as:

* user interaction requiring local state
* browser APIs
* real-time interaction
* client-only libraries
* interactive accessibility behavior that cannot be expressed with native HTML

Do not add `"use client"` merely because a component is rendered inside another Client Component.

Keep the client boundary as small and as deep in the component tree as practical.

Prefer:

```text
Server Component
├── Server Component
├── Server Component
└── Small Client Component
```

over:

```text
Large Client Component
├── Static content
├── Static content
└── Interactive content
```

Move static markup, data fetching, formatting, and non-interactive rendering back to Server Components whenever practical.

Do not convert an entire page or layout into a Client Component to support one interactive child.

## Data and Interactivity

Fetch data on the server by default.

Do not fetch data again in the browser when the server can provide it during rendering.

Prefer server-side operations for work that does not require immediate browser interaction.

Use client state only for state that genuinely belongs to the browser or an interactive session.

Do not mirror server data into client state without a concrete reason.

Prefer native HTML behavior before introducing JavaScript.

Accessibility is more important than minimizing JavaScript. Use client-side behavior when necessary to provide correct keyboard interaction, focus management, live updates, or other accessible interaction patterns.

However, do not implement behavior in JavaScript when semantic HTML already provides the required interaction and accessibility.

## Client Boundaries

Treat `"use client"` as an explicit server-to-client boundary.

Before adding it, determine which exact behavior requires browser execution.

Place the boundary around the smallest meaningful interactive component.

Avoid importing large dependency trees into Client Components when only a small part is needed in the browser.

Keep server-only code, secrets, database access, and privileged operations outside the client module graph.

Before choosing a rendering or data-fetching pattern, check the current official Next.js documentation and prefer the latest recommended approach.
