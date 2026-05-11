#!/usr/bin/env python3
from __future__ import annotations

import importlib
import json
import os
import platform
from pathlib import Path

# Use dynamic workspace root
WORKSPACE = Path(__file__).parents[2]
REPO = WORKSPACE / "simvla/code/SimVLA"
# These paths might vary depending on whether we use original SimVLA or modified
# But let's point to the most common ones in the new structure
META = REPO / "datasets" / "metas" / "libero_train.json"
NORM = REPO / "norm_stats" / "libero_norm.json"


def import_status(name: str) -> tuple[bool, str]:
    try:
        importlib.import_module(name)
        return True, "ok"
    except Exception as exc:  # pragma: no cover - diagnostic script
        return False, type(exc).__name__


def main() -> None:
    print("== SimVLA Baseline Audit ==")
    print(f"workspace: {WORKSPACE}")
    print(f"repo_exists: {REPO.exists()}")
    print(f"python: {platform.python_version()}")

    try:
        import torch

        print(f"torch: {torch.__version__}")
        print(f"torch_cuda_available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"torch_gpu_name: {torch.cuda.get_device_name(0)}")
        else:
            print("torch_gpu_name: none")
    except Exception as exc:  # pragma: no cover - diagnostic script
        print(f"torch: missing ({type(exc).__name__})")

    required = [
        "transformers",
        "fastapi",
        "uvicorn",
        "mmengine",
        "json_numpy",
        "peft",
        "mediapy",
        "num2words",
        "tensorflow",
        "websockets",
        "av",
    ]
    print("\n== Python imports ==")
    for name in required:
        ok, detail = import_status(name)
        print(f"{name}: {'ok' if ok else 'missing'} ({detail})")

    print("\n== Data ==")
    print(f"meta_exists: {META.exists()}")
    if META.exists():
        meta = json.loads(META.read_text())
        datalist = meta.get("datalist", [])
        existing = 0
        missing = 0
        for item in datalist:
            path = item["path"] if isinstance(item, dict) else item
            resolved = (REPO / path).resolve() if path.startswith("./") else Path(path)
            if resolved.exists():
                existing += 1
            else:
                missing += 1
        print(f"meta_entries: {len(datalist)}")
        print(f"meta_existing_files: {existing}")
        print(f"meta_missing_files: {missing}")
        if datalist:
            sample = datalist[0]["path"] if isinstance(datalist[0], dict) else datalist[0]
            print(f"meta_sample_path: {sample}")
    print(f"norm_exists: {NORM.exists()}")

    print("\n== Immediate blockers ==")
    blockers: list[str] = []
    ok, _ = import_status("transformers")
    if not ok:
        blockers.append("Missing runtime dependencies for model import.")
    try:
        import torch

        if not torch.cuda.is_available():
            blockers.append("Installed PyTorch is CPU-only, so unchanged training/inference will not use the GPU.")
    except Exception:
        blockers.append("PyTorch is missing.")
    if META.exists():
        meta = json.loads(META.read_text())
        if meta.get("datalist"):
            path = meta["datalist"][0]["path"] if isinstance(meta["datalist"][0], dict) else meta["datalist"][0]
            resolved = (REPO / path).resolve() if path.startswith("./") else Path(path)
            if not resolved.exists():
                blockers.append("LIBERO HDF5 data referenced by the repo metadata is not present.")
    else:
        blockers.append("Training metadata JSON is missing.")
    blockers.append("Official repo is SmolVLM-only and LIBERO-only, not the full paper release.")
    for idx, blocker in enumerate(blockers, 1):
        print(f"{idx}. {blocker}")


if __name__ == "__main__":
    main()
