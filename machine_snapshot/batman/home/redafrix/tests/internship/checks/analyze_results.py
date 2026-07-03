import json
import os
import re
from collections import defaultdict

with open("/home/redafrix/tests/internship/audit_results.json", "r") as f:
    data = json.load(f)

print("=== CHECKING CAMPAIGNS AND RUNS ===")
for camp_name, camp_info in data.items():
    if camp_name in ["detector_audit", "processes", "checkpoint_shas"]:
        continue
    print(f"\nCampaign: {camp_name} ({camp_info['root']})")
    print(f"Exists: {camp_info['exists']}")
    runs = camp_info.get("runs", [])
    print(f"Number of runs: {len(runs)}")
    prod_runs = [r for r in runs if not r["is_smoke"]]
    smoke_runs = [r for r in runs if r["is_smoke"]]
    print(f"  Production runs: {len(prod_runs)}")
    print(f"  Smoke runs: {len(smoke_runs)}")
    
    for run in prod_runs:
        rel_dir = run["rel_dir"]
        stats = run.get("stats", {})
        if stats:
            print(f"    Prod Run: {rel_dir}")
            print(f"      Rows: {stats.get('total_rows')}, Success: {stats.get('success_count')}, Failure: {stats.get('failure_count')}, Error: {stats.get('error_count')}")
            print(f"      Mean steps: {stats.get('mean_steps_all')}, Success mean: {stats.get('mean_steps_success')}, Failure mean: {stats.get('mean_steps_failure')}")
        else:
            print(f"    Prod Run: {rel_dir} (No stats/JSONL empty or errored)")

# Let's perform more detailed audits programmatically.
# Let's inspect seed parity.
print("\n=== SEED PARITY AUDIT ===")
# Group runs by campaign and task and check reset seeds.
for camp_name, camp_info in data.items():
    if camp_name in ["detector_audit", "processes", "checkpoint_shas"]:
        continue
    runs = camp_info.get("runs", [])
    prod_runs = [r for r in runs if not r["is_smoke"]]
    if not prod_runs:
        continue
        
    # Group by task_id / task name
    task_groups = defaultdict(list)
    for r in prod_runs:
        task_id = r.get("manifest", {}).get("task_id", None)
        suite = r.get("manifest", {}).get("suite", "")
        # If task_id is None, maybe we can get it from path
        if task_id is None:
            # Check path
            match = re.search(r"task_?(\d+)", r["rel_dir"])
            if match:
                task_id = int(match.group(1))
            else:
                # OOD might have task names
                # e.g., 'runs/production_goal_swap_100ep_20260608/top_drawer_bowl/original_simvla/simvla_only'
                # Let's use the folder name as the task key
                parts = r["rel_dir"].split('/')
                if len(parts) >= 3:
                    task_id = parts[1] # e.g. top_drawer_bowl
        
        policy = r.get("manifest", {}).get("policy", "") or r.get("config", {}).get("policy", "")
        if not policy:
            # extract from rel_dir
            parts = r["rel_dir"].split('/')
            policy = parts[-2] if len(parts) >= 2 else "unknown"
            
        task_groups[task_id].append((policy, r))

    print(f"\nCampaign: {camp_name}")
    for task, group in task_groups.items():
        print(f"  Task: {task}")
        policy_seeds = {}
        for pol, run in group:
            seeds = run.get("stats", {}).get("reset_seeds", [])
            policy_seeds[pol] = seeds
            print(f"    Policy: {pol} | Shard: {run['rel_dir']} | Seed count: {len(seeds)} | Unique seeds: {len(set(seeds))}")
            dups = run.get("stats", {}).get("duplicate_seeds", [])
            if dups:
                print(f"      WARNING: Duplicated seeds found: {dups}")
            zeros = run.get("stats", {}).get("zero_step_episodes", 0)
            if zeros:
                print(f"      WARNING: {zeros} episodes with 0 steps!")
            errs = run.get("stats", {}).get("error_episodes", [])
            if errs:
                print(f"      WARNING: {len(errs)} error episodes: {errs[:3]}")

        # Check cross-policy seed parity
        pols = list(policy_seeds.keys())
        if len(pols) > 1:
            base_pol = pols[0]
            base_seeds = policy_seeds[base_pol]
            for other_pol in pols[1:]:
                other_seeds = policy_seeds[other_pol]
                # Compare sets
                if set(base_seeds) == set(other_seeds):
                    # Check order
                    if base_seeds == other_seeds:
                        print(f"    Parity between {base_pol} and {other_pol}: PASS (exact match and order)")
                    else:
                        print(f"    Parity between {base_pol} and {other_pol}: MIXED (sets match but order is different)")
                else:
                    diff1 = set(base_seeds) - set(other_seeds)
                    diff2 = set(other_seeds) - set(base_seeds)
                    print(f"    Parity between {base_pol} and {other_pol}: FAIL!")
                    if diff1:
                        print(f"      Seeds in {base_pol} not in {other_pol}: {list(diff1)[:10]}...")
                    if diff2:
                        print(f"      Seeds in {other_pol} not in {base_pol}: {list(diff2)[:10]}...")

print("\n=== DETECTOR TRAINING / DATA LEAKAGE AUDIT ===")
det = data.get("detector_audit", {})
if det:
    print(f"Buckets exist: {det.get('buckets_exist')}")
    print(f"Counts exist: {det.get('counts_exist')}")
    print(f"Flat summaries exist: {det.get('flat_summaries_exist')}")
    print(f"Total mapped episodes: {det.get('total_mapped_episodes')}")
    
    buckets = det.get("buckets", {})
    for bname, binfo in buckets.items():
        print(f"  Bucket: {bname}")
        print(f"    Total episodes: {binfo['total_episodes']}")
        print(f"    Task counts: {binfo['task_counts']}")
        print(f"    Missing mappings: {binfo['missing_mappings']}")

print("\n=== AGGRESSIVE THRESHOLD AUDIT ===")
# Let's confirm Task 3 and Task 6 success counts for Aggressive TopK8 Campaign 2 & 3
# Campaign 2: h10_goal_object_topk8_aggressive_task3_20260608
c2_runs = data.get("campaign2_aggressive_task3", {}).get("runs", [])
print("\nCampaign 2 (Aggressive TopK8 Task 3):")
for r in c2_runs:
    if not r["is_smoke"]:
        print(f"  Run: {r['rel_dir']}")
        print(f"    Stats: {r.get('stats')}")

c3_runs = data.get("campaign3_old_detector_task6", {}).get("runs", [])
print("\nCampaign 3 (Old detector Task 6):")
for r in c3_runs:
    if not r["is_smoke"]:
        print(f"  Run: {r['rel_dir']}")
        print(f"    Stats: {r.get('stats')}")
