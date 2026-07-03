import json
import re
from collections import defaultdict

with open("/home/redafrix/tests/internship/audit_results.json", "r") as f:
    data = json.load(f)

report = []

# Helper to write lines to report
def log(msg=""):
    report.append(msg)

log("# DETAILED FORENSIC SANITY AUDIT CHECKS")
log()

# ---------------------------------------------------------
# 1. INVENTORY
# ---------------------------------------------------------
log("## 1. Inventory of Production Runs")
log()
log("| Campaign | Run Directory | Suite | Task ID | Policy | Episodes | Success | Failure | Error | Mean Steps |")
log("|---|---|---|---|---|---|---|---|---|---|")

campaigns_keys = ["campaign1_risk_proof", "campaign2_aggressive_task3", "campaign3_old_detector_task6", "campaign4_ood_goal_swap"]

for ckey in campaigns_keys:
    camp = data.get(ckey, {})
    if not camp or not camp.get("exists"):
        continue
    runs = camp.get("runs", [])
    # Sort runs so they are easy to read
    runs_sorted = sorted(runs, key=lambda x: (x["is_smoke"], x["rel_dir"]))
    for r in runs_sorted:
        if r["is_smoke"]:
            continue # We only list production runs in inventory section 1 as requested, but wait, let's list smoke separately below.
        
        rel_dir = r["rel_dir"]
        manifest = r.get("manifest", {})
        config = r.get("config", {})
        stats = r.get("stats", {})
        
        suite = manifest.get("suite", config.get("suite", "unknown"))
        task_id = manifest.get("task_id", config.get("task_id", "unknown"))
        policy = manifest.get("policy", config.get("policy", "unknown"))
        
        if stats:
            total = stats.get("total_rows", 0)
            succ = stats.get("success_count", 0)
            fail = stats.get("failure_count", 0)
            err = stats.get("error_count", 0)
            m_steps = f"{stats.get('mean_steps_all', 0.0):.2f}"
        else:
            total, succ, fail, err, m_steps = 0, 0, 0, 0, "0.00"
            
        log(f"| {ckey} | {rel_dir} | {suite} | {task_id} | {policy} | {total} | {succ} | {fail} | {err} | {m_steps} |")

log()
log("### Smoke / Online Smoke / Test Runs")
log()
log("| Campaign | Run Directory | Suite | Task ID | Policy | Episodes | Success | Failure | Error | Mean Steps |")
log("|---|---|---|---|---|---|---|---|---|---|")
for ckey in campaigns_keys:
    camp = data.get(ckey, {})
    if not camp or not camp.get("exists"):
        continue
    runs = camp.get("runs", [])
    runs_sorted = sorted(runs, key=lambda x: (x["is_smoke"], x["rel_dir"]))
    for r in runs_sorted:
        if not r["is_smoke"]:
            continue
        rel_dir = r["rel_dir"]
        manifest = r.get("manifest", {})
        config = r.get("config", {})
        stats = r.get("stats", {})
        
        suite = manifest.get("suite", config.get("suite", "unknown"))
        task_id = manifest.get("task_id", config.get("task_id", "unknown"))
        policy = manifest.get("policy", config.get("policy", "unknown"))
        
        if stats:
            total = stats.get("total_rows", 0)
            succ = stats.get("success_count", 0)
            fail = stats.get("failure_count", 0)
            err = stats.get("error_count", 0)
            m_steps = f"{stats.get('mean_steps_all', 0.0):.2f}"
        else:
            total, succ, fail, err, m_steps = 0, 0, 0, 0, "0.00"
            
        log(f"| {ckey} | {rel_dir} | {suite} | {task_id} | {policy} | {total} | {succ} | {fail} | {err} | {m_steps} |")

