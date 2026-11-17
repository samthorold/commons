---
address: guides/project-knowledge/system-design.md
origin: samthorold/go-slow#333
signal: gap
---

Code comments that cite a system-design section by its heading ("(system design: *Weaving runs at most once a day*)") drift silently when the heading is renamed: one docs pass found eight such citations naming sections that no longer existed, and nothing checked them. The Project knowledge Guide puts reasons in the design and facts in the code, which invites these links, but says nothing about keeping them true. Either cite design sections from code sparingly (the package doc only), or check citations against the design's headings (a test or hook that greps the cited titles).
