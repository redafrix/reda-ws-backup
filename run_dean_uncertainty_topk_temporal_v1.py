#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import numpy as np
import torch

import run_dean_uncertainty_transformer_exploration_v2 as v2


CANONICAL_SPLITS = {
    "all_tasks_full": {
        "trained_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_all_tasks_full_uncertainty_test_20260601",
        "source_split": "all_tasks_random",
        "eval_success": "success_test_seen",
        "eval_failure": "failure_test_seen",
        "topk_job": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/all_tasks_full/unc_topk8",
        "rank_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/all_tasks_full",
    },
    "ood_last2_taskids_full": {
        "trained_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_ood_last2_taskids_full_v1_20260601",
        "source_split": "ood_last2_taskids_full",
        "eval_success": "success_test_ood",
        "eval_failure": "failure_eval_ood",
        "topk_job": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/ood_last2_taskids_full/unc_topk8",
        "rank_dir": "/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_feature_sweep_v1_20260602/ood_last2_taskids_full",
    },
}


VARIANT = "unc_topk8_temporal_v1"
SELECTED_DIMS = np.asarray([], dtype=np.int64)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, default=str) + "\n")


def select_topk_dims(rank_dir: Path, topk: int) -> list[int]:
    metrics_path = rank_dir / f"unc_topk{topk}" / "metrics.json"
    if metrics_path.exists():
        metrics = load_json(metrics_path)
        dims = metrics.get("feature_selection", {}).get("selected_dims")
        if dims:
            return [int(d) for d in dims]
    ranking = load_json(rank_dir / "uncertainty_dim_ranking.json")
    return [int(r["dim"]) for r in ranking[:topk]]


def make_arrays_temporal(rows: list[v2.RowEx], variant: str):
    if variant != VARIANT:
        return ORIGINAL_MAKE_ARRAYS(rows, variant)
    h = np.stack([r.history for r in rows], axis=0).astype(np.float32)
    a = np.stack([r.action for r in rows], axis=0).astype(np.float32)
    st = np.stack(
        [np.concatenate([r.static_base, r.uncertainty[SELECTED_DIMS]]).astype(np.float32) for r in rows],
        axis=0,
    )
    y = np.asarray([r.y for r in rows], dtype=np.float32)
    episode_ids = [r.episode_id for r in rows]
    timesteps = np.asarray([r.timestep for r in rows], dtype=np.int32)
    return h, a, st, y, episode_ids, timesteps


ORIGINAL_MAKE_ARRAYS = v2.make_arrays
v2.make_arrays = make_arrays_temporal


def build_rows_temporal(
    run_root: Path,
    episodes: dict[str, v2.EpisodeMeta],
    buckets: dict[str, set[str]],
    history_steps: int,
) -> dict[str, list[v2.RowEx]]:
    episode_to_bucket: dict[str, str] = {}
    for bucket, ids in buckets.items():
        for eid in ids:
            episode_to_bucket[eid] = bucket

    rows_by_bucket: dict[str, list[v2.RowEx]] = {k: [] for k in buckets}
    wanted = set(episode_to_bucket)
    parsed_rows = 0
    used_rows = 0

    for worker_dir in v2.WORKER_DIRS:
        path = run_root / worker_dir / "fiper_receding_samples.jsonl"
        if not path.exists():
            continue
        current_eid = None
        history_buffer: list[tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]] = []
        for raw in v2.read_jsonl(path):
            parsed_rows += 1
            eid = str(raw.get("episode_id"))
            if eid != current_eid:
                current_eid = eid
                history_buffer = []
            current = raw.get("current") or {}
            proprio = v2.pad_flat(current.get("proprio"), 8)
            executed = v2.pad_flat(raw.get("executed_action"), 7)
            ace = v2.compute_ace_metrics(raw.get("ace_candidate_chunks_normalized"))
            unc = v2.pad_flat(raw.get("simvla_uncertainty_49d"), 49)
            delta = v2.pad_flat(raw.get("simvla_uncertainty_delta_49d"), 49)
            uncertainty = np.concatenate([unc, delta]).astype(np.float32)
            selected_unc = uncertainty[SELECTED_DIMS].astype(np.float32)

            if eid not in wanted:
                history_buffer.append((proprio, executed, ace, selected_unc))
                continue

            meta = episodes[eid]
            bucket = episode_to_bucket[eid]
            action = v2.pad_seq(raw.get("main_candidate_action_chunk_normalized"), 10, 7)
            action_stats = np.concatenate([action[0], action.mean(axis=0), action.std(axis=0), action[-1] - action[0]]).astype(np.float32)
            static_base = np.concatenate([action_stats, ace, proprio]).astype(np.float32)

            hist_dim = 21 + int(SELECTED_DIMS.size)
            hist = np.zeros((history_steps, hist_dim), dtype=np.float32)
            hist_src = history_buffer[-history_steps:]
            offset = history_steps - len(hist_src)
            for i, (h_prop, h_act, h_ace, h_unc) in enumerate(hist_src):
                hist[offset + i, :] = np.concatenate([h_prop, h_act, h_ace[:6], h_unc]).astype(np.float32)

            rows_by_bucket[bucket].append(
                v2.RowEx(
                    episode_id=eid,
                    timestep=int(raw.get("timestep") or 0),
                    y=0.0 if meta.success else 1.0,
                    history=hist,
                    action=action,
                    static_base=static_base,
                    uncertainty=uncertainty,
                )
            )
            history_buffer.append((proprio, executed, ace, selected_unc))
            used_rows += 1
    print(f"Built temporal rows: parsed={parsed_rows}, used={used_rows}, history_dim={21 + int(SELECTED_DIMS.size)}", flush=True)
    return rows_by_bucket


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


