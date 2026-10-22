---
address: skills/grind-issues
origin: samthorold/py-minimax-games#199
signal: contradiction
---

The rule to give each delegated agent's files a unique name (Agentic development Guide, the trap on delegated agents outliving their hand-back) reaches agents only through the `grind-issues` brief, which applies it to the PR body alone (`pr-body-[NUMBER].md`). Parallel worktree agents share one scratchpad directory, and they also write helper scripts there (conflict resolvers, one-off analysis scripts), under generic names such as `resolve.py`: in one run, one agent overwrote another's resolver while it was in use. The brief should say that every file an agent writes outside its worktree is named after its issue (or lives in a per-issue subdirectory of the scratchpad), not just the PR body; and the Guide's trap could say "every file outside the worktree" rather than giving the PR body as its example.
