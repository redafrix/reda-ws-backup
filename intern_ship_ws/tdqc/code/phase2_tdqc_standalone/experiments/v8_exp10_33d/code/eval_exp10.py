import sys, torch, numpy as np, argparse
from pathlib import Path
from torch.utils.data import DataLoader
from sklearn.metrics import roc_auc_score

# Add code to path
sys.path.insert(0, str(Path(__file__).parent))

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--name", type=str, default="Eval")
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Paths relative to the standalone folder
    ckpt_path = Path("experiments/v8_exp10_33d/runs/best.pt")
    if not ckpt_path.exists():
        print(f"Error: {ckpt_path} not found")
        return

    ckpt = torch.load(ckpt_path, map_location=device)
    mean, std = ckpt["mean"].to(device), ckpt["std"].to(device)
    cfg = ckpt["config"]
    
    model = TDQCLSTMCalibrator(
        input_dim=cfg["input_dim"], hidden_dim=cfg["hidden_dim"],
        num_layers=cfg["num_layers"], dropout=cfg["dropout"],
    ).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()

    test_set = TDQCDataset(args.dataset)
    test_loader = DataLoader(test_set, batch_size=64, shuffle=False, collate_fn=tdqc_collate)

    all_preds = []
    all_labels = []
    all_sq_err = []

    with torch.no_grad():
        for batch in test_loader:
            batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
            x = normalize_features(batch["features"], mean, std)
            q = model(x, batch["lengths"], suite_ids=batch["suite_id"])
            
            for b in range(q.shape[0]):
                L = int(batch["lengths"][b].item())
                lbl = int(batch["failure"][b].item())
                traj = q[b, :L].cpu().numpy()
                
                all_preds.append(traj.max())
                all_labels.append(lbl)
                all_sq_err.extend(((traj - lbl)**2).tolist())

    brier = np.mean(all_sq_err)
    auc = roc_auc_score(all_labels, all_preds)

    print(f"\n--- {args.name} Results ---")
    print(f"Brier Score: {brier:.6f}")
    print(f"AUC-ROC    : {auc:.4f}")
    
    import json
    res_path = Path("experiments/v8_exp10_33d/runs") / f"results_{args.name.lower().replace('-','_')}.json"
    res_path.write_text(json.dumps({"brier": float(brier), "auc": float(auc)}, indent=2))

if __name__ == "__main__":
    main()
