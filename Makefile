SKILL_NAME := getting-better
DIST       := dist
BUNDLE     := $(DIST)/$(SKILL_NAME).skill
PY         := python3

BUNDLE_PATHS := SKILL.md README.md LICENSE

.PHONY: all bundle check clean clean-bundle

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

## Structural validation: frontmatter, name match, description length, anchors.
check:
	@$(PY) scripts/check_skill.py

clean-bundle:
	@rm -rf $(DIST)

clean: clean-bundle
	@find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
