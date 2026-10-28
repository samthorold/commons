---
address: guides/web-apps.md#responses-and-routing
origin: samthorold/go-slow#156
signal: trap
---

A `<form>` rendered inside a `<p>` (an inline command button beside the text it acts on, e.g. an Undo next to a "given" mark) is pulled out of it by the browser's HTML parser: a `<form>` start tag closes an open `<p>`, so the control lands on a line of its own. End-to-end tests that assert on the HTML the server sent never see it, since the server's text is unchanged; only a browser (or a screenshot) shows it. In a hypermedia app, where every command is a small form placed inline, the container for text with a control beside it is a `<div>` or `<span>`, never a `<p>`.
