# Project knowledge Guide

**Scope:** every Stack, every Archetype. The topic is where an Adopter keeps what it knows: its language, its domain, its design and its code, and what never gets written down separately.

## Stance: durable knowledge goes in source control, not private memory

- **Stance:** anything worth remembering across sessions (workflow, runtimes, known traps, vision, how to work on the project) goes in the repo's `CLAUDE.md` or the docs it points to, never only in an agent's auto-memory. Knowledge that would hold for other projects goes to the Commons as a Lesson, not only into the project's own docs.
- **Why:** private memory isn't committed, reviewed or visible, and drifts out of date unseen.
- **How to apply:** update the docs instead of writing a memory file. A handoff document (the `handoff` Skill) is transient by design: before writing one, make sure anything durable is already in a commit, a doc or an issue.
- **What would change our mind:** a harness whose memory is versioned and reviewable like the repo.

## Stance: three layers, written in one language

- **Stance:** an Adopter's knowledge has three layers, each with one home:
  - **Domain**: the real-world facts, rules and dynamics the system models, independent of any software. Home: `docs/<domain-area>/` (the project's own name, e.g. `docs/ecology/`).
  - **System design**: our opinion about how to model the domain (which rules we carry forward or simplify, which mechanisms are load-bearing, the concepts, relationships and functional forms), implementation-agnostic. Home: `docs/system-design/` (or `docs/`).
  - **Implementation**: the code. There is no documentation layer for it: if a fact lives in the code, the code is its home.

  Underneath all three is the **ubiquitous language**, `CONTEXT.md` (or a `CONTEXT-MAP.md` pointing to one per context): what terms mean, with no design, implementation or decisions in it.
- **Why:** each layer changes for a different reason (the world is understood better; the model changes; the code is refactored), so mixing them makes every change touch everything. A shared language keeps the layers, the issues, the tests and the conversation saying the same thing.
- **How to apply:** work at one layer at a time, and write each fact once, at its layer, referencing the others rather than restating them. Create files lazily, only when there is something to write, and conform to the layout a repo already has. The `grill-with-docs` Skill is the Procedure that writes these layers; its `CONTEXT-FORMAT.md` and `SYSTEM-DESIGN-FORMAT.md` are the formats.
- **What would change our mind:** a project with no domain beyond the software itself (a pure tool), where the domain layer stays empty; that's expected, not a Deviation.

## Stance: there is no decision-record layer

- **Stance:** no ADRs, decision logs or "we chose X over Y" files, and no decisions recorded in issues as the design's home. The *why* of the design lives in the system-design docs, in the present tense.
- **Why:** a decision record is a chronology; to understand today's design from it, a reader reconstructs a trail of superseded choices, and records drift from the design they describe. The chronology already exists in git and PR history (see the Agentic development Guide's *decide, record, carry on*).
- **How to apply:** wanting to write "we decided X over Y because Z" signals that the system-design doc under-explains the present: fold the reason, including why Y fails, into the doc. When the design changes, rewrite the doc to describe the new present.
- **What would change our mind:** a decision that has to be audited as of a date (a regulatory or contractual record), which a present-tense doc can't serve.

## Stance: system design justifies itself

- **Stance:** a system-design doc states each load-bearing mechanism as it is today, why it has that shape (the domain fact or constraint that forces it), and why the obvious alternative fails, as a standing property of the design.
- **Why:** a newcomer, human or agent, should understand from the doc alone both what the design is and why it must be so, without asking "why didn't they just…?". An agent that doesn't know why a shape is load-bearing will simplify it away.
- **How to apply:** no chronology, no "considered options" log, no status or dates. A rejected feature request that is worth remembering goes here, as part of why the design has its shape (the issue is closed as *not planned*). Parameter values belong with the code, not here. A reading rule's declared values (its range, panel, review interval) are not parameters: they belong with the rule, in the design.
- **What would change our mind:** design docs that grow so long agents stop reading them; then split by area, but keep the present tense.

## Stance: the system design states its end state as hypotheses

