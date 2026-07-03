#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import numpy as np
import torch

import run_dean_uncertainty_transformer_exploration_v2 as v2


CANONICAL_SPLITS = {
    "all_tasks_full": {
        "trained_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_all_tasks_full_uncertainty_test_20260601",
        "split_name": "all_tasks_random",
        "eval_success": "success_test_seen",
        "eval_failure": "failure_test_seen",
    },
    "ood_last2_taskids_full": {
        "trained_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_ood_last2_taskids_full_v1_20260601",
        "split_name": "ood_last2_taskids_full",
        "eval_success": "success_test_ood",
        "eval_failure": "failure_eval_ood",
    },
}


SELECTED_DIMS_BY_VARIANT: dict[str, np.ndarray] = {}
ORIGINAL_MAKE_ARRAYS = v2.make_arrays


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, default=str) + "\n")


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


def stack_unc(rows: list[v2.RowEx]) -> tuple[np.ndarray, np.ndarray]:
    x = np.stack([r.uncertainty for r in rows], axis=0).astype(np.float32)
    y = np.asarray([r.y for r in rows], dtype=np.float32)
    return x, y


def rank_uncertainty_dims(train_rows: list[v2.RowEx], val_rows: list[v2.RowEx]) -> list[dict[str, float]]:
    x_train, y_train = stack_unc(train_rows)
    x_val, y_val = stack_unc(val_rows)
    ranking: list[dict[str, float]] = []
    for dim in range(x_train.shape[1]):
        train_auc = v2.auroc_binary(y_train, x_train[:, dim])
        val_auc = v2.auroc_binary(y_val, x_val[:, dim])
        train_dir = np.sign(train_auc - 0.5)
        val_dir = np.sign(val_auc - 0.5)
        consistent = bool(train_dir == 0 or val_dir == 0 or train_dir == val_dir)
        score = abs(train_auc - 0.5) + 0.75 * abs(val_auc - 0.5)
        if not consistent:
            score *= 0.25
        ranking.append(
            {
                "dim": dim,
                "score": float(score),
                "train_auc": float(train_auc),
                "val_auc": float(val_auc),
                "consistent_direction": consistent,
            }
        )
    ranking.sort(key=lambda r: r["score"], reverse=True)
    return ranking


def metrics_summary(result: dict[str, Any], spec: dict[str, str]) -> dict[str, Any]:
    metrics = result["metrics_by_bucket"]
    success_eval = spec["eval_success"]
    failure_eval = spec["eval_failure"]
    return {
        "success_fa": metrics[success_eval].get("success_false_alarm_rate"),
        "failure_detection": metrics[failure_eval].get("failure_detection_rate"),
        "failure_det_at_25": metrics[failure_eval].get("det_at_25"),
        "failure_det_at_50": metrics[failure_eval].get("det_at_50"),
        "failure_mean_detection_time": metrics[failure_eval].get("mean_detection_time"),
    }


def pct(v: Any) -> str:
    return "" if v is None else f"{100.0 * float(v):.1f}%"


def load_reference_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for split_key, spec in CANONICAL_SPLITS.items():
        csv_path = Path(spec["trained_dir"]) / "dean_uncertainty_comparison_results.csv"
        if not csv_path.exists():
            continue
        with csv_path.open() as f:
            for row in csv.DictReader(f):
                if row.get("variant") not in {"base", "unc_raw"}:
                    continue
                row["canonical_split"] = split_key
                row["policy"] = row["variant"]
                if split_key == "all_tasks_full":
                    row["success_fa"] = row.get("seen_success_fa")
                    row["failure_detection"] = row.get("seen_failure_detection")
                    row["failure_det_at_25"] = row.get("seen_failure_det_at_25")
                    row["failure_det_at_50"] = row.get("seen_failure_det_at_50")
                else:
                    row["success_fa"] = row.get("ood_success_fa")
                    row["failure_detection"] = row.get("ood_failure_detection")
                    row["failure_det_at_25"] = row.get("ood_failure_det_at_25")
                    row["failure_det_at_50"] = row.get("ood_failure_det_at_50")
                rows.append(row)
    return rows


def as_float(v: Any) -> float | None:
    if v is None or v == "":
        return None
    return float(v)


