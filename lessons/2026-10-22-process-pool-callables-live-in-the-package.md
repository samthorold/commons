---
address: guides/python.md#testing
origin: samthorold/py-minimax-games#195
signal: gap
---

A test that passes a callable to code running it in a process pool (`multiprocessing`, `ProcessPoolExecutor`, a `jobs=N` option) must use a callable defined in the package, not one defined in the test module: under the default `spawn` start method (macOS, Windows) the workers re-import the callable by module path, and `tests` isn't importable from them, so they fail with `ModuleNotFoundError: tests`. The Testing section's advice to pass in a small fake by injection meets this whenever the code under test parallelises. Options: pick a real callable from the package (a registered bot, a named function), keep pool-crossing fakes in a small importable helper in the package, or test that path with `jobs=1` and cover parallel = serial with a package callable.
