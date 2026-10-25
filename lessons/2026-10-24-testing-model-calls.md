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
