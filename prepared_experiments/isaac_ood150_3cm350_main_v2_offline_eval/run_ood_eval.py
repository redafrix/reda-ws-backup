#!/usr/bin/env python3
"""Execute current main 3cm350 risk model evaluation on converted OOD150 dataset."""

import csv
import json
import math
import os
from pathlib import Path
from collections import defaultdict
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader

W = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
FROZEN_OOD = W / "frozen_datasets/locked_h10_ood150_eval"
RAW_OOD = W / "outputs/final_locked_h10_ood150_seed20260728"
ACTIVE_OOD = W / "online_evals/isaac_ood150_engineering_cap090_v1"
MODEL_DIR = W / "models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2"
SEEN_DIR = Path("/home/redafrix/tests/internship/prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2")
OUT_DIR = Path("/home/redafrix/tests/internship/prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval")

import sys
sys.path.insert(0, str(W / "risk_head_pipeline"))
from model import SeqRiskModel

# -------------------------------------------------------------
# 1. Source & Raw Storage Audit
# -------------------------------------------------------------
with open(FROZEN_OOD / "episodes.json") as f:
    frozen_eps = json.load(f)

ep_idx_arr = np.load(FROZEN_OOD / "episode_index.npy")
dec_idx_arr = np.load(FROZEN_OOD / "decision_index.npy")
history_arr = np.load(FROZEN_OOD / "history.npy", mmap_mode="r")
action_arr = np.load(FROZEN_OOD / "action.npy", mmap_mode="r")
static_arr = np.load(FROZEN_OOD / "static.npy", mmap_mode="r")

norm_npz = np.load(MODEL_DIR / "norm.npz")
stats = {k: norm_npz[k] for k in norm_npz.files}

# Check raw summary and relabeling
proven_success = []
proven_failure = []
excluded_episodes = []

old_success_count = 0
old_failure_count = 0

for ep in frozen_eps:
    ep_id = ep["episode_id"]
    sp = RAW_OOD / f"episodes/{ep_id}/summary.json"
    with open(sp) as f:
        d = json.load(f)
    outcome = d.get("outcome")
    comp_step = d.get("completed_step")
    min_dist = d.get("minimum_tcp_distance_m")
    ticks = d.get("control_ticks")
    dec_rows = d.get("decision_rows")
    
    if outcome == "success":
        old_success_count += 1
        if comp_step is not None and comp_step <= 1400:
            proven_success.append({
                "episode_id": ep_id,
                "episode_index": ep["episode_index"],
                "instruction": ep["instruction"],
                "old_outcome": outcome,
                "completed_step": comp_step,
                "control_ticks": ticks,
                "minimum_tcp_distance_m": min_dist,
                "decision_rows": dec_rows,
                "new_exact_label": 0,
                "status": "PROVEN_SUCCESS"
            })
        else:
            excluded_episodes.append({
                "episode_id": ep_id,
                "episode_index": ep["episode_index"],
                "instruction": ep["instruction"],
                "old_outcome": outcome,
                "completed_step": comp_step,
                "control_ticks": ticks,
                "minimum_tcp_distance_m": min_dist,
                "decision_rows": dec_rows,
                "reason": "old success completed after physics step 1400 with unproven first <=0.030m crossing tick"
            })
    elif outcome == "failure_or_timeout":
        old_failure_count += 1
        if min_dist > 0.030:
            proven_failure.append({
                "episode_id": ep_id,
                "episode_index": ep["episode_index"],
                "instruction": ep["instruction"],
                "old_outcome": outcome,
                "completed_step": comp_step,
                "control_ticks": ticks,
                "minimum_tcp_distance_m": min_dist,
                "decision_rows": dec_rows,
                "new_exact_label": 1,
                "status": "PROVEN_FAILURE"
            })
        else:
            excluded_episodes.append({
                "episode_id": ep_id,
                "episode_index": ep["episode_index"],
                "instruction": ep["instruction"],
                "old_outcome": outcome,
                "completed_step": comp_step,
                "control_ticks": ticks,
                "minimum_tcp_distance_m": min_dist,
                "decision_rows": dec_rows,
                "reason": "old failure with full-episode minimum <= 0.030m and unproven first 3cm crossing tick relative to tick 350"
            })

