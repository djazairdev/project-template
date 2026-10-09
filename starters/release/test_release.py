"""Tests for release.py, run by the template's own CI (python3 -m unittest discover -s starters/release).
Not copied into projects. Standard library only."""
import contextlib
import io
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import release  # noqa: E402

CHANGELOG = """# Changelog

## Unreleased

- Soon.

## 1.1.0 (2026-11-02)

- New: [the guide](docs/guide.md).

## 1.0.0 (2026-10-09)

- First.
"""


class Release(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.saved = release.ROOT, release.REPOSITORY, os.environ.get('PATH')
        release.ROOT, release.REPOSITORY = self.tmp.name, 'owner/name'
        self.write(CHANGELOG)
        self.git('init', '-q')
        self.git('add', '-A')
        self.git('commit', '-q', '-m', 'test')

    def tearDown(self):
        release.ROOT, release.REPOSITORY, path = self.saved
        os.environ['PATH'] = path
        self.tmp.cleanup()

    def git(self, *args):
        subprocess.run(['git', '-c', 'user.name=test', '-c', 'user.email=test@example.invalid', *args],
                       cwd=self.tmp.name, check=True, capture_output=True)

    def write(self, text):
        with open(os.path.join(self.tmp.name, 'CHANGELOG.md'), 'w', encoding='utf-8') as f:
            f.write(text)

    def run_quietly(self, fn, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            fn(*args)
        return out.getvalue()

    def test_entries_skip_unreleased(self):
        found = release.entries(CHANGELOG)
        self.assertEqual([(v, d) for v, d, _ in found], [((1, 1, 0), '2026-11-02'), ((1, 0, 0), '2026-10-09')])
        self.assertEqual(found[0][2], '- New: [the guide](docs/guide.md).')

    def test_check(self):
        self.assertIn('v1.1.0 is new', self.run_quietly(release.check))
        self.git('tag', 'v1.1.0')
        self.assertIn('v1.1.0 is released', self.run_quietly(release.check))
        self.git('tag', 'v1.2.0')
        with self.assertRaises(SystemExit):
            release.check()

    def test_check_refuses_disorder_and_empty_entries(self):
        for text in (CHANGELOG.replace('1.1.0', '0.9.0'), CHANGELOG.replace('2026-11-02', '2026-01-01'),
                     CHANGELOG.replace('- First.', '')):
            self.write(text)
            with self.subTest(text=text), self.assertRaises(SystemExit):
                release.check()

    def test_publish(self):
        bin_dir = os.path.join(self.tmp.name, 'bin')
        os.makedirs(bin_dir)
        log = os.path.join(self.tmp.name, 'gh.log')
        with open(os.path.join(bin_dir, 'gh'), 'w') as f:
            f.write(f'#!/bin/sh\necho "$@" > {log}\nfor a; do case "$a" in *.md) cat "$a" >> {log};; esac; done\n')
        os.chmod(os.path.join(bin_dir, 'gh'), 0o755)
        os.environ['PATH'] = bin_dir + os.pathsep + os.environ['PATH']
        self.run_quietly(release.publish, 'abc123')
        with open(log, encoding='utf-8') as f:
            call = f.read()
        self.assertIn('release create v1.1.0 --target abc123 --title v1.1.0 (2026-11-02)', call)
        self.assertIn('[the guide](https://github.com/owner/name/blob/v1.1.0/docs/guide.md)', call)
        os.remove(log)
        self.git('tag', 'v1.1.0')
        self.assertIn('already released', self.run_quietly(release.publish, 'abc123'))
        self.assertFalse(os.path.exists(log))


if __name__ == '__main__':
    unittest.main()
