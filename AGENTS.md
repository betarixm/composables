# Instructions

## Scope

These instructions apply to the entire repository.

If a deeper directory contains its own `AGENTS.md`, follow the more specific
instructions for files within that directory.

## Rules

Before making changes, read the rules relevant to the task.

Always follow:

* [`.agents/rules/clean-code.md`](.agents/rules/clean-code.md)
* [`.agents/rules/file-naming.md`](.agents/rules/file-naming.md)
* [`.agents/rules/git.md`](.agents/rules/git.md)

Apply additional rules based on the files and technologies involved:

* Markdown: [`.agents/rules/markdown.md`](.agents/rules/markdown.md)
* Python: [`.agents/rules/python-general.md`](.agents/rules/python-general.md)
* Python packaging: [`.agents/rules/python-packaging.md`](.agents/rules/python-packaging.md)
* Python tooling and dependencies: [`.agents/rules/python-uv.md`](.agents/rules/python-uv.md)
* Django: [`.agents/rules/django.md`](.agents/rules/django.md)
* TypeScript: [`.agents/rules/typescript.md`](.agents/rules/typescript.md)
* Bun: [`.agents/rules/typescript-bun.md`](.agents/rules/typescript-bun.md)
* React: [`.agents/rules/react.md`](.agents/rules/react.md)
* Next.js: [`.agents/rules/next-js.md`](.agents/rules/next-js.md)
* Astro: [`.agents/rules/astro.md`](.agents/rules/astro.md)
* Databases and ORMs in web applications: [`.agents/rules/database.md`](.agents/rules/database.md)
* Research-related tasks only: [`.agents/rules/research.md`](.agents/rules/research.md)

Multiple rule files may apply to the same change. Follow all applicable rules.

When rules conflict, prefer the more specific rule over the more general rule.

## Existing Projects

Respect the existing architecture, tooling, and conventions of the project
being modified.

Do not introduce a new framework, package manager, formatter, linter, test
runner, or architectural pattern solely to conform to these boilerplate
preferences when the existing project has an established alternative.

Prefer incremental changes over unrelated refactoring. When a small patch would
add case-specific exceptions or duplicate a policy, make the smallest in-scope
change that restores a coherent invariant-based design instead.

## Verification

After making changes, run the relevant formatter, linter, type checker, tests,
and build commands defined by the project.

Do not consider a change complete while known relevant checks are failing.
