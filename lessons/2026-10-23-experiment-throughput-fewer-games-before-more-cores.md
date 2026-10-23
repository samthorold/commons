---
address: guides/simulation.md (missing; see MAP's Known Gaps)
origin: samthorold/py-minimax-games#219, #220, #221
signal: gap
---

In a project whose experiments are many seeded runs (games, simulations), measurements get repeated as a matter of routine: each hypothesis is re-read on every new champion or model, and a reading too close to call is read again with more runs. Wall time then becomes the limit, and the obvious answer, renting more compute, comes too early. In one such project, nearly all of an instrument's time went into playing the runs, not into measuring them (a probe took 104 s, all but 0.1 s of it playing games). The levers, in the order they paid:

1. **Fewer runs per decision.** A fixed-size match comes out undecided whenever the true effect is near the line, and then it's replayed. A sequential test (SPRT, checked after each batch, with a cap read as declared) keeps going until it decides, and usually needs far fewer runs. One decided after 200 of a possible 1,200. Pooling an undecided fixed-size reading with a new one isn't a substitute: adding runs until the result crosses the line is optional stopping.
2. **Run once, measure many times.** With deterministic seeds, a recording keyed by (model, seed range, settings) stays valid until the model changes. Several instruments were each playing their own copy of the same runs, sometimes on the very same seeds.
3. **Use the machine's cores when it's free.** Runs throttled for a machine shared with other agents stay throttled after the machine is free.
4. **Measure only what's due.** Give settled hypotheses a longer review interval, rather than re-running every instrument each time.
5. **Only then, more machines.** Work that splits by seed shards cleanly across CI runners (free for public repos) or rented many-core CPUs. GPU services don't help CPU-bound search or simulation.

Before relying on another platform, check determinism. Floating-point maths library functions (e.g. `tanh`) can differ in the last bit between operating systems or architectures. In a search, that flips a near-tie and the run diverges. A cloud reading is still a valid reading, but it can't be paired seed by seed with runs recorded elsewhere until a replay of a recorded run matches exactly.
