# The template's docs

- [ADOPT.md](ADOPT.md): the prompt that makes a repository djazairdev ready with a coding agent.
- [CHECKLIST.md](CHECKLIST.md): what "djazairdev ready" means, item by item. **Required** items are the Hub's seven checks, **Recommended** items keep a project healthy, **Optional** items depend on the project.

## What's here

| File | What it is | In a project |
|---|---|---|
| [`docs/`](.) | These docs | Deleted after use |
| [`README.template.md`](../README.template.md) | A short README: badges, quick start, first contribution, feedback | Becomes `README.md` |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | How to set up, test and send a pull request, with the pledge | Kept, filled in |
| [`AGENTS.md`](../AGENTS.md) | Instructions for coding agents working in the project | Kept, filled in |
| [`CHANGELOG.md`](../CHANGELOG.md) | Versions, newest first, written by release-please | Kept |
| [`LICENSE`](../LICENSE) | MIT | Kept, with the project's copyright holder |
| [`.editorconfig`](../.editorconfig), [`.gitattributes`](../.gitattributes) | Line endings and indentation | Kept |
| [`.github/dependabot.yml`](../.github/dependabot.yml) | Weekly dependency updates | Kept, with the project's package managers |
| [`.github/rulesets/`](../.github/rulesets/) | The default branch's ruleset, to import | Kept, with the project's test jobs |
| [`starters/ci/`](../starters/ci/) | CI for Python, JavaScript and TypeScript, PHP, Go, Rust, Flutter and Dart, and static sites and datasets with Cloudflare deploys | One becomes `.github/workflows/ci.yml` |
| [`starters/release-please/`](../starters/release-please/) | Semantic versions, tags, GitHub releases and the changelog, from pull request titles | Workflows to `.github/workflows/`, JSON files to the root |
| [`.github/workflows/template.yml`](../.github/workflows/template.yml) | Checks the template itself | Deleted |

The code of conduct, the security policy, the support page and the issue forms aren't here: every repository in the organisation inherits them from [djazairdev/.github](https://github.com/djazairdev/.github). A project outside the organisation copies them from there.

## Changing the template

Open a pull request. Every starter must pass the [template's CI](../.github/workflows/template.yml), which lints the workflows. When a change matters to projects that already adopted the template, raise the version in `AGENTS.md` and `ADOPT.md` and add a line below, so the next run of `ADOPT.md` picks it up.

## Versions

- **1.3.0** (2026-10-10): a short README that leads to a first contribution: badges (CI, latest release, good first issues, ideas by votes), quick start, *Make your first contribution*, *Feedback* (Discussions, bug and idea forms, the Facebook Page, in English), licence. Long docs go in `docs/`. The template's own docs moved to `docs/`.
- **1.2.0** (2026-10-10): releases with release-please (C6) replace the changelog script: Conventional Commit pull request titles, checked by `pr-title.yml`; squash merges only; the ruleset requires `PR title`. README badges (C11). The optional items are renumbered O1–O3.
- **1.1.0** (2026-10-10): `.github/rulesets/main.json`, the default branch's ruleset, which each repository imports (C3). R4 asks for a beginner label, not 3 open issues (Hub decision D27).
- **1.0.0** (2026-10-09): the first version.
