#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import torch

import run_dean_uncertainty_transformer_exploration_v2 as v2


CANONICAL_SPLITS = {
    "all_tasks_full": {
        "trained_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_all_tasks_full_uncertainty_test_20260601",
        "source_split": "all_tasks_random",
        "topk_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/all_tasks_full/unc_topk8",
        "topk_rank_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/all_tasks_full",
        "eval_success": "success_test_seen",
        "eval_failure": "failure_test_seen",
    },
    "ood_last2_taskids_full": {
        "trained_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_ood_last2_taskids_full_v1_20260601",
        "source_split": "ood_last2_taskids_full",
        "topk_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/ood_last2_taskids_full/unc_topk8",
        "topk_rank_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/ood_last2_taskids_full",
        "eval_success": "success_test_ood",
        "eval_failure": "failure_eval_ood",
    },
}


ORIGINAL_MAKE_ARRAYS = v2.make_arrays
SELECTED_DIMS_BY_VARIANT: dict[str, np.ndarray] = {}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, default=str) + "\n")


def np_stats(obj: dict[str, dict[str, list[float]]]) -> dict[str, dict[str, np.ndarray]]:
    return {k: {kk: np.asarray(vv, dtype=np.float32) for kk, vv in val.items()} for k, val in obj.items()}


def make_arrays_selected(rows: list[v2.RowEx], variant: str):
    if not variant.startswith("unc_topk"):
        return ORIGINAL_MAKE_ARRAYS(rows, variant)
    dims = SELECTED_DIMS_BY_VARIANT[variant]
    h = np.stack([r.history for r in rows], axis=0).astype(np.float32)
    a = np.stack([r.action for r in rows], axis=0).astype(np.float32)
    st = np.stack(
        [np.concatenate([r.static_base, r.uncertainty[dims]]).astype(np.float32) for r in rows],
        axis=0,
    )
    y = np.asarray([r.y for r in rows], dtype=np.float32)
    episode_ids = [r.episode_id for r in rows]
    timesteps = np.asarray([r.timestep for r in rows], dtype=np.int32)
    return h, a, st, y, episode_ids, timesteps


v2.make_arrays = make_arrays_selected


def load_seq_model(job_dir: Path, cfg: dict[str, Any], device: torch.device) -> tuple[torch.nn.Module, dict[str, dict[str, np.ndarray]]]:
    stats = np_stats(load_json(job_dir / "normalization.json"))
    model = v2.SeqRiskModel(
        hist_dim=int(stats["history"]["mean"].shape[0]),
        action_dim=int(stats["action"]["mean"].shape[0]),
        static_dim=int(stats["static"]["mean"].shape[0]),
        width=int(cfg["width"]),
        layers=int(cfg["layers"]),
        heads=int(cfg["heads"]),
        dropout=float(cfg["dropout"]),
    ).to(device)
    model.load_state_dict(torch.load(job_dir / "model.pt", map_location=device))
    model.eval()
    return model, stats


def sigmoid(x: np.ndarray) -> np.ndarray:
    return (1.0 / (1.0 + np.exp(-x))).astype(np.float32)


def logit(x: np.ndarray) -> np.ndarray:
    x = np.clip(x.astype(np.float32), 1e-5, 1.0 - 1e-5)
    return np.log(x / (1.0 - x)).astype(np.float32)


def pct(v: Any) -> str:
    if v is None:
        return ""
    return f"{100.0 * float(v):.2f}%"


def fnum(v: Any, digits: int = 4) -> str:
    if v is None:
        return ""
    return f"{float(v):.{digits}f}"


def select_topk_dims(rank_dir: Path, topk: int) -> list[int]:
    metrics_path = rank_dir / f"unc_topk{topk}" / "metrics.json"
    if metrics_path.exists():
        metrics = load_json(metrics_path)
        dims = metrics.get("feature_selection", {}).get("selected_dims")
        if dims:
            return [int(d) for d in dims]
    ranking = load_json(rank_dir / "uncertainty_dim_ranking.json")
    return [int(r["dim"]) for r in ranking[:topk]]


def row_ratios(ids: list[str], ts: np.ndarray, episodes: dict[str, v2.EpisodeMeta]) -> np.ndarray:
    out = np.zeros(len(ids), dtype=np.float32)
    for i, (eid, t) in enumerate(zip(ids, ts)):
        out[i] = float(t) / float(max(1, episodes[eid].num_steps))
    return out


