"""Simulation configuration compatibility helpers."""

from __future__ import annotations

import isaaclab.sim as sim_utils

from franka_wrist_camera_scene.settings import SIM_DT

FABRIC_RENDER_TRANSFORM_SETTING = "/rtx/hydra/readTransformsFromFabricInRenderDelegate"


def make_simulation_cfg(device: str, use_fabric: bool = True) -> sim_utils.SimulationCfg:
    physx_cfg = _make_physx_cfg()
    cfg_kwargs = {
        "dt": SIM_DT,
        "device": device,
        "use_fabric": use_fabric,
    }
    if hasattr(sim_utils, "RenderCfg"):
        cfg_kwargs["render"] = sim_utils.RenderCfg(
            carb_settings={
                FABRIC_RENDER_TRANSFORM_SETTING: False,
            }
        )

    if "physics" in getattr(sim_utils.SimulationCfg, "__dataclass_fields__", {}):
        cfg_kwargs["physics"] = physx_cfg
    else:
        cfg_kwargs["physx"] = physx_cfg

    return sim_utils.SimulationCfg(**cfg_kwargs)


def _make_physx_cfg():
    try:
        from isaaclab_physx.physics import PhysxCfg
    except ModuleNotFoundError:
        PhysxCfg = sim_utils.PhysxCfg

    return PhysxCfg(
        enable_external_forces_every_iteration=True,
        min_velocity_iteration_count=1,
        min_position_iteration_count=4,
        gpu_max_rigid_contact_count=33554432,
        gpu_max_rigid_patch_count=8388608,
        gpu_found_lost_pairs_capacity=8388608,
    )
