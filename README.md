# commons

The shared approach behind my projects: Guides (Conventions and Stances per Stack and Archetype), Skills (Procedures), and Lessons waiting to be promoted. The vocabulary is in [`CONTEXT.md`](CONTEXT.md); the list of Guides is in [`MAP.md`](MAP.md).

## How the repos fit together

| Repo | Visibility | Job |
|---|---|---|
| [dotfiles](https://github.com/samthorold/dotfiles) | public | Machine and Claude Code configuration, and the wiring that links this repo into `~/.claude/`. |
| **commons** (this repo) | public | Approach: vocabulary, Map, Guides, Skills, Lessons. No list of projects. |
| portfolio | private | The projects themselves: Groups and Direction. |

Each project records its own Adoptions (Imports of Guides) in its `CLAUDE.md`.

## Layout

- `CONTEXT.md`: the vocabulary.
- `MAP.md`: one line per Guide with its Scope. Imported into every session.
- `guides/`: the Guides, each with a Scope; several may share one, split by topic.
- `lessons/`: Lessons waiting for Promotion, and their format.
- `skills/`: Skills (Procedures), each a `SKILL.md` directory. Skills apply Guides rather than restating them.

## Wiring

How this repo and its Skills are linked into `~/.claude/` is machine setup, so it lives in the [dotfiles README](https://github.com/samthorold/dotfiles#claude-code). Imports read `@~/.claude/commons/...`; the global `~/.claude/CLAUDE.md` Imports `MAP.md`, the Global Guide and the Agentic development Guide.

## Changing it

Commit straight to `main`, no PR, as in dotfiles. A new Skill is written from a Procedure already carried out by hand, not in advance (candidates waiting on a first run: Promotion sweep, Propagation, Adoption). A Revision's reason goes in the commit message. Keep it free of secrets and private details: the repo is public.
