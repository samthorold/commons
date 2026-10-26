---
address: guides/model-calls.md#stance-models-sit-behind-a-port-and-are-chosen-by-measurement
origin: samthorold/go-slow#98
signal: trap
---

On a model whose thinking is on by default, a call that sets no thinking option still thinks, and the thinking counts against the output bound (`max_tokens`). The response can show none of it (an empty thinking block), so the answer looks far shorter than the tokens billed. An output bound sized for the answer then cuts off long inputs now and then. In the origin, 5,697 of 9,445 output tokens in one structured-output call were thinking, and readings of one long input used up to 92% of a 16,000-token bound.

Two things follow:

- **Size the output bound from the reported usage** (the provider's count of thinking tokens), not from the visible answer.
- **Pinning the model version doesn't pin its behaviour if a request relies on the provider's defaults.** Thinking on or off, and its effort, is part of what an act does and much of what it costs. Set it explicitly in the request, chosen by measurement on the act's fixtures like the model itself, so a change of default can't change the act between two readings.
