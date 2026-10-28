---
address: guides/agentic-development.md#agents-in-parallel
origin: samthorold/go-slow#145 (PRs #179, #180, #181, #182)
signal: trap
---

With several agents in parallel on a small machine, each running the repo's full check (a Go `go test -race ./...` whose slowest packages take about 2 minutes alone), those packages ran past the test runner's default 10-minute per-package timeout from contention alone: 4 of 4 agents in one run hit it, with load averages of 10–13. Nothing hung. The test named as running when the timer fired had been going only 0–3 seconds, which is how a contention timeout differs from a real hang. Run alone with a longer timeout, the same packages passed in 4–11 minutes.

The Guide's "cap build and test parallelism per agent" doesn't reach this: a per-agent cap (`-p 4`) limits packages per process, not how many agents' race binaries run at once, and it can't reach the check's own command, which the pre-commit hook fixes. A brief that says "report a test that runs away" then reads as a hang report, or makes the agent skip the full check. CI, on its own runner, passed every one.

How it would apply: cap the number of agents whose full checks may run at once by the full check's cost, not only by memory; and tell briefs that a timeout with the running test only seconds old is load, to be re-run alone with a longer timeout (or left to CI), not reported as a hang.
