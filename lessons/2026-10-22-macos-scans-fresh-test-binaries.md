---
address: Rust (missing Guide)
origin: samthorold/explorers@88fe3d9 (docs/agents/known-traps.md)
signal: trap
---

On macOS, `syspolicyd` (Gatekeeper/XProtect) scans every newly linked executable on its first launch. `cargo test` relinks its test binaries on every rebuild, so each test run after an edit pays the scan, which can dwarf the tests themselves (measured: tens of seconds to minutes against ~15 s of testing). The tell is a binary reporting `finished in 0.07s` after a long wall-clock wait, with `syspolicyd` high in `ps -Ao pcpu,comm -r`. Fix: add the terminal app under System Settings → Privacy & Security → Developer Tools, then restart the terminal and any agent session in it. Would hit any Rust project developed on macOS, and any Stack that links many fresh binaries; the fix itself may belong in the dotfiles machine setup rather than a Guide.
