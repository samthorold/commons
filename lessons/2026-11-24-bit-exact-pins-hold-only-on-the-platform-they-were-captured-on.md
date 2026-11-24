---
address: guides/rust/checks.md#ci-github-actions
origin: samthorold/explorers#849
signal: contradiction
---

Golden tests that pin exact `f32`/`f64` bits (digests of a simulation's trajectory, recorded readings) hold only on the platform they were captured on, whenever the code calls transcendental functions. Rust's `exp`, `ln`, `powf` and the trigonometric functions call the platform's libm, and Apple's libm and glibc's differ in the last bits. So a suite pinned on a developer's Mac fails on CI's Ubuntu runner: in one simulation project, seed 3 of a pinned recipe read different bits for every score. The pre-commit and CI Convention doesn't name a runner, and its reference implementation uses `ubuntu-latest`, so it leaves a Mac-pinned suite failing in CI with no change to the code. There are two fixes. One is to run CI on the platform where the pins are captured (`macos-15`, which is Apple silicon and free on public repos), and record that in `CLAUDE.md` along with "re-pin on Apple silicon". The other is to compute through a portable implementation (the `libm` crate), so the bits are the same everywhere. That second fix changes every pinned value at once, so it's a design change, not a CI fix. A related trap on the same runner: a GUI crate built with eframe's default features off has no Linux display backend, and winit fails to compile there.
