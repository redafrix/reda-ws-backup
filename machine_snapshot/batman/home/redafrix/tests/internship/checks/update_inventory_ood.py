import json
from datetime import datetime

inventory_path = 'fiper_ws/experiment_catalog/inventory.json'

with open(inventory_path, 'r') as f:
    data = json.load(f)

# Define the 3 OOD sweep entries to add
new_entries = [
    {
        "name": "h10_goal_object_ood_all_tasks_10ep_20260609",
        "host": "bob",
        "absolute_path": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_20260609",
        "date": "2026-06-09",
        "type": "online_eval",
        "suite": "libero_goal_object_ood",
        "tasks": [0],
        "policies": ["original_simvla", "modified_simvla", "risk_topk8"],
        "episode_counts": {
            "original_simvla": 10,
            "modified_simvla": 10,
            "risk_topk8": 9
        },
        "trust_verdict": "DO_NOT_TRUST (diagnostic only)",
        "caveats": "Aborted due to SSH disconnect. Did not use aggressive T=0.3 controls (used q95 default fallback).",
        "source_report_paths": [
            "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/LIBERO_GOAL_OBJECT_OOD_STALL_ROOT_AUDIT_20260609.md"
        ]
    },
    {
        "name": "h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609",
        "host": "bob",
        "absolute_path": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609",
        "date": "2026-06-09",
        "type": "online_eval",
        "suite": "libero_goal_object_ood",
        "tasks": list(range(18)),
        "policies": ["original_simvla", "modified_simvla", "modified_h10_risk_topk8"],
        "episode_counts": {
            "original_simvla": 180,
            "modified_simvla": 180,
            "modified_h10_risk_topk8": 180
        },
        "trust_verdict": "TRUSTWORTHY",
        "caveats": "Mechanically sound but weak statistical signal due to N=10 per task. Aggressive threshold T=0.3 verified.",
        "source_report_paths": [
            "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/LIBERO_GOAL_OBJECT_OOD_AGGRESSIVE_FIXED_10EP_FORENSIC_AUDIT_20260609.md",
            "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/LIBERO_GOAL_OBJECT_OOD_AGGRESSIVE_FIXED_FINAL_ANALYSIS_20260609.md"
        ]
    },
    {
        "name": "h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609",
        "host": "bob",
        "absolute_path": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609",
        "date": "2026-06-09",
        "type": "online_eval",
        "suite": "libero_goal_object_ood",
        "tasks": list(range(18)),
        "policies": ["original_simvla", "modified_simvla", "risk_topk8"],
        "episode_counts": 0,
        "trust_verdict": "PENDING",
        "caveats": "Managed by CLI 1. Preparation or execution in progress.",
        "source_report_paths": []
    }
]

# Append or replace the entries by name
existing_names = [e["name"] for e in new_entries]
data["entries"] = [e for e in data["entries"] if e.get("name") not in existing_names]
data["entries"].extend(new_entries)

# Update generated_at
data["generated_at"] = datetime.now().isoformat()

with open(inventory_path, 'w') as f:
    json.dump(data, f, indent=2)

print("SUCCESS: Updated inventory.json with OOD sweep entries")
