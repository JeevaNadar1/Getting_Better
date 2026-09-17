#!/usr/bin/env python3
"""Structural validation for the getting-better skill.

Catches the defects that stop a Claude Skill from loading at all, plus the
documentation drift that makes it load but behave wrongly. Exits non-zero on
any failure so CI and `make check` both gate on it.
"""

import pathlib
import re
import sys

SKILL_PATH = pathlib.Path("SKILL.md")
EXPECTED_NAME = "getting-better"
DESC_LIMIT = 1024

failures: list[str] = []
notes: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)
    print(f"FAIL  {msg}")


def ok(msg: str) -> None:
    print(f"ok    {msg}")


def warn(msg: str) -> None:
    notes.append(msg)
    print(f"warn  {msg}")


# 1. The file Claude actually looks for must exist and be named exactly SKILL.md.
if not SKILL_PATH.exists():
    fail("SKILL.md not found. Claude loads skills by this exact filename; a skill "
         "named anything else will not be discovered.")
    sys.exit(1)
ok("SKILL.md present")

text = SKILL_PATH.read_text(encoding="utf-8")

# 2. YAML frontmatter must open the file.
if not text.startswith("---\n"):
    fail("SKILL.md does not open with '---' frontmatter")
    sys.exit(1)

parts = text.split("---", 2)
if len(parts) < 3:
    fail("frontmatter block is not closed with a second '---'")
    sys.exit(1)

frontmatter, body = parts[1], parts[2]
ok("frontmatter block parsed")

# 3. name: must exist and match the directory/bundle name.
name_match = re.search(r"^name:\s*(.+?)\s*$", frontmatter, re.M)
if not name_match:
    fail("frontmatter has no 'name:' field")
else:
    name = name_match.group(1)
    if name != EXPECTED_NAME:
        fail(f"frontmatter name is '{name}', expected '{EXPECTED_NAME}' — "
             "must match the skill directory and bundle name")
    else:
        ok(f"name: {name}")

# 4. description: must exist, be substantial, and fit the platform limit.
desc_match = re.search(r"^description:\s*(.+?)\s*$", frontmatter, re.M)
if not desc_match:
    fail("frontmatter has no 'description:' field — Claude uses this to decide "
         "when to trigger the skill")
else:
    desc = desc_match.group(1)
    if len(desc) > DESC_LIMIT:
        fail(f"description is {len(desc)} chars, over the {DESC_LIMIT} limit")
    elif len(desc) < 80:
        fail(f"description is only {len(desc)} chars — too thin to trigger reliably")
    else:
        ok(f"description: {len(desc)} chars (limit {DESC_LIMIT})")
        if len(desc) > DESC_LIMIT * 0.95:
            warn(f"description is within 5% of the {DESC_LIMIT} limit; "
                 "future edits will overflow")

# 5. Exactly one H1, and it must be a title rather than a section.
h1s = re.findall(r"^# (.+)$", body, re.M)
if len(h1s) != 1:
    fail(f"expected exactly 1 H1 heading, found {len(h1s)}")
else:
    ok(f"H1: {h1s[0]}")

# 6. Every in-document anchor link must resolve to a real heading.
headings = set()
for level, raw in re.findall(r"^(#{1,6}) (.+)$", body, re.M):
    slug = raw.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    headings.add(slug)

anchors = re.findall(r"\]\(#([\w-]+)\)", body)
broken = sorted({a for a in anchors if a not in headings})
if broken:
    fail(f"{len(broken)} broken internal anchor(s): {', '.join(broken)}")
else:
    ok(f"{len(anchors)} internal anchors, all resolve")

# 7. Relative file references must exist. Guards the progressive-disclosure
#    failure mode: a reference pointing at a file that was never committed.
refs = re.findall(r"\]\((?!https?://|#)([\w./-]+\.(?:md|py|json|csv|yml|yaml))\)", body)
missing = sorted({r for r in refs if not pathlib.Path(r).exists()})
if missing:
    fail(f"referenced but not committed: {', '.join(missing)}")
elif refs:
    ok(f"{len(refs)} relative file references, all present")

# 8. Size report. Not a failure — a standing cost signal.
chars = len(text)
approx_tokens = chars // 4
print(f"\ninfo  SKILL.md: {chars:,} chars, {body.count(chr(10)):,} lines, "
      f"~{approx_tokens:,} tokens loaded per trigger")
if approx_tokens > 20000:
    warn(f"~{approx_tokens:,} tokens is a large always-loaded payload. Consider "
         "progressive disclosure: a lean SKILL.md plus references/ loaded on demand.")

print()
if failures:
    print(f"{len(failures)} failure(s).")
    sys.exit(1)
print(f"All structural checks passed{f' ({len(notes)} warning(s))' if notes else ''}.")
