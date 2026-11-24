---
address: guides/rust.md
origin: samthorold/explorers#902
signal: gap
---

The Rust Guide's *Testing* says output that must reproduce never depends on `HashMap`/`HashSet` order, and offers a fixed hasher (`rustc-hash`) as one remedy. It does not say how to keep it that way. The recipe that worked:

- A root `clippy.toml` bans `std::collections::HashMap` and `HashSet` through `disallowed_types`, with a reason citing the Guide.
- Lookup-only containers become `rustc_hash::FxHashMap`/`FxHashSet`.
- Containers whose iteration reaches output become `BTreeMap`/`BTreeSet`.

`FxHashMap` is still the std `HashMap` type with another hasher. It passes the ban only because clippy resolves the alias rather than the std path: written out as `HashMap<K, V, FxBuildHasher>`, the same type is flagged.

A fixed hasher's order is the same from run to run, but it depends on insertion history, so a new loop over an Fx container that reaches output is reproducible but arbitrary, and the ban doesn't see it. `clippy::iter_over_hash_type` (a restriction lint, which catches `for` loops over Fx containers too) with per-use allows would close that. It doesn't see iterator adapters.

The Guide could state the ban, the alias behaviour and the loop lint together.
