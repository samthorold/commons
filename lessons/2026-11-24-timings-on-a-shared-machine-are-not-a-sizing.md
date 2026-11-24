---
address: guides/agentic-development/agents-in-parallel.md
origin: samthorold/py-minimax-games#231
signal: trap
---

An agent that sizes a run from measured cost, or reads a speed hypothesis, measures whatever else the machine is doing. With several agents and sessions working on one laptop (load 9-26 on 8 cores), every timing came out about 2-3× slower than on a quiet machine, so the run was sized smaller and took longer than the sizing predicted. A timing taken by an agent should be recorded with the load it ran under, and a speed reading (as opposed to a sizing) taken while other agents run should be treated as an upper bound and taken again on a quiet machine.
