---
address: guides/agentic-development.md#agents-in-parallel
origin: samthorold/go-slow#47 (PRs #50, #54)
signal: gap
---

When a delegated slice comes back with something to fix, the orchestrator's easy move is to send it back to the same agent on the same PR with another change. Three send-backs grew one PR from one change into four: inline schema, dropped summary, an attribution run, precedent text. Each extra change made the merge harder to review and its paid re-recording harder to attribute. Land what is done and sound as its own PR, and give each further change its own small slice, even when the same agent does them. The Guide's PR workflow says how one PR merges, but not when to stop adding to it.
