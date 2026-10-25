---
address: guides/model-calls.md#stance-everything-the-model-is-shown-is-part-of-its-instructions
origin: samthorold/go-slow#61
signal: gap
---

A slice that adds a plain-code check on an act's output can look like it changes nothing the model sees: same instructions, same schema, same request hash. It still changes what the act must produce. If the instructions never state the standard the check enforces, the model fails it systematically, and in use the work fails every attempt.

The case: a check that every Entity a Fact's statement names is among that Fact's Entities. The model treats a place named as a qualifier ("Zelenskyy of Ukraine") as background, and refused 6 of 8 existing recordings, the same way on every try.

This is the mirror of the Stance: a check the model isn't shown is a standard it can't meet. Candidate rule: before a slice that adds a check is marked ready, run the check against the existing recordings (free) and a few fresh samples. If they fail, the slice changes the instructions too, on the act alone, for the owner to accept.
