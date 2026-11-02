# Rust Guide: pre-commit and CI

The *pre-commit and CI* Conventions of [the Rust Guide](../rust.md#pre-commit-and-ci), which says when to read them.

## pre-commit

The shape is the Global Guide's *Checks and CI*; the Rust specifics are:

- **pre-commit is a uv tool**, pinned to the version CI uses: `uv tool install pre-commit==X.Y.Z`, then `pre-commit install` once per clone. A Rust repo has no `pyproject.toml`, so this is the one Python tool it needs.
- actionlint and shellcheck come from their PyPI-backed hook repos (`Mateusz-Grzelinski/actionlint-py`, `shellcheck-py/shellcheck-py`), pinned by `rev`. The actionlint hook also lists `shellcheck-py==<version>` in its `additional_dependencies`: it is a Python hook, so that installs shellcheck into its own environment, on actionlint's PATH (Global Guide, *Checks and CI*).
- Local hooks, `language: system`, `pass_filenames: false`, `files: (\.rs|Cargo\.toml|Cargo\.lock|rust-toolchain\.toml)$`: `cargo fmt --all --check`, `cargo clippy --workspace --all-targets --all-features -- -D warnings`, `cargo test --workspace`. They run with the pinned toolchain.

## CI (GitHub Actions)

- The `pre-commit` job: `rustup toolchain install` (reads the pin), `Swatinem/rust-cache`, `astral-sh/setup-uv` with `version` set to the uv release in use, `actions/cache` on `~/.cache/pre-commit` keyed on the hash of `.pre-commit-config.yaml`, then `uvx pre-commit@X.Y.Z run --all-files --show-diff-on-failure`.
- The `push` to `main` paths are `Cargo.lock` and `rust-toolchain.toml`, which keep the cargo cache warm.
