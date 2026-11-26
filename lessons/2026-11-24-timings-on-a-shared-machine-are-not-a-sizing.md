---
address: guides/agentic-development/agents-in-parallel.md
origin: samthorold/py-minimax-games#231
signal: trap
---

An agent that sizes a run from measured cost, or reads a speed hypothesis, measures whatever else the machine is doing. With several agents and sessions working on one laptop (load 9-26 on 8 cores), every timing came out about 2-3× slower than on a quiet machine, so the run was sized smaller and took longer than the sizing predicted. A timing taken by an agent should be recorded with the load it ran under, and a speed reading (as opposed to a sizing) taken while other agents run should be treated as an upper bound and taken again on a quiet machine.

"No other agent running" doesn't make the machine quiet (samthorold/py-minimax-games#240). A run made with no other agent going was still about 3-5× slower than earlier measurements. The 1-minute load ran 5.5-60 because of the owner's own applications (a browser, an emulator), under memory pressure. Record memory pressure beside load, and before a timed run check what is running, not only which agents are.
