import os
import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch


ROOT_DIR = "/home/dean/fiper_uncertainty_collection/external/fiper"
sys.path.insert(0, ROOT_DIR)
os.chdir(ROOT_DIR)

from evaluation import EvaluationManager  # noqa: E402
from shared_utils.hydra_utils import load_config  # noqa: E402
from shared_utils.utility_functions import get_required_tensors, set_seed  # noqa: E402
from tasks import TaskManager  # noqa: E402


TASK = "libero_fold00"
EXP_DIR = Path("/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625")
SRC_PROCESSED = EXP_DIR / "official_fiper_data" / TASK / "processed_rollouts"
OUT_DIR = EXP_DIR / "threshold_sweep_ood180_cap300_20260629"
SEEDS = [0, 1, 2, 42, 43]
METHODS = ["entropy", "rnd_oe"]
COMBINED = {1: {"m1": {"name": "rnd_oe"}, "m2": {"name": "entropy"}, "operation": "and"}}


def metrics_from_first_alarm(detected, first_alarm_steps, success_mask, episode_lengths):
    success_idx = np.where(success_mask)[0]
    failure_idx = np.where(~success_mask)[0]

    success_fa = float(np.mean([detected[i] for i in success_idx])) if len(success_idx) else 0.0
    failure_det = float(np.mean([detected[i] for i in failure_idx])) if len(failure_idx) else 0.0
    never = 1.0 - failure_det

    det_10 = det_25 = det_50 = 0
    det_times = []
    for i in failure_idx:
        if not detected[i]:
            continue
        frac = (first_alarm_steps[i] + 1) / max(1, int(episode_lengths[i]))
        det_times.append(frac)
        det_10 += int(frac <= 0.10)
        det_25 += int(frac <= 0.25)
        det_50 += int(frac <= 0.50)

    n_fail = len(failure_idx)
    return {
        "Success FA": success_fa,
        "Failure Det": failure_det,
        "Det@10": det_10 / n_fail if n_fail else 0.0,
        "Det@25": det_25 / n_fail if n_fail else 0.0,
        "Det@50": det_50 / n_fail if n_fail else 0.0,
        "Mean Time": float(np.mean(det_times)) if det_times else 1.0,
        "Never": never,
    }


def eval_any_score(ep_scores, threshold, success_mask, episode_lengths):
    detected = []
    first_alarm_steps = []
    for scores in ep_scores:
        arr = np.asarray(scores, dtype=np.float64)
        hits = np.flatnonzero(arr >= threshold)
        detected.append(bool(len(hits)))
        first_alarm_steps.append(int(hits[0]) if len(hits) else None)
    return metrics_from_first_alarm(detected, first_alarm_steps, success_mask, episode_lengths)


def eval_mass(ep_scores, row_threshold, mass_threshold, success_mask, episode_lengths):
    detected = []
    first_alarm_steps = []
    for scores in ep_scores:
        mass = 0.0
        first = None
        for i, score in enumerate(scores):
            mass += max(0.0, float(score) - row_threshold)
            if mass >= mass_threshold:
                first = i
                break
        detected.append(first is not None)
        first_alarm_steps.append(first)
    return metrics_from_first_alarm(detected, first_alarm_steps, success_mask, episode_lengths)


def pct(x):
    return 100.0 * float(x)


