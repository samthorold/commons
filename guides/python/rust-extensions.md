# Python Guide: Rust extensions

The *Rust extensions* Conventions of [the Python Guide](../python.md#rust-extensions), which says when to read them. The Rust Guide's parts they build on are in [its tooling](../rust/tooling.md) and [its pre-commit and CI](../rust/checks.md).

When part of a project needs compiled speed, it becomes a Rust extension in the same repo, with Python orchestrating. Reference implementation: `~/Projects/py-minimax-games` (`rust/`, `minimax_games._native`). Copy from it. The crate follows the Rust Guide; this section adds only what the Python+Rust cell needs.

- **One crate, `rust/`, in maturin's mixed layout**: `[tool.maturin]` with `manifest-path = "rust/Cargo.toml"`, `module-name = "<pkg>._native"`, `python-source = "src"`. The Python package stays at `src/<pkg>/`. Make it a Cargo workspace only when a second engine arrives.
- **maturin replaces `uv_build`** (`requires = ["maturin>=X.Y,<X.(Y+1)"]`). PyO3 behind a `python` cargo feature (enabled by `[tool.maturin] features`), so plain `cargo test` needs no Python. Build for the stable ABI from the minimum Python (`abi3-py3XX`), so one wheel per platform serves every version.
- **`[tool.uv] cache-keys`** must list `pyproject.toml`, `rust/Cargo.toml`, `rust/Cargo.lock` and `rust/src/**/*.rs`, or `uv run` keeps a stale extension after Rust changes.
- **The Rust Guide's `rust-toolchain.toml` sits at the repo root**, not in `rust/`: rustup finds it from the working directory, and cargo, maturin and the hooks run from the root. Include it in the sdist (`[tool.maturin] include`).
- **Type stubs** for the extension in `src/<pkg>/_native/*.pyi`, with no `__init__.py`, so the compiled module wins at import time.
- **pre-commit**: the Rust Guide's cargo hooks with `--manifest-path rust/Cargo.toml` and `files: ^(rust/|rust-toolchain\.toml$)`, clippy run through `uv run --locked` so PyO3's build script finds the venv's Python. pytest also runs on Rust and TOML changes.
- **CI**: the Rust Guide's toolchain and cache steps (`workspaces: rust`) before `uv sync --locked`, and its `push` paths under `rust/`.
- **Releases**: `release.yml` runs `uv build` on the platform that needs a wheel (e.g. `macos-15` for Apple silicon), giving the sdist plus that wheel; the dry run builds on every PR.
- **The Python implementation stays the reference**: differential tests compare the Rust and Python results after every step on seeded inputs, and bit-identical randomness (port CPython's MT19937 and the `random` methods used) makes them exact.
