# Skills

Procedures, one `SKILL.md` directory each. A Skill applies the Guides rather than restating them. How they're linked into `~/.claude/skills/` is in the dotfiles README.

They form one delivery pipeline: `grill-me` / `grill-with-docs` → `to-prd` → `to-issues` → `triage` → `grind-issues` → `tdd`, with `diagnose` for hard bugs, `prototype` for throwaway answers to design questions, and `handoff` between sessions. Where a repo has `docs/agents/issue-tracker.md` and `triage-labels.md`, the planning Skills read them; otherwise they assume GitHub Issues and the default labels.

## Provenance

| Skill | Origin |
|---|---|
| `grind-issues` | Written here. |
| `diagnose`, `grill-me`, `grill-with-docs`, `handoff`, `prototype`, `tdd`, `to-issues`, `to-prd`, `triage` | Derived from [mattpocock/skills](https://github.com/mattpocock/skills) (installed 2026-05-23), modified since. MIT licence: see [`LICENSE-mattpocock-skills`](LICENSE-mattpocock-skills). |

These are now maintained here, not synced from upstream. To take an upstream change, compare by hand and Revise as for any other part of the Commons.
