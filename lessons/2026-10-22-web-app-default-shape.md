---
address: web app (missing Archetype Guide)
origin: samthorold/go-wine@05aa996 (CLAUDE.md, *Architecture — ports & adapters (onion)*)
signal: gap
---

The owner's default shape for a new web app or service, shown while designing one and meant as the default for the next: **ports and adapters (onion)**, with **DDD only where it earns its keep**: a rich domain model for genuine invariants and behaviour, thin CRUD for the rest. The boundary is explicit and treated as movable, so a concept is promoted into the domain once it grows real rules. **Lightweight CQRS**: read services return view DTOs, separate from the command and domain paths (not event sourcing, not two databases). Tests go through the **repository port as the seam**: unit tests against in-memory adapters (fast, no container), integration tests against the real datastore. Going straight to **Postgres with docker-compose** rather than SQLite is fine when compose removes the ops burden. It holds for any web app the owner starts, whatever the language, so it belongs in a web-app Archetype Guide, not one repo's docs. Until that Guide exists, a new web app has to rediscover it, or an agent proposes a different shape.
