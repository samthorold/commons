---
address: guides/project-knowledge.md#stance-the-system-design-states-its-end-state-as-hypotheses
origin: samthorold/go-slow#46
signal: gap
---

The Guide says a hypothesis is Due when its review interval has passed or "what it was read on has changed", and that the register is derived, not written. A register derived afresh on every view has no memory of when it last read a hypothesis, so the interval needs fixed review points (here, back-to-back windows from the first day of use), and "changed" has to be detected from outside the running system: the app can't see a change to its own code. Here commit history is fed in by an admin command, and commits touching the Editor's paths mark it changed; a change made only through configuration (switching a model) stays invisible. The Guide could say how a derived register learns of changes.

Relatedly, a reading rule like "refuted by any missed day", read over the whole history, refutes permanently after one outage. Rules should say over what window they read.
