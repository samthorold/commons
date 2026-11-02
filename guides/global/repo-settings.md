# GitHub repo settings and branch protection

Detail for the [Global Guide](../global.md). Read when creating a GitHub repo, or changing its merge settings, its `main` ruleset or the CI job names the ruleset requires.

- Merge settings: squash merge only (no merge commits, no rebase), delete branch on merge.
- **The squash commit is the PR's title and body** (`squash_merge_commit_title: PR_TITLE`, `squash_merge_commit_message: PR_BODY`). *Why:* the PR body is where a change's reasons are recorded (see the Agentic development Guide's *decide, record, carry on*), and only what lands in the commit reaches `git log` and `git blame`, which outlive the forge.
- A `main` **ruleset** (Settings → Rules, or `gh api -X POST repos/<owner>/<repo>/rulesets --input ruleset.json`): block deletion and non-fast-forward; require a PR with 0 approvals and `allowed_merge_methods: ["squash"]`; required status checks = the CI job names (`integration_id` 15368, GitHub Actions) with `strict_required_status_checks_policy: true` (branch must be up to date); no bypass actors. Copy py-ev's with `gh api repos/samthorold/py-ev/rulesets/<id>`.
- Create the ruleset only after CI has reported under the exact job names, and record the required check names in the repo's `CLAUDE.md`: renaming the job or changing the matrix breaks merging until the ruleset is updated.
- **A private repo on a free plan gets no ruleset.** GitHub refuses rulesets and classic branch protection there (403, "Upgrade to GitHub Pro or make this repository public"). The merge settings still apply, and the checks are held only by the merge rule (Agentic development Guide: merge only on green). The repo's `CLAUDE.md` records this as a Deviation, with the job names a ruleset would require.