def apply_policy(
    name: str,
    base: np.ndarray,
    topk: np.ndarray,
    ratios: np.ndarray,
    base_q95: float,
    base_q99: float,
    topk_q95: float,
    topk_q99: float,
) -> np.ndarray:
    if name == "base_ref":
        return base.astype(np.float32)
    if name == "topk8_ref":
        return topk.astype(np.float32)
    if name.startswith("prob_avg_"):
        w = float(name.split("_")[-1].replace("topk", "")) / 100.0
        return ((1.0 - w) * base + w * topk).astype(np.float32)
    if name.startswith("logit_avg_"):
        w = float(name.split("_")[-1].replace("topk", "")) / 100.0
        return sigmoid((1.0 - w) * logit(base) + w * logit(topk))
    if name == "max_base_topk8":
        return np.maximum(base, topk).astype(np.float32)
    if name == "topk_q95_rescue":
        return np.where(topk >= topk_q95, np.maximum(base, topk), base).astype(np.float32)
    if name == "topk_q99_rescue":
        return np.where(topk >= topk_q99, np.maximum(base, topk), base).astype(np.float32)
    if name == "agreement_q95_max":
        return np.where((base >= base_q95) & (topk >= topk_q95), np.maximum(base, topk), base).astype(np.float32)
    if name.startswith("base_plus_topk_excess_"):
        lam = float(name.rsplit("_", 1)[-1].replace("p", "."))
        return np.clip(base + lam * np.maximum(0.0, topk - topk_q95), 0.0, 1.0).astype(np.float32)
    if name.startswith("early_max_until_"):
        cutoff = float(name.rsplit("_", 1)[-1]) / 100.0
        return np.where(ratios <= cutoff, np.maximum(base, topk), base).astype(np.float32)
    if name.startswith("early_excess50_"):
        lam = float(name.rsplit("_", 1)[-1].replace("p", "."))
        boosted = np.clip(base + lam * np.maximum(0.0, topk - topk_q95), 0.0, 1.0)
        return np.where(ratios <= 0.50, boosted, base).astype(np.float32)
    raise KeyError(name)


POLICIES = [
    "base_ref",
    "topk8_ref",
    "prob_avg_25topk",
    "prob_avg_50topk",
    "prob_avg_75topk",
    "logit_avg_25topk",
    "logit_avg_50topk",
    "logit_avg_75topk",
    "max_base_topk8",
    "topk_q95_rescue",
    "topk_q99_rescue",
    "agreement_q95_max",
    "base_plus_topk_excess_0p5",
    "base_plus_topk_excess_1p0",
    "base_plus_topk_excess_1p5",
    "early_max_until_25",
    "early_max_until_50",
    "early_excess50_0p5",
    "early_excess50_1p0",
]


def metric_get(metrics: dict[str, Any], bucket: str, key: str) -> Any:
    return metrics.get(bucket, {}).get(key)


def validation_score(row: dict[str, Any], base_val: dict[str, float]) -> float:
    val_fa = float(row["val_fa"])
    val_det = float(row["val_det"])
    val25 = float(row["val_det_at_25"])
    val50 = float(row["val_det_at_50"])
    base_det = float(base_val["val_det"])
    base_fa = float(base_val["val_fa"])
    det_floor_penalty = max(0.0, (base_det - 0.02) - val_det) * 5.0
    fa_excess_penalty = max(0.0, val_fa - (base_fa + 0.03)) * 4.0
    return (2.0 * val_det + 1.0 * val25 + 0.75 * val50) - (1.75 * val_fa) - det_floor_penalty - fa_excess_penalty


