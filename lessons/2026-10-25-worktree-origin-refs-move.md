---
address: guides/agentic-development.md#the-pr-workflow
origin: samthorold/go-slow#77
signal: trap
---

Worktrees share one repository, so `origin/*` refs move whenever any agent fetches. The Guide's pre-push check, that `git diff origin/main --stat` lists only the PR's own changes, can then show other PRs' merged work as deletions in yours until you merge `main` again. A careful agent reads that as a bad resolution, or a careless one pushes past it.

Fix: run `git fetch origin` and merge `main` immediately before the `--stat` check.

Related, also seen with several agents at once:
- `git fetch` can fail on a ref-lock held by another agent's fetch, and works on retry.
- golangci-lint refuses to start while another instance runs ("parallel golangci-lint is running", exit 3), across worktrees too, so a pre-commit run fails for a reason unrelated to the change.

Briefs for parallel agents should say to expect and retry both.