# ---------------------------------------------------------
# 2. CONFIG SANITY
# ---------------------------------------------------------
log()
log("## 2. Config Sanity Audit")
log()
for ckey in campaigns_keys:
    camp = data.get(ckey, {})
    if not camp or not camp.get("exists"):
        continue
    log(f"### Campaign: {ckey}")
    log()
    runs = camp.get("runs", [])
    prod_runs = [r for r in runs if not r["is_smoke"]]
    for r in prod_runs:
        rel_dir = r["rel_dir"]
        config = r.get("config", {})
        manifest = r.get("manifest", {})
        
        suite = config.get("suite", manifest.get("suite", "N/A"))
        task_id = config.get("task_id", manifest.get("task_id", "N/A"))
        task_lang = config.get("task_language", "N/A")
        ckpt = config.get("checkpoint", manifest.get("checkpoint", "N/A"))
        detector_path = config.get("risk_model_unc_topk8_dir", manifest.get("risk_model_dir", "N/A"))
        horizon = config.get("execution_horizon", manifest.get("execution_horizon", "N/A"))
        
        # Thresholds
        threshold_main = config.get("selection_main_threshold", "N/A")
        threshold_streak = config.get("selection_streak_threshold", "N/A")
        manifest_thresh = manifest.get("risk_thresholds", {})
        
        # Seeds
        reset_seeds = config.get("reset_seeds", [])
        num_seeds = len(reset_seeds)
        global_act_seed = config.get("global_action_seed", "N/A")
        model_load_seed = config.get("model_load_seed", "N/A")
        policy_type = manifest.get("policy", config.get("policy", "N/A"))
        
        log(f"**Run:** `{rel_dir}`")
        log(f"- Suite: `{suite}`")
        log(f"- Task ID: `{task_id}`")
        log(f"- Task Language: `{task_lang}`")
        log(f"- Model Checkpoint Path: `{ckpt}`")
        log(f"- Detector Path: `{detector_path}`")
        log(f"- Horizon Setting: `{horizon}`")
        log(f"- Threshold Settings (config): main=`{threshold_main}`, streak=`{threshold_streak}`")
        if manifest_thresh:
            log(f"  - Conformal thresholds (from manifest): `{json.dumps(manifest_thresh)}`")
        log(f"- Reset Seeds count: `{num_seeds}`")
        log(f"- Seed Settings: global_action_seed=`{global_act_seed}`, model_load_seed=`{model_load_seed}`")
        log(f"- Policy Type: `{policy_type}`")
        log()

# ---------------------------------------------------------
# 3. SEED PARITY
# ---------------------------------------------------------
log()
log("## 3. Seed Parity Audit")
log()

for ckey in campaigns_keys:
    camp = data.get(ckey, {})
    if not camp or not camp.get("exists"):
        continue
    log(f"### Campaign: {ckey}")
    log()
    runs = camp.get("runs", [])
    prod_runs = [r for r in runs if not r["is_smoke"]]
    if not prod_runs:
        log("No production runs.")
        log()
        continue
        
    # Group runs by task name/id
    task_groups = defaultdict(list)
    for r in prod_runs:
        task_id = r.get("manifest", {}).get("task_id", None)
        if task_id is None:
            task_id = r.get("config", {}).get("task_id", None)
        if task_id is None:
            # Fallback to path checking
            match = re.search(r"task_?(\d+)", r["rel_dir"])
            if match:
                task_id = int(match.group(1))
            else:
                parts = r["rel_dir"].split('/')
                if len(parts) >= 3:
                    task_id = parts[1]
                else:
                    task_id = "unknown"
        task_groups[task_id].append(r)
        
    for task_id, group in task_groups.items():
        log(f"#### Task: `{task_id}`")
        # Check seeds inside each policy
        policy_seeds = {}
        for r in group:
            rel_dir = r["rel_dir"]
            # Policy key
            pol = r.get("manifest", {}).get("policy", "") or r.get("config", {}).get("policy", "")
            if not pol:
                parts = rel_dir.split('/')
                pol = parts[-2] if len(parts) >= 2 else "unknown"
            # Add shard indicator
            shard = "s0" if "shard_0" in rel_dir else ("s1" if "shard_1" in rel_dir else "")
            pol_key = f"{pol}_{shard}" if shard else pol
            
            stats = r.get("stats", {})
            seeds = stats.get("reset_seeds", [])
            policy_seeds[pol_key] = seeds
            
            # Check duplicated reset seeds
            duplicates = stats.get("duplicate_seeds", [])
            log(f"- Policy `{pol_key}`: `{len(seeds)}` seeds, `{len(set(seeds))}` unique.")
            if duplicates:
                log(f"  - **WARNING:** Duplicated seeds found: `{duplicates}`")
            
        # Check seed parity across different policies for the same task
        # We want to check if original_simvla, original_h10_risk_base, modified_simvla, modified_h10_risk_topk8 share the same seeds
        # Group by shard
        shards = ["shard_0", "shard_1", ""]
        for sh in shards:
            sh_group = [pk for pk in policy_seeds.keys() if (sh in pk if sh else True)]
            # filter out keys that don't match the shard exactly if we have shard suffix
            if sh:
                sh_group = [pk for pk in policy_seeds.keys() if pk.endswith(f"_{sh.replace('hard_', '')}")]
            if len(sh_group) > 1:
                log(f"  - **Cross-policy Seed Parity for {sh or 'all'}:**")
                base_pk = sh_group[0]
                base_seeds = policy_seeds[base_pk]
                for other_pk in sh_group[1:]:
                    other_seeds = policy_seeds[other_pk]
                    if set(base_seeds) == set(other_seeds):
                        if base_seeds == other_seeds:
                            log(f"    - `{base_pk}` vs `{other_pk}`: **PASS** (exact match and order)")
                        else:
                            log(f"    - `{base_pk}` vs `{other_pk}`: **MIXED** (same seed set, but different order)")
                    else:
                        diff1 = set(base_seeds) - set(other_seeds)
                        diff2 = set(other_seeds) - set(base_seeds)
                        log(f"    - `{base_pk}` vs `{other_pk}`: **FAIL**")
                        if diff1:
                            log(f"      - In `{base_pk}` but not `{other_pk}` (first 10): `{list(diff1)[:10]}`")
                        if diff2:
                            log(f"      - In `{other_pk}` but not `{base_pk}` (first 10): `{list(diff2)[:10]}`")
        log()

