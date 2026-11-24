---
address: skills/grind-issues/SKILL.md
origin: samthorold/explorers#886
signal: trap
---

Where a repo's ruleset requires a PR's branch to be up to date with `main` before merging, and auto-merge is disabled, every merge in a `grind-issues` run sends every other open PR back through CI: `gh pr merge` refuses a green PR whose base is stale ("the head branch is not up to date"), and `--auto` is refused too. Updating all the waiting PRs at once wastes runs, since each merge makes the rest stale again. What worked: fix a merge order, run `gh pr update-branch` only on the next PR in it, merge it once its new run is green, then update the next. Step 3 could say so, and Test Discovery could check the ruleset's strictness (`gh api repos/<o>/<r>/rulesets`) so the orchestrator plans for it.
