import sys
import os
import shutil
import pickle
import numpy as np
import torch
import pandas as pd
import copy

ROOT_DIR = "/home/dean/fiper_uncertainty_collection/external/fiper"
sys.path.insert(0, ROOT_DIR)
os.chdir(ROOT_DIR)

from tasks import TaskManager
from evaluation import EvaluationManager
from shared_utils.hydra_utils import load_config
from shared_utils.utility_functions import get_required_tensors, set_seed

class ForensicEvaluationManager(EvaluationManager):
    def __init__(self, *args, is_option_a=False, **kwargs):
        self.is_option_a = is_option_a
        super().__init__(*args, **kwargs)
        
    def _load_config(self, method_name: str = "base"):
        cfg = super()._load_config(method_name)
        if hasattr(self, 'is_option_a') and self.is_option_a and method_name == "rnd_oe":
            cfg = copy.deepcopy(cfg)
            cfg.hparams.model = {
                'required_tensors': ['obs_embeddings'],
                'optional_tensors': [],
                'required_actions': ['position'],
                'optional_actions': ['rotation'],
                'normalize_tensors': {
                    'obs_embeddings': False,
                    'rgb_images': True,
                    'actions': False,
                    'action_preds': False,
                    'states': False,
                    'mode': 'gaussian',
                    'range_eps': 1e-05,
                    'limits': [-1, 1],
                    'fit_offset': True
                },
                'history_length': 0,
                'seed': 42,
                'action_batch_handling': None,
                'model_hyperparameters': {'rnd_loss': 'l2'},
                'rnd_train': {
                    'batch_size': 256,
                    'n_epochs': 250,
                    'lr': 0.0001,
                    'lr_scheduler': 'cosine',
                    'lr_min': 1e-06,
                    'optimizer': 'adamw',
                    'weight_decay': 1e-05,
                    'eps': 1e-08,
                    'num_workers': 8,
                    'save_every_n_epochs': 0,
                    'keep_checkpoints': 2,
                    'patience': 7,
                    'stop_when_avg_improvement': 0,
                    'stop_when_val_to_train_ratio': 5,
                    'early_stopping': True,
                    'use_validation': True,
                    'train_ratio': 0.9,
                    'overwrite': False
                }
            }
        return cfg

