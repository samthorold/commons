---
address: guides/web-apps.md#responses-and-routing
origin: samthorold/go-slow#28
signal: contradiction
---

The Guide's example vendored file name, `htmx-2.0.11.min.js`, names a version that doesn't exist (the latest 2.x was 2.0.10 when checked), and htmx 4 has since been released. Several of the Guide's specifics (configuring `responseHandling` to swap 422) are htmx 2 behaviour. The Guide should say which htmx major it is written against, so an Adopter knows whether a newer major is a deliberate departure.
