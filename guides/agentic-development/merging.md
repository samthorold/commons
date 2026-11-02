# Agentic development Guide: merging a PR

The Conventions for merging a PR, from [the Agentic development Guide](../agentic-development.md#the-pr-workflow), which says when to read them.

- A PR whose checks all pass may be squash-merged without asking (`gh pr merge <n> --squash --delete-branch`, then `git switch main`, `git pull`), including one that publishes a release when merged (the Stack's Guide says which PRs do). Wait for green with `gh pr checks <n> --watch`; never merge with failing or pending checks.
- **Merge authority is granted per repo, never globally.** *Why:* a merge to `main` is irreversible and, for a release PR, publishes; granting it only in repos explicitly opted in confines a misfiring agent's blast radius to those repos. How the grant is made is harness-specific: for Claude Code, see the per-project allowlist in the global `CLAUDE.md`.
