# Emergent systems Guide

**Scope:** Archetype = emergent systems, any Stack. A system is emergent when **the system-level behaviour that matters can't be derived from the actors' rules, only observed by running them**: agent-based models, ecologies, market models, simulations, and the play and training of game-playing agents. Exact code inside such a system (a search function a test can derive) is ordinary code; the Guide applies to the behaviour that emerges from it.

How hypotheses about the end state are declared and read is the Project knowledge Guide's end-state Stance; this Guide says what is particular to systems whose hypotheses are about emergent behaviour.

## Stance: the model never contains its phenomena

- **Stance:** no part of the model produces a phenomenon it is meant to show: no designer-set response curve, amplitude, phase variable or fixed weight stands in for behaviour that should emerge. If a phenomenon doesn't emerge, the cause is looked for in the actors' rules and the substrate, not fixed by adding a mechanism that produces it.
- **Why:** a phenomenon produced by its own mechanism agrees with its parameters by construction, so it can't falsify anything, and the model stops being an instrument for studying it. It also hides the rule that was actually wrong.
- **How to apply:**
  - A new mechanism is checked by asking which phenomenon's outcome it sets directly. One that sets it is the phenomenon built in, whatever it's called.
  - A test scenario built so that its outcome is guaranteed checks the wiring, not emergence. Design the starting state and the trigger, and let the rules decide what follows; only that counts as a reading.
  - Where the domain itself fixes a behaviour (a regulation, a game's rules), it is a rule of the substrate, not a phenomenon, and encoding it is right.
- **What would change our mind:** a phenomenon that is outside what the model is for, needed only as a backdrop for the ones it studies, where encoding it is the cheaper honest choice, stated as such in the design.

## Stance: the substrate is a part of the end state

- **Stance:** the substrate the behaviour emerges from (the physics, the loss engine, the ecology, the game engine) is a part of the end state with hypotheses of its own, and they must hold before any emergent finding counts. Some are exact (a claim never exceeds its sum insured); many can only be stated as a direction (an aggregate's spread falls as the pool grows; a population recovers after a shock).
- **Why:** an emergent finding inherits every error in what it emerges from, and no reading of the finding can tell. A wrong substrate produces artefacts that look like phenomena.
- **How to apply:**
  - Exact substrate hypotheses run on every change (the fast test lane). Directional ones take a directional reading rule: most of the panel agrees on the sign and the mean's interval excludes zero; refuted when the interval lies below the panel's measured sensitivity (a null run with identical arms, and a planted effect of known size).
  - A change to the substrate makes every hypothesis Due.
  - A phenomenon hypothesis names the setup it's read in: the reference setup, or a controlled variant that changes one thing with all else the same, to isolate an effect. Requiring every phenomenon to appear in one reference setup is the wrong test.
- **What would change our mind:** a substrate so simple that its behaviour is derivable, where the exact tests are enough.

## Lessons

If something in this Guide proves wrong or incomplete while you work, or you hit something another emergent system would also hit, record a Lesson addressed to it, as described in `~/.claude/commons/lessons/README.md`.
