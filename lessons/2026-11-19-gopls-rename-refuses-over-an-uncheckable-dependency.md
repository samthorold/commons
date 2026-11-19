---
address: guides/go.md
origin: samthorold/go-slow#349
signal: trap
---

`gopls rename` refuses ("package has errors") in any package that imports a dependency gopls can't type-check, even when `go build` and `go vet` are clean. One very large generated SDK package (`anthropic-sdk-go`, some 120k lines) is enough: `gopls check` reports its types as undefined. A rename across such packages needs another tool: a careful search and replace, checked with `go vet ./...` and the tests. A brief for a rename shouldn't rely on gopls.
