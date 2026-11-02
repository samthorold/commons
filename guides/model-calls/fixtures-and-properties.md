# Model calls Guide: three tiers, and the suite never pays for a call

How to apply the Stance *three tiers, and the suite never pays for a call*, from [the Model calls Guide](../model-calls.md#stance-three-tiers-and-the-suite-never-pays-for-a-call), which states the Stance.

## Why, in full

A suite that calls a model is slow, costs money on every run and isn't deterministic, so it stops being run. A suite that only fakes the model never sees what a real one does with the instructions. Asserting exact text breaks on every re-recording without saying anything about whether the act works.

## How to apply

- Fixtures are material the repo may hold. Material the app may read but not store or redistribute can't be a committed fixture.
- Make fixtures by the production path (the same collection, the same truncation), or check that they match it. A fixture richer than what production collects lets a property pass on input the model is never given in use, and nothing fails to say so.
- A property that relies on a case appearing (a reaction, a piece of feedback) names the fixture it needs, hand-made from admissible material, and asserts that the case is present, in a test of its own over the act's inputs (fixtures and frozen copies). Otherwise a re-recording or a refreshed input that drops the case leaves the property testing nothing, and an assertion that runs only inside the replay never runs while the recordings are stale, so the loss shows only on a paid run.
- **A property tied to a case reads only that case's output.** It names the output it rests on (the item drawn from the reaction, not everything drawn from the input), asserts it is present, and checks only it; everything else the input yields is free to vary. A property worded over the whole fixture is refuted when an upstream change rightly draws a second item from the same input, and narrowing it after the reading looks like moving the line: it is a fix only with the evidence that the failure came from another output, shown in the PR.
- **Selection is not classification.** "Drawn as X" fails two ways: drawn as something else, or not drawn at all. A property says which it tests, and a classification property ("when drawn, it is X") sits beside a selection property, never in its place. A change that widens or narrows a category in the instructions moves selection too (newly counted items crowd out what used to be drawn), so its paired report is read for what each fixture draws, not only for the category.
- **Assert judgement, not wording.** A property that is a list of words (no statement contains *will*) tests wording: the model meets it with synonyms, and it catches legitimate uses. Assert the property on the cases the standard is about, by meaning, and report word counts in the paired report rather than asserting them. A property's words stay out of the act's instructions ([what the model is shown](what-the-model-is-shown.md)).
- **A property's helper reads only the field the property is about.** A helper that also searches what is tied to the output (names linked to a statement) passes on text the output never held. A change that removes a bridge or a derived field checks every helper that reads it, since a replay stays green either way.
