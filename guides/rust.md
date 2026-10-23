# Rust Guide

**Scope:** Stack = Rust, any Archetype. For a Rust extension inside a Python project (the Python+Rust cell), the Python Guide's *Rust extensions* section adds what that cell needs on top of this Guide.

The default setup for every Rust project. When starting or touching a Rust repo, bring it in line with this, and record the project's own specifics (commands, check names, slow tests, traps) in that repo's `CLAUDE.md`. Reference implementation for the toolchain and hooks: `~/Projects/py-minimax-games` (`rust-toolchain.toml`, `.pre-commit-config.yaml`, `.github/workflows/ci.yml`). Changes to this Guide are Revisions of the Commons: see the commons `README.md`.

## Tooling

- **Edition 2024, resolver 3.**
- **The toolchain is pinned exactly** in `rust-toolchain.toml` at the repo root: `channel = "X.Y.Z"`, `profile = "minimal"`, `components = ["clippy", "rustfmt"]`. rustup installs it on first use, locally and in CI. Upgrade it deliberately in its own PR, fixing whatever new clippy lints it brings. *Why:* stable moves every six weeks and each release adds clippy lints, so an unpinned toolchain fails `-D warnings` on a PR that changed nothing about it.
- **`Cargo.lock` is committed**, libraries included, so local runs, hooks and CI build the same dependency versions.
- **One crate until there's a second.** Then a virtual workspace (no root package) with members under `crates/`, and dependency versions shared through `[workspace.dependencies]`.
- **rustfmt and clippy at their defaults**: no `rustfmt.toml`, clippy's default lint set, and warnings fail (`-D warnings`). Adopting this in a repo that has never enforced clippy is one cleanup PR; after it, warnings can't accumulate.
- **cargo is the task runner.** A Taskfile (Python Guide, *Tooling*) only when the project has commands beyond cargo's.
- **Compute-heavy tests build optimised.** Where tests run the code for long (simulations, search), set `[profile.dev.package."*"] opt-level = 3` (dependencies compile once and rarely change), and raise `opt-level` on the hot crate only, so the other crates keep fast debug builds.

## Testing

How Rust Adopters carry out the Agentic development Guide's test-first Stance (the `/tdd` Skill is the Procedure).

- **Integration tests live in one test binary**, `tests/<name>/main.rs` with each suite as a module, not one file per suite directly under `tests/`. *Why:* every top-level file in `tests/` is a separate binary that links the crate again, which on an optimised crate makes linking most of the build.
- **proptest's failure persistence is pinned.** Its default walks up from a test file to the nearest directory holding a `lib.rs` or `main.rs`, so moving suites under a `main.rs` silently changes where seeds are read and written, and the committed regression seeds stop replaying. Every `proptest!` block takes its config from one shared helper that sets `FileFailurePersistence::WithSource("proptest-regressions")`; a stray `tests/proptest-regressions/` directory means a block bypassed it. Regression files are committed.
- **Slow tests carry a `slow_` name prefix**, rather than `#[ignore]` or a feature flag, so they stay in the full run and the inner loop skips them with `cargo test -p <crate> -- --skip slow_`. Run the whole workspace before committing.
- **Randomness is a parameter**: code takes `&mut impl Rng` (or a seed) rather than calling `rand::rng()`. Seeded streams that must reproduce use a named algorithm (`rand_chacha::ChaCha8Rng`), never `StdRng`. *Why:* rand documents `StdRng` as non-portable, so any rand release may change its stream ([rand book, *Reproducibility*](https://rust-random.github.io/book/crate-reprod.html)).
- **Output that must reproduce never depends on `HashMap` or `HashSet` order.** std seeds their hasher per process, so iterating one visits entries in a different order each run, and a float sum or a file built that way differs in the last bits. Use a `BTreeMap`, sort before iterating, or a fixed hasher (`rustc-hash`).

## pre-commit

The shape is the Global Guide's *Checks and CI*; the Rust specifics are:

- **pre-commit is a uv tool**, pinned to the version CI uses: `uv tool install pre-commit==X.Y.Z`, then `pre-commit install` once per clone. A Rust repo has no `pyproject.toml`, so this is the one Python tool it needs.
- actionlint and shellcheck come from their PyPI-backed hook repos (`Mateusz-Grzelinski/actionlint-py`, `shellcheck-py/shellcheck-py`), pinned by `rev`.
- Local hooks, `language: system`, `pass_filenames: false`, `files: (\.rs|Cargo\.toml|Cargo\.lock|rust-toolchain\.toml)$`: `cargo fmt --all --check`, `cargo clippy --workspace --all-targets --all-features -- -D warnings`, `cargo test --workspace`. They run with the pinned toolchain.

## CI (GitHub Actions)

- The `pre-commit` job: `rustup toolchain install` (reads the pin), `Swatinem/rust-cache`, `astral-sh/setup-uv` with `version` set to the uv release in use, `actions/cache` on `~/.cache/pre-commit` keyed on the hash of `.pre-commit-config.yaml`, then `uvx pre-commit@X.Y.Z run --all-files --show-diff-on-failure`.
- The `push` to `main` paths are `Cargo.lock` and `rust-toolchain.toml`, which keep the cargo cache warm.

## Releases

No Rust Adopter publishes yet, so there is no release Convention. The first one to publish settles it, starting from the Python Guide's (a version-bump PR that tags and releases when merged).

## Lessons

If something in this Guide proves wrong or incomplete while you work (a Contradiction, a Deviation, a Gap or a Trap that another Rust project would also hit), record a Lesson addressed to this Guide, as described in `~/.claude/commons/lessons/README.md`. Trouble specific to one project stays in that project's own docs.
