---
address: guides/global.md#github-repo-settings-and-branch-protection
origin: a private repo on a free GitHub plan, its first CI PR
signal: contradiction
---

The Guide requires a `main` ruleset with required status checks. On a private repo under a free GitHub plan, GitHub refuses both rulesets and classic branch protection: `POST /repos/<owner>/<repo>/rulesets` returns 403 "Upgrade to GitHub Pro or make this repository public to enable this feature." The merge settings (squash only, delete branch, PR title and body as the squash commit) still apply.

The check is then held only by the merge rule in the Agentic development Guide (merge only once `gh pr checks <n> --watch` is green), recorded as a Deviation in the repo's `CLAUDE.md`, along with the job name a ruleset would require if the plan changes. The Guide could name this case so that each private repo doesn't rediscover it.
