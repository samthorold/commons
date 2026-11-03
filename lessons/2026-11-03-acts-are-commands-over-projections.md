---
address: guides/model-calls.md#stance-change-an-act-on-its-cheapest-stage-then-record-the-chain-once
origin: samthorold/go-slow#296
signal: gap
---

The Guide treats an app's acts as a chain (upstream, downstream, refreshed in chain order) and says nothing about whether a downstream act waits for an upstream one in use. When the app keeps its Record as events, a shape that holds up better is: each act is a command that reads a projection of the Record as it stands and outputs zero or more events; no act waits for or knows which acts ran before it, so the Record is eventually consistent; and an act run again over a Record that has moved on (an upstream judgement arrived since) may judge differently, which is intended, since it is how judgements improve as the Record fills in. Ordering acts in use (B only once A has judged) makes the slowest act, often a batch taking hours, hold up every act after it, and an output due at a set time misses it. Decoupling moves the risk elsewhere: events that lead to commands can loop, so "no chain of commands runs away" becomes a stated constraint of the design. The chain still matters for recordings (frozen inputs, refresh order), just not for when acts run. Worth a line in the Guide: acts in use are decoupled commands over projections; the chain is a property of the recordings.
