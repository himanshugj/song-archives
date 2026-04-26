# Song Archives

A personal music learning library. Songs live as Markdown files with structured YAML frontmatter for music theory metadata and freeform sections for personal notes.

The idea: build a library of everything you can play, discover harmonic patterns across songs, and deepen your music theory understanding over time — for any instrument.

---

## Adding a Song

### With an AI assistant (Claude Code, Cursor, Copilot, etc.)

Open this folder in your AI assistant and use the `/add-song` slash command (Claude Code) or prompt it directly:

```
/add-song Blackbird by The Beatles
/add-song Hotel California by Eagles — I play it in A minor with capo 2 on guitar
/add-song Clair de Lune by Debussy — learning on piano, intermediate level
```

The assistant searches online for music theory metadata, fills in the frontmatter, and creates the song file. You fill in the Personal Notes section yourself.

For other AI tools, paste the contents of `CLAUDE.md` as a system prompt or context, then describe the song you want to add.

### Manually

1. Copy `templates/song-template.md` to `songs/title--artist.md` (lowercase, hyphens, double-dash between title and artist — e.g. `blackbird--the-beatles.md`)
2. Fill in the YAML frontmatter fields you know
3. Write the About, Music Theory Notes, and How to Play sections
4. Leave Personal Notes for yourself — it's a blockquote intentionally

---

## Updating a Song

Tell your AI assistant directly:

```
/add-song mark Blackbird as polished
```

Or just prompt it:

> "Mark Blackbird as polished"  
> "Update the last played date for Clair de Lune to today"  
> "Add a note to Hotel California — finally nailed the intro riff"

---

## Querying Your Library

```bash
python3 scripts/query.py list                        # all songs
python3 scripts/query.py instrument piano            # by instrument
python3 scripts/query.py scale pentatonic_minor      # by scale
python3 scripts/query.py my_key "E minor"            # songs in your playing key
python3 scripts/query.py status polished             # songs you've mastered
python3 scripts/query.py roman_numerals "I V vi IV"  # by chord pattern (key-agnostic)
python3 scripts/query.py techniques fingerpicking    # by technique
python3 scripts/query.py genre blues                 # by genre
python3 scripts/query.py all                         # dump full metadata for all songs
```

---

## Song File Format

Each song is `songs/title--artist.md` with YAML frontmatter. Example: `blackbird--the-beatles.md`.

<!-- README_SYNC: Keep this table in sync with the Schema Reference table in CLAUDE.md
     and the field list in templates/song-template.md when fields are added or removed. -->

| Field | Example | Purpose |
|---|---|---|
| `instrument` | `guitar` | What you're learning this on |
| `original_key` | `F# minor` | Key as recorded |
| `my_key` | `E minor` | Key you play in — leave blank if same as original |
| `capo` | `2` | Capo position — guitar/ukulele only (0 = none) |
| `tuning` | `standard` | `standard`, `drop_d`, `open_g`, `dadgad`, etc. |
| `scale` | `pentatonic_minor` | `major`, `natural_minor`, `pentatonic_minor`, `dorian`, `mixolydian`, `blues`, etc. |
| `mode` | `aeolian` | `ionian`, `dorian`, `phrygian`, `lydian`, `mixolydian`, `aeolian`, `locrian` |
| `chord_progression` | `[Am, G, C, F]` | Actual chords in your playing key |
| `roman_numerals` | `[i, VII, IV, VI]` | Key-agnostic harmonic pattern — find songs with similar progressions regardless of key |
| `borrowed_chords` | `[A7]` | Chords outside the diatonic key (modal interchange) |
| `techniques` | `[fingerpicking, barre_chords]` | Instrument-specific techniques |
| `status` | `learning` | `learning`, `polished`, `rusty`, `shelved` |
| `feel` | `[melancholic, sparse]` | Vibe tags for mood-based browsing |
| `tags` | `[campfire, iconic-riff]` | Freeform tags |

Full field list with descriptions: [templates/song-template.md](templates/song-template.md)

### Body sections

Each song file has four sections:

- **About This Song** — ground truth: origin, cultural context, what makes it notable
- **Music Theory Notes** — why the progression creates its mood, modal color, borrowed chords, theory insights
- **How to Play** — how *you* play it: patterns, tricky parts, instrument-specific notes
- **Personal Notes** — your subjective take: why you learned it, how it makes you feel, memories

---

## Requirements

- Python 3 for `scripts/query.py` (no extra packages)
- An AI assistant for the AI-assisted workflow (optional — everything works manually too)

---

## Project Structure

```
song-archives/
├── CLAUDE.md                        # AI workflow instructions (Claude Code)
├── README.md                        # this file
├── songs/                           # one .md file per song
├── templates/
│   └── song-template.md             # copy this for new songs
├── scripts/
│   └── query.py                     # filter songs by any frontmatter field
└── .claude/
    └── skills/add-song/SKILL.md     # /add-song slash command (Claude Code)
```
