import os, shutil
from pathlib import Path

def patch_file(path, old, new):
    with open(path, 'r') as f: content = f.read()
    with open(path, 'w') as f: f.write(content.replace(old, new))

base_idea = 'idea_118'
for i in range(125, 135):
    new_idea = f'idea_{i}'
    if os.path.exists(new_idea): shutil.rmtree(new_idea)
    shutil.copytree(base_idea, new_idea)
    
    # Remove existing runs folder if it was copied
    runs_dir = Path(new_idea) / 'runs'
    if runs_dir.exists(): shutil.rmtree(runs_dir)
    
    model_path = Path(new_idea) / 'phase2_tdqc' / 'tdqc_model.py'
    train_path = Path(new_idea) / 'phase2_tdqc' / 'train_tdqc.py'
    
    # ADD MISSING IMPORTS TO train_path
    patch_file(train_path, 'from phase2_tdqc.tdqc_losses import tdqc_brier_td_loss, sequential_brier_score', 
                           'from phase2_tdqc.tdqc_losses import tdqc_brier_td_loss, tdqc_mc_brier_loss, sequential_brier_score')
    
    if i == 125: # MC Loss
        patch_file(train_path, 'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])', 
                               'tdqc_mc_brier_loss(q_online, batch["failure"], batch["mask"])')
    
    elif i == 126: # TD Loss + FailWeight=5
        patch_file(train_path, 'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])', 
                               'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"], fail_weight=5.0)')
                               
    elif i == 127: # Multi-Scale Delta (1, 3, 5)
        code = """        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]
        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]
        logits = self.head(self.mlp(torch.cat([x, v1, v3, v5], dim=-1))).squeeze(-1)"""
        patch_file(model_path, 'in_d = input_dim * 3', 'in_d = input_dim * 4')
        patch_file(model_path, '        v = torch.zeros_like(x)\n        v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        a = torch.zeros_like(x)\n        a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]\n        logits = self.head(self.mlp(torch.cat([x, v, a], dim=-1))).squeeze(-1)', code)

    elif i == 128: # Multi-Scale Delta (1, 10, 30)
        code = """        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        v10 = torch.zeros_like(x); v10[:, 10:, :] = x[:, 10:, :] - x[:, :-10, :]
        v30 = torch.zeros_like(x); v30[:, 30:, :] = x[:, 30:, :] - x[:, :-30, :]
        logits = self.head(self.mlp(torch.cat([x, v1, v10, v30], dim=-1))).squeeze(-1)"""
        patch_file(model_path, 'in_d = input_dim * 3', 'in_d = input_dim * 4')
        patch_file(model_path, '        v = torch.zeros_like(x)\n        v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        a = torch.zeros_like(x)\n        a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]\n        logits = self.head(self.mlp(torch.cat([x, v, a], dim=-1))).squeeze(-1)', code)

    elif i == 129: # MC Loss + FailWeight=5
        patch_file(train_path, 'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])', 
                               'tdqc_mc_brier_loss(q_online, batch["failure"], batch["mask"], fail_weight=5.0)')

    elif i == 130: # 118 + Deeper MLP (3 layers)
        patch_file(train_path, 'num_layers=args.num_layers', 'num_layers=3')

    elif i == 131: # Hybrid MC/TD Loss
        patch_file(train_path, 'loss = tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])', 
                               'loss = 0.5 * tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"]) + 0.5 * tdqc_mc_brier_loss(q_online, batch["failure"], batch["mask"])')

    elif i == 132: # Log-Compressed Derivatives
        code = """        v = torch.zeros_like(x); v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        a = torch.zeros_like(x); a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]
        v = v.sign() * torch.log1p(v.abs())
        a = a.sign() * torch.log1p(a.abs())
        logits = self.head(self.mlp(torch.cat([x, v, a], dim=-1))).squeeze(-1)"""
        patch_file(model_path, '        v = torch.zeros_like(x)\n        v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        a = torch.zeros_like(x)\n        a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]\n        logits = self.head(self.mlp(torch.cat([x, v, a], dim=-1))).squeeze(-1)', code)

    elif i == 133: # Derivative of Uncertainty ONLY
        code = """        # features [14:21] are uncertainty summaries
        u = x[:, :, 14:22]
        du = torch.zeros_like(u); du[:, 1:, :] = u[:, 1:, :] - u[:, :-1, :]
        d2u = torch.zeros_like(u); d2u[:, 1:, :] = du[:, 1:, :] - du[:, :-1, :]
        logits = self.head(self.mlp(torch.cat([x, du, d2u], dim=-1))).squeeze(-1)"""
        patch_file(model_path, 'in_d = input_dim * 3', 'in_d = input_dim + 16')
        patch_file(model_path, '        v = torch.zeros_like(x)\n        v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        a = torch.zeros_like(x)\n        a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]\n        logits = self.head(self.mlp(torch.cat([x, v, a], dim=-1))).squeeze(-1)', code)

    elif i == 134: # MC Loss + HiddenDim=256
        patch_file(train_path, 'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])', 
                               'tdqc_mc_brier_loss(q_online, batch["failure"], batch["mask"])')
        patch_file(train_path, 'hidden_dim=args.hidden_dim', 'hidden_dim=256')

print('V5 Ideas 125-134 Regenerated with imports fixed.')
