# Web apps Guide: ports and adapters, with DDD only where it earns its keep

How to apply the Stance *ports and adapters, with DDD only where it earns its keep*, from [the Web apps Guide](../web-apps.md#stance-ports-and-adapters-with-ddd-only-where-it-earns-its-keep), which states the Stance.

## Why, in full

The logic worth having is where the app's value is, and it has to be testable without a browser or a database. Dressing every table as an aggregate buys ceremony for concepts with no rules; leaving rich rules in handlers scatters them across adapters, where they drift. The htmx authors' own shape is the same in MVC terms: thin controllers over a fat model, which is what lets a hypermedia API and a JSON API share one domain (*HS* 10).

## How to apply

- **One repository per aggregate root**, not per table.
- **Lightweight CQRS:** commands go through the domain; queries return view-model DTOs and may read the store directly, with the joins and aggregates one screen needs. Not two databases, and not event sourcing, with one exception: a **record of judgements** (a model's, or several judges' side by side) is kept as events, with its views derived from them. *Why:* such a record is read as it stood at a time (by work run on it then, by feedback given then) and by a view choosing whose judgements it reads, and tables updated in place can answer neither without replaying a log. Configuration nobody judges stays CRUD, and text a source's terms may require forgetting is kept outside the events.
- Templates render **view models, never domain entities**.
- Each design doc says which concepts are domain and which are CRUD today, and why.
