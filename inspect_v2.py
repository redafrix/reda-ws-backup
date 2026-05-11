import torch
import os

path = "intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/final_calibrated_3924rollouts_v2.pt"
if not os.path.exists(path):
    print(f"File not found: {path}")
    exit(1)

data = torch.load(path)
episodes = data['episodes']
print(f"Total episodes: {len(episodes)}")

type_A_count = 0
type_B_count = 0

for i, ep in enumerate(episodes):
    feats = torch.tensor(ep['features'])
    if feats.shape[0] == 0:
        continue
    
    # check if indices 1,3,5,7 are exactly 0
    if (feats[:, 1] == 0.0).all() and (feats[:, 3] == 0.0).all():
        type_A_count += 1
        if type_A_count == 1:
            print(f"\nExample 'Misaligned/External' episode ({i}) features (first step):")
            print(feats[0])
    else:
        type_B_count += 1
        if type_B_count == 1:
            print(f"\nExample 'Correct/Online' episode ({i}) features (first step):")
            print(feats[0])

print(f"\nTotal Misaligned/External (zeros at 1,3,5,7): {type_A_count}")
print(f"Total Correct/Online (fully populated): {type_B_count}")
