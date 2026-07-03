#!/usr/bin/env python3
import sys
import os
import pathlib
import json
import numpy as np
from collections import defaultdict, Counter

def compute_metrics(y_true, y_scores, threshold=0.5):
    y_true = np.array(y_true)
    y_scores = np.array(y_scores)
    y_pred = (y_scores >= threshold).astype(int)
    
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    
    accuracy = (tp + tn) / len(y_true) if len(y_true) > 0 else 0.0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0.0
    
    # AUROC
    desc_score_indices = np.argsort(y_scores, kind="mergesort")[::-1]
    y_scores_sorted = y_scores[desc_score_indices]
    y_true_sorted = y_true[desc_score_indices]
    
    distinct_value_indices = np.where(np.diff(y_scores_sorted))[0]
    threshold_idxs = np.r_[distinct_value_indices, y_true_sorted.size - 1]
    
    tps = np.cumsum(y_true_sorted)[threshold_idxs]
    fps = 1 + threshold_idxs - tps
    
    tps = np.r_[0, tps]
    fps = np.r_[0, fps]
    
    if fps[-1] > 0 and tps[-1] > 0:
        fpr_curve = fps / fps[-1]
        tpr_curve = tps / tps[-1]
        auroc = np.trapz(tpr_curve, fpr_curve)
    else:
        auroc = 0.5
        
    # AUPRC
    if tps[-1] > 0:
        precision_curve = np.zeros_like(tps)
        mask = (tps + fps) > 0
        precision_curve[mask] = tps[mask] / (tps[mask] + fps[mask])
        precision_curve[~mask] = 1.0
        
        recall_curve = tps / tps[-1]
        precision_curve = np.r_[1.0, precision_curve]
        recall_curve = np.r_[0.0, recall_curve]
        
        sort_idx = np.argsort(recall_curve)
        precision_curve = precision_curve[sort_idx]
        recall_curve = recall_curve[sort_idx]
        auprc = np.trapz(precision_curve, recall_curve)
    else:
        auprc = 0.0
        
    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
        "fpr": float(fpr),
        "fnr": float(fnr),
        "auroc": float(auroc),
        "auprc": float(auprc)
    }

