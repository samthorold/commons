# Python Guide: pre-commit and CI

The *pre-commit and CI* Conventions of [the Python Guide](../python.md#pre-commit-and-ci), which says when to read them.

## pre-commit

- `uv run pre-commit install` once per clone. `uv run pre-commit run --all-files` is exactly what CI runs.
- pre-commit itself is a dev dependency. Beyond the Global Guide's hooks (plus `debug-statements`), local hooks run through `uv run --locked` (so they use `uv.lock`'s versions, and fail if it's stale): ruff check `--fix`, ruff format, the type checker(s), actionlint, shellcheck, and the tests (`pass_filenames: false`).
- actionlint and shellcheck come from PyPI as dev dependencies (`actionlint-py`, `shellcheck-py`), not system installs.

## CI (GitHub Actions)

The shape is the Global Guide's *Checks and CI*; the Python steps are:

- The `pre-commit` job runs `uv sync --locked` then `uv run --locked pre-commit run --all-files --show-diff-on-failure`, after `astral-sh/setup-uv` with `enable-cache: true`. The `push` to `main` paths are `[uv.lock]`.
- Several Python versions: a matrix, job named `pre-commit (${{ matrix.python-version }})`, with `env: UV_PYTHON: ${{ matrix.python-version }}` so every `uv` call, including the hooks', uses it. One version: no matrix.