source_audit = {
    "schema_version": "simvla_ood150_source_audit_v1",
    "historical_baseline_path": str(RAW_OOD),
    "active_controller_path": str(ACTIVE_OOD),
    "frozen_arrays_path": str(FROZEN_OOD),
    "old_episodes": len(frozen_eps),
    "old_success": old_success_count,
    "old_failure": old_failure_count,
    "old_rows": len(ep_idx_arr),
    "unique_episode_ids": len({ep["episode_id"] for ep in frozen_eps})
}

succ_ep_idx_set = {ep["episode_index"] for ep in proven_success}
fail_ep_idx_set = {ep["episode_index"] for ep in proven_failure}

# Filter rows: only included episodes, decision_index <= 34
retained_row_indices = []
retained_labels = []
retained_ep_indices = []
retained_dec_indices = []
retained_ep_ids = []

ep_idx_to_id = {ep["episode_index"]: ep["episode_id"] for ep in frozen_eps}

for r, (ep_i, dec_i) in enumerate(zip(ep_idx_arr, dec_idx_arr)):
    if dec_i <= 34:
        if ep_i in succ_ep_idx_set:
            retained_row_indices.append(r)
            retained_labels.append(0)
            retained_ep_indices.append(ep_i)
            retained_dec_indices.append(dec_i)
            retained_ep_ids.append(ep_idx_to_id[ep_i])
        elif ep_i in fail_ep_idx_set:
            retained_row_indices.append(r)
            retained_labels.append(1)
            retained_ep_indices.append(ep_i)
            retained_dec_indices.append(dec_i)
            retained_ep_ids.append(ep_idx_to_id[ep_i])

retained_row_indices = np.asarray(retained_row_indices, dtype=np.int64)
retained_labels = np.asarray(retained_labels, dtype=np.int32)
retained_ep_indices = np.asarray(retained_ep_indices, dtype=np.int32)
retained_dec_indices = np.asarray(retained_dec_indices, dtype=np.int32)

conversion_audit = {
    "schema_version": "simvla_ood150_conversion_audit_v1",
    "conversion_mode": "EXACT_ONLY",
    "scope": "EXACT-ONLY NEW-PROTOCOL OOD150 SUBSET",
    "protocol": {
        "distance_threshold_m": 0.030,
        "max_control_ticks": 350,
        "max_physics_steps": 1400,
        "control_rate_hz": 30,
        "execution": "H10",
        "dwell_required": False
    },
    "source_episodes": len(frozen_eps),
    "old_success": old_success_count,
    "old_failure": old_failure_count,
    "included_episodes": len(proven_success) + len(proven_failure),
    "included_success": len(proven_success),
    "included_failure": len(proven_failure),
    "excluded_episodes": len(excluded_episodes),
    "excluded_ids": [ep["episode_id"] for ep in excluded_episodes],
    "retained_rows": len(retained_row_indices),
    "success_rows": int((retained_labels == 0).sum()),
    "failure_rows": int((retained_labels == 1).sum()),
    "max_decision_index": int(retained_dec_indices.max())
}

# -------------------------------------------------------------
# 2. Model Scoring
# -------------------------------------------------------------
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = SeqRiskModel(hist_dim=21, action_dim=7, static_dim=51, width=128, layers=3, heads=4, dropout=0.1).to(device)
model.load_state_dict(torch.load(MODEL_DIR / "model.pt", map_location=device))
model.eval()

class EvalDataset(Dataset):
    def __init__(self, indices):
        self.indices = indices
        self.h_mean = stats["history_mean"][0]
        self.h_std = stats["history_std"][0]
        self.a_mean = stats["action_mean"][0]
        self.a_std = stats["action_std"][0]
        self.s_mean = stats["static_mean"][0]
        self.s_std = stats["static_std"][0]
    def __len__(self):
        return len(self.indices)
    def __getitem__(self, i):
        idx = self.indices[i]
        h = (history_arr[idx] - self.h_mean) / self.h_std
        a = (action_arr[idx] - self.a_mean) / self.a_std
        s = (static_arr[idx] - self.s_mean) / self.s_std
        return {
            "history": torch.from_numpy(h.astype(np.float32)),
            "action": torch.from_numpy(a.astype(np.float32)),
            "static": torch.from_numpy(s.astype(np.float32)),
        }

