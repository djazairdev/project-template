# Releases from the changelog

Optional (O1 in the [checklist](../../CHECKLIST.md)). Each time a new version reaches `CHANGELOG.md` on `main` and CI passes, this tags the commit `v1.2.3` and creates a GitHub release with the changelog entry as its notes. It works for any language: the script needs only Python, which GitHub's runners have.

## Set it up

1. Copy `release.yml` to `.github/workflows/release.yml` and `release.py` to `.github/scripts/release.py`.
2. Name the CI workflow `CI` (`name: CI`), or change `workflows: [CI]` in `release.yml`.
3. Head each released entry in `CHANGELOG.md` with its version and date: `## 1.2.3 (2026-10-09)`. Entries headed otherwise, such as *Unreleased*, are skipped.

## How it works

- **On every pull request**, `release.py check` fails if the entries aren't newest first, if one is empty, or if the newest version is older than the last tag.
- **After CI passes on `main`**, `release.py publish` tags the commit and creates the release, unless that version's tag exists. A merge without a new version releases nothing.

To release, rename *Unreleased* to the next version and today's date in a pull request. Attach files to a release with `gh release upload v1.2.3 FILE` in a step after it.
