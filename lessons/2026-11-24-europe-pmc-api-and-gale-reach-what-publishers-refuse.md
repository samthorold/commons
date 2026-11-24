---
address: guides/project-knowledge/research.md
origin: samthorold/explorers#880
signal: trap
---

A research agent's fetch tools are refused by most publishers (ScienceDirect, Royal Society and similar answer 403; ADS returns an empty page; PMC's own pages can return a browser check), which costs time on every older paper. Two routes worked: Europe PMC's REST API (`www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&resultType=core`) returns a paper's full abstract as JSON, a reliable "abstract only" for papers indexed there; and Gale records (go.gale.com) sometimes give a fetch tool a review's full text that its publisher refuses. Neither is a full read of a paywalled paper, so evidence-quality notes still say which route was used.
