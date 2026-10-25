---
address: guides/web-apps.md#responses-and-routing
origin: samthorold/go-slow#51
signal: gap
---

A command that can be issued from several pages (undoing a piece of feedback from the page it was given on, or from a list of all of it) has no stated pattern for where its `303` lands. A single route has to guess the page to return to, or read it from `Referer` or a hidden field, which brings back the request-dependent response shape that *one URL, one response shape* avoids. What worked: one route per page the command is issued from, nested under that page's resource (`PUT /<page>/feedback/{id}/undone`), each answering `303` to its own page, all calling the same use case. The duplication is only in the thin handler. A one-line rule under *Responses and routing* would settle it.
