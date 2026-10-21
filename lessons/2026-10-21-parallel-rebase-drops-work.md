---
address: guides/global.md   # as above: the PR flow is currently in guides/python.md#workflow
origin: samthorold/py-minimax-games#145
signal: trap
---

When several agents develop in parallel and each rebases its PR onto a `main` that others have just merged into, a conflict resolved by taking one side of a whole file silently deletes the other PR's merged work. CI stays green because the deleted tests go with the deleted code, and requiring branches to be up to date doesn't catch it, because the bad resolution happens before CI runs. One PR's merge removed a whole module, its tests, CLI options and docs from an earlier PR.

The guard: resolve conflicts hunk by hunk, never by taking one side of a file, and before pushing check `git diff origin/main --stat`. It should list only the files and changes the PR is meant to make; a deletion outside its scope means a resolution went wrong. Say this explicitly in every parallel agent's brief.
