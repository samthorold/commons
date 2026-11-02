# Rust Guide: tooling

The *Tooling* Conventions of [the Rust Guide](../rust.md#tooling), which says when to read them.

- **Edition 2024, resolver 3.**
- **The toolchain is pinned exactly** in `rust-toolchain.toml` at the repo root: `channel = "X.Y.Z"`, `profile = "minimal"`, `components = ["clippy", "rustfmt"]`. rustup installs it on first use, locally and in CI. Upgrade it deliberately in its own PR, fixing whatever new clippy lints it brings. *Why:* stable moves every six weeks and each release adds clippy lints, so an unpinned toolchain fails `-D warnings` on a PR that changed nothing about it.
- **`Cargo.lock` is committed**, libraries included, so local runs, hooks and CI build the same dependency versions.
- **One crate until there's a second.** Then a virtual workspace (no root package) with members under `crates/`, and dependency versions shared through `[workspace.dependencies]`.
- **rustfmt and clippy at their defaults**: no `rustfmt.toml`, clippy's default lint set, and warnings fail (`-D warnings`). Adopting this in a repo that has never enforced clippy is one cleanup PR; after it, warnings can't accumulate.
- **cargo is the task runner.** A Taskfile (Python Guide, *Tooling*) only when the project has commands beyond cargo's.
- **Compute-heavy tests build optimised.** Where tests run the code for long (simulations, search), set `[profile.dev.package."*"] opt-level = 3` (dependencies compile once and rarely change), and raise `opt-level` on the hot crate only, so the other crates keep fast debug builds.
