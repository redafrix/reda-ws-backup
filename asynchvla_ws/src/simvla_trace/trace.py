from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

import torch


@dataclass(frozen=True)
class TraceConfig:
    steps: int = 10
    seed: int = 0
    return_initial_noise: bool = False


@torch.no_grad()
def generate_actions_trace(
    model,
    *,
    input_ids: torch.LongTensor,
    image_input: torch.FloatTensor,
    image_mask: torch.Tensor,
    proprio: torch.Tensor,
    steps: int = 10,
    seed: int = 0,
    return_initial_noise: bool = False,
) -> Dict[str, Any]:
    """Non-breaking trace wrapper for SmolVLM-VLA flow-matching inference.

    This intentionally does not use trajectory timestep, episode progress,
    episode length, or success/failure labels.
    """
    model.eval()
    device = proprio.device
    dtype = proprio.dtype
    B = input_ids.shape[0]
    D = model.action_space.dim_action
    steps = max(1, int(steps))

    enc = model.forward_vlm_efficient(image_input, image_mask, input_ids)
    vlm_features = enc["vlm_features"]
    pooled_vlm_features = vlm_features.mean(dim=1)

    if hasattr(model.action_space, "normalize_state"):
        proprio_norm = model.action_space.normalize_state(proprio)
    elif hasattr(model.action_space, "normalize"):
        proprio_norm = model.action_space.normalize(proprio)
    else:
        proprio_norm = proprio

    generator = torch.Generator(device=device)
    generator.manual_seed(int(seed))
    x_t = torch.randn(B, model.num_actions, D, device=device, dtype=dtype, generator=generator)
    initial_noise = x_t.detach().clone() if return_initial_noise else None

    dt = -1.0 / steps
    t_value = 1.0
    flow_steps = []
    while t_value > -dt / 2:
        t_tensor = torch.full((B,), t_value, device=device, dtype=dtype)
        pred = model.transformer(
            vlm_features=vlm_features,
            action_with_noise=x_t,
            proprio=proprio_norm,
            t=t_tensor,
        )
        if getattr(model.config, "predict_uncertainty", False):
            v_t, logvar_t = pred
            flow_steps.append({
                "t": float(t_value),
                "dt": float(dt),
                "velocity_mean": float(v_t.detach().mean().cpu()),
                "logvar_mean": float(logvar_t.detach().mean().cpu()),
            })
        else:
            v_t = pred
            flow_steps.append({
                "t": float(t_value),
                "dt": float(dt),
                "velocity_mean": float(v_t.detach().mean().cpu()),
            })
        x_t = x_t + dt * v_t
        t_value = t_value + dt

    generated_normalized_action = x_t
    generated_postprocessed_action = model.action_space.postprocess(generated_normalized_action)

    out: Dict[str, Any] = {
        "generated_normalized_action": generated_normalized_action,
        "generated_postprocessed_action": generated_postprocessed_action,
        "pooled_vlm_features": pooled_vlm_features,
        "vlm_feature_shape": tuple(vlm_features.shape),
        "proprio": proprio,
        "proprio_norm": proprio_norm,
        "seed": int(seed),
        "num_flow_steps": len(flow_steps),
        "flow_steps": flow_steps,
    }
    if initial_noise is not None:
        out["initial_noise"] = initial_noise
    return out
