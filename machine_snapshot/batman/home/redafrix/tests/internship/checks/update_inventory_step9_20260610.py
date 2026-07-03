import json
from datetime import datetime

inventory_path = 'fiper_ws/experiment_catalog/inventory.json'

with open(inventory_path, 'r') as f:
    data = json.load(f)

# Define the updated and new entries
updated_entries = [
    {
        "name": "h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609",
        "host": "bob",
        "absolute_path": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609",
        "date": "2026-06-09",
        "type": "online_eval",
        "suite": "libero_goal_object_ood",
        "tasks": list(range(18)),
        "policies": ["original_simvla", "modified_simvla", "modified_h10_risk_topk8"],
        "episode_counts": {
            "original_simvla": 1800,
            "modified_simvla": 1800,
            "modified_h10_risk_topk8": 1800
        },
        "trust_verdict": "TRUSTWORTHY",
        "caveats": "Mechanically sound with N=100 per task. Threshold T=0.3 gating was overly aggressive, yielding 24 rescues and 29 regressions (-5 net successes) with 11.40% action modification rate.",
        "source_report_paths": [
            "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/LIBERO_GOAL_OBJECT_OOD_STEP9_FORENSIC_AUDIT_20260609.md"
        ]
    },
    {
        "name": "h10_goal_object_ood_all_tasks_100ep_threshold_0.5_20260610",
        "host": "bob",
        "absolute_path": "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_0.5_20260610",
        "date": "2026-06-10",
        "type": "online_eval",
        "suite": "libero_goal_object_ood",
        "tasks": list(range(18)),
        "policies": ["modified_h10_risk_topk8"],
        "episode_counts": {
            "modified_h10_risk_topk8": 1800
        },
        "trust_verdict": "TRUSTWORTHY",
        "caveats": "Mechanically sound with N=100 per task. Threshold T=0.5 gating reduced action modifications to 4.99% (a 56.2% decrease from T=0.3) while improving net outcomes to 21 rescues and 21 regressions (0 net loss vs baseline).",
        "source_report_paths": [
            "/home/redafrix/.gemini/antigravity-cli/brain/dbebaa92-28e0-4ba8-a2d8-8a9dcdfb5cae/LIBERO_GOAL_OBJECT_OOD_STEP9_FORENSIC_AUDIT_THRESH_0.5_20260610.md"
        ]
    }
]

# Update in-place
existing_names = [e["name"] for e in updated_entries]
data["entries"] = [e for e in data["entries"] if e.get("name") not in existing_names]
data["entries"].extend(updated_entries)

# Update generated_at timestamp
data["generated_at"] = datetime.now().isoformat()

with open(inventory_path, 'w') as f:
    json.dump(data, f, indent=2)

print("SUCCESS: Updated inventory.json with finalized 100ep OOD sweep entries (threshold 0.3 and 0.5)")
