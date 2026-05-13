import argparse, torch, numpy as np
from pathlib import Path
from torch.utils.data import DataLoader
from sklearn.metrics import roc_auc_score, brier_score_loss, precision_score, recall_score, f1_score
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset_path", required=True)
    p.add_argument("--ckpt", required=True)
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--device", default="cuda")
    p.add_argument("--threshold", type=float, default=0.5)
    return p.parse_args()

@torch.no_grad()
def main():
    args = parse_args()
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    dataset = TDQCDataset(args.dataset_path, max_horizon=150, is_train=False)
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=False, collate_fn=tdqc_collate)
    
    ckpt = torch.load(args.ckpt, map_location="cpu")
    cfg = ckpt["config"]
    model = TDQCTransformerCalibrator(input_dim=dataset.input_dim, hidden_dim=cfg["hidden_dim"], num_layers=cfg["num_layers"]).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()
    
    mean, std = ckpt["mean"].to(device), ckpt["std"].to(device)

    # Accumulators for step-level metrics
    all_step_probs = []
    all_step_labels = []
    
    # Accumulators for episode-level metrics
    ep_targets = []
    ep_preds = []
    lead_times = []

    for batch in loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, mask=batch["mask"])
        
        # Step-level extraction
        for b in range(q.shape[0]):
            L = int(batch["lengths"][b].item())
            is_fail = int(batch["failure"][b].item())
            
            # Probability and label trajectory for this episode
            probs = q[b, :L].cpu().numpy()
            
            # Step labels: 0 for success episodes, 1 for failure episodes (at all steps for simplicity, or we can use the horizon logic)
            # In our training, failure episodes have label 1 at all steps within the horizon.
            labels = np.full_like(probs, is_fail)
            
            all_step_probs.extend(probs)
            all_step_labels.extend(labels)
            
            # Episode-level decision
            detection = (probs >= args.threshold).any()
            ep_targets.append(is_fail)
            ep_preds.append(int(detection))
            
            if is_fail and detection:
                first_step = np.where(probs >= args.threshold)[0][0]
                lead_times.append(L - first_step)

    all_step_probs = np.array(all_step_probs)
    all_step_labels = np.array(all_step_labels)
    ep_targets = np.array(ep_targets)
    ep_preds = np.array(ep_preds)

    print(f"\n--- Comprehensive Evaluation [{Path(args.dataset_path).name}] ---")
    
    # Step-level metrics
    step_brier = brier_score_loss(all_step_labels, all_step_probs)
    step_auc = roc_auc_score(all_step_labels, all_step_probs)
    
    print(f"Step-level Brier Score: {step_brier:.4f} (Lower is better)")
    print(f"Step-level AUC-ROC:     {step_auc:.4f} (Higher is better)")
    
    # Episode-level metrics
    precision = precision_score(ep_targets, ep_preds, zero_division=0)
    recall = recall_score(ep_targets, ep_preds, zero_division=0)
    f1 = f1_score(ep_targets, ep_preds, zero_division=0)
    
    # Calculate FPR manually
    tn = np.sum((ep_targets == 0) & (ep_preds == 0))
    fp = np.sum((ep_targets == 0) & (ep_preds == 1))
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    
    print(f"Episode-level Precision: {precision:.2%}")
    print(f"Episode-level Recall:    {recall:.2%}")
    print(f"Episode-level FPR:       {fpr:.2%}")
    print(f"Episode-level F1-Score:  {f1:.4f}")
    
    if lead_times:
        print(f"Mean Lead Time: {np.mean(lead_times):.1f} steps")
    print("----------------------------------------------")

if __name__ == "__main__":
    main()
