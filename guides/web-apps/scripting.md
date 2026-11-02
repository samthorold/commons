# Web apps Guide: scripting is hypermedia-friendly

How to apply the Stance *scripting is hypermedia-friendly*, from [the Web apps Guide](../web-apps.md#stance-scripting-is-hypermedia-friendly), which states the Stance.

## Why, in full

The goal is less code, not less JavaScript (*HS* 9). State kept outside the DOM is lost or contradicted by the next swap; a widget that needs a JSON endpoint quietly reintroduces the data API this Guide rules out.

## How to apply

- a third-party widget must work on the DOM without a JSON endpoint; wrap a callback-style one so it dispatches an event, and let `hx-trigger` listen for it. Alpine or _hyperscript (the authors' own favourite) come in only when plain behaviours get unwieldy, and the app's design doc says so. For complex widgets use an established accessible library; no ARIA is better than bad ARIA.
