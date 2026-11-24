---
address: guides/project-knowledge/three-layers.md
origin: samthorold/explorers#872
signal: gap
---

When a glossary entry says a parameter is "searched" (part of a parameter search's box), it is unclear which layer holds that fact. The box is defined in code, so membership is a code fact whose home is the code; but a parameter left out of the box on purpose, with a reason, is a design fact. Cleaning a `CONTEXT.md` down to definitions, one Adopter kept inclusion in the code only and moved each exclusion-with-reason into the design, and found a design doc still claiming a parameter was searched that the code doesn't search, the drift this split would prevent. Any Adopter with a parameter search (genesis, calibration, tuning) faces the same choice; the three-layers file could state the split.
