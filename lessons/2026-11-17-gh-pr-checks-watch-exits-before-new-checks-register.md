---
address: guides/agentic-development/merging.md
origin: samthorold/go-slow#313
signal: trap
---

Right after a push or `gh pr update-branch`, `gh pr checks <n> --watch` can exit at once with "no checks reported on the '<branch>' branch" and a non-zero code, before GitHub has registered the new run, or report the previous run's result. It reads like a failed CI. It happened twice in one run. Wait on the run itself instead: `gh run list --branch <branch> --limit 1` for its id, then `gh run watch <id> --exit-status`. Before merging, confirm the passing check belongs to the PR's current head (`gh pr view <n> --json headRefOid,statusCheckRollup`). A run cancelled because a newer one for the same ref superseded it is also not a failure.
