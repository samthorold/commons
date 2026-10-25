---
address: guides/model-calls.md#stance-change-an-act-on-its-cheapest-stage-then-record-the-chain-once
origin: samthorold/go-slow#72
signal: gap
---

The Stance assumes chained recordings: a downstream act is replayed over the upstream act's live recordings, so every upstream re-recording makes the whole chain stale at once. Another shape decouples them. Each act is recorded over its own frozen copies of the upstream recordings. Copies are used rather than hand-made fixtures, because copies were made by the production path and hand-made input would let a downstream act pass on what no upstream act writes.

With frozen copies, recording the chain becomes a **refresh**. It is its own change, made after the upstream behaviour is accepted. It copies every upstream act together, because a mix of new and old upstream output is a run no production pipeline makes.

Two checks cover the gap between refreshes, neither needing a recording of its own:

- **A chain replay over the most downstream act's frozen snapshot**, which is one consistent run. It asserts only properties that span acts, such as tracing an output back to its source.
- **A model-free compatibility check.** Each act's current recordings are fed to the acts downstream with a fake model, so a change in the shape of an upstream output fails at once. A change in what the upstream act judges is not a code failure, and is brought downstream by a refresh.

A frozen copy is part of the downstream act's request, so it belongs in the request hash.
