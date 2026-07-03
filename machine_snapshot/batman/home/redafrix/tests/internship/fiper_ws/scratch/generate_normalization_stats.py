#!/usr/bin/env python3
import os
import sys
import json
import numpy as np
from pathlib import Path

# Setup path to import run_clean_temporal_nextgen_campaign_v2
sys.path.append(str(Path(__file__).parent.parent / "scripts"))

# Import functions from run_clean_temporal_nextgen_campaign_v2
import run_clean_temporal_nextgen_campaign_v2 as runner

def main():
    fiper_ws = Path(__file__).parent.parent.resolve()
    
    # Target Job directory
    job_dir = fiper_ws / "experiments/current_baseline_v2_018_20260528/00_global_main/jobs/v2_018_transformer_k16"
    if not job_dir.exists():
        print(f"Error: job dir {job_dir} does not exist.")
        sys.exit(1)
        
    cfg = json.loads((job_dir / "config.json").read_text())
    print("Loaded job config:", cfg)
    
    refs_dir = fiper_ws / "experiments/prepared_20260527/00_global_main/datasets/refs"
    base_dir = fiper_ws
    
    # Only load success_train_seen and failure_train_seen to speed up
    runner.SPLITS_TO_LOAD = ["success_train_seen", "failure_train_seen"]
    
    print("Loading training rows...")
    max_rows_by_split = {"success_train_seen": None, "failure_train_seen": None}
    history_steps_needed = [16]
    
    rows_by_split = runner.load_rows_from_refs(refs_dir, base_dir, max_rows_by_split, history_steps_needed)
    
    train_rows = rows_by_split["success_train_seen"] + rows_by_split["failure_train_seen"]
    print(f"Total training rows loaded: {len(train_rows)}")
    
    print("Computing sequence features...")
    h_train_raw, a_train_raw, st_train_raw = runner.sequence_features(train_rows, cfg)
    
    print("Fitting standardizers...")
    h_stats = runner.fit_seq_standardizer(h_train_raw)
    a_stats = runner.fit_seq_standardizer(a_train_raw)
    st_stats = runner.fit_standardizer(st_train_raw)
    
    # Save standardizers
    stats_dict = {
        "history": {
            "mean": h_stats["mean"].tolist(),
            "std": h_stats["std"].tolist()
        },
        "action": {
            "mean": a_stats["mean"].tolist(),
            "std": a_stats["std"].tolist()
        },
        "static": {
            "mean": st_stats["mean"].tolist(),
            "std": st_stats["std"].tolist()
        }
    }
    
    out_path = job_dir / "normalization.json"
    out_path.write_text(json.dumps(stats_dict, indent=2) + "\n")
    print(f"Successfully computed and wrote standardizers to {out_path}")
    
    # Also save to fallback job dir just in case
    fallback_job_dir = fiper_ws / "experiments/current_baseline_v2_018_20260528/01_ood_task_8_9/jobs/v2_018_transformer_k16"
    if fallback_job_dir.exists():
        fb_out_path = fallback_job_dir / "normalization.json"
        fb_out_path.write_text(json.dumps(stats_dict, indent=2) + "\n")
        print(f"Successfully wrote standardizers to fallback: {fb_out_path}")

if __name__ == "__main__":
    main()
