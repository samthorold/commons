---
address: guides/global.md#checks-and-ci
origin: a private docs-and-data repo, its first CI PR
signal: gap
---

*Checks and CI* leaves installing and pinning pre-commit, and how actionlint finds a shellcheck, to the Stack's Guide. A repo with no Stack (docs and data only) then has no rule. One answer was verified to work:

- run pre-commit as `uvx pre-commit@<exact version>`, locally and in CI, after `astral-sh/setup-uv`. The version in that command is the pin, so the repo's `CLAUDE.md` and `ci.yml` change it together;
- take every hook from a remote hook repo pinned by `rev`, since there is no lock file for local hooks to run from;
- give the `actionlint-py` hook `additional_dependencies: [shellcheck-py==<version>]`. A probe workflow with an unquoted `$VAR` reported SC2086 with no system shellcheck installed, so actionlint does shellcheck `run:` steps that way.

The Global Guide could state this as the default for a repo without a Stack.
