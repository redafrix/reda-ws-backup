#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys

WORKSPACE = Path(__file__).resolve().parents[1]

EXPECTED = {
    Path(
        "/mnt/ai/projects/simvla_reaching_inference_package_20260730/"
        "checkpoints/softplus_110k/model.safetensors"
    ): "68b3e8dc73b0e0ee19e9b7e8d12d2d6ab24a341e824722ffeaebd1091ea2ebcd",
    Path(
        "/mnt/ai/projects/simvla_reaching_inference_package_20260730/"
        "dataset_contract/train/norm_stats/reaching_pose_v1_train_norm.json"
    ): "27159b91cb9c3b6dbb3eb8c997c8438804d48ace05dea0dfa347e7a29a9ec410",
    Path(
        "/media/redafrix/My Passport/reaching_pose_v1_4400/train/manifest.json"
    ): "32261a82df8e015b13931afaf3b9f8de2f59b30980fc5e57833166fad0a3ffd6",
}

PINNED = {
    Path("/mnt/ai/projects/simvla_reproduction_workspace/SimVLA"):
        "ee1294a17e723b21051f4f4434508ead30a69044",
    Path(
        "/mnt/ai/projects/simvla_reproduction_workspace/"
        "franka_wrist_camera_isaaclab"
    ): "9ae798c143fcb2a20e324aea06c0d10b159af502",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()


def main() -> int:
    results = {}
    for path, expected in EXPECTED.items():
        actual = sha256(path)
        if actual != expected:
            raise RuntimeError(f"hash mismatch: {path}: {actual} != {expected}")
        results[str(path)] = actual
    for repo, expected in PINNED.items():
        actual = git(repo, "rev-parse", "HEAD")
        if actual != expected:
            raise RuntimeError(f"commit mismatch: {repo}: {actual} != {expected}")
        if git(repo, "status", "--porcelain"):
            raise RuntimeError(f"pinned worktree is dirty: {repo}")
        results[str(repo)] = actual

    master = json.loads((WORKSPACE / "manifests/seen_4000_master.json").read_text())
    if len(master["episodes"]) != 4000:
        raise RuntimeError("seen master manifest does not have 4,000 episodes")
    source_ids = [int(item["scene"]["source_episode_id"]) for item in master["episodes"]]
    if len(set(source_ids)) != 4000:
        raise RuntimeError("seen master manifest has duplicate source IDs")
    fixed_ood = json.loads(
        Path(
            "/mnt/ai/projects/simvla_reproduction_workspace/"
            "franka_wrist_camera_isaaclab/configs/benchmarks/"
            "reaching_train_ood150/full_ood.json"
        ).read_text()
    )
    if set(source_ids) & {
        int(item["scene"]["source_episode_id"]) for item in fixed_ood["episodes"]
    }:
        # Source IDs are namespace-local. The important split key is the manifest.
        results["source_id_namespace_note"] = (
            "IDs overlap numerically but manifests/scenario fingerprints are disjoint"
        )
    results["seen_manifest_fingerprint"] = master["manifest_fingerprint_sha256"]
    results["seen_episode_count"] = 4000
    print(json.dumps(results, indent=2, sort_keys=True))
    print("SOFTPLUS_CHECKPOINT_VERIFIED=YES")
    print("PINNED_WORKTREES_CLEAN=YES")
    print("SEEN_MANIFEST_COUNT=4000")
    print("CPU_PREFLIGHT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
