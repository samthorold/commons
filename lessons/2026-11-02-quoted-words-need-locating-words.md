---
address: guides/model-calls/addressing-the-source.md
origin: samthorold/go-slow#257
signal: gap
---

When a model cites a finer stretch as words quoted within a numbered stretch, and code turns the quote into an address by finding the words, the quote can only stand for one occurrence (say, the first). A short expression that recurs in the stretch, such as a pronoun used twice for different things, can then be reached only by quoting the words around it, so the model over-quotes ("they then found" instead of "they"). The address kept then holds words the judgement is not about, and anything that replaces the stretch (hydration: the stretch shown as what it refers to) swallows them. Telling the model to quote only the expression doesn't fix this, because it leaves no way to reach a repeat; in one attempt, it made a nearby slip (a pronoun cited in the wrong numbered stretch) several times more frequent.

The citation should carry the stretch and, apart from it, optional locating words that contain it. Code finds the locating words, then the stretch within them, and keeps only the stretch's address. A judgement whose words commonly recur (references, pronouns) needs this; one that cites names or whole stretches mostly doesn't.
