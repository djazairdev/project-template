# Contributing

Thanks for helping. Newcomers are welcome: you don't need to be an expert, and no question is too small.

## Find something to work on

- Issues labelled [good first issue](../../issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) are small and well described. [help wanted](../../issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) issues need more context but are ready for anyone.
- Comment on the issue to say you're working on it, so no one else starts the same thing. If you stop, say so.
- For anything bigger than a small fix, open an issue first and agree on the approach.

## Set up

<!-- The exact commands: what to install (with versions), how to get the dependencies, how to run the project. -->

```bash
git clone https://github.com/OWNER/NAME
cd NAME
# install the dependencies
# run the project
```

## Run the tests

```bash
# the command CI runs, so a pull request passes there too
```

## Send a pull request

1. Fork the repository and create a branch from the default branch.
2. Make one change per pull request, with a test when you change behaviour.
3. Run the tests and the linter.
4. Open the pull request, say what it changes and why, and link the issue (`Closes #12`).
5. Give it a title in the [Conventional Commits](https://www.conventionalcommits.org) form, `type: what it does`:

   | Title | When |
   |---|---|
   | `fix: wrong code for Adrar` | A bug fix |
   | `feat: add postal codes` | A new feature |
   | `feat!: rename the code field` | A change that could break someone who uses the project |
   | `docs: explain the setup` | Documentation only; also `test:`, `ci:`, `chore:`, `refactor:`, `build:`, `style:`, `perf:` |

   A scope in brackets is optional: `fix(api): …`. A check fails until the title fits, and you can edit the title at any time.

CI runs the tests on every pull request. A maintainer reviews it; we may ask for changes, which is normal. Pull requests are squash-merged, so the title becomes the commit's message, and the changelog and the next version are made from it: don't edit `CHANGELOG.md` yourself.

## Our pledge

The maintainers reply to every newcomer's pull request within 7 days, even if only to say when we'll review it.

## Conduct and security

Everyone follows the [code of conduct](https://github.com/djazairdev/.github/blob/main/CODE_OF_CONDUCT.md). Report security problems privately, as [SECURITY.md](https://github.com/djazairdev/.github/blob/main/SECURITY.md) says, never in a public issue.

## Licence

By contributing, you agree that your work is released under the project's [licence](LICENSE).
