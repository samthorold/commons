---
address: guides/flutter.md
origin: a private Adopter (see the portfolio)
signal: trap
---

In Flutter widget tests, `scrollUntilVisible(finder, …)` stops as soon as the widget is built, and a scrollable builds items in its cache area just off screen, so the following tap misses (with a warning, or no effect). Pass `finder.hitTestable()` so it scrolls until the widget can actually be tapped.
