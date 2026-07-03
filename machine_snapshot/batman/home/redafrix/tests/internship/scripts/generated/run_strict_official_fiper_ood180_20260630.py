#!/usr/bin/env python3
import json
import os
import pickle
import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import yaml


FIPER_DIR = Path("/home/dean/fiper_uncertainty_collection/external/fiper_official_clean_20260630")
SRC_PROCESSED = Path(
    "/home/dean/fiper_uncertainty_collection/experiments/"
    "official_fiper_goal_object_ood_ablation_20260625/official_fiper_data/"
    "libero_fold00/processed_rollouts"
)
EXP_DIR = Path("/home/dean/fiper_uncertainty_collection/experiments/strict_official_fiper_ood180_20260630")
TASK = "libero_fold00"
SEEDS = [0, 1, 2, 42, 43]
METHODS = ["entropy", "rnd_oe"]
COMBINED = {1: {"m1": {"name": "rnd_oe"}, "m2": {"name": "entropy"}, "operation": "and"}}


def fail(msg: str) -> None:
    raise RuntimeError(msg)


def install_task_config() -> None:
    cfg_path = FIPER_DIR / "configs" / "task" / f"{TASK}.yaml"
    cfg_path.parent.mkdir(parents=True, exist_ok=True)
    cfg = {
        "defaults": ["base"],
        "name": TASK,
        "description": "Strict official FIPER adapter for LIBERO goal_object seen calibration and goal_object_ood test",
        "type": "simulation",
        "environment": {
            "ts": 0.1,
            "max_episode_steps": 300,
            "fail_on_error": True,
            "fail_after_steps": 300,
        },
        "action_space": {
            "action_type": "continuous",
            "actions": {
                "dim": 7,
                "action_bounds": {"low": -1.0, "high": 1.0},
                "action_mapping": {"position": [0, 1, 2], "rotation": [3, 4, 5], "gripper": [6]},
            },
            "action_pred": {
                "format": "(batch_size, prediction_horizon, action_dim)",
                "shape": "(9, 10, 7)",
                "action_prediction_horizon": 10,
            },
            "action_execution_horizon": 1,
        },
    }
    cfg_path.write_text(yaml.safe_dump(cfg, sort_keys=False))


def patch_official_loader_runtime():
    """Keep repo files clean; fix only the official .pt key-loading bug at runtime."""
    from datasets.rollout_datasets import ProcessedRolloutDataset
    from shared_utils.data_management import load_data

    def load_dataset_fixed(self, load_dir=None, optional_tensors_required=None, weights_only=True):
        if optional_tensors_required is None:
            optional_tensors_required = []
        self.dataset_loaded = True
        tensors_required = list(set(optional_tensors_required + self.required_tensors))
        if load_dir is None:
            load_dir = self.save_dir
        if not self._dataset_exists(save_dir=load_dir, tensors_required=tensors_required):
            self.dataset_loaded = False
            return

        data = {}
        data["metadata"] = load_data(load_dirs=load_dir, keywords="metadata", data_types="pkl")
        for tensor_keyword in tensors_required:
            filename_keyword = (
                tensor_keyword + ".pt"
                if (not tensor_keyword.endswith(".pt") and not tensor_keyword.endswith("."))
                else tensor_keyword
            )
            tensor = load_data(
                load_dirs=load_dir,
                keywords=filename_keyword,
                data_types="pt",
                weights_only=weights_only,
                error_if_not_found=True,
            )
            data[tensor_keyword.removesuffix(".pt")] = tensor
        self.data = data
        try:
            self.normalizer = load_data(load_dirs=load_dir, keywords="normalizer", data_types=["pkl"])
        except Exception:
            self.normalizer = None

    ProcessedRolloutDataset.load_dataset = load_dataset_fixed