def load_reference_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for split_key, spec in CANONICAL_SPLITS.items():
        csv_path = Path(spec["trained_dir"]) / "dean_uncertainty_comparison_results.csv"
        with csv_path.open() as f:
            for row in csv.DictReader(f):
                if row.get("variant") != "base":
                    continue
                rows.append(
                    {
                        "canonical_split": split_key,
                        "policy": "ref_base",
                        "best_epoch": row.get("best_epoch", ""),
                        "success_fa": row.get("seen_success_fa") if split_key == "all_tasks_full" else row.get("ood_success_fa"),
                        "failure_detection": row.get("seen_failure_detection") if split_key == "all_tasks_full" else row.get("ood_failure_detection"),
                        "failure_det_at_25": row.get("seen_failure_det_at_25") if split_key == "all_tasks_full" else row.get("ood_failure_det_at_25"),
                        "failure_det_at_50": row.get("seen_failure_det_at_50") if split_key == "all_tasks_full" else row.get("ood_failure_det_at_50"),
                        "failure_mean_detection_time": "",
                    }
                )
        topk_metrics = load_json(Path(spec["topk_job"]) / "metrics.json")
        summary = metrics_summary(topk_metrics, spec)
        rows.append(
            {
                "canonical_split": split_key,
                "policy": "ref_unc_topk8",
                "best_epoch": topk_metrics["best_epoch"],
                **summary,
            }
        )
    return rows


def as_float(v: Any) -> float | None:
    if v is None or v == "":
        return None
    return float(v)


def pct(v: Any) -> str:
    val = as_float(v)
    return "" if val is None else f"{100.0 * val:.1f}%"


def run_split(split_key: str, args: argparse.Namespace, episodes: dict[str, v2.EpisodeMeta]) -> dict[str, Any]:
    global SELECTED_DIMS
    spec = CANONICAL_SPLITS[split_key]
    trained_dir = Path(spec["trained_dir"])
    source_split = spec["source_split"]
    cfg = load_json(trained_dir / "run_config.json")
    buckets = {k: set(v) for k, v in load_json(trained_dir / source_split / "episode_buckets.json").items()}
    dims = select_topk_dims(Path(spec["rank_dir"]), args.topk)
    SELECTED_DIMS = np.asarray(dims, dtype=np.int64)
    print(f"=== {split_key} {VARIANT} dims={dims} ===", flush=True)
    rows_by_bucket = build_rows_temporal(Path(args.run_root), episodes, buckets, int(cfg["history_steps"]))

    run_args = SimpleNamespace(**cfg)
    run_args.output_dir = args.output_dir
    run_args.run_root = args.run_root
    run_args.max_epochs = args.max_epochs
    run_args.patience = args.patience
    run_args.batch_size = args.batch_size
    run_args.variants = [VARIANT]
    run_args.unc_raw_static_dropout = 0.0
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    result = v2.run_job(split_key, VARIANT, rows_by_bucket, episodes, run_args, device, Path(args.output_dir))
    result["feature_audit"]["input_fields"].extend(
        [
            "history.previous_selected_uncertainty_top8",
            "current.selected_uncertainty_top8",
        ]
    )
    result["feature_audit"]["selected_uncertainty_dims"] = dims
    result["feature_audit"]["selected_uncertainty_dim_count"] = int(args.topk)
    result["feature_audit"]["history_dim"] = int(21 + args.topk)
    result["feature_audit"]["static_dim"] = int(43 + args.topk)
    result["feature_audit"]["uses_test_rows_for_feature_selection"] = False
    result["feature_audit"]["uses_ood_rows_for_feature_selection"] = False
    result["feature_selection"] = {
        "selection_source": "existing unc_topk8 ranking selected from seen train/validation rows only",
        "topk": int(args.topk),
        "selected_dims": dims,
        "uses_test_rows_for_selection": False,
        "uses_ood_rows_for_selection": False,
    }
    job_dir = Path(args.output_dir) / split_key / VARIANT
    write_json(job_dir / "metrics.json", result)
    return {
        "canonical_split": split_key,
        "policy": VARIANT,
        "topk": int(args.topk),
        "best_epoch": result["best_epoch"],
        **metrics_summary(result, spec),
        "q95": result["thresholds"]["q95"],
        "q99": result["thresholds"]["q99"],
        "conformal_mass": result["thresholds"]["conformal_mass"],
        "selected_dims": ",".join(str(d) for d in dims),
    }


