#!/usr/bin/env python3
import argparse
import json
import math
import os
import sys
from pathlib import Path
from collections import Counter, defaultdict
import numpy as np
import torch
from torch.utils.data import DataLoader

# Add fiper_ws to python path
sys.path.append("/home/rootalkhatib/test/reda_ws/fiper_ws")

from stage9_training_experiments.stage9_dataset import Stage9RiskDataset, collate_stage9, parse_source_remaps
from stage9_training_experiments.stage9_eval import auroc, auprc, ece_score, brier, nll, threshold_metrics, accepted_risk_table
from stage9_training_experiments.stage9_losses import risk_prob_from_outputs
from stage9_training_experiments.stage9_models import Stage9Dims, create_model

def make_loader(dataset, batch_size, workers):
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=workers,
        pin_memory=torch.cuda.is_available(),
        collate_fn=collate_stage9,
        drop_last=False,
    )

def evaluate_model_on_loader(model, loader, device, target_mode):
    model.eval()
    preds = []
    targets = []
    labels = []
    subtypes = []
    groups = []
    sources = []
    sample_ids = []
    seeds = []
    
    with torch.no_grad():
        for batch in loader:
            dev_batch = {}
            for k, v in batch.items():
                dev_batch[k] = v.to(device) if torch.is_tensor(v) else v
            prob_tensor = risk_prob_from_outputs(model(dev_batch), target_mode).detach().cpu()
            preds.extend(prob_tensor.numpy().tolist())
            targets.extend(batch["target"].numpy().tolist())
            labels.extend(batch["label"])
            subtypes.extend(batch["bad_subtype"])
            sample_ids.extend(batch["sample_id"])
            seeds.extend(batch["seed"])
            
            # Since Stage9RiskDataset __getitem__ returns the original sample, we can query metadata/split_row fields if they were preserved.
            # But they might not be in collate. Let's fall back gracefully.
            # In our Stage9RiskDataset code, __getitem__ returns 'state_id' (which is the metadata state_id or split_row state_id)
            # Let's check group_id by state_id.
            groups.extend(batch["state_id"])
            
    return {
        "preds": np.array(preds),
        "targets": np.array(targets),
        "labels": labels,
        "subtypes": subtypes,
        "groups": groups,
        "sample_ids": sample_ids,
        "seeds": seeds,
    }

def get_spearman(p, t):
    if len(p) > 1 and np.std(p) > 1e-9 and np.std(t) > 1e-9:
        try:
            from scipy.stats import spearmanr
            return float(spearmanr(p, t)[0])
        except Exception:
            pass
    return None

def get_pearson(p, t):
    if len(p) > 1 and np.std(p) > 1e-9 and np.std(t) > 1e-9:
        try:
            return float(np.corrcoef(p, t)[0, 1])
        except Exception:
            pass
    return None

def compute_group_ranking_accuracy(groups, targets, preds):
    # Group samples by group_id
    by_group = defaultdict(list)
    for g, t, p in zip(groups, targets, preds):
        if g:
            by_group[g].append((t, p))
            
    total_pairs = 0
    correct_pairs = 0
    
    for gid, members in by_group.items():
        # High risk: target >= 0.75 or label == VALIDATED_BAD (using target >= 0.75 here)
        highs = [m for m in members if m[0] >= 0.75]
        lows = [m for m in members if m[0] <= 0.20]
        
        if not highs or not lows:
            continue
            
        for h_t, h_p in highs:
            for l_t, l_p in lows:
                total_pairs += 1
                if h_p > l_p:
                    correct_pairs += 1.0
                elif h_p == l_p:
                    correct_pairs += 0.5
                    
    if total_pairs == 0:
        return None
    return float(correct_pairs / total_pairs)

