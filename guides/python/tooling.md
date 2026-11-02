# Python Guide: tooling

The *Tooling* Conventions of [the Python Guide](../python.md#tooling), which says when to read them.

- **uv for everything**: environments, dependencies, running tools (`uv run ...`, `uv add --dev ...`). No bare `pip`, no globally installed tools. src layout, `uv_build` backend.
- **uv itself is pinned** with `[tool.uv] required-version = "==X.Y.Z"` in `pyproject.toml`, and the `[build-system]` bound matches it (`uv_build>=X.Y.Z,<X.(Y+1)`). setup-uv reads the pin in CI; without it, CI silently uses the latest uv and drifts from local. Upgrade uv deliberately in one PR (pin, build bound, `uv lock`). Locally, uv comes from the standalone installer (`~/.local/bin`), so `uv self update <version>` works.
- **Dev dependencies pinned exactly** (`==`), so `uv.lock`, pre-commit and CI run identical versions.
- **ruff** for lint and format. Rule set: `E, W, F, I, B, UP, SIM, RUF`, `target-version` = the minimum Python. If ruff should skip some paths (`extend-exclude`), also set `force-exclude = true`, because pre-commit passes files explicitly and ruff ignores excludes for explicit files otherwise.
- **Type checking**: ty at least. Add pyright and/or mypy (strict) where typing is part of the product. Put pyright config in `pyrightconfig.json`, not `[tool.pyright]`: a `pyrightconfig.json` in a parent directory (e.g. `~`) wins over a pyproject section.
- **pytest**, with doctests where the project has them.
- **Version**: single source in `pyproject.toml`. The package's `__version__ = importlib.metadata.version("<dist-name>")`, with a test that it matches `pyproject.toml`.
- **Taskfile.yml** ([Task](https://taskfile.dev)) for common commands: `test`, `lint`, `fmt`, plus project-specific ones, and `version` / `bump` (`uv version --bump {{.CLI_ARGS}}`). Without `task` installed: `uvx --from go-task-bin task <name>`.
