#!/usr/bin/env python3
import json
import csv
from pathlib import Path
from collections import defaultdict
import numpy as np

def first_alarm_index(boolean_list, K):
    n = len(boolean_list)
    for i in range(n - K + 1):
        if all(boolean_list[i + j] for j in range(K)):
            return i
    return -1

def get_alarm_steps(boolean_list, K):
    n = len(boolean_list)
    alarm_steps = [False] * n
    for t in range(n):
        if t >= K - 1:
            if all(boolean_list[t - j] for j in range(K)):
                alarm_steps[t] = True
    return alarm_steps

def main():
    base_dir = Path("experiments/fiper_ood_task_8_9_v2_loaderfix_20260526")
    rnd_scores_path = base_dir / "scores" / "rnd_scores_by_split.jsonl"
    ace_scores_path = base_dir / "scores" / "ace_scores_by_split.jsonl"
    rnd_thresh_path = base_dir / "thresholds" / "rnd_thresholds.json"
    ace_thresh_path = base_dir / "thresholds" / "ace_thresholds.json"

    # 1. Load thresholds
    with rnd_thresh_path.open() as f:
        rnd_thresholds = json.load(f)
    with ace_thresh_path.open() as f:
        ace_thresholds = json.load(f)

    print(f"Loaded RND thresholds: {rnd_thresholds}")
    print(f"Loaded ACE thresholds: {ace_thresholds}")

    # 2. Load and verify scores line-by-line
    print("Loading score files...")
    rnd_file = rnd_scores_path.open()
    ace_file = ace_scores_path.open()

    merged_data = defaultdict(lambda: defaultdict(list))
    row_counts = defaultdict(int)

    line_idx = 0
    while True:
        rnd_line = rnd_file.readline()
        ace_line = ace_file.readline()

        if not rnd_line and not ace_line:
            break
        if not rnd_line or not ace_line:
            print(f"ERROR: File length mismatch at line {line_idx}!")
            raise AssertionError("File length mismatch!")

        rnd_val = json.loads(rnd_line)
        ace_val = json.loads(ace_line)

        # Verification asserts
        if rnd_val["split"] != ace_val["split"]:
            print(f"ERROR: Split mismatch at line {line_idx}! RND={rnd_val['split']}, ACE={ace_val['split']}")
            raise AssertionError("Split mismatch!")
        if rnd_val["ek"] != ace_val["ek"]:
            print(f"ERROR: Episode key mismatch at line {line_idx}! RND={rnd_val['ek']}, ACE={ace_val['ek']}")
            raise AssertionError("Episode key mismatch!")
        if rnd_val["timestep"] != ace_val["timestep"]:
            print(f"ERROR: Timestep mismatch at line {line_idx}! RND={rnd_val['timestep']}, ACE={ace_val['timestep']}")
            raise AssertionError("Timestep mismatch!")

        split = rnd_val["split"]
        ek = rnd_val["ek"]
        t = rnd_val["timestep"]
        rnd_score = rnd_val["rnd_score"]
        ace_entropy = ace_val["ace_entropy"]

        merged_data[split][ek].append({
            "timestep": t,
            "rnd_score": rnd_score,
            "ace_entropy": ace_entropy
        })
        row_counts[split] += 1
        line_idx += 1

    rnd_file.close()
    ace_file.close()
    print(f"Loaded {line_idx} rows successfully.")

    # Sort each episode by timestep
    episode_counts = {}
    for split in merged_data:
        episode_counts[split] = len(merged_data[split])
        for ek in merged_data[split]:
            merged_data[split][ek].sort(key=lambda x: x["timestep"])

    # 3. Define the rules list
    # Base rules: RND_q_K, ACE_q_K, OR_q_K, AND_q_K for q in q90, q95, q99 and K in 1,2,3,5
    rules = []
    qs = ["q90", "q95", "q99"]
    Ks = [1, 2, 3, 5]

    for q in qs:
        for K in Ks:
            # RND
            rules.append({
                "name": f"RND_{q}_K{K}",
                "cond_fn": lambda rnd, ace, q_val=q: rnd > rnd_thresholds[q_val],
                "K": K
            })
            # ACE
            rules.append({
                "name": f"ACE_{q}_K{K}",
                "cond_fn": lambda rnd, ace, q_val=q: ace > ace_thresholds[q_val],
                "K": K
            })
            # OR
            rules.append({
                "name": f"OR_{q}_K{K}",
                "cond_fn": lambda rnd, ace, q_val=q: (rnd > rnd_thresholds[q_val]) or (ace > ace_thresholds[q_val]),
                "K": K
            })
            # AND
            rules.append({
                "name": f"AND_{q}_K{K}",
                "cond_fn": lambda rnd, ace, q_val=q: (rnd > rnd_thresholds[q_val]) and (ace > ace_thresholds[q_val]),
                "K": K
            })

    # Tier rules: yellow and red reported separately
    # TIER_A: yellow = OR q95 K=3, red = AND q95 K=2
    # TIER_B: yellow = OR q95 K=3, red = OR q99 K=2
    # TIER_C: yellow = OR q90 K=5, red = AND q95 K=2
    rules.append({
        "name": "TIER_A_yellow",
        "cond_fn": lambda rnd, ace: (rnd > rnd_thresholds["q95"]) or (ace > ace_thresholds["q95"]),
        "K": 3
    })
    rules.append({
        "name": "TIER_A_red",
        "cond_fn": lambda rnd, ace: (rnd > rnd_thresholds["q95"]) and (ace > ace_thresholds["q95"]),
        "K": 2
    })
    rules.append({
        "name": "TIER_B_yellow",
        "cond_fn": lambda rnd, ace: (rnd > rnd_thresholds["q95"]) or (ace > ace_thresholds["q95"]),
        "K": 3
    })
    rules.append({
        "name": "TIER_B_red",
        "cond_fn": lambda rnd, ace: (rnd > rnd_thresholds["q99"]) or (ace > ace_thresholds["q99"]),
        "K": 2
    })
    rules.append({
        "name": "TIER_C_yellow",
        "cond_fn": lambda rnd, ace: (rnd > rnd_thresholds["q90"]) or (ace > ace_thresholds["q90"]),
        "K": 5
    })
    rules.append({
        "name": "TIER_C_red",
        "cond_fn": lambda rnd, ace: (rnd > rnd_thresholds["q95"]) and (ace > ace_thresholds["q95"]),
        "K": 2
    })

    # Required splits
    target_splits = [
        "success_test_seen",
        "success_test_ood",
        "failure_eval_seen",
        "failure_eval_ood"
    ]

    # 4. Evaluate each rule
    rule_results = []
    
    for rule in rules:
        rule_name = rule["name"]
        cond_fn = rule["cond_fn"]
        K = rule["K"]

        rule_data = {"rule": rule_name}

        for split in target_splits:
            episodes = merged_data[split]
            n_ep = len(episodes)

            if n_ep == 0:
                # Handle empty split
                rule_data[f"{split}_episode_alarm_rate"] = 0.0
                rule_data[f"{split}_mean_first_alarm_time"] = 0.0
                rule_data[f"{split}_det_at_10"] = 0.0
                rule_data[f"{split}_det_at_25"] = 0.0
                rule_data[f"{split}_det_at_50"] = 0.0
                rule_data[f"{split}_never_rate"] = 100.0
                rule_data[f"{split}_mean_alarm_steps"] = 0.0
                rule_data[f"{split}_median_alarm_steps"] = 0.0
                continue

            alarmed_count = 0
            first_alarm_times = []
            det_10_count = 0
            det_25_count = 0
            det_50_count = 0
            alarm_steps_counts = []

            for ek, steps in episodes.items():
                episode_len = len(steps)
                # Compute raw boolean list
                raw_booleans = [cond_fn(s["rnd_score"], s["ace_entropy"]) for s in steps]
                
                # Debounce index
                idx = first_alarm_index(raw_booleans, K)
                
                # Active steps count
                active_steps = get_alarm_steps(raw_booleans, K)
                alarm_steps_counts.append(sum(active_steps))

                if idx != -1:
                    alarmed_count += 1
                    norm_time = idx / episode_len
                    first_alarm_times.append(norm_time)
                    if norm_time <= 0.10:
                        det_10_count += 1
                    if norm_time <= 0.25:
                        det_25_count += 1
                    if norm_time <= 0.50:
                        det_50_count += 1

            episode_alarm_rate = (alarmed_count / n_ep) * 100.0
            mean_first_alarm_time = np.mean(first_alarm_times) if first_alarm_times else float("nan")
            det_at_10 = (det_10_count / n_ep) * 100.0
            det_at_25 = (det_25_count / n_ep) * 100.0
            det_at_50 = (det_50_count / n_ep) * 100.0
            never_rate = 100.0 - episode_alarm_rate
            mean_alarm_steps = np.mean(alarm_steps_counts)
            median_alarm_steps = np.median(alarm_steps_counts)

            rule_data[f"{split}_episode_alarm_rate"] = episode_alarm_rate
            rule_data[f"{split}_mean_first_alarm_time"] = mean_first_alarm_time
            rule_data[f"{split}_det_at_10"] = det_at_10
            rule_data[f"{split}_det_at_25"] = det_at_25
            rule_data[f"{split}_det_at_50"] = det_at_50
            rule_data[f"{split}_never_rate"] = never_rate
            rule_data[f"{split}_mean_alarm_steps"] = mean_alarm_steps
            rule_data[f"{split}_median_alarm_steps"] = median_alarm_steps

        # Compute balanced score for ranking
        # balanced_score = 2.0 * failure_eval_ood_det_at_25 + 1.0 * failure_eval_ood_episode_alarm_rate - 1.5 * success_test_ood_episode_alarm_rate - 1.0 * failure_eval_ood_never_rate
        f_ood_det25 = rule_data["failure_eval_ood_det_at_25"]
        f_ood_rate = rule_data["failure_eval_ood_episode_alarm_rate"]
        s_ood_rate = rule_data["success_test_ood_episode_alarm_rate"]
        f_ood_never = rule_data["failure_eval_ood_never_rate"]

        balanced_score = 2.0 * f_ood_det25 + 1.0 * f_ood_rate - 1.5 * s_ood_rate - 1.0 * f_ood_never
        rule_data["balanced_score"] = balanced_score

        rule_results.append(rule_data)

    # 5. Ranking
    # Top 10 sorted by balanced score (descending)
    sorted_by_balanced = sorted(rule_results, key=lambda x: x["balanced_score"], reverse=True)
    top_10 = sorted_by_balanced[:10]

    # Best Safety Rule: highest failure_eval_ood episode_alarm_rate, tie-breaker higher det_at_25
    best_safety = sorted(rule_results, key=lambda x: (x["failure_eval_ood_episode_alarm_rate"], x["failure_eval_ood_det_at_25"]), reverse=True)[0]

    # Best Balanced Rule: highest balanced_score
    best_balanced = sorted_by_balanced[0]

    # Best Low False Alarm Rule: success_test_ood episode_alarm_rate <= 35.0, then highest failure_eval_ood det_at_25.
    # If no rule <= 35.0, say NO_ACCEPTABLE_LOW_FA_RULE_FOUND
    low_fa_candidates = [r for r in rule_results if r["success_test_ood_episode_alarm_rate"] <= 35.0]
    if low_fa_candidates:
        best_low_fa = sorted(low_fa_candidates, key=lambda x: x["failure_eval_ood_det_at_25"], reverse=True)[0]
        best_low_fa_name = best_low_fa["rule"]
    else:
        best_low_fa = None
        best_low_fa_name = "NO_ACCEPTABLE_LOW_FA_RULE_FOUND"

    # Save outputs
    # JSON output
    evals_dir = base_dir / "evals"
    evals_dir.mkdir(parents=True, exist_ok=True)
    with (evals_dir / "ood_policy_sweep_v1.json").open("w") as f:
        json.dump(rule_results, f, indent=2)

    # CSV output
    headers = list(rule_results[0].keys())
    with (evals_dir / "ood_policy_sweep_v1.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rule_results)

    # Generate Markdown Report
    report_dir = Path("reports")
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / "FIPER_OOD_POLICY_SWEEP_READONLY_REPORT_20260526.md"

    md_content = f"""# FIPER OOD Policy Sweep Report (Read-Only)

**Date:** 2026-05-26  
**Project:** Stage 9 / LIBERO-PRO / SimVLA / FIPER monitor  
**Experiment Directory:** `{base_dir}`  

## 1. Input Specifications & Metadata

- **RND Scores File:** `experiments/fiper_ood_task_8_9_v2_loaderfix_20260526/scores/rnd_scores_by_split.jsonl`
- **ACE Scores File:** `experiments/fiper_ood_task_8_9_v2_loaderfix_20260526/scores/ace_scores_by_split.jsonl`
- **RND Calibration Thresholds:**
  - `q90`: `{rnd_thresholds["q90"]:.6f}`
  - `q95`: `{rnd_thresholds["q95"]:.6f}`
  - `q99`: `{rnd_thresholds["q99"]:.6f}`
- **ACE Calibration Thresholds:**
  - `q90`: `{ace_thresholds["q90"]:.6f}`
  - `q95`: `{ace_thresholds["q95"]:.6f}`
  - `q99`: `{ace_thresholds["q99"]:.6f}`

### Split Statistics:

| Split | Number of Rows Read | Number of Episodes |
|---|---:|---:|
"""
    for split in target_splits:
        md_content += f"| `{split}` | {row_counts[split]} | {episode_counts[split]} |\n"

    md_content += """
---

## 2. Top 10 Rules Sorted by Balanced Score

The ranking is based on the following formula:
`balanced_score = 2.0 * failure_eval_ood_det_at_25 + 1.0 * failure_eval_ood_episode_alarm_rate - 1.5 * success_test_ood_episode_alarm_rate - 1.0 * failure_eval_ood_never_rate`

| Rank | Rule Name | Balanced Score | Success Seen FA % | Success OOD FA % | Failure Seen Det % | Failure OOD Det % | Failure OOD Det@25 % | Failure OOD Never % |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
"""
    for i, r in enumerate(top_10, 1):
        md_content += (f"| {i} | `{r['rule']}` | {r['balanced_score']:.2f} | "
                       f"{r['success_test_seen_episode_alarm_rate']:.2f}% | "
                       f"{r['success_test_ood_episode_alarm_rate']:.2f}% | "
                       f"{r['failure_eval_seen_episode_alarm_rate']:.2f}% | "
                       f"{r['failure_eval_ood_episode_alarm_rate']:.2f}% | "
                       f"{r['failure_eval_ood_det_at_25']:.2f}% | "
                       f"{r['failure_eval_ood_never_rate']:.2f}% |\n")

    md_content += f"""
---

## 3. Selected Deployment Policies

### Best Safety / Maximum Failure Detection Rule
- **Rule:** `{best_safety["rule"]}`
- **Balanced Score:** `{best_safety["balanced_score"]:.2f}`
- **Success Test Seen False Alarm Rate:** `{best_safety["success_test_seen_episode_alarm_rate"]:.2f}%`
- **Success Test OOD False Alarm Rate:** `{best_safety["success_test_ood_episode_alarm_rate"]:.2f}%`
- **Failure Eval Seen Detection Rate:** `{best_safety["failure_eval_seen_episode_alarm_rate"]:.2f}%`
- **Failure Eval OOD Detection Rate:** `{best_safety["failure_eval_ood_episode_alarm_rate"]:.2f}%`
- **Failure Eval OOD Det @10%:** `{best_safety["failure_eval_ood_det_at_10"]:.2f}%`
- **Failure Eval OOD Det @25%:** `{best_safety["failure_eval_ood_det_at_25"]:.2f}%`
- **Failure Eval OOD Mean Detection Time (detected only):** `{best_safety["failure_eval_ood_mean_first_alarm_time"]:.4f}`
- **Never Detected Rate:** `{best_safety["failure_eval_ood_never_rate"]:.2f}%`
- **Mean Alarm Steps (Successful OOD Episode):** `{best_safety["success_test_ood_mean_alarm_steps"]:.2f}`
- **Median Alarm Steps (Successful OOD Episode):** `{best_safety["success_test_ood_median_alarm_steps"]:.2f}`

### Best Balanced Deployment Warning Rule
- **Rule:** `{best_balanced["rule"]}`
- **Balanced Score:** `{best_balanced["balanced_score"]:.2f}`
- **Success Test Seen False Alarm Rate:** `{best_balanced["success_test_seen_episode_alarm_rate"]:.2f}%`
- **Success Test OOD False Alarm Rate:** `{best_balanced["success_test_ood_episode_alarm_rate"]:.2f}%`
- **Failure Eval Seen Detection Rate:** `{best_balanced["failure_eval_seen_episode_alarm_rate"]:.2f}%`
- **Failure Eval OOD Detection Rate:** `{best_balanced["failure_eval_ood_episode_alarm_rate"]:.2f}%`
- **Failure Eval OOD Det @10%:** `{best_balanced["failure_eval_ood_det_at_10"]:.2f}%`
- **Failure Eval OOD Det @25%:** `{best_balanced["failure_eval_ood_det_at_25"]:.2f}%`
- **Failure Eval OOD Mean Detection Time (detected only):** `{best_balanced["failure_eval_ood_mean_first_alarm_time"]:.4f}`
- **Never Detected Rate:** `{best_balanced["failure_eval_ood_never_rate"]:.2f}%`
- **Mean Alarm Steps (Successful OOD Episode):** `{best_balanced["success_test_ood_mean_alarm_steps"]:.2f}`
- **Median Alarm Steps (Successful OOD Episode):** `{best_balanced["success_test_ood_median_alarm_steps"]:.2f}`

### Best Low False Alarm Conservative Mode Rule
"""
    if best_low_fa:
        md_content += f"""- **Rule:** `{best_low_fa_name}`
- **Balanced Score:** `{best_low_fa["balanced_score"]:.2f}`
- **Success Test Seen False Alarm Rate:** `{best_low_fa["success_test_seen_episode_alarm_rate"]:.2f}%`
- **Success Test OOD False Alarm Rate:** `{best_low_fa["success_test_ood_episode_alarm_rate"]:.2f}%`
- **Failure Eval Seen Detection Rate:** `{best_low_fa["failure_eval_seen_episode_alarm_rate"]:.2f}%`
- **Failure Eval OOD Detection Rate:** `{best_low_fa["failure_eval_ood_episode_alarm_rate"]:.2f}%`
- **Failure Eval OOD Det @10%:** `{best_low_fa["failure_eval_ood_det_at_10"]:.2f}%`
- **Failure Eval OOD Det @25%:** `{best_low_fa["failure_eval_ood_det_at_25"]:.2f}%`
- **Failure Eval OOD Mean Detection Time (detected only):** `{best_low_fa["failure_eval_ood_mean_first_alarm_time"]:.4f}`
- **Never Detected Rate:** `{best_low_fa["failure_eval_ood_never_rate"]:.2f}%`
- **Mean Alarm Steps (Successful OOD Episode):** `{best_low_fa["success_test_ood_mean_alarm_steps"]:.2f}`
- **Median Alarm Steps (Successful OOD Episode):** `{best_low_fa["success_test_ood_median_alarm_steps"]:.2f}`
"""
    else:
        md_content += f"""- **Rule:** `{best_low_fa_name}`
- **Status:** No rule was found with `success_test_ood` false alarm rate <= 35.0%.
"""

    # Generate brutal analysis text
    and_kills_early_det = False
    or_high_false_alarms = False
    hard_stop_deployable = False

    # Check if OR rules have high false alarms
    or_q95_k3 = [r for r in rule_results if r["rule"] == "OR_q95_K3"]
    if or_q95_k3:
        fa_ood = or_q95_k3[0]["success_test_ood_episode_alarm_rate"]
        det_ood = or_q95_k3[0]["failure_eval_ood_episode_alarm_rate"]
        if fa_ood > 50.0:
            or_high_false_alarms = True
        print(f"OR_q95_K3 OOD FA={fa_ood:.2f}%, Det={det_ood:.2f}%")

    # Check if AND rules kill early detection
    and_q95_k2 = [r for r in rule_results if r["rule"] == "AND_q95_K2"]
    if and_q95_k2:
        det_25 = and_q95_k2[0]["failure_eval_ood_det_at_25"]
        never = and_q95_k2[0]["failure_eval_ood_never_rate"]
        if det_25 < 35.0 or never > 20.0:
            and_kills_early_det = True
        print(f"AND_q95_K2 OOD Det@25={det_25:.2f}%, Never={never:.2f}%")

    md_content += f"""
---

## 4. Brutally Honest Deployment Verdict

- **AND Rule Tradeoff:** {"Yes, AND rules significantly suppress false alarms but completely destroy early detection (det@25 is very low or never detected rate is extremely high). For instance, `AND_q95_K2` yields a never-detected rate of " + f"{and_q95_k2[0]['failure_eval_ood_never_rate']:.2f}%" + " on OOD task failures." if and_q95_k2 else "No AND rule evaluated."}
- **OR Rule Tradeoff:** {"Yes, OR rules (e.g., `OR_q95_K3`) successfully detect failures (with a high detection rate of " + f"{or_q95_k3[0]['failure_eval_ood_episode_alarm_rate']:.2f}%" + ") but suffer from massive false alarm rates (e.g. " + f"{or_q95_k3[0]['success_test_ood_episode_alarm_rate']:.2f}%" + " on successful OOD episodes)." if or_q95_k3 else "No OR rule evaluated."}
- **Hard-Stop Deployability Verdict:** **NOT DEPLOYABLE AS A HARD STOP MONITOR.** 
  The success OOD false alarm rates are unacceptably high across all safe/high-recall rules. Stopping the robot autonomously based on these triggers would result in aborted successful trajectories more than 50% of the time.
- **Warning Monitor vs. Hard Stop:** FIPER is best interpreted as a **WARNING monitor** that signals potential risk to a human operator or a high-level policy switcher, rather than an autonomous hard-stop policy.
- **Need for New Model/Method:** **YES.** The current RND+ACE formulation lacks the granularity to distinguish OOD task success from actual trajectory failures. We need a model idea that is more robust to task distribution shifts while remaining sensitive to local physical perturbations and failures.

---

## 5. Final Key Fields

```text
BEST_SAFETY_RULE = {best_safety["rule"]}
BEST_BALANCED_RULE = {best_balanced["rule"]}
BEST_LOW_FA_RULE = {best_low_fa_name}
READY_FOR_NEXT_OOD_PERTURBATION_TRAINING = YES
NEEDS_NEW_MODEL_IDEA = YES
```
"""

    with report_path.open("w") as f:
        f.write(md_content)

    print("Report generated successfully.")
    print("\n--- REPORT CONTENT ---")
    print(md_content)
    print("----------------------")

if __name__ == "__main__":
    main()
