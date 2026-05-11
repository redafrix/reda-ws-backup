import torch
import torch.nn.functional as F
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator
from phase2_tdqc.tdqc_features import compute_feature_stats, normalize_features
from torch.utils.data import DataLoader

def debug():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dataset = TDQCDataset("../../../data/v8_balanced/v8_train.pt")
    loader = DataLoader(dataset, batch_size=64, collate_fn=tdqc_collate)
    
    stats = compute_feature_stats(torch.cat([ep.features for ep in dataset.episodes[:100]]), None)
    mean, std = stats["mean"].to(device), stats["std"].to(device)
    
    model = TDQCTransformerCalibrator(
        input_dim=dataset.input_dim,
        hidden_dim=256,
        n_heads=8,
        num_layers=4,
    ).to(device)
    
    batch = next(iter(loader))
    batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
    x = normalize_features(batch["features"], mean, std)
    
    # Run forward through model
    q = model(x, mask=batch["mask"])
    print("Model Output NaNs:", torch.isnan(q).any().item())
    if not torch.isnan(q).any():
        print("Model Output min/max:", q.min().item(), q.max().item())

if __name__ == "__main__":
    debug()
