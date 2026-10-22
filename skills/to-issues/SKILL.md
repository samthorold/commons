---
name: to-issues
description: Break a settled plan into independently-grabbable issues using tracer-bullet vertical slices, under an epic when there is more than one. Use when user wants to convert a plan, spec or PRD into issues, create an epic or implementation tickets, or break down work into issues, typically right after a grill.
---

# To Issues

Break a plan into independently-grabbable issues using vertical slices (tracer bullets). This is the step after a grill: the grill has already written the design into the repo's docs, so the issues point at it rather than restating it.

Issues, their states (`ready`, `needs-design`) and the slice body follow the Global Guide's *Issues* Conventions, unless the repo's `CLAUDE.md` records a Deviation.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes an issue reference (issue number, URL, or path) as an argument, fetch it from the issue tracker and read its full body and comments.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Issue titles and descriptions should use the project's domain glossary vocabulary, and respect the documented system design (`docs/system-design/`) in the area you're touching.

### 3. Draft vertical slices

Break the plan into **tracer bullet** issues. Each issue is a thin vertical slice that cuts through ALL integration layers end-to-end, NOT a horizontal slice of one layer.

Each slice is `ready` (can be implemented and merged with no further design) or `needs-design` (needs a grill with the owner first, e.g. an unsettled architectural question). Prefer `ready`: a slice that needs design usually means the plan isn't settled yet.

<vertical-slice-rules>
- Each slice delivers a narrow but COMPLETE path through every layer (schema, API, UI, tests)
- A completed slice is demoable or verifiable on its own
- Prefer many thin slices over few thick ones
</vertical-slice-rules>

### 4. Present the breakdown

Present the proposed breakdown as a numbered list. For each slice, show:

- **Title**: short descriptive name
- **State**: `ready` / `needs-design`
- **Blocked by**: which other slices (if any) must complete first
- **User stories covered**: which user stories this addresses (if the source material has them)

Check, and invite the owner to correct: is the granularity right (too coarse / too fine)? are the dependencies right? should any slices be merged or split? are the right slices `needs-design`? Following the Agentic development Guide's *decide, record, carry on*, the breakdown is your default: publish it unless corrected.

### 5. Publish the epic (more than one slice only)

A plan with more than one slice gets an epic (Global Guide, *Issues*): a parent that says what the feature is for and ties the slices together. One slice needs no epic. If the plan came from an existing issue, that issue becomes the epic: retitle it and remove its state label.

<epic-template>
Title: `Epic: <feature>`

## Problem

The problem, from the user's perspective.

## Who it's for

A numbered list of user stories ("As an <actor>, I want <feature>, so that <benefit>"), covering the whole feature. The slices are checked against these.

## Design

Links to the system-design (and domain) docs the grill wrote. Don't restate them, and don't record decisions here: a decision that isn't in the docs yet goes into them first, in the present tense.

## Out of scope

What the feature deliberately doesn't do. If it's a standing property of the design, it belongs in the system-design docs instead.

## Slices

Filled in once the slices are published.
</epic-template>

### 6. Publish the slices

For each slice, publish a new issue using the template below, labelled with its state.

Publish issues in dependency order (blockers first) so you can reference real issue identifiers in the "Blocked by" field.

<issue-template>
## Parent

A reference to the epic (omit if there is none).

## What to build

A concise description of this vertical slice. Describe the end-to-end behavior, not layer-by-layer implementation.

Avoid specific file paths or code snippets — they go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it here and note briefly that it came from a prototype. Trim to the decision-rich parts — not a working demo, just the important bits.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Out of scope

What this slice deliberately doesn't do, so the implementer doesn't gold-plate into neighbouring slices.

## Blocked by

- A reference to the blocking ticket (if any)

Or "None - can start immediately" if no blockers.

</issue-template>

Then list the slices in the epic's *Slices* section. Never close the epic: it closes when its last slice does.
