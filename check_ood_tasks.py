import torch
from pathlib import Path

paths = [
    "intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_unseen_obj_ood.pt",
    "intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v7_22d/v7_22d_ood.pt",
    "intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/goal_object_ood/v7_22d_ood.pt",
    "intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/ood/goal_object_ood.pt"
]

for p in paths:
    path = Path(p)
    if not path.exists():
        print(f"Skipping {p} (not found)")
        continue
    obj = torch.load(path, map_location="cpu", weights_only=False)
    eps = obj["episodes"] if isinstance(obj, dict) else obj
    suites = set(e["task_suite"] for e in eps)
    task_ids = set(e["task_id"] for e in eps)
    print(f"\nFile: {p}")
    print(f"  Count:    {len(eps)}")
    print(f"  Suites:   {sorted(list(suites))}")
    print(f"  Task IDs: {sorted(list(task_ids))}")
