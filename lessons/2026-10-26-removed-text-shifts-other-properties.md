---
address: guides/model-calls.md#stance-everything-the-model-is-shown-is-part-of-its-instructions
origin: samthorold/go-slow#111
signal: gap
---

The Stance warns that text *added* to what a model is shown shifts its judgement everywhere. Text *taken away* does too, including text with no apparent bearing on the property that moves. The case: an extraction act's instructions lost a paragraph defining which entities each statement involved (the slice moved that judgement to another act). A property tested elsewhere, that an unattributed estimate is not drawn as an established fact, went from 5 of 5 to 4 of 5 on two separate draws. The removed paragraph had said who makes an attributed statement is not involved in it, one of the few places the instructions framed statements as someone's voice.

The free stale check (replay with no model) says which recordings a change touches, never which properties will still hold; only sampling does. What fixed it was not a patch aimed at the failing case but a rule stating the domain distinction the removed text had carried implicitly (a projected effect can't be corroborated as at its date, so it is never a fact). That rule moved statements across every fixture, so it was the owner's call and its shift was reviewed.

Candidate rule: removing instructions is changing them. A slice that takes text out of an act's instructions samples every property of the act, not only those about what was removed, and budgets for an instructions fix the owner decides.