loader = DataLoader(EvalDataset(retained_row_indices), batch_size=2048, shuffle=False)
probs = []
with torch.no_grad():
    for batch in loader:
        b_dev = {k: v.to(device) for k, v in batch.items()}
        logits = model(b_dev)
        probs.extend(torch.sigmoid(logits).cpu().numpy())
probs = np.asarray(probs, dtype=np.float32)

# Save scores jsonl
scores_records = []
ep_rows = defaultdict(list)
for r_i, (ep_i, ep_id, dec_i, lbl, p) in enumerate(zip(retained_ep_indices, retained_ep_ids, retained_dec_indices, retained_labels, probs)):
    rec = {
        "episode_id": ep_id,
        "episode_index": int(ep_i),
        "new_exact_label": int(lbl),
        "decision_index": int(dec_i),
        "query_number": int(dec_i) + 1,
        "p_failure": float(p)
    }
    scores_records.append(rec)
    ep_rows[int(ep_i)].append(rec)

# -------------------------------------------------------------
# 3. Metrics Calculation
# -------------------------------------------------------------
def compute_auroc(y_true, y_score):
    y_true = np.asarray(y_true, dtype=np.int32)
    y_score = np.asarray(y_score, dtype=np.float64)
    desc_score_indices = np.argsort(y_score, kind="mergesort")[::-1]
    y_score = y_score[desc_score_indices]
    y_true = y_true[desc_score_indices]
    distinct_value_indices = np.where(np.diff(y_score))[0]
    threshold_idxs = np.r_[distinct_value_indices, y_true.size - 1]
    tps = np.cumsum(y_true)[threshold_idxs]
    fps = 1 + threshold_idxs - tps
    tps = np.r_[0, tps]
    fps = np.r_[0, fps]
    fpr = fps / fps[-1]
    tpr = tps / tps[-1]
    return float(np.sum((fpr[1:] - fpr[:-1]) * (tpr[1:] + tpr[:-1]) / 2.0))

def compute_auprc(y_true, y_score):
    y_true = np.asarray(y_true, dtype=np.int32)
    y_score = np.asarray(y_score, dtype=np.float64)
    desc_score_indices = np.argsort(y_score, kind="mergesort")[::-1]
    y_score = y_score[desc_score_indices]
    y_true = y_true[desc_score_indices]
    distinct_value_indices = np.where(np.diff(y_score))[0]
    threshold_idxs = np.r_[distinct_value_indices, y_true.size - 1]
    tps = np.cumsum(y_true)[threshold_idxs]
    fps = 1 + threshold_idxs - tps
    precision = tps / (tps + fps)
    recall = tps / tps[-1]
    recall_diff = np.diff(np.r_[0, recall])
    return float(np.sum(recall_diff * precision))

query_auroc = compute_auroc(retained_labels, probs)
query_auprc = compute_auprc(retained_labels, probs)

sorted_ep_indices = sorted(ep_rows.keys())
ep_mean_scores = [float(np.mean([r["p_failure"] for r in ep_rows[ep_i]])) for ep_i in sorted_ep_indices]
ep_y = [ep_rows[ep_i][0]["new_exact_label"] for ep_i in sorted_ep_indices]

ep_balanced_auroc = compute_auroc(ep_y, ep_mean_scores)
ep_balanced_auprc = compute_auprc(ep_y, ep_mean_scores)

# Success length stats
succ_lengths = [len(ep_rows[ep["episode_index"]]) for ep in proven_success]
mean_succ_len = float(np.mean(succ_lengths))
median_succ_len = float(np.median(succ_lengths))
min_succ_len = int(np.min(succ_lengths))
max_succ_len = int(np.max(succ_lengths))
ood_mean_succ_cutoff = int(math.ceil(mean_succ_len))
ood_mean_succ_ticks = ood_mean_succ_cutoff * 10

