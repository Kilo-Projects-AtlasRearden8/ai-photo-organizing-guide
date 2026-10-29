# STATUS — AI Photo Organizing Guide

## What Was Built

A beginner-friendly, privacy-first manual and static HTML site for organizing digital photos with free AI tools. All tools run locally — no photos are ever uploaded to cloud AI.

### Files Created

| File | Purpose |
|------|---------|
| `docs/manual.md` | Full beginner manual covering all 7 phases |
| `docs/checklist.md` | Printable workflow checklist with checkboxes |
| `site/index.html` | Interactive static HTML version of the manual |
| `site/css/style.css` | Clean, readable styles for the HTML site |
| `site/js/script.js` | Auto-generates table of contents from headings |
| `scripts/rename_photos.py` | Python helper to batch-rename photos by date |
| `scripts/find_duplicates.py` | Python helper to find and remove duplicate files |
| `scripts/backup_check.py` | Python helper to verify backup integrity |
| `README.md` | Project overview with Asdale Dynamics, LLC credit |
| `LICENSE` | MIT License, copyright 2026 Asdale Dynamics, LLC |

### Topics Covered

1. Sorting photos by date (EXIF metadata via ExifTool)
2. Sorting photos by event (DigiKam tags, manual folders)
3. Sorting photos by people (local face detection via DigiKam / PhotoPrism)
4. Renaming files with meaningful date-based names
5. Removing duplicate files (fdupes, rdfind, Python script)
6. Creating backups (rsync, BorgBackup, 3-2-1 rule)
7. Privacy-first workflow — everything runs locally

## How to Run

### Read the Manual
Open `docs/manual.md` in any Markdown reader, or open `site/index.html` in a web browser for the interactive HTML version.

### Print the Checklist
Print `docs/checklist.md` and check off each step as you work through it.

### Use the Python Scripts

```bash
# Rename photos by date with optional event name
python3 scripts/rename_photos.py --folder ~/Photos/Organizing --event "Summer Vacation" --dry-run

# Find duplicates (dry run first, then delete)
python3 scripts/find_duplicates.py --folder ~/Photos/Organizing --dry-run
python3 scripts/find_duplicates.py --folder ~/Photos/Organizing --delete

# Verify backup integrity
python3 scripts/backup_check.py --source ~/Photos/Organizing --backup /Volumes/ExternalDrive/Photos-Backup
```

### Install Required Tools

macOS (Homebrew):
```bash
brew install exiftool fdupes rdfind rsync borg python3
```

Ubuntu/Debian:
```bash
sudo apt install exiftool fdupes rdfind rsync borgbackup python3
```

## Verification Results

All checks passed:

| Check | Result |
|-------|--------|
| `rename_photos.py --help` | Parses correctly, all arguments documented |
| `find_duplicates.py --help` | Parses correctly, all arguments documented |
| `backup_check.py --help` | Parses correctly, all arguments documented |
| `find_duplicates.py` end-to-end (dry-run) | Correctly identified 3 identical files as a duplicate group |
| `rename_photos.py` end-to-end (dry-run) | Correctly generated date-based filenames with event tag |
| `backup_check.py` end-to-end | Correctly matched 2 source files against 2 backup files via hash |
| HTML structure validation | Valid DOCTYPE, title present, Asdale Dynamics credit present |
| LICENSE copyright line | Exactly: "Copyright (c) 2026 Asdale Dynamics, LLC" |
| README credit | Asdale Dynamics, LLC credited |
| Git commit | Successful, 10 files committed, no Co-authored-by trailers |
| No .github/workflows | Confirmed absent |
| No secrets/API keys | Confirmed absent |

## Known Gaps

1. **No automated test suite** — scripts were tested manually with temporary directories. A formal test suite (e.g., pytest) could be added.
2. **No macOS/Windows installers** — installation instructions cover Homebrew and apt; Windows users need WSL or individual tool installers.
3. **HTML site is single-page** — all content is on index.html; no separate pages per section.
4. **No search** — the HTML site has a table of contents but no in-page search.
5. **EXIF date dependency** — sorting by date relies on EXIF metadata; photos without dates need manual handling (documented in the manual).
6. **Docker required for PhotoPrism** — the local face detection option via PhotoPrism requires Docker, which may be a barrier for absolute beginners.

## Credits

Created by **Asdale Dynamics, LLC** — Indiana, formed October 2026.

Beginner-friendly AI education, books, and practical tools.

Visit [dylanasdale.github.io](https://dylanasdale.github.io) for more guides like *The Massive AI Manual*.