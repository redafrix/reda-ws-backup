import json

with open("/home/redafrix/tests/internship/audit_results.json", "r") as f:
    data = json.load(f)

c1 = data["campaign1_risk_proof"]["runs"]
c2 = data["campaign2_aggressive_task3"]["runs"]
c3 = data["campaign3_old_detector_task6"]["runs"]

def find_run(runs, task_id, policy, shard_str):
    for r in runs:
        if r["is_smoke"]:
            continue
        rel = r["rel_dir"]
        config = r.get("config", {})
        manifest = r.get("manifest", {})
        t = config.get("task_id", manifest.get("task_id", None))
        p = manifest.get("policy", config.get("policy", ""))
        # Check task
        if str(t) != str(task_id):
            continue
        # Check shard
        if shard_str not in rel:
            continue
        # Check policy
        if policy == "simvla_only" and "simvla_only" in rel:
            return r
        if policy == "risk_topk8" and "risk_topk8" in rel:
            return r
    return None

tasks = [3, 6]
shards = ["shard_0", "shard_1"]

print("=== CHECKING SEED PARITY BETWEEN CAMPAIGN 1 AND CAMPAIGN 2 ===")
for t in tasks:
    for sh in shards:
        r1_sim = find_run(c1, t, "simvla_only", sh) # modified_simvla
        # Wait, c1 has original_simvla and modified_simvla. Let's make sure we get modified_simvla.
        # Let's write a custom finder
        r1_mod_sim = None
        for r in c1:
            if not r["is_smoke"] and f"task{t}" in r["rel_dir"] and "modified_simvla" in r["rel_dir"] and sh in r["rel_dir"]:
                r1_mod_sim = r
                break
                
        r2_risk = None
        for r in c2:
            if not r["is_smoke"] and f"task{t}" in r["rel_dir"] and "modified_h10_risk_topk8" in r["rel_dir"] and sh in r["rel_dir"]:
                r2_risk = r
                break
                
        if r1_mod_sim and r2_risk:
            s1 = r1_mod_sim.get("stats", {}).get("reset_seeds", [])
            s2 = r2_risk.get("stats", {}).get("reset_seeds", [])
            same_set = set(s1) == set(s2)
            same_ord = s1 == s2
            print(f"Task {t} {sh}: C1 modified_simvla vs C2 modified_risk_topk8 | Seeds count: C1={len(s1)}, C2={len(s2)} | Same Set: {same_set} | Same Order: {same_ord}")
        else:
            print(f"Task {t} {sh}: Could not find C1 modified_simvla ({r1_mod_sim is not None}) or C2 risk_topk8 ({r2_risk is not None})")

print("\n=== CHECKING SEED PARITY BETWEEN CAMPAIGN 1 AND CAMPAIGN 3 ===")
for sh in shards:
    r1_mod_sim = None
    for r in c1:
        if not r["is_smoke"] and "task6" in r["rel_dir"] and "modified_simvla" in r["rel_dir"] and sh in r["rel_dir"]:
            r1_mod_sim = r
            break
            
    r3_risk = None
    for r in c3:
        if not r["is_smoke"] and "task6" in r["rel_dir"] and "modified_h10_risk_topk8" in r["rel_dir"] and sh in r["rel_dir"]:
            r3_risk = r
            break
            
    if r1_mod_sim and r3_risk:
        s1 = r1_mod_sim.get("stats", {}).get("reset_seeds", [])
        s3 = r3_risk.get("stats", {}).get("reset_seeds", [])
        same_set = set(s1) == set(s3)
        same_ord = s1 == s3
        print(f"Task 6 {sh}: C1 modified_simvla vs C3 modified_risk_topk8 | Seeds count: C1={len(s1)}, C3={len(s3)} | Same Set: {same_set} | Same Order: {same_ord}")
    else:
        print(f"Task 6 {sh}: Could not find C1 modified_simvla ({r1_mod_sim is not None}) or C3 risk_topk8 ({r3_risk is not None})")
