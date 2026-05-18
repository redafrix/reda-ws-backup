from __future__ import annotations

import torch

FLOW_KEYS = [
    "initial_noise_norm",
    "final_action_norm",
    "velocity_norm_mean",
    "velocity_norm_max",
    "velocity_norm_final",
    "update_norm_mean",
    "update_norm_max",
    "update_norm_last",
    "total_path_length",
    "final_update_over_mean_update",
    "action_state_norm_mean",
    "action_state_norm_delta",
]


def flow_trace_vector(row: dict) -> torch.Tensor:
    meta = row.get("flow_trace_summary") or row.get("candidate_flow_trace_summary") or {}
    vals = []
    for key in FLOW_KEYS:
        value = meta.get(key, 0.0)
        if isinstance(value, torch.Tensor):
            value = value.detach().float().reshape(-1)[0].item() if value.numel() else 0.0
        vals.append(float(value))
    out = torch.tensor(vals, dtype=torch.float32)
    return torch.nan_to_num(out, nan=0.0, posinf=1e6, neginf=-1e6)
