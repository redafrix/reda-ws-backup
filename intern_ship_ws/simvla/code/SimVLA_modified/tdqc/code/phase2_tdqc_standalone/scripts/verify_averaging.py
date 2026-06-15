import torch
from torch.utils.data import DataLoader
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator
import numpy as np

def verify(ckpt_path, dataset_path, horizon=100):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    ckpt = torch.load(ckpt_path, map_location="cpu")
    model = TDQCLSTMCalibrator(
        input_dim=ckpt["config"]["input_dim"],
        hidden_dim=ckpt["config"]["hidden_dim"],
        num_layers=ckpt["config"]["num_layers"]
    ).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()
    mean, std = ckpt["mean"].to(device), ckpt["std"].to(device)
    
    dataset = TDQCDataset(dataset_path)
    n_total = len(dataset)
    n_train, n_val = int(0.7 * n_total), int(0.15 * n_total)
    _, _, test_set = torch.utils.data.random_split(
        dataset, [n_train, n_val, n_total - n_train - n_val],
        generator=torch.Generator().manual_seed(0)
    )
    loader = DataLoader(test_set, batch_size=64, shuffle=False, collate_fn=tdqc_collate)
    
    total_sq_err = 0.0
    total_frames = 0.0
    episode_briers = []
    
    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
            q = model(normalize_features(batch["features"], mean, std), batch["lengths"])
            target = batch["failure"][:, None].expand_as(q)
            mask = batch["mask"]
            
            if q.shape[1] > horizon:
                mask[:, horizon:] = 0.0
            
            sq_err = (q - target).pow(2) * mask
            
            # Global method accumulator
            total_sq_err += sq_err.sum().item()
            total_frames += mask.sum().item()
            
            # Episode-wise method
            for b in range(q.shape[0]):
                ep_mask = mask[b]
                ep_steps = ep_mask.sum().item()
                if ep_steps > 0:
                    ep_sq_err = sq_err[b].sum().item()
                    episode_briers.append(ep_sq_err / ep_steps)

    method1_score = np.mean(episode_briers)
    method2_score = total_sq_err / total_frames
    
    print(f"Horizon: {horizon}")
    print(f"Method 1 (Episode-wise Average): {method1_score:.6f}")
    print(f"Method 2 (Global Frame Average): {method2_score:.6f}")

if __name__ == "__main__":
    # Default paths relative to phase2_tdqc_standalone root
    verify("results/checkpoints/lstm_td0_final_polish_v2/best.pt", "data/final_calibrated_3751rollouts.pt")
