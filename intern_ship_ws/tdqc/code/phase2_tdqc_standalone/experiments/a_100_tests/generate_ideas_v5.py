import os, shutil
from pathlib import Path

def patch_file(path, old, new):
    with open(path, 'r') as f: content = f.read()
    with open(path, 'w') as f: f.write(content.replace(old, new))

base_idea = 'idea_118'
for i in range(133, 135):
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
    
    if i == 133: # Derivative of Uncertainty ONLY
        code = """        # features [14:21] are uncertainty summaries
        u = x[:, :, 14:22]
        du = torch.zeros_like(u); du[:, 1:, :] = u[:, 1:, :] - u[:, :-1, :]
        d2u = torch.zeros_like(u); d2u[:, 1:, :] = du[:, 1:, :] - du[:, :-1, :]
        logits = self.head(self.mlp(torch.cat([x, du, d2u], dim=-1))).squeeze(-1)"""
        patch_file(model_path, 'in_d = input_dim * 3', 'in_d = input_dim + 16')
        patch_file(model_path, '        v = torch.zeros_like(x)\n        v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]\n        a = torch.zeros_like(x)\n        a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]\n        logits = self.head(self.mlp(torch.cat([x, v, a], dim=-1))).squeeze(-1)', code)

    elif i == 134: # MC Loss + HiddenDim=256
        patch_file(train_path, 'args = parse_args()', 'args = parse_args(); args.hidden_dim = 256')
        patch_file(train_path, 'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])', 
                               'tdqc_mc_brier_loss(q_online, batch["failure"], batch["mask"])')

print('V5 Ideas 133-134 Regenerated with Architecture, Import, and GPU Speed fixes.')
