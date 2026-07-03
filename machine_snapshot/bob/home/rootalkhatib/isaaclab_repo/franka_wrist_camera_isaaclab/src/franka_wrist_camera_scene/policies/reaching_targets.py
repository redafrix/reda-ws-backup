"""Pure Python target computation for reaching policies."""

from __future__ import annotations

import torch
from ..control.motion_primitives import MinimumJerkPositionMotion


def quat_apply_xyzw(quat: torch.Tensor, vec: torch.Tensor) -> torch.Tensor:
    """Apply an XYZW quaternion rotation to a vector."""
    xyz = quat[:, :3]
    t = torch.cross(xyz, vec, dim=-1) * 2.0
    return vec + quat[:, 3:4] * t + torch.cross(xyz, t, dim=-1)


def compute_reaching_targets(
    sim_time_s: float,
    state: str,
    state_start_time: float | None,
    motion: MinimumJerkPositionMotion | None,
    ee_pos_w: torch.Tensor,
    ee_quat_w: torch.Tensor,
    reach_pos_w: torch.Tensor,
    tcp_offset_local: torch.Tensor,
    direct_reach_max_speed_m_s: float,
    reach_dwell_s: float,
    target_quat_w: torch.Tensor | None = None,
) -> tuple[torch.Tensor, str, float | None, MinimumJerkPositionMotion | None, bool]:
    """Compute the next reaching hand position command.
    
    This function has no Isaac Sim dependencies and is fully deterministic and testable.
    """
    # Compute current TCP position
    tcp_offset_w = quat_apply_xyzw(ee_quat_w, tcp_offset_local.expand(ee_pos_w.shape[0], -1))
    current_tcp_pos_w = ee_pos_w + tcp_offset_w

    done = False
    new_state = state
    new_state_start_time = state_start_time
    new_motion = motion

    if state == "move_to_target":
        if motion is None:
            new_motion = MinimumJerkPositionMotion.from_speed(
                start_pos_w=current_tcp_pos_w,
                goal_pos_w=reach_pos_w,
                start_time_s=sim_time_s,
                max_speed_m_s=direct_reach_max_speed_m_s,
            )
            motion = new_motion
        desired_tcp_pos_w, finished = motion.sample(sim_time_s)
        if finished:
            new_state = "reach_dwell"
            new_state_start_time = sim_time_s
            new_motion = None
    elif state == "reach_dwell":
        desired_tcp_pos_w = reach_pos_w
        if state_start_time is None:
            new_state_start_time = sim_time_s
            state_start_time = sim_time_s
        if sim_time_s - state_start_time >= reach_dwell_s:
            done = True
    else:
        raise ValueError(f"Unsupported reaching policy state: {state!r}")

    # Convert desired TCP position to a hand-body position using the orientation
    # that will be commanded with that hand position.
    command_quat_w = ee_quat_w if target_quat_w is None else target_quat_w
    tcp_offset_w_command = quat_apply_xyzw(command_quat_w, tcp_offset_local.expand(ee_pos_w.shape[0], -1))
    target_hand_pos_w = desired_tcp_pos_w - tcp_offset_w_command

    return target_hand_pos_w, new_state, new_state_start_time, new_motion, done
