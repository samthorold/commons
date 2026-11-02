# Python Guide: releases

The *Releases* Conventions of [the Python Guide](../python.md#releases), which says when to read them.

- `release.yml` + `.github/scripts/release-check.sh` (copy from py-ev): on every push to `main`, if `v<version>` isn't tagged, build, tag and publish a GitHub Release with the distributions and generated notes; on PRs a dry run, failing if the PR changes the version to one already tagged.
- **Feature PRs never change the version.** A release is its own PR that only bumps it (`task bump -- patch|minor|major`). Never tag by hand. Hotfixes fix forward (fix, then a patch-bump PR).
- **The version-bump PR is the one that publishes a release when merged.** Whether and how it merges is the Agentic development Guide's PR workflow.
- A tag created by `GITHUB_TOKEN` triggers no other workflows, so release work belongs in `release.yml` itself.
