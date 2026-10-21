# Agentic development Guide

**Scope:** every Stack, every Archetype. The topic is how agents change a repo: branches, PRs, merging, and agents working in parallel.

## The PR workflow

- Every change goes through a branch and a PR, never straight to `main`.
- A PR whose checks all pass may be squash-merged without asking (`gh pr merge <n> --squash --delete-branch`, then `git switch main`, `git pull`), except a PR that publishes a release when merged: ask before merging that (the Stack's Guide says which PRs do). Wait for green with `gh pr checks <n> --watch`; never merge with failing or pending checks.
- A PR that falls behind `main`: merge `main` into it, never rebase (`gh pr update-branch <n>`, or `git merge origin/main` when it conflicts), then wait for CI again. With squash merges the branch history never reaches `main`, so rebasing buys nothing; a merge resolves conflicts once, in one commit `git show` exposes, with no force-push.
- Resolve conflicts hunk by hunk, never by taking one side of a whole file, and before pushing check that `git diff origin/main --stat` lists only the PR's own changes. *Why:* a resolution that takes one side of a file silently deletes another PR's merged work, and CI stays green because the deleted tests go with the deleted code. A deletion outside the PR's scope means a resolution went wrong.
- Repos using this flow need the per-project allowlist in `.claude/settings.local.json` (see the global `CLAUDE.md`).

## Agents in parallel

- **One git worktree and one branch per agent.** Independent slices run concurrently; their merges still happen one at a time, each PR catching up with `main` as above.
- **Each brief carries the workflow rules above**, conflict resolution included. A sub-agent sees only its brief and the Imported Guides, not the conversation that launched it.
- **Ignore the worktrees directory** (e.g. `.claude/worktrees/`) in `.gitignore`, so a `git add -A` in the primary checkout can't stage the worktrees as embedded repositories.
- **Each worktree builds its own environment** (virtualenv, compiled artefacts), from shared caches. On a small machine, cap build and test parallelism per agent so several agents fit at once.
- **Slices that touch the same files** (lock files, a shared results document, a CLI entry point) are fine to run in parallel: the later PR merges `main` in and resolves. Sequence them only when one slice's design depends on another's outcome.

## Known traps

- `gh pr merge --delete-branch` run from a git worktree prints `fatal: 'main' is already used by worktree` after merging, because it can't switch that worktree to `main`. The merge itself succeeded; check with `gh pr view <n> --json state` rather than retrying.

## Lessons

If something in this Guide proves wrong or incomplete while you work, or you hit a workflow problem another project would also hit, record a Lesson addressed to this Guide, as described in `~/.claude/commons/lessons/README.md`.
