#!/usr/bin/env python3
"""
Find duplicate files in a folder using content hashing.
Runs locally - no data leaves your computer.
"""

import argparse
import hashlib
import os
import sys
from collections import defaultdict


def parse_args():
    parser = argparse.ArgumentParser(
        description="Find duplicate files locally (no cloud upload)"
    )
    parser.add_argument(
        "--folder", required=True, help="Folder to scan for duplicates"
    )
    parser.add_argument(
        "--delete", action="store_true", help="Delete duplicates (keeps first copy)"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Show duplicates without deleting"
    )
    return parser.parse_args()


def hash_file(filepath, chunk_size=8192):
    """Return SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (OSError, IOError):
        return None


def find_duplicates(folder):
    """Find duplicate files by size then by hash."""
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a valid directory")
        sys.exit(1)

    # Group by size first (quick filter)
    size_groups = defaultdict(list)
    for root, _, files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                size = os.path.getsize(filepath)
                size_groups[size].append(filepath)
            except OSError:
                continue

    # Only check files with the same size
    hash_groups = defaultdict(list)
    for size, paths in size_groups.items():
        if len(paths) < 2:
            continue
        for filepath in paths:
            file_hash = hash_file(filepath)
            if file_hash:
                hash_groups[file_hash].append(filepath)

    # Return groups with more than one file (actual duplicates)
    duplicates = [paths for paths in hash_groups.values() if len(paths) > 1]
    return duplicates


def main():
    args = parse_args()
    duplicates = find_duplicates(args.folder)

    if not duplicates:
        print("No duplicates found.")
        return

    total_wasted = 0
    total_duplicates = 0

    for i, group in enumerate(duplicates, 1):
        print(f"\nDuplicate group {i} ({len(group)} copies):")
        for j, path in enumerate(group):
            size = os.path.getsize(path)
            marker = "KEEP" if j == 0 else "DUPLICATE"
            print(f"  [{marker}] {path} ({size} bytes)")
            if j > 0:
                total_wasted += size
                total_duplicates += 1

    print(f"\n--- Summary ---")
    print(f"Duplicate groups: {len(duplicates)}")
    print(f"Extra copies: {total_duplicates}")
    print(f"Space wasted: {total_wasted} bytes ({total_wasted / 1024 / 1024:.2f} MB)")

    if args.delete or args.dry_run:
        action = "WOULD DELETE" if args.dry_run else "DELETING"
        print(f"\n{action} duplicates...")
        for group in duplicates:
            for path in group[1:]:  # Skip first (keep original)
                if args.dry_run:
                    print(f"  WOULD DELETE: {path}")
                else:
                    os.remove(path)
                    print(f"  DELETED: {path}")
        if not args.dry_run:
            print(f"\nDone. {total_duplicates} files deleted.")


if __name__ == "__main__":
    main()