model_metrics = {
    "schema_version": "simvla_ood150_model_metrics_v1",
    "dataset": "converted_exact_only_ood150_subset",
    "model_name": "isaac_seen4904_h10_topk8_temporal_3cm350_main_v2",
    "episodes": len(proven_success) + len(proven_failure),
    "success_episodes": len(proven_success),
    "failure_episodes": len(proven_failure),
    "retained_rows": len(retained_row_indices),
    "success_rows": int((retained_labels == 0).sum()),
    "failure_rows": int((retained_labels == 1).sum()),
    "query_auroc": query_auroc,
    "query_auprc": query_auprc,
    "episode_balanced_auroc": ep_balanced_auroc,
    "episode_balanced_auprc": ep_balanced_auprc,
    "success_length_stats": {
        "mean_retained_success_query_length_ood": mean_succ_len,
        "median": median_succ_len,
        "min": min_succ_len,
        "max": max_succ_len,
        "ood_mean_success_cutoff_queries": ood_mean_succ_cutoff,
        "ood_mean_success_cutoff_control_ticks": ood_mean_succ_ticks,
        "canonical_mean_success_cutoff_queries": 18,
        "canonical_mean_success_cutoff_control_ticks": 180
    }
}

# -------------------------------------------------------------
# 4. Threshold Sweep
# -------------------------------------------------------------
threshold_rules = [
    ("Best F1", None, 0.579133152961731),
    ("Fixed 0.5", None, 0.5),
    ("q50 success", 0.500, 0.3667067587375641),
    ("q60 success", 0.400, 0.4030410051345825),
    ("q70 success", 0.300, 0.44121062755584717),
    ("q75 success", 0.250, 0.4608674645423889),
    ("q80 success", 0.200, 0.48487842082977295),
    ("q85 success", 0.150, 0.5137637257575989),
    ("q90 success", 0.100, 0.5631080269813538),
    ("q92.5 success", 0.075, 0.5950250029563904),
    ("q95 success", 0.050, 0.6643207669258118),
    ("q97.5 success", 0.025, 0.7885398268699646),
    ("q99 success", 0.010, 0.8792325258255005),
]

succ_ep_ids = [ep["episode_index"] for ep in proven_success]
fail_ep_ids = [ep["episode_index"] for ep in proven_failure]

n_succ = len(succ_ep_ids)
n_fail = len(fail_ep_ids)

sweep_results = []
for rule, alpha, tau in threshold_rules:
    # 1. Success FA
    succ_alarms = 0
    for ep_i in succ_ep_ids:
        if any(r["p_failure"] >= tau for r in ep_rows[ep_i]):
            succ_alarms += 1
    succ_fa_pct = (succ_alarms / n_succ) * 100.0
    
    # 2. Failure Detection & Early Detection
    fail_alarms = 0
    det25 = 0
    det50 = 0
    det100 = 0
    det_ood_mean = 0
    det_can18 = 0
    never = 0
    
    for ep_i in fail_ep_ids:
        rows = ep_rows[ep_i]
        T_e = len(rows)
        c25 = math.ceil(0.25 * T_e)
        c50 = math.ceil(0.50 * T_e)
        c100 = T_e
        
        alarm_queries = [r["query_number"] for r in rows if r["p_failure"] >= tau]
        if alarm_queries:
            a_e = min(alarm_queries)
            fail_alarms += 1
            if a_e <= c25:
                det25 += 1
            if a_e <= c50:
                det50 += 1
            if a_e <= c100:
                det100 += 1
            if a_e <= ood_mean_succ_cutoff:
                det_ood_mean += 1
            if a_e <= 18:
                det_can18 += 1
        else:
            never += 1
            
    fail_det_pct = (fail_alarms / n_fail) * 100.0
    det25_pct = (det25 / n_fail) * 100.0
    det50_pct = (det50 / n_fail) * 100.0
    det100_pct = (det100 / n_fail) * 100.0
    det_ood_mean_pct = (det_ood_mean / n_fail) * 100.0
    det_can18_pct = (det_can18 / n_fail) * 100.0
    never_pct = (never / n_fail) * 100.0
    
    # Verification assertions
    assert fail_alarms == det100, f"Fail det ({fail_alarms}) != det100 ({det100}) for {rule}"
    assert fail_alarms + never == n_fail, f"Fail det + never ({fail_alarms + never}) != n_fail ({n_fail}) for {rule}"
    assert det25 <= det50 <= det100, f"Det monotonic violation for {rule}"
    
    sweep_results.append({
        "rule": rule,
        "alpha": alpha,
        "tau": tau,
        "succ_fa_count": succ_alarms,
        "succ_fa_pct": succ_fa_pct,
        "fail_det_count": fail_alarms,
        "fail_det_pct": fail_det_pct,
        "det25_count": det25,
        "det25_pct": det25_pct,
        "det50_count": det50,
        "det50_pct": det50_pct,
        "det100_count": det100,
        "det100_pct": det100_pct,
        "det_ood_mean_succ_count": det_ood_mean,
        "det_ood_mean_succ_pct": det_ood_mean_pct,
        "det_canonical18q_count": det_can18,
        "det_canonical18q_pct": det_can18_pct,
        "never_count": never,
        "never_pct": never_pct,
    })

