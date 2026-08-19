import json
import math
import sys
from pathlib import Path
from collections import defaultdict
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import precision_recall_curve

W = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
DATA = W / "frozen_datasets/isaac_seen4904_h10_3cm350_exact_v1"
MODEL_DIR = W / "models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2"

sys.path.insert(0, str(W / "risk_head_pipeline"))
from model import SeqRiskModel

episodes_meta = json.loads((DATA / "episodes.json").read_text())["episodes"]
split_manifest = json.loads((MODEL_DIR / "split_manifest.json").read_text())["episodes"]

ep_split_map = {ep["final_episode_id"]: ep["split"] for ep in split_manifest}
history_arr = np.load(DATA / "history.npy", mmap_mode="r")
action_arr = np.load(DATA / "action.npy", mmap_mode="r")
static_arr = np.load(DATA / "static.npy", mmap_mode="r")
episode_idx_arr = np.load(DATA / "episode_index.npy", mmap_mode="r")
decision_idx_arr = np.load(DATA / "decision_index.npy", mmap_mode="r")
label_arr = np.load(DATA / "label.npy", mmap_mode="r")

norm_npz = np.load(MODEL_DIR / "norm.npz")
stats = {k: norm_npz[k] for k in norm_npz.files}

val_row_indices = [r for r, ep_i in enumerate(episode_idx_arr) if ep_split_map[episodes_meta[ep_i]["final_episode_id"]] == "validation"]
test_row_indices = [r for r, ep_i in enumerate(episode_idx_arr) if ep_split_map[episodes_meta[ep_i]["final_episode_id"]] == "test"]

val_row_indices = np.asarray(val_row_indices, dtype=np.int64)
test_row_indices = np.asarray(test_row_indices, dtype=np.int64)

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

def compute_probabilities(indices):
    ds = EvalDataset(indices)
    loader = DataLoader(ds, batch_size=2048, shuffle=False, num_workers=4, pin_memory=True)
    probs = []
    with torch.no_grad():
        for batch in loader:
            b_dev = {k: v.to(device) for k, v in batch.items()}
            logits = model(b_dev)
            p = torch.sigmoid(logits).cpu().numpy()
            probs.extend(p)
    return np.asarray(probs, dtype=np.float32)

print("Scoring validation split...")
val_probs = compute_probabilities(val_row_indices)
print("Scoring test split...")
test_probs = compute_probabilities(test_row_indices)

# CALIBRATION SCORES ON VALIDATION
val_ep_scores = defaultdict(list)
for r_idx, p in zip(val_row_indices, val_probs):
    ep_idx = int(episode_idx_arr[r_idx])
    ep_id = episodes_meta[ep_idx]["final_episode_id"]
    dec_idx = int(decision_idx_arr[r_idx])
    lbl = int(label_arr[r_idx])
    val_ep_scores[ep_id].append((dec_idx, p, lbl))

val_success_max_scores = []
for ep_id, rows in val_ep_scores.items():
    lbl = rows[0][2]
    max_p = max(r[1] for r in rows)
    if lbl == 0:
        val_success_max_scores.append(max_p)

assert len(val_success_max_scores) == 658, f"Expected 658 val success eps, got {len(val_success_max_scores)}"

sorted_cal_scores = np.sort(np.asarray(val_success_max_scores, dtype=np.float64))
n_cal = len(sorted_cal_scores)

alpha_list = [
    ("q50 success", 0.50),
    ("q60 success", 0.40),
    ("q70 success", 0.30),
    ("q75 success", 0.25),
    ("q80 success", 0.20),
    ("q85 success", 0.15),
    ("q90 success", 0.10),
    ("q92.5 success", 0.075),
    ("q95 success", 0.05),
    ("q97.5 success", 0.025),
    ("q99 success", 0.01),
]

conformal_th = {}
for name, alpha in alpha_list:
    k = math.ceil((n_cal + 1) * (1.0 - alpha))
    k_clipped = max(1, min(n_cal, k))
    tau = float(sorted_cal_scores[k_clipped - 1])
    conformal_th[name] = {
        "alpha": alpha,
        "coverage": 1.0 - alpha,
        "n": n_cal,
        "k": k_clipped,
        "tau": tau
    }

# Best Val F1
val_labels = label_arr[val_row_indices].astype(int)
prec, rec, ths = precision_recall_curve(val_labels, val_probs)
f1s = 2 * prec * rec / np.maximum(prec + rec, 1e-9)
best_f1_idx = int(np.nanargmax(f1s[:len(ths)])) if len(ths) > 0 else 0
best_val_f1_th = float(ths[best_f1_idx])

