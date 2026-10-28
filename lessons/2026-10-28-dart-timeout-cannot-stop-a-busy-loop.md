---
address: guides/flutter.md
origin: a private Adopter (see the portfolio)
signal: trap
---

`dart test --timeout` (and a test's own timeout) can't stop a test stuck in a synchronous loop: the timer only fires when the loop yields to the event loop, which it never does. A generator test that asks for something it can't reach (a puzzle grade the grader can't yet produce) then hangs the whole run instead of failing. Search and generation loops under test need an attempt cap that throws, and an agent watching a run that is past its baseline must find and stop the stuck test rather than wait for the timeout.
