#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


TOPK8_DIMS = [6, 21, 25, 27, 23, 2, 26, 24]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    args = parser.parse_args()
    root = Path(args.root)
    manifest = json.loads((root / "manifests/campaign_manifest.json").read_text())
    jobs = manifest["jobs"]
    ids = [job["id"] for job in jobs]
    if len(ids) != len(set(ids)):
        raise RuntimeError("duplicate job IDs")
    known = set()
    for job in jobs:
        for dep in job.get("depends_on", []):
            if dep not in known:
                raise RuntimeError(f"job {job['id']} depends on missing or later job {dep}")
        known.add(job["id"])
        if "prod100" in job["id"]:
            if not any(dep.endswith("_smoke") for dep in job.get("depends_on", [])):
                raise RuntimeError(f"production job lacks smoke dependency: {job['id']}")

    configs = []
    for path in sorted((root / "configs/generated").glob("*.json")):
        cfg = json.loads(path.read_text())
        configs.append((path, cfg))
        if cfg.get("expected_topk8_dims") != TOPK8_DIMS:
            raise RuntimeError(f"Top-8 identity missing in {path}")
        checkpoint = str(cfg["checkpoint"])
        if "topk8" in path.name and "simvla_libero_uncertainty/ckpt-60000" not in checkpoint:
            raise RuntimeError(f"Top-8 config uses non-modified checkpoint: {path}")
        if path.stem.endswith("_smoke") and int(cfg["max_steps"]) > 12:
            raise RuntimeError(f"smoke max_steps too high: {path}")
        if cfg.get("episode_manifest_csv") and int(cfg.get("exact_episodes_per_task") or 0) != 10:
            raise RuntimeError(f"exact evaluation is not balanced 10-per-task: {path}")

    paired = defaultdict(list)
    for path, cfg in configs:
        name = path.stem.replace("_smoke", "").replace("_prod100", "")
        paired[name].append((path, cfg))
    for name, rows in paired.items():
        if len(rows) != 2:
            raise RuntimeError(f"runtime config pair incomplete for {name}: {len(rows)}")
        values = {(cfg["global_action_seed"], cfg["model_load_seed"], tuple(cfg.get("reset_seeds", []))) for _, cfg in rows}
        if len(values) != 1:
            raise RuntimeError(f"smoke/production seed mismatch for {name}")

    broad_groups = defaultdict(list)
    for path, cfg in configs:
        if not path.stem.startswith("broad_") or not path.stem.endswith("_prod100"):
            continue
        key = (cfg["suite"], int(cfg["task_id"]), int(cfg["execution_horizon"]))
        broad_groups[key].append(cfg)
    for key, rows in broad_groups.items():
        seeds = {tuple(row["reset_seeds"]) for row in rows}
        if len(rows) != 3 or len(seeds) != 1 or len(next(iter(seeds))) != 100:
            raise RuntimeError(f"broad pairing invalid for {key}")

    report = {
        "pass": True,
        "job_count": len(jobs),
        "runtime_config_count": len(configs),
        "broad_task_groups": len(broad_groups),
    }
    (root / "docs/STATIC_VALIDATION.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
