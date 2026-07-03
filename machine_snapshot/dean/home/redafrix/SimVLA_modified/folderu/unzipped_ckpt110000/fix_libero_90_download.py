#!/usr/bin/env python
"""
Download only the missing LIBERO-90 split from the official Hugging Face dataset repo.

Usage:
    python fix_libero_90_download.py
    python fix_libero_90_download.py --download-dir /home/redafrix/LIBERO/libero/datasets
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from huggingface_hub import snapshot_download


HF_REPO_ID = "yifengzhu-hf/LIBERO-datasets"


def count_hdf5_files(path: Path) -> int:
    return sum(1 for _ in path.glob("*.hdf5"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Download the missing LIBERO-90 split")
    parser.add_argument(
        "--download-dir",
        default="/home/redafrix/LIBERO/libero/datasets",
        help="Destination directory that should contain libero_90",
    )
    args = parser.parse_args()

    download_dir = Path(args.download_dir).expanduser().resolve()
    libero_90_dir = download_dir / "libero_90"

    os.makedirs(download_dir, exist_ok=True)

    if libero_90_dir.exists():
        existing = count_hdf5_files(libero_90_dir)
        if existing == 90:
            print(f"libero_90 already complete at {libero_90_dir}")
            return
        print(f"libero_90 exists but is incomplete: {existing} files")

    print(f"Downloading libero_90 into {download_dir}")
    snapshot_download(
        repo_id=HF_REPO_ID,
        repo_type="dataset",
        local_dir=str(download_dir),
        allow_patterns="libero_90/*",
        local_dir_use_symlinks=False,
        force_download=True,
    )

    final_count = count_hdf5_files(libero_90_dir)
    print(f"libero_90 file count: {final_count}")
    if final_count != 90:
        raise SystemExit(f"Expected 90 HDF5 files, found {final_count}")


if __name__ == "__main__":
    main()
