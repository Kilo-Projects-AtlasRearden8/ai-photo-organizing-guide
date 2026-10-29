# Organizing Your Digital Photos with Free AI Tools

A beginner-friendly, privacy-first manual for sorting, renaming, deduplicating, and backing up your photos — without ever uploading them to the cloud.

---

## About This Guide

This guide is written for anyone who has a folder full of photos with names like `IMG_4829.jpg` and no idea where to start. You don't need coding experience. You don't need to pay for anything. And most importantly — your photos never leave your computer.

**Written by Asdale Dynamics, LLC** — beginner-friendly AI education, books, and practical tools. Visit [dylanasdale.github.io](https://dylanasdale.github.io) for more guides like *The Massive AI Manual*.

---

## Table of Contents

1. [The Privacy-First Rule](#the-privacy-first-rule)
2. [Tools You'll Need (All Free)](#tools-youll-need-all-free)
3. [Step 1: Gather Your Photos in One Place](#step-1-gather-your-photos-in-one-place)
4. [Step 2: Sort by Date](#step-2-sort-by-date)
5. [Step 3: Sort by Event](#step-3-sort-by-event)
6. [Step 4: Sort by People (Face Detection)](#step-4-sort-by-people-face-detection)
7. [Step 5: Rename Your Files](#step-5-rename-your-files)
8. [Step 6: Remove Duplicates](#step-6-remove-duplicates)
9. [Step 7: Create Backups](#step-7-create-backups)
10. [Printable Workflow Checklist](#printable-workflow-checklist)
11. [Troubleshooting & FAQ](#troubleshooting--faq)

---

## The Privacy-First Rule

> **Never upload sensitive photos to cloud AI.**

This is the golden rule of this guide. Every tool recommended here runs **locally** on your computer. Your photos never leave your hard drive, never get sent to a server, and never get used to train someone else's AI.

Why this matters: Photos contain personal data — your face, your home, your family, your location, your life. Once a photo is uploaded to a cloud AI service, you lose control over how it's used, stored, or shared.

All tools in this guide are:
- **Local**: They run on your computer, not in the cloud
- **Free**: No subscriptions, no hidden costs
- **Open source or widely trusted**: You can verify what they do

---

## Tools You'll Need (All Free)

| Tool | What It Does | Platform |
|------|-------------|----------|
| **ExifTool** | Reads and writes photo metadata (date, camera, GPS) | Windows, Mac, Linux |
| **DigiKam** | Photo management with local AI face detection | Windows, Mac, Linux |
| **PhotoPrism** | Local AI photo organization (runs via Docker) | Windows, Mac, Linux |
| **fdupes** | Finds duplicate files | Windows, Mac, Linux |
| **rdfind** | Finds duplicate files (alternative) | Windows, Mac, Linux |
| **rsync** | Copies and syncs files for backups | Mac, Linux (Windows via WSL) |
| **BorgBackup** | Encrypted, deduplicated backups | Mac, Linux (Windows via WSL) |
| **Python** | Runs helper scripts included in this guide | Windows, Mac, Linux |

### Quick Install

**macOS** (using Homebrew):
```bash
brew install exiftool fdupes rdfind rsync borg python3
```

**Ubuntu/Debian Linux**:
```bash
sudo apt update && sudo apt install exiftool fdupes rdfind rsync borgbackup python3
```

**Windows**: Download installers from each tool's website, or use [WSL](https://learn.microsoft.com/windows/wsl/) to run the Linux commands.

---

## Step 1: Gather Your Photos in One Place

Before organizing, collect all your photos into a single working folder. Photos often live in multiple places — phone backups, old cameras, SD cards, downloads folder, etc.

### Create Your Working Folder

```bash
mkdir -p ~/Photos/Organizing
```

Copy all your photos into this folder. Don't move them yet — copy them. You want your originals safe until you're confident in the process.

### Check How Many Photos You Have

```bash
find ~/Photos/Organizing -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.heic" \) | wc -l
```

This gives you a count so you can track progress.

---

## Step 2: Sort by Date

Most digital photos contain EXIF metadata with the date and time they were taken. This is the most reliable way to organize photos chronologically.

### Using ExifTool to Sort by Date

ExifTool can read the date a photo was taken and organize files into folders by year/month:

```bash
exiftool -d "%Y/%Y-%m/%Y-%m-%d" -Directory<DateTimeOriginal -r ~/Photos/Organizing
```

What this does:
- `-d "%Y/%Y-%m/%Y-%m-%d"` — creates folder structure like `2024/2024-03/2024-03-15/`
- `-Directory<DateTimeOriginal` — moves each photo into the folder based on its "DateTimeOriginal" tag
- `-r` — processes recursively (includes subfolders)

### If a Photo Has No Date

Some photos (especially older scans or screenshots) may not have EXIF date data. ExifTool will skip those. You can find them with:

```bash
exiftool -if "not $DateTimeOriginal" -filename ~/Photos/Organizing
```

For photos without dates, you can:
- Use the file's modification date as a fallback
- Place them in an `Undated` folder to review manually
- Add a date manually using your photo manager

---

## Step 3: Sort by Event

"Event" sorting groups photos by occasion — a birthday party, a vacation, a holiday. AI tools can help identify events by looking at patterns in dates, locations, and photo content.

### Using DigiKam for Event Sorting

DigiKam is a free, open-source photo manager with local AI features.

1. Install DigiKam from [digikam.org](https://www.digikam.org)
2. Open DigiKam and import your `~/Photos/Organizing` folder
3. Use **Tags** to label events (e.g., "Summer Vacation 2024", "Sarah's Birthday")
4. Use **Albums** to group photos by event

### Manual Event Sorting (Beginner-Friendly)

If you prefer not to install DigiKam yet, you can sort by event manually:

1. Look through your date-sorted folders
2. Identify groups of photos taken on the same day or consecutive days
3. Create event folders: `mkdir "Birthday Party" "Beach Trip" "Holiday Dinner"`
4. Move photos into the appropriate event folders

Event folders can live alongside or inside your date folders — whatever makes sense to you.

---

## Step 4: Sort by People (Face Detection)

Face detection identifies who appears in each photo. This runs **entirely on your computer** — no facial data is sent anywhere.

### Using DigiKam's Local Face Detection

1. Open DigiKam and import your photo folder
2. Go to **Tools → Maintain → Face Detection**
3. DigiKam will scan all photos and detect faces locally
4. It will group similar faces together and ask you to name each person
5. Once named, you can filter by person to see all photos of that individual

### Using PhotoPrism (Docker, Local Only)

PhotoPrism is a self-hosted photo app with AI face recognition. It runs entirely on your machine via Docker.

1. Install Docker from [docker.com](https://www.docker.com)
2. Run PhotoPrism locally:
```bash
docker run --name photoprism -d \
  -p 2342:2342 \
  -v ~/Photos:/photos \
  photoprism/photoprism
```
3. Open `http://localhost:2342` in your browser
4. PhotoPrism will index your photos and run face recognition locally

**Privacy note**: Because this runs via Docker on your own computer, no data leaves your machine.

---

## Step 5: Rename Your Files

Default camera names like `IMG_4829.jpg` don't tell you anything. Renaming files with meaningful names makes them easier to find later.

### Recommended Naming Pattern

```
YYYY-MM-DD_Event-Description_Sequence.jpg
```

Examples:
- `2024-03-15_Sarahs-Birthday_001.jpg`
- `2024-07-04_Beach-Trip_042.jpg`
- `2023-12-25_Holiday-Dinner_007.jpg`

### Using ExifTool to Rename by Date

```bash
exiftool '-FileName<DateTimeOriginal' -d "%Y-%m-%d_%H%M%S%%c.%%e" -r ~/Photos/Organizing
```

This renames files to `2024-03-15_143022.jpg` format based on when the photo was taken.

### Using the Included Python Rename Script

This guide includes a Python helper script (`scripts/rename_photos.py`) that lets you add event names to files:

```bash
python3 scripts/rename_photos.py --folder ~/Photos/Organizing --event "Summer Vacation"
```

The script will prompt you for each photo or batch-rename by date sequence.

---

## Step 6: Remove Duplicates

Duplicate photos waste space and make organizing harder. They often come from importing the same photos multiple times or having both edited and original versions.

### Using fdupes to Find Duplicates

```bash
fdupes -r ~/Photos/Organizing
```

This lists groups of duplicate files. To delete duplicates interactively (keeping one copy of each):

```bash
fdupes -rd ~/Photos/Organizing
```

The `-d` flag prompts you to choose which file to keep in each duplicate group.

### Using rdfind (Alternative)

rdfind ranks duplicates and can automatically keep the highest-quality copy:

```bash
rdfind -makehardlinks true -make symlinks false ~/Photos/Organizing
```

### Safety Tips for Deduplication

1. **Always work on copies, not originals** — until you're confident
2. **Review before deleting** — use `fdupes` without `-d` first to see what it found
3. **Don't deduplicate across different quality levels** — a smaller file might be a lower-quality edit you want to keep
4. **Exact duplicates only** — tools like `fdupes` find identical files. Similar but not identical photos (e.g., burst mode shots) won't be caught, which is usually what you want.

---

## Step 7: Create Backups

Organizing your photos is pointless if you lose them. Backups protect against hardware failure, accidental deletion, theft, and disasters.

### The 3-2-1 Backup Rule

- **3** copies of your data
- **2** different media types (e.g., computer + external drive)
- **1** copy offsite (e.g., a drive at a friend's house, or encrypted cloud storage)

### Local Backup with rsync

rsync copies your photos to an external drive, only copying changed files:

```bash
rsync -av --delete ~/Photos/Organizing/ /Volumes/ExternalDrive/Photos-Backup/
```

- `-a` — archive mode (preserves dates, permissions)
- `-v` — verbose (shows what's being copied)
- `--delete` — removes files from backup that no longer exist in source (use carefully)

### Encrypted Backup with BorgBackup

BorgBackup creates encrypted, deduplicated backups — ideal for sensitive photos:

```bash
# Initialize a backup repository on an external drive
borg init --encryption repokey /Volumes/ExternalDrive/Backups/photos

# Create a backup
borg create --stats /Volumes/ExternalDrive/Backups/photos::"2024-01-15" ~/Photos/Organizing
```

The `--encryption repokey` option means the backup is encrypted with a password only you know. Even if someone steals the backup drive, they can't read your photos without the password.

### Cloud Backups (Optional, Encrypted Only)

If you use cloud storage, **encrypt before uploading**. Tools like Cryptomator or BorgBackup with encryption ensure your photos stay private even in the cloud. Never upload unencrypted sensitive photos to cloud services.

---

## Printable Workflow Checklist

See [docs/checklist.md](docs/checklist.md) for a printable, checkbox-style checklist you can print and follow step by step.

---

## Troubleshooting & FAQ

### Q: My photos don't have dates. What do I do?

**A:** Use the file modification date as a fallback, or organize by event manually. In DigiKam, you can batch-edit dates for photos taken at the same event.

### Q: Can I undo a rename if I make a mistake?

**A:** ExifTool creates backup files by default (with `_original` appended). You can restore with:
```bash
exiftool -restore_original ~/Photos/Organizing
```

Or simply work from your copies and keep originals untouched.

### Q: Is face detection safe?

**A:** Yes, when it runs locally. DigiKam and PhotoPrism perform face detection on your computer. No facial data is sent to any server.

### Q: How often should I back up?

**A:** After each organizing session at minimum. Ideally, set up an automated weekly backup using rsync or BorgBackup.

### Q: What if I have thousands of photos?

**A:** Work in batches. Sort by date first (this is fast with ExifTool), then tackle events and people one folder at a time. Don't try to organize everything in one day.

---

## Scripts Included

- `scripts/rename_photos.py` — Interactive file renaming helper
- `scripts/find_duplicates.py` — Python duplicate finder
- `scripts/backup_check.py` — Verify backup integrity

---

## Credits

Created by **Asdale Dynamics, LLC** — Indiana, formed October 2026.

Beginner-friendly AI education, books, and practical tools. Visit [dylanasdale.github.io](https://dylanasdale.github.io) for more guides like *The Massive AI Manual*.

---

*This guide is for educational purposes. It does not provide medical advice.*