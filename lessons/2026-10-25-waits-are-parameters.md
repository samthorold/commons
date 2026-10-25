---
address: guides/web-apps.md#testing
origin: samthorold/go-slow#29
signal: gap
---

"Time is a parameter" names only the clock. Code that waits (backoff on `Retry-After`, per-host rate limits, an in-process timetable) also needs the wait injected: a `Sleep(ctx, d)` function and a channel of ticks. Without them a test either really sleeps or races on cancellation, and the first version of such a test is flaky.