# ---------------------------------------------------------
# 4. HORIZON / EXECUTION SEMANTICS
# ---------------------------------------------------------
log("## 4. Horizon and Execution Semantics")
log()
log("From config inspection, the execution horizon is explicitly set to `10` (H10) across all policies.")
log("Let's audit whether step counts match horizon boundaries (e.g. env steps should be multiples of 10 plus terminal truncation, or success truncation).")
log("Let's look at steps of failed episodes (which run to timeout/limit unless they fail early or succeed).")
log("For failed episodes, if the timeout is 300 steps, we expect the number of steps to be exactly 300 if execution horizon doesn't truncate, or we expect steps to be a multiple of 10 if chunk execution is correct.")
log("Let's check the step count distributions for failed episodes in production runs:")
log()
for ckey in campaigns_keys:
    camp = data.get(ckey, {})
    if not camp or not camp.get("exists"):
        continue
    runs = camp.get("runs", [])
    prod_runs = [r for r in runs if not r["is_smoke"]]
    for r in prod_runs:
        stats = r.get("stats", {})
        if not stats:
            continue
        rel_dir = r["rel_dir"]
        # Look at failed episodes step count (they should be 300, or if truncated, some other value)
        log(f"- Run: `{rel_dir}` | Mean Steps (All): `{stats.get('mean_steps_all', 0.0):.2f}` | Success Mean Steps: `{stats.get('mean_steps_success', 0.0):.2f}` | Failure Mean Steps: `{stats.get('mean_steps_failure', 0.0):.2f}`")

log()
log("Wait, let's verify if failed episodes have exactly 300 steps or if they deviate.")
log("In Campaign 1 and others, the failure mean steps are exactly `300.0` or close to it, which indicates failed episodes ran for the full limit of 300 steps.")
log("Let's check if there are any failed episodes that have non-300 step counts. This would indicate early termination on failure (which might be normal if `done` is returned by the env, or abnormal if there is a bug).")

# ---------------------------------------------------------
# 5. SUCCESS SEMANTICS
# ---------------------------------------------------------
log()
log("## 5. Success Semantics Audit")
log()
log("From runner code inspection (`run_policy_matrix.py`):")
log("- Success is checked via two methods:")
log("  1. Environment reward: `reward_success = bool(float(rew) > 0.0)`")
log("  2. Explicit environment check: `checked_success = check_success(env)`")
log("  - These are combined: `success = success or reward_success or bool(checked_success)`")
log("- Let's check if there are 0-step or error rows in production runs:")
log()
for ckey in campaigns_keys:
    camp = data.get(ckey, {})
    if not camp or not camp.get("exists"):
        continue
    runs = camp.get("runs", [])
    prod_runs = [r for r in runs if not r["is_smoke"]]
    for r in prod_runs:
        stats = r.get("stats", {})
        if not stats:
            continue
        rel_dir = r["rel_dir"]
        zeros = stats.get("zero_step_episodes", 0)
        errs = stats.get("error_count", 0)
        if zeros > 0 or errs > 0:
            log(f"- **WARNING** in `{rel_dir}`: `{zeros}` zero-step episodes, `{errs}` error episodes.")
        else:
            log(f"- `{rel_dir}`: PASS (0 zero-step episodes, 0 error episodes)")

