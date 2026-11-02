# Web apps Guide: twelve-factor, wired in `main`

How to apply the Stance *twelve-factor, wired in `main`*, from [the Web apps Guide](../web-apps.md#stance-twelve-factor-wired-in-main), which states the Stance.

## Why, in full

An app constructed from its dependencies is tested by constructing it with the ones the test wants, with nothing to patch and no heavy mocking. A factory keyed on an environment name hides the wiring, and named environments multiply with every new deploy (12factor, *Config*). Config in the environment also keeps credentials out of the repo, so a repo can go public without a scrub.

## How to apply

- **Backing services are attached resources:** swapping the database for another instance is a change of config, never of code (12factor, *Backing services*).
- **Dev/prod parity:** every deploy, the developer's included, uses the same backing services at the same versions (12factor, *Dev/prod parity*). docker-compose runs them locally, and runs the app from the same image with its environment set as in production. In-memory adapters are for tests, never a running app.
- **Logs are an event stream:** written unbuffered to stdout, never to files the app manages.
- **Disposable processes:** start in seconds; on SIGTERM stop accepting connections, finish in-flight requests, then exit.
- **Admin tasks are one-off processes** from the same codebase and config: migrations and fix-up scripts are commands of the app (e.g. a subcommand of its binary), not separate tooling.
- The repo carries a `.env.example` listing every variable with a safe local value; the real `.env` is gitignored.