def calculate_metrics(results):
    preds = results["preds"]
    targets = results["targets"]
    labels = results["labels"]
    subtypes = results["subtypes"]
    groups = results["groups"]
    
    n = len(preds)
    if n == 0:
        return {"n": 0}
        
    # Continuous regression metrics
    mae = float(np.mean(np.abs(preds - targets)))
    mse = float(np.mean((preds - targets) ** 2))
    rmse = float(math.sqrt(mse))
    pearson = get_pearson(preds, targets)
    spearman = get_spearman(preds, targets)
    
    # Binary classification definitions:
    # Class 1: high risk (target >= 0.75 or label == "VALIDATED_BAD")
    # Class 0: low risk (target <= 0.20 or label == "GOOD_STRONG")
    y_bin = []
    p_bin = []
    subtypes_bin = []
    
    for p, t, lbl, sub in zip(preds, targets, labels, subtypes):
        is_high = (t >= 0.75 or lbl == "VALIDATED_BAD")
        is_low = (t <= 0.20 or lbl == "GOOD_STRONG")
        if is_high:
            y_bin.append(1)
            p_bin.append(p)
            subtypes_bin.append(sub)
        elif is_low:
            y_bin.append(0)
            p_bin.append(p)
            subtypes_bin.append(sub)
            
    y_bin = np.array(y_bin)
    p_bin = np.array(p_bin)
    
    # Check class counts
    pos_count = int((y_bin == 1).sum()) if len(y_bin) else 0
    neg_count = int((y_bin == 0).sum()) if len(y_bin) else 0
    
    auroc_val = "INVALID_SINGLE_CLASS"
    auprc_val = "INVALID_SINGLE_CLASS"
    
    if pos_count > 0 and neg_count > 0:
        auroc_val = auroc(y_bin, p_bin)
        if auroc_val is None:
            auroc_val = "INVALID_SINGLE_CLASS"
        auprc_val = auprc(y_bin, p_bin)
        if auprc_val is None:
            auprc_val = "INVALID_SINGLE_CLASS"
            
    brier_val = brier(y_bin, p_bin) if len(y_bin) else None
    ece_val = ece_score(y_bin, p_bin) if len(y_bin) else None
    
    # Threshold metrics
    thrs = [0.5, 0.65, 0.75, 0.8, 0.9]
    thr_m = {}
    for thr in thrs:
        pred_bad = p_bin >= thr
        tp = int(((pred_bad == 1) & (y_bin == 1)).sum()) if len(y_bin) else 0
        fp = int(((pred_bad == 1) & (y_bin == 0)).sum()) if len(y_bin) else 0
        tn = int(((pred_bad == 0) & (y_bin == 0)).sum()) if len(y_bin) else 0
        fn = int(((pred_bad == 0) & (y_bin == 1)).sum()) if len(y_bin) else 0
        
        precision = float(tp / (tp + fp)) if (tp + fp) > 0 else 0.0
        recall = float(tp / (tp + fn)) if (tp + fn) > 0 else 0.0
        f1 = float(2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0
        
        # Subtype-specific recall
        tp_state_ctx = 0
        fn_state_ctx = 0
        tp_act_spec = 0
        fn_act_spec = 0
        
        for p, y, sub in zip(p_bin, y_bin, subtypes_bin):
            if y == 1:
                pred = (p >= thr)
                if sub == "state_context":
                    if pred:
                        tp_state_ctx += 1
                    else:
                        fn_state_ctx += 1
                elif sub == "action_specific":
                    if pred:
                        tp_act_spec += 1
                    else:
                        fn_act_spec += 1
                        
        recall_state_ctx = float(tp_state_ctx / (tp_state_ctx + fn_state_ctx)) if (tp_state_ctx + fn_state_ctx) > 0 else None
        recall_act_spec = float(tp_act_spec / (tp_act_spec + fn_act_spec)) if (tp_act_spec + fn_act_spec) > 0 else None
        
        # Expert false alarm rate
        # Defined as fp / (tn + fp) on the clean subset (since all negative samples in clean subset are low-risk)
        # But we also have a dedicated test set `expert_false_alarm_test` which has only expert anchors (low risk).
        # We will compute the expert false alarm rate specifically on the expert_false_alarm_test set using predictions there.
        
        thr_m[f"{thr:.2f}"] = {
            "confusion_matrix": {"tp": tp, "fp": fp, "tn": tn, "fn": fn},
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "recall_state_context": recall_state_ctx,
            "recall_action_specific": recall_act_spec,
        }
        
    # Accepted high-risk leakage at accept fractions
    accept_fracs = [0.90, 0.75, 0.50, 0.25]
    accept_table = {}
    if len(p_bin) > 0:
        order = np.argsort(p_bin)
        for frac in accept_fracs:
            k = max(1, int(round(len(p_bin) * frac)))
            accepted_indices = order[:k]
            accepted_y = y_bin[accepted_indices]
            accepted_high_risk = int(accepted_y.sum())
            accepted_low_risk = k - accepted_high_risk
            
            leakage = float(accepted_high_risk / k)
            purity = float(accepted_low_risk / k)
            threshold = float(p_bin[accepted_indices].max()) if len(accepted_indices) else None
            
            accept_table[f"accept_{int(frac * 100)}pct"] = {
                "accepted_count": k,
                "accepted_high_risk_count": accepted_high_risk,
                "leakage": leakage,
                "purity": purity,
                "threshold": threshold,
            }
            
    # Same-state group ranking accuracy
    ranking_accuracy = compute_group_ranking_accuracy(groups, targets, preds)
    
    # Calibration bins data
    bins = 15
    reliability_bins = []
    if len(y_bin) > 0:
        for i in range(bins):
            lo, hi = i / bins, (i + 1) / bins
            mask = (p_bin >= lo) & ((p_bin < hi) if i < bins - 1 else (p_bin <= hi))
            count = int(mask.sum())
            if count > 0:
                avg_pred = float(p_bin[mask].mean())
                avg_true = float(y_bin[mask].mean())
                reliability_bins.append({
                    "bin_range": [lo, hi],
                    "count": count,
                    "avg_pred": avg_pred,
                    "avg_true": avg_true,
                })
                
    return {
        "n": n,
        "clean_n": len(y_bin),
        "pos_count": pos_count,
        "neg_count": neg_count,
        "continuous": {
            "mae": mae,
            "mse": mse,
            "rmse": rmse,
            "pearson": pearson,
            "spearman": spearman,
        },
        "binary": {
            "auroc": auroc_val,
            "auprc": auprc_val,
            "brier": brier_val,
            "ece": ece_val,
        },
        "threshold_metrics": thr_m,
        "accepted_risk": accept_table,
        "ranking_accuracy": ranking_accuracy,
        "reliability_bins": reliability_bins,
    }

def get_expert_false_alarm_rate(preds, thresholds):
    # All samples in expert_false_alarm_test are low risk (expert anchors)
    out = {}
    n = len(preds)
    if n == 0:
        return out
    for thr in thresholds:
        alarms = int((preds >= thr).sum())
        out[f"{thr:.2f}"] = {
            "total_count": n,
            "alarm_count": alarms,
            "false_alarm_rate": float(alarms / n),
        }
    return out

def main():
    campaign_dir = Path("/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/experiments/stage9_fiper_v2_sam_20h_20260520_173700")
    hard_eval_dir = campaign_dir / "datasets" / "hard_eval_v2"
    train_dir = campaign_dir / "training"
    out_dir = campaign_dir / "hard_eval_results"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)
    
    # 1. Load the hard datasets
    splits = [
        "hard_balanced_test",
        "state_context_test",
        "action_specific_test",
        "ood_task_test",
        "ood_source_test",
        "expert_false_alarm_test",
        "same_state_group_test",
    ]
    
    # 2. Checkpoints to evaluate
    MODELS = [
        "residual_mlp_large",
        "context_action_mlp",
        "history_lstm_k8",
        "TCN_history_k8",
        "history_gru_k8",  # Load to construct ensemble
    ]
    
    # We will load configs and models
    loaded_models = {}
    model_configs = {}
    model_targets = {}
    
    for model_name in MODELS:
        ckpt_path = train_dir / model_name / "checkpoint.pt"
        if not ckpt_path.exists():
            print(f"ERROR: {model_name} checkpoint not found at {ckpt_path}")
            sys.exit(1)
            
        print(f"Loading {model_name}...")
        checkpoint = torch.load(ckpt_path, map_location=device)
        config = checkpoint["config"]
        dims_dict = checkpoint["dims"]
        target_mode = config["target_mode"]
        
        dims = Stage9Dims(
            flat_dim=dims_dict["flat_dim"],
            context_action_dim=dims_dict["context_action_dim"],
            action_flat_dim=dims_dict["action_flat_dim"],
            action_steps=dims_dict["action_steps"],
            action_dim=dims_dict["action_dim"],
            history_steps=dims_dict["history_steps"],
            history_dim=dims_dict["history_dim"],
        )
        
        model = create_model(model_name, dims, target_mode).to(device)
        model.load_state_dict(checkpoint["model_state_dict"])
        model.eval()
        
        loaded_models[model_name] = model
        model_configs[model_name] = config
        model_targets[model_name] = target_mode
        
    print("All models loaded successfully.")
    
    # We evaluate residual_mlp_large, TCN_history_k8, history_lstm_k8, context_action_mlp, and ensemble_top3 (which averages residual_mlp_large, history_gru_k8, and context_action_mlp).
    eval_model_names = [
        "residual_mlp_large",
        "context_action_mlp",
        "history_lstm_k8",
        "TCN_history_k8",
        "ensemble_top3",
    ]
    
    # Initialize dictionary to collect predictions across splits for all models
    # model_name -> split_name -> predictions_results
    predictions_results = {name: {} for name in eval_model_names}
    
    # Run evaluation
    for split_name in splits:
        print(f"\n--- Evaluating on {split_name} ---")
        jsonl_path = hard_eval_dir / f"{split_name}.jsonl"
        
        # We can use the configuration of residual_mlp_large to load dataset, since it matches target_mode = continuous_regression
        target_mode = "continuous_regression"
        source_remaps = parse_source_remaps(model_configs["residual_mlp_large"].get("source_remap"))
        
        dataset = Stage9RiskDataset(
            jsonl_path,
            target_mode,
            source_remaps,
            max_samples=None
        )
        loader = make_loader(dataset, batch_size=256, workers=2)
        
        # Evaluate individual models
        split_preds = {}
        eval_meta = None
        
        for model_name in MODELS:
            res = evaluate_model_on_loader(loaded_models[model_name], loader, device, model_targets[model_name])
            split_preds[model_name] = res["preds"]
            if eval_meta is None:
                # Save target, label, subtype, group, seed metadata
                eval_meta = {
                    "targets": res["targets"],
                    "labels": res["labels"],
                    "subtypes": res["subtypes"],
                    "groups": res["groups"],
                    "sample_ids": res["sample_ids"],
                    "seeds": res["seeds"],
                }
                
        # Now populate evaluation results for our models of interest
        for name in eval_model_names:
            if name == "ensemble_top3":
                # Average predictions of residual_mlp_large, history_gru_k8, context_action_mlp
                ensemble_preds = (split_preds["residual_mlp_large"] + split_preds["history_gru_k8"] + split_preds["context_action_mlp"]) / 3.0
                predictions_results[name][split_name] = {
                    "preds": ensemble_preds,
                    **eval_meta
                }
            else:
                predictions_results[name][split_name] = {
                    "preds": split_preds[name],
                    **eval_meta
                }
                
    # 3. Compute metrics and write results for each evaluated model
    for model_name in eval_model_names:
        print(f"\nComputing final metrics and saving files for model: {model_name}")
        model_out_dir = out_dir / model_name
        model_out_dir.mkdir(parents=True, exist_ok=True)
        
        summary_lines = [
            f"# Hard Evaluation Summary: {model_name}",
            "",
            "| Split | N | Clean N | AUROC | AUPRC | Brier | MAE | RMSE | Ranking Acc |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
        
        all_metrics = {}
        
        for split_name in splits:
            res = predictions_results[model_name][split_name]
            metrics = calculate_metrics(res)
            all_metrics[split_name] = metrics
            
            # Save predictions
            pred_rows = []
            for i in range(len(res["preds"])):
                pred_rows.append({
                    "sample_id": res["sample_ids"][i],
                    "predicted_risk": float(res["preds"][i]),
                    "target_risk": float(res["targets"][i]),
                    "label": res["labels"][i],
                    "bad_subtype": res["subtypes"][i],
                    "group_id": res["groups"][i],
                    "seed": res["seeds"][i],
                })
            
            pred_file = model_out_dir / f"predictions_{split_name}.jsonl"
            with pred_file.open("w") as f:
                for row in pred_rows:
                    f.write(json.dumps(row) + "\n")
                    
            # Save metrics
            metrics_file = model_out_dir / f"metrics_{split_name}.json"
            with metrics_file.open("w") as f:
                json.dump(metrics, f, indent=2, sort_keys=True, default=str)
                f.write("\n")
                
            # Add dedicated false alarm stats for expert false alarm set
            if split_name == "expert_false_alarm_test":
                fa_metrics = get_expert_false_alarm_rate(res["preds"], [0.5, 0.65, 0.75, 0.8, 0.9])
                metrics["expert_false_alarm_rates"] = fa_metrics
                with metrics_file.open("w") as f:
                    json.dump(metrics, f, indent=2, sort_keys=True, default=str)
                    f.write("\n")
            
            # Extract summary stats
            n_val = metrics["n"]
            clean_n = metrics.get("clean_n", 0)
            auroc_val = metrics["binary"]["auroc"]
            auprc_val = metrics["binary"]["auprc"]
            brier_val = metrics["binary"]["brier"]
            mae_val = metrics["continuous"]["mae"]
            rmse_val = metrics["continuous"]["rmse"]
            rank_acc = metrics.get("ranking_accuracy")
            
            # Format display values
            auroc_str = f"{auroc_val:.4f}" if isinstance(auroc_val, float) else str(auroc_val)
            auprc_str = f"{auprc_val:.4f}" if isinstance(auprc_val, float) else str(auprc_val)
            brier_str = f"{brier_val:.4f}" if isinstance(brier_val, float) else "N/A"
            rank_acc_str = f"{rank_acc:.4f}" if isinstance(rank_acc, float) else "N/A"
            
            summary_lines.append(
                f"| {split_name} | {n_val} | {clean_n} | {auroc_str} | {auprc_str} | {brier_str} | {mae_val:.4f} | {rmse_val:.4f} | {rank_acc_str} |"
            )
            
        # Append detailed metrics details to summary.md
        summary_lines.extend(["", "## Detailed Threshold Metrics", ""])
        for split_name in splits:
            metrics = all_metrics[split_name]
            summary_lines.append(f"### Split: {split_name}")
            summary_lines.append("")
            
            if split_name == "expert_false_alarm_test" and "expert_false_alarm_rates" in metrics:
                summary_lines.append("#### Expert False Alarm Rates")
                summary_lines.append("| Threshold | Alarms | Total | False Alarm Rate |")
                summary_lines.append("|---|---|---|---|")
                for thr, val in sorted(metrics["expert_false_alarm_rates"].items()):
                    summary_lines.append(f"| {thr} | {val['alarm_count']} | {val['total_count']} | {val['false_alarm_rate']:.4f} |")
                summary_lines.append("")
                
            summary_lines.append("| Threshold | TP | FP | TN | FN | Precision | Recall | F1 | Recall State Ctx | Recall Action Spec |")
            summary_lines.append("|---|---|---|---|---|---|---|---|---|---|")
            
            thrs_dict = metrics.get("threshold_metrics", {})
            for thr in sorted(thrs_dict.keys()):
                val = thrs_dict[thr]
                cm = val["confusion_matrix"]
                rec_sc = val.get("recall_state_context")
                rec_sc_str = f"{rec_sc:.4f}" if isinstance(rec_sc, float) else "N/A"
                rec_as = val.get("recall_action_specific")
                rec_as_str = f"{rec_as:.4f}" if isinstance(rec_as, float) else "N/A"
                
                summary_lines.append(
                    f"| {thr} | {cm['tp']} | {cm['fp']} | {cm['tn']} | {cm['fn']} | {val['precision']:.4f} | {val['recall']:.4f} | {val['f1']:.4f} | {rec_sc_str} | {rec_as_str} |"
                )
            summary_lines.append("")
            
            # Add Leakage table
            summary_lines.append("#### Accepted High-Risk Leakage Table")
            summary_lines.append("| Accept Fraction | Accepted Count | Accepted High-Risk | Leakage Rate | Low-Risk Purity | Risk Threshold |")
            summary_lines.append("|---|---|---|---|---|---|")
            ar_dict = metrics.get("accepted_risk", {})
            for accept_key in sorted(ar_dict.keys()):
                val = ar_dict[accept_key]
                thr = val["threshold"]
                thr_str = f"{thr:.4f}" if isinstance(thr, float) else "N/A"
                summary_lines.append(
                    f"| {accept_key} | {val['accepted_count']} | {val['accepted_high_risk_count']} | {val['leakage']:.4f} | {val['purity']:.4f} | {thr_str} |"
                )
            summary_lines.append("")
            
        summary_md_path = model_out_dir / "summary.md"
        summary_md_path.write_text("\n".join(summary_lines) + "\n")
        print(f"Written summary.md for {model_name}")
        
    print("\nAll evaluations completed successfully!")

if __name__ == "__main__":
    main()
