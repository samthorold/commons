# Model calls Guide

**Scope:** Archetype = apps whose acts call a language model, any Stack. An **act** is a piece of the app's work done by a model call: its instructions, the input it is shown, the output schema it answers in and the checks its output must pass before anything is written back. An app is in this Archetype when behaviour that matters comes from a model's judgement at run time. Like an emergent system's, that behaviour is observed by running it, not derived from the code; unlike one, it comes from a component the project neither owns nor can inspect, and every run of it costs money.

Code around an act (parsing, checks, storage, the loop that drives a conversation) is ordinary code under the Agentic development Guide's test-first Stance. This Guide says how that Stance applies to the act itself, and how the act's inputs are shaped. How hypotheses about the end state are declared and read is the Project knowledge Guide's end-state Stance.

## Stance: models sit behind a port, and are chosen by measurement

- **Stance:** each act calls a provider-neutral port (one call, a batch, a conversation turn), and the provider's SDK and types stay inside its adapter. The model each act runs on is config, chosen per act by measuring candidates on the act's own fixtures, not by reputation.
- **Why:** models change faster than the app: new versions ship, prices move, and one act's best model isn't another's. An act that knows its provider can't be measured against another one. The agent advising on the choice is itself one vendor's model, and a vendor-specific skill may supply that vendor's prices and defaults. Its framing then drifts toward that vendor (comparisons within one line-up, recalled terms presented as fact), and nothing in the conversation corrects it.
- **How to apply:** research the options from sources (Project knowledge Guide, *domain claims come from sources*), with a brief that names no vendor and asks for even-handedness, and put several vendors on the shortlist, open-weight and closed. One adapter is fine while measurement favours one provider: the port is what keeps the choice open. Pin the model version an act runs on, so a provider's silent upgrade can't change behaviour between two readings.
- **What would change our mind:** an act that depends on a feature only one provider has, where the port would have to pretend otherwise. The act then names the provider in the design, and says why.

## Stance: three tiers, and the suite never pays for a call

- **Stance:** an act is tested in three tiers.
  1. **A fake model, injected at the port**, for everything around the call: typed results, the checks before anything is written back, tracing, errors and retries. Fast, deterministic, written test-first.
  2. **Recorded runs**: the real model is called on committed fixtures, its responses are kept, and the suite replays them, asserting properties of the outputs (never exact text). Only recording costs money; it is done deliberately, never by the suite.
  3. **Judgement quality is a hypothesis**, read in use (from the owner's feedback, say), not something CI asserts.
- **Why:** a suite that calls a model is slow, costs money on every run and isn't deterministic, so it stops being run. A suite that only fakes the model never sees what a real one does with the instructions. Asserting exact text breaks on every re-recording without saying anything about whether the act works.
- **How to apply:**
  - Fixtures are material the repo may hold. Material the app may read but not store or redistribute can't be a committed fixture.
  - Make fixtures by the production path (the same collection, the same truncation), or check that they match it. A fixture richer than what production collects lets a property pass on input the model is never given in use, and nothing fails to say so.
  - A property that relies on a case appearing (a reaction, a piece of feedback) names the fixture it needs, hand-made from admissible material, and asserts that the case is present. Otherwise a re-recording that drops the case leaves the property testing nothing.
- **What would change our mind:** models cheap and deterministic enough to call in the suite, which would make tier 2 a live test.

## Stance: a recording is one sample of one request

- **Stance:** a recording answers exactly the request it was made for, and is one sample of a stochastic act. The replay checks the request; the pass rate is judged at recording time, over several samples.
- **Why:** a replay that doesn't compare the request the code would send now stays green after the instructions, schema or model change, testing a prompt that no longer exists. A property passing on one sample says little about its pass rate: a recording that happened to pass hides a flaky property until the next re-recording exposes it.
- **How to apply:**
  - Keep a hash of the request (instructions, schema, input, model) with each recording, and fail the replay as stale on a mismatch. Fail, don't skip: a skipped property quietly tests nothing.
  - Sample each fixture N times at recording, with N declared before the run, and judge each property by a declared pass rate (supported, refuted, undecided), as reading rules are judged. The suite then replays one sample deterministically.
  - Acts that feed each other (one act's output is the next one's input) record in sequence and stop at the first failure. Otherwise one failed call moves every later call onto a request no recording holds.
  - Write each recording as soon as it arrives, or check its destination before the first call: a harness that writes only at the end loses a paid run when the write fails.
  - A re-recording can fail the act's own strict checks for reasons unrelated to the change. Brief one with a retry budget per fixture and a rule for telling flake from regression: the same fixture failing the same check on every try is a regression; different fixtures failing on different tries is flake.
- **What would change our mind:** an act whose output is deterministic for a fixed request (temperature zero, a provider that guarantees it), where one sample is a verdict.

## Stance: change an act on its cheapest stage, then record the chain once

- **Stance:** an act's instructions or schema change in a loop on that act alone, sampled several times and looked at, until its behaviour is accepted. Only then is what builds on it re-recorded, once.
- **Why:** re-recording cascades. A change to one act makes every downstream act's recordings stale, so its real cost is the whole chain's. Problems in a changed act are visible in its own output, and re-recording the chain for each fix pays the cascade every time.
- **How to apply:**
  - Change one thing per recording. Two prompt changes and a schema change in one recording can't say which did what.
  - "Re-record once the instructions settle" is not a ready criterion: it depends on behaviour nobody has seen yet, and an unattended run meets questions only the owner can answer. Split it into a slice that changes the act and shows its new behaviour for the owner to accept, and a slice that records the chain.
  - Slices that re-record the same recordings run in sequence. A conflict in a recording can't be resolved hunk by hunk, only recorded again, and that costs money.
  - Every brief that re-records says which recordings, the retry budget per fixture and the most it may spend. A run on an expensive model needs the owner's say.
- **What would change our mind:** recordings cheap enough that the cascade costs nothing worth planning around.

## Stance: everything the model is shown is part of its instructions

- **Stance:** the act's standard is stated once, in its own instructions. Whatever else reaches the model (precedents, schema descriptions, the order of the schema's fields, framing text around the input) is treated as instructions too, and is changed and recorded as deliberately as they are.
- **Why:** a model takes everything in its context as guidance. Text added for one feature shifts its judgement on every input, which is editing the instructions by another route, and nothing in the instructions' diff shows it.
- **How to apply:**
  - **A precedent is a case, not a rule.** Past feedback shown as precedent comes with explanatory text only when there are precedents to show, and that text restates no rule. An input with no precedents is then processed exactly as it would be without the feature. A standing paragraph explaining what counts as an error, shown even when no precedent is, shifts the model's judgement everywhere.
  - **Schema order is generation order.** A model writing structured output tends to write the fields in schema order, so set the order deliberately: what is referred to comes before what refers to it. A schema built from an unordered type is serialized in an order the design never chose (a Go `map[string]any` marshals its keys alphabetically); build it with an ordered type, or shape it so order can't matter (inline the referenced objects instead of referring to them by name).
- **What would change our mind:** models whose judgement is demonstrably insensitive to such context, measured on the act's own fixtures.

## Lessons

If something in this Guide proves wrong or incomplete while you work, or you hit something another app calling a model would also hit, record a Lesson addressed to it, as described in `~/.claude/commons/lessons/README.md`.
