# The djazairdev ready checklist

What a project needs before it joins djazairdev. **Required** items are the seven checks the [djazair.dev Hub](https://github.com/djazairdev/djazair.dev/blob/main/CONTRIBUTING.md#list-a-project-in-the-hub) runs before it lists a project. **Recommended** items are what keeps a project healthy once people start using it and contributing. **Optional** items depend on the project.

Some items are settings only a maintainer can change, marked **(maintainer)**. A coding agent following [ADOPT.md](ADOPT.md) prepares everything else and lists those for you.

## Required

| # | Item | How to meet it | How to check |
|---|---|---|---|
| R1 | An open-source licence | A `LICENSE` file in the root with an OSI-approved licence, unchanged so GitHub recognises it. MIT is our default. A dataset may use an open data licence instead (CC0, CC BY 4.0, CC BY-SA 4.0, ODbL, ODC-By or PDDL), for example code under MIT in `LICENSE` and data under CC0 in `LICENSE-data`. | The repository page shows the licence's name in *About* |
| R2 | Recent activity | At least one commit on the default branch in the last 90 days | The latest commit's date |
| R3 | README and CONTRIBUTING | `README.md` says what the project does, for whom, and how to run it. `CONTRIBUTING.md` says how to set it up, run the tests and send a pull request. Keep both in the repository itself: they describe this project's setup, so the organisation has no default for them. | Both files exist in the root, `docs/` or `.github/` |
| R4 | Issues for newcomers | At least 3 open issues labelled `good first issue` or `help wanted`, each with the context a newcomer needs, where to start, when it's done, and a line such as `You'll need: Python, pytest` | The repository's issues, filtered by those labels |
| R5 | The maintainer pledge | The maintainers reply to newcomers' pull requests within 7 days. Say so in `CONTRIBUTING.md`, and set `maintainer_pledge: true` when you list the project. | `CONTRIBUTING.md` |
| R6 | The `djazairdev` topic **(maintainer)** | Add the topic `djazairdev` under *About → Topics* on the repository page | The repository page |
| R7 | Relevance to Algeria | Algerian maintainers, or a clear link to Algeria: local data, languages, payments, public services and so on. The README says which in its first lines. | A person reads the README |

Run checks R1 to R6 on a repository that's on GitHub with djazair.dev's checker (it needs only Python):

```bash
git clone --depth 1 https://github.com/djazairdev/djazair.dev
cd djazair.dev
python3 -m hub check-project owner/name --pledge
```

## Recommended

| # | Item | How to meet it |
|---|---|---|
| C1 | Code of conduct and security policy | Repositories in the djazairdev organisation inherit them from [djazairdev/.github](https://github.com/djazairdev/.github). A project outside it copies `CODE_OF_CONDUCT.md` and `SECURITY.md` from there and puts its own contact in them. |
| C2 | CI on every pull request | A workflow that runs the linter, the tests and the build on every pull request and every push to the default branch: start from [`starters/ci/`](starters/ci/) |
| C3 | A protected default branch **(maintainer)** | *Settings → Rules → Rulesets*: changes go through pull requests, and CI must pass |
| C4 | Code scanning **(maintainer)** | *Settings → Advanced Security*: CodeQL's default setup, Dependabot alerts and security updates, and private vulnerability reporting, which the security policy's *Report a vulnerability* button needs |
| C5 | Dependency updates | `.github/dependabot.yml` for GitHub Actions and the project's package managers |
| C6 | A changelog and versions | `CHANGELOG.md` with an entry for every release, and [semantic versions](https://semver.org) tagged `v1.2.3` |
| C7 | Instructions for coding agents | `AGENTS.md`: how to build and test the project, and its rules |
| C8 | Consistent files | `.editorconfig` and `.gitattributes`, so editors and operating systems agree on line endings and indentation |
| C9 | Issue forms | Repositories in the organisation inherit a bug form and an idea form. A repository that adds a form of its own loses the inherited ones, so it copies those it still wants. A label a form sets must exist in the repository. |
| C10 | No secrets in the repository | Secrets live in GitHub's *Settings → Secrets*, never in files; `.gitignore` covers local environment files such as `.env` |

## Optional

| # | Item | When |
|---|---|---|
| O1 | Releases from the changelog | When people download or depend on versions: [`starters/release/`](starters/release/) tags `v1.2.3` and creates a GitHub release from each new changelog entry |
| O2 | Deploys from CI | For a site or an API: deploy only from the default branch, after CI passes, behind a repository variable such as `DEPLOY_ENABLED` so deploys can be paused without touching secrets ([`starters/ci/static.yml`](starters/ci/static.yml)) |
| O3 | An Arabic README | Once a fluent speaker has reviewed it |
| O4 | Discussions **(maintainer)** | When questions outgrow issues |
