---
address: guides/global.md#checks-and-ci
origin: samthorold/go-slow#28
signal: trap
---

With actionlint run as a pre-commit hook (e.g. `rhysd/actionlint`), it shellchecks workflow `run:` steps only when a `shellcheck` binary is on PATH. GitHub's runners have one; a developer machine may not, and `shellcheck-py` installed as a separate hook doesn't put it on actionlint's PATH. A local run then passes a step that CI fails. The Global Guide asks for both hooks but doesn't say they must share a shellcheck.
