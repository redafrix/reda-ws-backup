#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

try:
    import numpy as np
except ImportError as exc:
    raise SystemExit("numpy is required for quantiles") from exc


SUCCESS_SPLITS = ["success_val_seen", "success_test_seen", "success_test_ood"]
FAILURE_SPLITS = ["failure_val_seen", "failure_test_seen", "failure_eval_ood"]


def pct(x: float | None) -> str:
    if x is None or math.isnan(x):
        return "n/a"
    return f"{100.0 * x:.1f}%"


def load_calibration_scores(score_path: Path):
    by_split: dict[str, list[float]] = defaultdict(list)
    with score_path.open() as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            split = row.get("split")
            score = row.get("score")
            if split and score is not None:
                by_split[split].append(float(score))
    return by_split


def load_episode_summaries(score_path: Path):
    episodes = []
    current_key = None
    current_split = None
    rows: list[tuple[int, float]] = []

    def flush():
        nonlocal current_key, current_split, rows
        if current_key is None or current_split not in SUCCESS_SPLITS + FAILURE_SPLITS:
            return
        max_t = max((t for t, _ in rows), default=0)
        c25 = 0.25 * max(max_t, 1)
        c50 = 0.50 * max(max_t, 1)
        episodes.append(
            {
                "split": current_split,
                "max_all": max((s for _, s in rows), default=-float("inf")),
                "max_25": max((s for t, s in rows if t <= c25), default=-float("inf")),
                "max_50": max((s for t, s in rows if t <= c50), default=-float("inf")),
            }
        )

    with score_path.open() as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            split = row.get("split")
            key = (split, row.get("episode_key"))
            if key != current_key:
                flush()
                current_key = key
                current_split = split
                rows = []
            rows.append((int(row.get("timestep", 0)), float(row.get("score", 0.0))))
    flush()
    return episodes


def episode_metrics_from_summaries(episodes: list[dict], thresholds: dict[str, float]):
    aggregates = {
        name: {
            split: {"episodes": 0, "alarms": 0, "det25": 0, "det50": 0}
            for split in SUCCESS_SPLITS + FAILURE_SPLITS
        }
        for name in thresholds
    }
    for ep in episodes:
        split = ep["split"]
        for name, threshold in thresholds.items():
            ag = aggregates[name][split]
            ag["episodes"] += 1
            if ep["max_all"] >= threshold:
                ag["alarms"] += 1
            if ep["max_25"] >= threshold:
                ag["det25"] += 1
            if ep["max_50"] >= threshold:
                ag["det50"] += 1
    return aggregates


def rate(num: int, den: int) -> float | None:
    return None if den == 0 else num / den


def summarize_one(score_path: Path):
    by_split = load_calibration_scores(score_path)
    episodes = load_episode_summaries(score_path)
    thresholds = {}
    if by_split.get("success_calib_seen"):
        thresholds["success_only_q95"] = float(np.quantile(by_split["success_calib_seen"], 0.95))
    if by_split.get("success_calib_seen") and by_split.get("failure_val_seen"):
        thresholds["success_plus_failure_val_q95"] = float(
            np.quantile(by_split["success_calib_seen"] + by_split["failure_val_seen"], 0.95)
        )
    if by_split.get("success_calib_seen") and by_split.get("failure_train_seen"):
        thresholds["success_plus_failure_train_q95"] = float(
            np.quantile(by_split["success_calib_seen"] + by_split["failure_train_seen"], 0.95)
        )

    # A diagnostic failure-aware threshold: choose the validation threshold that maximizes
    # episode-level failure detection minus success false alarms.
    val_scores = by_split.get("success_val_seen", []) + by_split.get("failure_val_seen", [])
    if by_split.get("success_val_seen") and by_split.get("failure_val_seen") and val_scores:
        candidates = np.quantile(val_scores, np.linspace(0.05, 0.99, 95))
        best = None
        success_val = [ep for ep in episodes if ep["split"] == "success_val_seen"]
        failure_val = [ep for ep in episodes if ep["split"] == "failure_val_seen"]
        for cand in candidates:
            succ_alarm = sum(ep["max_all"] >= cand for ep in success_val)
            fail_alarm = sum(ep["max_all"] >= cand for ep in failure_val)
            util = rate(fail_alarm, len(failure_val)) or 0.0
            util -= rate(succ_alarm, len(success_val)) or 0.0
            if best is None or util > best[0]:
                best = (util, float(cand))
        if best:
            thresholds["val_youden_any"] = best[1]

    metrics = episode_metrics_from_summaries(episodes, thresholds)
    return thresholds, metrics


