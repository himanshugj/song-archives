# Song Archives

A personal guitar learning library. Each song lives as one Markdown file in `songs/` with YAML frontmatter for structured metadata and freeform sections for personal notes and theory context.

---

## Adding a New Song

When the user says **"add [Song] by [Artist]"** or similar:

1. **Search the web** for: original recording key, chord progression, time signature, tempo, scale/mode, genre, primary techniques, and any notable music theory details (modal interchange, borrowed chords, why the progression works, etc.).
2. **Ask the user** for anything they've specified: their playing key (transposed), capo position, difficulty rating, status, and whether they have a tabs URL.
3. **Generate the filename**: `title--artist.md`, all lowercase, spaces → hyphens. Examples: `blackbird--the-beatles.md`, `hotel-california--eagles.md`.
4. **Copy the template** from `templates/song-template.md` into `songs/[filename].md`.
5. **Fill in the frontmatter** as completely as possible. Leave `personal_notes`, `tabs_url`, `last_played` empty unless provided by the user.
6. **Write the body sections**: "About This Song" (2–3 sentences of ground truth context), "Music Theory Notes" (what's interesting — modal interchange, why certain chords create tension, the characteristic sound of the scale), and "How to Play" (techniques, tricky parts).
7. Leave **Personal Notes** as an empty blockquote prompt — the user fills this themselves.
8. **Do not commit** the file — the user manages commits.

### Handling transpositions

If the user plays in a different key than the recording:
- Set `original_key` to the recorded key.
- Set `my_key` to their playing key.
- Set `capo` if they use one to achieve the transposition.
- In "How to Play", note any chord shape changes or capo reasoning.

---

## Updating a Song

- **Status change**: `status: learning → polished` when the user says they've mastered it.
- **Adding personal notes**: append to the Personal Notes section, preserving the blockquote format.
- **Last played**: update `last_played` date when the user mentions playing a song.

---

## Querying the Library

Use the query script directly:

```bash
python3 scripts/query.py list                        # all songs
python3 scripts/query.py scale pentatonic_minor      # by scale
python3 scripts/query.py my_key "E minor"            # by playing key
python3 scripts/query.py status polished             # songs I've mastered
python3 scripts/query.py techniques fingerpicking    # by technique
python3 scripts/query.py roman_numerals "I V vi IV"  # by progression
python3 scripts/query.py genre blues                 # by genre
python3 scripts/query.py capo 2                      # by capo position
```

Or grep directly for quick lookups:
```bash
grep -rl "scale: dorian" songs/
```

---

## Schema Reference

<!-- README_SYNC: When you add, remove, or rename frontmatter fields here, also update:
     1. The field table in README.md (under "Song File Format")
     2. templates/song-template.md (the template itself)
     These three sources must stay in sync. -->

All fields are optional but fill in as many as you can. See `templates/song-template.md` for the full template with inline comments.

| Field | Purpose |
|---|---|
| `instrument` | What the user is learning this on, e.g., `guitar`, `piano`, `ukulele` |
| `original_key` | Key as recorded, e.g., `F# minor` |
| `my_key` | Key the user actually plays in |
| `capo` | Fret number (0 = no capo) — guitar/ukulele only |
| `scale` | `major`, `natural_minor`, `pentatonic_major`, `pentatonic_minor`, `dorian`, `mixolydian`, `blues`, etc. |
| `mode` | `ionian`, `dorian`, `phrygian`, `lydian`, `mixolydian`, `aeolian`, `locrian` |
| `chord_progression` | Actual chords in `my_key`, e.g., `[Am, G, C, F]` |
| `roman_numerals` | e.g., `[i, VII, IV, VI]` — for cross-key pattern matching |
| `borrowed_chords` | Chords from the parallel scale or other modal borrowing |
| `techniques` | Instrument-specific techniques, e.g., `fingerpicking`, `barre_chords`, `pedaling`, `sight-reading` |
| `status` | `learning`, `polished`, `rusty`, `shelved` |
| `feel` | Vibe tags: `melancholic`, `upbeat`, `driving`, `dreamy`, `tense`, `resolved`, `sparse` |

---

## File Naming

`songs/title--artist.md`  
- Lowercase, hyphens for spaces, double-dash separates title from artist.  
- For "The" in artist names: `the-beatles` not `beatles`.  
- For featuring: `song-title--main-artist.md` (omit feat. artist from filename).
