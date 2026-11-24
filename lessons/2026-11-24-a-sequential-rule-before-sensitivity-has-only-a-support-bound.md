---
address: guides/project-knowledge/end-state.md
origin: samthorold/explorers#883
signal: contradiction
---

The Guide's sequential rule "keeps going until it crosses a declared bound" assumes two bounds, one either way. But a directional rule whose panel sensitivity isn't measured yet may not refute (a failure may only mean the panel couldn't see the effect). So a "k of n seeds, stop once decided" rule declared before sensitivity is measured has only a support bound: reaching the failure count stops the sequence as *undecided*, not refuted. The instrument that runs the sequence then needs a failure bound whose meaning is declared by the rule (refuted or undecided), not hard-coded. The Guide could say that a sequential rule read before sensitivity is measured has only a support bound, and that measuring sensitivity is what earns it a refutation bound.
