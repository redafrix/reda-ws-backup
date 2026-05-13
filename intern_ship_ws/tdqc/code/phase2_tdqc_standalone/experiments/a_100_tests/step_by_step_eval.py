import argparse, torch, numpy as np
from pathlib import Path
from torch.utils.data import DataLoader
from sklearn.metrics import roc_auc_score, brier_score_loss, recall_score
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset_path", required=True)
    p.add_argument("--ckpt", required=True)
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--device", default="cuda")
    p.add_argument("--max_steps", type=int, default=150)
    return p.parse_args()

@torch.no_grad()
def main():
    args = parse_args()
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    dataset = TDQCDataset(args.dataset_path, max_horizon=args.max_steps, is_train=False)
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=False, collate_fn=tdqc_collate)
    
    ckpt = torch.load(args.ckpt, map_location="cpu")
    cfg = ckpt["config"]
    model = TDQCTransformerCalibrator(input_dim=dataset.input_dim, hidden_dim=cfg["hidden_dim"], num_layers=cfg["num_layers"]).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()
    
    mean, std = ckpt["mean"].to(device), ckpt["std"].to(device)

    # Dictionary to store labels and probs per timestep
    # key: timestep (0 to 149), value: list of [label, prob]
    step_data = {t: {'labels': [], 'probs': []} for t in range(args.max_steps)}

    for batch in loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, mask=batch["mask"])
        
        for b in range(q.shape[0]):
            L = int(batch["lengths"][b].item())
            is_fail = int(batch["failure"][b].item())
            probs = q[b, :L].cpu().numpy()
            
            for t in range(L):
                if t < args.max_steps:
                    step_data[t]['labels'].append(is_fail)
                    step_data[t]['probs'].append(probs[t])

    print(f"Timestep | Samples | Brier | AUC-ROC | Avg Prob Fail | Avg Prob Succ")
    print("---------|---------|-------|---------|---------------|---------------")
    
    for t in range(0, args.max_steps, 10): # Print every 10 steps to keep it readable
        labels = np.array(step_data[t]['labels'])
        probs = np.array(step_data[t]['probs'])
        
        if len(np.unique(labels)) < 2:
            auc = 0.0
        else:
            auc = roc_auc_score(labels, probs)
            
        brier = brier_score_loss(labels, probs)
        
        fail_mask = (labels == 1)
        succ_mask = (labels == 0)
        
        avg_p_fail = np.mean(probs[fail_mask]) if any(fail_mask) else 0.0
        avg_p_succ = np.mean(probs[succ_mask]) if any(succ_mask) else 0.0
        
        print(f"{t:8d} | {len(labels):7d} | {brier:.4f} | {auc:.4f}  | {avg_p_fail:.4f}        | {avg_p_succ:.4f}")

if __name__ == "__main__":
    main()
