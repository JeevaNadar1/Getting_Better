# Getting Better

A Claude Skill that front-loads clarifying questions, kills padded output, and locks
corrections in as standing rules — so every response gets sharper instead of repeating the
same mistakes.

Humans get better every time they make a mistake and understand something new. That
ability isn't limited to humans. I wanted my Claude supercharged at learning and improving,
and that is why I built this. Use the skill and Claude gets sharper with every step
forward.

---

## What it does

1. **Batches 5–10 clarifying questions with sensible defaults** before starting substantial
   work, instead of trickling questions out one at a time across four turns.
2. **Produces dense, no-padding output** — no hedges, no restating the question back, no
   explaining what you already know.
3. **Carries corrections forward as standing rules** for the rest of the session, so a fix
   given once never has to be given twice.
4. **Calibrates depth to the task** — a one-line fix does not get a five-question intake.
5. **Tracks improvement across the conversation**, so round four is measurably better than
   round one rather than the same class of mistake in new clothes.

---

## Coverage

The protocol is domain-general, with dedicated playbooks for each:

| Area | Playbook |
|---|---|
| Coding | build order, interface-first, failure modes |
| Creative writing | voice, specificity, anti-slop |
| Documents and prose | structure, compression, register |
| Design and UI | taste, hierarchy, intentional choices |
| Analysis, research, decisions | evidence discipline, trade-off framing |

Plus cross-cutting sections: Thinking, Clarification Protocol, Improvement Rate, Depth
Calibration, Efficiency, Verify, and a Question Bank.

---

## When it triggers

Any task involving building, writing, coding, designing, analyzing or planning — especially
short or open-ended requests like "build me X", "help me with Z", "make this better". Also
when you tell Claude its output was generic, shallow, padded or off-target.

It deliberately skips lightweight Q&A and casual exchange. A factual lookup does not need a
protocol.

---

## Install

**Claude.ai / Claude Desktop** — download `getting-better.skill` from the
[latest release](https://github.com/JeevaNadar1/Getting_Better/releases), then upload it in
Settings → Capabilities → Skills.

To build the bundle from source:

```bash
make bundle          # writes dist/getting-better.skill
```

**Claude Code** — clone into your skills directory. The directory name must be
`getting-better`, matching the `name:` field in `SKILL.md`:

```bash
git clone https://github.com/JeevaNadar1/Getting_Better.git ~/.claude/skills/getting-better
```

**Claude Projects** — paste the contents of `SKILL.md` into project instructions. The file
is self-contained, so this works without modification.

---

## Constraints, stated plainly

1. The question batch is capped at 10. It is an intake, not an interrogation.
2. Defaults must be stated explicitly, not implied, so you can skip answering and still get
   a correct-by-default result.
3. Nothing already answered or corrected earlier in the session gets re-asked.
4. It scales down. Trivial tasks bypass the protocol entirely.
5. Output favours substance over scaffolding — no filler headers, no repeated summaries.

---

## Structure

```
getting-better/
├── SKILL.md                      the complete protocol, self-contained
├── LICENSE                       MIT
├── Makefile                      make bundle / make check / make clean
├── scripts/check_skill.py        frontmatter, naming and anchor validation
└── .github/workflows/ci.yml      runs the validator and the bundle check
```

`SKILL.md` is currently a single self-contained file. It uploads to Claude as-is and reads
as documentation in the repository.

---

## License

MIT. See [LICENSE](LICENSE).
