---
address: guides/model-calls.md#stance-change-an-act-on-its-cheapest-stage-then-record-the-chain-once
origin: samthorold/go-slow#109
signal: gap
---

Freezing each act's copies of its upstream recordings (see the frozen-inputs Lesson) lets one act be re-recorded without making the others stale, but only while the change stays inside that act's output. A change to vocabulary the acts share (a value kept in the store and rendered into another act's request) crosses the copies. Rewriting the downstream copies to the new value, as the store's migration rewrites kept rows, still changes what the downstream act is shown, and its recordings go stale.

The case: one act's output labelled the part an entity plays in a statement, and a slice renamed one label. The slice re-recorded only that act and rewrote the label in every downstream act's frozen copies. One downstream act was an agent whose tool printed each entity with its label. From its second turn on, its requests carried the new word, so every recording failed as stale. The fix was a re-record of that act, on an expensive model the slice's brief had excluded, which needed the owner's say mid-run.

Candidate rule: a brief that re-records one act lists the other acts whose requests show the vocabulary it changes (instructions, schema descriptions, tool results, rendered input), and budgets their re-records or sequences the slice with the chain's refresh. Finding them is cheap before any spend: change the value, run the replay suite with no model, and see which acts go stale.
