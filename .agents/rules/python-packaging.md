# Python Packaging Rules

## Workspace

* Every Python package MUST be a member of the `uv` workspace.
* Configure each package's build settings so that workspace dependencies are installed and importable correctly.
* All Python packages MUST live under `packages/`.
* Python packages MUST use a flat layout. Place each import package directly under its workspace member directory.
* Do not create or retain a `src/` directory for Python packages.
* All Python tests MUST live under the project-root `tests/` directory.
* Prefer registering all workspace packages as root development dependencies to maintain a single shared `.venv`.

Example:

```text
<project-root>/
├── packages/
    └── python-package1/
        ├── python_package1/
        │   ├── __init__.py
        │   ├── py.typed
        │   └── <notion>/
        ├── README.md
        └── pyproject.toml
└── tests/
```

When a package uses the `uv_build` backend, configure the flat layout explicitly:

```toml
[tool.uv.build-backend]
module-root = ""
```

Scaffolding defaults do not override this layout. If a project initializer creates `src/<import-package>/`, move the import package to the workspace member directory and remove `src/`.

## Library Packages

A **notion** represents a domain concept in the business logic.

Notion directory names MUST be singular.

Each notion is a directory containing modules named after plural, general programming concepts.

Example:

```text
<notion>/
├── __init__.py
├── functions.py
├── types.py
└── models.py
```

A library package SHOULD be a flat collection of notions.

Avoid introducing additional architectural layers unless they are clearly necessary.

## Application Packages

Prefer placing application code directly in `__init__.py`.

When using a framework with an established project structure, such as Django, FastAPI, or Flask, follow the framework's conventions instead.

Do not avoid creating application packages merely to reduce the package count. Prefer small, explicit application packages over combining unrelated applications.
