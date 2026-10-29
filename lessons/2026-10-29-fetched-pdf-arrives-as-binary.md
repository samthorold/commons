---
address: guides/project-knowledge.md#stance-domain-claims-come-from-sources-not-recall
origin: a private Adopter (see the portfolio), legal and tax research slices
signal: trap
---

WebFetch returns a compressed PDF as unreadable binary, so a research agent reports the primary source as unreadable and falls back to secondary write-ups. But the tool also saves the file, and `pdftotext -layout <saved file> -` extracts it cleanly. This worked for official gazettes, tax-authority rulings, a data-protection board and government publications, where the PDF is often the only primary text. A research brief that expects PDFs should say so.
