# Commons: ubiquitous language

The vocabulary for knowledge shared across projects. Use these terms, and only these, when talking or writing about it; the "Avoid" lines list synonyms that blur them.

## The Commons

**Commons**: the whole body of shared knowledge that projects draw on and contribute back to. It lives in this repo.
*Avoid:* meta information, common knowledge, common approach, playbook.

The Commons holds approach only. Which projects exist, how they group and where they are heading is the **Portfolio** (see below), kept elsewhere.

## Kinds of knowledge, and their artefacts

| Kind | What it is | Artefact |
|---|---|---|
| **Convention** | A checkable rule whose reason is short or obvious. | A rule in a Guide. |
| **Stance** | A design position that needs judgement to apply. | An entry in a Guide, always shaped: stance / why / how to apply / what would change our mind. |
| **Known trap** | A warning about something that behaves surprisingly and can't (yet) be designed away. | An entry in a Guide's *Known traps*: the trap, what to do instead, and *remove when*. |
| **Procedure** | How to carry out a kind of task. | A Skill (a `SKILL.md` directory). One Procedure, one Skill. |
| **Lesson** | Something learned in one Adopter that may hold more widely, not yet settled. | A Lesson file in `lessons/` (see `lessons/README.md`). |

**Guide**: a document holding the Conventions and Stances for one Scope. It always states current truth; history lives in git. Write each Stance so that breaking it is recognisable: its one-line *why* is what lets an agent notice a situation where the reason no longer holds.

**One home per rule.** A Guide doesn't restate another Guide: where a rule spans Scopes, it lives in the broadest Guide it holds for, and a narrower Guide supplies only its own facts (e.g. the Stack Guide says which PR publishes a release; the Agentic development Guide says whether it may merge). A copy drifts from its original unseen.

**Skill**: the artefact for a Procedure. A Skill that depends on a Stance links to its Guide rather than restating it. "Skill" names the artefact only, never the knowledge.

**Known traps are the weakest fix.** An Imported trap costs context in every session, so a trap should move up this ladder whenever it can, and leave the Guide when it reaches the top:

1. **Eliminate**: fix the cause (the tooling, the upstream bug), so the trap can't happen.
2. **Automate**: a hook, a CI check, or a step in a Skill catches it.
3. **State it positively**: a Convention or Stance says what to do.
4. **Known trap**: "watch out for X", for what can't be designed away, usually something external behaving oddly.

Every Known trap ends with **remove when**: the condition under which it stops being true or stops being needed (e.g. an upstream fix ships, or a Skill step makes it redundant). It is to a trap what *what would change our mind* is to a Stance. Removing a trap, or moving it up the ladder, is a Revision.

A Stance can point to a choice on another axis (e.g. "discrete event simulation → Rust"). It is still just a Stance; if agents wouldn't reach for that choice unprompted, the Commons isn't clear enough yet.

## Scope: the matrix

Scope has two independent dimensions, and they combine.

- **Stack**: a language or tool ecosystem, including combinations (Python, Rust, Python+Rust).
- **Archetype**: the shape of a system, whatever its subject (discrete event simulation, game search).
- **Global**: every Stack and every Archetype.
- **Local**: one Adopter only. Local knowledge stays in that Adopter's own docs, not in the Commons.

Each Guide is pinned to a cell, a row or a column of the Stack × Archetype matrix. Several Guides may share a Scope, each on its own topic: the Global Guide and the Agentic development Guide are both any × any. A topic is not a third dimension; Scope still says only which Adopters a Guide applies to. An Adopter's Guides are every Guide whose row or column covers its cell.

**Map**: one line per Guide giving its name and Scope (`MAP.md`). Always loaded, and tiny: it lets an agent address a Lesson and see when its cell has no Guide.

## Adopters

**Adopter**: a project, *or a component of one*, that follows a Guide. A single repo can hold several Adopters (e.g. the search code and each game in a games repo).

**Adoption**: an Adopter's declaration that it follows a Guide: the Import line in its `CLAUDE.md`. Adoptions live in the Adopters, not in the Commons, so the Commons keeps no list of projects. To find a Guide's Adopters, search for its Import.

**Deviation**: a *recorded* departure from a Guide, with its reason, in the Adopter's `CLAUDE.md`.

**Drift**: an *unrecorded* departure from something declared. Two cases:
- For an Adopter and the Commons: a gap where the Adopter is behind a Guide. (Recorded, it is a Deviation.)
- For a system design: a declared value (a reading rule, an instrument, a review interval) that changed without a change to the system design. (With one, it is part of revising the end state; see *End states and hypotheses*.)