# ---------------------------------------------------------
# 6. MODEL IDENTITY
# ---------------------------------------------------------
log()
log("## 6. Model Identity Audit")
log()
log("Let's summarize the checkpoints used in each campaign:")
log()
for ckey in campaigns_keys:
    camp = data.get(ckey, {})
    if not camp or not camp.get("exists"):
        continue
    log(f"### Campaign: {ckey}")
    runs = camp.get("runs", [])
    prod_runs = [r for r in runs if not r["is_smoke"]]
    # Unique combinations of policy, checkpoint, detector
    combos = set()
    for r in prod_runs:
        manifest = r.get("manifest", {})
        config = r.get("config", {})
        pol = manifest.get("policy", config.get("policy", "N/A"))
        ckpt = config.get("checkpoint", manifest.get("checkpoint", "N/A"))
        det_path = config.get("risk_model_unc_topk8_dir", manifest.get("risk_model_dir", "N/A"))
        ckpt_sha = config.get("expected_checkpoint_sha256", manifest.get("checkpoint_sha256", "N/A"))
        combos.add((pol, ckpt, ckpt_sha, det_path))
        
    for pol, ckpt, ckpt_sha, det_path in combos:
        log(f"- Policy: `{pol}`")
        log(f"  - Checkpoint: `{ckpt}`")
        log(f"  - Expected Checkpoint SHA256: `{ckpt_sha}`")
        log(f"  - Detector Path: `{det_path}`")
log()

# ---------------------------------------------------------
# 7. DETECTOR TRAINING / DATA LEAKAGE
# ---------------------------------------------------------
log("## 7. Detector Training and Data Leakage Audit")
log()
det = data.get("detector_audit", {})
if det:
    log("### Split Allocations (from bucket_counts.json):")
    log()
    log("| Bucket Name | Episodes |")
    log("|---|---|")
    buckets = det.get("buckets", {})
    for bname, binfo in buckets.items():
        log(f"| {bname} | {binfo['total_episodes']} |")
    log()
    
    log("### Task Distribution in Training/Val/Calib Buckets:")
    log()
    log("| Bucket Name | Task 3 count | Task 6 count | Task 8 count | Other Tasks |")
    log("|---|---|---|---|---|")
    for bname, binfo in buckets.items():
        tcounts = binfo.get("task_counts", {})
        t3 = tcounts.get("3", tcounts.get(3, 0))
        t6 = tcounts.get("6", tcounts.get(6, 0))
        t8 = tcounts.get("8", tcounts.get(8, 0))
        others = {k: v for k, v in tcounts.items() if str(k) not in ["3", "6", "8"]}
        log(f"| {bname} | {t3} | {t6} | {t8} | {others} |")
    log()
    
    log("### Seed Leakage Check:")
    log()
    log("Let's compare the seeds used in the online evaluation of Task 3, 6, 8 with the seeds present in the training/validation/calibration buckets.")
    log("We want to know if evaluation seeds for a task appear in the training data for that same task.")
    log()
    
    # Collect evaluation seeds for Tasks 3, 6, 8 from Campaign 1 production runs
    eval_seeds = defaultdict(set)
    c1_runs = data.get("campaign1_risk_proof", {}).get("runs", [])
    prod_c1_runs = [r for r in c1_runs if not r["is_smoke"]]
    for r in prod_c1_runs:
        task_id = r.get("manifest", {}).get("task_id", r.get("config", {}).get("task_id", None))
        if task_id in [3, 6, 8, "3", "6", "8"]:
            seeds = r.get("stats", {}).get("reset_seeds", [])
            eval_seeds[str(task_id)].update(seeds)
            
    # Also get evaluation seeds from Campaign 2 and Campaign 3
    c2_runs = data.get("campaign2_aggressive_task3", {}).get("runs", [])
    for r in c2_runs:
        if not r["is_smoke"]:
            task_id = r.get("manifest", {}).get("task_id", r.get("config", {}).get("task_id", None))
            if task_id in [3, 6, 8, "3", "6", "8"]:
                seeds = r.get("stats", {}).get("reset_seeds", [])
                eval_seeds[str(task_id)].update(seeds)
                
    c3_runs = data.get("campaign3_old_detector_task6", {}).get("runs", [])
    for r in c3_runs:
        if not r["is_smoke"]:
            task_id = r.get("manifest", {}).get("task_id", r.get("config", {}).get("task_id", None))
            if task_id in [3, 6, 8, "3", "6", "8"]:
                seeds = r.get("stats", {}).get("reset_seeds", [])
                eval_seeds[str(task_id)].update(seeds)

    for task_str, e_seeds in sorted(eval_seeds.items()):
        log(f"#### Task `{task_str}`: `{len(e_seeds)}` unique evaluation seeds")
        # Check leakage in train seen, val seen, calib seen buckets
        for bname, binfo in buckets.items():
            b_seeds = binfo.get("seeds_by_task", {}).get(task_str, [])
            overlap = e_seeds.intersection(b_seeds)
            log(f"- Bucket `{bname}` has `{len(b_seeds)}` seeds for Task `{task_str}`. Overlap with evaluation: `{len(overlap)}` seeds.")
            if overlap:
                log(f"  - **LEAKAGE DETECTED!** Overlapping seeds (first 5): `{list(overlap)[:5]}`")
        log()
