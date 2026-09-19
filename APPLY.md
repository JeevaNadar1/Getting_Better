# How to apply this update

This archive is the complete repository as it should look after the update. Unzip it over
your working copy, delete one file, verify, then tag.

```bash
cd Getting_Better

# 1. Overlay the new and updated files (dotfiles included)
cp -R /path/to/Getting_Better_update/. .

# 2. Delete the duplicate spec — this is the only removal
git rm Getting_Better.md

# 3. Verify. Must exit zero.
make check
make release-check

# 4. Commit
git add -A
git commit -m "Add CI, contribution docs, issue templates; drop duplicate spec"
git push

# 5. Cut the first release. CI builds the bundle and attaches it automatically,
#    which fixes the dead download link in the README.
git tag -a v1.0.0 -m "v1.0.0"
git push --tags
```

## What changed

**New**

1. `.github/workflows/ci.yml`
2. `.github/PULL_REQUEST_TEMPLATE.md`
3. `.github/ISSUE_TEMPLATE/bug_report.yml`
4. `.github/ISSUE_TEMPLATE/feature_request.yml`
5. `.github/ISSUE_TEMPLATE/config.yml`
6. `CONTRIBUTING.md`
7. `CHANGELOG.md`
8. `CODE_OF_CONDUCT.md`
9. `.gitattributes`

**Updated**

1. `scripts/check_skill.py` — adds duplicate-spec detection, README phantom-file
   detection, and changelog presence checks.
2. `Makefile` — adds `version`, `release-check`, and `help` targets.
3. `README.md` — corrected Structure block, working install fallback, Contributing
   section.

**Deleted**

1. `Getting_Better.md` — byte-identical duplicate of `SKILL.md`.

**Untouched**

1. `SKILL.md`, `LICENSE`, `.gitignore`.

## One thing to fill in

`CODE_OF_CONDUCT.md` contains the placeholder `[maintainer contact]`. Replace it with an
email address, or delete that clause and leave only the GitHub private-report route.
