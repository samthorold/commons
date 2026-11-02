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
  2. **Recorded runs**: the real model is called on committed fixtures, its responses are kept, and the suite replays them, judging properties of the outputs (never exact text). Only recording costs money; it is done deliberately, never by the suite.
  3. **Judgement quality is a hypothesis**, read in use (from the owner's feedback, say), not something CI asserts.
- **Why:** a suite that calls a model is slow, costs money on every run and isn't deterministic, so it stops being run. A suite that only fakes the model never sees what a real one does with the instructions. Asserting exact text breaks on every re-recording without saying anything about whether the act works.
- **How to apply:**
  - Fixtures are material the repo may hold. Material the app may read but not store or redistribute can't be a committed fixture.
  - Make fixtures by the production path (the same collection, the same truncation), or check that they match it. A fixture richer than what production collects lets a property pass on input the model is never given in use, and nothing fails to say so.
  - A property that relies on a case appearing (a reaction, a piece of feedback) names the fixture it needs, hand-made from admissible material, and asserts that the case is present, in a test of its own over the act's inputs (fixtures and frozen copies). Otherwise a re-recording or a refreshed input that drops the case leaves the property testing nothing, and an assertion that runs only inside the replay never runs while the recordings are stale, so the loss shows only on a paid run.
- **What would change our mind:** models cheap and deterministic enough to call in the suite, which would make tier 2 a live test.

## Stance: a recording answers exactly one request

- **Stance:** a recording answers the request it was made for, exactly as it was sent, and the replay fails as stale when the code would now send any other.
- **Why:** a replay that doesn't compare the request the code would send now stays green after the instructions, schema or model change, testing a prompt that no longer exists. And a sample is only a sample of the act if it answers the same request as the others: one drawn over a different prior state, or lost to the provider, measures something else.
- **How to apply:**
  - Keep a hash of the request as sent (instructions, schema, input, model, and in a conversation the model's earlier turns in the form the provider returned them) with each recording, and keep in the recording whatever is needed to rebuild it. Fail the replay as stale on a mismatch. Fail, don't skip: a skipped property quietly tests nothing.
  - Acts that feed each other (one act's output is the next one's input) record in sequence and stop at the first failure. Otherwise one failed call moves every later call onto a request no recording holds.
  - Fixtures that build on each other (each one's work changes the state the next is run over) carry each earlier fixture forward by one sample chosen before its results are seen (its first), and every sample of a later fixture runs over a copy of that state. Otherwise each sample answers a different request.
  - A call that brings back no answer while recording (a transport error, the provider overloaded) is not a sample: retry it, or stop without keeping it. An answer that came back counts, even one returned as an error (the model refusing, an answer cut off), since that is the act's behaviour on its request.
  - Write each recording as soon as it arrives, or check its destination before the first call: a harness that writes only at the end loses a paid run when the write fails.
  - A recording of a tool-using act keeps, beside each turn, what the tools returned and the outcome (continued, refused with the reason told back, applied). The replay doesn't need it; whoever compares two recordings does.
- **What would change our mind:** nothing foreseeable. A request either is the one the code sends or it isn't.

## Stance: an act is judged over its samples, in the suite

- **Stance:** a recording is one sample of a stochastic act. Each fixture is sampled N times, every sample is kept, and the suite replays them all and judges each property per fixture by a rule declared before the samples were drawn, on every run.
- **Why:** a property passing on one sample says little about its pass rate: a recording that happened to pass hides a flaky property until the next re-recording exposes it. A rate judged once at recording time is a claim in a PR body that nothing checks again; a later change to how a property is asserted quietly stops testing the samples it was measured on. Derived on every run, the status stays true of the code, as a register's does (Project knowledge Guide, end-state Stance). Pooled across fixtures, a rate hides a property that fails on one input.
- **How to apply:**
  - Declare N and each property's rule (supported, refuted, undecided, by count) before the samples are drawn, as reading rules are declared.
  - A sample is one piece of work run as it runs in use, with the act's retry budget. Passing the act's own checks is rated over all samples ("passes within its attempts": a refused try costs a retry, not a wrong output). A property only the suite asserts runs nowhere in use, so it is rated over the samples that passed their checks.
  - A re-recording reads its failures by where they fall. The same fixture failing the same check on every try is a regression. On a large share of tries but not all, it is a slip: a defect in the act, paid for as a retry every time it happens in use. Different fixtures failing on different tries is flake. Only flake is answered by drawing again.
  - Redrawing a fixture re-reads every property it has. A slip, or any property refuted or undecided that the run wasn't aimed at, stops the run and is reported, never redrawn: drawing until a count crosses its line is not a reading. The fix is a change to the act (*change an act on its cheapest stage*). A slice that redraws one fixture for a narrow reason counts the cost of re-reading all of it when it is sized.
  - A change to an act's instructions, schema or model reports its samples beside the current version's, per fixture and with every output field counted, next to the rule's verdict. The pairing removes the variance between fixtures, and shows side effects no pass-rate line catches. It is a report for whoever accepts the change, not a second rule: a suite this small detects only large differences (Miller 2024, *Adding Error Bars to Evals*, arXiv:2411.00640).
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
