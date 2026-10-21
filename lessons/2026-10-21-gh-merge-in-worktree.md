---
address: guides/global.md   # no workflow section yet; the PR flow it applies to is in guides/python.md#workflow
origin: samthorold/py-minimax-games#144
signal: trap
---

`gh pr merge --delete-branch`, run from a git worktree, prints `fatal: 'main' is already used by worktree` after merging. It tries to switch the current worktree to `main`, and git refuses because `main` is checked out in the primary worktree. The merge itself has already succeeded. An agent that reads the error as a failed merge may retry or stop needlessly. Check the outcome with `gh pr view <n> --json state` instead.

This holds for any Stack using GitHub PRs from worktrees. The squash-merge workflow that triggers it is currently written down in the Python Guide, so promoting this may also mean moving that workflow to the Global Guide.
