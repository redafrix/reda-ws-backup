import torch

def inspect_dataset(path):
    data = torch.load(path)
    episodes = data['episodes']
    print(f"Total episodes: {len(episodes)}")
    
    # Check values for episode 0 and 15
    for i in [0, 15]:
        feats = torch.tensor(episodes[i]['features'])
        print(f"\nEpisode {i} features (first 5 steps):")
        print(f"Indices 2, 3 (first step): {feats[:5, 2:4]}")
        print(f"Indices 6, 7 (gripper): {feats[:5, 6:8]}")

if __name__ == "__main__":
    inspect_dataset("intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/final_calibrated_3751rollouts.pt")
