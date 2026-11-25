---
address: guides/project-knowledge/end-state.md
origin: samthorold/py-minimax-games@4d953a4:docs/star-realms.md
signal: gap
---

A test whose instrument is a search for a counterexample can read *supported* but never *refuted*. Examples are an exploiter trained to beat a frozen player, a fuzzer or an adversarial search. A reading rule for such a test is one-sided: *supported* if the search finds one, *undecided* otherwise. Failing to find one is bounded by the searcher's strength, not by the system's, so a stronger searcher could still succeed. The rule should state its searcher's size and budget, and say what a null reading does mean ("not found by a searcher of this form and size").

The Guide already covers the mirror case: cheap necessary conditions that "can refute but not confirm", and instruments whose error runs one way. It doesn't say that a search instrument runs the other way. Without that, a rule writer is pushed to declare a refutation threshold ("no exploiter wins in N rounds"), which reads a weak learner as evidence about the system. The sources for the exploiter case are Timbers et al. 2022 (approximate exploitability is a lower bound) and Wang et al. 2023.
