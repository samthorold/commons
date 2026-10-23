# Skills

Procedures, one `SKILL.md` directory each. A Skill applies the Guides rather than restating them. How they're linked into `~/.claude/skills/` is in the dotfiles README.

They form one delivery graph, with three ways in:

- **A design idea**: `grill-with-docs` → `to-issues` (an epic when there's more than one slice) → `grind-issues` → `tdd` per slice.
- **A `needs-design` issue**: `grill-with-docs` on the issue → `ready` (or `to-issues` if it splits) → `grind-issues`.
- **A hard bug**: `diagnose`.

Alongside: `grill-me` for plans with no repo docs to write into, `open-session` for a concept that is itself still in question (it ends in an issue's working concepts, which a later grill can settle), `prototype` for throwaway answers to design questions a grill can't settle by talk, and `handoff` between sessions. Issues follow the Global Guide's *Issues* Conventions; the Skills apply the Guides rather than restating them.

## Provenance

| Skill | Origin |
|---|---|
| `grind-issues`, `open-session` | Written here. |
| `diagnose`, `grill-me`, `grill-with-docs`, `handoff`, `prototype`, `tdd`, `to-issues` | Derived from [mattpocock/skills](https://github.com/mattpocock/skills) (installed 2026-05-23), modified since (retired since: `triage`, as two issue states left it nothing a grill doesn't do; `to-prd`, as the grill writes the design into the docs and `to-issues` makes the epic). MIT licence: see [`LICENSE-mattpocock-skills`](LICENSE-mattpocock-skills). |

These are now maintained here, not synced from upstream. To take an upstream change, compare by hand and Revise as for any other part of the Commons.
