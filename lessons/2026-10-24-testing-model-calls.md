---
address: guides/agentic-development.md#stance-agents-implement-test-first
origin: samthorold/go-slow#10
signal: gap
---

When the product itself calls a language model, test-first needs a shape the Guide doesn't give. Three tiers work, and none of them makes the suite pay for a model call:

1. **A fake model, injected at a port**, for everything around the call: typed results, checks before anything is written back, tracing, error handling. Fast, deterministic, written test-first.
2. **Recorded runs**: call the real model once on committed fixtures, keep its responses, and replay them in the suite, asserting properties (not exact text) on the outputs. Re-record deliberately when the prompt or instructions change; the diff shows what changed. Only the re-recording costs money.
3. **Judgement quality is not a test.** Whether the model judges well is a hypothesis read in use (e.g. from the owner's feedback), not something CI asserts.

Fixtures must be content the repo may hold. Material the project may read but not store or redistribute cannot be a committed fixture.

What building it taught (origin samthorold/go-slow#40, #45, #48), all about recorded runs:

- **Recordings that depend on each other in sequence** (one act's output is the next act's input) must stop at the first failure. Otherwise one failed call shifts every later call onto a request no recording holds, and quietly corrupts the recordings after it.
- **Re-recording cascades.** Changing one act's instructions makes every downstream act's recordings stale; the real cost of a prompt change is the whole chain's re-recording, so scope and budget it as such.
- **A recorded property names the fixture it needs.** A property that relies on a case appearing in one model's output (a reaction, a piece of feedback) silently stops testing anything when a re-recording drops the case. Make the case a hand-made fixture from admissible material, and assert it is present.
- **Write a recording as it goes, or check its destination first.** A harness that writes only at the end loses a paid run when the write fails.
- **Make fixtures by the production collection path, or check that they match it.** Fixtures fetched another way (a full document from an API) when production collects something thinner (a feed summary) let a recorded property pass on input production never gives the model, and nothing fails to say so (origin samthorold/go-slow#30).
- **A re-recording can fail the act's own strict checks for reasons unrelated to the change** (origin samthorold/go-slow#50: half of the fixtures failed a naming-consistency check after an instructions change that didn't touch naming). A one-shot run can't tell a flaky check from a regression, and an unattended agent briefed "re-record once, don't retry" leaves the criterion unmet. Brief a re-recording with a retry budget per fixture and a rule for telling the two apart (e.g. the same fixture failing the same check on every try is a regression; different fixtures failing on different tries is flake).
- **A replay must know which request it answers.** A harness that replays a recorded response without comparing the request the current code would send keeps passing after the instructions, schema or model change: green, and testing a prompt that no longer exists (origin samthorold/go-slow#50, #56). Keep a hash of the request (instructions, schema, input, model) with each recording, and fail the replay as stale on a mismatch. Fail rather than skip, since a skipped property quietly tests nothing.
- **One recording is one sample, not a verdict.** A stochastic act's recorded property passing once says little about its pass rate. A recording that happened to pass hides a flaky property until the next re-recording exposes it (origin samthorold/go-slow#47: 4 of 8 fixtures failing one run, one fixture failing 2 of 3). Sample each fixture N times at record time, with N declared before the run, and judge each property by a declared pass rate (supported, refuted, undecided), as the Project knowledge Guide's reading rules do. The suite then replays one sample deterministically (origin samthorold/go-slow#60, still in design).
