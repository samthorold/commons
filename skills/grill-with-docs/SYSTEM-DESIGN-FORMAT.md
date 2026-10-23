# System Design Format

System-design docs live in the project's design home — `docs/` or `docs/system-design/`. They are the bridge between the domain (the true facts and rules) and the implementation (the code). This is where the design *and the reasons for it* live.

There is no separate decision-record layer. The rationale a decision record would have held belongs here, written in the present tense.

## What this layer is

Our opinion about how to model the domain: which of its rules we carry forward, which we simplify, which mechanisms are load-bearing, and the shape the system takes to realise them — concepts, relationships, constraints, and functional forms. Implementation-agnostic.

It is built on the domain layer (it must faithfully represent the ground truth) and it informs the implementation (the code encodes it). It references the domain as foundation and does not restate it; it does not reach down to prescribe data structures or algorithms.

## Write it self-justifying, in the present tense

A system-design doc must answer "why is it this way?" on its own, so that no chronology of past decisions is ever needed to understand the present. For each load-bearing piece of the design:

1. **State the mechanism as it stands today** — the functional form, the rule, what a concept *is*. Present tense.
2. **Explain why it has this shape** — the domain fact, constraint, or emergent property that forces it. Ground it in the domain layer where relevant.
3. **Pre-empt the obvious alternative** — where a reader would reasonably expect a simpler or different approach, explain why that approach fails. State this as a standing property of the design ("a single shared counter would serialise every request, so…"), not as a dated rejection ("in v2 we tried X and reverted").

The test: a newcomer reading only this doc understands both what the design is and why it must be that way — including why the tempting shortcut doesn't work — without asking "but why didn't they just…?"

## Describe the destination, not the journey

- **No chronology.** Don't record how the design evolved, which mechanism superseded which, or what the previous iteration was. Describe the current design as if it had always been this way.
- **No "considered options" log.** The reasoning for the chosen design (including why alternatives fail) belongs woven into the prose as present-tense justification — not as a separate list of rejected candidates with verdicts.
- **No decision metadata.** No status fields, dates, supersession links, or "we decided" framing. The doc is a description of the system, not a record of a meeting. A hypothesis's status is in the register, never here.

When the design changes, change the doc to describe the new present and delete the obsolete description. Version control holds the history; the doc holds the truth as it stands.

## Keep the layers clean

- **Domain facts** (how the real-world problem behaves, independent of our system) belong in the domain layer, not here. Reference them; don't restate them.
- **Implementation details** (data structures, algorithms, concrete parameter values, file layout) belong in the code, not here. A system-design doc names a functional form and why it has that shape; it does not pin the constant or choose the container.
- **Language** (what a term means) belongs in `CONTEXT.md`. Use the canonical terms here; don't redefine them.

## The end state and its hypotheses

The Project knowledge Guide's Stance *the system design states its end state as hypotheses* says what this section is for; the terms are in the Commons' `CONTEXT.md` (*End states and hypotheses*). Its shape:

- **The end state as a tree of parts**, from the system's purpose at the top down to the mechanisms that realise each part. Where the design already maps phenomena or features to mechanisms (a coverage map), that map is the tree.
- **Under each part, its hypotheses**, in the present tense. Where the domain is sourced, each is a domain phenomenon the model should reproduce.
- **Beside each hypothesis, its reading rule**: the test that reads it, the panel or size (or stopping rule), what counts as supported, refuted and undecided, and how the instrument's error is treated. Where the domain gives an empirical range, the rule cites it rather than restating the number. Plus the review interval, and which mechanisms make it Due when they change.
- **Nothing about status.** No "holds", "failed", "the null", last readings or dates: those are the register's.

A refuted hypothesis changes this section, in the same change that records the reading in the register. A declared value that changes on its own is Drift.

## A note on parameter values

Specific numeric values that calibrate the mechanisms are an implementation concern — they live with the code (and any parameter-search tooling), not in the system-design layer. The design layer describes the *form* of a cost or flow and why it has that form; the values that make it concrete are found and tuned downstream.

A reading rule's declared values (its range, panel size, threshold, review interval) are not calibration: they say what would count as the end state being reached or missed, so they are design, and they live with the rule.