def render_table(rows: list[dict]) -> str:
    headers = [
        "campaign",
        "threshold",
        "thr",
        "seen_FA",
        "ood_FA",
        "seen_det",
        "ood_det",
        "ood_det25",
        "ood_det50",
    ]
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for r in rows:
        out.append(
            "| "
            + " | ".join(
                [
                    r["campaign"],
                    r["threshold"],
                    f"{r['thr']:.4f}",
                    pct(r["seen_FA"]),
                    pct(r["ood_FA"]),
                    pct(r["seen_det"]),
                    pct(r["ood_det"]),
                    pct(r["ood_det25"]),
                    pct(r["ood_det50"]),
                ]
            )
            + " |"
        )
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    score_paths = sorted(args.root.glob("*/jobs/v2_018_transformer_k16/scores.jsonl"))
    rows = []
    for score_path in score_paths:
        campaign = score_path.parents[2].name
        thresholds, metrics_by_threshold = summarize_one(score_path)
        for name, threshold in thresholds.items():
            m = metrics_by_threshold[name]
            s_seen = m["success_test_seen"]
            s_ood = m["success_test_ood"]
            f_seen = m["failure_test_seen"]
            f_ood = m["failure_eval_ood"]
            rows.append(
                {
                    "campaign": campaign,
                    "threshold": name,
                    "thr": threshold,
                    "seen_FA": rate(s_seen["alarms"], s_seen["episodes"]),
                    "ood_FA": rate(s_ood["alarms"], s_ood["episodes"]),
                    "seen_det": rate(f_seen["alarms"], f_seen["episodes"]),
                    "ood_det": rate(f_ood["alarms"], f_ood["episodes"]),
                    "ood_det25": rate(f_ood["det25"], f_ood["episodes"]),
                    "ood_det50": rate(f_ood["det50"], f_ood["episodes"]),
                }
            )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    report = []
    report.append("# Offline Failure-Calibration Probe\n")
    report.append("Model: `v2_018_transformer_k16`\n")
    report.append("Question: does adding failure episodes to the threshold calibration improve the offline detector tradeoff?\n")
    report.append("Definitions: `FA` = episode has at least one alarm on success episodes; `det` = episode has at least one alarm on failure episodes. `det25/det50` are approximate first-alarm timing metrics from logged timesteps.\n")
    report.append(render_table(rows))
    report.append("\n## Compact Verdict\n")
    for campaign in sorted({r["campaign"] for r in rows}):
        cr = [r for r in rows if r["campaign"] == campaign]
        base = next((r for r in cr if r["threshold"] == "success_only_q95"), None)
        if not base:
            continue
        report.append(f"### {campaign}\n")
        report.append(f"- Baseline success-only q95: seen FA {pct(base['seen_FA'])}, OOD FA {pct(base['ood_FA'])}, seen det {pct(base['seen_det'])}, OOD det {pct(base['ood_det'])}, OOD det@25 {pct(base['ood_det25'])}.\n")
        for r in cr:
            if r["threshold"] == "success_only_q95":
                continue
            report.append(
                f"- {r['threshold']}: threshold {r['thr']:.4f}; "
                f"seen FA {pct(r['seen_FA'])}, OOD FA {pct(r['ood_FA'])}, "
                f"seen det {pct(r['seen_det'])}, OOD det {pct(r['ood_det'])}, OOD det@25 {pct(r['ood_det25'])}.\n"
            )
    args.out.write_text("\n".join(report))
    print(args.out)


if __name__ == "__main__":
    main()
