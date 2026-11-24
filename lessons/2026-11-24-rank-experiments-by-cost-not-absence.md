---
address: guides/project-knowledge/end-state.md
origin: samthorold/py-minimax-games#230
signal: gap
---

When an end state's parts are pursued one at a time, the order needs a measure of what each gap *costs* in the outcome, not of whether the gap exists. An instrument that asks whether a learned system holds an idea (a probe) finds many missing ideas and can't rank them: an idea it lacks that rarely changes a decision costs nothing. Ranking by "what the measurement says is missing" picks whichever probe happened to read lowest, so a broken probe can set the agenda. Rank instead by measured loss attributable to each kind of decision or component (e.g. regret against a rollout reference, as frequency × size), and use the "is it missing" instruments as candidate explanations for the largest loss.
