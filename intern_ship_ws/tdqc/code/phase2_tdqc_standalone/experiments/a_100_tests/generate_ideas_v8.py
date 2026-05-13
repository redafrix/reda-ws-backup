import os, shutil
from pathlib import Path

def patch_file(path, old, new):
    if not os.path.exists(path): return
    with open(path, 'r') as f: content = f.read()
    with open(path, 'w') as f: f.write(content.replace(old, new))

base_idea = 'idea_166' # The Softplus Champion
for i in range(200, 250):
    new_idea = f'idea_{i}'
    if os.path.exists(new_idea): shutil.rmtree(new_idea)
    shutil.copytree(base_idea, new_idea)
    if (Path(new_idea) / 'runs').exists(): shutil.rmtree(Path(new_idea) / 'runs')
    
    model_path = Path(new_idea) / 'phase2_tdqc' / 'tdqc_model.py'
    train_path = Path(new_idea) / 'phase2_tdqc' / 'train_tdqc.py'

    # TIER 1: The "Physics Sentinel" Sweep (200-209)
    if 200 <= i <= 209:
        k_size = [3, 5, 7][(i-200)%3]
        smooth_code = f"""        # Physics Sentinel: Temporal Smoothing
        x_pad = F.pad(x.transpose(1, 2), ({k_size-1}, 0), mode='replicate')
        x_smooth = F.avg_pool1d(x_pad, kernel_size={k_size}, stride=1).transpose(1, 2)
        v1 = torch.zeros_like(x_smooth); v1[:, 1:, :] = x_smooth[:, 1:, :] - x_smooth[:, :-1, :]"""
        patch_file(model_path, "        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]", smooth_code)
        patch_file(model_path, "v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]", "v3 = torch.zeros_like(x_smooth); v3[:, 3:, :] = x_smooth[:, 3:, :] - x_smooth[:, :-3, :]")
        patch_file(model_path, "v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]", "v5 = torch.zeros_like(x_smooth); v5[:, 5:, :] = x_smooth[:, 5:, :] - x_smooth[:, :-5, :]")
        patch_file(model_path, "torch.cat([x,", "torch.cat([x_smooth,")

    # TIER 2: Uncertainty-Gated Derivatives (210-219)
    elif 210 <= i <= 219:
        gate_type = ['high_uncertainty_alert', 'low_uncertainty_trust'][(i-210)%2]
        if gate_type == 'high_uncertainty_alert':
            gate_code = "gate = torch.sigmoid(x[:, :, 14:22])"
        else:
            gate_code = "gate = 1.0 - torch.sigmoid(x[:, :, 14:22])"
        patch_file(model_path, "u_v1 = F.softplus(v1[:, :, 14:22])", f"{gate_code}\n        u_v1 = F.softplus(v1[:, :, 14:22]) * gate")

    # TIER 3: The "Anti-Drift" Calibration Loss (220-229)
    elif 220 <= i <= 229:
        lambda_drift = [0.01, 0.05, 0.1][(i-220)%3]
        drift_loss_code = f"""            # Anti-Drift Penalty
            q_diff = torch.abs(q_online[:, 1:] - q_online[:, :-1])
            drift_loss = (q_diff * batch['mask'][:, 1:]).mean() * {lambda_drift}
            loss = loss + drift_loss"""
        # Note the careful insertion before optim.zero_grad()
        patch_file(train_path, "            optim.zero_grad()", f"{drift_loss_code}\n            optim.zero_grad()")

    # TIER 4: Multi-Scale Softplus Fusion (230-239)
    elif 230 <= i <= 239:
        patch_file(model_path, "u_v1 = F.softplus(v1[:, :, 14:22])", "u_v1 = F.softplus(v1[:, :, 14:22])")
        patch_file(model_path, "u_v5 = F.softplus(v5[:, :, 14:22])", "u_v3 = F.softplus(v3[:, :, 14:22])\n        u_v5 = F.softplus(v5[:, :, 14:22])")
        patch_file(model_path, "torch.cat([x, v1, v3, v5, u_v1, u_v5]", "torch.cat([x, v1, v3, v5, u_v1, u_v3, u_v5]")
        patch_file(model_path, "in_d = input_dim * 4 + 16", "in_d = input_dim * 4 + 24")

    # TIER 5: Adaptive Focal Gamma (240-249)
    elif 240 <= i <= 249:
        gamma = [0.2, 0.5, 0.8, 1.2, 1.5][(i-240)%5]
        patch_file(train_path, "focal_gamma=1.0", f"focal_gamma={gamma}")

print('Marathon V8 Ideas (200-249) Generated: Physics Sentinel, Gated Uncertainty, and Anti-Drift Loss.')

# Final verification and fix for entry point
for i in range(200, 250):
    train_path = Path(f'idea_{i}') / 'phase2_tdqc' / 'train_tdqc.py'
    with open(train_path, 'a') as f:
        f.write("\nif __name__ == '__main__':\n    main()\n")
