import sys
import os
import pathlib
import numpy as np
import torch
import pandas as pd
from omegaconf import DictConfig, OmegaConf

ROOT_DIR = "/home/dean/fiper_uncertainty_collection/external/fiper"
sys.path.insert(0, ROOT_DIR)
os.chdir(ROOT_DIR)

from evaluation import EvaluationManager
from tasks import TaskManager
from shared_utils.hydra_utils import load_config
from shared_utils.utility_functions import get_required_tensors, set_seed
from evaluation.utils import calculate_metrics

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
    
    seeds = [0, 1, 2, 42, 43]
    all_seed_results = []
    
    seed_0_results = None
    
    for seed in seeds:
        print(f"Evaluating seed {seed}...", flush=True)
        set_seed(seed)
        evaluationmanager = EvaluationManager(base_config_path, task_data_path, dataset, device=device, seed=seed)
        
        if seed == 0:
            seed_results = evaluationmanager.evaluate(methods, combine_methods, combined_methods)
            seed_0_results = seed_results
        else:
            seed_results = evaluationmanager.evaluate(["rnd_oe"], combine_methods=False)
            # copy entropy results
            seed_results["entropy"] = seed_0_results["entropy"]
            # manually combine
            seed_results = evaluationmanager._combine_two_methods(combined_methods[1], seed_results)
            seed_results = evaluationmanager._combine_two_methods(combined_methods[2], seed_results)
            
        # Filter metrics to OOD-only
        ood_task_results = {}
        for method_name, result in seed_results.items():
            ood_task_results[method_name] = {}
            ood_mask = result["ood_test_rollouts"]
            successful_mask = result["successful_test_rollouts"]
            
            # dataset_stats for OOD-only
            n_ood = np.sum(ood_mask)
            dataset_stats = {
                "max_episode_length": result["max_episode_length"],
                "id_rollouts": np.zeros(n_ood, dtype=bool),
                "ood_rollouts": np.ones(n_ood, dtype=bool),
                "successful_rollouts": successful_mask[ood_mask],
            }
            
            # We need to compute metrics for each threshold style, quantile, and window size
            test_metrics = {}
            for threshold_style in result["test_metrics"].keys():
                test_metrics[threshold_style] = {}
                quantiles = result["quantiles"] if result["quantiles"] is not None else result["cfg"].quantiles
                window_sizes = result["window_sizes"] if result["window_sizes"] is not None else result["cfg"].window_sizes
                
                # If quantiles/window_sizes is None, we use default ones from result cfg
                if quantiles is None:
                    quantiles = [0.9] # fallback
                
                for q in quantiles:
                    test_metrics[threshold_style][q] = {}
                    for w in window_sizes:
                        # Extract the uncertainty scores for this method, style, quantile, and window size
                        scores_by_threshold = result["test_scores_by_threshold"][threshold_style][q][w]
                        
                        # Filter to OOD-only
                        ood_scores = [scores for scores, is_ood in zip(scores_by_threshold, ood_mask) if is_ood]
                        
                        # Calculate OOD-only metrics
                        ood_metrics = calculate_metrics(ood_scores, dataset_stats, result["cfg"].get("detection_patience", 0))
                        test_metrics[threshold_style][q][w] = ood_metrics
            
            # Pack it as required by ResultsManager
            ood_task_results[method_name] = {
                "test_metrics": test_metrics,
                "quantiles": result["quantiles"] if result["quantiles"] is not None else result["cfg"].quantiles,
                "window_sizes": result["window_sizes"] if result["window_sizes"] is not None else result["cfg"].window_sizes,
                "cfg": result["cfg"],
                "max_episode_length": result["max_episode_length"]
            }
            
        all_seed_results.append({task: ood_task_results})
        
    # Now we accumulate results across seeds
    from evaluation import ResultsManager
    resultsmanager = ResultsManager(base_config_path, base_data_path)
    total_results = resultsmanager.accumulate_seed_results(all_seed_results)
    
    # We will build complete_df from memory
    rows = []
    for method in total_results[task].keys():
        method_results = total_results[task][method]
        window_sizes = method_results["window_sizes"] if method_results["window_sizes"] is not None else method_results["cfg"].get("window_sizes", [1])
        quantiles = method_results["quantiles"] if method_results["quantiles"] is not None else method_results["cfg"].get("quantiles", [0.9])
        for window_size in window_sizes:
            for quantile in quantiles:
                for threshold_style in method_results["test_metrics"].keys():
                    if quantile not in method_results["test_metrics"][threshold_style]:
                        continue
                    if window_size not in method_results["test_metrics"][threshold_style][quantile]:
                        continue
                    metrics = method_results["test_metrics"][threshold_style][quantile][window_size]
                    
                    never_rate = 1.0 - metrics["TPR"]
                    never_rate_std = metrics.get("TPR_std", 0.0)
                    
                    row = {
                        "Method": method,
                        "Task": task,
                        "Window": str(window_size),
                        "Quantile": float(quantile),
                        "Threshold": str(threshold_style),
                        "TPR (Failure Det)": float(metrics["TPR"]),
                        "TPR_std": float(metrics.get("TPR_std", 0.0)),
                        "TNR": float(metrics["TNR"]),
                        "TNR_std": float(metrics.get("TNR_std", 0.0)),
                        "Success FA": float(1.0 - metrics["TNR"]),
                        "Success FA_std": float(metrics.get("TNR_std", 0.0)),
                        "Accuracy": float(metrics["balanced_accuracy"]),
                        "Accuracy_std": float(metrics.get("balanced_accuracy_std", 0.0)),
                        "Det. Time Fraction": float(metrics["avg_detection_time"]),
                        "Det. Time Fraction_std": float(metrics.get("avg_detection_time_std", 0.0)),
                        "OOD Never": float(never_rate),
                        "OOD Never_std": float(never_rate_std)
                    }
                    rows.append(row)
                    
    complete_df = pd.DataFrame(rows).round(3)
    
    print("\n--- OOD-ONLY TVT_QUANTILE RESULTS ---", flush=True)
    summary_df = complete_df[complete_df["Threshold"] == "tvt_quantile"]
    print(summary_df.to_string(index=False))

    # Also save the results to a CSV file
    os.makedirs(os.path.join(ROOT_DIR, "scratch"), exist_ok=True)
    complete_df.to_csv(os.path.join(ROOT_DIR, "scratch/option_b_ood_only_complete_results.csv"), index=False)
    summary_df.to_csv(os.path.join(ROOT_DIR, "scratch/option_b_ood_only_tvt_quantile_summary.csv"), index=False)
    print("\nSaved OOD-only results to scratch/option_b_ood_only_complete_results.csv", flush=True)

if __name__ == "__main__":
    main()
