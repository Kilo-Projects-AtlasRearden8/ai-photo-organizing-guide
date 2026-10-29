#!/usr/bin/env python3
"""
Rename photos using date-based patterns.
Runs locally - no data leaves your computer.
"""

import argparse
import os
import re
import sys
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(
        description="Rename photos with date-based patterns (local only)"
    )
    parser.add_argument(
        "--folder", required=True, help="Folder containing photos to rename"
    )
    parser.add_argument(
        "--event", default=None, help="Event name to include in filenames"
    )
    parser.add_argument(
        "--pattern",
        default="%Y-%m-%d",
        help="Date pattern for filenames (strftime format)",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be renamed without doing it"
    )
    return parser.parse_args()


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".heic", ".tiff", ".bmp"}


def is_image_file(filename):
    return os.path.splitext(filename)[1].lower() in IMAGE_EXTENSIONS


def get_creation_date(filepath):
    """Get the creation/modification date of a file."""
    stat = os.stat(filepath)
    # Use modification time as a fallback; EXIF reading requires exiftool
    return datetime.fromtimestamp(stat.st_mtime)


def sanitize_event_name(event):
    """Make event name safe for filenames."""
    if not event:
        return ""
    # Replace spaces and special characters with hyphens
    sanitized = re.sub(r"[^\w\s-]", "", event.strip())
    sanitized = re.sub(r"[-\s]+", "-", sanitized)
    return sanitized.lower()


def generate_new_name(filepath, event_name, pattern, counter):
    """Generate a new filename based on date and optional event."""
    date = get_creation_date(filepath)
    ext = os.path.splitext(filepath)[1]
    date_str = date.strftime(pattern)
    event_part = f"_{event_name}" if event_name else ""
    counter_part = f"_{counter:03d}"
    return f"{date_str}{event_part}{counter_part}{ext}"


def rename_photos(folder, event_name, pattern, dry_run=False):
    """Rename all image files in the folder."""
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a valid directory")
        sys.exit(1)

    files = sorted(
        [f for f in os.listdir(folder) if is_image_file(f)]
    )

    if not files:
        print("No image files found in the specified folder.")
        return

    event_sanitized = sanitize_event_name(event_name)
    renamed = 0
    counters = {}

    for filename in files:
        filepath = os.path.join(folder, filename)
        date = get_creation_date(filepath)
        date_key = date.strftime(pattern)

        if date_key not in counters:
            counters[date_key] = 0
        counters[date_key] += 1

        new_name = generate_new_name(filepath, event_sanitized, pattern, counters[date_key])
        new_path = os.path.join(folder, new_name)

        if filepath == new_path:
            continue

        if os.path.exists(new_path):
            print(f"SKIP (already exists): {filename} -> {new_name}")
            continue

        if dry_run:
            print(f"WOULD RENAME: {filename} -> {new_name}")
        else:
            os.rename(filepath, new_path)
            print(f"RENAMED: {filename} -> {new_name}")
        renamed += 1

    if dry_run:
        print(f"\nDry run complete. {renamed} files would be renamed.")
    else:
        print(f"\nDone. {renamed} files renamed.")


def main():
    args = parse_args()
    rename_photos(args.folder, args.event, args.pattern, dry_run=args.dry_run)


if __name__ == "__main__":
    main()