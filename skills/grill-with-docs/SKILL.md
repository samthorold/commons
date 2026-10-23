---
name: grill-with-docs
description: Grilling session about a plan that belongs to a repo: challenges it against the repo's language, domain and system design (and its Archetype's Guide), and writes what's settled into CONTEXT.md and the design docs inline. Use when user wants to stress-test a project's plan or design, or to grill a `needs-design` issue until it is `ready`. For a plan with no repo docs to write into, use grill-me.
---

<what-to-do>

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time, waiting for feedback on each question before continuing.

If a question can be answered by exploring the codebase, explore the codebase instead.

If the grill was about an issue ("grill #42"), end it by rewriting the issue's body as the slice contract and labelling it `ready` (the Global Guide's *Issues* Conventions), or, if it turned out to be several slices, by handing over to `/to-issues`.

At the end of the session, run a Lesson pass (Global Guide, *Lessons*): did anything settled here contradict a Guide, depart from one, or fill a Gap that another project of the same Stack or Archetype would face?

</what-to-do>

<supporting-info>

## The layers

What the layers are, and why there is no decision-record layer and system design justifies itself, is the **Project knowledge Guide** (`~/.claude/commons/guides/project-knowledge.md`, Imported into every session). This skill is the Procedure that writes them; where they seem to disagree, the Guide wins. Formats: [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md) for `CONTEXT.md`, [SYSTEM-DESIGN-FORMAT.md](./SYSTEM-DESIGN-FORMAT.md) for system design.

## Working at one layer at a time

When a grilling question touches something fundamental, resist jumping to a conclusion. Figure out which layer is unsettled and work there first.

**Zoom-out signals** — the conversation needs to move to a higher layer:

- A term is being used inconsistently or vaguely → the language (`CONTEXT.md`)
- The discussion reveals a misunderstanding about how the real-world domain works → the domain layer
- The system's shape, a mechanism, or a functional form doesn't match the domain model → the system-design layer

**Zoom-in signals** — the conversation is ready to move to a lower layer:

- Language is precise and shared → move past the glossary
- Domain behaviour is understood and documented → move past the domain layer
- System shape is clear and justified → it's ready to be encoded in the implementation

When you notice a zoom-out signal, say so: "Before we decide X, I think we need to settle Y at the domain level." Don't update multiple layers in a single exchange.

## Domain awareness — conform to the project's existing layout

During codebase exploration, find the existing documentation and **conform to where this project already keeps each layer** rather than imposing a fixed structure. If a doc already defines the layer contract (e.g. a `docs/system-design/README.md` or a docs index), read it and honour it.

Most repos have a single context:

```
/
├── CONTEXT.md
├── docs/
│   ├── {domain-area}/       ← domain knowledge
│   └── system-design/       ← system design (may just be docs/ itself)
└── src/                      ← implementation
```

If a `CONTEXT-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:

```
/
├── CONTEXT-MAP.md
├── docs/
│   ├── {domain-area}/                   ← domain knowledge
│   └── system-design/
├── src/
│   ├── ordering/
│   │   └── CONTEXT.md
│   └── billing/
│       └── CONTEXT.md
```

Create files and directories lazily — only when you have something to write. Match the project's existing naming and structure; don't invent a parallel layout beside one that already exists.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `CONTEXT.md`, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account' — do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Challenge against the Archetype's Guide

The project's Archetype Guide (e.g. for discrete event simulation), where there is one, says how systems of this shape are generally approached, whatever the Stack. When the design departs from one of its Stances, say so: "The Guide's Stance is X; you're proposing Y — is this a Deviation?" A departure the owner keeps is recorded as a Deviation, with its reason, in the repo's `CLAUDE.md`. If the project's cell has no Archetype Guide yet, a decision another project of the same shape would face is a Gap (`~/.claude/commons/CONTEXT.md`, *Recognising a Lesson*).

### Challenge against the end state

The design states its end state as hypotheses (the Project knowledge Guide's Stance; format in [SYSTEM-DESIGN-FORMAT.md](./SYSTEM-DESIGN-FORMAT.md)). Start from the register's Due rows, not from the last result. Then, as the session goes:

- A new mechanism: "Which part of the end state does this serve?" One that serves none is there for a local reason.
- A new hypothesis: what's its source, its test, its reading rule (supported, refuted, undecided, with the error) and its review interval? One with no source is a candidate to drop.
- A changed threshold, panel or instrument: is the design changing with it? If not, it's Drift. Say so: "That moves the line after the reading — what in the design changed?"
- A design with no end state yet: the session that writes one starts from what the design already maps (phenomena to mechanisms, features to components), takes hypotheses and ranges from the domain, and leaves every register row Due.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible — which is right?"

### Update docs at the right layer

When something is resolved, update the appropriate layer immediately — don't batch. But only update one layer per resolution:

- A term clarified → update `CONTEXT.md`
- A domain fact understood → update `docs/{domain-area}/`
- A system-level concept, mechanism, functional form, or its rationale settled → update the system-design layer
- An implementation detail decided → it belongs in the code, not in a doc

`CONTEXT.md` should be totally devoid of implementation details. Do not treat it as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

### Write system design self-justifying

Most resolutions land in the system-design layer. Write them as the Guide's Stance *system design justifies itself* says, in the present tense, using [SYSTEM-DESIGN-FORMAT.md](./SYSTEM-DESIGN-FORMAT.md). Domain claims go in only once grounded in sources (the Guide's *domain claims come from sources, not recall*).

</supporting-info>
