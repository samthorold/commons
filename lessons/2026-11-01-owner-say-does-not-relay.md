---
address: guides/agentic-development.md#agents-in-parallel
origin: samthorold/go-slow#254 (PR #262)
signal: gap
---

An act gated on the owner's say (here, a re-recording on an expensive model) can't be authorized to a running sub-agent by relaying the owner's answer in a message. The sub-agent rightly treats an agent's message as direction, never as the owner's consent, and stops short. The orchestrator then has to run the act itself, which works but costs a round trip and splits the slice's work between two agents.

Candidate rule: before launching a slice that may need a gated act, get the owner's say for it up front, with its cap, and put it in the brief, which the sub-agent treats as its instructions. If the need only appears mid-run, the orchestrator runs the gated act itself rather than relaying consent.
