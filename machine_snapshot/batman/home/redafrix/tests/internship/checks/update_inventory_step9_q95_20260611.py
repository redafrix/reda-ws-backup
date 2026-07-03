import json
from datetime import datetime

inventory_path = 'fiper_ws/experiment_catalog/inventory.json'

with open(inventory_path, 'r') as f:
    data = json.load(f)

# Define the new q95 entry
new_entry = {
    "name": "h10_goal_object_ood_all_tasks_100ep_threshold_q95_20260610",
    "host": "bob",
    "absolute_path": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_q95_20260610",
    "date": "2026-06-10",
    "type": "online_eval",
    "suite": "libero_goal_object_ood",
    "tasks": list(range(18)),
    "policies": ["modified_h10_risk_topk8"],
    "episode_counts": {
        "modified_h10_risk_topk8": 1800
    },
    "trust_verdict": "TRUSTWORTHY",
    "caveats": "Mechanically sound with N=100 per task. Threshold T=q95 (0.6155) gating was too conservative, yielding 10 rescues and 18 regressions (-8 net successes) with 1.81% action modification rate.",
    "source_report_paths": [
        "/home/redafrix/.gemini/antigravity-cli/brain/dbebaa92-28e0-4ba8-a2d8-8a9dcdfb5cae/LIBERO_GOAL_OBJECT_OOD_STEP9_FORENSIC_AUDIT_THRESH_q95_20260611.md"
    ]
}

# Update in-place
data["entries"] = [e for e in data["entries"] if e.get("name") != new_entry["name"]]
data["entries"].append(new_entry)

# Update generated_at timestamp
data["generated_at"] = datetime.now().isoformat()

with open(inventory_path, 'w') as f:
    json.dump(data, f, indent=2)

print("SUCCESS: Updated inventory.json with finalized 100ep OOD sweep entry (threshold q95)")
