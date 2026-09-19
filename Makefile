SKILL_NAME := getting-better
DIST       := dist
BUNDLE     := $(DIST)/$(SKILL_NAME).skill
PY         := python3

BUNDLE_PATHS := SKILL.md README.md LICENSE

.PHONY: all bundle check clean clean-bundle version release-check help

all: check bundle

## Rebuild the .skill archive from the working tree. The tree is the source of
## truth; the bundle is a build artefact and is never edited by hand.
bundle: clean-bundle
	@mkdir -p $(DIST)/$(SKILL_NAME)
	@for p in $(BUNDLE_PATHS); do cp -R $$p $(DIST)/$(SKILL_NAME)/; done
	@cd $(DIST) && zip -qr $(SKILL_NAME).skill $(SKILL_NAME)
	@rm -rf $(DIST)/$(SKILL_NAME)
	@echo "built $(BUNDLE)"
	@unzip -l $(BUNDLE) | tail -3

## Structural validation: frontmatter, name match, description length, anchors,
## duplicate specs, README drift, changelog presence.
check:
	@$(PY) scripts/check_skill.py

## Latest released version according to the changelog.
version:
	@grep -m1 -oE '^## \[[0-9]+\.[0-9]+\.[0-9]+\]' CHANGELOG.md \
		| tr -d '#[] ' || echo "no released version"

## Pre-tag gate. Run this before cutting a release; CI runs the same steps.
release-check: check bundle
	@test -s CHANGELOG.md || { echo "CHANGELOG.md missing or empty"; exit 1; }
	@grep -q '^## \[Unreleased\]' CHANGELOG.md \
		|| { echo "CHANGELOG.md has no [Unreleased] section"; exit 1; }
	@unzip -p $(BUNDLE) $(SKILL_NAME)/SKILL.md | head -1 | grep -q '^---$$' \
		|| { echo "bundled SKILL.md lost its frontmatter"; exit 1; }
	@echo "release-check passed — safe to tag v$$($(MAKE) -s version)"

clean-bundle:
	@rm -rf $(DIST)

clean: clean-bundle
	@find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true

help:
	@grep -B1 -E '^[a-z-]+:' Makefile | grep -E '^##|^[a-z-]+:' \
		| sed 's/^## //' | paste - - 2>/dev/null || true
