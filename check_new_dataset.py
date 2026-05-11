import json
import numpy as np
from tqdm import tqdm
from collections import Counter

path = "intern_ship_ws/ood_data/libero_object_object_new/ckpt-60000/combined_libero_object_object_all_seeds.jsonl"
print(f"Checking {path}...")

stats = Counter()
suites = Counter()
task_ids = Counter()
skipped = 0
total = 0

with open(path, "r") as f:
    for line in tqdm(f):
        total += 1
        try:
            data = json.loads(line)
            trace = data.get("uncertainty_trace", [])
            if not trace:
                stats["empty_trace"] += 1
                continue
            
            # Check fields in first step
            step = trace[0]
            required_fields = ["path_variance", "last_step_variance", "denoise_initial_mean", "denoise_delta", "denoise_final_rotation_mean"]
            missing = [f for f in required_fields if f not in step]
            if missing:
                stats["missing_fields"] += 1
                continue
            
            stats["valid"] += 1
            stats["success" if data.get("success") else "failure"] += 1
            suites[data.get("task_suite")] += 1
            task_ids[data.get("task_id")] += 1
            
        except Exception as e:
            stats["error"] += 1
            skipped += 1

print("\n--- Statistics ---")
for k, v in stats.items():
    print(f"  {k}: {v}")

print("\n--- Suites ---")
for k, v in suites.items():
    print(f"  {k}: {v}")

print("\n--- Task IDs ---")
for k, v in sorted(task_ids.items()):
    print(f"  ID {k}: {v}")

print(f"\nTotal: {total}")
