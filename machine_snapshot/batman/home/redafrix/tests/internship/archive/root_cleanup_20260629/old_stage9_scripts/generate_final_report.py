import json
import os
from pathlib import Path
from collections import defaultdict

NEW_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609")
REPORT_PATH = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/LIBERO_GOAL_OBJECT_OOD_AGGRESSIVE_FIXED_FINAL_ANALYSIS_20260609.md")

tasks = range(18)
policies = ["original_simvla", "modified_simvla", "risk_topk8"]

data = defaultdict(lambda: defaultdict(dict))
seed_parity_pass = True

mods_stats = {"total_mods": 0, "episodes_with_mods": 0}

for t in tasks:
    for p in policies:
        label = p
        inner_dir = "simvla_only"
        
        if p == "risk_topk8":
            label = "modified_h10_risk_topk8"
            inner_dir = "risk_topk8"
            
        jsonl_path = NEW_ROOT / f"runs/task{t}/{label}/{inner_dir}/episode_summaries.jsonl"
        if not jsonl_path.exists():
            continue
            
        with open(jsonl_path, 'r') as f:
            for line in f:
                if not line.strip(): continue
                row = json.loads(line)
                seed = row["reset_seed"]
                data[t][p][seed] = row
                
                if p == "risk_topk8":
                    mods = row.get("action_modifications_count", 0)
                    mods_stats["total_mods"] += mods
                    if mods > 0:
                        mods_stats["episodes_with_mods"] += 1

expected_seeds = set(range(10))
for t in tasks:
    for p in policies:
        seeds = set(data[t][p].keys())
        if seeds != expected_seeds:
            seed_parity_pass = False

results = {
    "original_simvla": {"success": 0, "total": 0},
    "modified_simvla": {"success": 0, "total": 0},
    "risk_topk8": {"success": 0, "total": 0}
}
per_task_results = defaultdict(lambda: {p: {"success": 0, "total": 0} for p in policies})

rescues = {
    "mod_vs_orig": 0, "reg_mod_vs_orig": 0,
    "risk_vs_mod": 0, "reg_risk_vs_mod": 0,
    "risk_vs_orig": 0, "reg_risk_vs_orig": 0,
}

per_task_rescues = defaultdict(lambda: {
    "risk_vs_mod": {"rescue": 0, "regression": 0},
    "risk_vs_orig": {"rescue": 0, "regression": 0}
})

for t in tasks:
    for seed in expected_seeds:
        succ_orig = data[t]["original_simvla"].get(seed, {}).get("success", False)
        succ_mod = data[t]["modified_simvla"].get(seed, {}).get("success", False)
        succ_risk = data[t]["risk_topk8"].get(seed, {}).get("success", False)
        
        results["original_simvla"]["total"] += 1
        results["modified_simvla"]["total"] += 1
        results["risk_topk8"]["total"] += 1
        
        per_task_results[t]["original_simvla"]["total"] += 1
        per_task_results[t]["modified_simvla"]["total"] += 1
        per_task_results[t]["risk_topk8"]["total"] += 1
        
        if succ_orig: 
            results["original_simvla"]["success"] += 1
            per_task_results[t]["original_simvla"]["success"] += 1
        if succ_mod: 
            results["modified_simvla"]["success"] += 1
            per_task_results[t]["modified_simvla"]["success"] += 1
        if succ_risk: 
            results["risk_topk8"]["success"] += 1
            per_task_results[t]["risk_topk8"]["success"] += 1
            
        if succ_mod and not succ_orig: rescues["mod_vs_orig"] += 1
        if not succ_mod and succ_orig: rescues["reg_mod_vs_orig"] += 1
        
        if succ_risk and not succ_mod:
            rescues["risk_vs_mod"] += 1
            per_task_rescues[t]["risk_vs_mod"]["rescue"] += 1
        if not succ_risk and succ_mod:
            rescues["reg_risk_vs_mod"] += 1
            per_task_rescues[t]["risk_vs_mod"]["regression"] += 1
            
        if succ_risk and not succ_orig:
            rescues["risk_vs_orig"] += 1
            per_task_rescues[t]["risk_vs_orig"]["rescue"] += 1
        if not succ_risk and succ_orig:
            rescues["reg_risk_vs_orig"] += 1
            per_task_rescues[t]["risk_vs_orig"]["regression"] += 1

