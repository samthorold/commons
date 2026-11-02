# Model calls Guide: the model judges addresses into the source, and never rewords it

How to apply the Stance *the model judges addresses into the source, and never rewords it*, from [the Model calls Guide](../model-calls.md#stance-the-model-judges-addresses-into-the-source-and-never-rewords-it), which states the Stance and why.

- Numbers, not offsets: models cite numbers reliably and character offsets poorly.
- Code turns quoted words into an address by matching them as a reader sees them (curled quotes as straight, markup dropped) and only as whole words ("he" inside "The" has no address), and the act's checks refuse a number not shown or words not in their stretch, naming both.
- Store the address, never the quoted words, and keep the judgements in their own records pointing at it (stand-off annotation).
- Text shown to a later act may be the stretches with their judgements applied (a reference followed to what it refers to), built by code from the addresses, so the source stays as written.
