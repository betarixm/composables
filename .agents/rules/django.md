# Django Rules

## Type Checking

Use `django-types` to type check Django projects.

```bash
uv add --dev django-types
```

Add `djangorestframework-types` when the project uses Django REST Framework.

`django-types` ships stubs only, so it works with `pyright` strict mode without a type checker plugin.

Do not install `django-stubs` alongside `django-types`. The two packages provide the same modules and conflict. Remove one before adding the other.

Do not switch the project to `mypy` and the `django-stubs` plugin in order to type check Django code.

Keep both packages as development dependencies. They are not needed at runtime.

## Working With The Stubs

Some Django constructs cannot be inferred from the stubs alone. Add explicit annotations at those points instead of suppressing the error.

Annotate custom managers and querysets on the model that uses them.

Declare the `<field>_id` attribute of a `ForeignKey` when the code reads it directly.

Narrow `request.user` before accessing attributes of the concrete user model, since it is typed as an authenticated user or `AnonymousUser`.

Follow [`python-general.md`](python-general.md) for the remaining typing rules, including the limits on `Any` and `# type: ignore`.

## Database

Follow [`database.md`](database.md) for engine selection.

Configure the engine through `DATABASES` from a single environment variable rather than branching on the environment in settings.

Generate migrations with `makemigrations`, commit them, and apply them with `migrate` in every environment.

## Project Conventions

Follow Django's established project structure and conventions, as described in [`python-packaging.md`](python-packaging.md).

Before choosing an approach, check the documentation for the Django version the project depends on.
