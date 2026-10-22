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

## Issues

- **Work is tracked in the repo's GitHub Issues**, through `gh`. A repo that tracks it elsewhere, or labels differently, records a Deviation in its `CLAUDE.md`.
- **An open issue is in one of three states**, by what it needs next, not by who does it:
  - `ready`: specified well enough to work on, by an agent or by the owner.
  - `needs-design`: needs a design session with the owner (a grill) before it can be `ready`.
  - no state label: the backlog, not yet looked at or not scheduled. Nothing picks it up.
- **An issue that won't be done is closed as *not planned*.** If the reason is worth knowing, it goes into the system-design docs, as part of why the design has its shape.
- **An epic** (a whole feature, broken into slices) says "Epic" in its title and carries no state label, so it is never picked up as work; its slices are.
- **A slice's body is its contract**: *Parent* (the epic, if any), *What to build* (behaviour end to end, not layer by layer; no file paths, which go stale), *Acceptance criteria* (each independently checkable), *Out of scope*, *Blocked by* (issue references, or "None"). When discussion changes the contract, rewrite the body rather than leaving the change in comments.
- `bug` and `enhancement` are optional categories, not states.

## Lessons

If something in a Guide proves wrong or incomplete while you work, or you hit something another project in the same Stack or Archetype would also hit, record a Lesson as described in `~/.claude/commons/lessons/README.md`. The Signals and the filter are in `~/.claude/commons/CONTEXT.md`.

- **A Lesson pass** (checking the four Signals) runs at the end of a grill and at the end of a `grind-issues` run: the checkpoints where the owner is present and thinking about design, or where several units of work come back together. Elsewhere, record a Lesson when one is obvious; a missed one recurs.
- **A sub-agent reports what it found to whoever launched it, and doesn't record it.** The launching agent records, so parallel agents can't write duplicate Lessons.
