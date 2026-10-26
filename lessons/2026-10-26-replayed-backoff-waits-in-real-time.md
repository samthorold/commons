---
address: guides/web-apps.md#testing
origin: samthorold/go-slow#109
signal: trap
---

A test fake that replays recorded HTTP responses can turn a kept backoff answer into a real wait. The case: a polite client to a public API backs off on a "lagging, retry later" answer (a 200 carrying an error body, or a 429), by the `Retry-After` header or a default. The API lagged while the fixtures were recorded, so the bodies kept were backoff answers. The recorder kept bodies but not headers, so at replay the client fell back to its default backoff, in real time, on every lookup, and the suite hung past its timeout.

*Time is a parameter* already says code that waits takes its sleep as a parameter; the gap is that a replaying fake's wiring must pass one that doesn't wait, since a recording can hold any answer the service gave, backoffs included. Candidate rule: a fake that replays recorded responses is built with a sleep that returns at once (and a recorder keeps the headers the client acts on), so a recorded backoff costs nothing.
