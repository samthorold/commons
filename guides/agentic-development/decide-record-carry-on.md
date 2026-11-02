# Agentic development Guide: decide, record, carry on

How to apply the Stance *decide, record, carry on*, from [the Agentic development Guide](../agentic-development.md#stance-decide-record-carry-on), which states the Stance.

## Why, in full

The owner delegates heavily. A question that waits for an answer stalls the run, while a recorded call costs at worst one revert. Git and PR history is the one chronological record an Adopter keeps (its docs state only the present), so it is where a later agent looks for why a change was made; a call recorded there is found, a call made silently is not.

## How to apply

- wherever a Skill says to confirm with the user or get their approval, decide and record when nobody is answering. With the owner present, still give the recommendation, as the default the agent will act on unless corrected, not as a blocking question. Skills whose purpose is the interview (`grill-me`, `grill-with-docs`) are exempt. A call that shapes the design doesn't stay only in history: its *why* also goes into the system-design docs, in the present tense.
- **Gates:** the owner's say gates expense, not acceptance: a spend beyond what the brief grants, an expensive run. Merges are gated only by the repo's grant of merge authority. Where a change's acceptance needs judgement, the judgement is declared as a criterion when the work is written (in its grill), and the agent reads the criterion and carries on; holding work for the owner's verdict is the fallback when no criterion can be declared, and a sign the instructions have a gap. What the owner should still see (review cases, a report) goes where they will read it, without blocking.
