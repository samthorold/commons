---
address: discrete event simulation (missing Guide), or a wider simulation Archetype
origin: samthorold/explorers@367666b (docs/agents/delivery-workflow.md)
signal: gap
---

In a simulation whose behaviour is pinned by golden fixtures and seeded runs, a new rule of the model lands behind a world parameter whose default reproduces the old behaviour, so its PR leaves every world and fixture byte-identical and is reviewable as pure addition; the rule is switched on where it is read. Making it the default is a separate, deliberate PR that flips the default, updates the fixtures with the change explained, and removes the old path, so code and design docs describe one model again. When to flip is decided per rule, by readiness, not by policy. Likely to hold for any seeded, fixture-pinned simulation (tick-based or discrete event), which also raises whether the missing Archetype is "discrete event simulation" or something broader.
