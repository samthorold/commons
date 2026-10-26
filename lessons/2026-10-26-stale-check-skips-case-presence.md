---
address: guides/model-calls.md#stance-a-recording-is-one-sample-of-one-request
origin: samthorold/go-slow#104
signal: gap
---

The free stale check (replaying with no recording) reports that a refreshed input changes an act's requests. It doesn't report that the refreshed input no longer holds the case a property needs. The check that the case is present sits inside the sample's property code, and that code never runs while the request hashes mismatch. So the missing case appears only on a paid recording run, here by luck after the first call.

The case: a downstream act's frozen copy of an upstream act's output was refreshed onto newer recordings, which no longer drew the statement a property looks for. The free check showed the act as stale (expected) and nothing else.

How it would apply: run each property's case-presence assertion over the act's inputs (its frozen copies and fixtures) as a test of its own, independent of whether the act's recordings are stale, so a refresh that removes a case fails for free before any call is paid for.
