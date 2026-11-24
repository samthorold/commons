---
address: (missing Guide: game search and learning)
origin: samthorold/py-minimax-games#231
signal: trap
---

An instrument that stands a reduced-budget copy of a player in for the player itself (a rollout policy, a regret reference, a sparring partner) reads the copy, not the player. Cutting the budget doesn't weaken it evenly: in a sampled-worlds planner for a hidden-information game, dropping to one sampled world lost 10-12 points of win chance against the full player at any search budget, while a quarter of the states lost about 6.5. So before an instrument's readings are trusted, play the reduced copy against the player it stands for, record the match beside the sizing, and choose which budget to cut by that match, not by which cut saves the most time.
