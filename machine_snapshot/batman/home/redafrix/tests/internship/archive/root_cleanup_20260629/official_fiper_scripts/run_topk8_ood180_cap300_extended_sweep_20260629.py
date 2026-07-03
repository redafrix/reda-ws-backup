#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np


DATASET_ROOT = Path("/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622")
PREV_EVAL_ROOT = Path("/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626")
OUT_ROOT = Path("/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_cap300_extended_sweep_20260629")


def read_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def fmt_pct(x: float) -> str:
    return f"{100.0 * x:.1f}%"


def episode_id(row: dict) -> str:
    eid = row.get("episode_id") or row.get("episode_uid")
    if not eid:
        raise RuntimeError(f"row missing episode id: {row.keys()}")
    return str(eid)


def load_summaries(path: Path) -> dict[str, dict]:
    out = {}
    for row in read_jsonl(path):
        out[episode_id(row)] = row
    return out


def load_cap300_rows(rows_path: Path, summaries: dict[str, dict], scores: np.ndarray):
    rows = []
    kept_scores = []
    dropped = 0
    for idx, row in enumerate(read_jsonl(rows_path)):
        eid = episode_id(row)
        summary = summaries[eid]
        timestep = int(row.get("timestep", 0))
        if timestep >= 300:
            dropped += 1
            continue
        orig_success = bool(summary.get("success"))
        steps = int(summary.get("num_steps", summary.get("steps", 10**9)) or 10**9)
        cap_success = orig_success and steps < 300
        rows.append(
            {
                "episode_id": eid,
                "task_id": int(row.get("task_id", summary.get("task_id", -1))),
                "timestep": timestep,
                "y": 0 if cap_success else 1,
                "success": cap_success,
                "source_success": orig_success,
                "source_steps": steps,
            }
        )
        kept_scores.append(float(scores[idx]))
    return rows, np.asarray(kept_scores, dtype=np.float64), dropped


def group_by_episode(rows: list[dict], scores: np.ndarray) -> dict[str, list[tuple[dict, float]]]:
    by_ep = defaultdict(list)
    for row, score in zip(rows, scores):
        by_ep[row["episode_id"]].append((row, float(score)))
    for vals in by_ep.values():
        vals.sort(key=lambda x: x[0]["timestep"])
    return dict(by_ep)


def metric_from_hit_fn(by_ep, hit_fn):
    succ = fail = fa = det = det10 = det25 = det50 = 0
    det_fracs = []
    per_task = defaultdict(Counter)
    for eid, vals in by_ep.items():
        y = max(v[0]["y"] for v in vals)
        task = vals[0][0]["task_id"]
        first_idx = hit_fn(vals)
        n = max(1, len(vals))
        if y:
            fail += 1
            per_task[task]["fail"] += 1
            if first_idx is not None:
                det += 1
                per_task[task]["det"] += 1
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
            per_task[task]["succ"] += 1
            if first_idx is not None:
                fa += 1
                per_task[task]["fa"] += 1
    return {
        "success_episodes": succ,
        "failure_episodes": fail,
        "false_alarm_count": fa,
        "detected_failure_count": det,
        "success_fa": fa / max(1, succ),
        "failure_det": det / max(1, fail),
        "det_at_10": det10 / max(1, fail),
        "det_at_25": det25 / max(1, fail),
        "det_at_50": det50 / max(1, fail),
        "mean_time": float(np.mean(det_fracs)) if det_fracs else None,
        "never": 1.0 - det / max(1, fail),
        "per_task": {str(k): dict(v) for k, v in sorted(per_task.items())},
    }


def any_metric(by_ep, threshold: float):
    return metric_from_hit_fn(
        by_ep,
        lambda vals: next((i for i, (_row, score) in enumerate(vals) if score >= threshold), None),
    )


def k_metric(by_ep, threshold: float, k: int):
    def hit(vals):
        run = 0
        for i, (_row, score) in enumerate(vals):
            if score >= threshold:
                run += 1
                if run >= k:
                    return i - k + 1
            else:
                run = 0
        return None

    return metric_from_hit_fn(by_ep, hit)


