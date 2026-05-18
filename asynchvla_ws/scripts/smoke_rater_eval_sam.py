#!/usr/bin/env python3
import torch
import sys
import os
from pathlib import Path

REDA_WS = Path("/home/rootalkhatib/test/reda_ws")
DATA_FILE = REDA_WS / "asynchvla_ws/data/processed_stage5/id_task_split/multiseed_candidate_test_id.pt"
CHECKPOINT = REDA_WS / "asynchvla_ws/outputs/checkpoints/stage6/id_task_split/context_gated_action/model.pt"

def main():
    if not DATA_FILE.exists():
        print(f"Data file missing: {DATA_FILE}")
        return
    if not CHECKPOINT.exists():
        print(f"Checkpoint missing: {CHECKPOINT}")
        return

    print(f"Loading data from {DATA_FILE}")
    try:
        data = torch.load(DATA_FILE, map_location="cpu")
        print(f"Loaded data type: {type(data)}")
        if isinstance(data, dict):
            print(f"Keys: {list(data.keys())}")
            features = data.get("features")
            if features is not None:
                print(f"Features shape: {features.shape}")
            else:
                print("No features key found")
        else:
            print("Data is not a dict")
    except Exception as e:
        print(f"Failed to load data: {e}")
        return

    print(f"Loading rater model from {CHECKPOINT}")
    try:
        rater_data = torch.load(CHECKPOINT, map_location="cpu")
        print("Rater checkpoint loaded OK")
    except Exception as e:
        print(f"Failed to load rater model: {e}")
        return

    print("Smoke test: Dataset + Rater Load OK")

if __name__ == "__main__":
    main()