def write_reports(out_dir: Path, rows: list[dict[str, Any]], refs: list[dict[str, Any]]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
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
        "selected_dims",
    ]
    csv_path = out_dir / "dean_uncertainty_topk_temporal_results.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k) for k in fields})

    lines = [
        "# Dean Uncertainty Top-K Temporal v1",
        "",
        "## Method",
        "",
        "This run starts from `unc_topk8` but moves the same selected uncertainty dimensions into the transformer temporal stream.",
        "",
        "- Current static input: canonical base static features + current selected uncertainty top-8.",
        "- History tokens: previous proprio/action/ACE history + previous selected uncertainty top-8.",
        "- The current timestep's uncertainty is not inserted into previous-history tokens.",
        "- Top-8 dimensions are reused from the prior seen train/validation ranking; test/OOD rows are not used for feature selection.",
        "",
        "## Results",
        "",
        "| Split | Policy | FA | Det | Det@25 | Det@50 | Mean Time | Best Epoch |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for split in CANONICAL_SPLITS:
        for row in [r for r in refs + rows if r["canonical_split"] == split]:
            mean_time = row.get("failure_mean_detection_time")
            mean_s = "" if mean_time in {None, ""} else f"{float(mean_time):.3f}"
            lines.append(
                f"| {split} | {row['policy']} | {pct(row.get('success_fa'))} | "
                f"{pct(row.get('failure_detection'))} | {pct(row.get('failure_det_at_25'))} | "
                f"{pct(row.get('failure_det_at_50'))} | {mean_s} | {row.get('best_epoch', '')} |"
            )
    lines.extend(["", "## Verdict Inputs", ""])
    for split in CANONICAL_SPLITS:
        base = next(r for r in refs if r["canonical_split"] == split and r["policy"] == "ref_base")
        topk = next(r for r in refs if r["canonical_split"] == split and r["policy"] == "ref_unc_topk8")
        temporal = next((r for r in rows if r["canonical_split"] == split), None)
        if temporal is None:
            continue
        lines.append(f"### {split}")
        lines.append("")
        lines.append(
            f"- Base: FA {pct(base['success_fa'])}, Det {pct(base['failure_detection'])}, Det@25 {pct(base['failure_det_at_25'])}, Det@50 {pct(base['failure_det_at_50'])}."
        )
        lines.append(
            f"- Top-K8: FA {pct(topk['success_fa'])}, Det {pct(topk['failure_detection'])}, Det@25 {pct(topk['failure_det_at_25'])}, Det@50 {pct(topk['failure_det_at_50'])}."
        )
        lines.append(
            f"- Temporal Top-K8: FA {pct(temporal['success_fa'])}, Det {pct(temporal['failure_detection'])}, Det@25 {pct(temporal['failure_det_at_25'])}, Det@50 {pct(temporal['failure_det_at_50'])}."
        )
        lines.append("")
    report_path = out_dir / "DEAN_UNCERTAINTY_TOPK_TEMPORAL_REPORT.md"
    report_path.write_text("\n".join(lines) + "\n")
    print(f"Wrote {csv_path}", flush=True)
    print(f"Wrote {report_path}", flush=True)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--run-root", default="/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529")
    p.add_argument("--output-dir", default="/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_topk_temporal_v1_20260602")
    p.add_argument("--splits", nargs="+", default=["all_tasks_full", "ood_last2_taskids_full"])
    p.add_argument("--topk", type=int, default=8)
    p.add_argument("--batch-size", type=int, default=512)
    p.add_argument("--max-epochs", type=int, default=35)
    p.add_argument("--patience", type=int, default=8)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Using device={'cuda' if torch.cuda.is_available() else 'cpu'}", flush=True)
    episodes = v2.load_episode_meta(Path(args.run_root))
    refs = load_reference_rows()
    rows = []
    for split in args.splits:
        rows.append(run_split(split, args, episodes))
        write_reports(out_dir, rows, refs)
    write_json(out_dir / "run_config.json", vars(args))
    write_reports(out_dir, rows, refs)


if __name__ == "__main__":
    main()
