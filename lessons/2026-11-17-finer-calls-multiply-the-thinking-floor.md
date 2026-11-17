---
address: guides/model-calls/choosing-a-model.md
origin: samthorold/go-slow#303
signal: gap
---

On a model that thinks by default, every call carries a floor of output tokens (about 1k on a small model, here, even at low effort), whatever the size of its question. Splitting an act into finer calls (one per sentence instead of one per document) multiplies that floor, and prompt caching only discounts repeated *input*: a measurement found caching worked inside batches (92–100% of requests read the cache) and the finer unit still cost about 9× the coarse one, since output was about 84% of its cost. A design that argues "the provider's cache carries the repetition" has to be priced on output too, before the unit is chosen.
