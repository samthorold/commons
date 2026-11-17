---
address: guides/go.md
origin: samthorold/go-slow#334
signal: trap
---

Go's `time.Parse` reads a zone abbreviation it doesn't know (such as "EST" in an RSS 2.0 `pubDate`, RFC 822) as a zone of that name with a zero offset, not as an error, so a date from an American feed parses silently five hours wrong. A feed reader maps the named zones it meets to their offsets by hand (or parses with `time.ParseInLocation` against a known location) and tests a date in each. Addressed to the missing Go Guide.
