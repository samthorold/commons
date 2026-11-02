# Model calls Guide

**Scope:** Archetype = apps whose acts call a language model, any Stack. An **act** is a piece of the app's work done by a model call: its instructions, the input it is shown, the output schema it answers in and the checks its output must pass before anything is written back. An app is in this Archetype when behaviour that matters comes from a model's judgement at run time. Like an emergent system's, that behaviour is observed by running it, not derived from the code; unlike one, it comes from a component the project neither owns nor can inspect, and every run of it costs money.

Code around an act (parsing, checks, storage, the loop that drives a conversation) is ordinary code under the Agentic development Guide's test-first Stance. This Guide says how that Stance applies to the act itself, and how the act's inputs are shaped. How hypotheses about the end state are declared and read is the Project knowledge Guide's end-state Stance.

Each Stance's *How to apply* lives in its own file under `~/.claude/commons/guides/model-calls/`, and the Stance says when to read it. Links are relative to this file.

## Stance: models sit behind a port, and are chosen by measurement

- **Stance:** each act calls a provider-neutral port (one call, a batch, a conversation turn), and the provider's SDK and types stay inside its adapter. The model each act runs on is config, chosen per act by measuring candidates on the act's own fixtures, not by reputation.
- **Why:** models change faster than the app: new versions ship, prices move, and one act's best model isn't another's. An act that knows its provider can't be measured against another one. The agent advising on the choice is itself one vendor's model, and a vendor-specific skill may supply that vendor's prices and defaults. Its framing then drifts toward that vendor (comparisons within one line-up, recalled terms presented as fact), and nothing in the conversation corrects it.
- **How to apply:** before choosing, pinning or changing the model an act runs on, or an option its request sets, read [choosing a model](model-calls/choosing-a-model.md).
- **What would change our mind:** an act that depends on a feature only one provider has, where the port would have to pretend otherwise. The act then names the provider in the design, and says why.

## Stance: three tiers, and the suite never pays for a call

- **Stance:** an act is tested in three tiers.
  1. **A fake model, injected at the port**, for everything around the call: typed results, the checks before anything is written back, tracing, errors and retries. Fast, deterministic, written test-first.
  2. **Recorded runs**: the real model is called on committed fixtures, its responses are kept, and the suite replays them, judging properties of the outputs (never exact text). Only recording costs money; it is done deliberately, never by the suite.
  3. **Judgement quality is a hypothesis**, read in use (from the owner's feedback, say), not something CI asserts.
- **Why:** a suite that calls a model is slow, costs money on every run and isn't deterministic, so it stops being run. A suite that only fakes the model never sees what a real one does with the instructions. Asserting exact text breaks on every re-recording without saying anything about whether the act works.
- **How to apply:** before making a fixture or writing a property for recorded runs, read [fixtures and properties](model-calls/fixtures-and-properties.md).
- **What would change our mind:** models cheap and deterministic enough to call in the suite, which would make tier 2 a live test.

## Stance: a recording answers exactly one request

- **Stance:** a recording answers the request it was made for, exactly as it was sent, and the replay fails as stale when the code would now send any other.
- **Why:** a replay that doesn't compare the request the code would send now stays green after the instructions, schema or model change, testing a prompt that no longer exists. And a sample is only a sample of the act if it answers the same request as the others: one drawn over a different prior state, or lost to the provider, measures something else.
- **How to apply:** before building or changing the recording harness, its replay, or how chained acts and fixtures are recorded, read [recording](model-calls/recording.md).
- **What would change our mind:** nothing foreseeable. A request either is the one the code sends or it isn't.

## Stance: an act is judged over its samples, in the suite

- **Stance:** a recording is one sample of a stochastic act. Each fixture is sampled N times, every sample is kept, and the suite replays them all and judges each property per fixture by a rule declared before the samples were drawn, on every run.
- **Why:** a property passing on one sample says little about its pass rate: a recording that happened to pass hides a flaky property until the next re-recording exposes it. A rate judged once at recording time is a claim in a PR body that nothing checks again; a later change to how a property is asserted quietly stops testing the samples it was measured on. Derived on every run, the status stays true of the code, as a register's does (Project knowledge Guide, end-state Stance). Pooled across fixtures, a rate hides a property that fails on one input.
- **How to apply:** before declaring an act's samples and rules, reading a re-recording's failures, or redrawing a fixture, read [samples](model-calls/samples.md).
- **What would change our mind:** an act whose output is deterministic for a fixed request (temperature zero, a provider that guarantees it), where one sample is a verdict.

## Stance: change an act on its cheapest stage, then record the chain once

- **Stance:** an act's instructions or schema change in a loop on that act alone, recorded over frozen copies of what it rests on, until its samples meet a criterion declared before they were drawn. Only then are the acts that build on it brought onto its new output, together and once: a **refresh**.
- **Why:** re-recording cascades. A change to one act makes every downstream act's recordings stale, so its real cost is the whole chain's. Problems in a changed act are visible in its own output, and re-recording the chain for each fix pays the cascade every time.
- **How to apply:** before writing, briefing or sizing a slice that changes an act or re-records it, read [changing an act](model-calls/changing-an-act.md).
- **What would change our mind:** recordings cheap enough that the cascade costs nothing worth planning around.

## Stance: everything the model is shown is part of its instructions

- **Stance:** the act's standard is stated once, in its own instructions, and every check its output must pass is a standard the instructions state. Whatever else reaches the model (precedents, schema descriptions, the order and placing of the schema's fields, framing text around the input, what its tools return) is treated as instructions too, and is changed and recorded as deliberately as they are.
- **Why:** a model takes everything in its context as guidance. Text added for one feature shifts its judgement on every input, and so does text taken away, on properties with no apparent bearing on it: that is editing the instructions by another route, and nothing in the instructions' diff shows it. The mirror holds too: a check the model isn't shown is a standard it can't meet, so it fails it the same way on every try, and in use the work fails every attempt.
- **How to apply:** before changing anything an act is shown (instructions, schema, precedents, tool results, the shared code that builds its input), or adding a check on its output, read [what the model is shown](model-calls/what-the-model-is-shown.md).
- **What would change our mind:** models whose judgement is demonstrably insensitive to such context, measured on the act's own fixtures.

