import os, shutil
from pathlib import Path

def patch_file(path, old, new):
    with open(path, 'r') as f: content = f.read()
    with open(path, 'w') as f: f.write(content.replace(old, new))

base_idea = 'idea_127' # The champion
for i in range(135, 145):
    new_idea = f'idea_{i}'
    if os.path.exists(new_idea): shutil.rmtree(new_idea)
    shutil.copytree(base_idea, new_idea)
    
    runs_dir = Path(new_idea) / 'runs'
    if runs_dir.exists(): shutil.rmtree(runs_dir)
    
    model_path = Path(new_idea) / 'phase2_tdqc' / 'tdqc_model.py'
    train_path = Path(new_idea) / 'phase2_tdqc' / 'train_tdqc.py'
    loss_path = Path(new_idea) / 'phase2_tdqc' / 'tdqc_losses.py'

    if i == 135: # Fine-Grained Scales {1, 2, 3, 4, 5}
        code = """        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        v2 = torch.zeros_like(x); v2[:, 2:, :] = x[:, 2:, :] - x[:, :-2, :]
        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]
        v4 = torch.zeros_like(x); v4[:, 4:, :] = x[:, 4:, :] - x[:, :-4, :]
        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]
        logits = self.head(self.mlp(torch.cat([x, v1, v2, v3, v4, v5], dim=-1))).squeeze(-1)"""
        patch_file(model_path, 'in_d = input_dim * 4', 'in_d = input_dim * 6')
        patch_file(model_path, '        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]\n        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]\n        logits = self.head(self.mlp(torch.cat([x, v1, v3, v5], dim=-1))).squeeze(-1)', code)

    elif i == 136: # Fibonacci Scales {1, 2, 3, 5, 8, 13}
        code = """        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        v2 = torch.zeros_like(x); v2[:, 2:, :] = x[:, 2:, :] - x[:, :-2, :]
        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]
        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]
        v8 = torch.zeros_like(x); v8[:, 8:, :] = x[:, 8:, :] - x[:, :-8, :]
        v13 = torch.zeros_like(x); v13[:, 13:, :] = x[:, 13:, :] - x[:, :-13, :]
        logits = self.head(self.mlp(torch.cat([x, v1, v2, v3, v5, v8, v13], dim=-1))).squeeze(-1)"""
        patch_file(model_path, 'in_d = input_dim * 4', 'in_d = input_dim * 7')
        patch_file(model_path, '        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]\n        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]\n        logits = self.head(self.mlp(torch.cat([x, v1, v3, v5], dim=-1))).squeeze(-1)', code)

    elif i == 137: # Class-Weighted TD Loss (3.0x Failure)
        patch_file(train_path, 'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])', 
                               'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"], fail_weight=3.0)')

    elif i == 138: # Class-Weighted TD Loss (5.0x Failure)
        patch_file(train_path, 'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])', 
                               'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"], fail_weight=5.0)')

    elif i == 139: # Log-Compressed Uncertainty Deltas
        code = """        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]
        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]
        # log-uncertainty deltas (cols 14-21)
        u_v1 = torch.log1p(torch.abs(v1[:, :, 14:22]))
        u_v5 = torch.log1p(torch.abs(v5[:, :, 14:22]))
        logits = self.head(self.mlp(torch.cat([x, v1, v3, v5, u_v1, u_v5], dim=-1))).squeeze(-1)"""
        patch_file(model_path, 'in_d = input_dim * 4', 'in_d = input_dim * 4 + 16')
        patch_file(model_path, '        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]\n        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]\n        logits = self.head(self.mlp(torch.cat([x, v1, v3, v5], dim=-1))).squeeze(-1)', code)

    elif i == 140: # Relative Jerk Features
        code = """        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]
        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]
        rel_v1 = v1 / (torch.abs(x) + 1e-6)
        logits = self.head(self.mlp(torch.cat([x, v1, v3, v5, rel_v1], dim=-1))).squeeze(-1)"""
        patch_file(model_path, 'in_d = input_dim * 4', 'in_d = input_dim * 5')
        patch_file(model_path, '        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]\n        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]\n        logits = self.head(self.mlp(torch.cat([x, v1, v3, v5], dim=-1))).squeeze(-1)', code)

    elif i == 141: # Second Order Derivatives (Position, Velocity, Acceleration)
        code = """        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        a = torch.zeros_like(x); a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]
        logits = self.head(self.mlp(torch.cat([x, v, a], dim=-1))).squeeze(-1)"""
        patch_file(model_path, 'in_d = input_dim * 4', 'in_d = input_dim * 3')
        patch_file(model_path, '        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]\n        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]\n        logits = self.head(self.mlp(torch.cat([x, v1, v3, v5], dim=-1))).squeeze(-1)', code)

    elif i == 142: # Focal Brier Loss (Gamma=2)
        code = """    losses = (q_online - targets).pow(2)
    # Focal weighting: (1 - confidence_in_correct_prediction)^gamma
    with torch.no_grad():
        confidence = 1.0 - torch.abs(q_online - targets)
        focal_w = (1.0 - confidence).pow(2.0)
    loss = (losses * weights * focal_w).sum() / (weights * focal_w).sum().clamp_min(1.0)"""
    
        patch_file(loss_path, '    losses = (q_online - targets).pow(2)\n    loss = (losses * weights).sum() / weights.sum().clamp_min(1.0)', code)

    elif i == 143: # Wide Range Deltas {1, 5, 10, 20} + 3x Weight
        code = """        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]
        v10 = torch.zeros_like(x); v10[:, 10:, :] = x[:, 10:, :] - x[:, :-10, :]
        v20 = torch.zeros_like(x); v20[:, 20:, :] = x[:, 20:, :] - x[:, :-20, :]
        logits = self.head(self.mlp(torch.cat([x, v1, v5, v10, v20], dim=-1))).squeeze(-1)"""
        patch_file(model_path, 'in_d = input_dim * 4', 'in_d = input_dim * 5')
        patch_file(model_path, '        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]\n        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]\n        logits = self.head(self.mlp(torch.cat([x, v1, v3, v5], dim=-1))).squeeze(-1)', code)
        patch_file(train_path, 'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])', 
                               'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"], fail_weight=3.0)')

    elif i == 144: # The V6 Elite: Fibonacci Scales + 3x Weight
        code = """        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        v2 = torch.zeros_like(x); v2[:, 2:, :] = x[:, 2:, :] - x[:, :-2, :]
        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]
        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]
        v8 = torch.zeros_like(x); v8[:, 8:, :] = x[:, 8:, :] - x[:, :-8, :]
        logits = self.head(self.mlp(torch.cat([x, v1, v2, v3, v5, v8], dim=-1))).squeeze(-1)"""
        patch_file(model_path, 'in_d = input_dim * 4', 'in_d = input_dim * 6')
        patch_file(model_path, '        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]\n        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]\n        logits = self.head(self.mlp(torch.cat([x, v1, v3, v5], dim=-1))).squeeze(-1)', code)
        patch_file(train_path, 'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])', 
                               'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"], fail_weight=3.0)')

print('V6 Ideas 135-144 Generated with Smart Refinements.')
