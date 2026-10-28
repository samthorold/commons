---
address: guides/model-calls.md#stance-models-sit-behind-a-port-and-are-chosen-by-measurement
origin: samthorold/go-slow#188
signal: gap
---

"Choose each act's model by measuring candidates on the act's own fixtures" assumes the recording harness can record a candidate model. A harness built as the Guide's recording Stances describe can't, once acts are chained. The replay hashes each request with the act's pinned model, and the carry-on between chained fixtures replays the earlier fixtures' samples to build the next one's input. Recorded on any other model, those samples are stale, so a run on a candidate fails at the second chained fixture. The measurement then needs a throwaway patch, and the patch decides a question the Guide doesn't raise: does each fixture run over what the pinned model left behind (the same requests bar the model, so only one placing at a time is compared), or over the candidate's own chain (which shows how differences compound, but on different requests)?

The Guide could say that a recording harness records a candidate into a scratch directory without touching the pin, hashing with the model being recorded, and that a measurement brief chooses one of those two bases and says so.
