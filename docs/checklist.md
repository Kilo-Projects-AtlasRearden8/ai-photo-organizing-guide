# Photo Organizing Workflow Checklist

**Print this checklist** and check off each step as you complete it. Keep it next to your computer while you work.

---

## Project Info

- **Photo folder:** ____________________________________
- **Start date:** ______________________________________
- **Total photos:** ____________________________________
- **Backup location:** _________________________________

---

## Phase 1: Setup

- [ ] Install required tools (ExifTool, DigiKam, fdupes, rsync, etc.)
- [ ] Create working folder: `~/Photos/Organizing/`
- [ ] Copy all photos into working folder (do not move originals yet)
- [ ] Count total photos for progress tracking
- [ ] Make a backup of originals before starting

---

## Phase 2: Sort by Date

- [ ] Run ExifTool to organize photos by year/month/date
- [ ] Identify photos without dates
- [ ] Place undated photos in `Undated/` folder
- [ ] Manually assign dates to undated photos where known
- [ ] Verify photos are in chronological order

---

## Phase 3: Sort by Event

- [ ] Review date-sorted folders
- [ ] Identify groups of photos from the same event
- [ ] Create event folders (e.g., "Birthday Party", "Vacation")
- [ ] Move photos into appropriate event folders
- [ ] Tag each event in your photo manager

---

## Phase 4: Sort by People (Local Face Detection)

- [ ] Install DigiKam or PhotoPrism (local, no cloud upload)
- [ ] Import your organized photo folder
- [ ] Run local face detection
- [ ] Name each person detected
- [ ] Review face groupings for accuracy
- [ ] Filter by person to verify results

---

## Phase 5: Rename Files

- [ ] Choose naming pattern: `YYYY-MM-DD_Event-Description_###.jpg`
- [ ] Run ExifTool batch rename by date
- [ ] Use rename script to add event names
- [ ] Spot-check renamed files for correctness
- [ ] Verify no files were accidentally overwritten

---

## Phase 6: Remove Duplicates

- [ ] Run fdupes or rdfind to find duplicate files
- [ ] Review duplicate groups before deleting
- [ ] Delete exact duplicates, keeping one copy of each
- [ ] Verify disk space recovered
- [ ] Check that no unique photos were accidentally removed

---

## Phase 7: Create Backups

- [ ] Set up external backup drive
- [ ] Run rsync or BorgBackup to create first backup
- [ ] Verify backup completed successfully
- [ ] Confirm backup files are readable
- [ ] Schedule regular backups (weekly recommended)
- [ ] Store one backup offsite (encrypted)

---

## Privacy Confirmation

- [ ] No photos were uploaded to any cloud AI service
- [ ] All face detection ran locally on this computer
- [ ] All backups are encrypted (if stored offsite or in cloud)
- [ ] Original photos remain untouched in a safe location

---

## Completion

- [ ] All phases complete
- [ ] Photos are organized by date, event, and people
- [ ] Files have meaningful names
- [ ] Duplicates removed
- [ ] Backups verified
- [ ] Checklist signed: ________________________  Date: __________

---

**Brought to you by Asdale Dynamics, LLC** — beginner-friendly AI education and practical tools.

Visit [dylanasdale.github.io](https://dylanasdale.github.io) for more guides.