## Stance: the model judges addresses into the source, and never rewords it

- **Stance:** an act that works on source text is shown it cut into numbered stretches by plain code, and cites stretches by number (finer ones as words quoted within a numbered one, which code turns into an address). Each judgement (what a stretch refers to, who speaks it, what it names) is kept apart from the text, addressing it. The source's words are never rewritten by a model.
- **Why:** a model asked to extract propositions rewords them, and every rewording makes judgements of its own that nobody asked for and nothing records: it resolves references ("the city" becomes Derby), invents attributions (the speaker of one sentence becomes the subject of the next), and drops the speaker's voice (a quoted view comes out in the app's own). Every later act then builds on text the source never wrote. Judged by address, each of those becomes a judgement of its own, checkable and open to feedback; tracing becomes a property of the address, not a quote check; and since the text never changes, no later judgement or feedback is left pointing at something reworded.
- **How to apply:** before building an act that works on source text, read [addressing the source](model-calls/addressing-the-source.md).
- **What would change our mind:** an act whose output is meant to be new prose (a summary, a briefing), where rewording is the work. It still cites the stretches it tells, by number.

## Stance: every call in use is kept, and a changed judge judges forward

- **Stance:** the running app keeps every model call it makes, the request exactly as sent and the response exactly as returned, for good and never rewritten, and each output points to the call that made it. The kept call names the output's judge (the act, its instructions' version, the model, the request's hash). Where the app keeps a model's judgements as its record, a new judge (another model, a new version of the instructions) judges what arrives from then on; the judgements made before stand, with their judge, and a view reads, for each thing judged, the newest judge that has judged it.
- **Why:** judgement is read in use (tier 3), and when feedback says an output is wrong, only the request as sent says why the act judged so: inputs assembled at run time (precedents, candidates drawn from the store as it stood) are reproduced by no commit. Re-judging the whole record on every change costs as much as the record is large, and it grows daily, for every instruction tried; judgements kept with their judge let every view say who judged what it shows, and let a change be tried without rewriting what is already in use.
- **How to apply:** before building or changing how the app keeps calls and judgements, or switching or comparing an act's judge, read [kept calls](model-calls/kept-calls.md).
- **What would change our mind:** a record small enough, or judges cheap enough, that re-judging all of it on each change costs nothing worth planning around.

## Lessons

If something in this Guide proves wrong or incomplete while you work, or you hit something another app calling a model would also hit, record a Lesson addressed to it (to the Stance's detail file, where the Lesson is about how to apply it), as described in `~/.claude/commons/lessons/README.md`.
