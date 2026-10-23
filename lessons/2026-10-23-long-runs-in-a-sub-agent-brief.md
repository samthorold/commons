---
address: skills/grind-issues
origin: samthorold/py-minimax-games#210
signal: gap
---

The sub-agent brief says "don't leave anything running in the background: report back only once all your work has stopped", and a brief for an experiment slice naturally adds "run the match in the foreground". But Claude Code caps a foreground command at 10 minutes, and a slice whose acceptance criteria include a run of up to the low tens of minutes (here a capped sequential test, expected 10-22 minutes) can't meet both. The agent resolved it correctly (ran it in the background, waited on it, reported once nothing was running) and recorded the departure, but a less careful agent could kill the run at the timeout or hand back while it still runs. The brief could say what the rule is for: a run longer than the foreground limit goes in the background, and the agent waits for its completion before reporting.