def prepare_repo_and_data() -> Path:
    if not FIPER_DIR.exists():
        fail(f"missing clean FIPER repo: {FIPER_DIR}")
    if not SRC_PROCESSED.exists():
        fail(f"missing processed dataset: {SRC_PROCESSED}")

    install_task_config()

    data_task = FIPER_DIR / "data" / TASK
    data_task.mkdir(parents=True, exist_ok=True)
    dst = data_task / "processed_rollouts"
    if dst.exists() or dst.is_symlink():
        if dst.is_symlink():
            dst.unlink()
        else:
            shutil.rmtree(dst)
    dst.symlink_to(SRC_PROCESSED, target_is_directory=True)

    for sub in ["rnd_models", "results", "rnd_training_data"]:
        p = data_task / sub
        if p.exists():
            shutil.rmtree(p)

    EXP_DIR.mkdir(parents=True, exist_ok=True)
    return data_task


def validate_dataset(dataset) -> dict:
    meta = dataset.data["metadata"]
    obs = dataset.data["obs_embeddings"]
    act = dataset.data["action_preds"]
    calib = np.asarray(meta["calibration_rollout_labels"], dtype=bool)
    test = np.asarray(meta["test_rollout_labels"], dtype=bool)
    succ = np.asarray(meta["successful_rollout_labels"], dtype=bool)
    oid = np.asarray(meta["ood_rollout_labels"], dtype=bool)
    iid = np.asarray(meta["id_rollout_labels"], dtype=bool)

    checks = {
        "num_rollouts": int(meta["num_rollouts"]),
        "num_steps": int(meta["num_steps"]),
        "obs_shape": list(obs.shape),
        "action_shape": list(act.shape),
        "calibration_rollouts": int(calib.sum()),
        "test_rollouts": int(test.sum()),
        "calibration_success": int((calib & succ).sum()),
        "calibration_failure": int((calib & ~succ).sum()),
        "calibration_id": int((calib & iid).sum()),
        "calibration_ood": int((calib & oid).sum()),
        "test_success": int((test & succ).sum()),
        "test_failure": int((test & ~succ).sum()),
        "test_id": int((test & iid).sum()),
        "test_ood": int((test & oid).sum()),
        "calibration_test_overlap": int((calib & test).sum()),
        "id_ood_overlap": int((iid & oid).sum()),
        "obs_finite": bool(torch.isfinite(obs).all().item()),
        "actions_finite": bool(torch.isfinite(act).all().item()),
    }

    expected = {
        "num_rollouts": 830,
        "calibration_rollouts": 150,
        "test_rollouts": 180,
        "calibration_success": 150,
        "calibration_failure": 0,
        "calibration_id": 150,
        "calibration_ood": 0,
        "test_id": 0,
        "test_ood": 180,
        "calibration_test_overlap": 0,
        "id_ood_overlap": 0,
        "obs_finite": True,
        "actions_finite": True,
    }
    for k, v in expected.items():
        if checks[k] != v:
            fail(f"dataset validation failed for {k}: got {checks[k]} expected {v}")
    if tuple(obs.shape[1:]) != (960,):
        fail(f"bad obs shape {obs.shape}")
    if tuple(act.shape[1:]) != (9, 10, 7):
        fail(f"bad action_preds shape {act.shape}")
    return checks


