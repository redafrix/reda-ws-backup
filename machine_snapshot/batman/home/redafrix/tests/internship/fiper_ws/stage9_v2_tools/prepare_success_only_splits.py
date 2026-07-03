#!/usr/bin/env python3
import argparse
import json
import os
import random
import subprocess
import shutil
from pathlib import Path
from collections import Counter

def run_cmd(cmd, env=None):
    print(f"Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error executing command: {res.stderr}")
        raise RuntimeError(f"Command failed: {res.stderr}")
    return res.stdout

def main():
    parser = argparse.ArgumentParser(description="Prepare success-only splits from Libero expert datasets")
    parser.add_argument("--campaign-dir", required=True, help="Campaign root directory")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for splitting")
    args = parser.parse_args()

    campaign_dir = Path(args.campaign_dir)
    datasets_dir = campaign_dir / "datasets"
    datasets_dir.mkdir(parents=True, exist_ok=True)
    
    temp_dir = datasets_dir / "temp_suites"
    temp_dir.mkdir(parents=True, exist_ok=True)

    expert_demo_root = Path("/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/data/libero_datasets")
    
    # Define suites and parameters
    suites = {
        "libero_spatial": {"max_files": 20, "max_demos": 10},
        "libero_object": {"max_files": 20, "max_demos": 10},
        "libero_goal": {"max_files": 20, "max_demos": 10},
        "libero_10": {"max_files": 20, "max_demos": 10},
        "libero_90": {"max_files": 30, "max_demos": 10}
    }

    env = os.environ.copy()
    env["PYTHONPATH"] = f"/home/rootalkhatib/test/reda_ws/fiper_ws:/home/rootalkhatib/test/reda_ws/asynchvla_ws/src:{env.get('PYTHONPATH', '')}"

    # Step 1: Extract chunks using build_expert_low_risk_anchor_dataset
    suite_jsonls = {}
    for suite, params in suites.items():
        suite_dir = expert_demo_root / suite
        if not suite_dir.exists():
            print(f"Warning: {suite_dir} does not exist. Skipping.")
            continue
        
        out_suite_dir = temp_dir / suite
        out_suite_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"--- Extracting expert success chunks for suite: {suite} ---")
        cmd = [
            "python3", "-u", "-m", "data_collection_stage9.build_expert_low_risk_anchor_dataset",
            "--dataset-root", str(suite_dir),
            "--out-dir", str(out_suite_dir),
            "--glob", "**/*demo.hdf5",
            "--max-files", str(params["max_files"]),
            "--max-demos-per-file", str(params["max_demos"]),
            "--chunk-steps", "10",
            "--stride", "5"
        ]
        run_cmd(cmd, env=env)
        
        jsonl_file = out_suite_dir / "expert_low_risk_anchors.jsonl"
        if jsonl_file.exists():
            suite_jsonls[suite] = jsonl_file
            print(f"Extracted {sum(1 for _ in jsonl_file.open())} chunks for {suite}")
        else:
            print(f"Error: {jsonl_file} was not generated.")

    # Step 2: Load samples and partition them
    ood_suite_samples = []
    ood_task_samples = []
    id_candidate_samples = []

    # OOD task files to hold out from ID pool
    ood_task_files = {
        "KITCHEN_SCENE1_put_the_biscuit_box_to_the_left_of_the_plate_demo.hdf5",
        "STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy_demo.hdf5"
    }

    for suite, jsonl_path in suite_jsonls.items():
        with jsonl_path.open() as f:
            for line in f:
                if not line.strip():
                    continue
                sample = json.loads(line)
                
                # Add suite info for analysis
                sample["metadata"]["suite"] = suite
                
                source_file = Path(sample["metadata"]["source_hdf5"]).name
                
                if suite == "libero_spatial":
                    # OOD Suite
                    ood_suite_samples.append(sample)
                elif source_file in ood_task_files:
                    # OOD Task
                    ood_task_samples.append(sample)
                else:
                    # ID Candidate
                    id_candidate_samples.append(sample)

    print(f"\nLoaded totals:")
    print(f"  OOD Suite samples (libero_spatial): {len(ood_suite_samples)}")
    print(f"  OOD Task samples (held-out tasks): {len(ood_task_samples)}")
    print(f"  ID Candidate samples: {len(id_candidate_samples)}")

    # Step 3: Perform group-safe split on ID Candidates
    # Unique demo ID format: taskname_demoname (e.g. KITCHEN_SCENE3_turn_on_..._demo_demo_0)
    demo_to_samples = {}
    for sample in id_candidate_samples:
        task_name = Path(sample["metadata"]["source_hdf5"]).stem
        demo_name = sample["metadata"]["demo_name"]
        unique_demo_id = f"{task_name}_{demo_name}"
        
        if unique_demo_id not in demo_to_samples:
            demo_to_samples[unique_demo_id] = []
        demo_to_samples[unique_demo_id].append(sample)

    unique_demos = sorted(list(demo_to_samples.keys()))
    random.Random(args.seed).shuffle(unique_demos)

    n_demos = len(unique_demos)
    train_split_end = int(n_demos * 0.6)
    calib_split_end = int(n_demos * 0.8)

    train_demos = set(unique_demos[:train_split_end])
    calib_demos = set(unique_demos[train_split_end:calib_split_end])
    test_demos = set(unique_demos[calib_split_end:])

    train_samples = []
    calib_samples = []
    test_samples = []

    for demo_id, samples in demo_to_samples.items():
        if demo_id in train_demos:
            train_samples.extend(samples)
        elif demo_id in calib_demos:
            calib_samples.extend(samples)
        elif demo_id in test_demos:
            test_samples.extend(samples)

    # Step 4: Write splits to files
    splits = {
        "train_success_id": train_samples,
        "calib_success_id": calib_samples,
        "test_success_id": test_samples,
        "test_success_ood_task": ood_task_samples,
        "test_success_ood_suite": ood_suite_samples
    }

    print("\nWriting split files...")
    for split_name, split_data in splits.items():
        out_path = datasets_dir / f"{split_name}.jsonl"
        with out_path.open("w") as f:
            for sample in split_data:
                f.write(json.dumps(sample) + "\n")
        print(f"  Wrote {len(split_data)} samples to {out_path}")

    # Step 5: Audit & Validation checks
    print("\n=== Split Audit Report ===")
    
    # 1. Leakage check
    train_demo_set = set(train_demos)
    calib_demo_set = set(calib_demos)
    test_demo_set = set(test_demos)

    leakage_train_calib = train_demo_set.intersection(calib_demo_set)
    leakage_train_test = train_demo_set.intersection(test_demo_set)
    leakage_calib_test = calib_demo_set.intersection(test_demo_set)

    print(f"  Unique Demos count: Train={len(train_demo_set)}, Calib={len(calib_demo_set)}, Test={len(test_demo_set)}")
    print(f"  Demo Leakage: Train-Calib={len(leakage_train_calib)}, Train-Test={len(leakage_train_test)}, Calib-Test={len(leakage_calib_test)}")
    if len(leakage_train_calib) > 0 or len(leakage_train_test) > 0 or len(leakage_calib_test) > 0:
        print("  WARNING: Leakage detected between ID splits!")
    else:
        print("  SUCCESS: No demo ID leakage detected between ID splits.")

    # 2. Check task overlaps with OOD
    train_tasks = set(s["metadata"]["source_hdf5"] for s in train_samples)
    calib_tasks = set(s["metadata"]["source_hdf5"] for s in calib_samples)
    test_tasks = set(s["metadata"]["source_hdf5"] for s in test_samples)
    ood_tasks = set(s["metadata"]["source_hdf5"] for s in ood_task_samples)
    ood_suites = set(s["metadata"]["source_hdf5"] for s in ood_suite_samples)

    print(f"  OOD Tasks overlap check: {len(train_tasks.intersection(ood_tasks))} overlap with train")
    print(f"  OOD Suites overlap check: {len(train_tasks.intersection(ood_suites))} overlap with train")

    # 3. Clean up temp suite outputs
    shutil.rmtree(temp_dir)
    print("  Temporary suite directories cleaned up.")

    # 4. Save metadata audit report
    audit_summary = {
        "seed": args.seed,
        "split_counts": {k: len(v) for k, v in splits.items()},
        "unique_demos": {
            "train": len(train_demo_set),
            "calib": len(calib_demo_set),
            "test": len(test_demo_set)
        },
        "leakage": {
            "train_calib": len(leakage_train_calib),
            "train_test": len(leakage_train_test),
            "calib_test": len(leakage_calib_test)
        }
    }
    
    with (datasets_dir / "split_audit.json").open("w") as f:
        json.dump(audit_summary, f, indent=2)

if __name__ == "__main__":
    main()
