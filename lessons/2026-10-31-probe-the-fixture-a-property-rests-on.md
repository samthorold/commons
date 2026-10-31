---
address: guides/model-calls.md#stance-change-an-act-on-its-cheapest-stage-then-record-the-chain-once
origin: samthorold/go-slow PRs #234, #242, #244
signal: gap
---

Before recording a fixture's N samples, probe it with one sample and check that the case its property rests on reaches the act at all. Three times in one run, a single probe of the key fixture (about a cent each) caught what a full recording would have paid to find:

- a candidate scheme built per unit got no candidates for the unit the property named, because the upstream act judged the entity only at its first occurrence;
- a precedent didn't carry to a case that was only similar, so the recorded case had to move to the case the feedback was given on;
- an agent's first submission was empty and refused, so the act's own retry had to cover it.

The Guide says to iterate an act's change "sampled several times and looked at", but not to check first that the fixture's inputs exercise the property. A shared recording harness also needs a way to draw a single sample (a `-max-samples 1` flag), or "probe first" can't be done without hand-editing the sample count.
