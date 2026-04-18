# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Program

```bash
pipenv install       # install dependencies
pipenv run python main.py  # run the program
```

## Architecture

Two-module design:

- **`scraper.py`** — fetches a Sputnik Music URL (e.g. a user's vote page like `uservote.php?memberid=...`), parses the HTML for `profilebox` table rows, and returns a set of artist names whose album ratings are ≥ 4.0.
- **`main.py`** — `MusicManager` class that owns two flat text files (`music-to-try.txt`, `music-to-ignore.txt`). It calls `scraper.py` to populate `music-to-try.txt`, then lets the user randomly pick an artist to check; confirming moves the artist to `music-to-ignore.txt` so it never resurfaces.

## Data Files

- `music-to-try.txt` — ordered list of artists yet to be checked; duplicates are prevented at insertion time.
- `music-to-ignore.txt` — append-only log of artists already checked (also used as a dedup filter when adding new sources).

Both files are plain text, one artist per line, committed to the repo.
