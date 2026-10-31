---
address: guides/model-calls.md
origin: samthorold/go-slow PR #251 (found running PR #248's migration)
signal: trap
---

A migration to a new record shape can make a "what's new since the last run" query see the whole backlog. The daily summary act was shown the items *first processed since the previous summary*. The new processing step (cutting text into spans) had never run on the existing items, so the first run after the switch processed all of them at once. The next summary would have been handed every item in the record in one model call: far past any normal input, over the long-context price step, or failing outright. Tests on fresh records couldn't see it, and nor could the migration test. It surfaced only as a dry run against the real record that priced 0 requests because nothing had been processed yet.

How it would apply: when a migration or a new step changes what marks an item as new, say how the first run after it treats existing items, and bound every model-calling act's input by a cutoff the switch records (items collected after it), not by the step's own first-run timestamps. A priced dry run against the real record before the first live run catches it.
