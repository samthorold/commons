# Project knowledge Guide: research

How to brief research, what of it lands, and how a researcher's web tools fail. Detail for [the Project knowledge Guide](../project-knowledge.md#research-lands-as-an-opinion-and-a-signpost); the briefing rules apply its Stance [*domain claims come from sources, not recall*](../project-knowledge.md#stance-domain-claims-come-from-sources-not-recall), whose other rules are in [domain claims](domain-claims.md).

## Briefing research

- Brief research from the owner's question, not from a working hypothesis: the categories, candidate answers and framing collected so far stay out of the brief, and so does anything the briefer remembers (a rate added "as context"), or the research echoes them back as findings and can no longer say whether the framing was right. Delegated researchers, who see only the brief, are the most prone to this. Research that only confirms recall usually means a brief written from recall; the remedy is the brief, not skipping research.
- Where research replaces a document written from recall, no researcher or report writer sees that document. Once the report is written, the coordinator adds where the sources disagree with the document, and rewrites the document from the report.
- The brief names the kinds of source the question needs (forums for failures, filings for figures), and the note records any it couldn't reach as missing evidence, not negative, saying which way their absence biases the opinion.

## Research lands as an opinion and a signpost

What lasts from research is the opinion, not a summary of the readings. A summary mostly repeats what an agent would recall anyway, and loaded into context it dilutes the Stances that carry the value. So research lands as a Stance or other opinion at its layer (domain findings in the domain docs, measurements and project-specific analysis in `docs/research/<issue>-<slug>.md`, design in system design through a grill), with a signpost to its grounding: the sources and the evidence notes the Stance above asks for.

Research outputs (deep-research `research_notes/` and `reports/`, scratch runs) are working folders, not committed, and deleted once the opinion and its signpost have landed. The exception is a question that stays open across sessions: its outputs are committed beside the question, each pass labelled with how it was briefed, until a Stance exists to carry them.

## Known traps

How a research agent's web tools fail, so a brief can plan around them.

- **Guessed URLs 404, and professional registers can't be fetched.** Official pages move and manuals get renamed, so a URL from recall often fails and wastes a researcher's limited calls: search first, and fetch what the search returns. Registers (of tax advisers, lawyers, accountants) refuse fetches or show results only after an interactive search, so a report that needs registrations confirmed hands the owner a list of registers to check in a browser. *Remove when:* registers offer a query a fetch can read (guessed URLs will keep failing).
- **A fetch tool can return a PDF as unreadable binary**, and the researcher then reports the primary source unreadable and falls back to write-ups. Where the tool also saves the file, `pdftotext -layout <file> -` extracts it cleanly. A brief that expects PDFs (gazettes, rulings, government publications) says so. *Remove when:* the fetch tool returns a PDF's text.
- **A fetch tool that summarises a page flattens its tables**, and the summary can give a cell to the wrong row. Before a figure from a table goes into a domain doc, have the tool quote the table's cells in order and read the row off that; a brief can ask for it up front. *Remove when:* the fetch tool returns tables with their structure.
- **Forums are out of reach.** reddit.com refuses fetches and `site:reddit.com` searches return no threads, even when the brief names forums; the HN Algolia API (`hn.algolia.com/api/v1/search`) does reach developers' own posts. Expect forum evidence to be missing, and say so in the note. *Remove when:* fetches and searches reach forum threads.
