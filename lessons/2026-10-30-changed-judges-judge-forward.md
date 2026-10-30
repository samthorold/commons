---
address: guides/model-calls.md#stance-models-sit-behind-a-port-and-are-chosen-by-measurement
origin: samthorold/go-slow#208
signal: gap
---

An app that keeps a model's judgements as its record has to decide what happens to them when the judge changes (a new model, a new version of the instructions). The Guide covers recordings going stale, but not judgements already in use. Two answers that held up:

- **A changed judge judges forward.** Each judgement carries its judge (act, instructions version, model, request hash). A new judge judges what arrives from then on; earlier judgements stand, with their judge, and a view reads, per thing judged, the newest judge that has judged it. Re-judging the whole record on every change costs as much as the record is large, and that grows daily. Re-judging a range is a deliberate run on the owner's say, priced first like a re-recording. A candidate judge is compared on the live record by re-judging a sample that no view reads until it is chosen.
- **Feedback on judgements ages by kind.** Feedback that says what the owner wants (missed, unwanted) drifts with their taste, so as precedent it weighs less the older it is. Feedback that a judgement is wrong holds at any age, because a judgement is never redone.

A working concept in the Origin, not yet built: promote once an Adopter has run on it.