def main():
    CAP_STEPS = 300
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    task_data_path = Path(ROOT_DIR) / "data" / TASK
    dst_processed = task_data_path / "processed_rollouts"
    if not SRC_PROCESSED.exists():
        raise FileNotFoundError(SRC_PROCESSED)
    if dst_processed.exists() or dst_processed.is_symlink():
        if dst_processed.is_symlink():
            dst_processed.unlink()
        else:
            shutil.rmtree(dst_processed)
    task_data_path.mkdir(parents=True, exist_ok=True)
    dst_processed.symlink_to(SRC_PROCESSED, target_is_directory=True)

    cfg = load_config("task", TASK, return_only_subdict=False)
    required_tensors, optional_tensors = get_required_tensors(METHODS, str(Path(ROOT_DIR) / "configs"))
    device = "cuda" if torch.cuda.is_available() else "cpu"

    taskmanager = TaskManager(
        cfg,
        TASK,
        str(Path(ROOT_DIR) / "configs"),
        str(task_data_path),
        required_tensors=required_tensors,
        optional_tensors=optional_tensors,
        device=device,
    )
    dataset = taskmanager.get_rollout_dataset(load_dataset_if_exists=True)

    save_dir = task_data_path / "rnd_models" / "rnd_oe"
    ckpts = list(save_dir.glob("*.ckpt"))
    missing = []
    for seed in SEEDS:
        found = False
        for ckpt_path in ckpts:
            try:
                ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
                if ckpt.get("cfg", {}).get("hparams", {}).get("seed") == seed:
                    found = True
                    break
            except Exception:
                pass
        if not found:
            missing.append(seed)
    if missing:
        raise RuntimeError(f"Missing pre-trained RND checkpoints for seeds {missing}")

    raw_by_seed = {}
    seed0 = None
    for seed in SEEDS:
        print(f"[eval] seed={seed}", flush=True)
        set_seed(seed)
        manager = EvaluationManager(str(Path(ROOT_DIR) / "configs"), str(task_data_path), dataset, device=device, seed=seed)
        if seed == 0:
            seed0 = manager.evaluate(METHODS, True, COMBINED)
            raw_by_seed[seed] = seed0
        else:
            seed_res = manager.evaluate(["rnd_oe"], combine_methods=False)
            seed_res["entropy"] = seed0["entropy"]
            seed_res = manager._combine_two_methods(COMBINED[1], seed_res)
            raw_by_seed[seed] = seed_res

    any_res = raw_by_seed[0]["entropy"]
    ood_mask = np.asarray(any_res["ood_test_rollouts"], dtype=bool)
    success_all = np.asarray(any_res["successful_test_rollouts"], dtype=bool)
    orig_success_mask = success_all[ood_mask]
    episode_lengths_all = np.asarray(dataset.data["metadata"]["episode_lengths"])[dataset.data["metadata"]["test_rollout_labels"]]
    orig_episode_lengths = episode_lengths_all[ood_mask]
    success_mask = orig_success_mask & (orig_episode_lengths <= CAP_STEPS)
    episode_lengths = np.minimum(orig_episode_lengths, CAP_STEPS)

    method_specs = {
        "entropy": {"window": 29, "quantile": 0.95},
        "rnd_oe": {"window": 48, "quantile": 0.95},
        "rnd_oe_and_entropy": {"window": "48/16", "quantile": 0.95},
    }
    any_thresholds = [1, 1.25, 1.5, 2, 3, 5, 10, 20, 50, 100]
    mass_thresholds = [0.15, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]

    rows = []
    for method, spec in method_specs.items():
        for policy_kind, thresholds in [("any", any_thresholds), ("mass_above_1", mass_thresholds)]:
            per_threshold_seed_metrics = {th: [] for th in thresholds}
            for seed in SEEDS:
                res = raw_by_seed[seed][method]
                ep_scores_all = res["test_scores_by_threshold"]["tvt_quantile"][spec["quantile"]][spec["window"]]
                ep_scores = [np.asarray(scores, dtype=np.float64)[:CAP_STEPS] for scores, is_ood in zip(ep_scores_all, ood_mask) if is_ood]
                for th in thresholds:
                    if policy_kind == "any":
                        m = eval_any_score(ep_scores, th, success_mask, episode_lengths)
                    else:
                        m = eval_mass(ep_scores, 1.0, th, success_mask, episode_lengths)
                    per_threshold_seed_metrics[th].append(m)

            for th, seed_metrics in per_threshold_seed_metrics.items():
                avg = {k: float(np.mean([m[k] for m in seed_metrics])) for k in seed_metrics[0]}
                rows.append({
                    "Method": method,
                    "Policy": f"{policy_kind}_{th:g}",
                    "Threshold": th,
                    "Success FA": pct(avg["Success FA"]),
                    "Failure Det": pct(avg["Failure Det"]),
                    "Det@10": pct(avg["Det@10"]),
                    "Det@25": pct(avg["Det@25"]),
                    "Det@50": pct(avg["Det@50"]),
                    "Mean Time": avg["Mean Time"],
                    "Never": pct(avg["Never"]),
                })

    df = pd.DataFrame(rows)
    csv_path = OUT_DIR / "official_fiper_ood180_cap300_threshold_sweep.csv"
    df.to_csv(csv_path, index=False)

    lines = []
    lines.append("# Official FIPER OOD180 Cap-300 Threshold Sweep")
    lines.append("")
    lines.append("- No retrain.")
    lines.append("- Reuses official FIPER RND checkpoints already trained on in-domain data.")
    lines.append(f"- OOD test set only: 180 episodes. Cap-300 relabel: success only if original success length <= {CAP_STEPS}; any episode reaching/exceeding cap is failure.")
    lines.append("- Scores are official FIPER `tvt_quantile` q=0.95 normalized scores truncated to first 300 steps; official deployment point is `any_1`.")
    lines.append("- `mass_above_1_M` accumulates `max(0, normalized_score - 1.0)` and alarms when cumulative mass reaches `M`; this is an OOD operating-curve diagnostic, not the unchanged paper deployment rule.")
    lines.append(f"- Cap-300 labels: {int(success_mask.sum())} successes / {int((~success_mask).sum())} failures.")
    lines.append("")
    for method in method_specs:
        sub = df[df["Method"] == method].copy()
        lines.append(f"## {method}")
        lines.append("")
        lines.append(sub.to_markdown(index=False, floatfmt=".3f"))
        lines.append("")

    report_path = OUT_DIR / "OFFICIAL_FIPER_OOD180_CAP300_THRESHOLD_SWEEP_20260629.md"
    report_path.write_text("\n".join(lines) + "\n")
    print(f"WROTE {csv_path}")
    print(f"WROTE {report_path}")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
