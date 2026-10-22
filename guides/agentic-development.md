# Agentic development Guide

**Scope:** every Stack, every Archetype. The topic is how agents change a repo: branches, PRs, merging, and agents working in parallel.

## Stance: agents implement test-first

- **Stance:** an agent implements a change through test-driven development, in vertical slices: one failing test, the code to pass it, refactor, repeat (the `/tdd` Skill). Never all the tests first, never the code first.
- **Why:** an agent working unattended needs an objective signal of done that it didn't shape to fit its own code. A test written before the code pins down the intended behaviour while the agent still only knows the intent; tests written after tend to describe whatever got built, bugs included. Small red-green steps also keep each change small enough to diagnose when it goes wrong, and leave a suite that lets the next agent change the code safely.
- **How to apply:** for every feature or bug fix, whether in a Skill-driven run (e.g. `grind-issues`) or not. A bug fix starts with a test that reproduces it. Where the Archetype makes exact assertions hard (stochastic simulations, search), test properties, invariants or seeded runs rather than skipping the test.
- **What would change our mind:** work where a failing test can't express the intent before the code exists, such as throwaway prototypes (the `prototype` Skill) and exploratory spikes whose output is a finding, not code to keep. Those are exempt as long as their code isn't merged as-is. If a kind of change keeps needing that exemption, record a Lesson.

## The PR workflow

- Every change goes through a branch and a PR, never straight to `main`.
- A PR whose checks all pass may be squash-merged without asking (`gh pr merge <n> --squash --delete-branch`, then `git switch main`, `git pull`), including one that publishes a release when merged (the Stack's Guide says which PRs do). Wait for green with `gh pr checks <n> --watch`; never merge with failing or pending checks.
- A PR that falls behind `main`: merge `main` into it, never rebase (`gh pr update-branch <n>`, or `git merge origin/main` when it conflicts), then wait for CI again. With squash merges the branch history never reaches `main`, so rebasing buys nothing; a merge resolves conflicts once, in one commit `git show` exposes, with no force-push.
- Resolve conflicts hunk by hunk, never by taking one side of a whole file, and before pushing check that `git diff origin/main --stat` lists only the PR's own changes. *Why:* a resolution that takes one side of a file silently deletes another PR's merged work, and CI stays green because the deleted tests go with the deleted code. A deletion outside the PR's scope means a resolution went wrong.
- **Merge authority is granted per repo, never globally.** *Why:* a merge to `main` is irreversible and, for a release PR, publishes; granting it only in repos explicitly opted in confines a misfiring agent's blast radius to those repos. How the grant is made is harness-specific: for Claude Code, see the per-project allowlist in the global `CLAUDE.md`.

## Agents in parallel

- **One git worktree and one branch per agent.** Independent slices run concurrently; their merges still happen one at a time, each PR catching up with `main` as above.
- **Each brief carries the workflow rules above**, conflict resolution included. A sub-agent sees only its brief and the Imported Guides, not the conversation that launched it.
- **Ignore the worktrees directory** (e.g. `.claude/worktrees/`) in `.gitignore`, so a `git add -A` in the primary checkout can't stage the worktrees as embedded repositories.
- **Each worktree builds its own environment** (virtualenv, compiled artefacts), from shared caches. On a small machine, cap build and test parallelism per agent so several agents fit at once.
- **Slices that touch the same files** (lock files, a shared results document, a CLI entry point) are fine to run in parallel: the later PR merges `main` in and resolves. Sequence them only when one slice's design depends on another's outcome.

## Known traps

- **GitHub closes `#N` wherever a closing keyword sits directly before it**: `close`, `closes`, `fix`, `fixes`, `resolve` or `resolves` (any case), anywhere in a PR body or commit message, even inside a quoted table cell or a sentence about another issue. Merging then closes that issue unintended. Write "#N closes" or "the row closing #N" unless you mean it, and check a PR body's references before merging (`grind-issues` does this). *Remove when:* GitHub stops treating keywords in quoted text as closing, or a check enforces it on every PR.
- **A delegated agent can outlive its hand-back.** A sub-agent can report done while work it started is still running: its own sub-agent, which goes on to commit, open a PR or overwrite a shared file, or background processes (long test or simulation runs). Before touching a branch after a delegated agent hands back: wait for every completion notification, check `gh pr list --head <branch>` and running processes, and confirm the branch head is stable. Give each delegated agent's files (e.g. a PR body written to a scratchpad) a unique name, and don't let delegated agents spawn agents of their own. Running agents in parallel makes this more likely, not less. *Remove when:* the harness stops reporting a sub-agent done while its own work runs; `grind-issues` already applies the check, so this entry covers delegation outside it.

- `gh pr merge --delete-branch` run from a git worktree prints `fatal: 'main' is already used by worktree` after merging, because it can't switch that worktree to `main`. The merge itself succeeded; check with `gh pr view <n> --json state` rather than retrying. *Remove when:* `gh pr merge` handles a worktree whose `main` is checked out elsewhere.

## Lessons

If something in this Guide proves wrong or incomplete while you work, or you hit a workflow problem another project would also hit, record a Lesson addressed to this Guide, as described in `~/.claude/commons/lessons/README.md`.
