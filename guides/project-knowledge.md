# Project knowledge Guide

**Scope:** every Stack, every Archetype. The topic is where an Adopter keeps what it knows: its language, its domain, its design and its code, and what never gets written down separately.

Each Stance's *How to apply*, and the Conventions and Known traps for research, live in files under `~/.claude/commons/guides/project-knowledge/`, and each section says when to read its file. Links are relative to this file.

## Stance: durable knowledge goes in source control, not private memory

- **Stance:** anything worth remembering across sessions (workflow, runtimes, known traps, vision, how to work on the project) goes in the repo's `CLAUDE.md` or the docs it points to, never only in an agent's auto-memory. Knowledge that would hold for other projects goes to the Commons as a Lesson, not only into the project's own docs.
- **Why:** private memory isn't committed, reviewed or visible, and drifts out of date unseen.
- **How to apply:** before writing a memory file or a handoff document, read [durable knowledge](project-knowledge/durable-knowledge.md).
- **What would change our mind:** a harness whose memory is versioned and reviewable like the repo.

## Stance: three layers, written in one language

- **Stance:** an Adopter's knowledge has three layers, each with one home:
  - **Domain**: the real-world facts, rules and dynamics the system models, independent of any software. Home: `docs/<domain-area>/` (the project's own name, e.g. `docs/ecology/`).
  - **System design**: our opinion about how to model the domain (which rules we carry forward or simplify, which mechanisms are load-bearing, the concepts, relationships and functional forms), implementation-agnostic. Home: `docs/system-design/` (or `docs/`).
  - **Implementation**: the code. There is no documentation layer for it: if a fact lives in the code, the code is its home.

  Underneath all three is the **ubiquitous language**, `CONTEXT.md` (or a `CONTEXT-MAP.md` pointing to one per context): what terms mean, with no design, implementation or decisions in it.
- **Why:** each layer changes for a different reason, so mixing them makes every change touch everything.
- **How to apply:** before writing to an Adopter's `CONTEXT.md` or docs, or creating a docs file, read [three layers](project-knowledge/three-layers.md).
- **What would change our mind:** a project with no domain beyond the software itself (a pure tool), where the domain layer stays empty; that's expected, not a Deviation.

## Stance: there is no decision-record layer

- **Stance:** no ADRs, decision logs or "we chose X over Y" files, and no decisions recorded in issues as the design's home. The *why* of the design lives in the system-design docs, in the present tense.
- **Why:** a decision record is a chronology, from which a reader has to reconstruct today's design out of superseded choices.
- **How to apply:** when about to write "we decided X over Y", or when the design changes, read [no decision records](project-knowledge/no-decision-records.md).
- **What would change our mind:** a decision that has to be audited as of a date (a regulatory or contractual record), which a present-tense doc can't serve.

## Stance: system design justifies itself

- **Stance:** a system-design doc states each load-bearing mechanism as it is today, why it has that shape (the domain fact or constraint that forces it), and why the obvious alternative fails, as a standing property of the design.
- **Why:** an agent that doesn't know why a shape is load-bearing will simplify it away.
- **How to apply:** before writing or revising a system-design doc, read [system design](project-knowledge/system-design.md).
- **What would change our mind:** design docs that grow so long agents stop reading them; then split by area, but keep the present tense.

## Stance: the system design states its end state as hypotheses

- **Stance:** the system design states the end state and the hypotheses each part of it rests on (vocabulary: `~/.claude/commons/CONTEXT.md`, *End states and hypotheses*). Each hypothesis has its own test, and its reading rule and review interval are stated beside it in the system design; the test implements the rule. Status lives in a register derived from readings, never in the design.
- **Why:** an end state is never certain, and without rules declared before the readings a project drifts into local optimisation, each step judged against the last result.
- **How to apply:** before declaring, revising or reading a hypothesis (its reading rule, its test), or building the register or how it learns what changed, read [end state](project-knowledge/end-state.md).
- **What would change our mind:** registers that can't stay derived, for instance expensive instruments whose stored outputs go stale. Or reviews that cost more than the Drift they catch.

## Stance: domain claims come from sources, not recall

- **Stance:** every claim in the domain layer is grounded in sources first, cited, with a note of evidence quality: what was read in full, what only as an extract (a fetch tool's answer about a page, with the cited passages quoted, not the page read line by line) or an abstract, what was recalled rather than read, and what the sources leave open. Only then is it carried into the design.
- **Why:** an agent's own reading of how the world works is fluent and often wrong, and a design built on it inherits the error with no trail back to check.
- **How to apply:** before writing a domain claim, or offering categories in a design (an enum of roles, kinds or statuses), read [domain claims](project-knowledge/domain-claims.md); before briefing research, read [research](project-knowledge/research.md).
- **What would change our mind:** a domain the project defines itself (a game's rules), where the rules are the source.

## Research lands as an opinion and a signpost

- **Before briefing or running research (researchers, a deep-research run, web fetches), or deciding what of its output to keep, read [research](project-knowledge/research.md).** It decides how a brief is written, that research lands as an opinion at its layer with a signpost to its sources while its working folders go uncommitted, and holds the Known traps of a research agent's web tools.

## Lessons

If something in this Guide proves wrong or incomplete while you work, record a Lesson addressed to it (to the Stance's detail file, where the Lesson is about how to apply it), as described in `~/.claude/commons/lessons/README.md`.
