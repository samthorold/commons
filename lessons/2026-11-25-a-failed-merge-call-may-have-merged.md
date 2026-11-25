---
address: guides/agentic-development/merging.md
origin: samthorold/explorers#913
signal: trap
---

`gh pr merge` can return a server error (a 502, or a GraphQL "Something went wrong") after GitHub has merged the PR, and the PR's state read just afterwards can still say open. Here three retries failed while the merge had landed between them; the REST view then showed the PR "behind" its own squash commit. Before retrying a failed merge, fetch and check `main`'s log for the PR's squash commit; if it is there, the merge happened and only the cleanup (branch deletion) is left. The same holds for `gh issue create`: check for the issue before creating it again.
