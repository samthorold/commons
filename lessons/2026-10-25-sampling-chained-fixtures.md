---
address: guides/model-calls.md#stance-a-recording-is-one-sample-of-one-request
origin: samthorold/go-slow#86
signal: gap
---

Sampling each fixture N times assumes each fixture's request is fixed. For an act whose fixtures build on each other, it isn't. A placing act weighs each Item against the Stories the earlier Items started, so each sample of an earlier fixture leaves a different store behind.

Every sample of a fixture has to run over one shared prior state, or the samples answer different requests and are not samples of one rate. A workable rule is to carry each earlier fixture forward by its first sample that passed, chosen before the later fixture is sampled, and run each sample of the later fixture over a copy of that state.

Related trap (Go): `go test`'s default 10-minute timeout kills a multi-sample recording partway through. Writing each attempt as it arrives, and resuming by keeping samples that still match the current request, kept every paid call. The recording command should pass an explicit long `-timeout`.
