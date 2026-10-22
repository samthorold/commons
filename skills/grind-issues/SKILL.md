---
name: grind-issues
description: Work through the open ready-for-agent GitHub issues (or a given list) using TDD, each implemented by a sub-agent: branch, red-green-refactor, commit, open PR, squash-merge. Independent issues run in parallel, dependent ones in sequence. Use when user says "grind issues", "work through issues", "clear the backlog", or wants automated issue-by-issue TDD delivery.
---

# Grind Issues

Work through the current repo's open issues that are ready for an agent (or the issues the user names). Each issue is implemented by its own **sub-agent**, so context stays clean between issues. Issues that don't depend on each other run in parallel; the orchestrator (you) assesses, plans the order and merges.

How agents branch, catch up with `main`, resolve conflicts and work in parallel is the **Agentic development Guide** (`~/.claude/commons/guides/agentic-development.md`, Imported into every session). This skill applies it; where they seem to disagree, the Guide wins.

## Startup

1. **Check for a user-supplied list first.** If the user included specific issue numbers in their invocation (e.g., "grind #12 #15 #20"), use exactly those issues — skip the fetch-and-ask step entirely and go straight to step 4.

2. Otherwise, fetch the open issues that are ready for an agent — the triage state the planning skills (`to-issues`, `triage`) give grabbable work; epics, `needs-triage`, `ready-for-human` and parked issues are not on the list. Map the label through the repo's triage-label doc if it has one:

```
gh issue list --state open --label ready-for-agent --json number,title,body,labels \
  --jq 'sort_by(.number) | .[] | {number, title, body, labels: [.labels[].name]}'
```

3. Present the list to the user with a numbered summary. Ask: **"Ready to start grinding through these? Any you want to skip or reorder?"**

4. **Lock the worklist.** After confirmation (or if the user supplied a list), create one task per issue — a separate `TaskCreate` call for each, because the harness shows one to-do item per call and a checklist inside a single task's description renders as one entry. For each issue, call `TaskCreate` with:

- `subject`: `#<number> — <title>` (e.g., `#15 — Fix energy overflow`)
- `description`: a one-line note that the issue will be assessed and implemented via the per-issue loop
- `activeForm`: `Grinding #<number>` (e.g., `Grinding #15`)

These tasks are the single source of truth for what to work on. Do NOT add issues that aren't on this list. Do NOT skip issues that are on this list (unless they're already closed/done). When you start an issue, mark its task `in_progress` via `TaskUpdate`; when it's resolved, mark it `completed`.

5. Discover the test command (see below), plan the order (see below), then begin the loop.

## Test Discovery (once, before the loop)

Before delegating any issues, find out how the project runs its tests. Its `CLAUDE.md` or contributor docs may name a fast inner-loop command (one crate, package or file, slow tests skipped) and a full command to run before committing; otherwise use the standard full-suite command for the toolchain. Run the full command once and record:

- **The commands**: inner loop (if the project has one) and full
- **How many tests currently pass** (e.g., "220 passed")
- **How long the full run took**, and roughly how much of that was building rather than testing, if the output shows it

Include these in every sub-agent prompt under a `## How to run tests` header.

## Planning the order (once, before the loop)

Read every issue on the worklist, then decide which can run together:

- **Sequence an issue after another** when its design depends on the other's outcome: it says it's blocked by it, extends what the other introduces, or would be designed differently once the other lands.
- **Otherwise run it in parallel.** Touching the same files (lock files, a shared results document, a CLI entry point) is not a reason to sequence: the later PR merges `main` in and resolves, as the Guide says.
- **Cap how many run at once** by what the machine can hold: each worktree builds its own environment, and the full test run's duration from Test Discovery is a guide to how heavy each agent is. When unsure, start with two or three.

Tell the user the plan in a line or two (what runs first, what waits for what). Within those constraints, start issues in worklist order — ID order, unless the user reordered them or supplied their own list. One issue at a time is still a valid plan when everything depends on everything.

## Per-Issue Loop

For each issue, the orchestrator performs a quick assessment, then delegates implementation to a sub-agent. Several issues can be in the loop at once, each at its own step.

### Step 1 — Assess (orchestrator)

Mark this issue's task `in_progress` via `TaskUpdate`. Then read the issue body and comments (`gh issue view <number> --comments`). Determine:

- **Actionable**: the issue describes a concrete change that can be implemented and tested. → Delegate to sub-agent (Step 2).
- **Already done**: the feature/fix already exists in the codebase. → Close with a comment explaining why, mark the task `completed`, move to next issue.
- **Unclear**: not enough detail to implement. → Post a comment saying what is missing, starting with the line `> *This was generated by AI during triage.*`; move the issue from `ready-for-agent` to `needs-info` (label strings per the repo's triage-label doc); mark the task `completed` (it's been processed), move to next issue. Issues sequenced after it may need re-planning.

### Step 2 — Delegate to sub-agent

Spawn a sub-agent using the **Agent tool** with `isolation: "worktree"`, so parallel agents never share a checkout, and a `name` (e.g. `issue-[NUMBER]`) so you can message it again in Step 3. Launch independent issues in the same message so they run concurrently. The sub-agent gets a self-contained prompt with everything it needs.

**Sub-agent prompt template:**

