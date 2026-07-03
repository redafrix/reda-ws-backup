import torch
import numpy as np
import sys
sys.path.append('/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests/idea_166')
from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator
from torch.utils.data import DataLoader

# Load dataset without truncation (max_horizon = 1000)
d_val = TDQCDataset('/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_unseen_obj_ood.pt', max_horizon=1000, is_train=False)
loader = DataLoader(d_val, batch_size=64, shuffle=False, collate_fn=tdqc_collate)

ckpt = torch.load('/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests/idea_166/runs/best.pt', map_location='cpu')
cfg = ckpt['config']
model = TDQCTransformerCalibrator(input_dim=d_val.input_dim, hidden_dim=cfg['hidden_dim'], num_layers=cfg['num_layers'])
model.load_state_dict(ckpt['model'])
mean = ckpt['mean']
std = ckpt['std']
model.eval()

threshold = 0.5
lead_times = []
false_positives = 0
true_positives = 0
total_failures = 0
total_successes = 0

with torch.no_grad():
    for batch in loader:
        x = normalize_features(batch["features"], mean, std)
        q = model(x, mask=batch["mask"])
        
        for b in range(q.shape[0]):
            is_fail = int(batch["failure"][b].item())
            L = int(batch["lengths"][b].item())
            probs = q[b, :L].numpy()
            
            crossed = (probs >= threshold).nonzero()[0]
            if len(crossed) > 0:
                first_step = crossed[0].item()
                if is_fail:
                    true_positives += 1
                    lead_times.append(L - first_step)
                else:
                    false_positives += 1
            
            if is_fail:
                total_failures += 1
            else:
                total_successes += 1

print(f"--- Full Horizon Evaluation (No Truncation, Threshold={threshold}) ---")
print(f"Total Failures: {total_failures} | Total Successes: {total_successes}")
print(f"Detection Recall: {true_positives/max(total_failures, 1):.2%}")
print(f"False Positive Rate: {false_positives/max(total_successes, 1):.2%}")
if lead_times:
    print(f"Mean Lead Time: {np.mean(lead_times):.1f} steps")
    print(f"Median Lead Time: {np.median(lead_times):.1f} steps")
    print(f"P90 Lead Time: {np.percentile(lead_times, 90):.1f} steps")
else:
    print("No detections found.")
print("-----------------------------------------------------------------")