def custom_metrics(ep_scores, success_mask, episode_lengths, threshold=1.0, cap300=False):
    success_mask = np.asarray(success_mask, dtype=bool)
    lengths = np.asarray(episode_lengths, dtype=int)
    detected = []
    first_steps = []
    for scores, length in zip(ep_scores, lengths):
        arr = np.asarray(scores, dtype=float)
        if cap300:
            arr = arr[: min(len(arr), 300)]
        above = arr > threshold
        found = bool(np.any(above))
        detected.append(found)
        first_steps.append(int(np.where(above)[0][0]) if found else None)

    detected = np.asarray(detected, dtype=bool)
    sidx = np.where(success_mask)[0]
    fidx = np.where(~success_mask)[0]
    success_fa = float(detected[sidx].mean()) if len(sidx) else 0.0
    failure_det = float(detected[fidx].mean()) if len(fidx) else 0.0

    det_counts = {10: 0, 25: 0, 50: 0}
    det_times = []
    for i in fidx:
        if not detected[i]:
            continue
        denom = min(lengths[i], 300) if cap300 else lengths[i]
        denom = max(1, int(denom))
        frac = (first_steps[i] + 1) / denom
        det_times.append(frac)
        for pct in det_counts:
            if frac <= pct / 100.0:
                det_counts[pct] += 1
    nf = len(fidx)
    return {
        "Success FA": 100.0 * success_fa,
        "Failure Det": 100.0 * failure_det,
        "Det@10": 100.0 * det_counts[10] / nf if nf else 0.0,
        "Det@25": 100.0 * det_counts[25] / nf if nf else 0.0,
        "Det@50": 100.0 * det_counts[50] / nf if nf else 0.0,
        "Mean Time": float(np.mean(det_times)) if det_times else 1.0,
        "Never": 100.0 * (1.0 - failure_det),
    }


def collect_result_rows(raw_by_seed, dataset):
    meta = dataset.data["metadata"]
    test_mask_full = np.asarray(meta["test_rollout_labels"], dtype=bool)
    ood_test_mask = np.asarray(raw_by_seed[SEEDS[0]]["entropy"]["ood_test_rollouts"], dtype=bool)
    success_test_mask = np.asarray(raw_by_seed[SEEDS[0]]["entropy"]["successful_test_rollouts"], dtype=bool)
    lengths_test_all = np.asarray(meta["episode_lengths"], dtype=int)[test_mask_full]

    rows = []
    for seed, seed_res in raw_by_seed.items():
        for method_name, res in seed_res.items():
            for threshold_style, qdict in res["test_scores_by_threshold"].items():
                for q, wdict in qdict.items():
                    for window, scores_all in wdict.items():
                        scores = [s for s, is_ood in zip(scores_all, ood_test_mask) if is_ood]
                        succ = success_test_mask[ood_test_mask]
                        lengths = lengths_test_all[ood_test_mask]
                        m = custom_metrics(scores, succ, lengths, threshold=1.0, cap300=False)
                        mc = custom_metrics(scores, succ, lengths, threshold=1.0, cap300=True)
                        rows.append({
                            "seed": seed,
                            "method": method_name,
                            "threshold_style": threshold_style,
                            "quantile": float(q),
                            "window": str(window),
                            "cap300": False,
                            **m,
                        })
                        rows.append({
                            "seed": seed,
                            "method": method_name,
                            "threshold_style": threshold_style,
                            "quantile": float(q),
                            "window": str(window),
                            "cap300": True,
                            **mc,
                        })
    df = pd.DataFrame(rows)
    avg = (
        df.groupby(["method", "threshold_style", "quantile", "window", "cap300"], as_index=False)
        [["Success FA", "Failure Det", "Det@10", "Det@25", "Det@50", "Mean Time", "Never"]]
        .mean()
    )
    return df, avg


