---
address: guides/web-apps.md#testing
origin: samthorold/go-slow#155
signal: trap
---

Headless Chromium (`--headless=new --screenshot`, here Brave) never finishes a screenshot of a page that carries an htmx poll (`hx-trigger="every 30s"`): the page never goes idle, so the browser waits for it indefinitely. Passing `--virtual-time-budget=<ms>` and `--timeout=<ms>` makes it take the shot. Any hypermedia app that screenshots pages for a PR (a slice whose criterion is "the PR shows a screenshot") meets this on its first polling page. A brand-new profile directory also hung once where a reused one worked, which may be the same cause or a separate one.
