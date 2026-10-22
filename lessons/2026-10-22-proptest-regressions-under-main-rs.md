---
address: Rust (missing Guide)
origin: samthorold/explorers@88fe3d9 (docs/agents/known-traps.md; the move in explorers PR for issue 784)
signal: trap
---

proptest's default failure persistence (`SourceParallel`) walks up from a test's source file to the nearest directory holding a `lib.rs` or `main.rs` and stores failures in a sibling `proptest-regressions/<path>.txt`, falling back to `<file>.proptest-regressions` beside the source only when it finds none. Consolidating integration tests into one binary (`tests/<name>/main.rs`, a common move to cut link time) therefore silently changes where seeds are read and written, and the committed regression seeds stop replaying. Fix: pin the persistence explicitly (e.g. a shared config helper using `FileFailurePersistence::WithSource("proptest-regressions")`) for every `proptest!` block; a stray `tests/proptest-regressions/` directory means a block bypassed it.
