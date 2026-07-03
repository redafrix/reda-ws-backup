#!/usr/bin/env python3
"""
enrich_expert_splits_with_obs.py — Read existing expert JSONL splits and enrich
each sample with observation features extracted from the source HDF5 files.

This produces new *_enriched.jsonl files with added fields:
  - current.proprio: [ee_pos(3), ee_ori(3), gripper_states(2)] = 8 dims
  - current.joint_states: 7 dims  
  - current.ee_states: 6 dims

Also creates the new OOD-object/task-ID test split by holding out specific
tasks within ID suites.

Usage:
    python3 enrich_expert_splits_with_obs.py
"""
from __future__ import annotations

import json
import hashlib
import time
from collections import defaultdict, Counter
from pathlib import Path

import h5py
import numpy as np

# ---- CONFIG ----
CAMPAIGN_DIR = Path("/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/success_only_fiper_20260521_102354")
DATASETS_DIR = CAMPAIGN_DIR / "datasets"

TIMESTAMP = time.strftime("%Y%m%d_%H%M%S")
OUT_DIR = CAMPAIGN_DIR / f"rnd_observation_only_fix_{TIMESTAMP}"

# Splits to enrich
SPLITS = [
    "train_success_id.jsonl",
    "calib_success_id.jsonl",
    "test_success_id.jsonl",
    "test_success_ood_task.jsonl",
    "test_success_ood_suite.jsonl",
]

# Tasks to hold out for OOD-object/task-ID test
# Hold out 2 tasks per suite from the ID suites (not libero_spatial which is already OOD-suite)
# These are object-centric tasks where different objects are manipulated
OOD_OBJECT_HOLDOUT = {
    "libero_object": [
        "pick up the cream cheese and place it in the basket",
        "pick up the salad dressing and place it in the basket",
    ],
    "libero_goal": [
        "put the bowl on the plate",
        "put the cream cheese in the bowl",
    ],
    "libero_10": [
        "put the yellow and white mug in the microwave and close it",
        "put the black bowl in the bottom drawer of the cabinet and close it",
    ],
    "libero_90": [
        "pick up the alphabet soup and place it in the basket",
        "turn on the stove",
    ],
}


def extract_obs_from_hdf5(hdf5_path: str, demo_name: str, chunk_start: int) -> dict:
    """Extract observation features from HDF5 at the chunk start timestep."""
    try:
        with h5py.File(hdf5_path, "r") as f:
            demo = f["data"][demo_name]
            obs = demo["obs"]
            
            t = min(chunk_start, obs["ee_pos"].shape[0] - 1)
            
            ee_pos = obs["ee_pos"][t].tolist()        # 3 dims
            ee_ori = obs["ee_ori"][t].tolist()        # 3 dims
            gripper = obs["gripper_states"][t].tolist() # 2 dims
            joint = obs["joint_states"][t].tolist()    # 7 dims
            ee_states = obs["ee_states"][t].tolist()   # 6 dims
            
            # Build proprio = [ee_pos, ee_ori, gripper] = 8 dims
            proprio = ee_pos + ee_ori + gripper
            
            return {
                "proprio": proprio,            # 8 dims
                "joint_states": joint,          # 7 dims
                "ee_states": ee_states,         # 6 dims
            }
    except Exception as e:
        print(f"  WARN: Failed to extract obs from {hdf5_path} {demo_name} t={chunk_start}: {e}")
        return None


def enrich_split(split_name: str, out_dir: Path) -> tuple[list[dict], int, int]:
    """Enrich a split with observation features."""
    in_path = DATASETS_DIR / split_name
    if not in_path.exists():
        print(f"  SKIP: {in_path} not found")
        return [], 0, 0
    
    with in_path.open() as f:
        samples = [json.loads(line) for line in f if line.strip()]
    
    enriched = 0
    failed = 0
    
    for s in samples:
        md = s.get("metadata", {})
        hdf5_path = md.get("source_hdf5", "")
        demo_name = md.get("demo_name", "")
        chunk_start = md.get("chunk_start", 0)
        
        obs = extract_obs_from_hdf5(hdf5_path, demo_name, chunk_start)
        if obs:
            # Enrich the current field
            cur = s.get("current", {})
            cur["proprio"] = obs["proprio"]
            cur["joint_states"] = obs["joint_states"]
            cur["ee_states"] = obs["ee_states"]
            s["current"] = cur
            enriched += 1
        else:
            # Fill with zeros so feature extraction doesn't crash
            cur = s.get("current", {})
            cur["proprio"] = [0.0] * 8
            cur["joint_states"] = [0.0] * 7
            cur["ee_states"] = [0.0] * 6
            s["current"] = cur
            failed += 1
    
    out_name = split_name.replace(".jsonl", "_enriched.jsonl")
    out_path = out_dir / out_name
    with out_path.open("w") as f:
        for s in samples:
            f.write(json.dumps(s) + "\n")
    
    print(f"  {split_name}: {len(samples)} samples, {enriched} enriched, {failed} failed -> {out_name}")
    return samples, enriched, failed