def run_split(name: str, args: argparse.Namespace, episodes: dict[str, v2.EpisodeMeta]) -> list[dict[str, Any]]:
    spec = CANONICAL_SPLITS[name]
    trained_dir = Path(spec["trained_dir"])
    split_name = spec["source_split"]
    cfg = load_json(trained_dir / "run_config.json")
    buckets = {k: set(v) for k, v in load_json(trained_dir / split_name / "episode_buckets.json").items()}
    rows_by_bucket = v2.build_rows_for_split(Path(args.run_root), episodes, buckets, int(cfg["history_steps"]))
    print(f"{name}: built rows " + json.dumps({k: len(v) for k, v in rows_by_bucket.items()}, sort_keys=True), flush=True)

    dims = select_topk_dims(Path(spec["topk_rank_dir"]), args.topk)
    SELECTED_DIMS_BY_VARIANT[f"unc_topk{args.topk}"] = np.asarray(dims, dtype=np.int64)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    base_model, base_stats = load_seq_model(trained_dir / split_name / "base", cfg, device)
    topk_model, topk_stats = load_seq_model(Path(spec["topk_dir"]), cfg, device)
    variant = f"unc_topk{args.topk}"

    score_pack: dict[str, dict[str, Any]] = {}
    for bucket, rows in rows_by_bucket.items():
        bs, labels, ids, ts = v2.score_rows(base_model, base_stats, rows, "base", args.batch_size, device)
        us, labels2, ids2, ts2 = v2.score_rows(topk_model, topk_stats, rows, variant, args.batch_size, device)
        if ids != ids2 or not np.array_equal(ts, ts2) or not np.array_equal(labels, labels2):
            raise RuntimeError(f"score alignment mismatch for {name}/{bucket}")
        score_pack[bucket] = {
            "base": bs.astype(np.float32),
            "topk": us.astype(np.float32),
            "labels": labels,
            "ids": ids,
            "ts": ts,
            "ratios": row_ratios(ids, ts, episodes),
        }

    base_q95 = float(np.quantile(score_pack["success_calib_seen"]["base"], 0.95))
    base_q99 = float(np.quantile(score_pack["success_calib_seen"]["base"], 0.99))
    topk_q95 = float(np.quantile(score_pack["success_calib_seen"]["topk"], 0.95))
    topk_q99 = float(np.quantile(score_pack["success_calib_seen"]["topk"], 0.99))

    rows_out: list[dict[str, Any]] = []
    for policy in POLICIES:
        scores_by_bucket: dict[str, np.ndarray] = {}
        ids_by_bucket: dict[str, list[str]] = {}
        ts_by_bucket: dict[str, np.ndarray] = {}
        for bucket, pack in score_pack.items():
            scores_by_bucket[bucket] = apply_policy(
                policy,
                pack["base"],
                pack["topk"],
                pack["ratios"],
                base_q95,
                base_q99,
                topk_q95,
                topk_q99,
            )
            ids_by_bucket[bucket] = pack["ids"]
            ts_by_bucket[bucket] = pack["ts"]
        thresholds = v2.calibrate_thresholds(scores_by_bucket, ids_by_bucket, args.alpha, args.min_conformal_mass)
        metrics = {
            bucket: v2.evaluate_bucket(bucket, rows_by_bucket[bucket], scores_by_bucket[bucket], ids_by_bucket[bucket], ts_by_bucket[bucket], episodes, thresholds)
            for bucket in rows_by_bucket
        }
        row = {
            "canonical_split": name,
            "policy": policy,
            "topk": args.topk,
            "selected_dims": ",".join(str(d) for d in dims),
            "val_fa": metric_get(metrics, "success_val_seen", "success_false_alarm_rate") or 0.0,
            "val_det": metric_get(metrics, "failure_val_seen", "failure_detection_rate") or 0.0,
            "val_det_at_25": metric_get(metrics, "failure_val_seen", "det_at_25") or 0.0,
            "val_det_at_50": metric_get(metrics, "failure_val_seen", "det_at_50") or 0.0,
            "val_mean_time": metric_get(metrics, "failure_val_seen", "mean_detection_time"),
            "eval_fa": metric_get(metrics, spec["eval_success"], "success_false_alarm_rate") or 0.0,
            "eval_det": metric_get(metrics, spec["eval_failure"], "failure_detection_rate") or 0.0,
            "eval_det_at_25": metric_get(metrics, spec["eval_failure"], "det_at_25") or 0.0,
            "eval_det_at_50": metric_get(metrics, spec["eval_failure"], "det_at_50") or 0.0,
            "eval_mean_time": metric_get(metrics, spec["eval_failure"], "mean_detection_time"),
            "q95": thresholds["q95"],
            "q99": thresholds["q99"],
            "conformal_mass": thresholds["conformal_mass"],
        }
        rows_out.append(row)

    base_row = next(r for r in rows_out if r["policy"] == "base_ref")
    base_val = {"val_fa": float(base_row["val_fa"]), "val_det": float(base_row["val_det"])}
    for row in rows_out:
        row["validation_score"] = validation_score(row, base_val)
        row["eval_net_vs_base"] = (float(row["eval_det"]) - float(base_row["eval_det"])) - (float(row["eval_fa"]) - float(base_row["eval_fa"]))
        row["eval_det_delta_vs_base"] = float(row["eval_det"]) - float(base_row["eval_det"])
        row["eval_fa_delta_vs_base"] = float(row["eval_fa"]) - float(base_row["eval_fa"])
        row["eval_det25_delta_vs_base"] = float(row["eval_det_at_25"]) - float(base_row["eval_det_at_25"])
        row["eval_det50_delta_vs_base"] = float(row["eval_det_at_50"]) - float(base_row["eval_det_at_50"])
    best_val = max(rows_out, key=lambda r: float(r["validation_score"]))
    best_eval = max(rows_out, key=lambda r: float(r["eval_net_vs_base"]))
    for row in rows_out:
        row["selected_by_validation"] = row["policy"] == best_val["policy"]
        row["best_eval_diagnostic"] = row["policy"] == best_eval["policy"]
    return rows_out


