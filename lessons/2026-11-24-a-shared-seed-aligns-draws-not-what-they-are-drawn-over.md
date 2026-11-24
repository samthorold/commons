---
address: guides/emergent-systems.md
origin: samthorold/py-minimax-games#233
signal: gap
---

Comparing two options by running each forward on the same seeds (common random numbers) cancels their shared luck only while the draws land on the same things. Once the two runs differ by one item (one card bought instead of another, one actor added), a draw over a collection (a shuffle, a sample of hidden states) picks different items in each run from the same seed, and most of the variance comes back. Reseeding the sampler per decision doesn't fix it, since it still aligns the draw and not what it is drawn over. What does is keying each item's draw by its identity (e.g. each item's place in a shuffle from a hash of the seed and the item), and that has to be done for every sampler the comparison passes through. Measured twice in one Adopter: keyed shuffles cut the paired variance to 0.30 of independent for options that bought alike but only to about 0.7 for options that bought differently, and reseeding the planner's world sampling per plan gained nothing more (0.250 against 0.242).
