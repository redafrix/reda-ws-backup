import torch
from pathlib import Path
from collections import defaultdict

path = Path("intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt")
obj = torch.load(path, map_location="cpu", weights_only=False)
eps = obj["episodes"] if isinstance(obj, dict) else obj

suite_tasks = defaultdict(set)
for e in eps:
    suite_tasks[e["task_suite"]].add(e["task_id"])

print("\n=== Tasks in TRAINING set ===")
for suite, tasks in sorted(suite_tasks.items()):
    print(f"  {suite}: {sorted(list(tasks))}")
