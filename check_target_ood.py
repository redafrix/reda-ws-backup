import torch
from pathlib import Path

p = "intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/libero_object_object_new/v7_22d_ood.pt"
path = Path(p)
if path.exists():
    obj = torch.load(path, map_location="cpu", weights_only=False)
    eps = obj["episodes"] if isinstance(obj, dict) else obj
    suites = set(e["task_suite"] for e in eps)
    task_ids = set(e["task_id"] for e in eps)
    print(f"\nFile: {p}")
    print(f"  Count:    {len(eps)}")
    print(f"  Suites:   {sorted(list(suites))}")
    print(f"  Task IDs: {sorted(list(task_ids))}")
else:
    print(f"File {p} not found")