def write_report(validation, avg):
    official_rows = avg[
        (avg["threshold_style"] == "tvt_quantile")
        & (avg["quantile"] == 0.95)
        & (
            ((avg["method"] == "entropy") & (avg["window"] == "29"))
            | ((avg["method"] == "rnd_oe") & (avg["window"] == "48"))
            | ((avg["method"] == "rnd_oe_and_entropy") & (avg["window"] == "48/16"))
        )
    ].sort_values(["cap300", "method"])
    best_twa_proxy = avg[(avg["cap300"] == True)].copy()
    best_twa_proxy["balanced"] = (100.0 - best_twa_proxy["Success FA"] + best_twa_proxy["Failure Det"]) / 2.0
    best = best_twa_proxy.sort_values(["method", "balanced"], ascending=[True, False]).groupby("method").head(5)

    lines = []
    lines.append("# Strict Official FIPER OOD180 Audit (2026-06-30)")
    lines.append("")
    lines.append("This run uses a fresh GitHub clone of `learnsyslab/fiper` at commit `13d79c5c3069def843e454787ff128defc249838`.")
    lines.append("Only runtime compatibility is applied: the processed `.pt` loader key bug is monkeypatched in the runner without modifying repo files.")
    lines.append("")
    lines.append("## Non-Leakage Dataset Validation")
    lines.append("```json")
    lines.append(json.dumps(validation, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("Critical flags: calibration contains 150 seen successes, 0 failures, 0 OOD. Test contains 180 OOD rollouts only.")
    lines.append("")
    lines.append("## Fixed q95/tvt_quantile Reference Rows")
    lines.append("```text")
    lines.append(official_rows.to_string(index=False))
    lines.append("```")
    lines.append("")
    lines.append("## Top Diagnostic Rows by Balanced Score (cap300, not calibration)")
    lines.append("```text")
    lines.append(best.to_string(index=False))
    lines.append("```")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("- RND-OE is trained from scratch by official `RNDTrainer` on the calibration subset only.")
    lines.append("- FIPER thresholds are produced by official `BaseEvalClass` from successful calibration rollouts only.")
    lines.append("- OOD test labels are used only after scoring to compute metrics and diagnostic tables.")
    lines.append("- Any threshold/window sweep rows are diagnostic analysis, not OOD calibration.")
    (EXP_DIR / "STRICT_OFFICIAL_FIPER_AUDIT_REPORT.md").write_text("\\n".join(lines))


def main():
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    os.chdir(FIPER_DIR)
    sys.path.insert(0, str(FIPER_DIR))
    patch_official_loader_runtime()

    from tasks import TaskManager
    from rnd import RNDTrainer
    from evaluation import EvaluationManager
    from shared_utils.hydra_utils import load_config
    from shared_utils.utility_functions import get_required_tensors, set_seed

    data_task = prepare_repo_and_data()
    cfg = load_config("task", TASK, return_only_subdict=False)
    required_tensors, optional_tensors = get_required_tensors(METHODS, str(FIPER_DIR / "configs"))
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(f"[setup] device={device}", flush=True)
    print(f"[setup] required_tensors={required_tensors} optional={optional_tensors}", flush=True)

    taskmanager = TaskManager(
        cfg,
        TASK,
        str(FIPER_DIR / "configs"),
        str(data_task),
        required_tensors=required_tensors,
        optional_tensors=optional_tensors,
        device=device,
    )
    dataset = taskmanager.get_rollout_dataset(load_dataset_if_exists=True)
    validation = validate_dataset(dataset)
    (EXP_DIR / "DATASET_VALIDATION.json").write_text(json.dumps(validation, indent=2))
    print("[validation] PASS", json.dumps(validation, indent=2), flush=True)

    raw_by_seed = {}
    for seed in SEEDS:
        print(f"[seed {seed}] training official RND-OE from calibration only", flush=True)
        set_seed(seed)
        trainer = RNDTrainer(str(FIPER_DIR / "configs"), str(data_task), dataset, device=device, seed=seed, task_cfg=cfg)
        trainer.train(["rnd_oe"])

        print(f"[seed {seed}] evaluating official entropy + rnd_oe + AND fusion", flush=True)
        set_seed(seed)
        evaluator = EvaluationManager(str(FIPER_DIR / "configs"), str(data_task), dataset, device=device, seed=seed)
        res = evaluator.evaluate(METHODS, combine_methods=True, combined_methods=COMBINED)
        raw_by_seed[seed] = res

    with (EXP_DIR / "raw_results_by_seed.pkl").open("wb") as f:
        pickle.dump(raw_by_seed, f)
    per_seed, avg = collect_result_rows(raw_by_seed, dataset)
    per_seed.to_csv(EXP_DIR / "strict_official_fiper_per_seed_all_grid.csv", index=False)
    avg.to_csv(EXP_DIR / "strict_official_fiper_avg_all_grid.csv", index=False)
    write_report(validation, avg)
    print(f"[done] wrote {EXP_DIR}", flush=True)


if __name__ == "__main__":
    main()
