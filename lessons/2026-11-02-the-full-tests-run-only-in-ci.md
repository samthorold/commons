---
address: guides/global.md#checks-and-ci
origin: samthorold/go-slow#281
signal: contradiction
---

Making the full test suite a pre-commit hook runs it locally on every commit that touches code, and an agent also runs the full check before opening a PR, so a suite that takes minutes is paid locally and then again in CI. Moving it to the pre-push stage only moves the duplicate. Running it locally buys a few minutes' earlier warning, but an agent waits on CI anyway. The hook can sit at `stages: [manual]` instead: it runs only when asked (`pre-commit run --hook-stage manual <id>`), CI asks for it, and the fast hooks (formatting, linting, file checks) stay at commit. A hook with no `stages` runs at every stage, manual included, so one `pre-commit run --hook-stage manual` in CI runs the manual-only hooks and all the others, under one listing and one set of refs (samthorold/go-slow#285). "A repo's checks are its hooks, and CI runs exactly them" still holds. Locally the inner loop is the Stack's test command on the code being changed. The cost is a CI round trip for a failure only the full suite catches. The Python Guide also lists the tests among the hooks and would move with it, and so would whatever tells agents to run the full check before a PR (`grind-issues`' brief).
