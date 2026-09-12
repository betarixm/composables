# Bun Rules

## Default Tooling

Prefer Bun for JavaScript and TypeScript projects.

Use Bun as the default:

* package manager
* script runner
* package executor
* test runner
* JavaScript and TypeScript runtime

Prefer:

```bash
bun install
bun add <package>
bun remove <package>
bun run <script>
bunx <package>
bun test
```

over equivalent `npm`, `npx`, `yarn`, or `pnpm` commands.

Do not introduce another JavaScript package manager unless the project, framework, deployment environment, or dependency requires it.

## Project Setup

Use Bun when initializing new JavaScript or TypeScript projects unless the chosen framework provides a Bun-compatible initializer that should be used instead.

Commit the Bun lockfile.

Do not maintain multiple package-manager lockfiles.

When migrating an existing project to Bun, remove obsolete lockfiles only after confirming that Bun installation and project tooling work correctly.

## Runtime

Prefer running JavaScript and TypeScript directly with Bun when the application supports it.

```bash
bun run src/index.ts
```

Prefer Bun's built-in TypeScript support over adding runtime transpilation tools solely to execute TypeScript.

Do not introduce Node.js-specific runtime dependencies when Bun provides an appropriate built-in capability and portability is not required.

However, do not use Bun-specific APIs in libraries that are expected to run across multiple JavaScript runtimes unless the Bun dependency is intentional.

## Built-in APIs

Prefer Bun's built-in capabilities over additional dependencies when they provide a clear and sufficient implementation.

Examples include:

* `Bun.serve`
* `Bun.file`
* `Bun.write`
* `Bun.spawn`
* `Bun.$`
* built-in database clients
* built-in hashing and password APIs

Do not add a dependency merely to wrap functionality already provided cleanly by Bun.

Prefer Web-standard APIs when they are equally suitable and improve portability.

## Testing

Prefer `bun test` for new test suites when compatible with the project.

Use `bun:test` for Bun-native tests.

Avoid introducing Jest or another test runner solely out of convention when `bun test` satisfies the requirements.

Preserve an existing test framework when migration would provide little value or create compatibility problems.

## Scripts

Run project scripts through Bun.

```bash
bun run lint
bun run typecheck
bun run test
bun run build
```

Use `bunx` for package executables that are not installed as project scripts.

Do not rely on globally installed JavaScript tools when they can be executed through the project's Bun environment.

## Compatibility

Bun preference does not override correctness or ecosystem requirements.

Before replacing Node.js-specific tooling or adopting Bun-specific APIs, verify compatibility with:

* the framework
* build tooling
* native dependencies
* deployment environment
* CI environment

Do not introduce compatibility workarounds solely to force Bun where the supported ecosystem path is clearly better.

Prefer incremental Bun adoption when full runtime migration is unnecessary.

## Review

Before completing JavaScript or TypeScript changes, verify that:

* Bun is used instead of another package manager where practical
* project scripts run through `bun run`
* package executables use `bunx`
* tests use `bun test` when appropriate
* unnecessary runtime or tooling dependencies are avoided
* Bun built-ins are considered before adding dependencies
* Bun-specific APIs do not accidentally reduce required portability
* only one package-manager lockfile is maintained
