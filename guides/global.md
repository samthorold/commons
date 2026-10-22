# Global Guide

**Scope:** every Stack, every Archetype.

## Durable knowledge goes in source control, not private memory

- **Don't keep project knowledge in auto-memory.** Anything worth remembering across sessions (workflow, runtimes, known traps, vision, how to work on the project) goes in the repo's `CLAUDE.md` or the docs it points to, so it is committed, reviewed and visible. Update those docs instead of writing a memory file.
- **Knowledge that would hold for other projects goes to the Commons**, as a Lesson (see below), not only into the project's own docs.

## GitHub repo settings and branch protection

- Merge settings: squash merge only (no merge commits, no rebase), delete branch on merge.
- **The squash commit is the PR's title and body** (`squash_merge_commit_title: PR_TITLE`, `squash_merge_commit_message: PR_BODY`). *Why:* the PR body is where a change's reasons are recorded (see the Agentic development Guide's *decide, record, carry on*), and only what lands in the commit reaches `git log` and `git blame`, which outlive the forge.
- A `main` **ruleset** (Settings → Rules, or `gh api -X POST repos/<owner>/<repo>/rulesets --input ruleset.json`): block deletion and non-fast-forward; require a PR with 0 approvals and `allowed_merge_methods: ["squash"]`; required status checks = the CI job names (`integration_id` 15368, GitHub Actions) with `strict_required_status_checks_policy: true` (branch must be up to date); no bypass actors. Copy py-ev's with `gh api repos/samthorold/py-ev/rulesets/<id>`.
- Create the ruleset only after CI has reported under the exact job names, and record the required check names in the repo's `CLAUDE.md`: renaming the job or changing the matrix breaks merging until the ruleset is updated.

## Lessons

If something in a Guide proves wrong or incomplete while you work, or you hit something another project in the same Stack or Archetype would also hit, record a Lesson as described in `~/.claude/commons/lessons/README.md`. The Signals and the filter are in `~/.claude/commons/CONTEXT.md`.
