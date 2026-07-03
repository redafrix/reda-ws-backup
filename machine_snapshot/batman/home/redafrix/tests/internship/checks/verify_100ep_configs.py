import json
import os
import subprocess

NEW_ROOT = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609"

# Let's retrieve all config file contents via ssh
ssh_cmd = f"ssh pcrobot \"cat '{NEW_ROOT}/configs/'*.json\""

# Wait, it's easier to run a script on Bob that reads all configs and returns a JSON summary.
# Let's run a one-liner on Bob using python to verify and output the results.
bob_python_code = """
import json
import glob
import os

NEW_ROOT = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609"
configs_dir = os.path.join(NEW_ROOT, "configs")
config_files = glob.glob(os.path.join(configs_dir, "task*.json"))

report = []
errors = []

for cf in sorted(config_files):
    with open(cf, "r") as f:
        cfg = json.load(f)
    
    task_id = cfg.get("task_id")
    policy = cfg.get("experiment_id", "").split("_", 1)[1] if "_" in cfg.get("experiment_id", "") else ""
    # wait, policy could be original_simvla, modified_simvla, modified_h10_risk_topk8
    label = cfg.get("experiment_id", "").replace(f"task{task_id}_", "")
    
    seeds = cfg.get("reset_seeds", [])
    seed_count = len(seeds)
    suite = cfg.get("suite")
    output_dir = cfg.get("output_dir")
    checkpoint = cfg.get("checkpoint")
    
    detector = cfg.get("risk_model_unc_topk8_dir", "N/A")
    
    # Check threshold fields
    threshold_fields = {
        "selection_main_threshold": cfg.get("selection_main_threshold", "N/A"),
        "selection_streak_threshold": cfg.get("selection_streak_threshold", "N/A"),
        "selection_min_margin": cfg.get("selection_min_margin", "N/A"),
        "selection_strong_margin": cfg.get("selection_strong_margin", "N/A")
    }
    
    report.append({
        "task_id": task_id,
        "label": label,
        "seed_count": seed_count,
        "suite": suite,
        "output_dir": output_dir,
        "checkpoint": checkpoint,
        "detector": detector,
        "threshold_fields": threshold_fields,
        "seeds": seeds
    })

# Run config audits
# 1. CONFIG_COUNT_54
if len(report) != 54:
    errors.append(f"Expected 54 configs, found {len(report)}")

# 2. ALL_18_TASKS_PRESENT
tasks_found = sorted(list(set([r["task_id"] for r in report])))
if tasks_found != list(range(18)):
    errors.append(f"Expected tasks 0-17, found: {tasks_found}")

# 3. ALL_3_POLICIES_PRESENT
for t in range(18):
    labels = [r["label"] for r in report if r["task_id"] == t]
    expected_labels = ["original_simvla", "modified_simvla", "modified_h10_risk_topk8"]
    if sorted(labels) != sorted(expected_labels):
        errors.append(f"Task {t} has incorrect policies: {labels}")

# 4. each task has same 100 seeds across policies
for t in range(18):
    task_configs = [r for r in report if r["task_id"] == t]
    s0, s1, s2 = task_configs[0]["seeds"], task_configs[1]["seeds"], task_configs[2]["seeds"]
    if s0 != s1 or s1 != s2:
        errors.append(f"Task {t} seed mismatch across policies")
    if len(s0) != 100:
        errors.append(f"Task {t} has {len(s0)} seeds instead of 100")
    if len(set(s0)) != 100:
        errors.append(f"Task {t} has duplicate seeds: {s0}")
    # 5. old 10 seeds (0-9) are not the whole seed list
    if set(s0).issubset(set(range(10))):
        errors.append(f"Task {t} is using old smoke/10ep seeds: {s0}")

# 6. suite is libero_goal_object_ood everywhere
for r in report:
    if r["suite"] != "libero_goal_object_ood":
        errors.append(f"Config for {r['task_id']} {r['label']} has incorrect suite: {r['suite']}")

# 7. risk configs contain aggressive values (no q95 fallback)
for r in report:
    if r["label"] == "modified_h10_risk_topk8":
        tf = r["threshold_fields"]
        if tf["selection_main_threshold"] != 0.3 or tf["selection_streak_threshold"] != 0.3:
            errors.append(f"Config for task {r['task_id']} risk policy has incorrect thresholds: {tf}")
        if tf["selection_min_margin"] != 0.02 or tf["selection_strong_margin"] != 0.05:
            errors.append(f"Config for task {r['task_id']} risk policy has incorrect margins: {tf}")

# 8. no broken zip reference
for r in report:
    if "zip" in r["checkpoint"] or "zip" in r["detector"]:
        errors.append(f"Config for {r['task_id']} {r['label']} references zip: {r}")

# 9. no deprecated tmp checkpoint reference
for r in report:
    if "ckpt-60000-tmp" in r["checkpoint"]:
        errors.append(f"Config for {r['task_id']} {r['label']} references deprecated tmp ckpt: {r}")

# 10. output dirs point only to the new 100ep root
for r in report:
    if NEW_ROOT not in r["output_dir"]:
        errors.append(f"Config for {r['task_id']} {r['label']} has output outside NEW_ROOT: {r['output_dir']}")

print(json.dumps({
    "errors": errors,
    "report": report
}))
"""

# Let's execute this python code on Bob
p = subprocess.run(["ssh", "pcrobot", "python3 -"], input=bob_python_code, text=True, capture_output=True)
if p.returncode != 0:
    print(f"SSH execution failed: {p.stderr}")
else:
    res = json.loads(p.stdout)
    errors = res["errors"]
    print(f"Config audit errors found: {len(errors)}")
    for err in errors:
        print(f"ERROR: {err}")
    
    # Save the parsed config report locally as json for reporting
    with open("checks/libero_goal_object_ood_100ep_configs_audit.json", "w") as f:
        json.dump(res, f, indent=2)
    print("Saved configs audit details to checks/libero_goal_object_ood_100ep_configs_audit.json")
