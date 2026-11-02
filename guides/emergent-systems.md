# Emergent systems Guide

**Scope:** Archetype = emergent systems, any Stack. A system is emergent when **the system-level behaviour that matters can't be derived from the actors' rules, only observed by running them**: agent-based models, ecologies, market models, simulations, and the play and training of game-playing agents. Exact code inside such a system (a search function a test can derive) is ordinary code; the Guide applies to the behaviour that emerges from it.

How hypotheses about the end state are declared and read is the Project knowledge Guide's end-state Stance; this Guide says what is particular to systems whose hypotheses are about emergent behaviour.

Each Stance's *How to apply* and the full text of its Why live in their own files under `~/.claude/commons/guides/emergent-systems/`, and this Guide says when to read each. Links are relative to this file.

## Stance: the model never contains its phenomena

- **Stance:** no part of the model produces a phenomenon it is meant to show: no designer-set response curve, amplitude, phase variable or fixed weight stands in for behaviour that should emerge. If a phenomenon doesn't emerge, the cause is looked for in the actors' rules and the substrate, not fixed by adding a mechanism that produces it.
- **Why:** a phenomenon produced by its own mechanism agrees with its parameters by construction, so it can't falsify anything.
- **How to apply:** before adding a mechanism to the model, designing a test scenario, or encoding a behaviour the domain fixes, read [the model never contains its phenomena](emergent-systems/model-never-contains-its-phenomena.md).
- **What would change our mind:** a phenomenon that is outside what the model is for, needed only as a backdrop for the ones it studies, where encoding it is the cheaper honest choice, stated as such in the design.

## Stance: the substrate is a part of the end state

- **Stance:** the substrate the behaviour emerges from (the physics, the loss engine, the ecology, the game engine) is a part of the end state with hypotheses of its own, and they must hold before any emergent finding counts. Some are exact (a claim never exceeds its sum insured); many can only be stated as a direction (an aggregate's spread falls as the pool grows; a population recovers after a shock).
- **Why:** an emergent finding inherits every error in what it emerges from, and no reading of the finding can tell.
- **How to apply:** before stating or reading a hypothesis about the substrate or a phenomenon, or changing the substrate, read [the substrate is a part of the end state](emergent-systems/substrate-is-part-of-the-end-state.md).
- **What would change our mind:** a substrate so simple that its behaviour is derivable, where the exact tests are enough.

## Lessons

If something in this Guide proves wrong or incomplete while you work, or you hit something another emergent system would also hit, record a Lesson addressed to it (to the detail file, where the Lesson is about how to apply a Stance), as described in `~/.claude/commons/lessons/README.md`.
