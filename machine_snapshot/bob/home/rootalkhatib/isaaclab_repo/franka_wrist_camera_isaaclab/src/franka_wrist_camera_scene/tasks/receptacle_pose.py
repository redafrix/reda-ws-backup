"""Scene pose queries for pick-place receptacles."""

from __future__ import annotations

import torch
from isaaclab.scene import InteractiveScene

from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
from franka_wrist_camera_scene.utils.tensors import as_torch


def placement_target_root_pos_w(scene: InteractiveScene, spec: PickPlaceTaskSpec) -> torch.Tensor:
    """Return the current managed receptacle root position in world coordinates."""
    if spec.placement_target_pos_local is None:
        target_pos_local = torch.tensor(spec.place_pos_local, device=scene.env_origins.device).view(1, 3)
        return scene.env_origins + target_pos_local

    target = scene[spec.placement_target_name]
    target_data = getattr(target, "data", None)
    if target_data is None or not hasattr(target_data, "root_pos_w"):
        raise RuntimeError(
            "Placement receptacle must be a managed RigidObject with root_pos_w. "
            f"Got entity {spec.placement_target_name!r} without root_pos_w."
        )

    return as_torch(target_data.root_pos_w)
