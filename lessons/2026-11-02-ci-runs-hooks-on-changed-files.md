---
address: guides/global.md#checks-and-ci
origin: samthorold/go-slow#281
signal: contradiction
---

Running `pre-commit run --all-files` in CI hands every file to every hook, which defeats each hook's `files:` filter, so every PR pays for every hook. Where one hook is expensive (a test suite of about 12 minutes), a docs-only PR pays the full cost for nothing. Running `pre-commit run --from-ref origin/<base> --to-ref HEAD` on pull requests keeps the Convention's point (CI runs exactly the hooks, as a local run does, under one job name) while honouring the same filters a local commit does. `--all-files` stays right where everything should be checked: a push changing pins, or a change to the hook config itself, which the filters should then name. The filters become load-bearing: each must name everything its hook depends on (for tests, recorded fixtures and `testdata/`), or CI skips a check it needed.
