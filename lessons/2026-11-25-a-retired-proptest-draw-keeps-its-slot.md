---
address: guides/rust.md#testing
origin: samthorold/explorers#913
signal: trap
---

When a parameter is retired, removing its draw from a proptest strategy shifts every value drawn after it, so every generated case changes and the committed regression seeds silently stop replaying the cases they were saved for (they still pass, against different cases). Keep drawing the retired dimension and stop reading it; the seeds then replay the same inputs. The same holds for any change to a strategy's draw order.
