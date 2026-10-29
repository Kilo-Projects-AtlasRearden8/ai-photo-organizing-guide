#!/usr/bin/env python3
"""
Verify backup integrity by checking file counts and spot-checking hashes.
Runs locally - no data leaves your computer.
"""

import argparse
import hashlib
import os
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Verify backup integrity (local only)"
    )
    parser.add_argument(
        "--source", required=True, help="Original photo folder"
    )
    parser.add_argument(
        "--backup", required=True, help="Backup folder to verify"
    )
    parser.add_argument(
        "--sample", type=int, default=10, help="Number of files to spot-check by hash"
    )
    return parser.parse_args()


def count_files(folder):
    """Count files in a folder recursively."""
    count = 0
    for root, _, files in os.walk(folder):
        count += len(files)
    return count


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


def main():
    args = parse_args()

    if not os.path.isdir(args.source):
        print(f"Error: source '{args.source}' is not a valid directory")
        sys.exit(1)
    if not os.path.isdir(args.backup):
        print(f"Error: backup '{args.backup}' is not a valid directory")
        sys.exit(1)

    source_count = count_files(args.source)
    backup_count = count_files(args.backup)

    print(f"Source files: {source_count}")
    print(f"Backup files: {backup_count}")

    if source_count != backup_count:
        print(f"WARNING: File count mismatch! Source has {source_count}, backup has {backup_count}")
    else:
        print("File counts match.")

    # Spot-check hashes
    import random
    source_files = []
    for root, _, files in os.walk(args.source):
        for f in files:
            source_files.append(os.path.join(root, f))

    sample_size = min(args.sample, len(source_files))
    sample = random.sample(source_files, sample_size)

    mismatches = 0
    for src_path in sample:
        rel_path = os.path.relpath(src_path, args.source)
        backup_path = os.path.join(args.backup, rel_path)

        if not os.path.exists(backup_path):
            print(f"MISSING in backup: {rel_path}")
            mismatches += 1
            continue

        src_hash = hash_file(src_path)
        bak_hash = hash_file(backup_path)

        if src_hash != bak_hash:
            print(f"HASH MISMATCH: {rel_path}")
            mismatches += 1

    if mismatches == 0:
        print(f"\nSpot-check passed: {sample_size} files verified.")
    else:
        print(f"\nSpot-check found {mismatches} issues out of {sample_size} files sampled.")


if __name__ == "__main__":
    main()