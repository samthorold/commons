---
address: guides/flutter.md
origin: a private Adopter (see the portfolio)
signal: gap
---

Flutter (Dart) is now an Adopter's Stack, chosen because agents write most of the code: it is code-first with headless `flutter test`, one codebase serves Android and iOS, and its ads, billing and analytics plugins are first-party. No Guide covers it, so nothing completes the Global Guide's *Checks and CI* for it: how pre-commit, the Flutter SDK and the tools (`dart format`, `dart analyze`, `flutter test`) are installed and pinned, how CI gets the pinned Flutter, and how a Dart workspace monorepo is laid out. The first repo to set it up decides these alone, and a Flutter Guide should be written from that repo once its checks run.