def mass_metric(by_ep, row_threshold: float, mass_threshold: float):
    def hit(vals):
        mass = 0.0
        for i, (_row, score) in enumerate(vals):
            mass += max(0.0, score - row_threshold)
            if mass >= mass_threshold:
                return i
        return None

    return metric_from_hit_fn(by_ep, hit)


def useful_score(m: dict) -> float:
    # Balanced paper-search score: prefer detection, penalize false alarms and late alarms.
    mean_time = m["mean_time"] if m["mean_time"] is not None else 1.0
    return (m["failure_det"] - m["success_fa"]) + 0.25 * m["det_at_50"] + 0.15 * m["det_at_25"] - 0.10 * mean_time


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    summaries = load_summaries(DATASET_ROOT / "episode_summaries.jsonl")
    scores_file = PREV_EVAL_ROOT / "scores.npz"
    results_file = PREV_EVAL_ROOT / "results.json"
    z = np.load(scores_file)
    full_scores = z["scores"].astype(np.float64)
    rows, scores, dropped = load_cap300_rows(DATASET_ROOT / "fiper_receding_samples.jsonl", summaries, full_scores)
    by_ep = group_by_episode(rows, scores)
    results = json.loads(results_file.read_text())
    thresholds = results["thresholds"]
    q95 = float(thresholds["q95"])
    q99 = float(thresholds["q99"])
    saved_mass = float(thresholds.get("conformal_mass", 0.15))

    ep_labels = {eid: max(v[0]["y"] for v in vals) for eid, vals in by_ep.items()}
    counts = Counter("failure" if y else "success" for y in ep_labels.values())
    converted = 0
    for eid, vals in by_ep.items():
        if vals[0][0]["source_success"] and ep_labels[eid]:
            converted += 1

    policies = []
    for th in [0.1, 0.2, 0.3, 0.4, 0.5, q95, 0.7, 0.8, 0.9, q99]:
        policies.append((f"any_row_{th:.4g}", "any", th, any_metric(by_ep, th)))
    for row_name, row_th in [("q95", q95), ("q99", q99), ("fixed_0.3", 0.3), ("fixed_0.5", 0.5), ("fixed_0.7", 0.7)]:
        for k in [2, 3, 5, 8, 10, 15, 20]:
            policies.append((f"{row_name}_K{k}", "k", k, k_metric(by_ep, row_th, k)))
    mass_grid = [0.02, 0.05, 0.1, saved_mass, 0.2, 0.3, 0.5, 0.75, 1, 1.25, 1.5, 2, 3, 5, 7.5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200]
    for row_name, row_th in [("q95", q95), ("q99", q99), ("fixed_0.3", 0.3), ("fixed_0.5", 0.5)]:
        for mass in mass_grid:
            policies.append((f"{row_name}_mass_{mass:g}", "mass", mass, mass_metric(by_ep, row_th, mass)))

    csv_path = OUT_ROOT / "topk8_ood180_cap300_extended_sweep.csv"
    with csv_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Policy", "Kind", "Param", "Success_FA", "Failure_Det", "Det@10", "Det@25", "Det@50", "Mean_Time", "Never", "False_Alarms", "Detected_Failures"])
        for name, kind, param, m in policies:
            w.writerow([
                name, kind, param, m["success_fa"], m["failure_det"], m["det_at_10"],
                m["det_at_25"], m["det_at_50"], m["mean_time"], m["never"],
                m["false_alarm_count"], m["detected_failure_count"],
            ])

    selected_names = {
        "q95_mass_0.15", "q95_mass_1", "q95_mass_5", "q95_mass_10", "q95_mass_20",
        "q95_mass_30", "q95_mass_40", "q95_mass_50", "q99_mass_0.5", "q99_mass_1",
        "q99_mass_2", "q99_mass_5", "q99_mass_10", "q95_K3", "q99_K3",
    }
    selected = [p for p in policies if p[0] in selected_names]
    constraints = [
        ("best_overall", lambda m: True),
        ("best_FA_le_50", lambda m: m["success_fa"] <= 0.50),
        ("best_FA_le_35", lambda m: m["success_fa"] <= 0.35),
        ("best_FA_le_25", lambda m: m["success_fa"] <= 0.25),
        ("best_FA_le_15", lambda m: m["success_fa"] <= 0.15),
        ("best_FA_le_10", lambda m: m["success_fa"] <= 0.10),
        ("best_FA_le_5", lambda m: m["success_fa"] <= 0.05),
    ]
    best_rows = []
    for label, pred in constraints:
        candidates = [p for p in policies if pred(p[3])]
        if candidates:
            best_rows.append((label, max(candidates, key=lambda p: useful_score(p[3]))))

    report = []
    report.append("# H10 TopK8 OOD180 Cap-300 Extended Threshold Sweep")
    report.append("")
    report.append("No retrain. No OOD recalibration of the model. This sweep reuses the saved H10 TopK8 row scores and evaluates many episode-level alarm policies under the cap-300 label rule.")
    report.append("")
    report.append("## Dataset")
    report.append("")
    report.append(f"- Source dataset: `{DATASET_ROOT}`")
    report.append("- Cap rule: keep only rows with `timestep < 300`; success only if the original rollout succeeded before step 300; otherwise failure.")
    report.append(f"- Episodes: `{len(by_ep)}`")
    report.append(f"- Cap-300 successes: `{counts['success']}`")
    report.append(f"- Cap-300 failures: `{counts['failure']}`")
    report.append(f"- Original successful episodes converted to cap-300 failures: `{converted}`")
    report.append(f"- Kept rows: `{len(rows)}`")
    report.append(f"- Dropped rows: `{dropped}`")
    report.append(f"- Saved row thresholds: q95=`{q95:.6f}`, q99=`{q99:.6f}`, saved mass=`{saved_mass:.6f}`")
    report.append("")
    report.append("## Selected Policies")
    report.append("")
    report.append("| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |")
    report.append("| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for name, _kind, _param, m in selected:
        report.append(f"| `{name}` | {fmt_pct(m['success_fa'])} | {fmt_pct(m['failure_det'])} | {fmt_pct(m['det_at_10'])} | {fmt_pct(m['det_at_25'])} | {fmt_pct(m['det_at_50'])} | {m['mean_time'] if m['mean_time'] is not None else 0:.3f} | {fmt_pct(m['never'])} |")
    report.append("")
    report.append("## Best Candidates by False-Alarm Constraint")
    report.append("")
    report.append("| Constraint | Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |")
    report.append("| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for label, (name, _kind, _param, m) in best_rows:
        report.append(f"| {label} | `{name}` | {fmt_pct(m['success_fa'])} | {fmt_pct(m['failure_det'])} | {fmt_pct(m['det_at_10'])} | {fmt_pct(m['det_at_25'])} | {fmt_pct(m['det_at_50'])} | {m['mean_time'] if m['mean_time'] is not None else 0:.3f} | {fmt_pct(m['never'])} |")
    report.append("")
    report.append("## Interpretation")
    report.append("")
    report.append("The cap-300 rule is stricter than the full-length 800-step audit. It rewards alarms that happen early enough to matter before a 300-step timeout and penalizes policies that detect only after the useful intervention window.")
    report.append("")
    report.append(f"Full CSV: `{csv_path}`")
    report_path = OUT_ROOT / "TOPK8_OOD180_CAP300_EXTENDED_SWEEP_20260629.md"
    report_path.write_text("\n".join(report) + "\n")

    summary = {
        "dataset_root": str(DATASET_ROOT),
        "scores_file": str(scores_file),
        "results_file": str(results_file),
        "out_root": str(OUT_ROOT),
        "episodes": len(by_ep),
        "cap300_successes": counts["success"],
        "cap300_failures": counts["failure"],
        "converted_success_to_failure": converted,
        "kept_rows": len(rows),
        "dropped_rows": dropped,
        "q95": q95,
        "q99": q99,
        "saved_mass": saved_mass,
        "best_rows": [
            {"constraint": label, "policy": name, "metrics": m}
            for label, (name, _kind, _param, m) in best_rows
        ],
    }
    (OUT_ROOT / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(report_path)
    print(csv_path)
    print(json.dumps(summary["best_rows"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
