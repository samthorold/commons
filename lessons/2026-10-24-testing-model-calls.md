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
