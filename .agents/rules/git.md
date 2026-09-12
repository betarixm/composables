# Git Rules

Use `git` commands instead of the GitHub CLI (`gh`) for all operations that Git
supports. Use `gh` only for GitHub-specific operations that `git` cannot perform.

Maintain a semi-linear commit history: rebase branches onto the target branch
before merging, and preserve merge commits for completed branches.

Write commit messages according to the Conventional Commits specification.
