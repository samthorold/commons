---
address: (missing Guide: apps whose acts call a language model)
origin: samthorold/go-slow#47 (PR #54)
signal: gap
---

When past user feedback is shown to a model call as precedent (few-shot cases of what the user judged wrong), the text explaining the precedents must appear only when there are some, and must restate no rule. A standing paragraph on every call that explains what counts as an error, even with no precedents shown, shifts the model's judgement on every input. In the origin, one run per variant suggested such a paragraph accounted for most of a drop in extracted facts across all fixtures, none of which showed a precedent. That is the act's instructions being edited by another route. State the standard once, in the act's own instructions, and treat a precedent as a case to compare against. Then an input with no precedents is processed exactly as it would be without the feature.
