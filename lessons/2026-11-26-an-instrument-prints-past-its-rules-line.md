---
address: guides/project-knowledge/end-state.md
origin: samthorold/py-minimax-games#237
signal: gap
---

An instrument should report the quantity a reading rule reads more precisely than the rule's line. In the origin, a calibration gap was printed to three decimals against a line of 0.03, and the deciding value printed as +0.030, exactly on the line. Its counts allowed a value anywhere from 0.0295 to 0.0302, so the log couldn't say whether the reading was *supported* or *refuted*. The only way to settle it was to replay the same games with a scratch script, which works only because the run is deterministic. Where a run isn't deterministic, the reading is lost. When a rule is declared, its instrument should print the quantity at least one digit past the line, together with the error the rule names, or mark which side of the line it falls. This is the precision counterpart of a rule naming the error it reads.
