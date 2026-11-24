---
address: guides/global.md#known-traps
origin: samthorold/explorers@1473eee:docs/agents/known-traps.md
signal: trap
---

On macOS, `syspolicyd` (Gatekeeper/XProtect) scans every newly linked executable the first time it runs. Every rebuild relinks the test binaries, so every test run after an edit pays the scan again: about 85 s for a Rust workspace and 400 s for one crate's tests, against about 15 s of actual testing. The tell is a test binary that reports `finished in 0.07s` after tens of seconds of wall-clock, with `syspolicyd` high in `ps -Ao pcpu,comm -r`. The fix is to add the terminal app to System Settings → Privacy & Security → Developer Tools. It applies only to processes started afterwards, so restart the terminal and any Claude Code session running in it. This holds for any Stack that links fresh test binaries (Rust, Go), not only for the Rust project where it was found.
