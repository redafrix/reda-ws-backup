import json
import os
import sys
from pathlib import Path

# Add fiper_ws to python path
sys.path.append("/home/rootalkhatib/test/reda_ws/fiper_ws")

import torch
from torch.utils.data import DataLoader

from stage9_training_experiments.stage9_dataset import Stage9RiskDataset, collate_stage9, parse_source_remaps
from stage9_training_experiments.stage9_eval import summarize_predictions, write_eval_report, write_predictions
from stage9_training_experiments.stage9_losses import risk_prob_from_outputs
from stage9_training_experiments.stage9_models import Stage9Dims, create_model

def make_loader(dataset, batch_size, shuffle, workers):
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=workers,
        pin_memory=torch.cuda.is_available(),
        collate_fn=collate_stage9,
        drop_last=False,
    )

def evaluate_model(model, loader, device, target_mode, split_name):
    model.eval()
    rows = []
    with torch.no_grad():
        for batch in loader:
            dev_batch = {}
            for k, v in batch.items():
                dev_batch[k] = v.to(device) if torch.is_tensor(v) else v
            prob_tensor = risk_prob_from_outputs(model(dev_batch), target_mode).detach().cpu()
            prob = prob_tensor.numpy()
            for i, sample_id in enumerate(batch["sample_id"]):
                rows.append(
                    {
                        "split": split_name,
                        "sample_id": sample_id,
                        "state_id": batch["state_id"][i],
                        "task_name": batch["task_name"][i],
                        "perturbation_type": batch["perturbation_type"][i],
                        "seed": batch["seed"][i],
                        "label": batch["label"][i],
                        "bad_subtype": batch["bad_subtype"][i],
                        "risk_prob": float(prob[i]),
                        "risk_prob_std": 0.0,
                        "target_value": float(batch["target"][i].item()),
                        "weight": float(batch["weight"][i].item()),
                    }
                )
    return rows

def main():
    campaign_dir = Path("/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/experiments/stage9_fiper_v2_sam_20h_20260520_173700")
    split_dir = campaign_dir / "datasets" / "continuous_v2_trainset"
    train_dir = campaign_dir / "training"
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)
    
    unseen_path = split_dir / "test_unseen_group.jsonl"
    if not unseen_path.exists():
        print("ERROR: test_unseen_group.jsonl does not exist at", unseen_path)
        sys.exit(1)
        
    MODELS = [
        "residual_mlp_large",
        "context_action_mlp",
        "history_lstm_k8",
        "TCN_history_k8",
        "action_only_mlp",
        "history_gru_k8",
        "gated_context_action_mlp"
    ]
    
    for model_name in MODELS:
        model_dir = train_dir / model_name
        ckpt_path = model_dir / "checkpoint.pt"
        if not ckpt_path.exists():
            print(f"Skipping {model_name}, no checkpoint found.")
            continue
            
        print(f"Loading {model_name}...")
        checkpoint = torch.load(ckpt_path, map_location=device)
        config = checkpoint["config"]
        dims_dict = checkpoint["dims"]
        target_mode = config["target_mode"]
        
        # Load dataset
        unseen_dataset = Stage9RiskDataset(
            unseen_path,
            target_mode,
            parse_source_remaps(config.get("source_remap")),
            max_samples=config.get("max_eval_samples")
        )
        loader = make_loader(unseen_dataset, config.get("batch_size", 256), False, config.get("num_workers", 2))
        
        # Recreate model
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
        
        print(f"Evaluating {model_name} on test_unseen_group...")
        unseen_rows = evaluate_model(model, loader, device, target_mode, "test_unseen_group")
        
        # Read existing predictions and update
        pred_path = model_dir / "predictions.jsonl"
        existing_rows = []
        if pred_path.exists():
            with open(pred_path) as f:
                existing_rows = [json.loads(l) for l in f if l.strip()]
        
        # Filter out old test_unseen_group predictions if they exist
        existing_rows = [r for r in existing_rows if r.get("split") != "test_unseen_group"]
        existing_rows.extend(unseen_rows)
        write_predictions(pred_path, existing_rows)
        
        # Update metrics.json
        metrics_path = model_dir / "metrics.json"
        metrics = {}
        if metrics_path.exists():
            with open(metrics_path) as f:
                metrics = json.load(f)
        
        # Recompute splits metrics
        metrics["splits"] = summarize_predictions(existing_rows, target_mode)
        with open(metrics_path, "w") as f:
            json.dump(metrics, f, indent=2, sort_keys=True, default=str)
            f.write("\n")
        
        # Rewrite eval_report.md
        write_eval_report(model_dir / "eval_report.md", config, metrics)
        print(f"Successfully evaluated and updated metrics for {model_name}.")

if __name__ == "__main__":
    main()
