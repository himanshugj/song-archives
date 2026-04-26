#!/usr/bin/env python3
"""Query the song library by any frontmatter field.

Usage:
  query.py list                        — list all songs
  query.py all                         — dump all frontmatter
  query.py <field> <value>             — filter by field containing value

Examples:
  query.py scale pentatonic_minor
  query.py my_key "E minor"
  query.py status polished
  query.py techniques fingerpicking
  query.py roman_numerals "I V vi IV"
  query.py genre blues
  query.py capo 2
"""

import sys
from pathlib import Path

SONGS_DIR = Path(__file__).parent.parent / "songs"


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    data = {}
    for line in text[3:end].splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" in stripped:
            key, _, val = stripped.partition(":")
            val = val.strip()
            # strip inline comments
            if " #" in val:
                val = val[: val.index(" #")].strip()
            data[key.strip()] = val
    return data


def fmt(path: Path, fm: dict) -> str:
    title = fm.get("title") or path.stem
    artist = fm.get("artist", "")
    key = fm.get("my_key") or fm.get("original_key", "")
    status = fm.get("status", "")
    parts = [f"  {title} — {artist}"]
    meta = []
    if key:
        meta.append(f"key: {key}")
    if status:
        meta.append(f"status: {status}")
    if meta:
        parts.append(f"  [{', '.join(meta)}]")
    parts.append(f"  → {path.name}")
    return "".join(parts)


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return

    songs = sorted(SONGS_DIR.glob("*.md"))
    songs = [s for s in songs if s.name != ".gitkeep"]

    if not songs:
        print("No songs yet. Add one with: \"add [Song Title] by [Artist]\"")
        return

    if args[0] == "list":
        for p in songs:
            fm = parse_frontmatter(p)
            print(fmt(p, fm))
        return

    if args[0] == "all":
        for p in songs:
            fm = parse_frontmatter(p)
            print(f"\n{'─' * 52}")
            for k, v in fm.items():
                if v:
                    print(f"  {k}: {v}")
        return

    field = args[0]
    value = " ".join(args[1:]).lower()
    results = [
        (p, fm)
        for p in songs
        for fm in [parse_frontmatter(p)]
        if value in fm.get(field, "").lower()
    ]

    if not results:
        print(f"No songs found where '{field}' contains '{value}'")
        return

    print(f"\nSongs where '{field}' contains '{value}':\n")
    for p, fm in results:
        print(fmt(p, fm))


if __name__ == "__main__":
    main()