all_rules = [
    ("Best F1", None, best_val_f1_th),
    ("Fixed 0.5", None, 0.5),
]
for name, alpha in alpha_list:
    all_rules.append((name, alpha, conformal_th[name]["tau"]))

# TEST EVALUATION
test_ep_rows = defaultdict(list)
for r_idx, p in zip(test_row_indices, test_probs):
    ep_idx = int(episode_idx_arr[r_idx])
    ep_id = episodes_meta[ep_idx]["final_episode_id"]
    dec_idx = int(decision_idx_arr[r_idx])
    q_num = dec_idx + 1
    lbl = int(label_arr[r_idx])
    test_ep_rows[ep_id].append((q_num, p, lbl))

test_success_lengths = [len(rows) for ep_id, rows in test_ep_rows.items() if rows[0][2] == 0]
test_failure_lengths = [len(rows) for ep_id, rows in test_ep_rows.items() if rows[0][2] == 1]

n_test_succ = len(test_success_lengths)
n_test_fail = len(test_failure_lengths)

assert n_test_succ == 658
assert n_test_fail == 78

mean_succ_len = float(np.mean(test_success_lengths))
median_succ_len = float(np.median(test_success_lengths))
min_succ_len = int(np.min(test_success_lengths))
max_succ_len = int(np.max(test_success_lengths))
mean_succ_cutoff = math.ceil(mean_succ_len)

print(f"Test Success Retained Query Lengths: mean={mean_succ_len:.4f}, median={median_succ_len}, min={min_succ_len}, max={max_succ_len}")
print(f"Mean Success Cutoff (queries): {mean_succ_cutoff} (approx {mean_succ_cutoff * 10} control ticks)")

def evaluate_table(ep_rows_dict, n_succ, n_fail, cutoff_mean_succ):
    rows_out = []
    for rule_name, alpha, tau in all_rules:
        succ_fa = 0
        fail_det = 0
        det25 = 0
        det50 = 0
        det100 = 0
        det_mean_succ = 0
        never = 0
        
        first_alarm_queries = []
        first_alarm_fractions = []
        
        for ep_id, rows in ep_rows_dict.items():
            lbl = rows[0][2]
            T_e = len(rows)
            alarm_queries = [r[0] for r in rows if r[1] >= tau]
            a_e = min(alarm_queries) if alarm_queries else None
            
            if lbl == 0:
                if a_e is not None:
                    succ_fa += 1
            else:
                if a_e is not None:
                    fail_det += 1
                    first_alarm_queries.append(a_e)
                    first_alarm_fractions.append(a_e / T_e)
                    
                    c25 = math.ceil(0.25 * T_e)
                    c50 = math.ceil(0.50 * T_e)
                    c100 = T_e
                    
                    if a_e <= c25:
                        det25 += 1
                    if a_e <= c50:
                        det50 += 1
                    if a_e <= c100:
                        det100 += 1
                    if a_e <= cutoff_mean_succ:
                        det_mean_succ += 1
                else:
                    never += 1
                    
        assert fail_det == det100, f"FailDet {fail_det} != Det100 {det100}"
        assert fail_det + never == n_fail, f"FailDet + Never {fail_det + never} != {n_fail}"
        
        rows_out.append({
            "rule": rule_name,
            "alpha": alpha,
            "tau": float(tau),
            "succ_fa_count": succ_fa,
            "succ_fa_pct": (succ_fa / n_succ) * 100.0,
            "fail_det_count": fail_det,
            "fail_det_pct": (fail_det / n_fail) * 100.0,
            "det25_count": det25,
            "det25_pct": (det25 / n_fail) * 100.0,
            "det50_count": det50,
            "det50_pct": (det50 / n_fail) * 100.0,
            "det100_count": det100,
            "det100_pct": (det100 / n_fail) * 100.0,
            "det_mean_succ_count": det_mean_succ,
            "det_mean_succ_pct": (det_mean_succ / n_fail) * 100.0,
            "never_count": never,
            "never_pct": (never / n_fail) * 100.0,
            "median_first_alarm_query": float(np.median(first_alarm_queries)) if first_alarm_queries else None,
            "mean_first_alarm_query": float(np.mean(first_alarm_queries)) if first_alarm_queries else None,
            "median_first_alarm_fraction": float(np.median(first_alarm_fractions)) if first_alarm_fractions else None,
            "mean_first_alarm_fraction": float(np.mean(first_alarm_fractions)) if first_alarm_fractions else None,
        })
    return rows_out

test_table = evaluate_table(test_ep_rows, n_test_succ, n_test_fail, mean_succ_cutoff)

# Validation table
val_success_lengths = [len(rows) for ep_id, rows in val_ep_scores.items() if rows[0][2] == 0]
val_table = evaluate_table(val_ep_scores, len(val_success_lengths), 77, math.ceil(np.mean(val_success_lengths)))

