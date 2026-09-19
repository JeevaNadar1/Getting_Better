# Contributing

This repository holds one Claude Skill. The working tree is the source of truth; anything
in `dist/` is a build artefact and is never edited by hand.

---

## Before you open a PR

1. Run `make check`. It must exit zero. CI runs the same command and gates the merge.
2. Run `make bundle`. The archive must build and contain `SKILL.md` with intact
   frontmatter.
3. Load the modified `SKILL.md` into Claude and exercise it against at least two real
   prompts — one that should trigger the skill, one that should not. Paste both outcomes
   into the PR description.
4. Update `CHANGELOG.md` under `## [Unreleased]`.

---

## Invariants

These are the rules the validator enforces, plus the ones it cannot.

1. The filename is `SKILL.md`, exactly. Claude discovers skills by that literal name;
   anything else is invisible.
2. `name:` in the frontmatter is `getting-better` and must match the bundle name and the
   install directory.
3. `description:` stays under 1024 characters. It currently sits at ~989, so any addition
   needs a matching deletion.
4. Exactly one H1 in the body. Sections are H2 and below.
5. Every in-document anchor resolves to a real heading. Renaming a heading means updating
   the Contents block in the same commit.
6. No duplicate copies of `SKILL.md` under another filename. A second copy always drifts,
   and readers cannot tell which one is live.
7. Relative file references must point at committed files.

---

## Changing the protocol itself

`SKILL.md` is a behavioural specification, not prose. Edits are judged on whether they
change model behaviour, not on whether they read well.

1. State the failure mode the change fixes. "The skill asked eleven questions for a
   one-line CSS fix" is a reason. "Clearer wording" is not.
2. Prefer deletion. The file is already ~28k tokens and is loaded in full on every
   trigger. Adding a section is a permanent tax on every conversation that fires the
   skill; justify it against that cost.
3. Keep instructions imperative and testable. "Cap the batch at 10 questions" is
   enforceable. "Be thoughtful about question count" is not.
4. New playbooks follow the existing section shape: trigger conditions, procedure,
   failure modes, worked example.
5. Do not add sycophancy, persona framing, or instructions that suppress disagreement.
   The skill exists to raise output quality, not agreeableness.

---

## Commit and branch conventions

1. Branch names: `fix/`, `feat/`, `docs/`, `chore/` followed by a short slug.
2. Commit subjects are imperative and under 72 characters — `Cap clarification batch at
   10`, not `Capped the batch`.
3. One logical change per commit. Protocol edits and tooling edits go in separate commits.

---

## Releasing

Maintainers only.

1. Move `## [Unreleased]` entries into a new dated version heading in `CHANGELOG.md`.
2. Commit, then tag: `git tag -a v1.1.0 -m "v1.1.0"` and `git push --tags`.
3. CI builds `getting-better.skill` and attaches it to the GitHub release automatically.
   Do not upload the bundle by hand.

---

## Reporting problems

Open an issue using the bug template. A useful report includes the prompt that triggered
the skill, the output you got, the output you expected, and which Claude surface you were
on (claude.ai, Desktop, Code, or Projects).