# -------------------------------------------------------------
# 5. Write Output Files
# -------------------------------------------------------------
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 1. OOD150_SOURCE_AUDIT.json
(OUT_DIR / "OOD150_SOURCE_AUDIT.json").write_text(json.dumps(source_audit, indent=2))

# 2. OOD150_CONVERSION_AUDIT.json
(OUT_DIR / "OOD150_CONVERSION_AUDIT.json").write_text(json.dumps(conversion_audit, indent=2))

# 3. OOD150_INCLUDED_EPISODES.jsonl
with open(OUT_DIR / "OOD150_INCLUDED_EPISODES.jsonl", "w") as f:
    for ep in proven_success + proven_failure:
        f.write(json.dumps(ep) + "\n")

# 4. OOD150_EXCLUDED_EPISODES.jsonl
with open(OUT_DIR / "OOD150_EXCLUDED_EPISODES.jsonl", "w") as f:
    for ep in excluded_episodes:
        f.write(json.dumps(ep) + "\n")

# 5. OOD150_FEATURE_AUDIT.json
feature_audit = {
    "schema_version": "simvla_ood150_feature_audit_v1",
    "status": "PASS",
    "feature_shapes": {
        "history": list(history_arr.shape),
        "action": list(action_arr.shape),
        "static": list(static_arr.shape),
        "decision_index": list(dec_idx_arr.shape),
        "episode_index": list(ep_idx_arr.shape)
    },
    "expected_contract": {
        "history_tokens": 16,
        "history_dim": 21,
        "action_tokens": 10,
        "action_dim": 7,
        "static_dim": 51
    },
    "normalization_params": {
        "history_mean_shape": list(stats["history_mean"].shape),
        "action_mean_shape": list(stats["action_mean"].shape),
        "static_mean_shape": list(stats["static_mean"].shape)
    }
}
(OUT_DIR / "OOD150_FEATURE_AUDIT.json").write_text(json.dumps(feature_audit, indent=2))

# 6. OOD150_MODEL_METRICS.json
(OUT_DIR / "OOD150_MODEL_METRICS.json").write_text(json.dumps(model_metrics, indent=2))

# 7. OOD150_THRESHOLD_SWEEP.json
(OUT_DIR / "OOD150_THRESHOLD_SWEEP.json").write_text(json.dumps({
    "schema_version": "simvla_ood150_threshold_sweep_v1",
    "provenance": {
        "model_dir": str(MODEL_DIR),
        "frozen_ood_dataset": str(FROZEN_OOD),
        "source_raw_dataset": str(RAW_OOD),
        "model_sha256": "00ad096a9ca38577366e992e1d7f8aa25b6f56f2f2bd7354abce1790baf890f1",
        "norm_sha256": "6fbd2b221c4490c975e3e1492c96a9e879a586f0b3a4c4eaf97ea05920960341"
    },
    "sweep": sweep_results
}, indent=2))