def write_reports(out_dir: Path, rows: list[dict[str, Any]]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    fields = [
        "canonical_split",
        "policy",
        "topk",
        "selected_by_validation",
        "best_eval_diagnostic",
        "validation_score",
        "eval_net_vs_base",
        "eval_det_delta_vs_base",
        "eval_fa_delta_vs_base",
        "eval_det25_delta_vs_base",
        "eval_det50_delta_vs_base",
        "val_fa",
        "val_det",
        "val_det_at_25",
        "val_det_at_50",
        "val_mean_time",
        "eval_fa",
        "eval_det",
        "eval_det_at_25",
        "eval_det_at_50",
        "eval_mean_time",
        "q95",
        "q99",
        "conformal_mass",
        "selected_dims",
    ]
    csv_path = out_dir / "dean_topk8_fusion_policy_results.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k) for k in fields})

    lines = [
        "# Dean Top-K8 Fusion Policy v1",
        "",
        "## Method",
        "",
        "This test does not retrain the transformer. It reuses the canonical base detector and the `unc_topk8` detector, scores the same fixed buckets, then applies post-hoc fusion policies.",
        "",
        "Thresholds are recalibrated per policy using the same conformal protocol: q95 from `success_calib_seen`, then conformal mass from `success_val_seen`.",
        "",
        "Policy selection is reported two ways:",
        "",
        "- `selected_by_validation`: chosen only from seen validation metrics.",
        "- `best_eval_diagnostic`: best test/OOD trade-off after evaluation, useful for analysis but not a deployable selection rule.",
        "",
        "## Results",
        "",
    ]
    present_splits = [split for split in CANONICAL_SPLITS if any(r["canonical_split"] == split for r in rows)]
    for split in present_splits:
        split_rows = [r for r in rows if r["canonical_split"] == split]
        selected = next(r for r in split_rows if r["selected_by_validation"])
        best_eval = next(r for r in split_rows if r["best_eval_diagnostic"])
        base = next(r for r in split_rows if r["policy"] == "base_ref")
        topk = next(r for r in split_rows if r["policy"] == "topk8_ref")
        lines.extend(
            [
                f"### {split}",
                "",
                "| Policy | Selected | Eval FA | Eval Det | Det@25 | Det@50 | Mean Time | Net vs Base |",
                "|---|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        ordered = [base, topk, selected, best_eval]
        seen = set()
        compact = []
        for row in ordered:
            if row["policy"] not in seen:
                compact.append(row)
                seen.add(row["policy"])
        remaining = sorted(
            [r for r in split_rows if r["policy"] not in seen],
            key=lambda r: float(r["eval_net_vs_base"]),
            reverse=True,
        )[:6]
        compact.extend(remaining)
        for row in compact:
            sel = "validation" if row["selected_by_validation"] else "eval-diagnostic" if row["best_eval_diagnostic"] else ""
            mean_time = "" if row["eval_mean_time"] is None or (isinstance(row["eval_mean_time"], float) and math.isnan(row["eval_mean_time"])) else fnum(row["eval_mean_time"], 3)
            lines.append(
                f"| {row['policy']} | {sel} | {pct(row['eval_fa'])} | {pct(row['eval_det'])} | "
                f"{pct(row['eval_det_at_25'])} | {pct(row['eval_det_at_50'])} | {mean_time} | {fnum(row['eval_net_vs_base'], 4)} |"
            )
        lines.extend(
            [
                "",
                f"- Validation-selected policy: `{selected['policy']}`.",
                f"- Eval-diagnostic best policy: `{best_eval['policy']}`.",
                f"- Base reference: FA {pct(base['eval_fa'])}, detection {pct(base['eval_det'])}, Det@25 {pct(base['eval_det_at_25'])}, Det@50 {pct(base['eval_det_at_50'])}.",
                f"- Top-K8 reference: FA {pct(topk['eval_fa'])}, detection {pct(topk['eval_det'])}, Det@25 {pct(topk['eval_det_at_25'])}, Det@50 {pct(topk['eval_det_at_50'])}.",
                "",
            ]
        )
    report_path = out_dir / "DEAN_TOPK8_FUSION_POLICY_REPORT.md"
    report_path.write_text("\n".join(lines) + "\n")
    print(f"Wrote {csv_path}", flush=True)
    print(f"Wrote {report_path}", flush=True)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--run-root", default="/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529")
    p.add_argument("--output-dir", default="/home/dean/fiper_uncertainty_collection/experiments/dean_topk8_fusion_policy_v1_20260602")
    p.add_argument("--splits", nargs="+", default=["all_tasks_full", "ood_last2_taskids_full"])
    p.add_argument("--topk", type=int, default=8)
    p.add_argument("--batch-size", type=int, default=1024)
    p.add_argument("--alpha", type=float, default=0.15)
    p.add_argument("--min-conformal-mass", type=float, default=0.15)
    return p.parse_args()


def parse_bool(v: Any) -> bool:
    if isinstance(v, bool):
        return v
    return str(v).strip().lower() in {"1", "true", "yes"}


def load_existing_rows(out_dir: Path) -> list[dict[str, Any]]:
    csv_path = out_dir / "dean_topk8_fusion_policy_results.csv"
    if not csv_path.exists():
        return []
    numeric_fields = {
        "topk",
        "validation_score",
        "eval_net_vs_base",
        "eval_det_delta_vs_base",
        "eval_fa_delta_vs_base",
        "eval_det25_delta_vs_base",
        "eval_det50_delta_vs_base",
        "val_fa",
        "val_det",
        "val_det_at_25",
        "val_det_at_50",
        "val_mean_time",
        "eval_fa",
        "eval_det",
        "eval_det_at_25",
        "eval_det_at_50",
        "eval_mean_time",
        "q95",
        "q99",
        "conformal_mass",
    }
    rows: list[dict[str, Any]] = []
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            for key in numeric_fields:
                if key in row and row[key] not in {"", None}:
                    row[key] = float(row[key])
                elif key in row:
                    row[key] = None
            row["topk"] = int(row["topk"]) if row.get("topk") is not None else None
            row["selected_by_validation"] = parse_bool(row.get("selected_by_validation"))
            row["best_eval_diagnostic"] = parse_bool(row.get("best_eval_diagnostic"))
            rows.append(row)
    return rows


def main() -> None:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Using device={'cuda' if torch.cuda.is_available() else 'cpu'}", flush=True)
    episodes = v2.load_episode_meta(Path(args.run_root))
    all_rows: list[dict[str, Any]] = load_existing_rows(out_dir)
    if all_rows:
        print(f"Loaded existing rows: {len(all_rows)}", flush=True)
    completed_splits = {str(r["canonical_split"]) for r in all_rows}
    for split in args.splits:
        if split in completed_splits:
            print(f"Skipping completed split {split}", flush=True)
            continue
        print(f"=== SPLIT {split} ===", flush=True)
        all_rows.extend(run_split(split, args, episodes))
        write_reports(out_dir, all_rows)
    write_json(out_dir / "run_config.json", vars(args))
    write_reports(out_dir, all_rows)


if __name__ == "__main__":
    main()
