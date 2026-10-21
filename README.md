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

The whole repo is symlinked into `~/.claude/`, so Imports read `@~/.claude/commons/...`:

```sh
ln -s ~/Projects/commons ~/.claude/commons
```

Each Skill is symlinked into `~/.claude/skills/` on its own (other skills there come from elsewhere):

```sh
ln -s ~/.claude/commons/skills/grind-issues ~/.claude/skills/grind-issues
```

The global `~/.claude/CLAUDE.md` (in dotfiles) Imports `MAP.md`, the Global Guide and the Agentic development Guide.

## Changing it

Commit straight to `main`, no PR, as in dotfiles. A Revision's reason goes in the commit message. Keep it free of secrets and private details: the repo is public.
