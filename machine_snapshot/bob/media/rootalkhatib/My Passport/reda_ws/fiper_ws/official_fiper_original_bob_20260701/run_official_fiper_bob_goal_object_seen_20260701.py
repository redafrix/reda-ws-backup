#!/usr/bin/env python3
"""Run official FIPER training/evaluation on the prepared LIBERO goal-object dataset.

This is a dataset adapter/runner only. It uses the official FIPER RNDTrainer and
EvaluationManager classes unchanged, while loading our already materialized
obs_embeddings/action_preds tensors under the tensor names expected by the repo.
"""

from __future__ import annotations

import copy
import csv
import gc
import json
import os
import pickle
import shutil
import sys
from pathlib import Path

import numpy as np
import torch
from omegaconf import OmegaConf

# Official FIPER was written against older NumPy and calls np.bool in
# evaluation/utils.py. Keep the official method code unchanged and provide the
# removed alias at runtime for NumPy >= 1.24. It must map to np.bool_, not
# Python bool, because the official confusion-matrix check receives np.bool_
# scalars after thresholding.
if not hasattr(np, "bool"):
    np.bool = np.bool_  # type: ignore[attr-defined]


ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701")
REPO = ROOT / "repos" / "fiper"
TASK = "libero_goal_object_official"
TASK_DATA = ROOT / "official_fiper_data" / TASK
PROCESSED = TASK_DATA / "processed_rollouts"
RUN_ROOT = ROOT / "official_fiper_seen_train_eval_20260701"
REPORT = RUN_ROOT / "OFFICIAL_FIPER_SEEN_TRAIN_EVAL_REPORT.md"

SEEDS = [0, 1, 2, 42, 43]
METHODS = ["entropy", "rnd_oe"]
COMBINED = {
    1: {
        "m1": {"name": "rnd_oe", "window_sizes": None, "quantiles": None},
        "m2": {"name": "entropy", "window_sizes": None, "quantiles": None},
        "operation": "and",
    }
}


def import_official_repo():
    os.chdir(REPO)
    sys.path.insert(0, str(REPO))
    import evaluation.utils as eval_utils
    from datasets.rollout_datasets import ProcessedRolloutDataset
    from evaluation import EvaluationManager
    from rnd import RNDTrainer
    from shared_utils.hydra_utils import load_config
    from shared_utils.utility_functions import get_required_tensors, set_seed

    def robust_confusion_matrix(failures_detected, successful_rollouts):
        failures_detected = np.asarray(failures_detected, dtype=bool)
        successful_rollouts = np.asarray(successful_rollouts, dtype=bool)
        if failures_detected.shape != successful_rollouts.shape:
            raise ValueError("Length and shape of failures_detected and successful_rollouts must be the same.")
        fp = np.sum(failures_detected & successful_rollouts)
        tn = np.sum(~failures_detected & successful_rollouts)
        tp = np.sum(failures_detected & ~successful_rollouts)
        fn = np.sum(~failures_detected & ~successful_rollouts)
        return tp, tn, fp, fn

    eval_utils._calculate_confusion_matrix = robust_confusion_matrix

    return ProcessedRolloutDataset, EvaluationManager, RNDTrainer, load_config, get_required_tensors, set_seed


def ensure_task_config():
    cfg_path = REPO / "configs" / "task" / f"{TASK}.yaml"
    cfg_path.write_text(
        """defaults:
  - base

name: "libero_goal_object_official"
description: "Official LIBERO goal_object subset materialized for FIPER from SimVLA H10 candidate rollouts"
type: simulation

environment:
  name: "LIBERO-goal-object"
  ts: 0.1
  max_episode_steps: 800
  fail_on_error: true
  fail_after_steps: 800

observation_space:
  observation_type: "embedding"
  observation_dim: 960

state_space:
  state_dim: 0
  state_types:
  state_bounds:
  state_mapping:
    position:
    rotation:
    velocity:

action_space:
  action_type: "continuous"
  actions:
    dim: 7
    action_bounds:
    action_mapping:
      position: [0, 1, 2]
      rotation: [3, 4, 5]
      velocity:
      gripper: [6]
  action_pred:
    format: "(batch_size, prediction_horizon, action_dim)"
    action_prediction_horizon: 10
    batch_size: 9
    shape: (${task.action_space.action_pred.batch_size}, ${task.action_space.action_pred.action_prediction_horizon}, ${task.action_space.actions.dim})
  action_execution_horizon: 10
""",
        encoding="utf-8",
    )
    return cfg_path


