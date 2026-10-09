"""Tag and release each version in CHANGELOG.md (starters/release/README.md).

The version is the newest entry headed "## 1.2.3 (2026-10-09)". Its release is the git tag v1.2.3
and a GitHub release "v1.2.3 (2026-10-09)", with the entry as its notes.

    python3 .github/scripts/release.py check            # on pull requests: the changelog is in order
    python3 .github/scripts/release.py notes            # prints the newest entry
    python3 .github/scripts/release.py publish [SHA]    # tags SHA (default HEAD) and creates the
                                                        # release, unless the tag exists

check and publish need the repository's tags (fetch-depth: 0); publish needs gh and GH_TOKEN.
Standard library only, so it runs on any project's CI.
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.getcwd()
CHANGELOG = 'CHANGELOG.md'
HEADING = re.compile(r'^## (\d+)\.(\d+)\.(\d+) \((\d{4}-\d{2}-\d{2})\)[ \t]*$', re.M)
REPOSITORY = os.environ.get('GITHUB_REPOSITORY', '')


def entries(text):
    """[(version tuple, date, entry)] in the order they appear, each entry up to the next ## heading."""
    out = []
    for m in HEADING.finditer(text):
        rest = text[m.end():]
        end = re.search(r'^## ', rest, re.M)
        out.append((tuple(int(n) for n in m.groups()[:3]), m.group(4), rest[:end.start() if end else None].strip()))
    return out


def name(version):
    return '.'.join(map(str, version))


def read():
    with open(os.path.join(ROOT, CHANGELOG), encoding='utf-8') as f:
        found = entries(f.read())
    if not found:
        raise SystemExit(f'{CHANGELOG}: no entry headed "## 1.2.3 (YYYY-MM-DD)" yet, so nothing to release.')
    return found


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout


def released():
    """The versions tagged so far, as tuples."""
    out = set()
    for tag in git('tag', '--list', 'v*').split():
        m = re.fullmatch(r'v(\d+)\.(\d+)\.(\d+)', tag)
        if m:
            out.add(tuple(int(n) for n in m.groups()))
    return out


def check():
    found = read()
    versions = [v for v, _, _ in found]
    dates = [d for _, d, _ in found]
    if versions != sorted(set(versions), reverse=True):
        raise SystemExit(f'{CHANGELOG}: the versions must be newest first, each once.')
    if dates != sorted(dates, reverse=True):
        raise SystemExit(f'{CHANGELOG}: the dates must be newest first.')
    for version, _, entry in found:
        if not entry:
            raise SystemExit(f'{CHANGELOG}: the entry for {name(version)} is empty.')
    newest, tags = versions[0], released()
    if tags and newest < max(tags):
        raise SystemExit(f'{CHANGELOG}: the newest entry, {name(newest)}, is older than the last release, '
                         f'v{name(max(tags))}.')
    if newest in tags:
        print(f'v{name(newest)} is released.')
    else:
        print(f'v{name(newest)} is new: it is released once the default branch passes CI.')


def release_notes(entry, tag):
    """An entry as release notes: relative links point to the files at the tag."""
    if not REPOSITORY:
        return entry
    return re.sub(r'\]\((?!https?://|#|mailto:)([^)]+)\)', rf'](https://github.com/{REPOSITORY}/blob/{tag}/\1)', entry)


def publish(sha):
    check()
    version, date, entry = read()[0]
    tag = 'v' + name(version)
    if version in released():
        print(f'{tag} is already released.')
        return
    with tempfile.TemporaryDirectory() as tmp:
        notes = os.path.join(tmp, 'notes.md')
        with open(notes, 'w', encoding='utf-8') as f:
            f.write(release_notes(entry, tag) + '\n')
        subprocess.run(['gh', 'release', 'create', tag, '--target', sha, '--title', f'{tag} ({date})',
                        '--notes-file', notes], cwd=ROOT, check=True)
    print(f'Released {tag}.')


def main():
    args = sys.argv[1:]
    if args == ['check']:
        check()
    elif args == ['notes']:
        print(read()[0][2])
    elif args[:1] == ['publish'] and len(args) <= 2:
        publish(args[1] if len(args) == 2 else git('rev-parse', 'HEAD').strip())
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main()
