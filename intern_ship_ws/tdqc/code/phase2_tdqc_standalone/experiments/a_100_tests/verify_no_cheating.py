import torch
import torch.nn as nn
import numpy as np
import os
import argparse
from phase2_tdqc.tdqc_model import TDQCTransformerCalibrator
from phase2_tdqc.tdqc_dataset import TDQCDataset
from phase2_tdqc.tdqc_features import normalize_features

def run_timer_test(model, mean, std, device):
    print("\n--- Test 1: Timer Trap Check (Constant State) ---")
    dummy_input = torch.zeros((1, 500, 22)).to(device)
    dummy_input = normalize_features(dummy_input, mean, std)
    with torch.no_grad():
        probs = model(dummy_input).cpu().numpy().flatten()
    
    print(f"Prob at step 10: {probs[10]:.6f}")
    print(f"Prob at step 490: {probs[490]:.6f}")
    drift = probs[490] - probs[10]
    print(f"Drift over 480 steps: {drift:.6f}")
    
    if abs(drift) > 0.01:
        print("[!] WARNING: Model shows temporal drift.")
    else:
        print("[✓] PASSED: Model is temporally stable.")

def run_ablation_sweep(model, dataset, mean, std, device):
    print("\n--- Test 2: Ablation Sweep ---")
    
    def get_recall(ds, mode='none'):
        all_detected = 0
        total_fails = 0
        
        for episode in ds.episodes:
            x = episode.features.unsqueeze(0)
            
            if mode == 'mask_u':
                x[:, :, 14:22] = 0
            elif mode == 'mask_all_deltas':
                # Model internally calculates v1, v3, v5. 
                # To 'mask' them, we make the input static.
                # Since the model calculates v1 = x[t] - x[t-1], 
                # if we make x[t] = x[0] for all t, all deltas become 0.
                x = x[:, 0:1, :].repeat(1, x.shape[1], 1)
            
            x = x.to(device)
            x = normalize_features(x, mean, std)
            with torch.no_grad():
                probs = model(x).cpu().numpy().flatten()
            
            if episode.failure:
                total_fails += 1
                if (probs > 0.5).any():
                    all_detected += 1
        
        return all_detected / (total_fails + 1e-9)

    orig = get_recall(dataset, mode='none')
    mask_u = get_recall(dataset, mode='mask_u')
    mask_static = get_recall(dataset, mode='mask_all_deltas')
    
    print(f"Original Recall: {orig*100:.2f}%")
    print(f"Recall (Mask Uncertainty): {mask_u*100:.2f}%")
    print(f"Recall (Static/No-Deltas): {mask_static*100:.2f}%")
    
    if mask_static < 0.2:
        print("[✓] PASSED: Model is strictly derivative-based (Vibration Sensitive).")
    else:
        print("[!] WARNING: Model can predict failure from static state alone (Bias).")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--idea', type=str, default='idea_166')
    args = parser.parse_args()
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    base_path = f'/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests/{args.idea}'
    ckpt_path = f'{base_path}/runs/best.pt'
    
    ckpt = torch.load(ckpt_path, map_location='cpu')
    config = ckpt['config']
    
    model = TDQCTransformerCalibrator(input_dim=22, hidden_dim=config['hidden_dim'], num_layers=config['num_layers']).to(device)
    model.load_state_dict(ckpt['model']); model.eval()
    mean, std = ckpt['mean'].to(device), ckpt['std'].to(device)
    
    ds_path = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_unseen_obj_ood.pt'
    dataset = TDQCDataset(ds_path, is_train=False)
    
    run_timer_test(model, mean, std, device)
    run_ablation_sweep(model, dataset, mean, std, device)