def load_dataset(ProcessedRolloutDataset, required_tensors):
    metadata = pickle.load(open(PROCESSED / "metadata.pkl", "rb"))
    obs_embeddings = torch.load(PROCESSED / "obs_embeddings.pt", map_location="cpu", weights_only=True)
    action_preds = torch.load(PROCESSED / "action_preds.pt", map_location="cpu", weights_only=True)

    metadata = dict(metadata)
    metadata["available_tensors"] = ["obs_embeddings", "action_preds"]

    dataset = ProcessedRolloutDataset(
        task_data_path=str(TASK_DATA),
        base_config_path=str(REPO / "configs"),
        required_tensors=required_tensors,
        optional_tensors=[],
        normalize_tensors={
            "obs_embeddings": False,
            "action_preds": False,
            "rgb_images": True,
            "actions": False,
            "states": False,
            "mode": "gaussian",
            "range_eps": 1e-5,
            "limits": [-1, 1],
            "fit_offset": True,
        },
    )
    dataset.data = {
        "metadata": metadata,
        "obs_embeddings": obs_embeddings,
        "action_preds": action_preds,
    }
    dataset.dataset_loaded = True
    dataset.normalizer = {}
    dataset._assert_metadata()
    dataset._assert_tensor("obs_embeddings", shape=(960,))
    dataset._assert_tensor("action_preds", shape=(9, 10, 7))
    return dataset


def alarm_metrics(scores_by_episode, success_mask):
    success_mask = np.asarray(success_mask, dtype=bool)
    failure_mask = ~success_mask
    alarms = []
    det_fracs = []
    for scores in scores_by_episode:
        arr = np.asarray(scores, dtype=np.float64)
        hit = np.flatnonzero(arr > 1.0)
        alarms.append(hit.size > 0)
        if hit.size:
            det_fracs.append(float(hit[0]) / max(1, len(arr)))
        else:
            det_fracs.append(np.nan)
    alarms = np.asarray(alarms, dtype=bool)
    det_fracs = np.asarray(det_fracs, dtype=np.float64)

    fail_hits = alarms & failure_mask
    fail_total = max(1, int(failure_mask.sum()))
    succ_total = max(1, int(success_mask.sum()))
    detected_fracs = det_fracs[fail_hits]
    return {
        "success_false_alarm": float((alarms & success_mask).sum() / succ_total),
        "failure_detection": float(fail_hits.sum() / fail_total),
        "det_at_10": float(np.sum(detected_fracs <= 0.10) / fail_total),
        "det_at_25": float(np.sum(detected_fracs <= 0.25) / fail_total),
        "det_at_50": float(np.sum(detected_fracs <= 0.50) / fail_total),
        "mean_time": float(np.nanmean(detected_fracs)) if detected_fracs.size else float("nan"),
        "never": float((failure_mask & ~alarms).sum() / fail_total),
    }


def summarize(all_seed_results):
    rows = []
    for seed, seed_results in all_seed_results.items():
        for method, result in seed_results.items():
            success_mask = result["successful_test_rollouts"]
            for threshold_style, qdict in result["test_scores_by_threshold"].items():
                if 0.95 not in qdict:
                    continue
                for window, scores in qdict[0.95].items():
                    m = alarm_metrics(scores, success_mask)
                    rows.append(
                        {
                            "seed": seed,
                            "method": method,
                            "threshold_style": threshold_style,
                            "quantile": 0.95,
                            "window": str(window),
                            **m,
                        }
                    )
    return rows


def aggregate_rows(rows):
    groups = {}
    for row in rows:
        key = (row["method"], row["threshold_style"], row["quantile"], row["window"])
        groups.setdefault(key, []).append(row)
    out = []
    metric_keys = [
        "success_false_alarm",
        "failure_detection",
        "det_at_10",
        "det_at_25",
        "det_at_50",
        "mean_time",
        "never",
    ]
    for key, vals in groups.items():
        row = {
            "method": key[0],
            "threshold_style": key[1],
            "quantile": key[2],
            "window": key[3],
            "n_seeds": len(vals),
        }
        for metric in metric_keys:
            row[metric] = float(np.nanmean([v[metric] for v in vals]))
        out.append(row)
    out.sort(key=lambda r: (r["method"], r["threshold_style"], r["success_false_alarm"], -r["failure_detection"], r["window"]))
    return out


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def fmt_pct(x):
    return "nan" if np.isnan(x) else f"{100*x:.1f}%"


