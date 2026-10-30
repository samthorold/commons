---
address: guides/model-calls.md
origin: samthorold/go-slow#208
signal: gap
---

An act that extracts propositions from source text, each checked against a quote, tends to return the quote lightly reworded: the proposition stutters its span. What the rewording adds is mostly judgements folded into the text, out of sight: resolving a reference from elsewhere in the document ("the city" becomes a named place), inventing an attribution from a "X said:" line, and sometimes an error the span wouldn't make (a speaker's opinion restated in the document's own voice). Keeping the span itself as the unit, and putting each of those judgements in a tag or a separate, traced rewrite of the span, makes every judgement visible, checkable and redoable on its own, and leaves the unit cheap and never redone. Another app extracting statements from documents with a model would face the same choice; the Guide has no Stance on what an extraction act's unit should be.
