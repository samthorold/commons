---
address: guides/rust.md#testing
origin: samthorold/explorers#925
signal: trap
---

`cargo test --workspace` stops after the first test binary that fails, so the binaries of later crates never run and their failures stay hidden until the first is fixed. An agent fixing failures one run at a time then takes several full runs to see them all. Add `--no-fail-fast` to the full run when diagnosing, so one run reports every failing test in the workspace.