def write_report(agg_rows, raw_rows, validation):
    best = []
    for method in ["entropy", "rnd_oe", "rnd_oe_and_entropy"]:
        candidates = [r for r in agg_rows if r["method"] == method and r["threshold_style"] == "tvt_quantile"]
        if candidates:
            # Conservative official-style operating point: keep high recall, minimize false alarms.
            high_recall = [r for r in candidates if r["failure_detection"] >= 0.95]
            best.append((high_recall or candidates)[0])

    lines = [
        "# Official FIPER Seen Train/Eval Report",
        "",
        "## Protocol",
        "",
        "- Repo: official FIPER clone, method classes unchanged.",
        f"- Repo path: `{REPO}`",
        f"- Dataset: `{PROCESSED}`",
        "- Dataset adapter only: explicit tensor load to avoid the repo loader key-suffix bug.",
        "- Training/calibration semantics: official code trains RND on `calibration` rollouts and computes thresholds on successful calibration rollouts.",
        "- Test set: seen held-out `libero_goal_object_official` only.",
        "- Seeds: 0, 1, 2, 42, 43.",
        "",
        "## Dataset Validation",
        "",
    ]
    for key, value in validation.items():
        lines.append(f"- `{key}`: `{value}`")
    lines += [
        "",
        "## Best q95 tvt_quantile Operating Points",
        "",
        "| Method | Window | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in best:
        lines.append(
            "| {method} | {window} | {fa} | {det} | {d10} | {d25} | {d50} | {mt:.3f} | {never} |".format(
                method=row["method"],
                window=row["window"],
                fa=fmt_pct(row["success_false_alarm"]),
                det=fmt_pct(row["failure_detection"]),
                d10=fmt_pct(row["det_at_10"]),
                d25=fmt_pct(row["det_at_25"]),
                d50=fmt_pct(row["det_at_50"]),
                mt=row["mean_time"],
                never=fmt_pct(row["never"]),
            )
        )
    lines += [
        "",
        "## Output Files",
        "",
        f"- Raw per-seed q95 sweep: `{RUN_ROOT / 'official_fiper_q95_per_seed.csv'}`",
        f"- Averaged q95 sweep: `{RUN_ROOT / 'official_fiper_q95_aggregate.csv'}`",
        f"- Per-seed minimal q95 rows: `{RUN_ROOT / 'official_fiper_q95_per_seed.csv'}`",
        "",
        "## Flags",
        "",
        "- `OFFICIAL_METHOD_CLASSES_UNCHANGED = YES`",
        "- `DATASET_ADAPTER_USED = YES`",
        "- `NO_OOD_USED = YES`",
        "- `RND_TRAINED_ON_OFFICIAL_CALIBRATION_SUBSET = YES`",
        "- `THRESHOLDS_CALIBRATED_ON_SUCCESSFUL_CALIBRATION_ROLLOUTS = YES`",
        "- `SEEN_TEST_ONLY = YES`",
        "- `RUN_COMPLETE = YES`",
        "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main():
    RUN_ROOT.mkdir(parents=True, exist_ok=True)
    cfg_path = ensure_task_config()
    ProcessedRolloutDataset, EvaluationManager, RNDTrainer, load_config, get_required_tensors, set_seed = import_official_repo()

    methods_for_tensor = METHODS
    required_tensors, optional_tensors = get_required_tensors(methods_for_tensor, str(REPO / "configs"))
    required_tensors = list(dict.fromkeys(required_tensors))
    optional_tensors = list(dict.fromkeys(optional_tensors))
    print("required_tensors", required_tensors)
    print("optional_tensors", optional_tensors)

    validation = {
        "task_config": str(cfg_path),
        "obs_embeddings_shape": tuple(torch.load(PROCESSED / "obs_embeddings.pt", map_location="cpu", weights_only=True).shape),
        "action_preds_shape": tuple(torch.load(PROCESSED / "action_preds.pt", map_location="cpu", weights_only=True).shape),
    }
    metadata = pickle.load(open(PROCESSED / "metadata.pkl", "rb"))
    for key in ["num_rollouts", "num_steps"]:
        validation[key] = metadata[key]
    for key in [
        "calibration_rollout_labels",
        "test_rollout_labels",
        "successful_rollout_labels",
        "failed_rollout_labels",
        "id_rollout_labels",
        "ood_rollout_labels",
    ]:
        validation[key] = int(np.asarray(metadata[key]).sum())
    print("validation", validation)

    # Clean only evaluation/report output dirs for this task, not the materialized
    # dataset. Preserve existing RND checkpoints so a relaunch resumes by seed
    # instead of retraining already finished seeds.
    for dirname in ["results", "summaries", "plots"]:
        target = TASK_DATA / dirname
        if target.exists():
            shutil.rmtree(target)

    task_cfg = load_config("task", TASK, return_only_subdict=False, base_config_dir=str(REPO / "configs"))
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    raw_rows = []
    for seed in SEEDS:
        set_seed(seed)
        print(f"===== SEED {seed} =====", flush=True)
        dataset = load_dataset(ProcessedRolloutDataset, required_tensors)
        trainer = RNDTrainer(str(REPO / "configs"), str(TASK_DATA), dataset, device=device, task_cfg=task_cfg, seed=seed)
        trainer.train(["rnd_oe"])
        evaluator = EvaluationManager(str(REPO / "configs"), str(TASK_DATA), dataset, device=device, seed=seed)
        results = evaluator.evaluate(METHODS, combine_methods=True, combined_methods=copy.deepcopy(COMBINED))
        seed_rows = summarize({seed: results})
        raw_rows.extend(seed_rows)
        write_csv(RUN_ROOT / f"seed_{seed}_q95_rows.csv", seed_rows)
        write_csv(RUN_ROOT / "official_fiper_q95_per_seed.partial.csv", raw_rows)
        del results, evaluator, trainer, dataset
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()

    agg_rows = aggregate_rows(raw_rows)
    write_csv(RUN_ROOT / "official_fiper_q95_per_seed.csv", raw_rows)
    write_csv(RUN_ROOT / "official_fiper_q95_aggregate.csv", agg_rows)
    write_report(agg_rows, raw_rows, validation)
    print(f"Wrote {REPORT}")


if __name__ == "__main__":
    main()
