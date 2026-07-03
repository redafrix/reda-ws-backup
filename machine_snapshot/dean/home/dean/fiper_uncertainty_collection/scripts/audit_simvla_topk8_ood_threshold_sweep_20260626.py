#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np


DATASET_ROOT = Path("/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622")
PREV_EVAL_ROOT = Path("/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626")
OUT_ROOT = Path("/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_audited_threshold_sweep")
OFFICIAL_FIPER_CSV = Path("/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625/official_fiper_ablation_results.csv")


def read_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def load_episode_summaries(path: Path) -> dict[str, dict]:
    out = {}
    for row in read_jsonl(path):
        eid = str(row.get("episode_id") or row.get("episode_uid"))
        if not eid:
            raise RuntimeError(f"summary row has no episode id: {row.keys()}")
        out[eid] = row
    return out


def load_minimal_rows(rows_path: Path, summaries: dict[str, dict]) -> list[dict]:
    rows = []
    missing = 0
    for row in read_jsonl(rows_path):
        eid = str(row.get("episode_id") or row.get("episode_uid"))
        if eid not in summaries:
            missing += 1
            continue
        summary = summaries[eid]
        rows.append(
            {
                "episode_id": eid,
                "task_id": int(row.get("task_id", summary.get("task_id", -1))),
                "timestep": int(row.get("timestep", 0)),
                "y": 0 if bool(summary.get("success")) else 1,
                "success": bool(summary.get("success")),
                "summary_steps": int(summary.get("steps", summary.get("num_steps", 0)) or 0),
            }
        )
    if missing:
        print(f"[warn] skipped {missing} rows missing from episode summaries")
    return rows


def group_by_episode(rows: list[dict], scores: np.ndarray) -> dict[str, list[tuple[dict, float]]]:
    by_ep = defaultdict(list)
    for r, s in zip(rows, scores):
        by_ep[r["episode_id"]].append((r, float(s)))
    for vals in by_ep.values():
        vals.sort(key=lambda x: x[0]["timestep"])
    return dict(by_ep)


def metric_from_hits(by_ep: dict[str, list[tuple[dict, float]]], hit_fn):
    succ = fail = fa = det = det10 = det25 = det50 = 0
    det_query_fracs = []
    det_time_fracs = []
    per_task = defaultdict(Counter)
    for _eid, vals in by_ep.items():
        y = max(v[0]["y"] for v in vals)
        task = vals[0][0]["task_id"]
        n = len(vals)
        first_idx, first_timestep = hit_fn(vals)
        last_timestep = max(1, vals[-1][0]["timestep"])
        if y:
            fail += 1
            per_task[task]["failure"] += 1
            if first_idx is not None:
                det += 1
                per_task[task]["detected_failure"] += 1
                qfrac = (first_idx + 1) / max(1, n)
                tfrac = first_timestep / last_timestep
                det_query_fracs.append(qfrac)
                det_time_fracs.append(tfrac)
                if qfrac <= 0.10:
                    det10 += 1
                if qfrac <= 0.25:
                    det25 += 1
                if qfrac <= 0.50:
                    det50 += 1
        else:
            succ += 1
            per_task[task]["success"] += 1
            if first_idx is not None:
                fa += 1
                per_task[task]["false_alarm"] += 1

    return {
        "episodes": succ + fail,
        "success_episodes": succ,
        "failure_episodes": fail,
        "success_fa": fa / max(1, succ),
        "failure_det": det / max(1, fail),
        "det_at_10": det10 / max(1, fail),
        "det_at_25": det25 / max(1, fail),
        "det_at_50": det50 / max(1, fail),
        "mean_query_time": float(np.mean(det_query_fracs)) if det_query_fracs else None,
        "mean_timestep_time": float(np.mean(det_time_fracs)) if det_time_fracs else None,
        "never": 1.0 - det / max(1, fail),
        "false_alarm_count": fa,
        "detected_failure_count": det,
        "per_task": {
            str(k): {
                "success_episodes": int(c["success"]),
                "failure_episodes": int(c["failure"]),
                "false_alarm_count": int(c["false_alarm"]),
                "detected_failure_count": int(c["detected_failure"]),
                "success_fa": c["false_alarm"] / max(1, c["success"]),
                "failure_det": c["detected_failure"] / max(1, c["failure"]),
            }
            for k, c in sorted(per_task.items())
        },
    }


def any_row_metric(by_ep, threshold: float):
    def hit_fn(vals):
        for i, (r, s) in enumerate(vals):
            if s >= threshold:
                return i, r["timestep"]
        return None, None

    return metric_from_hits(by_ep, hit_fn)


