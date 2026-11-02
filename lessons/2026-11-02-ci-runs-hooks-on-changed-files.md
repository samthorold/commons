---
address: guides/global.md#checks-and-ci
origin: samthorold/go-slow#281
signal: contradiction
---

Running `pre-commit run --all-files` in CI hands every file to every hook, which defeats each hook's `files:` filter, so every PR pays for every hook. Where one hook is expensive (a test suite of about 12 minutes), a docs-only PR pays the full cost for nothing. Running `pre-commit run --from-ref origin/<base> --to-ref HEAD` on pull requests keeps the Convention's point (CI runs exactly the hooks, as a local run does, under one job name) while honouring the same filters a local commit does. `--all-files` stays right where everything should be checked: a push changing pins, or a PR changing the hook config or a workflow. The workflow has to make that choice: when such a file changed, it runs `--all-files` instead of `--from-ref`. Adding the config to every hook's filter doesn't work, because a filter decides only whether a hook runs, not which files it sees, so a check-yaml run would still see only the changed files (shown in samthorold/go-slow#285). The filters become load-bearing: each must name everything its hook depends on (for tests, recorded fixtures and `testdata/`), or CI skips a check it needed.
