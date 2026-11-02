# Rust Guide

**Scope:** Stack = Rust, any Archetype. For a Rust extension inside a Python project (the Python+Rust cell), the Python Guide's *Rust extensions* section adds what that cell needs on top of this Guide.

The default setup for every Rust project. When starting or touching a Rust repo, bring it in line with this, and record the project's own specifics (commands, check names, slow tests, traps) in that repo's `CLAUDE.md`. Reference implementation for the toolchain and hooks: `~/Projects/py-minimax-games` (`rust-toolchain.toml`, `.pre-commit-config.yaml`, `.github/workflows/ci.yml`). Changes to this Guide are Revisions of the Commons: see the commons `README.md`.

Conventions used for one job live in files under `~/.claude/commons/guides/rust/`, and each section says when to read its file. Links are relative to this file.

## Tooling

Decides the edition, the exactly pinned toolchain, the committed `Cargo.lock`, when to become a workspace, rustfmt and clippy at their defaults with warnings failing, and optimised test builds.
Before setting up a Rust repo, or changing its toolchain, `Cargo.toml` profiles, crate layout or lint settings, read [tooling](rust/tooling.md).

## Testing

How Rust Adopters carry out the Agentic development Guide's test-first Stance (the `/tdd` Skill is the Procedure).

- **Integration tests live in one test binary**, `tests/<name>/main.rs` with each suite as a module, not one file per suite directly under `tests/`. *Why:* every top-level file in `tests/` is a separate binary that links the crate again, which on an optimised crate makes linking most of the build.
- **proptest's failure persistence is pinned.** Its default walks up from a test file to the nearest directory holding a `lib.rs` or `main.rs`, so moving suites under a `main.rs` silently changes where seeds are read and written, and the committed regression seeds stop replaying. Every `proptest!` block takes its config from one shared helper that sets `FileFailurePersistence::WithSource("proptest-regressions")`; a stray `tests/proptest-regressions/` directory means a block bypassed it. Regression files are committed.
- **Slow tests carry a `slow_` name prefix**, rather than `#[ignore]` or a feature flag, so they stay in the full run and the inner loop skips them with `cargo test -p <crate> -- --skip slow_`. Run the whole workspace before committing.
- **Randomness is a parameter**: code takes `&mut impl Rng` (or a seed) rather than calling `rand::rng()`. Seeded streams that must reproduce use a named algorithm (`rand_chacha::ChaCha8Rng`), never `StdRng`. *Why:* rand documents `StdRng` as non-portable, so any rand release may change its stream ([rand book, *Reproducibility*](https://rust-random.github.io/book/crate-reprod.html)).
- **Output that must reproduce never depends on `HashMap` or `HashSet` order.** std seeds their hasher per process, so iterating one visits entries in a different order each run, and a float sum or a file built that way differs in the last bits. Use a `BTreeMap`, sort before iterating, or a fixed hasher (`rustc-hash`).

## pre-commit and CI

Decides how a Rust repo gets pre-commit (a pinned uv tool), its cargo hooks, and the steps and caches of the `pre-commit` CI job.
On a fresh clone, or before setting up or changing a repo's hooks or CI workflow, read [pre-commit and CI](rust/checks.md).

## Releases

No Rust Adopter publishes yet, so there is no release Convention. The first one to publish settles it, starting from the Python Guide's (a version-bump PR that tags and releases when merged).

## Lessons

If something in this Guide proves wrong or incomplete while you work (a Contradiction, a Deviation, a Gap or a Trap that another Rust project would also hit), record a Lesson addressed to this Guide (to the section's detail file, where the Lesson is about one job), as described in `~/.claude/commons/lessons/README.md`. Trouble specific to one project stays in that project's own docs.
