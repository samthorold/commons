---
address: guides/model-calls.md#stance-change-an-act-on-its-cheapest-stage-then-record-the-chain-once
origin: samthorold/go-slow#254 (PR #262)
signal: gap
---

The Guide names instructions, schema and model as what cascades from one act into the recordings downstream of it. Plain code cascades too: the code that turns an act's answer into what is kept, and from there into the next act's input. Here a matcher turning words the model quoted into byte offsets was fixed to match whole words only. The upstream act's request and recordings stayed valid, but three quotes in the frozen copies landed elsewhere. That changed the text the downstream acts were shown, and five acts' recordings went stale, one of them on an expensive model.

This extends the shared-vocabulary Lesson (2026-10-26): what crosses frozen copies is anything that renders an upstream answer into a downstream request, code included. The cheap check before any spend is the same: make the change, run the replay suite with no model, and see which acts go stale. Then budget their re-records in the brief, the expensive ones with the owner's say obtained up front.
