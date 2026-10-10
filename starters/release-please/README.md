# Versions and releases with release-please

C6 in the [checklist](../../CHECKLIST.md). Every djazairdev project versions its releases the same way: [semantic versions](https://semver.org) tagged `v1.2.3`, worked out by [release-please](https://github.com/googleapis/release-please) from pull request titles. Nobody picks a version number or edits the changelog by hand.

## How it works

1. **Each pull request's title is a [Conventional Commit](https://www.conventionalcommits.org):** a type, an optional scope, and a summary. `pr-title.yml` checks it.

   | Title | Means | Next version |
   |---|---|---|
   | `fix: wrong code for Adrar` | A bug fix | Patch: 1.2.3 → 1.2.4 |
   | `feat: add postal codes` | A new feature | Minor: 1.2.3 → 1.3.0 |
   | `feat!: rename the code field` | A change that breaks users (`!`) | Major: 1.2.3 → 2.0.0 |
   | `docs:`, `test:`, `ci:`, `chore:`, `refactor:`, `build:`, `style:`, `perf:` | Everything else | None on its own (`perf:` is listed under fixes) |

   Before 1.0.0, a breaking change raises the minor version instead (`bump-minor-pre-major`).
2. **Pull requests are squash-merged,** so each one lands on `main` as a single commit named by its title, which is what release-please reads.
3. **On every push to `main`,** `release.yml` keeps one pull request open, *chore(main): release X.Y.Z*, with the next version and the new `CHANGELOG.md` entry. It updates as more changes land.
4. **Merging that pull request** tags `vX.Y.Z` and publishes the GitHub release, with the changelog entry as its notes. Release when you choose: the release pull request can wait.

Pull requests made with `GITHUB_TOKEN` start no workflows, so `release.yml` starts CI and the title check on the release pull request itself. Its checks then pass the ruleset like any other pull request.

## Set it up

1. Copy `release.yml` and `pr-title.yml` to `.github/workflows/`, and `release-please-config.json` and `.release-please-manifest.json` to the repository's root. The CI workflow must be `.github/workflows/ci.yml` with `workflow_dispatch` among its triggers, as the starters have.
2. Set `release-type` in `release-please-config.json` for the project, so release-please also updates its version file:

   | Project | `release-type` | Updates |
   |---|---|---|
   | Python | `python` | `pyproject.toml`, `setup.py` or `__init__.py` |
   | JavaScript, TypeScript | `node` | `package.json` and its lock file |
   | PHP | `php` | `composer.json` |
   | Go | `go` | Nothing: Go reads versions from tags |
   | Rust | `rust` | `Cargo.toml` and `Cargo.lock` |
   | Flutter, Dart | `dart` | `pubspec.yaml` |
   | Static site, dataset, anything else | `simple` | `version.txt` |

3. Put the latest released version in `.release-please-manifest.json`, or keep `0.0.0` if there is none yet. The first `feat:` then releases 0.1.0. Keep `CHANGELOG.md`'s old entries: release-please adds new ones above them.
4. In the ruleset, add `PR title` to the required checks and allow only squash merges. The template's [`.github/rulesets/main.json`](../../.github/rulesets/main.json) does both.
5. **(maintainer)** In *Settings → General → Pull Requests*: allow only **squash merging**, with the default commit message set to **Pull request title**. Or run:

   ```bash
   gh repo edit OWNER/NAME --enable-squash-merge --enable-merge-commit=false --enable-rebase-merge=false
   gh api -X PATCH repos/OWNER/NAME -f squash_merge_commit_title=PR_TITLE -f squash_merge_commit_message=PR_BODY
   ```

6. **(maintainer)** Check that *Settings → Actions → General → Allow GitHub Actions to create and approve pull requests* is on. It is for djazairdev's repositories.

## Publishing a package

To publish to npm, PyPI, crates.io, pub.dev or Packagist when a release is made, add the steps to the end of `release.yml`'s job, under `if: steps.release.outputs.release_created == 'true'`. A tag made with `GITHUB_TOKEN` starts no workflows, so a separate workflow `on: release` wouldn't run.