Drift is a state you observe, not a work item; what an Adopter does about it is its own workflow.

## Channels: how knowledge reaches an agent

| Channel | Artefact | When it loads |
|---|---|---|
| **Import** | An `@~/.claude/commons/...` line in a `CLAUDE.md`. | Always, when working in that Adopter. Resolves only on this machine. |
| **Trigger** | The `description` in a Skill's frontmatter. | When the task matches. |
| **Reference** | A plain link in a `CLAUDE.md` or doc (local path or GitHub URL). | When an agent chooses to follow it. Works anywhere, since this repo is public. |

Context comes in three layers: the **Map** (always), the Adopter's own Guides **condensed** (Imported), and **detail** (behind References, read when needed).

## Flow: how the Commons changes

| Term | Direction | Meaning |
|---|---|---|
| **Propagation** | Commons → Adopters | A Guide changed; bring its Adopters back in line. Found through their Imports. |
| **Promotion** | Adopter → Commons | A Lesson becomes a Convention or Stance in a Guide (or a new Guide). |
| **Revision** | Within the Commons | A Stance, Convention or Known trap changes (or goes); the reason goes in the commit message. |

The two links: a **Lesson → its Address → a Guide** (upward), and a **Guide Revision → Imports → Adopters** (downward).

**Sweep**: the work that finds what no longer needs to be where it is, and removes it: Lessons waiting for Promotion, Known traps whose *remove when* is met or that can move up the ladder, an Adopter's Local copy of knowledge a Guide now holds, and Drift. It runs as a recurring review (`lessons/README.md`). An **idle sweep** is one slice of it, done by an agent while it waits on a background process, and only reported (Agentic development Guide, *Idle sweeps*).
*Avoid:* pruning, cleanup.

### Recognising a Lesson

Four **Signals**, each needing only the context an agent already has:

- **Contradiction**: following a Convention or Stance was wrong or not enough here.
- **Deviation**: a Deviation was recorded. Always a candidate.
- **Gap**: a decision the Adopter's own Guides didn't cover, which another Adopter would face too. (Whether some *other* Guide covers it is for the Promoter to check.)
- **Trap**: something cost time, and the cause isn't specific to this Adopter. (Once promoted it becomes a Known trap, or better, something higher up the ladder.)

The filter: *would this hold for another Adopter in the same cell, row or column?* If not, it's Local. The **Address** is the narrowest Guide whose Scope explains why the Lesson is true; if nothing fits, the Gap may be a missing Guide.

Detection is best done as a separate pass at a natural checkpoint (e.g. the end of a PR) rather than continuous vigilance. Missing a Lesson is cheap, because a real one recurs; a false one is filtered at Promotion.

## End states and hypotheses

How an Adopter's system design says where it is going when that can't be known for sure.

**End state**: what the system is meant to become, as its system design states it now. Always uncertain. It moves only when a hypothesis resolves, and only as a change to the system design.
*Avoid:* goal, target, vision.

**Hypothesis**: something a part of the end state rests on that isn't known to hold yet. The system design states it in the present tense, with no status. It names the part of the end state it hangs from, and it has its own test.
*Avoid:* belief, claim, assumption.

**Reading rule**: what a hypothesis's test must show for the hypothesis to be *supported*, *refuted* or *undecided*, including how it treats the instrument's error. It is declared before any reading it judges.
*Avoid:* threshold, success criterion.

**Reading**: one run of a test, judged by the reading rule in force when it ran, and true of the implementation it ran on. A reading stands alone: it isn't pooled with an earlier undecided one to reach a status.

**Due**: a hypothesis that needs a reading. Either it has none under its current reading rule, its review interval (*N*) has passed, or what it was read on has changed. Due hypotheses are reviewed before any other change: read now, deferred with a reason, or the design revised.

**Register**: the status of every hypothesis (supported, refuted, undecided, due), with its last reading. It is kept apart from the domain and the system design, and derived from tests and readings rather than written by hand. Status lives here and nowhere else. *Supported* means only that the hypothesis has survived its tests so far.

## The Portfolio (outside the Commons)

**Portfolio**: all the projects together. **Group**: a thematic cluster of projects (e.g. games and search; models of real-world systems). **Direction**: where the Portfolio and its Groups are heading. Groups exist for thinking about Direction; Archetypes exist for sharing approach; the two cut across each other. The Portfolio lives in the private `portfolio` repo.
