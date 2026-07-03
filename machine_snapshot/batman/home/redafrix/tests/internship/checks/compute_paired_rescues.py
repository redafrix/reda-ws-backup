import json

with open("/home/redafrix/tests/internship/audit_results.json", "r") as f:
    data = json.load(f)

c1 = data["campaign1_risk_proof"]["runs"]
c2 = data["campaign2_aggressive_task3"]["runs"]
c3 = data["campaign3_old_detector_task6"]["runs"]

# Helper to load seeds outcomes
def load_outcomes(runs, task_id, policy_pattern):
    outcomes = {}
    for r in runs:
        if r["is_smoke"]:
            continue
        rel = r["rel_dir"]
        config = r.get("config", {})
        manifest = r.get("manifest", {})
        t = config.get("task_id", manifest.get("task_id", None))
        if str(t) != str(task_id):
            continue
        if policy_pattern not in rel:
            continue
        
        # Read the raw JSONL rows
        # Wait, the remote audit script already parsed stats, let's load stats reset_seeds and success
        # Wait, we need the mapping of seed -> success for each episode.
        # But stats only gives lists. Let's write a python snippet that directly reads the JSONL files from pcrobot or we can do it locally since we have ssh.
        # Wait! Is it possible to get the seed-to-success mapping?
        # Yes! Let's write a python snippet to read the jsonl files via ssh or run it on pcrobot.
        # Running it on pcrobot is much easier because we have the remote python script execution capability.
    return outcomes

# Let's run a remote python script to compute paired rescues/regressions.
