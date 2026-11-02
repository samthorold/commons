# Model calls Guide: the model judges addresses into the source, and never rewords it

How to apply the Stance *the model judges addresses into the source, and never rewords it*, from [the Model calls Guide](../model-calls.md#stance-the-model-judges-addresses-into-the-source-and-never-rewords-it), which states the Stance.

## Why, in full

A model asked to extract propositions rewords them, and every rewording makes judgements of its own that nobody asked for and nothing records: it resolves references ("the city" becomes Derby), invents attributions (the speaker of one sentence becomes the subject of the next), and drops the speaker's voice (a quoted view comes out in the app's own). Every later act then builds on text the source never wrote. Judged by address, each of those becomes a judgement of its own, checkable and open to feedback; tracing becomes a property of the address, not a quote check; and since the text never changes, no later judgement or feedback is left pointing at something reworded.

## How to apply

- Numbers, not offsets: models cite numbers reliably and character offsets poorly.
- Code turns quoted words into an address by matching them as a reader sees them (curled quotes as straight, markup dropped) and only as whole words ("he" inside "The" has no address), and the act's checks refuse a number not shown or words not in their stretch, naming both.
- **A citation carries locating words apart from the quoted ones.** Quoted words can stand for only one occurrence in their stretch (say, the first), so a short expression that recurs (a pronoun used twice, for different things) can be reached only by quoting the words around it, and the model over-quotes ("they then found" for "they"). The address then holds words the judgement isn't about, and anything that replaces the stretch (a reference shown as what it refers to) swallows them. Telling the model to quote only the expression leaves no way to reach a repeat, and can make nearby slips more frequent. So a citation carries the quoted words and, apart from them, optional locating words that contain them: code finds the locating words, then the quoted words within them, and keeps only the quoted words' address. Judgements whose words commonly recur (references, pronouns) need it; those citing names or whole stretches mostly don't.
- Store the address, never the quoted words, and keep the judgements in their own records pointing at it (stand-off annotation).
- Text shown to a later act may be the stretches with their judgements applied (a reference followed to what it refers to), built by code from the addresses, so the source stays as written.
