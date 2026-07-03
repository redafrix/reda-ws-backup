import sys
import os
import shutil
import pickle
import numpy as np
import torch
import pandas as pd
import copy
from pathlib import Path

ROOT_DIR = "/home/dean/fiper_uncertainty_collection/external/fiper"
sys.path.insert(0, ROOT_DIR)
os.chdir(ROOT_DIR)

from tasks import TaskManager
from evaluation import EvaluationManager
from shared_utils.hydra_utils import load_config
from shared_utils.utility_functions import get_required_tensors, set_seed

class ForensicEvaluationManager(EvaluationManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def _load_config(self, method_name: str = "base"):
        cfg = super()._load_config(method_name)
        return cfg

def calculate_metrics_style_baseline(detected, first_alarm_steps, success_mask, episode_lengths):
    success_indices = np.where(success_mask == True)[0]
    failure_indices = np.where(success_mask == False)[0]
    
    success_alarms = [detected[idx] for idx in success_indices]
    success_fa = np.mean(success_alarms) if len(success_alarms) > 0 else 0.0
    
    failure_alarms = [detected[idx] for idx in failure_indices]
    failure_det = np.mean(failure_alarms) if len(failure_alarms) > 0 else 0.0
    
    never_det = 1.0 - failure_det
    
    det_10 = 0
    det_25 = 0
    det_50 = 0
    det_times = []
    
    for idx in failure_indices:
        if detected[idx]:
            step = first_alarm_steps[idx]
            length = episode_lengths[idx]
            n = max(1, length)
            frac = (step + 1) / n
            det_times.append(frac)
            
            if frac <= 0.10:
                det_10 += 1
            if frac <= 0.25:
                det_25 += 1
            if frac <= 0.50:
                det_50 += 1
                
    n_failures = len(failure_indices)
    det_10_rate = det_10 / n_failures if n_failures > 0 else 0.0
    det_25_rate = det_25 / n_failures if n_failures > 0 else 0.0
    det_50_rate = det_50 / n_failures if n_failures > 0 else 0.0
    mean_time = np.mean(det_times) if len(det_times) > 0 else 0.0
    
    return {
        "Success FA": success_fa,
        "Failure Det": failure_det,
        "Det@10": det_10_rate,
        "Det@25": det_25_rate,
        "Det@50": det_50_rate,
        "Mean Time": mean_time,
        "Never": never_det
    }

def calculate_metrics_style_forensic(detected, first_alarm_steps, success_mask, episode_lengths):
    success_indices = np.where(success_mask == True)[0]
    failure_indices = np.where(success_mask == False)[0]
    
    success_alarms = [detected[idx] for idx in success_indices]
    success_fa = np.mean(success_alarms) if len(success_alarms) > 0 else 0.0
    
    failure_alarms = [detected[idx] for idx in failure_indices]
    failure_det = np.mean(failure_alarms) if len(failure_alarms) > 0 else 0.0
    
    never_det = 1.0 - failure_det
    
    det_10 = 0
    det_25 = 0
    det_50 = 0
    det_times = []
    
    for idx in failure_indices:
        if detected[idx]:
            step = first_alarm_steps[idx]
            length = episode_lengths[idx]
            denom_capped = min(length, 300)
            frac_capped = step / (denom_capped - 1) if denom_capped > 1 else 0.0
            det_times.append(frac_capped)
            
            if frac_capped <= 0.10:
                det_10 += 1
            if frac_capped <= 0.25:
                det_25 += 1
            if frac_capped <= 0.50:
                det_50 += 1
                
    n_failures = len(failure_indices)
    det_10_rate = det_10 / n_failures if n_failures > 0 else 0.0
    det_25_rate = det_25 / n_failures if n_failures > 0 else 0.0
    det_50_rate = det_50 / n_failures if n_failures > 0 else 0.0
    mean_time = np.mean(det_times) if len(det_times) > 0 else 0.0
    
    return {
        "Success FA": success_fa,
        "Failure Det": failure_det,
        "Det@10": det_10_rate,
        "Det@25": det_25_rate,
        "Det@50": det_50_rate,
        "Mean Time": mean_time,
        "Never": never_det
    }

def main():
    task = "libero_fold00"
    methods = ["entropy", "rnd_oe"]
    combine_methods = True
    combined_methods = {
        1: {"m1": {"name": "rnd_oe"}, "m2": {"name": "entropy"}, "operation": "and"}
    }
    
    base_config_path = os.path.join(ROOT_DIR, "configs")
    base_data_path = os.path.join(ROOT_DIR, "data")
    task_data_path = os.path.join(base_data_path, task)
    
    # 1. Symlink processed_rollouts to the task data directory
    exp_dir = Path("/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625")
    src_processed = exp_dir / "official_fiper_data" / "libero_fold00" / "processed_rollouts"
    dst_processed = Path(task_data_path) / "processed_rollouts"
    
    if dst_processed.exists() or dst_processed.is_symlink():
        if dst_processed.is_symlink():
            dst_processed.unlink()
        else:
            shutil.rmtree(dst_processed)
    Path(task_data_path).mkdir(parents=True, exist_ok=True)
    dst_processed.symlink_to(src_processed, target_is_directory=True)
    print(f"Linked {dst_processed} -> {src_processed}", flush=True)

    cfg = load_config("task", task, return_only_subdict=False)
    required_tensors, optional_tensors = get_required_tensors(methods, base_config_path)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    taskmanager = TaskManager(
        cfg,
        task,
        base_config_path,
        task_data_path,
        required_tensors=required_tensors,
        optional_tensors=optional_tensors,
        device=device,
    )
    dataset = taskmanager.get_rollout_dataset(load_dataset_if_exists=True)
    
    # Reuse already-trained official FIPER RND checkpoints. Do not retrain here:
    # this ablation is strictly an OOD test of the original FIPER method on a
    # newly materialized dataset.
    seeds = [0, 1, 2, 42, 43]
    save_dir = os.path.join(task_data_path, "rnd_models", "rnd_oe")
    ckpt_files = [f for f in os.listdir(save_dir) if f.endswith(".ckpt")] if os.path.exists(save_dir) else []
    for seed in seeds:
        found = False
        for f in ckpt_files:
            try:
                ckpt = torch.load(os.path.join(save_dir, f), map_location="cpu", weights_only=False)
                if ckpt.get("cfg", {}).get("hparams", {}).get("seed") == seed:
                    found = True
                    break
            except Exception:
                continue
        if not found:
            raise FileNotFoundError(f"Missing pre-trained official FIPER rnd_oe checkpoint for seed {seed} in {save_dir}")
    print(f"Reusing {len(ckpt_files)} pre-trained rnd_oe checkpoint files from {save_dir}", flush=True)

    # Prevent stale eval caches from an older processed_rollouts symlink.
    results_dir = os.path.join(task_data_path, "results")
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
        print(f"Removed stale evaluation cache: {results_dir}", flush=True)

    print("\n--- Starting Evaluation ---", flush=True)
    raw_results_by_seed = {}
    seed_0_results = None
    
    for seed in seeds:
        print(f"Evaluating Seed {seed}...", flush=True)
        set_seed(seed)
        evaluationmanager = ForensicEvaluationManager(base_config_path, task_data_path, dataset, device=device, seed=seed)
        if seed == 0:
            seed_0_results = evaluationmanager.evaluate(methods, combine_methods, combined_methods)
            raw_results_by_seed[seed] = seed_0_results
        else:
            seed_results = evaluationmanager.evaluate(["rnd_oe"], combine_methods=False)
            seed_results["entropy"] = seed_0_results["entropy"]
            seed_results = evaluationmanager._combine_two_methods(combined_methods[1], seed_results)
            raw_results_by_seed[seed] = seed_results

    any_result = raw_results_by_seed[0]["entropy"]
    ood_mask = any_result["ood_test_rollouts"]
    successful_mask = any_result["successful_test_rollouts"]
    
    # Load all episode lengths and keys of test split
    episode_lengths_all = np.array(dataset.data["metadata"]["episode_lengths"])[dataset.data["metadata"]["test_rollout_labels"]]
    episode_keys_all = np.array(dataset.data["metadata"]["episode_keys"])[dataset.data["metadata"]["test_rollout_labels"]]
    
    # We evaluate strictly on the OOD test split (all 180 episodes)
    success_mask_split = successful_mask[ood_mask]
    episode_lengths_split = episode_lengths_all[ood_mask]
    episode_keys_split = episode_keys_all[ood_mask]
    
    methods_to_report = ["entropy", "rnd_oe", "rnd_oe_and_entropy"]
    window_settings = {
        "entropy": 29,
        "rnd_oe": 48,
        "rnd_oe_and_entropy": "48/16"
    }

    all_metrics = []
    
    for m_name in methods_to_report:
        w_size = window_settings[m_name]
        
        # We will average the raw scores over seeds for RND if seed-varying
        # But wait, we can compute metrics for each seed and average them, same style as FIPER verified splits
        seed_metrics_baseline = []
        seed_metrics_forensic = []
        
        for seed in seeds:
            res = raw_results_by_seed[seed][m_name]
            # Get step-wise scores scaled by threshold
            scores = res["test_scores_by_threshold"]["tvt_quantile"][0.95][w_size]
            # Select only OOD test episodes
            split_scores = [s for s, is_ood in zip(scores, ood_mask) if is_ood]
            
            # Determine detection for each episode (score > 1.0)
            detected = []
            first_alarm_steps = []
            for ep_scores in split_scores:
                scores_above = np.array(ep_scores) > 1.0
                has_alarm = np.any(scores_above)
                detected.append(has_alarm)
                if has_alarm:
                    first_alarm_steps.append(np.where(scores_above)[0][0])
                else:
                    first_alarm_steps.append(None)
            
            metrics_b = calculate_metrics_style_baseline(detected, first_alarm_steps, success_mask_split, episode_lengths_split)
            metrics_f = calculate_metrics_style_forensic(detected, first_alarm_steps, success_mask_split, episode_lengths_split)
            
            seed_metrics_baseline.append(metrics_b)
            seed_metrics_forensic.append(metrics_f)
            
        # Average metrics across seeds
        avg_b = {}
        for k in seed_metrics_baseline[0].keys():
            avg_b[k] = np.mean([sm[k] for sm in seed_metrics_baseline])
            
        avg_f = {}
        for k in seed_metrics_forensic[0].keys():
            avg_f[k] = np.mean([sm[k] for sm in seed_metrics_forensic])
            
        all_metrics.append({
            "Method": m_name,
            "Window": str(w_size),
            "Style": "Baseline (actual steps)",
            **avg_b
        })
        all_metrics.append({
            "Method": m_name,
            "Window": str(w_size),
            "Style": "FIPER Forensic (max 300 steps)",
            **avg_f
        })
        
    df = pd.DataFrame(all_metrics)
    print("\n=== FINAL ABLATION RESULTS ON OOD DATASET ===")
    print(df.to_string(index=False))
    
    # Save results to csv in exp_dir
    results_path = exp_dir / "official_fiper_ablation_results.csv"
    df.to_csv(results_path, index=False)
    print(f"Saved results to {results_path}", flush=True)

if __name__ == "__main__":
    main()
