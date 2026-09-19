# Changelog

All notable changes to this skill are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) as applied to a behavioural
specification:

1. **Major** — the protocol changes in a way that alters existing behaviour, such as a
   removed playbook or a reversed default.
2. **Minor** — new playbooks, new sections, or broadened trigger coverage.
3. **Patch** — wording, anchor fixes, tooling, and documentation.

---

## [Unreleased]

### Added
1. `.github/workflows/ci.yml` — validates the skill, builds the bundle, and publishes
   tagged releases automatically.
2. `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, issue templates, and a pull request template.
3. `.gitattributes` for consistent line endings and correct language statistics.
4. Duplicate-file and version-consistency checks in `scripts/check_skill.py`.
5. `make release-check` and `make version` targets.

### Removed
1. `Getting_Better.md` — a byte-identical duplicate of `SKILL.md` with no references
   pointing at it. Two copies of a specification always drift.

### Fixed
1. README documented `.github/workflows/ci.yml` in its Structure block while the file was
   never committed.
2. README's install instructions linked to a releases page that contained no releases.

---

## [1.0.0] — 2026-09-19

### Added
1. `SKILL.md` — the complete self-contained protocol covering clarification batching,
   depth calibration, standing corrections, improvement tracking, and efficiency.
2. Domain playbooks for coding, creative writing, documents and prose, design and UI, and
   analysis, research and decisions.
3. Cross-cutting sections: Thinking, Clarification Protocol, Improvement Rate, Depth
   Calibration, Efficiency, Verify, and the Question Bank.
4. `scripts/check_skill.py` — structural validation of frontmatter, name match,
   description length, H1 count, internal anchors, and relative file references.
5. `Makefile` with `check`, `bundle`, and `clean` targets.
6. MIT licence and README with install paths for claude.ai, Claude Code, and Projects.

[Unreleased]: https://github.com/JeevaNadar1/Getting_Better/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/JeevaNadar1/Getting_Better/releases/tag/v1.0.0
