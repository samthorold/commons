---
name: grill-with-docs
description: Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, domain docs, system design) inline as decisions crystallise. Use when user wants to stress-test a plan against their project's language and documented decisions, or to design a `needs-design` issue until it is `ready`.
---

<what-to-do>

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time, waiting for feedback on each question before continuing.

If a question can be answered by exploring the codebase, explore the codebase instead.

If the grill was about an issue ("grill #42"), end it by rewriting the issue's body as the slice contract and labelling it `ready` (the Global Guide's *Issues* Conventions), or, if it turned out to be several slices, by handing over to `/to-issues`.

</what-to-do>

<supporting-info>

## The three layers

Every meaningful project has three layers of knowledge. Two are documentation; the third is the code. Each has a different purpose and a different home. During a session, identify which layer the conversation is at and work there — don't skip layers or mix them.

### 1. Domain — the true underlying facts, rules, and dynamics

The real-world problem the system models, independent of any software. How double-entry bookkeeping works, how shipping logistics route freight, how a sport's scoring rules work. The ground truth the system design must faithfully represent. (These are illustrations — reason in whatever domain *this* project is about.)

This is not "our system's accounting module" — it's "how accounting works" as the team understands it. Written in domain language, not implementation language.

Home: `docs/{domain-area}/` (the project's own name for it — e.g. `docs/accounting/`, `docs/logistics/`).

### 2. System design — the approach any implementation must encode

Our opinion about how to model the domain: which of its rules we carry forward, which we simplify, which mechanisms are load-bearing, and what shape the system has — its concepts, relationships, constraints, and the functional forms that realise them. Implementation-agnostic: it describes the shape of the system without prescribing data structures, algorithms, or specific technologies.

This is the bridge between domain knowledge and code, and it is where **design rationale lives**. A system-design doc explains not just *what* the design is but *why* it is that way — including why tempting alternatives don't work — as a standing property of today's design (see "Self-justifying system design" below).

Home: `docs/` or `docs/system-design/`.

### 3. Implementation — the code

The code is the encoding of the system design. There is no separate documentation layer for it: if a fact lives in the code, the code is its home. The implementation should trace its shape back to the system design, not restate it.

### The ubiquitous language underpins all three → `CONTEXT.md`

The glossary is not a fourth layer — it's the precise shared vocabulary the three layers are written in. What terms mean in this project, with no implementation, no design, and no decisions. Just language.

Use the format in [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md).

## There is no decision-record layer

Resist the urge to record decisions as standalone artifacts (ADRs, decision logs, "we chose X over Y" files). They are not one of the layers, and this skill does not create them.

The one thing a decision record legitimately captures is **why** something is the way it is. That belongs inside the **system-design** layer, written in the present tense — not in a separate chronological store. A reader should understand why today's design looks the way it does from the design doc alone, without reconstructing a trail of superseded choices.

When you find yourself wanting to write "we decided X over Y because Z," treat it as a signal that the **system-design doc is under-explaining the present**. Fold the *why* into the design doc itself — including why the tempting alternative Y fails — and let version control hold the chronology. If you need a history of decisions to understand why something exists the way it does today, the present documentation is insufficient; fix that, don't start a decision log.

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

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible — which is right?"

### Update docs at the right layer

When something is resolved, update the appropriate layer immediately — don't batch. But only update one layer per resolution:

- A term clarified → update `CONTEXT.md`
- A domain fact understood → update `docs/{domain-area}/`
- A system-level concept, mechanism, functional form, or its rationale settled → update the system-design layer
- An implementation detail decided → it belongs in the code, not in a doc

`CONTEXT.md` should be totally devoid of implementation details. Do not treat it as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

### Self-justifying system design

Most resolutions in a design grilling land in the **system-design** layer, because that's where mechanisms, functional forms, and the reasoning behind them live. When you write or update a system-design doc, make it self-justifying: describe the present design *and the reasons it has that shape*, in the present tense.

A good system-design doc answers "why is it this way?" on its own:

- State the mechanism and its functional form as they stand today.
- Explain why the design has this shape — the constraint, property, or domain fact that forces it.
- Where a reader would reasonably expect a different (often simpler or more obvious) approach, explain why that approach fails — as a standing property of the design, not as a dated "we rejected X" note.

What this is **not**: a chronology of how the design evolved, a list of superseded mechanisms, or a "considered options" log. Describe the destination, not the journey. If the design changes later, the doc changes to describe the new present — the old version lives in version control.

See [SYSTEM-DESIGN-FORMAT.md](./SYSTEM-DESIGN-FORMAT.md) for what belongs in this layer and how to write it.

</supporting-info>
