from __future__ import annotations
import argparse, torch, numpy as np
from pathlib import Path
from torch.utils.data import DataLoader
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
    dataset = TDQCDataset(args.dataset_path, max_horizon=150) # Full horizon for evaluation
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=False, collate_fn=tdqc_collate)
    ckpt = torch.load(args.ckpt, map_location="cpu")
    cfg = ckpt["config"]
    model = TDQCTransformerCalibrator(input_dim=dataset.input_dim, hidden_dim=cfg["hidden_dim"], num_layers=cfg["num_layers"]).to(device)
    model.load_state_dict(ckpt["model"]); model.eval()
    mean, std = ckpt["mean"].to(device), ckpt["std"].to(device)

    lead_times = [] # How many steps before end was the threshold crossed?
    false_positives = 0
    true_positives = 0
    total_failures = 0
    total_successes = 0

    for batch in loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, mask=batch["mask"])
        
        for b in range(q.shape[0]):
            is_fail = int(batch["failure"][b].item())
            L = int(batch["lengths"][b].item())
            probs = q[b, :L]
            
            # Find the first step where prob >= threshold
            crossed = (probs >= args.threshold).nonzero(as_tuple=True)[0]
            if len(crossed) > 0:
                first_step = crossed[0].item()
                if is_fail:
                    true_positives += 1
                    lead_times.append(L - first_step)
                else:
                    false_positives += 1
            
            if is_fail: total_failures += 1
            else: total_successes += 1

    print(f"--- Meaningful Evaluation (Threshold={args.threshold}) ---")
    print(f"Detection Recall: {true_positives/max(total_failures, 1):.2%}")
    print(f"False Positive Rate: {false_positives/max(total_successes, 1):.2%}")
    if lead_times:
        print(f"Mean Lead Time: {np.mean(lead_times):.1f} steps")
        print(f"Median Lead Time: {np.median(lead_times):.1f} steps")
        print(f"P90 Lead Time: {np.percentile(lead_times, 90):.1f} steps")
    else:
        print("No detections found.")
    print("------------------------------------------")

if __name__ == "__main__":
    main()
