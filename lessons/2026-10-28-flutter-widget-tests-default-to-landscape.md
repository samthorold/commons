---
address: guides/flutter.md
origin: a private Adopter (see the portfolio)
signal: trap
---

Flutter widget tests render on an 800×600 logical surface (landscape) by default. A phone app's portrait layout can overflow there, so a layout change breaks tests that never touch it, and size assertions (touch targets, a board fitting the width) test a screen no player has. Tests that care about layout set `tester.view.physicalSize` and `devicePixelRatio` to a named phone size (e.g. 360×640 dp) and reset them in `addTearDown`; the font scale likewise via `tester.platformDispatcher.textScaleFactorTestValue`. A related point for slicing: an acceptance criterion about size ("cells at least 48 dp") should name the screen width it holds at, or it may be unmeetable on the phones it's for.