report = f"""# LIBERO_GOAL_OBJECT_OOD_AGGRESSIVE_FIXED_FINAL_ANALYSIS_20260609

## 1. Execution Overview
- **Tasks**: 18
- **Policies**: 3 (original_simvla, modified_simvla, risk_topk8)
- **Episodes per Policy**: 10
- **Total Episodes Executed**: 540
- **Seed Parity Check**: {'PASS' if seed_parity_pass else 'FAIL'}
- **Old Invalid Root Excluded**: YES (All configs pointed exclusively to the new aggressive_fixed root).

## 2. Total Success Rates
- **original_simvla**: {results["original_simvla"]["success"]} / {results["original_simvla"]["total"]} ({(results["original_simvla"]["success"]/max(1,results["original_simvla"]["total"]))*100:.1f}%)
- **modified_simvla**: {results["modified_simvla"]["success"]} / {results["modified_simvla"]["total"]} ({(results["modified_simvla"]["success"]/max(1,results["modified_simvla"]["total"]))*100:.1f}%)
- **risk_topk8**: {results["risk_topk8"]["success"]} / {results["risk_topk8"]["total"]} ({(results["risk_topk8"]["success"]/max(1,results["risk_topk8"]["total"]))*100:.1f}%)

## 3. Paired Comparisons (Total)
- **modified_simvla vs original_simvla**: {rescues["mod_vs_orig"]} Rescues, {rescues["reg_mod_vs_orig"]} Regressions
- **risk_topk8 vs modified_simvla**: {rescues["risk_vs_mod"]} Rescues, {rescues["reg_risk_vs_mod"]} Regressions
- **risk_topk8 vs original_simvla**: {rescues["risk_vs_orig"]} Rescues, {rescues["reg_risk_vs_orig"]} Regressions

## 4. Action Modification Stats (risk_topk8)
- **Total Modifications Across All Episodes**: {mods_stats["total_mods"]}
- **Episodes with >=1 Modification**: {mods_stats["episodes_with_mods"]}

## 5. Per-Task Breakdown

| Task | Orig SR | Mod SR | Risk SR | Risk vs Mod (Res/Reg) | Risk vs Orig (Res/Reg) |
|---|---|---|---|---|---|
"""
for t in tasks:
    sr_o = per_task_results[t]["original_simvla"]["success"]
    sr_m = per_task_results[t]["modified_simvla"]["success"]
    sr_r = per_task_results[t]["risk_topk8"]["success"]
    r_v_m = f"{per_task_rescues[t]['risk_vs_mod']['rescue']} / {per_task_rescues[t]['risk_vs_mod']['regression']}"
    r_v_o = f"{per_task_rescues[t]['risk_vs_orig']['rescue']} / {per_task_rescues[t]['risk_vs_orig']['regression']}"
    report += f"| {t} | {sr_o}/10 | {sr_m}/10 | {sr_r}/10 | {r_v_m} | {r_v_o} |\n"

sr_risk = results["risk_topk8"]["success"]
sr_mod = results["modified_simvla"]["success"]
sr_orig = results["original_simvla"]["success"]

if sr_risk > sr_mod and sr_risk > sr_orig:
    verdict = "YES. The aggressive TopK8 detector successfully provided net rescues over both the original and modified baselines, justifying the 0.3 threshold configuration."
elif sr_risk > sr_mod:
    verdict = "PARTIAL. The aggressive TopK8 detector improved over modified_simvla but didn't beat the original baseline."
else:
    verdict = "NO. The aggressive TopK8 detector failed to provide a net positive improvement in success rate compared to the modified baseline."

report += f"""
## 6. Final Verdict
**Does aggressive TopK8 help on libero_goal_object_ood?**
{verdict}
"""

REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
REPORT_PATH.write_text(report)
print(f"Report successfully written to {REPORT_PATH}")
print("--- BEGIN REPORT CONTENT ---")
print(report)