def build_ood_object_split(enriched_dir: Path) -> dict:
    """Build the OOD-object/task-ID test split from the enriched train/calib/test sets.
    
    Hold out specific tasks within each ID suite. Move their samples to a new
    test_success_ood_object_enriched.jsonl file and remove them from the other splits.
    """
    # Load all ID enriched splits
    id_splits = {}
    for name in ["train_success_id_enriched.jsonl", "calib_success_id_enriched.jsonl",
                  "test_success_id_enriched.jsonl"]:
        path = enriched_dir / name
        if not path.exists():
            continue
        with path.open() as f:
            id_splits[name] = [json.loads(line) for line in f if line.strip()]
    
    # Identify samples that match hold-out tasks
    ood_object_samples = []
    kept_splits = {}
    
    holdout_tasks_flat = set()
    for suite, tasks in OOD_OBJECT_HOLDOUT.items():
        for t in tasks:
            holdout_tasks_flat.add((suite, t))
    
    stats = Counter()
    
    for split_name, samples in id_splits.items():
        kept = []
        for s in samples:
            md = s.get("metadata", {})
            suite = md.get("suite", "")
            task_lang = md.get("task_language", "")
            
            if (suite, task_lang) in holdout_tasks_flat:
                ood_object_samples.append(s)
                stats[f"moved_from_{split_name}"] += 1
            else:
                kept.append(s)
        kept_splits[split_name] = kept
    
    # Write OOD-object split
    ood_path = enriched_dir / "test_success_ood_object_enriched.jsonl"
    with ood_path.open("w") as f:
        for s in ood_object_samples:
            f.write(json.dumps(s) + "\n")
    
    # Rewrite the ID splits without the held-out samples
    for split_name, samples in kept_splits.items():
        out_path = enriched_dir / split_name
        with out_path.open("w") as f:
            for s in samples:
                f.write(json.dumps(s) + "\n")
    
    # Demo-level leakage audit
    ood_demo_ids = set()
    for s in ood_object_samples:
        md = s.get("metadata", {})
        demo_id = f"{md.get('suite', '')}_{md.get('task_language', '')}_{md.get('demo_name', '')}"
        ood_demo_ids.add(demo_id)
    
    for split_name, samples in kept_splits.items():
        leak = 0
        for s in samples:
            md = s.get("metadata", {})
            demo_id = f"{md.get('suite', '')}_{md.get('task_language', '')}_{md.get('demo_name', '')}"
            if demo_id in ood_demo_ids:
                leak += 1
        stats[f"leakage_{split_name}"] = leak
    
    # Report
    print(f"\n=== OOD-Object Split ===")
    print(f"Total OOD-object samples: {len(ood_object_samples)}")
    print(f"Held-out task definitions:")
    for suite, tasks in sorted(OOD_OBJECT_HOLDOUT.items()):
        for t in tasks:
            matching = sum(1 for s in ood_object_samples
                          if s.get("metadata", {}).get("suite") == suite
                          and s.get("metadata", {}).get("task_language") == t)
            print(f"  {suite}: '{t}' -> {matching} samples")
    print(f"\nMovement stats: {dict(stats)}")
    print(f"Updated split sizes:")
    for name, samples in kept_splits.items():
        print(f"  {name}: {len(samples)}")
    
    return {
        "ood_object_count": len(ood_object_samples),
        "holdout_tasks": {suite: tasks for suite, tasks in OOD_OBJECT_HOLDOUT.items()},
        "movement_stats": dict(stats),
        "updated_split_sizes": {name: len(s) for name, s in kept_splits.items()},
    }


def main():
    print("=" * 70)
    print("ENRICHING EXPERT SPLITS WITH OBSERVATION FEATURES")
    print("=" * 70)
    
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUT_DIR}")
    
    # Step 1: Enrich all splits
    print("\n=== Step 1: Enriching splits with HDF5 observations ===")
    enrichment_stats = {}
    for split_name in SPLITS:
        samples, enriched, failed = enrich_split(split_name, OUT_DIR)
        enrichment_stats[split_name] = {
            "total": len(samples), "enriched": enriched, "failed": failed
        }
    
    # Step 2: Build OOD-object split
    print("\n=== Step 2: Building OOD-object/task-ID split ===")
    ood_report = build_ood_object_split(OUT_DIR)
    
    # Step 3: Save enrichment report
    report = {
        "timestamp": TIMESTAMP,
        "output_dir": str(OUT_DIR),
        "enrichment_stats": enrichment_stats,
        "ood_object_report": ood_report,
    }
    (OUT_DIR / "enrichment_report.json").write_text(json.dumps(report, indent=2) + "\n")
    
    print(f"\n=== Enrichment complete ===")
    print(f"Output: {OUT_DIR}")


if __name__ == "__main__":
    main()