```
You are working on issue #[NUMBER]: [TITLE]

## How to run tests

Inner loop: [INNER-LOOP COMMAND, or "none - use the full command"]
Before committing: [FULL COMMAND]
Baseline: [N] tests pass; the full run took [DURATION] ([BUILD SHARE] of it building).

Run the inner loop after each change and the full command before you
commit. The first run after an edit rebuilds and can take several times
the baseline - that is slow, not stuck. What to watch for is a test that
hangs or runs away: if a run is well past the baseline and no longer
compiling, find which test is still running, stop it, and report that
test to the orchestrator instead of waiting it out or retrying.
[IF PARALLEL: Other agents are running at the same time; cap build and
test parallelism to [LIMIT].]

## Issue description

[FULL ISSUE BODY AND RELEVANT COMMENTS]

## How to work

You are in your own git worktree. Follow the Agentic development Guide
(~/.claude/commons/guides/agentic-development.md): in particular, catch
up with main by merging it, never rebasing; resolve conflicts hunk by
hunk; and before pushing, check that `git diff origin/main --stat` lists
only this issue's changes.

## Your task

Implement this issue using strict TDD by invoking the `/tdd` skill.
You are running unattended, with no user to answer questions: where
`/tdd` says to confirm with the user or get their approval, make the
call yourself and state it, with your reasoning, in the PR body.

1. Read the codebase. Use the project's CONTEXT.md for domain
   vocabulary and docs/system-design/ for the design and the reasons
   behind it.
2. Create a branch from the latest main, running each command as its
   own call: `git fetch origin`, then
   `git switch -c issue-[NUMBER]-[SLUG] origin/main`
3. Invoke `/tdd` to implement the feature. Follow the skill's full
   workflow: planning, tracer bullet, incremental red-green loop,
   refactor. Do NOT write all tests first — vertical slices only.
4. When all tests pass and you're satisfied with the implementation,
   commit, push, and open a PR:

   git add <specific-files>
   git commit -m "<descriptive message>

   Closes #[NUMBER]"
   git push -u origin issue-[NUMBER]-[SLUG]
   gh pr create --title "<short title>" --body "$(cat <<'EOF'
   ## Summary
   <1-3 bullets>

   Closes #[NUMBER]

   ## Test plan
   - <what the tests verify>

   🤖 Generated with [Claude Code](https://claude.com/claude-code)
   EOF
   )"

5. Don't spawn agents of your own, and don't leave anything running in
   the background: report back only once all your work has stopped. If
   you write the PR body to a file, name it after the issue
   (e.g. `pr-body-[NUMBER].md`), since other agents are working too.

6. Report back: what you implemented, the PR number, and any problems.
   Also report anything that looked like a Lesson for the Commons (see
   ~/.claude/commons/CONTEXT.md, "Recognising a Lesson"): a Guide that
   was wrong or not enough, a Deviation you recorded, a decision no
   Guide covered, or a trap another project would hit. Say "none" if
   nothing did.
```

**Sub-agent instructions:**

- Include the full issue body in the prompt. The sub-agent has no access to previous context.

### Step 3 — Merge (orchestrator)

Merge PRs **one at a time**, as their sub-agents finish, under the Agentic development Guide's PR workflow (which says when a PR may merge without asking).

```bash
gh pr checks <PR-NUMBER> --watch
gh pr merge <PR-NUMBER> --squash --delete-branch
git switch main
git pull
```

Run each as its own call, from the primary checkout. Never merge with failing or pending checks.

**Before touching a PR, make sure its sub-agent has really finished** (see the Agentic development Guide's trap on delegated agents outliving their hand-back): you've had its completion notification, `gh pr list --head <branch>` shows only the one PR, nothing it started is still running, and the branch head hasn't moved since it reported. This wait is per PR: meanwhile, carry on assessing, launching and merging other issues.

**Check the PR's closing references** before merging (see the Guide's trap on closing keywords): `gh pr view <PR-NUMBER> --json closingIssuesReferences --jq '[.closingIssuesReferences[].number]'` should list only the issue being worked. If it lists others, edit the PR body (`gh pr edit <PR-NUMBER> --body-file <file>`) to reword them before merging.

After each merge, other open PRs from this run may be behind `main`. When you come to merge one, if it's behind, run `gh pr update-branch <PR-NUMBER>` and wait for checks again. If that fails on a conflict, send the PR back to its sub-agent (`SendMessage` to its name) to merge `main` in and resolve as the Guide says, then merge once it's green.

Record the outcome: issue number, PR number, status. Once an issue is merged, start any issue that was waiting on it.

### Step 4 — Update worklist and advance

Mark the completed issue's task `completed` using `TaskUpdate`. Start the next pending issues the plan allows, up to the cap. Do not pick issues outside the worklist. Repeat from Step 1.

## Completion

When all issues have been processed, report a summary:

- Issues implemented and merged (with PR numbers)
- Issues closed as already done
- Issues skipped (needs-info or unclear)
- Lessons the sub-agents reported. Record each that passes the filter (`~/.claude/commons/CONTEXT.md`, "Recognising a Lesson") as a Lesson, as `~/.claude/commons/lessons/README.md` describes.

## Rules

- **Parallel where independent, sequential where dependent.** Sequence only on design dependence, not on shared files. Merges are always one at a time.
- **One worktree per sub-agent.** Never let two agents share a checkout.
- **Always delegate implementation.** The orchestrator assesses, plans and merges. The sub-agents implement.
- **Implementation goes through `/tdd`, always.** The sub-agent invokes it with the Skill tool. This is the Agentic development Guide's test-first Stance; parallelism is a judgement call, TDD is not.
- **Squash-merge only, on green.** Keep main's history clean.
- **Check before implementing.** If the issue looks already resolved, verify before closing.
- **Respect the domain.** Use vocabulary from CONTEXT.md and honor the documented system design.
- **No context bleed.** Each sub-agent prompt must be self-contained.
- **Stick to the worklist.** Only work on issues that have a task created during startup. Never add or substitute issues mid-run.
