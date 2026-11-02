---
address: guides/global.md#checks-and-ci
origin: samthorold/go-slow#281
signal: contradiction
---

Making the test suite a pre-commit hook at the `pre-commit` stage runs it on every commit that touches code. That is unusual practice, and once the suite takes minutes it is too slow for a commit hook. The hook can sit at `stages: [pre-push]`, installed with `--hook-type pre-push`, while the fast hooks (formatting, linting, file checks) stay at commit. CI still runs both stages, so "a repo's checks are its hooks, and CI runs exactly them" still holds. The Python Guide also lists the tests among the hooks and would move with it.
