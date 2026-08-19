#!/usr/bin/env python3
"""Offline Risk Model Evaluation on Frozen OOD400 Baseline Dataset.

Applies frozen Seen-derived operating points, verifies score parity,
computes AUROC/AUPRC and early-detection metrics (Det@25, Det@50, Det@100, Det@MeanSucc100, Never).
"""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
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

from ood400_runtime import load_stats, make_seq_risk_model, normalize, sha256_file

FROZEN_SEEN_OPERATING_POINTS = {
    "Best F1": 0.579133152961731,
    "Fixed 0.5": 0.500000000000000,
    "q50 success": 0.3667067587375641,
    "q60 success": 0.4030410051345825,
    "q70 success": 0.44121062755584717,
    "q75 success": 0.4608674645423889,
    "q80 success": 0.48487842082977295,
    "q85 success": 0.5137637257575989,
    "q90 success": 0.5631080269813538,
    "q92.5 success": 0.5950250029563904,
    "q95 success": 0.6643207669258118,
    "q97.5 success": 0.7885398268699646,
    "q99 success": 0.8792325258255005,
}

PRIMARY_PAPER_ROWS = [
    "Best F1",
    "Fixed 0.5",
    "q90 success",
    "q95 success",
    "q99 success",
]


def compute_binary_metrics(labels: np.ndarray, scores: np.ndarray) -> tuple[float, float]:
    from sklearn.metrics import roc_auc_score, average_precision_score
    auroc = float(roc_auc_score(labels, scores))
    auprc = float(average_precision_score(labels, scores))
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

    # Load frozen arrays
    history = np.load(frozen_dir / "history.npy")
    action = np.load(frozen_dir / "action.npy")
    static = np.load(frozen_dir / "static.npy")
    labels = np.load(frozen_dir / "labels.npy")
    ep_indices = np.load(frozen_dir / "episode_index.npy")
    dec_indices = np.load(frozen_dir / "decision_index.npy")

    episodes = [json.loads(line) for line in (frozen_dir / "episodes.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    decisions = [json.loads(line) for line in (frozen_dir / "decisions.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]

    total_episodes = len(episodes)
    success_episodes = [s for s in episodes if s["success"]]
    failure_episodes = [s for s in episodes if not s["success"]]
    num_success = len(success_episodes)
    num_failure = len(failure_episodes)

    # Success episode query lengths
    succ_lengths = [int(s["decision_rows"]) for s in success_episodes]
    mean_succ_len = float(np.mean(succ_lengths))
    median_succ_len = float(np.median(succ_lengths))
    min_succ_len = int(np.min(succ_lengths))
    max_succ_len = int(np.max(succ_lengths))
    mean_succ_cutoff = int(math.ceil(mean_succ_len))

    # Model inference
    device = torch.device(device_str if torch.cuda.is_available() else "cpu")
    stats = load_stats(norm_path)
    h_norm, a_norm, s_norm = normalize(history, action, static, stats)

    model = make_seq_risk_model().to(device)
    state = torch.load(model_path, map_location=device, weights_only=True)
    model.load_state_dict(state)
    model.eval()

    batch_size = 256
    N = len(labels)
    scores = np.zeros(N, dtype=np.float32)

    with torch.no_grad():
        for i in range(0, N, batch_size):
            end_idx = min(i + batch_size, N)
            h_t = torch.as_tensor(h_norm[i:end_idx], device=device)
            a_t = torch.as_tensor(a_norm[i:end_idx], device=device)
            s_t = torch.as_tensor(s_norm[i:end_idx], device=device)
            out = model(h_t, a_t, s_t).view(-1)
            scores[i:end_idx] = out.detach().cpu().numpy()

    # Verify score parity with shadow online scores
    shadow_c0_scores = np.array([float(d["online_risk"]["main_score"]) for d in decisions], dtype=np.float32)
    score_diffs = np.abs(scores - shadow_c0_scores)
    max_score_diff = float(np.max(score_diffs))
    mean_score_diff = float(np.mean(score_diffs))

    if max_score_diff > 1e-4:
        raise RuntimeError(f"Offline score discrepancy too high: max_diff={max_score_diff}")

    # Query metrics
    query_auroc, query_auprc = compute_binary_metrics(labels, scores)

    # Episode metrics (max query risk per episode)
    ep_scores = {}
    ep_labels = {}
    ep_query_scores = {}

    for ep_id_int, dec_idx, score, label in zip(ep_indices, dec_indices, scores, labels):
        ep_id_str = f"{ep_id_int:06d}"
        ep_scores[ep_id_str] = max(ep_scores.get(ep_id_str, -1.0), float(score))
        ep_labels[ep_id_str] = int(label)
        ep_query_scores.setdefault(ep_id_str, []).append((int(dec_idx), float(score)))

    ep_score_arr = np.array([ep_scores[f"{i:06d}"] for i in range(total_episodes)], dtype=np.float32)
    ep_label_arr = np.array([ep_labels[f"{i:06d}"] for i in range(total_episodes)], dtype=np.int64)

    ep_auroc, ep_auprc = compute_binary_metrics(ep_label_arr, ep_score_arr)

    # Threshold sweep
    sweep_results: list[dict[str, Any]] = []

    for rule_name, tau in FROZEN_SEEN_OPERATING_POINTS.items():
        # Evaluate on successes
        succ_alarms = 0
        for s in success_episodes:
            ep_id = s["episode_id"]
            q_scores = ep_query_scores[ep_id]
            if any(score >= tau for _, score in q_scores):
                succ_alarms += 1

        succ_fa_rate = succ_alarms / num_success if num_success > 0 else 0.0

        # Evaluate on failures
        fail_det = 0
        det25 = 0
        det50 = 0
        det100 = 0
        det_mean_succ = 0
        never = 0

        for f in failure_episodes:
            ep_id = f["episode_id"]
            q_scores = ep_query_scores[ep_id]
            T_e = len(q_scores)
            c25 = int(math.ceil(0.25 * T_e))
            c50 = int(math.ceil(0.50 * T_e))
            c100 = T_e

            alarm_indices = [idx + 1 for idx, (_, score) in enumerate(q_scores) if score >= tau]
            if alarm_indices:
                t_first = min(alarm_indices)
                fail_det += 1
                if t_first <= c25:
                    det25 += 1
                if t_first <= c50:
                    det50 += 1
                if t_first <= c100:
                    det100 += 1
                if t_first <= mean_succ_cutoff:
                    det_mean_succ += 1
            else:
                never += 1

        # Strict Invariants
        if det100 != fail_det:
            raise RuntimeError(f"Invariant violation: det100 ({det100}) != fail_det ({fail_det})")
        if fail_det + never != num_failure:
            raise RuntimeError(f"Invariant violation: fail_det ({fail_det}) + never ({never}) != num_failure ({num_failure})")
        if not (det25 <= det50 <= det100):
            raise RuntimeError(f"Invariant violation: monotonic early detection failed ({det25} <= {det50} <= {det100})")

        fail_det_rate = fail_det / num_failure if num_failure > 0 else 0.0
        det25_rate = det25 / num_failure if num_failure > 0 else 0.0
        det50_rate = det50 / num_failure if num_failure > 0 else 0.0
        det100_rate = det100 / num_failure if num_failure > 0 else 0.0
        det_mean_succ_rate = det_mean_succ / num_failure if num_failure > 0 else 0.0
        never_rate = never / num_failure if num_failure > 0 else 0.0

        sweep_results.append({
            "rule_name": rule_name,
            "threshold": float(tau),
            "succ_false_alarm_count": succ_alarms,
            "succ_false_alarm_rate": succ_fa_rate,
            "succ_false_alarm_pct": succ_fa_rate * 100.0,
            "fail_detection_count": fail_det,
            "fail_detection_rate": fail_det_rate,
            "fail_detection_pct": fail_det_rate * 100.0,
            "det_at_25_count": det25,
            "det_at_25_pct": det25_rate * 100.0,
            "det_at_50_count": det50,
            "det_at_50_pct": det50_rate * 100.0,
            "det_at_100_count": det100,
            "det_at_100_pct": det100_rate * 100.0,
            "det_at_mean_succ_100_count": det_mean_succ,
            "det_at_mean_succ_100_pct": det_mean_succ_rate * 100.0,
            "never_count": never,
            "never_pct": never_rate * 100.0,
        })

    # Save outputs
    metrics_summary = {
        "schema_version": "ood400_model_metrics_v1",
        "benchmark_episodes_total": total_episodes,
        "success_episodes": num_success,
        "failure_episodes": num_failure,
        "decision_queries_total": N,
        "query_metrics": {
            "auroc": query_auroc,
            "auprc": query_auprc,
        },
        "episode_balanced_metrics": {
            "auroc": ep_auroc,
            "auprc": ep_auprc,
        },
        "score_parity": {
            "max_abs_diff": max_score_diff,
            "mean_abs_diff": mean_score_diff,
            "status": "PASS",
        },
        "success_query_length": {
            "mean": mean_succ_len,
            "median": median_succ_len,
            "min": min_succ_len,
            "max": max_succ_len,
            "mean_cutoff_ceil": mean_succ_cutoff,
        },
        "created_timestamp": datetime.now(timezone.utc).isoformat(),
    }
    (output_dir / "OOD400_MODEL_METRICS.json").write_text(json.dumps(metrics_summary, indent=2) + "\n")
    (output_dir / "OOD400_EXACT_SUCCESS_LENGTH.json").write_text(json.dumps(metrics_summary["success_query_length"], indent=2) + "\n")
    (output_dir / "OFFLINE_SCORE_PARITY.json").write_text(json.dumps(metrics_summary["score_parity"], indent=2) + "\n")
    (output_dir / "OOD400_THRESHOLD_SWEEP.json").write_text(json.dumps(sweep_results, indent=2) + "\n")

    # CSV output
    with (output_dir / "OOD400_THRESHOLD_SWEEP.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(sweep_results[0].keys()))
        writer.writeheader()
        writer.writerows(sweep_results)

    # Full Markdown sweep table
    sweep_md_lines = [
        "# OOD400 Offline Conformal & Operating Point Threshold Sweep",
        "",
        "| Rule | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@MeanSucc100 % | Never % |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for row in sweep_results:
        sweep_md_lines.append(
            f"| {row['rule_name']} | {row['threshold']:.4f} | {row['succ_false_alarm_pct']:.2f}% | "
            f"{row['fail_detection_pct']:.2f}% | {row['det_at_25_pct']:.2f}% | {row['det_at_50_pct']:.2f}% | "
            f"{row['det_at_100_pct']:.2f}% | {row['det_at_mean_succ_100_pct']:.2f}% | {row['never_pct']:.2f}% |"
        )
    (output_dir / "OOD400_THRESHOLD_SWEEP.md").write_text("\n".join(sweep_md_lines) + "\n")

    # Paper Style Table (Primary 5 rows)
    paper_rows = [r for r in sweep_results if r["rule_name"] in PRIMARY_PAPER_ROWS]
    paper_md_lines = [
        "# OOD400 Paper Style Monitor Operating Points Table",
        "",
        "| Rule | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@MeanSucc100 % | Never % |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for row in paper_rows:
        paper_md_lines.append(
            f"| {row['rule_name']} | {row['threshold']:.4f} | {row['succ_false_alarm_pct']:.2f}% | "
            f"{row['fail_detection_pct']:.2f}% | {row['det_at_25_pct']:.2f}% | {row['det_at_50_pct']:.2f}% | "
            f"{row['det_at_100_pct']:.2f}% | {row['det_at_mean_succ_100_pct']:.2f}% | {row['never_pct']:.2f}% |"
        )
    (output_dir / "OOD400_PAPER_STYLE_TABLE.md").write_text("\n".join(paper_md_lines) + "\n")

    # SHA256 sums
    sha_lines = []
    for f in sorted(output_dir.iterdir()):
        if f.is_file() and f.name != "SHA256SUMS.txt":
            sha_lines.append(f"{sha256_file(f)}  {f.name}")
    (output_dir / "SHA256SUMS.txt").write_text("\n".join(sha_lines) + "\n")

    print(f"=== Offline Evaluation COMPLETE: Query AUROC={query_auroc:.4f}, Episode AUROC={ep_auroc:.4f} ===")
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
