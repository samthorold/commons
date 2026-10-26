---
address: guides/model-calls.md#stance-change-an-act-on-its-cheapest-stage-then-record-the-chain-once
origin: samthorold/go-slow#92
signal: contradiction
---

The Stance splits "re-record once the instructions settle" into a slice that changes the act and shows its new behaviour *for the owner to accept*, and a slice that records the chain. Read literally, every slice that changes an act is held until the owner accepts it. In an epic of several such slices in sequence, each hold stops the run until the owner is back, and the next slice can't start. That contradicts the Agentic development Guide's *decide, record, carry on*: an agent makes reversible calls itself, and a slice whose successors are cheap to redo is reversible.

The case: an epic of four slices, three changing one act each (re-recorded on a cheap model, a few dollars each) and a fourth refreshing every act's frozen inputs and re-recording the chain. The first slice had declared, before recording, a mechanical refutation (the act's run-to-run agreement must beat the upstream act's on the same fixtures), plus qualitative review cases only the owner could judge. All three were held on the owner's acceptance anyway.

What would hold: the owner's acceptance gates the first step where being wrong gets expensive (the chain refresh, a run on an expensive model, a release), not every slice. A slice that changes an act merges on its declared criterion (a refutation declared before recording, every property supported), read by the agent. Its review cases and yield shift go in the PR body for the owner, reviewed without blocking. Holding a slice is justified only when its acceptance has no declared criterion, and then the fix is to declare one when the slice is written, during the grill. The caveat: if a later slice's *design*, not just its recordings, depends on the owner's verdict on an earlier one, that later slice waits.
