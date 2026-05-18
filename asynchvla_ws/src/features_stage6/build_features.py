from __future__ import annotations
from collections import defaultdict
import torch
import torch.nn.functional as F

SIMVLA_PREFIX = 'simvla_seed'

def is_simvla_type(t: str) -> bool:
    return str(t).startswith(SIMVLA_PREFIX)

def action_geometry(action: torch.Tensor) -> torch.Tensor:
    a = action.float()
    first = a[0]
    last = a[-1]
    mean = a.mean(0)
    std = a.std(0, unbiased=False)
    maxabs = a.abs().max(0).values
    step_l2 = torch.linalg.vector_norm(a, dim=-1)
    chunk_mean_l2 = step_l2.mean().view(1)
    chunk_max_l2 = step_l2.max().view(1)
    smooth = torch.linalg.vector_norm(a[1:] - a[:-1], dim=-1).mean().view(1)
    if a.shape[0] >= 3:
        jerk = torch.linalg.vector_norm(a[2:] - 2 * a[1:-1] + a[:-2], dim=-1).mean().view(1)
    else:
        jerk = torch.zeros(1)
    grip = a[:, 6] if a.shape[-1] >= 7 else a[:, -1]
    grip_stats = torch.stack([grip.mean(), grip.std(unbiased=False), grip[0], grip[-1], grip.abs().max()])
    return torch.cat([a.flatten(), first, last, mean, std, maxabs, step_l2, chunk_mean_l2, chunk_max_l2, smooth, jerk, grip_stats])

def proprio_action_delta(action: torch.Tensor, proprio: torch.Tensor) -> torch.Tensor:
    a = action.float(); p = proprio.float()
    d = min(a.shape[-1], p.numel())
    ps = p[:d]
    first_delta = a[0, :d] - ps
    mean_delta = a[:, :d].mean(0) - ps
    cum = a[:, :d].sum(0)
    xyz_d = min(3, d)
    xyz_first = a[0, :xyz_d]
    xyz_last = a[-1, :xyz_d]
    xyz_cum = a[:, :xyz_d].sum(0)
    norms = torch.tensor([
        torch.linalg.vector_norm(first_delta).item(),
        torch.linalg.vector_norm(mean_delta).item(),
        torch.linalg.vector_norm(cum).item(),
        torch.linalg.vector_norm(xyz_first).item(),
        torch.linalg.vector_norm(xyz_last).item(),
        torch.linalg.vector_norm(xyz_cum).item(),
    ], dtype=torch.float32)
    return torch.cat([first_delta, mean_delta, cum, xyz_first, xyz_last, xyz_cum, norms])

def context_summary(pooled_vlm: torch.Tensor, proprio: torch.Tensor) -> torch.Tensor:
    v = pooled_vlm.float(); p = proprio.float()
    stats = torch.tensor([v.mean().item(), v.std(unbiased=False).item(), v.abs().mean().item(), v.abs().max().item(), p.mean().item(), p.std(unbiased=False).item(), p.abs().max().item()], dtype=torch.float32)
    return torch.cat([v, p, stats])

def build_seed_stats(rows):
    by_ctx = defaultdict(list)
    for r in rows:
        if is_simvla_type(r['candidate_type']):
            by_ctx[r['context_id']].append(r['candidate_action_normalized'].float())
    stats = {}
    for ctx, acts in by_ctx.items():
        stack = torch.stack(acts)
        mean = stack.mean(0)
        std = stack.std(0, unbiased=False).clamp_min(1e-4)
        pair = torch.cdist(stack.flatten(1), stack.flatten(1)) if len(acts) > 1 else torch.zeros(1,1)
        diversity = pair[pair > 0].mean() if (pair > 0).any() else torch.tensor(0.)
        stats[ctx] = {'stack': stack, 'mean': mean, 'std': std, 'diversity': diversity.float()}
    return stats

def seed_ensemble_features(row, seed_stats) -> torch.Tensor:
    a = row['candidate_action_normalized'].float()
    st = seed_stats.get(row['context_id'])
    if st is None:
        z = torch.zeros_like(a)
        return torch.cat([z.flatten(), z.flatten(), z.flatten(), z.flatten(), torch.zeros(14)])
    mean = st['mean']; std = st['std']; diff = a - mean; absdiff = diff.abs(); zscore = (diff / std).clamp(-10.0, 10.0)
    stack = st['stack']
    flat = a.flatten().view(1, -1); sflat = stack.flatten(1)
    dists = torch.cdist(flat, sflat).squeeze(0)
    # if candidate is one of the seed actions, nearest other excludes exact/near-zero self.
    nonzero = dists[dists > 1e-6]
    nearest = nonzero.min() if len(nonzero) else torch.tensor(0.)
    farthest = dists.max() if len(dists) else torch.tensor(0.)
    per_step = torch.linalg.vector_norm(diff, dim=-1)
    scalars = torch.cat([torch.linalg.vector_norm(diff).view(1), per_step, nearest.view(1), farthest.view(1), st['diversity'].view(1)])
    return torch.cat([mean.flatten(), std.flatten(), diff.flatten(), absdiff.flatten(), zscore.flatten(), scalars.float()])

def interaction_features(row, seed_stats=None) -> torch.Tensor:
    a = row['candidate_action_normalized'].float()
    geom = action_geometry(a)
    ctx = context_summary(row['pooled_vlm_features'], row['proprio'])
    act_summary = torch.cat([a.mean(0), a.std(0, unbiased=False), a[0], a[-1], torch.linalg.vector_norm(a, dim=-1)])
    ctx_short = torch.cat([ctx[:32], ctx[-7:]])
    n = min(act_summary.numel(), ctx_short.numel())
    prod = act_summary[:n] * ctx_short[:n]
    cos = F.cosine_similarity(F.pad(act_summary[:n], (0,0)).view(1,-1), ctx_short[:n].view(1,-1)).view(1)
    return torch.cat([act_summary, ctx_short, prod, cos])

def feature_vector(row, mode: str, seed_stats=None) -> torch.Tensor:
    a = row['candidate_action_normalized'].float()
    ctx = torch.cat([row['pooled_vlm_features'].float(), row['proprio'].float()])
    if mode == 'A0_action_flat': return a.flatten()
    if mode == 'A1_context': return ctx
    if mode == 'A2_full_old': return torch.cat([ctx, a.flatten()])
    if mode == 'F1_action_geometry': return action_geometry(a)
    if mode == 'F2_proprio_action_delta': return proprio_action_delta(a, row['proprio'])
    if mode == 'F3_seed_ensemble': return seed_ensemble_features(row, seed_stats or {})
    if mode == 'F4_context_action_interactions': return interaction_features(row, seed_stats)
    if mode == 'M2_engineered': return torch.cat([ctx, a.flatten(), action_geometry(a), proprio_action_delta(a,row['proprio']), seed_ensemble_features(row, seed_stats or {})])
    if mode == 'M4_seed_relative': return torch.cat([ctx, a.flatten(), seed_ensemble_features(row, seed_stats or {}), action_geometry(a)])
    if mode == 'M3_gated_base': return torch.cat([ctx, action_geometry(a), seed_ensemble_features(row, seed_stats or {})])
    raise KeyError(mode)