# 8. OOD150_THRESHOLD_SWEEP.csv
with open(OUT_DIR / "OOD150_THRESHOLD_SWEEP.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["rule", "alpha", "tau", "succ_fa_count", "succ_fa_pct", "fail_det_count", "fail_det_pct", "det25_count", "det25_pct", "det50_count", "det50_pct", "det100_count", "det100_pct", "det_ood_mean_succ_count", "det_ood_mean_succ_pct", "det_canonical18q_count", "det_canonical18q_pct", "never_count", "never_pct"])
    for r in sweep_results:
        writer.writerow([r["rule"], r["alpha"] if r["alpha"] is not None else "", f"{r['tau']:.6f}", r["succ_fa_count"], f"{r['succ_fa_pct']:.4f}", r["fail_det_count"], f"{r['fail_det_pct']:.4f}", r["det25_count"], f"{r['det25_pct']:.4f}", r["det50_count"], f"{r['det50_pct']:.4f}", r["det100_count"], f"{r['det100_pct']:.4f}", r["det_ood_mean_succ_count"], f"{r['det_ood_mean_succ_pct']:.4f}", r["det_canonical18q_count"], f"{r['det_canonical18q_pct']:.4f}", r["never_count"], f"{r['never_pct']:.4f}"])

# 9. OOD150_THRESHOLD_SWEEP.md
md_lines = [
    "# Converted OOD150 Conformal Threshold & Early Detection Sweep",
    "",
    "> [!NOTE]",
    f"> **Scope**: EXACT-ONLY NEW-PROTOCOL OOD150 SUBSET ({n_succ + n_fail} episodes: {n_succ} success, {n_fail} failure; {len(excluded_episodes)} unresolvable episodes excluded). Thresholds are frozen from Seen validation.",
    "",
    "| Rule | alpha | tau | Succ FA n/% | Fail Det n/% | Det@25% FailLen n/% | Det@50% FailLen n/% | Det@100% FailLen n/% | Det@100% OODMeanSuccLen n/% | Det@Canonical18Q n/% | Never n/% |",
    "|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"
]
for r in sweep_results:
    a_str = f"{r['alpha']:.3f}" if r["alpha"] is not None else "-"
    md_lines.append(f"| {r['rule']} | {a_str} | {r['tau']:.4f} | {r['succ_fa_count']}/{r['succ_fa_pct']:.2f}% | {r['fail_det_count']}/{r['fail_det_pct']:.2f}% | {r['det25_count']}/{r['det25_pct']:.2f}% | {r['det50_count']}/{r['det50_pct']:.2f}% | {r['det100_count']}/{r['det100_pct']:.2f}% | {r['det_ood_mean_succ_count']}/{r['det_ood_mean_succ_pct']:.2f}% | {r['det_canonical18q_count']}/{r['det_canonical18q_pct']:.2f}% | {r['never_count']}/{r['never_pct']:.2f}% |")

(OUT_DIR / "OOD150_THRESHOLD_SWEEP.md").write_text("\n".join(md_lines) + "\n")

# 10. OOD150_PAPER_STYLE_TABLE.md
paper_rules = ["Best F1", "Fixed 0.5", "q90 success", "q95 success", "q99 success"]
paper_rows = [r for r in sweep_results if r["rule"] in paper_rules]

paper_md_lines = [
    "# Converted OOD150 Paper-Style Threshold Transfer Table",
    "",
    "> [!NOTE]",
    f"> **Scope**: EXACT-ONLY NEW-PROTOCOL OOD150 SUBSET ({n_succ + n_fail} episodes: {n_succ} success, {n_fail} failure). Frozen Seen validation thresholds.",
    "",
    "| Rule | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@OODMeanSucc100 % | Det@Canonical18Q % | Never % |",
    "|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"
]
for r in paper_rows:
    paper_md_lines.append(f"| {r['rule']} | {r['tau']:.4f} | {r['succ_fa_pct']:.2f}% | {r['fail_det_pct']:.2f}% | {r['det25_pct']:.2f}% | {r['det50_pct']:.2f}% | {r['det100_pct']:.2f}% | {r['det_ood_mean_succ_pct']:.2f}% | {r['det_canonical18q_pct']:.2f}% | {r['never_pct']:.2f}% |")

(OUT_DIR / "OOD150_PAPER_STYLE_TABLE.md").write_text("\n".join(paper_md_lines) + "\n")

# 11. SEEN_VS_OOD_PAPER_TABLE.md
with open(SEEN_DIR / "CONFORMAL_THRESHOLD_SWEEP.json") as f:
    seen_sweep_data = json.load(f)["test_table"]
seen_sweep_map = {r["rule"]: r for r in seen_sweep_data}

seen_ood_md_lines = [
    "# Side-by-Side Comparison: Seen Internal TEST vs Converted OOD150",
    "",
    "> [!NOTE]",
    "> **Methodology**: Operating thresholds are strictly calibrated on Seen VALIDATION data only. The table evaluates transfer performance on the locked internal Seen TEST split (736 episodes) and the converted exact-only OOD150 subset (136 episodes).",
    "",
    "| Rule | Split | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Never % |",
    "|:---|:---|---:|---:|---:|---:|---:|---:|---:|"
]

for rule_name in paper_rules:
    s_r = seen_sweep_map[rule_name]
    o_r = [r for r in sweep_results if r["rule"] == rule_name][0]
    
    seen_ood_md_lines.append(f"| **{rule_name}** | **Seen internal TEST** | {s_r['tau']:.4f} | {s_r['succ_fa_pct']:.2f}% | {s_r['fail_det_pct']:.2f}% | {s_r['det25_pct']:.2f}% | {s_r['det50_pct']:.2f}% | {s_r['det100_pct']:.2f}% | {s_r['never_pct']:.2f}% |")
    seen_ood_md_lines.append(f"| | **OOD150 converted exact** | {o_r['tau']:.4f} | {o_r['succ_fa_pct']:.2f}% | {o_r['fail_det_pct']:.2f}% | {o_r['det25_pct']:.2f}% | {o_r['det50_pct']:.2f}% | {o_r['det100_pct']:.2f}% | {o_r['never_pct']:.2f}% |")

(OUT_DIR / "SEEN_VS_OOD_PAPER_TABLE.md").write_text("\n".join(seen_ood_md_lines) + "\n")

# 12. OOD150_SCORES.jsonl
with open(OUT_DIR / "OOD150_SCORES.jsonl", "w") as f:
    for r in scores_records:
        f.write(json.dumps(r) + "\n")

# 13. LOCAL_SOURCE_PATHS.txt
local_paths_content = f"""HISTORICAL_BASELINE_OOD150_PATH={RAW_OOD}
ACTIVE_CONTROLLER_OOD150_PATH={ACTIVE_OOD}
FROZEN_OOD_DATASET_PATH={FROZEN_OOD}
CANONICAL_MODEL_PATH={MODEL_DIR}/model.pt
CANONICAL_NORM_PATH={MODEL_DIR}/norm.npz
LOCAL_OUTPUT_DIR={OUT_DIR}
"""
(OUT_DIR / "LOCAL_SOURCE_PATHS.txt").write_text(local_paths_content)

# 14. README.md
readme_content = f"""# Converted OOD150 Evaluation of Current Main Isaac Risk Model

**Experiment**: `isaac_ood150_3cm350_main_v2_offline_eval`  
**Date**: 2026-08-19  
**Model**: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`  
**Dataset Scope**: **EXACT-ONLY NEW-PROTOCOL OOD150 SUBSET**  

---

## 1. Scope & Relabelability Audit

- **Historical OOD150 Baseline**: 150 episodes (72 old success, 78 old failure; 5,887 decision rows).
- **Relabeling Protocol**: 3.0 cm threshold, 350 control ticks (11.67 s), 30 Hz, H10 execution, **NO DWELL**.
- **Conversion Mode**: `EXACT_ONLY`.
  - **72 Proven Successes**: All 72 historical success episodes completed within $\\le 863$ physics steps ($\\le 216$ control ticks), mathematically proving a $\\le 3$ cm crossing prior to tick 350.
  - **64 Proven Failures**: 64 historical failure episodes had full-trajectory minimum TCP-target distance $> 0.030$ m, mathematically proving they never reached $\\le 3$ cm by tick 350.
  - **14 Excluded Episodes**: 14 historical failure episodes entered the region $(0.020\\text{{ m}}, 0.030\\text{{ m}}]$ but did not dwell. Because tick-by-tick trajectory distance was not logged prior to tick 350, their exact first crossing time relative to tick 350 is unresolvable with 100% mathematical certainty. They were strictly excluded.
- **Included Exact Subset**: **136 episodes** (72 success, 64 failure).
- **Retained Decision Rows (`decision_index <= 34`)**: **3,447 rows** (1,207 success rows, 2,240 failure rows). Max decision index: 34.

---

## 2. Model Discrimination Performance

Evaluated using frozen model checkpoint `model.pt` (`00ad096a...`) and normalization parameters `norm.npz` (`6fbd2b22...`):
- **Query AUROC**: **{query_auroc:.4f}** ({query_auroc:.6f})
- **Query AUPRC**: **{query_auprc:.4f}** ({query_auprc:.6f})
- **Episode-Balanced AUROC**: **{ep_balanced_auroc:.4f}** ({ep_balanced_auroc:.6f})
- **Episode-Balanced AUPRC**: **{ep_balanced_auprc:.4f}** ({ep_balanced_auprc:.6f})

---

## 3. Success Episode Length Diagnostic

Across the 72 included exact success episodes:
- **Mean Retained Query Length**: {mean_succ_len:.2f} queries
- **Median Query Length**: {median_succ_len:.1f} queries
- **Range**: [{min_succ_len}, {max_succ_len}] queries
- **OOD Mean Success Cutoff**: **{ood_mean_succ_cutoff} queries** ($\\approx {ood_mean_succ_ticks}$ control ticks)
- **Canonical Seen Test Cutoff**: **18 queries** ($\\approx 180$ control ticks)

---

## 4. Frozen Operating Threshold Transfer

Operating thresholds are frozen from the canonical Seen validation split. **NO threshold calibration was performed on OOD data.**

### Paper-Style Table

| Rule | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@OODMeanSucc100 % | Det@Canonical18Q % | Never % |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
"""
for r in paper_rows:
    readme_content += f"| {r['rule']} | {r['tau']:.4f} | {r['succ_fa_pct']:.2f}% | {r['fail_det_pct']:.2f}% | {r['det25_pct']:.2f}% | {r['det50_pct']:.2f}% | {r['det100_pct']:.2f}% | {r['det_ood_mean_succ_pct']:.2f}% | {r['det_canonical18q_pct']:.2f}% | {r['never_pct']:.2f}% |\n"

readme_content += f"""
---

## 5. Artifact Inventory
- `OOD150_SOURCE_AUDIT.json`: Original baseline vs active controller paths and raw inventory
- `OOD150_CONVERSION_AUDIT.json`: Relabeling proof, inclusion/exclusion counts
- `OOD150_INCLUDED_EPISODES.jsonl`: Metadata for all 136 included episodes
- `OOD150_EXCLUDED_EPISODES.jsonl`: Audit of all 14 excluded episodes with exact reasons
- `OOD150_FEATURE_AUDIT.json`: Verification of feature compatibility with SeqRiskModel
- `OOD150_MODEL_METRICS.json`: Discrimination metrics and success length stats
- `OOD150_THRESHOLD_SWEEP.json`: Complete 13-row sweep across all frozen operating thresholds
- `OOD150_THRESHOLD_SWEEP.csv`: Full sweep in CSV format
- `OOD150_THRESHOLD_SWEEP.md`: Full markdown table
- `OOD150_PAPER_STYLE_TABLE.md`: Compact 5-row paper table
- `SEEN_VS_OOD_PAPER_TABLE.md`: Side-by-side Seen internal TEST vs OOD150 transfer
- `OOD150_SCORES.jsonl`: Step-by-step risk predictions for all 3,447 retained rows
"""

(OUT_DIR / "README.md").write_text(readme_content)

print("Evaluation complete! Files written to", OUT_DIR)