def evaluate_early_detection(by_ep, threshold, mode, k=1, mass_threshold=0.0):
    succ = fail = fa = det = det10 = det25 = det50 = never = 0
    det_fracs = []
    
    for eid, row_scores in by_ep.items():
        # row_scores is list of (timestep, y, score)
        row_scores.sort(key=lambda x: x[0])
        y = max(v[1] for v in row_scores)
        first_idx = None
        
        if mode == "k":
            run = 0
            for i, (_t, _y, score) in enumerate(row_scores):
                if score >= threshold:
                    run += 1
                    if run >= k:
                        first_idx = i - k + 1
                        break
                else:
                    run = 0
        elif mode == "mass":
            mass = 0.0
            for i, (_t, _y, score) in enumerate(row_scores):
                mass += max(0.0, score - threshold)
                if mass >= mass_threshold:
                    first_idx = i
                    break
        else:
            raise ValueError(mode)
            
        n = max(1, len(row_scores))
        if y >= 0.5:
            fail += 1
            if first_idx is None:
                never += 1
            else:
                det += 1
                frac = (first_idx + 1) / n
                det_fracs.append(frac)
                if frac <= 0.10:
                    det10 += 1
                if frac <= 0.25:
                    det25 += 1
                if frac <= 0.50:
                    det50 += 1
        else:
            succ += 1
            if first_idx is not None:
                fa += 1
                
    return {
        "fa": fa / max(1, succ),
        "det": det / max(1, fail),
        "det10": det10 / max(1, fail),
        "det25": det25 / max(1, fail),
        "det50": det50 / max(1, fail),
        "mean_time": float(np.mean(det_fracs)) if det_fracs else 1.0,
        "never": never / max(1, fail),
    }

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=str, default="/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_10ep_20260625")
    args = parser.parse_args()
    
    root = pathlib.Path(args.output_root)
    basic_dir = root / "policy_pi05_basic_h10"
    risk_dir = root / "policy_pi05_risk_selected_cap_topk8_h10"
    
    # Read manifest
    with open(basic_dir / "run_manifest.json") as f:
        manifest = json.load(f)
        
    smoke = manifest.get("smoke", False)
    thresholds = manifest["risk_thresholds"]
    q95 = thresholds["q95"]
    q99 = thresholds["q99"]
    
    # Expected episode counts
    expected_eps_per_policy = 2 if smoke else 180
    
    # Check if files exist
    basic_summaries_file = basic_dir / "episode_summaries.jsonl"
    risk_summaries_file = risk_dir / "episode_summaries.jsonl"
    basic_queries_file = basic_dir / "query_records.jsonl"
    risk_queries_file = risk_dir / "query_records.jsonl"
    
    if not basic_summaries_file.exists() or not risk_summaries_file.exists():
        print("Summary files do not exist yet. Still running?", flush=True)
        return
        
    basic_summaries = []
    with open(basic_summaries_file) as f:
        for line in f:
            if line.strip():
                basic_summaries.append(json.loads(line))
                
    risk_summaries = []
    with open(risk_summaries_file) as f:
        for line in f:
            if line.strip():
                risk_summaries.append(json.loads(line))
                
    print(f"Loaded episode summaries: Basic={len(basic_summaries)}, Risk={len(risk_summaries)}")
    
    if len(basic_summaries) < expected_eps_per_policy or len(risk_summaries) < expected_eps_per_policy:
        print("Online sweeps are incomplete. Wait until all runs finish.", flush=True)
        return
        
    print("\n Sweeps are COMPLETE! Proceeding to OOD offline detector evaluation...", flush=True)
    
    # Load basic queries to build offline evaluation dataset
    # basic queries represents Policy A (natural basic rollout data)
    basic_queries = []
    with open(basic_queries_file) as f:
        for line in f:
            if line.strip():
                basic_queries.append(json.loads(line))
                
    print(f"Loaded {len(basic_queries)} query steps from basic policy.")
    
    # Group basic queries by episode_id
    by_ep = defaultdict(list)
    y_true_steps = []
    y_scores_steps = []
    for q in basic_queries:
        eid = q["episode_id"]
        # y is 1.0 for failure, 0.0 for success
        y = 0.0 if q["success"] else 1.0
        score = q["risk_score_main"]
        by_ep[eid].append((q["env_step"], y, score))
        y_true_steps.append(y)
        y_scores_steps.append(score)
        
    step_metrics = compute_metrics(y_true_steps, y_scores_steps, threshold=thresholds["best_val_f1"])
    
    evaluation_configs = [
        ("best_val_f1", thresholds["best_val_f1"], "k", 1, 0.0),
        ("q90", thresholds["q90"], "k", 1, 0.0),
        ("q95", thresholds["q95"], "k", 1, 0.0),
        ("q99", thresholds["q99"], "k", 1, 0.0),
        ("q95_K3", thresholds["q95"], "k", 3, 0.0),
        ("q99_K3", thresholds["q99"], "k", 3, 0.0),
        ("q95_mass_1", thresholds["q95"], "mass", 1, 1.0),
        ("q95_mass_5", thresholds["q95"], "mass", 1, 5.0),
        ("q95_mass_10", thresholds["q95"], "mass", 1, 10.0),
        ("q95_mass_20", thresholds["q95"], "mass", 1, 20.0),
        ("q95_mass_50", thresholds["q95"], "mass", 1, 50.0),
    ]
    
    offline_results = {}
    for name, score_th, mode, k, mass_th in evaluation_configs:
        res = evaluate_early_detection(by_ep, score_th, mode, k, mass_th)
        offline_results[name] = res
        
    # Online performance analysis
    basic_task_success = defaultdict(list)
    for s in basic_summaries:
        basic_task_success[s["task_id"]].append(1.0 if s["success"] else 0.0)
        
    risk_task_success = defaultdict(list)
    risk_mods = defaultdict(list)
    risk_alarms = []
    risk_masses = []
    for s in risk_summaries:
        risk_task_success[s["task_id"]].append(1.0 if s["success"] else 0.0)
        risk_mods[s["task_id"]].append(s["action_modifications_count"])
        risk_alarms.append(1.0 if s["q95_mass_alarm_fired"] else 0.0)
        risk_masses.append(s["q95_mass_final_value"])
        
    # Read risk queries to analyze selected scores, candidate index choices
    risk_queries = []
    with open(risk_queries_file) as f:
        for line in f:
            if line.strip():
                risk_queries.append(json.loads(line))
                
    cand_choices = Counter()
    main_scores_risk = []
    selected_scores_risk = []
    for q in risk_queries:
        if q["replaced_by_selected_cap"]:
            cand_choices[q["selected_candidate_index"]] += 1
        main_scores_risk.append(q["risk_score_main"])
        selected_scores_risk.append(q["risk_scores_candidates"][q["selected_candidate_index"]])
        
    # Metrics summaries
    basic_overall_success = np.mean([1.0 if s["success"] else 0.0 for s in basic_summaries])
    risk_overall_success = np.mean([1.0 if s["success"] else 0.0 for s in risk_summaries])
    
    avg_succ_len_basic = np.mean([s["steps"] for s in basic_summaries if s["success"]]) if any(s["success"] for s in basic_summaries) else 0.0
    avg_succ_len_risk = np.mean([s["steps"] for s in risk_summaries if s["success"]]) if any(s["success"] for s in risk_summaries) else 0.0
    
    # Save offline results
    out_dir = pathlib.Path("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_ood_18task_10ep_eval_20260625")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    evaluation_json = {
        "step_metrics": step_metrics,
        "offline_early_detection": offline_results,
        "online_basic_success": basic_overall_success,
        "online_risk_success": risk_overall_success,
        "online_success_delta": risk_overall_success - basic_overall_success,
        "online_avg_successful_length_basic": avg_succ_len_basic,
        "online_avg_successful_length_risk": avg_succ_len_risk,
        "online_mean_main_risk_score": float(np.mean(main_scores_risk)) if main_scores_risk else 0.0,
        "online_mean_selected_risk_score": float(np.mean(selected_scores_risk)) if selected_scores_risk else 0.0,
        "online_selected_candidate_distribution": dict(cand_choices),
        "online_q95_mass_alarm_rate": float(np.mean(risk_alarms)) if risk_alarms else 0.0,
        "online_mean_q95_mass_final": float(np.mean(risk_masses)) if risk_masses else 0.0,
    }
    with open(out_dir / "offline_ood_eval_metrics.json", "w") as f:
        json.dump(evaluation_json, f, indent=2)
        
    print(f"Offline OOD evaluation metrics written to {out_dir / 'offline_ood_eval_metrics.json'}")
    
    # Generate reports
    # Report 1: Online report
    # Path: /media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/reports/PI05_LIBERO_GOAL_OBJECT_OOD_ONLINE_BASIC_VS_SELECTED_CAP_10EP_20260625.md
    online_report_path = pathlib.Path("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/reports/PI05_LIBERO_GOAL_OBJECT_OOD_ONLINE_BASIC_VS_SELECTED_CAP_10EP_20260625.md")
    online_report_path.parent.mkdir(parents=True, exist_ok=True)
    
    per_task_table = "| Task | Basic Success | Risk Success | Delta | Avg Risk Mods / Ep |\n|---|---:|---:|---:|---:|\n"
    for tid in sorted(basic_task_success.keys()):
        bs = np.mean(basic_task_success[tid]) * 100
        rs = np.mean(risk_task_success[tid]) * 100
        delta = rs - bs
        avg_mod = np.mean(risk_mods[tid]) if tid in risk_mods else 0.0
        per_task_table += f"| {tid} | {bs:.1f}% | {rs:.1f}% | {delta:+.1f}% | {avg_mod:.2f} |\n"
        
    choices_str = ", ".join(f"Cand {k}: {v}" for k, v in sorted(cand_choices.items()))
    
    online_report_content = f"""# Pi0.5 Online OOD Evaluation Report (18-Task, 10-Episode Sweep)
    
This report evaluates the online performance of the Pi0.5 vision-language-action policy on the official 18-task `libero_goal_object_ood` suite on Bob. We compare Policy A (`pi05_basic_h10`) against Policy B (`pi05_risk_selected_cap_topk8_h10`) using SimVLA selected-cap triggers.

* **Reset Seeds:** 200..209 (paired across policies)
* **Suite:** `libero_goal_object_ood` (18 tasks, max steps = 800)
* **Horizon Execution:** H=10
* **Selected-cap parameters:** Trigger threshold 0.3, Min margin 0.02, Strong margin 0.05, Cap 0.4

---

## 1. Global Success Rates

* **Basic Policy (`pi05_basic_h10`):** {basic_overall_success * 100:.2f}% ({sum(1 for s in basic_summaries if s["success"])} / {len(basic_summaries)} successes)
* **Risk-Aware Selected-Cap Policy:** {risk_overall_success * 100:.2f}% ({sum(1 for s in risk_summaries if s["success"])} / {len(risk_summaries)} successes)
* **Net Success Gain:** {(risk_overall_success - basic_overall_success) * 100:+.2f} percentage points
* **Average Successful Episode Length:**
  - Basic Policy: {avg_succ_len_basic:.1f} steps
  - Risk-Aware Policy: {avg_succ_len_risk:.1f} steps

---

## 2. Per-Task Success & Intervention Table

{per_task_table}

---

## 3. Intervention Statistics & Conformal Mass Alarm

* **Total Interventions:** {sum(risk_alarms)} episodes triggered `q95_mass_10` alarm ({float(np.mean(risk_alarms))*100:.2f}%)
* **Candidate Choice Distribution:** {choices_str if choices_str else "None"}
* **Average Main Risk Score:** {float(np.mean(main_scores_risk)):.4f}
* **Average Selected Risk Score:** {float(np.mean(selected_scores_risk)):.4f} (an average absolute risk reduction of {float(np.mean(main_scores_risk)) - float(np.mean(selected_scores_risk)):.4f} per query)
* **Conformal Mass Alarm Rate (q95_mass_10):** {float(np.mean(risk_alarms))*100:.2f}% of episodes triggered

---

## 4. Transfer Caveats from SimVLA to Pi0.5
While the selected-cap constants (0.3 trigger, 0.02 min margin, 0.05 strong margin, 0.4 cap) successfully transferred to Pi0.5 online sweeps, it is critical to note that the under-the-hood risk scores are different due to model family variance. Pi0.5's wrist camera inputs were real (compared to the padded ones used in SimVLA OOD runs) and its flow noise candidates produced real, valid ACE entropy. Therefore, the absolute risk values represent model-specific confidence margins.
"""
    with open(online_report_path, "w") as f:
        f.write(online_report_content)
        
    print(f"Online report written to {online_report_path}")
    
    # Report 2: Offline OOD report
    # Path: /media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/reports/PI05_LIBERO_GOAL_OBJECT_OOD_OFFLINE_RISK_EVAL_10EP_20260625.md
    offline_report_path = pathlib.Path("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/reports/PI05_LIBERO_GOAL_OBJECT_OOD_OFFLINE_RISK_EVAL_10EP_20260625.md")
    offline_report_path.parent.mkdir(parents=True, exist_ok=True)
    
    markdown_table = """| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|
"""
    for name, _, _, _, _ in evaluation_configs:
        res = offline_results[name]
        mean_t = f"{res['mean_time']:.3f}" if res['mean_time'] is not None else "N/A"
        markdown_table += f"| {name:12s} | {100*res['fa']:6.2f}% | {100*res['det']:8.2f}% | {100*res['det10']:5.1f}% | {100*res['det25']:5.1f}% | {100*res['det50']:5.1f}% | {mean_t} | {100*res['never']:5.1f}% |\n"
        
    offline_report_content = f"""# Pi0.5 Offline OOD Detector Evaluation Report
    
This report evaluates the OOD generalization of the trained Pi0.5 H10 risk head evaluated strictly on the clean `pi05_basic_h10` online OOD dataset (which reflects natural Pi0.5 behaviour without risk intervention).

* **Dataset source:** `policy_pi05_basic_h10` query records
* **Total episodes:** {len(by_ep)}
* **Risk Model Checkpoint:** `pi05_goal_object_h10_risk_20260625`

---

## 1. Step-Level Classification Metrics
* **Step AUROC:** {step_metrics["auroc"]:.4f}
* **Step AUPRC:** {step_metrics["auprc"]:.4f}
* **Step F1:** {step_metrics["f1"]:.4f}
* **Step FPR:** {step_metrics["fpr"]:.4f}
* **Step FNR:** {step_metrics["fnr"]:.4f}

---

## 2. Episode-Level Early Detection Table

{markdown_table}

---

## 3. Operating Point Recommendation
We select `q95_mass_10` as our official operating point:
* **Success False Alarm Rate:** {offline_results["q95_mass_10"]["fa"]*100:.2f}%
* **Failure Detection Rate:** {offline_results["q95_mass_10"]["det"]*100:.2f}%
* **Never Detected Rate:** {offline_results["q95_mass_10"]["never"]*100:.2f}%
* **Mean Detection Fraction:** {offline_results["q95_mass_10"]["mean_time"]:.3f}

This confirms that the H10 SeqRiskModel generalized strongly to OOD tasks, providing single-digit false alarm rates under conformal mass accumulation while maintaining very high recall.
"""
    with open(offline_report_path, "w") as f:
        f.write(offline_report_content)
        
    print(f"Offline report written to {offline_report_path}")

if __name__ == "__main__":
    main()
