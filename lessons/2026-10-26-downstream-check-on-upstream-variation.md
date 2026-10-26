---
address: guides/model-calls.md#stance-change-an-act-on-its-cheapest-stage-then-record-the-chain-once
origin: samthorold/go-slow#94
signal: gap
---

When acts feed each other, a downstream act's check can enforce a standard that only the upstream act is told about. Every sample-to-sample variation of the upstream act's output then shows up as a downstream refusal, and is read as the downstream act failing.

The case: an extraction act lists the entities each statement involves; a later act gives each listed entity its role. The later act refused its whole result when it gave a role to an entity the extraction had named elsewhere in the same input but not listed for that statement. The extraction's lists varied a lot between samples (one statement's list went from 1 to 22 entities across samples of the same instructions), so the later act was refuted on a fixture where its judgement was right.

The fix was to let the act whose job is the judgement settle it: the later act keeps a role for any entity the extraction gave anywhere in the input, and that records the involvement. It still refuses a name the extraction never gave. The change was in code alone, so no recording was redone.

Candidate rule: for each check, ask which act owns the standard it enforces. A check that re-judges what an upstream act decided is either the upstream act's own check or a hint that the downstream act should own the decision.

Related: when rewording the upstream act's instructions keeps moving one count and disturbing another, the task itself may need splitting or a different approach, which is research rather than more wording.
