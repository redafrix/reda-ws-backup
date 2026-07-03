"""Runtime appearance updates for the tabletop scene."""

from __future__ import annotations

from isaaclab.scene import InteractiveScene
from pxr import Gf, UsdShade


TABLE_SHADER_PATH = "/World/envs/env_0/Table/geometry/material/Shader"


def set_table_color(scene: InteractiveScene, color_rgb: tuple[float, float, float]) -> None:
    shader_prim = scene.stage.GetPrimAtPath(TABLE_SHADER_PATH)
    if not shader_prim.IsValid():
        raise RuntimeError(f"Table shader prim not found: {TABLE_SHADER_PATH}")

    diffuse_input = UsdShade.Shader(shader_prim).GetInput("diffuseColor")
    if not diffuse_input:
        raise RuntimeError(f"Table shader diffuseColor input not found: {TABLE_SHADER_PATH}")
    diffuse_input.Set(Gf.Vec3f(*color_rgb))