- **Stance:** the system design states the end state and the hypotheses each part of it rests on (vocabulary: `~/.claude/commons/CONTEXT.md`, *End states and hypotheses*). Each hypothesis has its own test, and its reading rule and review interval are stated beside it in the system design; the test implements the rule. Status lives in a register derived from readings, never in the design.
- **Why:** an end state is never certain. A mature project then drifts into local optimisation, each step judged against the last result instead of against where the work is going. Declaring rules before the readings makes that Drift visible as a declared value that changed with no design change. Status kept in the design would turn the design into a chronology.
- **How to apply:**
  - Where the domain is sourced, a hypothesis is a domain phenomenon the model should reproduce, and its rule uses the domain's empirical range (supported inside it, refuted wholly outside, undecided if it straddles), citing the number rather than restating it. A threshold of our own is set only where the sources give none, and a hypothesis no source supports is a candidate to drop: unsourced hypotheses are the ones that drift.
  - Tests stay in the suite whatever the status. A status holds only for the implementation it was read on.
  - A refuted hypothesis changes the system design, and that change is how the end state is revised. Declared values change only together with such a change.
  - A reading declares its size or its stopping rule before it runs, as part of its reading rule. A reading that leans one way without crossing its line is undecided: read again on fresh runs, judged alone, or use a sequential rule that keeps going until it crosses a declared bound. Adding runs to the same reading until it crosses the line is not a reading.
  - A reading rule says the window it reads over and the points it is read at (back-to-back windows from a stated start, the latest ended window giving the status). A register derived on every view keeps no memory of when it last read, and fixed points stand in for that memory. A rule read over the whole history ("refuted by any missed day") is refuted for good by one bad day.
  - A derived register learns from outside that what a hypothesis was read on has changed: a running system can't see a change to its own code. Feed the change in (commit history through an admin command, marking the paths the design names), and name in the design any change made only through configuration (switching a model), which commits don't show.
  - Between revisions, grain only gets finer. A hypothesis may be replaced by finer ones under the same part of the end state. A replacement that goes up a grain or sideways is a design change.
  - A link means relevance, not sufficiency. Supported children don't make their parent supported: the parent is resolved only by its own test.
  - Tests near the top are often cheap, coarse necessary conditions (e.g. "a game against a mock human ends in under ten minutes"). They can refute but not confirm, and they run on every change.
  - A supported hypothesis doesn't move into the domain layer. Domain facts come from sources about the world.
- **What would change our mind:** registers that can't stay derived, for instance expensive instruments whose stored outputs go stale. Or reviews that cost more than the Drift they catch.

## Stance: domain claims come from sources, not recall

- **Stance:** every claim in the domain layer is grounded in sources first, cited, with a note of evidence quality: what was read in full, what only from abstracts, what was recalled rather than read, and what the sources leave open. Only then is it carried into the design.
- **Why:** an agent's own reading of how the world works is fluent and often wrong, and a design built on it inherits the error with no trail back to check.
- **How to apply:** don't offer "my read" of the domain as a reason for a design choice. The categories a design offers (an enum of roles, kinds or statuses in a schema) are domain claims too: categories from recall carry their errors into every part built on them. Where the literature is silent, say so, and settle the gap by a reading set in advance across the range the domain allows. Note also where the sources disagreed with recall: it is the one thing research adds over the model's weights, and nothing else will catch it. Brief research from the owner's question, not from a working hypothesis: the categories, candidate answers and framing collected so far stay out of the brief, or the research echoes them back as findings and can no longer say whether the framing was right. Delegated researchers, who see only the brief, are the most prone to this. Research that only confirms recall usually means a brief written from recall; the remedy is the brief, not skipping research.
- **What would change our mind:** a domain the project defines itself (a game's rules), where the rules are the source.

## Research lands as an opinion and a signpost

What lasts from research is the opinion, not a summary of the readings. A summary mostly repeats what an agent would recall anyway, and loaded into context it dilutes the Stances that carry the value. So research lands as a Stance or other opinion at its layer (domain findings in the domain docs, measurements and project-specific analysis in `docs/research/<issue>-<slug>.md`, design in system design through a grill), with a signpost to its grounding: the sources and the evidence notes the Stance above asks for.

Research outputs (deep-research `research_notes/` and `reports/`, scratch runs) are working folders, not committed, and deleted once the opinion and its signpost have landed. The exception is a question that stays open across sessions: its outputs are committed beside the question, each pass labelled with how it was briefed, until a Stance exists to carry them.

## Lessons

If something in this Guide proves wrong or incomplete while you work, record a Lesson addressed to it, as described in `~/.claude/commons/lessons/README.md`.
