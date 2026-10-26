---
address: guides/project-knowledge.md#stance-the-system-design-states-its-end-state-as-hypotheses
origin: samthorold/go-slow#8
signal: gap
waiting: a second Adopter whose user is its builder, or this Adopter's first quiet-window reading
---

When an Adopter's only user is also its builder, two things about its end state are worth stating generally.

- **Use as the top hypothesis is biased upward while it is being built**, because the builder opens the product to check their work as well as to use it. Filtering out days with commits doesn't work during active development, because it excludes nearly every day. What works is an asymmetric reading rule: a busy window can refute (if even the builder doesn't open it, that's strong evidence) but never support; *supported* needs a quiet window, declared by commit frequency.
- **The owner's own feedback, kept in the product's data and typed by kind, is a derived instrument** for the parts under the top. In a domain the project defines itself (the owner's interests), it serves where no outside ground truth exists. Its known error is that less feedback looks like improvement, so those readings hold only while the top is not refuted.

The Guide covers domains the project defines itself ("the rules are the source") but not how to read hypotheses when the judge is the builder.
