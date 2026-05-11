import os, shutil
from pathlib import Path

def patch_file(path, old, new):
    if not os.path.exists(path): return
    with open(path, 'r') as f: content = f.read()
    with open(path, 'w') as f: f.write(content.replace(old, new))

# 1. Update the BASE loss function to support focal_gamma and weights natively
def prepare_base_loss(idea_path):
    loss_path = Path(idea_path) / 'phase2_tdqc' / 'tdqc_losses.py'
    new_loss_code = """
def tdqc_brier_td_loss(
    q_online: torch.Tensor,
    q_target: torch.Tensor,
    failure: torch.Tensor,
    lengths: torch.Tensor,
    mask: torch.Tensor,
    fail_weight: float = 1.0,
    success_weight: float = 1.0,
    focal_gamma: float = 0.0,
) -> torch.Tensor:
    with torch.no_grad():
        targets = make_td0_targets(q_target, failure, lengths, mask)
        sample_w = torch.where(
            failure > 0.5,
            torch.tensor(float(fail_weight), device=failure.device),
            torch.tensor(float(success_weight), device=failure.device),
        )
        weights = sample_w[:, None] * mask
        
        if focal_gamma > 0:
            confidence = 1.0 - torch.abs(q_online - targets)
            focal_w = (1.0 - confidence).pow(focal_gamma)
            weights = weights * focal_w

    losses = (q_online - targets).pow(2)
    loss = (losses * weights).sum() / weights.sum().clamp_min(1.0)
    return loss
"""
    # Replace the old function entirely
    with open(loss_path, 'r') as f: lines = f.readlines()
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(lines):
        if 'def tdqc_brier_td_loss' in line: start_idx = i
        if start_idx != -1 and 'return loss' in line: 
            end_idx = i + 1
            break
    if start_idx != -1 and end_idx != -1:
        lines[start_idx:end_idx] = [new_loss_code]
        with open(loss_path, 'w') as f: f.writelines(lines)

base_idea = 'idea_139' # The current 65% Recall champion
for i in range(145, 195):
    new_idea = f'idea_{i}'
    if os.path.exists(new_idea): shutil.rmtree(new_idea)
    shutil.copytree(base_idea, new_idea)
    if (Path(new_idea) / 'runs').exists(): shutil.rmtree(Path(new_idea) / 'runs')
    
    prepare_base_loss(new_idea)
    
    model_path = Path(new_idea) / 'phase2_tdqc' / 'tdqc_model.py'
    train_path = Path(new_idea) / 'phase2_tdqc' / 'train_tdqc.py'

    # TIER 1: Fusion Elite (145-154) - Log-Uncertainty + Focal Loss + Weights
    if 145 <= i <= 154:
        gamma = [0.5, 1.0, 1.5, 2.0][(i-145)%4]
        weight = [3.0, 5.0, 10.0][(i-145)//4] if (i-145)//4 < 3 else 3.0
        patch_file(train_path, 'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])',
                               f'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"], fail_weight={weight}, focal_gamma={gamma})')

    # TIER 2: Derivative Scale Sweep (155-164)
    elif 155 <= i <= 164:
        scales = [[1,2,3], [1,3,5], [1,5,10], [1,3,5,7,9], [1,2,3,4,5,6]][(i-155)%5]
        scale_code = "\n".join([f"        v{s} = torch.zeros_like(x); v{s}[:, {s}:, :] = x[:, {s}:, :] - x[:, :-{s}, :]" for s in scales])
        cat_code = f"torch.cat([x, {', '.join([f'v{s}' for s in scales])}, {', '.join([f'torch.log1p(torch.abs(v{s}[:, :, 14:22]))' for s in [scales[0], scales[-1]]])}], dim=-1)"
        
        full_code = f"""{scale_code}
        logits = self.head(self.mlp({cat_code})).squeeze(-1)"""
        
        patch_file(model_path, 'in_d = input_dim * 4 + 16', f'in_d = input_dim * {len(scales)+1} + 16')
        patch_file(model_path, """        v1 = torch.zeros_like(x); v1[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        v3 = torch.zeros_like(x); v3[:, 3:, :] = x[:, 3:, :] - x[:, :-3, :]
        v5 = torch.zeros_like(x); v5[:, 5:, :] = x[:, 5:, :] - x[:, :-5, :]
        # log-uncertainty deltas (cols 14-21)
        u_v1 = torch.log1p(torch.abs(v1[:, :, 14:22]))
        u_v5 = torch.log1p(torch.abs(v5[:, :, 14:22]))
        logits = self.head(self.mlp(torch.cat([x, v1, v3, v5, u_v1, u_v5], dim=-1))).squeeze(-1)""", full_code)

    # TIER 3: Non-linear Transforms on Uncertainty (165-174)
    elif 165 <= i <= 174:
        transform = ['torch.sqrt(torch.abs(v1[:, :, 14:22]))', 'F.softplus(v1[:, :, 14:22])', 'torch.tanh(v1[:, :, 14:22])', 'torch.log(torch.abs(v1[:, :, 14:22]) + 1e-3)'][(i-165)%4]
        patch_file(model_path, 'u_v1 = torch.log1p(torch.abs(v1[:, :, 14:22]))', f'u_v1 = {transform}')
        patch_file(model_path, 'u_v5 = torch.log1p(torch.abs(v5[:, :, 14:22]))', f'u_v5 = {transform.replace("v1", "v5")}')

    # TIER 4: Architectural Width Sweep (175-184)
    elif 175 <= i <= 184:
        h_dim = [128, 512, 1024][(i-175)%3]
        dropout = [0.1, 0.2, 0.3][(i-175)//4] if (i-175)//4 < 3 else 0.1
        patch_file(train_path, 'args = parse_args()', f'args = parse_args(); args.hidden_dim = {h_dim}; args.dropout = {dropout}')

    # TIER 5: Hybrid Robustness (185-194)
    elif 185 <= i <= 194:
        # 185: Force only derivatives
        if i == 185:
            patch_file(model_path, 'u_v1 = torch.log1p(torch.abs(v1[:, :, 14:22]))', 'u_v1 = v1[:, :, 0:6] # Force/Torque only')
            patch_file(model_path, 'u_v5 = torch.log1p(torch.abs(v5[:, :, 14:22]))', 'u_v5 = v5[:, :, 0:6]')
            patch_file(model_path, 'in_d = input_dim * 4 + 16', 'in_d = input_dim * 4 + 12')
        # 186-194: Mixed weighting and focal gamma
        else:
            gamma = 2.0 + (i-186)*0.1
            weight = 4.0
            patch_file(train_path, 'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"])',
                                   f'tdqc_brier_td_loss(q_online, q_target, batch["failure"], batch["lengths"], batch["mask"], fail_weight={weight}, focal_gamma={gamma})')

print('V7 Ideas 145-194 Generated. Fusion, Scales, and Architecture sweeps ready.')
