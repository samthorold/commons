---
address: guides/agentic-development.md#stance-decide-record-carry-on
origin: samthorold/go-slow#45
signal: trap
---

"Decide, record, carry on" asks an agent to record a call where the next reader will look, which sometimes means a follow-up issue. A sub-agent in a `grind-issues` run had `gh issue create` denied by the auto-mode classifier: the per-repo allowlist grants PRs and merges but not issues. The follow-up had to go back to the orchestrator as a drafted body. Either the brief should say "draft follow-up issues to a named file and report them; the orchestrator opens them", or the per-repo allowlist should include `gh issue create`.
