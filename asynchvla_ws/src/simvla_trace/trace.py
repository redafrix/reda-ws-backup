from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

import torch


@dataclass(frozen=True)
class TraceConfig:
    steps: int = 10
    seed: int = 0
    return_initial_noise: bool = False
    return_flow_trace: bool = True


def _safe_float(x: torch.Tensor) -> float:
    return float(x.detach().float().cpu())


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
    return_flow_trace: bool = True,
) -> Dict[str, Any]:
    """Non-breaking trace wrapper for SmolVLM-VLA flow-matching inference.

    This intentionally does not use trajectory timestep, episode progress,
    episode length, or success/failure labels. It leaves the model's original
    generate_actions() path untouched and only exposes compact side-channel
    metadata useful for uncertainty-rater experiments.
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
    initial_noise_norm = torch.linalg.vector_norm(x_t.reshape(B, -1), dim=-1)

    dt = -1.0 / steps
    t_value = 1.0
    flow_steps: List[Dict[str, float]] = []
    velocity_norms: List[torch.Tensor] = []
    update_norms: List[torch.Tensor] = []
    action_state_norms: List[torch.Tensor] = [torch.linalg.vector_norm(x_t.reshape(B, -1), dim=-1)]
    prev_x = x_t

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
        else:
            v_t = pred
            logvar_t = None

        update = dt * v_t
        velocity_norm = torch.linalg.vector_norm(v_t.reshape(B, -1), dim=-1)
        update_norm = torch.linalg.vector_norm(update.reshape(B, -1), dim=-1)
        velocity_norms.append(velocity_norm)
        update_norms.append(update_norm)

        step_meta: Dict[str, float] = {
            "t": float(t_value),
            "dt": float(dt),
            "velocity_mean": _safe_float(v_t.mean()),
            "velocity_abs_mean": _safe_float(v_t.abs().mean()),
            "velocity_norm_mean": _safe_float(velocity_norm.mean()),
            "velocity_norm_max": _safe_float(velocity_norm.max()),
            "update_norm_mean": _safe_float(update_norm.mean()),
            "update_norm_max": _safe_float(update_norm.max()),
        }
        if logvar_t is not None:
            step_meta["logvar_mean"] = _safe_float(logvar_t.mean())
            step_meta["logvar_abs_mean"] = _safe_float(logvar_t.abs().mean())
        flow_steps.append(step_meta)

        prev_x = x_t
        x_t = x_t + update
        action_state_norms.append(torch.linalg.vector_norm(x_t.reshape(B, -1), dim=-1))
        t_value = t_value + dt

    generated_normalized_action = x_t
    generated_postprocessed_action = model.action_space.postprocess(generated_normalized_action)

    velocity_stack = torch.stack(velocity_norms, dim=1) if velocity_norms else torch.zeros(B, 0, device=device, dtype=dtype)
    update_stack = torch.stack(update_norms, dim=1) if update_norms else torch.zeros(B, 0, device=device, dtype=dtype)
    action_norm_stack = torch.stack(action_state_norms, dim=1)
    final_action_norm = torch.linalg.vector_norm(generated_normalized_action.reshape(B, -1), dim=-1)
    total_path_length = update_stack.sum(dim=1) if update_stack.numel() else torch.zeros(B, device=device, dtype=dtype)
    mean_update = update_stack.mean(dim=1) if update_stack.numel() else torch.zeros(B, device=device, dtype=dtype)
    last_update = update_stack[:, -1] if update_stack.numel() else torch.zeros(B, device=device, dtype=dtype)
    ratio_final_mean = last_update / (mean_update + 1e-8)

    flow_trace_summary: Dict[str, torch.Tensor] = {
        "initial_noise_norm": initial_noise_norm,
        "final_action_norm": final_action_norm,
        "velocity_norm_mean": velocity_stack.mean(dim=1) if velocity_stack.numel() else torch.zeros(B, device=device, dtype=dtype),
        "velocity_norm_max": velocity_stack.max(dim=1).values if velocity_stack.numel() else torch.zeros(B, device=device, dtype=dtype),
        "velocity_norm_final": velocity_stack[:, -1] if velocity_stack.numel() else torch.zeros(B, device=device, dtype=dtype),
        "update_norm_mean": mean_update,
        "update_norm_max": update_stack.max(dim=1).values if update_stack.numel() else torch.zeros(B, device=device, dtype=dtype),
        "update_norm_last": last_update,
        "total_path_length": total_path_length,
        "final_update_over_mean_update": ratio_final_mean,
        "action_state_norm_mean": action_norm_stack.mean(dim=1),
        "action_state_norm_delta": action_norm_stack[:, -1] - action_norm_stack[:, 0],
    }

    out: Dict[str, Any] = {
        "generated_normalized_action": generated_normalized_action,
        "generated_postprocessed_action": generated_postprocessed_action,
        "pooled_vlm_features": pooled_vlm_features,
        "vlm_feature_shape": tuple(vlm_features.shape),
        "proprio": proprio,
        "proprio_norm": proprio_norm,
        "seed": int(seed),
        "num_flow_steps": len(flow_steps),
        "flow_steps": flow_steps if return_flow_trace else [],
        "flow_trace_summary": flow_trace_summary if return_flow_trace else {},
    }
    if initial_noise is not None:
        out["initial_noise"] = initial_noise
    return out
