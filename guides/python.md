# Python Guide

**Scope:** Stack = Python (and the Python+Rust cell, under *Rust extensions*), any Archetype.

The default setup for every Python project. When starting or touching a Python repo, bring it in line with this, and record the project's own specifics (commands, check names, versions, traps) in that repo's `CLAUDE.md`. Reference implementations: `~/Projects/py-ev` (single Python version) and `~/Projects/superenums` (Python version matrix, multiple type checkers). Copy files from them rather than rewriting from memory. Changes to this Guide are Revisions of the Commons: see the commons `README.md`.

Conventions used for one job live in files under `~/.claude/commons/guides/python/`, and each section says when to read its file. Links are relative to this file.

## Tooling

Decides the tools and how they are pinned: uv (itself pinned), ruff, the type checkers, pytest, the version's single source, the Taskfile.
Before setting up a Python repo, or changing its dependencies, build backend, uv version or tool config, read [tooling](python/tooling.md).

## Testing

How Python Adopters carry out the Agentic development Guide's test-first Stance (the `/tdd` Skill is the Procedure; its examples are Python).

- **Test through the package's public interface**, with plain pytest functions and `assert`. Shared setup goes in fixtures (`conftest.py`), files in `tmp_path`, never the real filesystem or the user's data.
- **Replace only boundaries, and by injection**: pass in a fake (a small class or function with the boundary's interface) rather than patching. `monkeypatch` is for boundaries that can't be injected (environment variables, `builtins.input`), never for the package's own modules: a test that patches internals breaks on a refactor that keeps behaviour.
- **A callable that crosses a process pool lives in the package**, not in the test module. Under the `spawn` start method (the default on macOS and Windows) workers re-import it by module path, and `tests` isn't importable from them, so a fake defined in a test fails with `ModuleNotFoundError: tests`. Pass a real callable from the package, keep pool-crossing fakes in a small helper module in the package, or test with one worker and cover parallel = serial with a package callable.
- **Randomness is a parameter**: code takes a `random.Random` (or a seed) instead of using the module-level `random`, so a test passes a seeded instance and the run is reproducible.

## pre-commit and CI

Decides the Python hooks (run through `uv run --locked`) and the steps of the `pre-commit` CI job, with its Python version matrix.
On a fresh clone, or before setting up or changing a repo's hooks or CI workflow, read [pre-commit and CI](python/checks.md).

## Releases

Decides how a release is cut: its own version-bump PR, published by `release.yml` when merged; feature PRs never change the version, and nobody tags by hand.
Before cutting a release, touching the version, or changing `release.yml`, read [releases](python/releases.md).

## Rust extensions

Decides how a Rust extension sits in a Python repo (maturin's mixed layout under `rust/`, stubs, hooks, CI, wheels) and how it is tested against the Python reference.
Before adding a Rust extension to a Python project, or changing its build, hooks, CI, release or differential tests, read [Rust extensions](python/rust-extensions.md).

## Lessons

If something in this Guide proves wrong or incomplete while you work (a Contradiction, a Deviation, a Gap or a Trap that another Python project would also hit), record a Lesson addressed to this Guide (to the section's detail file, where the Lesson is about one job), as described in `~/.claude/commons/lessons/README.md`. Trouble specific to one project stays in that project's own docs.
