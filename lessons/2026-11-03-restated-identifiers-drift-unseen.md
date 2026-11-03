---
address: guides/project-knowledge/durable-knowledge.md
origin: samthorold/go-slow#291
signal: gap
---

A project's `CLAUDE.md` that restates code facts (identifiers, routes, "not yet" claims about features) drifts from the code with nothing to catch it: no test reads it, and an agent loading it every session trusts it. Cutting one to a map turned up three such claims already stale: identifiers that no longer existed, and a "not yet supported" feature that had shipped. Moving the text into doc comments as it stood would have carried the drift along. So the cut has to check each identifier and claim it moves against the code (grep every named identifier) before giving it a new home, and drop what is false. The Guide says code facts belong in the code; it doesn't say that a cut moving them there must verify each one, and that verifying is where the drift is found.
