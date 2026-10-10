# djazairdev project template

Everything a project needs to join [djazairdev](https://github.com/djazairdev) and be listed in the [djazair.dev Hub](https://github.com/djazairdev/djazair.dev/blob/main/CONTRIBUTING.md#list-a-project-in-the-hub): the files, the checklist they meet, and a prompt that sets them up with a coding agent, for a new project or an existing one.

## Use it

**A new project:** click **Use this template** above, then open the new repository with a coding agent and ask it:

> Follow ADOPT.md in this repository.

**An existing project**, in the djazairdev organisation or not: open it with a coding agent and ask:

> Follow https://github.com/djazairdev/project-template/blob/main/ADOPT.md to make this repository djazairdev ready.

The agent compares the project with the [checklist](CHECKLIST.md), asks you a few questions, adds what is missing without overwriting what you have, runs the tests, and tells you what only a maintainer can do, such as adding the `djazairdev` topic. It doesn't push, open issues or change settings until you say so. Any agent that reads files and runs commands works: Claude Code, Codex, Cursor, Copilot and others.

Run it again later to pick up changes to the template: `AGENTS.md` records the version a project last adopted.

## What "djazairdev ready" means

The [checklist](CHECKLIST.md) has three levels:

- **Required:** the Hub's seven checks. An open-source licence, a commit in the last 90 days, a README and a CONTRIBUTING file, the `good first issue` or `help wanted` label, the pledge to reply to newcomers' pull requests within 7 days, the `djazairdev` topic, and a link to Algeria.
- **Recommended:** CI on every pull request, a protected default branch, code scanning, dependency updates, automatic semantic versions and releases, `AGENTS.md`, consistent files, and README badges.
- **Optional:** deploys from CI, an Arabic README, Discussions.

## What's here

| File | What it is | In a project |
|---|---|---|
| [`ADOPT.md`](ADOPT.md) | The prompt for coding agents | Deleted after use |
| [`CHECKLIST.md`](CHECKLIST.md) | What "djazairdev ready" means, item by item | Deleted after use |
| [`README.template.md`](README.template.md) | A README to fill in, with the badges | Becomes `README.md` |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to set up, test and send a pull request, with the pledge | Kept, filled in |
| [`AGENTS.md`](AGENTS.md) | Instructions for coding agents working in the project | Kept, filled in |
| [`CHANGELOG.md`](CHANGELOG.md) | Versions, newest first, written by release-please | Kept |
| [`LICENSE`](LICENSE) | MIT | Kept, with the project's copyright holder |
| [`.editorconfig`](.editorconfig), [`.gitattributes`](.gitattributes) | Line endings and indentation | Kept |
| [`.github/dependabot.yml`](.github/dependabot.yml) | Weekly dependency updates | Kept, with the project's package managers |
| [`.github/rulesets/`](.github/rulesets/) | The default branch's ruleset, to import | Kept, with the project's test jobs |
| [`starters/ci/`](starters/ci/) | CI for Python, JavaScript and TypeScript, PHP, Go, Rust, Flutter and Dart, and static sites and datasets with Cloudflare deploys | One becomes `.github/workflows/ci.yml` |
| [`starters/release-please/`](starters/release-please/) | Semantic versions, tags, GitHub releases and the changelog, from pull request titles | Workflows to `.github/workflows/`, JSON files to the root |
| [`.github/workflows/template.yml`](.github/workflows/template.yml) | Checks the template itself | Deleted |

The code of conduct, the security policy, the support page and the issue forms aren't here: every repository in the organisation inherits them from [djazairdev/.github](https://github.com/djazairdev/.github). A project outside the organisation copies them from there.

## Changing the template

Open a pull request. Every starter must pass the [template's CI](.github/workflows/template.yml), which lints the workflows. When a change matters to projects that already adopted the template, raise the version in `AGENTS.md` and add a line below, so the next run of `ADOPT.md` picks it up.

### Versions

- **1.2.0** (2026-10-10): releases with release-please (C6) replace the changelog script: Conventional Commit pull request titles, checked by `pr-title.yml`; squash merges only; the ruleset requires `PR title`. README badges (C11). The optional items are renumbered O1–O3.
- **1.1.0** (2026-10-10): `.github/rulesets/main.json`, the default branch's ruleset, which each repository imports (C3). R4 asks for a beginner label, not 3 open issues (Hub decision D27).
- **1.0.0** (2026-10-09): the first version.

## Licence

[MIT](LICENSE). Projects made from the template choose their own licence.