def write_final_report(out_dir: Path, results: list[dict[str, Any]], reference_rows: list[dict[str, Any]]) -> None:
    csv_path = out_dir / "dean_uncertainty_topk_feature_sweep_results.csv"
    fields = [
        "canonical_split",
        "policy",
        "topk",
        "best_epoch",
        "success_fa",
        "failure_detection",
        "failure_det_at_25",
        "failure_det_at_50",
        "failure_mean_detection_time",
        "q95",
        "q99",
        "conformal_mass",
    ]
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in results:
            row = {k: r.get(k) for k in fields}
            writer.writerow(row)

    ref_by_split = {}
    for row in reference_rows:
        ref_by_split.setdefault(row["canonical_split"], []).append(row)

    lines = [
        "# Dean Uncertainty Top-K Feature Sweep v1",
        "",
        "## Method",
        "",
        "This run keeps the canonical transformer architecture and canonical episode splits fixed.",
        "It adds only the top-K uncertainty dimensions selected from seen train/validation rows.",
        "Test and OOD rows are not used for feature ranking.",
        "",
        "## Results",
        "",
        "| Split | Policy | FA | Det | Det@25 | Det@50 | Mean Time | Best Epoch |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for split in CANONICAL_SPLITS:
        for ref in ref_by_split.get(split, []):
            lines.append(
                f"| {split} | ref_{ref['policy']} | {pct(as_float(ref['success_fa']))} | "
                f"{pct(as_float(ref['failure_detection']))} | {pct(as_float(ref['failure_det_at_25']))} | "
                f"{pct(as_float(ref['failure_det_at_50']))} |  | {ref.get('best_epoch', '')} |"
            )
        for r in [x for x in results if x["canonical_split"] == split]:
            mean_time = r["failure_mean_detection_time"]
            mean_time_s = "" if mean_time is None else f"{mean_time:.3f}"
            lines.append(
                f"| {split} | {r['policy']} | {pct(r['success_fa'])} | {pct(r['failure_detection'])} | "
                f"{pct(r['failure_det_at_25'])} | {pct(r['failure_det_at_50'])} | "
                f"{mean_time_s} | {r['best_epoch']} |"
            )
    report_path = out_dir / "DEAN_UNCERTAINTY_TOPK_FEATURE_SWEEP_REPORT.md"
    report_path.write_text("\n".join(lines) + "\n")
    print(f"Wrote {csv_path}", flush=True)
    print(f"Wrote {report_path}", flush=True)


def run_split(split_key: str, args: argparse.Namespace, episodes: dict[str, v2.EpisodeMeta]) -> list[dict[str, Any]]:
    spec = CANONICAL_SPLITS[split_key]
    trained_dir = Path(spec["trained_dir"])
    source_split = spec["split_name"]
    cfg = load_json(trained_dir / "run_config.json")
    buckets = {k: set(v) for k, v in load_json(trained_dir / source_split / "episode_buckets.json").items()}
    rows_by_bucket = v2.build_rows_for_split(Path(args.run_root), episodes, buckets, int(cfg["history_steps"]))
    train_rows = rows_by_bucket["success_train_seen"] + rows_by_bucket["failure_train_seen"]
    val_rows = rows_by_bucket["success_val_seen"] + rows_by_bucket["failure_val_seen"]
    ranking = rank_uncertainty_dims(train_rows, val_rows)

    split_out = Path(args.output_dir) / split_key
    write_json(split_out / "uncertainty_dim_ranking.json", ranking)
    write_json(split_out / "bucket_counts.json", {k: {"episodes": len(set(r.episode_id for r in v)), "rows": len(v)} for k, v in rows_by_bucket.items()})

    run_args = SimpleNamespace(**cfg)
    run_args.output_dir = args.output_dir
    run_args.run_root = args.run_root
    run_args.max_epochs = args.max_epochs
    run_args.patience = args.patience
    run_args.batch_size = args.batch_size
    run_args.variants = []
    run_args.unc_raw_static_dropout = float(cfg.get("unc_raw_static_dropout", 0.25))
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    results: list[dict[str, Any]] = []
    for topk in args.topk:
        variant = f"unc_topk{topk}"
        dims = np.asarray([int(r["dim"]) for r in ranking[:topk]], dtype=np.int64)
        SELECTED_DIMS_BY_VARIANT[variant] = dims
        run_args.variants = [variant]
        print(f"=== {split_key} {variant} dims={dims.tolist()} ===", flush=True)
        result = v2.run_job(split_key, variant, rows_by_bucket, episodes, run_args, device, Path(args.output_dir))
        result["feature_audit"]["input_fields"].append("selected_uncertainty_dims_from_seen_train_val")
        result["feature_audit"]["selected_uncertainty_dims"] = dims.tolist()
        result["feature_audit"]["selected_uncertainty_dim_count"] = int(topk)
        result["feature_audit"]["static_dim"] = int(43 + topk)
        result["feature_selection"] = {
            "selection_source": "success_train_seen+failure_train_seen and success_val_seen+failure_val_seen only",
            "topk": int(topk),
            "selected_dims": dims.tolist(),
            "ranking_top": ranking[:topk],
            "uses_test_rows_for_selection": False,
            "uses_ood_rows_for_selection": False,
        }
        job_dir = Path(args.output_dir) / split_key / variant
        write_json(job_dir / "metrics.json", result)
        summary = metrics_summary(result, spec)
        results.append(
            {
                "canonical_split": split_key,
                "policy": variant,
                "topk": int(topk),
                "best_epoch": result["best_epoch"],
                **summary,
                "q95": result["thresholds"]["q95"],
                "q99": result["thresholds"]["q99"],
                "conformal_mass": result["thresholds"]["conformal_mass"],
            }
        )
    return results


def load_canonical_buckets(split_key: str) -> tuple[dict[str, set[str]], int]:
    spec = CANONICAL_SPLITS[split_key]
    trained_dir = Path(spec["trained_dir"])
    source_split = spec["split_name"]
    cfg = load_json(trained_dir / "run_config.json")
    buckets = {k: set(v) for k, v in load_json(trained_dir / source_split / "episode_buckets.json").items()}
    return buckets, int(cfg["history_steps"])


def build_rows_for_splits_once(
    run_root: Path,
    episodes: dict[str, v2.EpisodeMeta],
    split_buckets: dict[str, dict[str, set[str]]],
    history_steps: int,
) -> dict[str, dict[str, list[v2.RowEx]]]:
    assignments: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for split_key, buckets in split_buckets.items():
        for bucket, ids in buckets.items():
            for eid in ids:
                assignments[eid].append((split_key, bucket))

    rows_by_split = {
        split_key: {bucket: [] for bucket in buckets}
        for split_key, buckets in split_buckets.items()
    }
    wanted = set(assignments)
    parsed_rows = 0
    used_rows = 0
    for worker_dir in v2.WORKER_DIRS:
        path = run_root / worker_dir / "fiper_receding_samples.jsonl"
        if not path.exists():
            continue
        current_eid = None
        history_buffer: list[tuple[np.ndarray, np.ndarray, np.ndarray]] = []
        for raw in v2.read_jsonl(path):
            parsed_rows += 1
            eid = str(raw.get("episode_id"))
            if eid != current_eid:
                current_eid = eid
                history_buffer = []
            if eid not in wanted:
                continue
            meta = episodes[eid]
            action = v2.pad_seq(raw.get("main_candidate_action_chunk_normalized"), 10, 7)
            ace = v2.compute_ace_metrics(raw.get("ace_candidate_chunks_normalized"))
            current = raw.get("current") or {}
            proprio = v2.pad_flat(current.get("proprio"), 8)
            executed = v2.pad_flat(raw.get("executed_action"), 7)
            action_stats = np.concatenate([action[0], action.mean(axis=0), action.std(axis=0), action[-1] - action[0]]).astype(np.float32)
            static_base = np.concatenate([action_stats, ace, proprio]).astype(np.float32)
            unc = v2.pad_flat(raw.get("simvla_uncertainty_49d"), 49)
            delta = v2.pad_flat(raw.get("simvla_uncertainty_delta_49d"), 49)
            uncertainty = np.concatenate([unc, delta]).astype(np.float32)

            hist = np.zeros((history_steps, 21), dtype=np.float32)
            hist_src = history_buffer[-history_steps:]
            offset = history_steps - len(hist_src)
            for i, (h_prop, h_act, h_ace) in enumerate(hist_src):
                hist[offset + i, :] = np.concatenate([h_prop, h_act, h_ace[:6]])

            row = v2.RowEx(
                episode_id=eid,
                timestep=int(raw.get("timestep") or 0),
                y=0.0 if meta.success else 1.0,
                history=hist,
                action=action,
                static_base=static_base,
                uncertainty=uncertainty,
            )
            for split_key, bucket in assignments[eid]:
                rows_by_split[split_key][bucket].append(row)
            history_buffer.append((proprio, executed, ace))
            used_rows += 1
    print(f"Built canonical split rows in one pass: parsed={parsed_rows}, matched={used_rows}", flush=True)
    return rows_by_split


def run_split_from_rows(
    split_key: str,
    rows_by_bucket: dict[str, list[v2.RowEx]],
    args: argparse.Namespace,
    episodes: dict[str, v2.EpisodeMeta],
) -> list[dict[str, Any]]:
    spec = CANONICAL_SPLITS[split_key]
    trained_dir = Path(spec["trained_dir"])
    cfg = load_json(trained_dir / "run_config.json")
    train_rows = rows_by_bucket["success_train_seen"] + rows_by_bucket["failure_train_seen"]
    val_rows = rows_by_bucket["success_val_seen"] + rows_by_bucket["failure_val_seen"]
    ranking = rank_uncertainty_dims(train_rows, val_rows)

    split_out = Path(args.output_dir) / split_key
    write_json(split_out / "uncertainty_dim_ranking.json", ranking)
    write_json(split_out / "bucket_counts.json", {k: {"episodes": len(set(r.episode_id for r in v)), "rows": len(v)} for k, v in rows_by_bucket.items()})

    run_args = SimpleNamespace(**cfg)
    run_args.output_dir = args.output_dir
    run_args.run_root = args.run_root
    run_args.max_epochs = args.max_epochs
    run_args.patience = args.patience
    run_args.batch_size = args.batch_size
    run_args.variants = []
    run_args.unc_raw_static_dropout = float(cfg.get("unc_raw_static_dropout", 0.25))
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    results: list[dict[str, Any]] = []
    for topk in args.topk:
        variant = f"unc_topk{topk}"
        dims = np.asarray([int(r["dim"]) for r in ranking[:topk]], dtype=np.int64)
        SELECTED_DIMS_BY_VARIANT[variant] = dims
        run_args.variants = [variant]
        print(f"=== {split_key} {variant} dims={dims.tolist()} ===", flush=True)
        result = v2.run_job(split_key, variant, rows_by_bucket, episodes, run_args, device, Path(args.output_dir))
        result["feature_audit"]["input_fields"].append("selected_uncertainty_dims_from_seen_train_val")
        result["feature_audit"]["selected_uncertainty_dims"] = dims.tolist()
        result["feature_audit"]["selected_uncertainty_dim_count"] = int(topk)
        result["feature_audit"]["static_dim"] = int(43 + topk)
        result["feature_selection"] = {
            "selection_source": "success_train_seen+failure_train_seen and success_val_seen+failure_val_seen only",
            "topk": int(topk),
            "selected_dims": dims.tolist(),
            "ranking_top": ranking[:topk],
            "uses_test_rows_for_selection": False,
            "uses_ood_rows_for_selection": False,
        }
        job_dir = Path(args.output_dir) / split_key / variant
        write_json(job_dir / "metrics.json", result)
        summary = metrics_summary(result, spec)
        results.append(
            {
                "canonical_split": split_key,
                "policy": variant,
                "topk": int(topk),
                "best_epoch": result["best_epoch"],
                **summary,
                "q95": result["thresholds"]["q95"],
                "q99": result["thresholds"]["q99"],
                "conformal_mass": result["thresholds"]["conformal_mass"],
            }
        )
    return results


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--run-root", default="/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529")
    p.add_argument("--output-dir", default="/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602")
    p.add_argument("--splits", nargs="+", default=["all_tasks_full", "ood_last2_taskids_full"])
    p.add_argument("--topk", nargs="+", type=int, default=[8, 16, 32])
    p.add_argument("--max-epochs", type=int, default=30)
    p.add_argument("--patience", type=int, default=6)
    p.add_argument("--batch-size", type=int, default=512)
    p.add_argument("--seed", type=int, default=20260602)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    v2.seed_everything(args.seed)
    v2.make_arrays = make_arrays_selected
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    episodes = v2.load_episode_meta(Path(args.run_root))
    split_buckets: dict[str, dict[str, set[str]]] = {}
    history_steps = None
    for split in args.splits:
        buckets, split_history_steps = load_canonical_buckets(split)
        split_buckets[split] = buckets
        if history_steps is None:
            history_steps = split_history_steps
        elif history_steps != split_history_steps:
            raise RuntimeError(f"history step mismatch: {history_steps} vs {split_history_steps}")
    rows_by_split = build_rows_for_splits_once(Path(args.run_root), episodes, split_buckets, int(history_steps or 16))
    all_results: list[dict[str, Any]] = []
    for split in args.splits:
        all_results.extend(run_split_from_rows(split, rows_by_split[split], args, episodes))
        write_final_report(out_dir, all_results, load_reference_rows())
    write_final_report(out_dir, all_results, load_reference_rows())
    write_json(out_dir / "run_config.json", vars(args))


if __name__ == "__main__":
    main()
