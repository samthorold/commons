---
name: grind-issues
description: Work through the open `ready` GitHub issues (or a given list) using TDD, each implemented by a sub-agent: branch, red-green-refactor, commit, open PR, squash-merge. Independent issues run in parallel, dependent ones in sequence. Use when user says "grind issues", "work through issues", "clear the backlog", or wants automated issue-by-issue TDD delivery.
---

# Grind Issues

Work through the current repo's open `ready` issues (or the issues the user names). Each issue is implemented by its own **sub-agent**, so context stays clean between issues. Issues that don't depend on each other run in parallel; the orchestrator (you) assesses, plans the order and merges.

How agents branch, catch up with `main`, resolve conflicts and work in parallel is the **Agentic development Guide** (`~/.claude/commons/guides/agentic-development.md`, Imported into every session). This skill applies it; where they seem to disagree, the Guide wins.

## Startup

1. **Check for a user-supplied list first.** If the user included specific issue numbers in their invocation (e.g., "grind #12 #15 #20"), use exactly those issues — skip the fetch-and-ask step entirely and go straight to step 4.

2. Otherwise, fetch the open `ready` issues (the Global Guide's *Issues* Conventions; epics, `needs-design` and the unlabelled backlog are not on the list):

```
gh issue list --state open --label ready --json number,title,body,labels \
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
- **Otherwise run it in parallel.** Touching the same files (lock files, a shared results document, a CLI entry point) is not a reason to sequence: the later PR merges `main` in and resolves, as the Guide says. The exception is files that can only be generated again, not merged (recorded model runs, under the Model calls Guide): issues that regenerate the same ones run in sequence.
- **Cap how many run at once** by what the machine can hold: each worktree builds its own environment, and the full test run's duration from Test Discovery is a guide to how heavy each agent is. When unsure, start with two or three.

Tell the user the plan in a line or two (what runs first, what waits for what). Within those constraints, start issues in worklist order — ID order, unless the user reordered them or supplied their own list. One issue at a time is still a valid plan when everything depends on everything.

## Per-Issue Loop

For each issue, the orchestrator performs a quick assessment, then delegates implementation to a sub-agent. Several issues can be in the loop at once, each at its own step.

### Step 1 — Assess (orchestrator)

Mark this issue's task `in_progress` via `TaskUpdate`. Then read the issue body and comments (`gh issue view <number> --comments`). Determine:

- **Actionable**: the issue describes a concrete change that can be implemented and tested. → Delegate to sub-agent (Step 2).
- **Already done**: the feature/fix already exists in the codebase. → Close with a comment explaining why, mark the task `completed`, move to next issue.
- **Unclear**: not enough detail to implement. → Post a comment saying what design is missing; move the issue from `ready` to `needs-design`; mark the task `completed` (it's been processed), move to next issue. Issues sequenced after it may need re-planning.

**If the Adopter keeps a register** (the Project knowledge Guide's end-state Stance), list the hypotheses an actionable issue will make Due: those whose Due mechanisms it touches, by the design's own rule. Split them by cost. **Cheap** ones are read by the full test command (the one run before committing). **Expensive** ones need anything beyond it: slow lanes, multi-seed instruments. The cheap ones go into the sub-agent's brief; the expensive ones are for the completion report. Nobody in the run defers or reads an expensive one: whether to read it now, defer it or revise the design is the owner's review, because a change deciding to defer the readings it made Due is the decision most open to Drift.

**If the issue re-records model runs** (the Model calls Guide), its brief carries a budget: which recordings, the retries per fixture, the rule for telling flake from regression, and the most it may spend. A run on an expensive model needs the owner's say before it is briefed. An issue whose criterion is to re-record "once the instructions settle" is **Unclear**: it needs splitting into a slice the owner accepts the behaviour of and a slice that records, as that Guide says.

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

[IF THE ADOPTER KEEPS A REGISTER:
## Hypotheses this change makes Due

Cheap, read by the full test command: [LIST, or "none"]. When they
pass, update their register rows (status, reading, this commit) in the
PR. If one fails under its reading rule, don't change the rule or the
test to make it pass: report it.
Expensive: [LIST, or "none"]. Don't run them and don't defer them; the
orchestrator reports them for the owner's review.]

[IF THE ISSUE RE-RECORDS MODEL RUNS:
## Re-recording budget

Recordings: [WHICH]. Retries per fixture: [N]. Spend at most [AMOUNT].
The same fixture failing the same check on every try is a regression:
stop and report it, don't change the check. Different fixtures failing
on different tries is flake: retry within the budget. Record nothing
outside the list, and no run on [EXPENSIVE MODELS].]

## How to work

You are in your own git worktree. Follow the Agentic development Guide
(~/.claude/commons/guides/agentic-development.md): in particular, catch
up with main by merging it, never rebasing; resolve conflicts hunk by
hunk, and after resolving one in prose, check that `git diff origin/main
-- <file>` removes or changes none of main's headings; and before
pushing, check that `git diff origin/main --stat` lists only this
issue's changes.

Run one shell command per call: no `cd <dir> && …`, chains, pipes into
an interpreter or heredocs. In a worktree a compound command is refused
whole, and nothing in it runs, even if the refusal reads as though the
first steps did. Write and change files with the Write and Edit tools,
and run scripts by absolute path.

## Your task

Implement this issue using strict TDD by invoking the `/tdd` skill.
You are running unattended, with no user to answer questions: apply
the Guide's Stance "decide, record, carry on".

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
   commit, push, and open a PR, each command as its own call:

   git add <specific-files>
   git commit -m "<descriptive message>

   Closes #[NUMBER]"
   git push -u origin issue-[NUMBER]-[SLUG]

   Write the PR body with the Write tool to a file named after the issue
   (`pr-body-[NUMBER].md`, since other agents are working too), outside
   the repo, e.g. in your scratchpad directory:

   ## Summary
   <1-3 bullets>

   Closes #[NUMBER]

   ## Test plan
   - <what the tests verify>

   🤖 Generated with [Claude Code](https://claude.com/claude-code)

   then: gh pr create --title "<short title>" --body-file <path to pr-body-[NUMBER].md>

5. Don't spawn agents of your own, and report back only once all your
   work has stopped. A run longer than the foreground time limit goes in
   the background; wait for its completion before reporting, never hand
   back while it runs. Name every file you write outside your worktree
   (scripts, notes, the PR body) after this issue, or keep it in a
   `[NUMBER]/` subdirectory of the scratchpad: other agents share it.

6. Don't open issues. Draft each follow-up issue you decide on (its
   full body, in the Global Guide's slice shape) to
   `followups-[NUMBER].md` in the scratchpad, and report it; the
   orchestrator opens it.

7. Report back: what you implemented, the PR number, and any problems.
   Also report anything that looked like a Lesson (the four Signals in
   ~/.claude/commons/CONTEXT.md, "Recognising a Lesson"); as a
   sub-agent you report it, you don't record it (Global Guide,
   *Lessons*). Say "none" if nothing did.
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

**A PR that comes back needing more goes back only for a fix to what its issue asked** (the Agentic development Guide, *a PR holds the change its slice asked for*). Anything further, merge what is sound and open a new issue for the rest; don't grow the PR by sending it back.

**Open the follow-up issues sub-agents drafted** (`followups-[NUMBER].md`), after checking that each isn't a duplicate of an open issue.

Record the outcome: issue number, PR number, status. Once an issue is merged, start any issue that was waiting on it.

### Step 4 — Update worklist and advance

Mark the completed issue's task `completed` using `TaskUpdate`. Start the next pending issues the plan allows, up to the cap. Do not pick issues outside the worklist. Repeat from Step 1.

## Completion

When all issues have been processed, report a summary:

- Issues implemented and merged (with PR numbers)
- Issues closed as already done
- Issues sent back to `needs-design`
- Hypotheses the run made Due and didn't read (the expensive ones, and any cheap one that failed), each with the PR that made it Due: the owner's review, before the next change
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
- **Stick to the worklist.** Only work on issues that have a task created during startup. Never add or substitute issues mid-run. Follow-ups opened during the run wait for the next one.
- **No growing send-backs.** A PR goes back to its sub-agent for a conflict or a fix to its own issue, never for a further change.