output_json = {
    "schema_version": "simvla_isaac_seen4904_conformal_sweep_v1",
    "calibration": {
        "successful_val_episodes": n_cal,
        "calibration_unit": "SUCCESS_EPISODE_MAXIMUM_RISK",
        "mean_retained_success_query_length_test": mean_succ_len,
        "median_retained_success_query_length_test": median_succ_len,
        "min_retained_success_query_length_test": min_succ_len,
        "max_retained_success_query_length_test": max_succ_len,
        "mean_success_cutoff_queries": mean_succ_cutoff,
        "mean_success_cutoff_control_ticks": mean_succ_cutoff * 10
    },
    "conformal_thresholds": conformal_th,
    "test_table": test_table,
    "validation_table": val_table
}

(MODEL_DIR / "CONFORMAL_THRESHOLD_SWEEP.json").write_text(json.dumps(output_json, indent=2))
print("SAVED CONFORMAL_THRESHOLD_SWEEP.json")

# Write CSV
csv_lines = [
    "Rule,alpha,tau,Succ FA n,Succ FA %,Fail Det n,Fail Det %,Det@25% FailLen n,Det@25% FailLen %,Det@50% FailLen n,Det@50% FailLen %,Det@100% FailLen n,Det@100% FailLen %,Det@100% MeanSuccLen n,Det@100% MeanSuccLen %,Never n,Never %"
]
for r in test_table:
    alpha_str = f"{r['alpha']:.3f}" if r["alpha"] is not None else ""
    csv_lines.append(
        f"{r['rule']},{alpha_str},{r['tau']:.6f},{r['succ_fa_count']},{r['succ_fa_pct']:.2f},{r['fail_det_count']},{r['fail_det_pct']:.2f},{r['det25_count']},{r['det25_pct']:.2f},{r['det50_count']},{r['det50_pct']:.2f},{r['det100_count']},{r['det100_pct']:.2f},{r['det_mean_succ_count']},{r['det_mean_succ_pct']:.2f},{r['never_count']},{r['never_pct']:.2f}"
    )

(MODEL_DIR / "CONFORMAL_THRESHOLD_SWEEP.csv").write_text("\n".join(csv_lines) + "\n")
print("SAVED CONFORMAL_THRESHOLD_SWEEP.csv")

# Print formatted tables
print("\n=== FULL TEST TABLE ===")
md_full = [
    "| Rule | alpha | tau | Succ FA n/% | Fail Det n/% | Det@25% FailLen n/% | Det@50% FailLen n/% | Det@100% FailLen n/% | Det@100% MeanSuccLen n/% | Never n/% |",
    "|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"
]
for r in test_table:
    alpha_str = f"{r['alpha']:.3f}" if r["alpha"] is not None else "-"
    md_full.append(
        f"| {r['rule']} | {alpha_str} | {r['tau']:.4f} | {r['succ_fa_count']}/{r['succ_fa_pct']:.2f}% | {r['fail_det_count']}/{r['fail_det_pct']:.2f}% | {r['det25_count']}/{r['det25_pct']:.2f}% | {r['det50_count']}/{r['det50_pct']:.2f}% | {r['det100_count']}/{r['det100_pct']:.2f}% | {r['det_mean_succ_count']}/{r['det_mean_succ_pct']:.2f}% | {r['never_count']}/{r['never_pct']:.2f}% |"
    )
print("\n".join(md_full))

print("\n=== COMPACT PAPER-STYLE TABLE ===")
compact_rules = {"Best F1", "Fixed 0.5", "q90 success", "q95 success", "q99 success"}
md_compact = [
    "| Rule | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@MeanSucc100 % | Never % |",
    "|:---|---:|---:|---:|---:|---:|---:|---:|---:|"
]
for r in test_table:
    if r["rule"] in compact_rules:
        md_compact.append(
            f"| {r['rule']} | {r['tau']:.4f} | {r['succ_fa_pct']:.2f}% | {r['fail_det_pct']:.2f}% | {r['det25_pct']:.2f}% | {r['det50_pct']:.2f}% | {r['det100_pct']:.2f}% | {r['det_mean_succ_pct']:.2f}% | {r['never_pct']:.2f}% |"
        )
print("\n".join(md_compact))

(MODEL_DIR / "CONFORMAL_THRESHOLD_SWEEP.md").write_text("# Conformal Threshold & Early-Detection Sweep\n\n## Full Test Table\n\n" + "\n".join(md_full) + "\n\n## Compact Paper-Style Table\n\n" + "\n".join(md_compact) + "\n")
print("SAVED CONFORMAL_THRESHOLD_SWEEP.md")