def main():
    task = "libero_fold00"
    methods = ["entropy", "rnd_oe"]
    combine_methods = True
    combined_methods = {
        1: {"m1": {"name": "rnd_oe"}, "m2": {"name": "entropy"}, "operation": "or"},
        2: {"m1": {"name": "rnd_oe"}, "m2": {"name": "entropy"}, "operation": "and"}
    }
    
    base_config_path = os.path.join(ROOT_DIR, "configs")
    base_data_path = os.path.join(ROOT_DIR, "data")
    task_data_path = os.path.join(base_data_path, task)
    
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
    
    # Path to models
    active_rnd_dir = os.path.join(task_data_path, "rnd_models", "rnd_oe")
    backup_rnd_dir = os.path.join(task_data_path, "rnd_models", "rnd_oe_backup")
    
    # Option B source
    opt_b_source_dir = "/home/dean/fiper_uncertainty_collection/external/fiper/data/libero_fold00_hygiene/rnd_models/rnd_oe"
    # Option A source
    opt_a_source_dir = "/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622/official_fiper_data/libero_fold00/rnd_models/rnd_oe"
    
    # Backup current active rnd models
    if os.path.exists(active_rnd_dir):
        if os.path.exists(backup_rnd_dir):
            shutil.rmtree(backup_rnd_dir)
        shutil.copytree(active_rnd_dir, backup_rnd_dir)
        print("Backed up active RND models.", flush=True)
        
    def setup_rnd_models(source_dir):
        if os.path.exists(active_rnd_dir):
            shutil.rmtree(active_rnd_dir)
        shutil.copytree(source_dir, active_rnd_dir)
        print(f"Set up RND models from {source_dir}", flush=True)
        
    def restore_backup():
        if os.path.exists(backup_rnd_dir):
            if os.path.exists(active_rnd_dir):
                shutil.rmtree(active_rnd_dir)
            shutil.copytree(backup_rnd_dir, active_rnd_dir)
            shutil.rmtree(backup_rnd_dir)
            print("Restored active RND models backup.", flush=True)

    def calculate_custom_metrics(scores_by_threshold, success_mask, episode_lengths):
        detected = []
        first_alarm_steps = []
        for scores in scores_by_threshold:
            scores_above = np.array(scores) > 1.0
            has_alarm = np.any(scores_above)
            detected.append(has_alarm)
            if has_alarm:
                first_alarm_steps.append(np.where(scores_above)[0][0])
            else:
                first_alarm_steps.append(None)
                
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
        
        det_times_capped = []
        det_times_fixed = []
        
        for idx in failure_indices:
            if detected[idx]:
                step = first_alarm_steps[idx]
                length = episode_lengths[idx]
                
                # Denominator A: capped rollout length
                denom_capped = min(length, 300)
                frac_capped = step / (denom_capped - 1) if denom_capped > 1 else 0.0
                det_times_capped.append(frac_capped)
                
                # Denominator B: fixed 300
                frac_fixed = step / 300.0
                det_times_fixed.append(frac_fixed)
                
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
        
        mean_time_capped = np.mean(det_times_capped) if len(det_times_capped) > 0 else 0.0
        mean_time_fixed = np.mean(det_times_fixed) if len(det_times_fixed) > 0 else 0.0
        
        balanced_acc = (failure_det + (1.0 - success_fa)) / 2.0
        
        return {
            "Success FA": success_fa,
            "Failure Det": failure_det,
            "Det@10": det_10_rate,
            "Det@25": det_25_rate,
            "Det@50": det_50_rate,
            "Mean Time Capped": mean_time_capped,
            "Mean Time Fixed": mean_time_fixed,
            "Never": never_det,
            "Accuracy": balanced_acc,
        }

    all_results = []
    
    try:
        # --- EVALUATE OPTION B ---
        setup_rnd_models(opt_b_source_dir)
        opt_b_seeds = [0, 1, 2, 42, 43]
        opt_b_raw_results = {}
        
        seed_0_results = None
        for seed in opt_b_seeds:
            print(f"Option B: Evaluating seed {seed}...", flush=True)
            set_seed(seed)
            evaluationmanager = ForensicEvaluationManager(base_config_path, task_data_path, dataset, device=device, seed=seed, is_option_a=False)
            
            if seed == 0:
                seed_results = evaluationmanager.evaluate(methods, combine_methods, combined_methods)
                seed_0_results = seed_results
            else:
                seed_results = evaluationmanager.evaluate(["rnd_oe"], combine_methods=False)
                seed_results["entropy"] = seed_0_results["entropy"]
                seed_results = evaluationmanager._combine_two_methods(combined_methods[1], seed_results)
                seed_results = evaluationmanager._combine_two_methods(combined_methods[2], seed_results)
            
            opt_b_raw_results[seed] = seed_results

        # Extract OOD metrics for Option B across seeds
        methods_to_report = ["entropy", "rnd_oe", "rnd_oe_and_entropy"]
        window_settings = {
            "entropy": 29,
            "rnd_oe": 48,
            "rnd_oe_and_entropy": "48/16"
        }
        
        any_result = opt_b_raw_results[0]["entropy"]
        ood_mask = any_result["ood_test_rollouts"]
        successful_mask = any_result["successful_test_rollouts"]
        episode_lengths = np.array(dataset.data["metadata"]["episode_lengths"])[dataset.data["metadata"]["test_rollout_labels"]][ood_mask]
        
        success_mask_ood = successful_mask[ood_mask]
        
        for m_name in methods_to_report:
            w_size = window_settings[m_name]
            seed_metrics = []
            
            for seed in opt_b_seeds:
                res = opt_b_raw_results[seed][m_name]
                scores_by_threshold = res["test_scores_by_threshold"]["tvt_quantile"][0.95][w_size]
                ood_scores = [scores for scores, is_ood in zip(scores_by_threshold, ood_mask) if is_ood]
                
                metrics = calculate_custom_metrics(ood_scores, success_mask_ood, episode_lengths)
                seed_metrics.append(metrics)
                
            # Aggregate over seeds
            agg_metrics = {}
            for k in seed_metrics[0].keys():
                vals = [m[k] for m in seed_metrics]
                agg_metrics[f"{k}_mean"] = np.mean(vals)
                agg_metrics[f"{k}_std"] = np.std(vals)
                
            all_results.append({
                "Option": "Option B",
                "Method": m_name,
                "Window": str(w_size),
                **agg_metrics
            })
            
        # --- INVESTIGATE RND-OE STEP 0 SATURATION (Option B, Seed 42) ---
        res_rnd = opt_b_raw_results[42]["rnd_oe"]
        scores_by_threshold = res_rnd["test_scores_by_threshold"]["tvt_quantile"][0.95][48]
        ood_scores = [scores for scores, is_ood in zip(scores_by_threshold, ood_mask) if is_ood]
        
        # Test uncertainty scores (unnormalized)
        unnorm_scores = res_rnd["test_uncertainty_scores"][48]
        ood_unnorm = [s["uncertainty_scores"] for s, is_ood in zip(unnorm_scores, ood_mask) if is_ood]
        
        thresholds = res_rnd["calibration_thresholds"]["tvt_quantile"][0.95][48]
        
        success_indices_ood = np.where(success_mask_ood == True)[0]
        failure_indices_ood = np.where(success_mask_ood == False)[0]
        
        print("\n--- RND-OE OPTION B DETAILED ROLLOUT SAMPLE (Seed 42) ---", flush=True)
        print("| rollout_id | type | length | step_0_score | threshold_0 | normalized_step_0 | max_score | first_alarm_step | first_alarm_frac |", flush=True)
        
        # Sample 10 successes and 10 failures
        sample_successes = success_indices_ood[:10]
        sample_failures = failure_indices_ood[:10]
        
        for idx in list(sample_successes) + list(sample_failures):
            type_str = "success" if idx in success_indices_ood else "failure"
            s_traj = ood_scores[idx]
            unnorm_traj = ood_unnorm[idx]
            length = len(unnorm_traj)
            
            step_0_score = unnorm_traj[0]
            thresh_0 = thresholds[0]
            norm_step_0 = s_traj[0]
            max_score = np.max(unnorm_traj)
            
            scores_above = np.array(s_traj) > 1.0
            has_alarm = np.any(scores_above)
            first_alarm = np.where(scores_above)[0][0] if has_alarm else None
            
            if first_alarm is not None:
                denom = min(length, 300)
                first_frac = first_alarm / (denom - 1) if denom > 1 else 0.0
            else:
                first_frac = None
                
            print(f"| {idx:10d} | {type_str:7s} | {length:6d} | {step_0_score:12.4f} | {thresh_0:11.4f} | {norm_step_0:17.4f} | {max_score:9.4f} | {str(first_alarm):16s} | {str(first_frac):16s} |", flush=True)
            
        # --- EVALUATE OPTION A (seed 42 only) ---
        setup_rnd_models(opt_a_source_dir)
        print("Option A: Evaluating seed 42...", flush=True)
        set_seed(42)
        evaluationmanager = ForensicEvaluationManager(base_config_path, task_data_path, dataset, device=device, seed=42, is_option_a=True)
        
        seed_results_a = evaluationmanager.evaluate(["rnd_oe"], combine_methods=False)
        seed_results_a["entropy"] = seed_0_results["entropy"]
        seed_results_a = evaluationmanager._combine_two_methods(combined_methods[1], seed_results_a)
        seed_results_a = evaluationmanager._combine_two_methods(combined_methods[2], seed_results_a)
        
        window_settings_a = {
            "entropy": 29,
            "rnd_oe": 48,
            "rnd_oe_and_entropy": "48/11"
        }
        
        for m_name in methods_to_report:
            w_size = window_settings_a[m_name]
            res = seed_results_a[m_name]
            scores_by_threshold = res["test_scores_by_threshold"]["tvt_quantile"][0.95][w_size]
            ood_scores = [scores for scores, is_ood in zip(scores_by_threshold, ood_mask) if is_ood]
            
            metrics = calculate_custom_metrics(ood_scores, success_mask_ood, episode_lengths)
            
            row = {"Option": "Option A", "Method": m_name, "Window": str(w_size)}
            for k, v in metrics.items():
                row[f"{k}_mean"] = v
                row[f"{k}_std"] = 0.0
            all_results.append(row)

    finally:
        restore_backup()
        
    # Build DataFrame
    df = pd.DataFrame(all_results)
    
    # Print results
    print("\n--- FORENSIC RECOMPUTED METRICS ---")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print(df.to_string(index=False))
    
    # Save to CSV
    df.to_csv("/home/dean/fiper_uncertainty_collection/external/fiper/scratch/forensic_verification_metrics.csv", index=False)
    print("\nSaved to scratch/forensic_verification_metrics.csv", flush=True)

if __name__ == "__main__":
    main()
