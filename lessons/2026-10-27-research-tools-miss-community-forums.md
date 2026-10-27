---
address: guides/project-knowledge.md#stance-domain-claims-come-from-sources-not-recall
origin: a private venture repo, three research notes (case histories, sale prices, revenue methods)
signal: trap
---

Delegated desk research couldn't reach Reddit (r/gamedev and similar), the likeliest home of small developers' failure stories. The sources that remained (press coverage, postmortems, vendor blogs) lean towards successes, so a case-history study came back biased towards hits, and probably understated how often later attempts do worse.

How it would apply: a research brief names the source kinds the question needs (community forums for failures, filings for figures) so the researcher reports which it couldn't reach. The note then records that evidence as missing, not negative, and says which way its absence biases the opinion.

Naming forums in the brief isn't enough to reach them. In two later research runs whose briefs named forums and marketplaces explicitly, the researchers still reached no forum threads: WebFetch is refused by reddit.com and old.reddit.com, and WebSearch with `site:reddit.com` returns no threads. One route did work: the HN Algolia API (`hn.algolia.com/api/v1/search`), which reaches developers' own posts. A Procedure for research could name the routes that work, or say up front that forum evidence is expected to be missing.
