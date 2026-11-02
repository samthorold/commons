---
address: guides/model-calls/changing-an-act.md
origin: samthorold/go-slow#257
signal: gap
---

A re-recording can come back undecided on a failure mode the act already had, which the change made more frequent: a slip that happened in 2 of 7 attempts before the change happened in 14 of 22 after it. Without the earlier rate, the agent doing the re-recording can't tell a regression from noise or from a new failure, and is tempted to tune the instructions until the count crosses the line. A brief for a slice that changes an act should name the known failure modes on the fixtures it will re-record, with their rate on the current recordings (attempts that failed each check, from the kept `earlier_attempts`), and say what to do if one comes back worse: read it again as the rule allows, then stop and report the counts.
