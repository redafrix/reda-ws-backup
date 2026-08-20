#!/usr/bin/env python3
"""Offline Risk Model Evaluation on Frozen OOD400 Baseline Dataset.

Performs:
1. Exact row-key join score parity audit between offline forward pass and shadow online scores.
2. Standard binary classification metrics (AUROC, AUPRC) using pure numpy.
3. Predeclared Seen operating points early detection and conformal tables.
4. Export to CSV, JSON, and Markdown tables.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import sys
from typing import Any

import numpy as np
import torch

WORKSPACE = Path(os.environ.get("SIMVLA_ISAAC_H10_WORKSPACE", "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813"))
sys.path.insert(0, str(WORKSPACE / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ood400_runtime import make_seq_risk_model, sha256_file


def compute_binary_metrics(y_true: np.ndarray, y_scores: np.ndarray) -> tuple[float, float]:
    """Compute AUROC and AUPRC in pure numpy without requiring scikit-learn."""
    y_true = np.asarray(y_true, dtype=np.int32)
    y_scores = np.asarray(y_scores, dtype=np.float64)

    n_pos = int(np.sum(y_true == 1))
    n_neg = int(np.sum(y_true == 0))

    if n_pos == 0 or n_neg == 0:
        return 0.5, 0.0

    # Sort descending
    desc_indices = np.argsort(-y_scores, kind="mergesort")
    y_sorted = y_true[desc_indices]
    scores_sorted = y_scores[desc_indices]

    # AUROC via trapezoidal integration of ROC
    # Distinct threshold indices
    distinct_indices = np.where(np.diff(scores_sorted))[0]
    threshold_idxs = np.r_[distinct_indices, y_sorted.size - 1]

    tps = np.cumsum(y_sorted)[threshold_idxs]
    fps = (1 + threshold_idxs) - tps

    tpr = np.r_[0, tps / n_pos]
    fpr = np.r_[0, fps / n_neg]

    # np.trapz(tpr, fpr)
    auroc = float(np.sum((fpr[1:] - fpr[:-1]) * (tpr[1:] + tpr[:-1]) / 2.0))

    # AUPRC via standard average precision formula sum((R_k - R_{k-1}) * P_k)
    cum_tp = np.cumsum(y_sorted)
    cum_total = np.arange(1, len(y_sorted) + 1)
    precision = cum_tp / cum_total
    
    # We only sum precision at positive recall steps
    pos_mask = (y_sorted == 1)
    if np.any(pos_mask):
        auprc = float(np.sum(precision[pos_mask]) / n_pos)
    else:
        auprc = 0.0

    return auroc, auprc


def run_offline_evaluation(
    *,
    frozen_dir: Path,
    model_path: Path,
    norm_path: Path,
    output_dir: Path,
    device_str: str = "cuda:0",
) -> dict[str, Any]:
    frozen_dir = Path(frozen_dir).resolve()
    model_path = Path(model_path).resolve()
    norm_path = Path(norm_path).resolve()
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"=== Running Offline OOD400 Evaluation in {output_dir} ===")

    # 1. Load frozen arrays
    history = np.load(frozen_dir / "history.npy")
    action = np.load(frozen_dir / "action.npy")
    static = np.load(frozen_dir / "static.npy")
    labels = np.load(frozen_dir / "labels.npy")
    episode_indices = np.load(frozen_dir / "episode_index.npy")
    decision_indices = np.load(frozen_dir / "decision_index.npy")
    shadow_scores = np.load(frozen_dir / "candidate_scores.npy")[:, 0]

    N = len(labels)
    print(f"Loaded {N} decision rows from {frozen_dir}")

    from ood400_runtime import load_stats, normalize
    stats = load_stats(norm_path)
    h_norm, a_norm, s_norm = normalize(history, action, static, stats)

    # Load model
    device = torch.device(device_str if torch.cuda.is_available() and "cuda" in device_str else "cpu")
    model = make_seq_risk_model().to(device)
    state = torch.load(model_path, map_location="cpu", weights_only=True)
    if "model_state_dict" in state:
        model.load_state_dict(state["model_state_dict"])
    else:
        model.load_state_dict(state)
    model.eval()

    # 2. Run batch inference
    batch_size = 256
    offline_probs_list = []

    with torch.inference_mode():
        for start_idx in range(0, N, batch_size):
            end_idx = min(start_idx + batch_size, N)
            h_b = torch.from_numpy(h_norm[start_idx:end_idx]).to(device)
            a_b = torch.from_numpy(a_norm[start_idx:end_idx]).to(device)
            s_b = torch.from_numpy(s_norm[start_idx:end_idx]).to(device)

            logits = model({"history": h_b, "action": a_b, "static": s_b}).view(-1)
            probs = torch.sigmoid(logits)
            offline_probs_list.append(probs.cpu().numpy())

    offline_probs = np.concatenate(offline_probs_list, axis=0)

    # 3. Exact Row-Key Join Parity Check
    row_diffs = np.abs(offline_probs - shadow_scores)
    max_diff = float(np.max(row_diffs))
    mean_diff = float(np.mean(row_diffs))
    p50_diff = float(np.percentile(row_diffs, 50))
    p95_diff = float(np.percentile(row_diffs, 95))
    p99_diff = float(np.percentile(row_diffs, 99))

    parity_doc = {
        "schema_version": "ood400_score_parity_v1",
        "total_queries_compared": N,
        "max_absolute_difference": max_diff,
        "mean_absolute_difference": mean_diff,
        "p50_difference": p50_diff,
        "p95_difference": p95_diff,
        "p99_difference": p99_diff,
        "tolerance_threshold": 1e-5,
        "status": "PASS" if max_diff <= 1e-5 else "FAIL",
        "created_timestamp": datetime.now(timezone.utc).isoformat(),
    }
    (output_dir / "OFFLINE_SCORE_PARITY.json").write_text(json.dumps(parity_doc, indent=2) + "\n")

    if max_diff > 1e-5:
        raise RuntimeError(f"Offline score parity check failed! Max diff {max_diff:.6e} > 1e-5")

    # 4. Standard Metrics (Query Level)
    query_auroc, query_auprc = compute_binary_metrics(labels, offline_probs)

    # Episode-Balanced Metrics
    unique_episodes = np.unique(episode_indices)
    ep_probs = []
    ep_labels = []
    for ep_id in unique_episodes:
        mask = (episode_indices == ep_id)
        ep_probs.append(float(np.mean(offline_probs[mask])))
        ep_labels.append(int(labels[mask][0]))
    ep_auroc, ep_auprc = compute_binary_metrics(np.array(ep_labels), np.array(ep_probs))

    # 5. Predeclared Operating Points Evaluation
    # Structure per-episode timeline: (t, score, label)
    episode_timelines: dict[int, list[tuple[int, float, int]]] = {}
    for i in range(N):
        ep_id = int(episode_indices[i])
        dec_idx = int(decision_indices[i])
        if ep_id not in episode_timelines:
            episode_timelines[ep_id] = []
        episode_timelines[ep_id].append((dec_idx + 1, float(offline_probs[i]), int(labels[i])))

    success_episodes = [ep_id for ep_id, tl in episode_timelines.items() if tl[0][2] == 0]
    failure_episodes = [ep_id for ep_id, tl in episode_timelines.items() if tl[0][2] == 1]

    # Predeclared Seen candidate points
    predeclared_points = [
        ("Best F1", 0.579133),
        ("Fixed 0.5", 0.500000),
        ("q90 success", 0.563108),
        ("q95 success", 0.664321),
        ("q99 success", 0.879233),
    ]

    sweep_results = []

    # Mean success length in baseline:
    mean_succ_ticks = np.mean([len(episode_timelines[ep_id]) for ep_id in success_episodes])

    for rule_name, tau in predeclared_points:
        # False alarm on successes:
        succ_fa_count = 0
        for ep_id in success_episodes:
            tl = episode_timelines[ep_id]
            if any(s >= tau for _, s, _ in tl):
                succ_fa_count += 1
        succ_fa_rate = succ_fa_count / len(success_episodes) if success_episodes else 0.0

        # Failure detections:
        fail_det_count = 0
        det25_count = 0
        det50_count = 0
        det100_count = 0
        det_mean_succ_count = 0
        never_count = 0

        for ep_id in failure_episodes:
            tl = episode_timelines[ep_id]
            T_e = len(tl)
            c25 = int(math.ceil(0.25 * T_e))
            c50 = int(math.ceil(0.50 * T_e))
            c100 = T_e
            c_mean_succ = int(math.ceil(mean_succ_ticks))

            alarms = [t for t, s, _ in tl if s >= tau]
            if alarms:
                t_first = min(alarms)
                fail_det_count += 1
                if t_first <= c25:
                    det25_count += 1
                if t_first <= c50:
                    det50_count += 1
                if t_first <= c100:
                    det100_count += 1
                if t_first <= c_mean_succ:
                    det_mean_succ_count += 1
            else:
                never_count += 1

        n_fail = len(failure_episodes)
        fail_det_rate = fail_det_count / n_fail if n_fail > 0 else 0.0

        sweep_results.append({
            "rule_name": rule_name,
            "threshold": tau,
            "succ_false_alarm_count": succ_fa_count,
            "succ_false_alarm_rate": succ_fa_rate,
            "succ_false_alarm_pct": succ_fa_rate * 100.0,
            "fail_detection_count": fail_det_count,
            "fail_detection_rate": fail_det_rate,
            "fail_detection_pct": fail_det_rate * 100.0,
            "det_at_25_pct": (det25_count / n_fail * 100.0) if n_fail > 0 else 0.0,
            "det_at_50_pct": (det50_count / n_fail * 100.0) if n_fail > 0 else 0.0,
            "det_at_100_pct": (det100_count / n_fail * 100.0) if n_fail > 0 else 0.0,
            "det_at_mean_succ_100_pct": (det_mean_succ_count / n_fail * 100.0) if n_fail > 0 else 0.0,
            "never_pct": (never_count / n_fail * 100.0) if n_fail > 0 else 0.0,
        })

    # Save Tables
    (output_dir / "OOD400_THRESHOLD_SWEEP.json").write_text(json.dumps(sweep_results, indent=2) + "\n")

    # CSV
    csv_lines = ["rule_name,threshold,succ_false_alarm_pct,fail_detection_pct,det_at_25_pct,det_at_50_pct,det_at_100_pct,det_at_mean_succ_100_pct,never_pct"]
    for r in sweep_results:
        csv_lines.append(f"{r['rule_name']},{r['threshold']:.6f},{r['succ_false_alarm_pct']:.2f},{r['fail_detection_pct']:.2f},{r['det_at_25_pct']:.2f},{r['det_at_50_pct']:.2f},{r['det_at_100_pct']:.2f},{r['det_at_mean_succ_100_pct']:.2f},{r['never_pct']:.2f}")
    (output_dir / "OOD400_THRESHOLD_SWEEP.csv").write_text("\n".join(csv_lines) + "\n")

    # Markdown Table
    md_lines = [
        "# Transfer evaluation of frozen Seen-derived operating points on OOD400",
        "",
        "| Operating Point | Threshold (tau) | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@MeanSucc100 % | Never % |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in sweep_results:
        md_lines.append(f"| {r['rule_name']} | {r['threshold']:.4f} | {r['succ_false_alarm_pct']:.2f}% | {r['fail_detection_pct']:.2f}% | {r['det_at_25_pct']:.2f}% | {r['det_at_50_pct']:.2f}% | {r['det_at_100_pct']:.2f}% | {r['det_at_mean_succ_100_pct']:.2f}% | {r['never_pct']:.2f}% |")
    (output_dir / "OOD400_THRESHOLD_SWEEP.md").write_text("\n".join(md_lines) + "\n")
    (output_dir / "OOD400_PAPER_STYLE_TABLE.md").write_text("\n".join(md_lines) + "\n")

    metrics_summary = {
        "schema_version": "ood400_offline_model_metrics_v1",
        "total_episodes": len(unique_episodes),
        "total_decision_rows": N,
        "query_metrics": {
            "auroc": float(query_auroc),
            "auprc": float(query_auprc),
        },
        "episode_balanced_metrics": {
            "auroc": float(ep_auroc),
            "auprc": float(ep_auprc),
        },
        "operating_points": sweep_results,
        "created_timestamp": datetime.now(timezone.utc).isoformat(),
    }
    (output_dir / "OOD400_MODEL_METRICS.json").write_text(json.dumps(metrics_summary, indent=2) + "\n")

    print(f"=== Offline Risk Model Evaluation COMPLETE: Query AUROC={query_auroc:.4f}, Episode AUROC={ep_auroc:.4f} ===")
    return metrics_summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frozen-dir", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--norm", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--device", type=str, default="cuda:0")
    args = parser.parse_args()

    run_offline_evaluation(
        frozen_dir=args.frozen_dir,
        model_path=args.model,
        norm_path=args.norm,
        output_dir=args.output_dir,
        device_str=args.device,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