def mass_metric(by_ep, row_threshold: float, mass_threshold: float):
    final_masses = []

    def hit_fn(vals):
        mass = 0.0
        first = (None, None)
        for i, (r, s) in enumerate(vals):
            mass += max(0.0, s - row_threshold)
            if first[0] is None and mass >= mass_threshold:
                first = (i, r["timestep"])
        final_masses.append(mass)
        return first

    out = metric_from_hits(by_ep, hit_fn)
    out["mean_final_mass"] = float(np.mean(final_masses)) if final_masses else None
    out["row_threshold"] = row_threshold
    out["mass_threshold"] = mass_threshold
    return out


def fmt_pct(x: float) -> str:
    return f"{100*x:.2f}%"


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    rows_path = DATASET_ROOT / "fiper_receding_samples.jsonl"
    summaries_path = DATASET_ROOT / "episode_summaries.jsonl"
    scores_path = PREV_EVAL_ROOT / "scores.npz"
    prev_results_path = PREV_EVAL_ROOT / "results.json"

    summaries = load_episode_summaries(summaries_path)
    rows = load_minimal_rows(rows_path, summaries)
    z = np.load(scores_path)
    scores = z["scores"].astype(np.float64)
    y_saved = z["y"].astype(np.int32)
    y_rows = np.asarray([r["y"] for r in rows], dtype=np.int32)
    if len(rows) != len(scores):
        raise RuntimeError(f"row/score length mismatch: rows={len(rows)} scores={len(scores)}")
    if not np.array_equal(y_saved, y_rows):
        raise RuntimeError("saved y labels do not match dataset summary labels in row order")

    prev = json.loads(prev_results_path.read_text())
    thresholds = prev["thresholds"]
    q95 = float(thresholds["q95"])
    q99 = float(thresholds["q99"])
    conformal_mass = float(thresholds["conformal_mass"])
    by_ep = group_by_episode(rows, scores)

    ep_labels = {eid: max(v[0]["y"] for v in vals) for eid, vals in by_ep.items()}
    task_counts = defaultdict(Counter)
    for eid, vals in by_ep.items():
        task_counts[vals[0][0]["task_id"]]["failure" if ep_labels[eid] else "success"] += 1

    policies = []
    for name, th in [
        ("any_row_fixed_0.3_online_gate", 0.3),
        ("any_row_fixed_0.5", 0.5),
        ("any_row_q95", q95),
        ("any_row_q99", q99),
    ]:
        m = any_row_metric(by_ep, th)
        policies.append((name, "any_row", th, m))

    mass_thresholds = [0.05, 0.1, conformal_mass, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 7.5, 10.0, 15.0, 20.0, 30.0, 50.0, 75.0, 100.0]
    for mt in mass_thresholds:
        policies.append((f"q95_mass_{mt:g}", "q95_mass", mt, mass_metric(by_ep, q95, mt)))
    for mt in [0.05, 0.1, conformal_mass, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 7.5, 10.0]:
        policies.append((f"q99_mass_{mt:g}", "q99_mass", mt, mass_metric(by_ep, q99, mt)))

    csv_path = OUT_ROOT / "audited_policy_metrics.csv"
    with csv_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Policy", "Kind", "Threshold", "Success_FA", "Failure_Det", "Det@10", "Det@25", "Det@50", "Mean_Query_Time", "Mean_Timestep_Time", "Never", "False_Alarms", "Detected_Failures"])
        for name, kind, th, m in policies:
            w.writerow([
                name,
                kind,
                th,
                m["success_fa"],
                m["failure_det"],
                m["det_at_10"],
                m["det_at_25"],
                m["det_at_50"],
                m["mean_query_time"],
                m["mean_timestep_time"],
                m["never"],
                m["false_alarm_count"],
                m["detected_failure_count"],
            ])

    summary = {
        "dataset_root": str(DATASET_ROOT),
        "rows_path": str(rows_path),
        "summaries_path": str(summaries_path),
        "scores_path": str(scores_path),
        "previous_results_path": str(prev_results_path),
        "official_fiper_csv": str(OFFICIAL_FIPER_CSV),
        "n_rows": len(rows),
        "n_scores": len(scores),
        "n_episodes": len(by_ep),
        "n_success_episodes": sum(1 for v in ep_labels.values() if not v),
        "n_failure_episodes": sum(1 for v in ep_labels.values() if v),
        "task_counts": {str(k): dict(v) for k, v in sorted(task_counts.items())},
        "saved_thresholds": thresholds,
        "q95": q95,
        "q99": q99,
        "conformal_mass": conformal_mass,
        "label_order_check": "PASS",
    }
    (OUT_ROOT / "audit_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")

    # Pick a small set of readable policies: saved online policy plus best tradeoff rows.
    def tradeoff_score(item):
        _name, _kind, _th, m = item
        return (m["failure_det"] - m["success_fa"], m["failure_det"], -m["success_fa"])

    best_overall = max(policies, key=tradeoff_score)
    best_under_50_fa = max([p for p in policies if p[3]["success_fa"] <= 0.50], key=tradeoff_score, default=None)
    best_under_25_fa = max([p for p in policies if p[3]["success_fa"] <= 0.25], key=tradeoff_score, default=None)
    best_under_10_fa = max([p for p in policies if p[3]["success_fa"] <= 0.10], key=tradeoff_score, default=None)

    report = []
    report.append("# Audited TopK8 Threshold Sweep on LIBERO Goal-Object OOD")
    report.append("")
    report.append("This audit does not retrain or recalibrate. It loads the saved row-level scores from the prior TopK8 evaluation and recomputes episode metrics on the OOD dataset only.")
    report.append("")
    report.append("## Dataset Checks")
    report.append("")
    report.append(f"- Dataset: `{DATASET_ROOT}`")
    report.append(f"- Rows: `{len(rows)}`")
    report.append(f"- Episodes: `{len(by_ep)}`")
    report.append(f"- Success episodes: `{summary['n_success_episodes']}`")
    report.append(f"- Failure episodes: `{summary['n_failure_episodes']}`")
    report.append("- Label-order check against `scores.npz`: `PASS`")
    report.append("")
    report.append("## Selected Policies")
    report.append("")
    report.append("| Policy | Threshold | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Query Time | Mean Timestep Time | Never |")
    report.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    selected_names = {"q95_mass_0.15", "q95_mass_0.2", "q95_mass_0.5", "q95_mass_1", "q95_mass_2", "q95_mass_5", "q95_mass_10", "q95_mass_20", "q99_mass_0.15", "q99_mass_0.5", "q99_mass_1"}
    selected_items = [p for p in policies if p[0] in selected_names or p[0].startswith("any_row_")]
    for name, _kind, th, m in selected_items:
        report.append(
            f"| {name} | {th:g} | {fmt_pct(m['success_fa'])} | {fmt_pct(m['failure_det'])} | {fmt_pct(m['det_at_10'])} | {fmt_pct(m['det_at_25'])} | {fmt_pct(m['det_at_50'])} | "
            f"{m['mean_query_time'] if m['mean_query_time'] is not None else 'NA':.3f} | {m['mean_timestep_time'] if m['mean_timestep_time'] is not None else 'NA':.3f} | {fmt_pct(m['never'])} |"
        )
    report.append("")
    report.append("## Best Tradeoff Candidates")
    report.append("")
    report.append("| Constraint | Policy | Threshold | Success FA | Failure Det | Det@25 | Det@50 | Mean Query Time | Never |")
    report.append("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for label, item in [("best_overall_det_minus_fa", best_overall), ("best_FA_le_50", best_under_50_fa), ("best_FA_le_25", best_under_25_fa), ("best_FA_le_10", best_under_10_fa)]:
        if item is None:
            continue
        name, _kind, th, m = item
        report.append(
            f"| {label} | {name} | {th:g} | {fmt_pct(m['success_fa'])} | {fmt_pct(m['failure_det'])} | {fmt_pct(m['det_at_25'])} | {fmt_pct(m['det_at_50'])} | "
            f"{m['mean_query_time'] if m['mean_query_time'] is not None else 'NA':.3f} | {fmt_pct(m['never'])} |"
        )
    report.append("")
    report.append("## Official FIPER Result on Same OOD Dataset")
    report.append("")
    if OFFICIAL_FIPER_CSV.exists():
        report.append("```csv")
        report.append(OFFICIAL_FIPER_CSV.read_text().strip())
        report.append("```")
    else:
        report.append(f"Missing official FIPER CSV: `{OFFICIAL_FIPER_CSV}`")
    report.append("")
    report.append("## Interpretation")
    report.append("")
    report.append("- The saved online selected-cap threshold `q95_mass_0.15` is not a good offline operating point on this OOD set: it detects all failures, but with very high false alarms.")
    report.append("- The official FIPER no-retrain ablation is worse as an OOD safety detector because every reported variant false-alarms on every successful OOD episode.")
    report.append("- For a paper table, use the sweep rows rather than only the saved online threshold, and clearly state that the OOD set was used only for test-time threshold comparison, not for training.")
    report.append("")
    (OUT_ROOT / "AUDITED_TOPK8_AND_OFFICIAL_FIPER_OOD_REPORT_20260626.md").write_text("\n".join(report) + "\n")

    print(f"Wrote {csv_path}")
    print(f"Wrote {OUT_ROOT / 'AUDITED_TOPK8_AND_OFFICIAL_FIPER_OOD_REPORT_20260626.md'}")
    print("Dataset:", summary)
    print("Selected policy rows:")
    for name, _kind, th, m in selected_items:
        print(name, th, fmt_pct(m["success_fa"]), fmt_pct(m["failure_det"]), fmt_pct(m["det_at_25"]), fmt_pct(m["det_at_50"]), m["mean_query_time"], fmt_pct(m["never"]))


if __name__ == "__main__":
    main()
