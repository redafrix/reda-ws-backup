#!/usr/bin/env bash
set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${1:-$WS_ROOT/assets/data/libero_datasets}"

mkdir -p "$OUT_DIR"

source "$WS_ROOT/activate_simvla.sh"

python - <<'PY' "$OUT_DIR"
import os
import sys

from huggingface_hub import snapshot_download
from libero.libero.utils.download_utils import check_libero_dataset

download_dir = os.path.abspath(sys.argv[1])

expected_counts = {
    "libero_object": 10,
    "libero_goal": 10,
    "libero_spatial": 10,
    "libero_10": 10,
    "libero_90": 90,
}

def local_count(name: str) -> int:
    path = os.path.join(download_dir, name)
    if not os.path.isdir(path):
        return 0
    return sum(1 for f in os.listdir(path) if f.endswith(".hdf5"))

for dataset_name in ("libero_object", "libero_goal", "libero_spatial", "libero_10", "libero_90"):
    count = local_count(dataset_name)
    if count >= expected_counts[dataset_name]:
        print(f"==> Skipping {dataset_name}: already complete ({count} files)")
        continue
    print(
        f"==> Resuming {dataset_name} from Hugging Face "
        f"({count}/{expected_counts[dataset_name]} files present)"
    )
    snapshot_download(
        repo_id="yifengzhu-hf/LIBERO-datasets",
        repo_type="dataset",
        local_dir=download_dir,
        allow_patterns=f"{dataset_name}/*",
        local_dir_use_symlinks=False,
    )

print()
print(f"Downloaded LIBERO datasets into: {download_dir}")
check_libero_dataset(download_dir=download_dir)
PY
