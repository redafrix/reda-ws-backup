import json
from datetime import datetime

inventory_path = 'fiper_ws/experiment_catalog/inventory.json'

with open(inventory_path, 'r') as f:
    data = json.load(f)

for e in data["entries"]:
    if e.get("name") == "h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609":
        e["caveats"] = "Launched in detached tmux session ood_production_aggressive_fixed_100ep_20260609, managed by cli__2."
        print(f"Updated inventory.json status for {e['name']}")

data["generated_at"] = datetime.now().isoformat()

with open(inventory_path, 'w') as f:
    json.dump(data, f, indent=2)

print("SUCCESS: Updated inventory.json with running status")
