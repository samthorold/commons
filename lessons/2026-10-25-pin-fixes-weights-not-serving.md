---
address: guides/model-calls.md#stance-models-sit-behind-a-port-and-are-chosen-by-measurement
origin: samthorold/go-slow#58
signal: gap
---

The Stance says to pin the model version an act runs on, so a provider's silent upgrade can't change behaviour between two readings. A pin fixes the weights, not everything around them. At least one provider's docs say the serving infrastructure around a fixed model ID (routing, classifiers, sampling) can still change behaviour slightly.

So a pinned act's recordings replaying green doesn't show that its behaviour in use is unchanged, and two readings on the same pin can differ with nothing in the project changed.

Also worth saying: what the provider *reports* as the model is what each result should keep, not the configured string. Then a moved alias, where one is used, shows in the store.
