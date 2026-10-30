---
address: guides/model-calls.md#stance-everything-the-model-is-shown-is-part-of-its-instructions
origin: samthorold/go-slow#208
signal: gap
---

An act that extracts propositions from source text tends to reword them. Each rewording makes judgements of its own that nobody asked for and nothing records:

- it resolves references ("the city" becomes Derby);
- it invents attributions ("X said:" becomes the subject of every sentence after it);
- it drops the speaker's voice (a quoted view comes out in the app's own voice).

Every later act then builds on text the source never wrote. The alternative is to keep the source's words and have the model judge **addresses** into them:

- **Show the text cut into numbered stretches**, by plain code, and have the model cite numbers (models cite numbers reliably and character offsets poorly), with finer stretches given as words quoted within a numbered one.
- **Store the address the number stands for.**
- **Keep each judgement apart from the text** (what a stretch refers to, who speaks it), the stand-off annotation pattern.

Tracing then becomes a property of the address, not a quote check, and since the text never changes, no later judgement or feedback is left pointing at something reworded. A working concept in the Origin, not yet built: promote once an Adopter has run on it.
