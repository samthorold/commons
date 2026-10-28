---
address: guides/flutter.md
origin: a private Adopter (see the portfolio)
signal: gap
---

Content generated from a seed, committed and checked to reproduce byte for byte (puzzle packs, level data), can't rely on `dart:math` `Random(seed)`: its documentation promises a deterministic sequence for a seed, not the same sequence across SDK versions, so an SDK upgrade could silently change what the seed produces and fail the reproduction check. Such generators use a small PRNG defined in the project. This is the Dart form of the Python Guide's "bit-identical randomness" point; worth checking against the current `Random` docs at Promotion.