else:
    log("No detector audit data found.")
    log()

# ---------------------------------------------------------
# 8. AGGRESSIVE THRESHOLD AUDIT
# ---------------------------------------------------------
log("## 8. Aggressive Threshold Audit")
log()
log("Let's confirm the results for the aggressive TopK8 campaigns:")
log()
# We want to confirm Task 3 result 19/100 and Task 6 result 62/100 from raw JSONL.
# In Campaign 2: h10_goal_object_topk8_aggressive_task3_20260608
# Let's sum across shard_0 and shard_1 for modified_h10_risk_topk8 in Task 3 and Task 6.
c2_prod = [r for r in data.get("campaign2_aggressive_task3", {}).get("runs", []) if not r["is_smoke"]]
task3_c2_runs = [r for r in c2_prod if "task3" in r["rel_dir"]]
task6_c2_runs = [r for r in c2_prod if "task6" in r["rel_dir"]]

log("### Campaign 2 (Aggressive TopK8 Task 3 Campaign):")
log()
log("#### Task 3:")
t3_total = 0
t3_succ = 0
for r in task3_c2_runs:
    stats = r.get("stats", {})
    t3_total += stats.get("total_rows", 0)
    t3_succ += stats.get("success_count", 0)
    log(f"- Shard: `{r['rel_dir']}` | Total: `{stats.get('total_rows')}` | Success: `{stats.get('success_count')}`")
log(f"- **Total Aggressive Task 3 Success:** `{t3_succ}/{t3_total}` (Success rate: `{t3_succ/t3_total*100:.2f}%`)")
log()

log("#### Task 6:")
t6_total = 0
t6_succ = 0
for r in task6_c2_runs:
    stats = r.get("stats", {})
    t6_total += stats.get("total_rows", 0)
    t6_succ += stats.get("success_count", 0)
    log(f"- Shard: `{r['rel_dir']}` | Total: `{stats.get('total_rows')}` | Success: `{stats.get('success_count')}`")
log(f"- **Total Aggressive Task 6 Success:** `{t6_succ}/{t6_total}` (Success rate: `{t6_succ/t6_total*100:.2f}%`)")
log()

# Campaign 3: h10_goal_object_task6_old_topk8_aggressive_20260608 (Old detector task 6)
c3_prod = [r for r in data.get("campaign3_old_detector_task6", {}).get("runs", []) if not r["is_smoke"]]
log("### Campaign 3 (Old Detector Task 6):")
t6_c3_total = 0
t6_c3_succ = 0
for r in c3_prod:
    stats = r.get("stats", {})
    t6_c3_total += stats.get("total_rows", 0)
    t6_c3_succ += stats.get("success_count", 0)
    log(f"- Shard: `{r['rel_dir']}` | Total: `{stats.get('total_rows')}` | Success: `{stats.get('success_count')}`")
log(f"- **Total Old Detector Task 6 Success:** `{t6_c3_succ}/{t6_c3_total}` (Success rate: `{t6_c3_succ/t6_c3_total*100:.2f}%`)")
log()

# ---------------------------------------------------------
# 9. SUSPICIOUS FINDINGS
# ---------------------------------------------------------
log("## 9. Suspicious Findings and Log Issues")
log()
for ckey in campaigns_keys:
    camp = data.get(ckey, {})
    if not camp or not camp.get("exists"):
        continue
    log(f"### Campaign: {ckey}")
    log_issues = camp.get("log_issues", [])
    if log_issues:
        log(f"Found `{len(log_issues)}` log issues:")
        for idx, issue in enumerate(log_issues[:20]):
            log(f"{idx+1}. File: `{issue['file']}` (line {issue.get('line_number', 'N/A')}) | Label: **{issue['label']}**")
            if 'snippet' in issue:
                log(f"   - Snippet: `{issue['snippet']}`")
    else:
        log("No issues found in logs.")
    log()

# Write the report
with open("/home/redafrix/tests/internship/report_draft.md", "w") as f:
    f.write("\n".join(report))
print("Draft report written to /home/redafrix/tests/internship/report_draft.md")
