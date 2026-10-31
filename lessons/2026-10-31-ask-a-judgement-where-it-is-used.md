---
address: guides/model-calls.md#stance-everything-the-model-is-shown-is-part-of-its-instructions
origin: samthorold/go-slow PR #238
signal: gap
---

Where a judgement sits in a structured output's schema matters, not only the fields' order. A per-item judgement asked for in a separate top-level list, apart from the element that uses it (each told item's grouping in a `gathered` list beside `statements`), was often skipped: 2 of 5 samples were refused for leaving items ungathered. Moved inside the element that uses it, with a short note field written before the prose (who speaks the quoted words), the same instructions passed 5 of 5, and the prose stopped telling a spokesperson's line in its own voice.

The Guide's *schema order is generation order* says to put what is referred to before what refers to it. It could add: ask for a judgement inside the element it belongs to, and put a brief note field before free prose that must respect it.
