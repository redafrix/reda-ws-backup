"""Reset logic for Franka tabletop episodes."""

from __future__ import annotations

import torch
import isaaclab.sim as sim_utils
from isaaclab.assets import Articulation
from isaaclab.scene import InteractiveScene
from isaaclab.utils.math import convert_quat

from franka_wrist_camera_scene.scene.clutter import ClutterObjectSpec
from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
from franka_wrist_camera_scene.utils.tensors import as_torch

PARKED_ASSET_POS = (100.0, 100.0, -10.0)


def reset_robot_to_default(scene: InteractiveScene) -> None:
    """Reset the robot to its default root and joint state."""
    robot: Articulation = scene["robot"]
    root_state = as_torch(robot.data.default_root_state).clone()
    root_state[:, :3] += scene.env_origins

    robot.write_root_pose_to_sim(root_state[:, :7])
    robot.write_root_velocity_to_sim(root_state[:, 7:])
    robot.write_joint_state_to_sim(
        as_torch(robot.data.default_joint_pos).clone(),
        as_torch(robot.data.default_joint_vel).clone(),
    )
    robot.set_joint_position_target(as_torch(robot.data.default_joint_pos).clone())


def _identity_quaternion(device: torch.device) -> torch.Tensor:
    return torch.tensor((1.0, 0.0, 0.0, 0.0), device=device).view(1, 4)


def _quaternion_wxyz_tensor(
    quat_wxyz: tuple[float, float, float, float],
    device: torch.device,
) -> torch.Tensor:
    return torch.tensor(quat_wxyz, device=device).view(1, 4)


def _rigid_quaternion_xyzw_tensor(
    quat_wxyz: tuple[float, float, float, float],
    device: torch.device,
) -> torch.Tensor:
    return convert_quat(_quaternion_wxyz_tensor(quat_wxyz, device), to="xyzw")


def _local_position_tensor(
    scene: InteractiveScene,
    pos_local: tuple[float, float, float],
) -> torch.Tensor:
    return scene.env_origins + torch.tensor(pos_local, device=scene.env_origins.device).view(1, 3)


def _local_translation_tensor(
    scene: InteractiveScene,
    pos_local: tuple[float, float, float],
) -> torch.Tensor:
    return torch.tensor(
        pos_local,
        device=scene.env_origins.device,
        dtype=scene.env_origins.dtype,
    ).view(1, 3).repeat(scene.env_origins.shape[0], 1)


def _require_finite_tensor(name: str, value: torch.Tensor) -> None:
    if not bool(torch.isfinite(value).all().item()):
        raise RuntimeError(f"{name} contains non-finite values: {value.detach().cpu().tolist()}")


def _raise_if_bad_pose_error(
    *,
    message: str,
    error: torch.Tensor,
    tolerance_m: float,
    details: str,
) -> None:
    if not bool(torch.isfinite(error).all().item()) or bool((error > tolerance_m).any().item()):
        raise RuntimeError(
            f"{message} {details}, error_m={error.detach().cpu().tolist()}, "
            f"tolerance_m={tolerance_m}"
        )


def _raise_if_bad_speed(
    *,
    message: str,
    velocity: torch.Tensor,
    speed: torch.Tensor,
    max_speed_m_s: float,
    details: str,
) -> None:
    if (
        not bool(torch.isfinite(velocity).all().item())
        or not bool(torch.isfinite(speed).all().item())
        or bool((speed > max_speed_m_s).any().item())
    ):
        raise RuntimeError(
            f"{message} {details}, root_vel_w={velocity.detach().cpu().tolist()}, "
            f"speed_m_s={speed.detach().cpu().tolist()}, max_speed_m_s={max_speed_m_s}"
        )


def _extra_local_translations(scene: InteractiveScene, entity_name: str) -> torch.Tensor:
    translations, _ = scene[entity_name].get_local_poses()
    return as_torch(translations)[:, :3]


def _extra_world_positions(scene: InteractiveScene, entity_name: str) -> torch.Tensor:
    positions, _ = scene[entity_name].get_world_poses()
    return as_torch(positions)[:, :3]


def _assert_extra_pose(
    scene: InteractiveScene,
    entity_name: str,
    expected_local_translations: torch.Tensor,
    tolerance_m: float = 0.005,
) -> None:
    entity = scene[entity_name]
    expected_local_translations = expected_local_translations.to(
        device=scene.env_origins.device,
        dtype=scene.env_origins.dtype,
    )
    expected_world_positions = scene.env_origins + expected_local_translations

    if callable(getattr(entity, "set_local_poses", None)) and callable(getattr(entity, "get_local_poses", None)):
        actual_local_translations = _extra_local_translations(scene, entity_name)
        _require_finite_tensor(f"{entity_name}.actual_local_translation", actual_local_translations)
        _require_finite_tensor(f"{entity_name}.expected_local_translation", expected_local_translations)
        local_error = torch.linalg.norm(actual_local_translations - expected_local_translations, dim=-1)
        _raise_if_bad_pose_error(
            message="Static extra USD-local pose was not reset.",
            error=local_error,
            tolerance_m=tolerance_m,
            details=(
                f"name={entity_name}, expected_local={expected_local_translations.detach().cpu().tolist()}, "
                f"actual_local={actual_local_translations.detach().cpu().tolist()}"
            ),
        )
        actual_world_positions = _extra_world_positions(scene, entity_name)
    else:
        actual_world_positions = as_torch(entity.data.root_pos_w)[:, :3]

    _require_finite_tensor(f"{entity_name}.actual_world_position", actual_world_positions)
    _require_finite_tensor(f"{entity_name}.expected_world_position", expected_world_positions)
    world_error = torch.linalg.norm(actual_world_positions - expected_world_positions, dim=-1)
    _raise_if_bad_pose_error(
        message="Static extra world pose was not reset.",
        error=world_error,
        tolerance_m=tolerance_m,
        details=(
            f"name={entity_name}, expected_world={expected_world_positions.detach().cpu().tolist()}, "
            f"actual_world={actual_world_positions.detach().cpu().tolist()}"
        ),
    )


def _assert_static_extra_poses(
    scene: InteractiveScene,
    expected_local_translations_by_name: dict[str, torch.Tensor],
) -> None:
    for entity_name, expected_local_translations in expected_local_translations_by_name.items():
        _assert_extra_pose(scene, entity_name, expected_local_translations)


def _single_static_extra_expected_translations(
    scene: InteractiveScene,
    clutter_specs: tuple[ClutterObjectSpec, ...],
    inactive_clutter_names: tuple[str, ...],
) -> dict[str, torch.Tensor]:
    expected = {
        clutter_name: _local_translation_tensor(scene, PARKED_ASSET_POS)
        for clutter_name in inactive_clutter_names
    }
    for clutter_spec in clutter_specs:
        expected[_clutter_entity_name(clutter_spec)] = _local_translation_tensor(scene, clutter_spec.pos_local)
    return expected


def _set_extra_pose(
    scene: InteractiveScene,
    entity_name: str,
    pos_local: tuple[float, float, float],
    quat_wxyz: tuple[float, float, float, float] = (1.0, 0.0, 0.0, 0.0),
) -> None:
    local_translations = _local_translation_tensor(scene, pos_local)
    orientations = _quaternion_wxyz_tensor(quat_wxyz, scene.env_origins.device).repeat(
        scene.env_origins.shape[0],
        1,
    )
    _set_extra_pose_tensors(scene, entity_name, local_translations, orientations)


def _set_extra_pose_tensors(
    scene: InteractiveScene,
    entity_name: str,
    local_translations: torch.Tensor,
    orientations_wxyz: torch.Tensor,
) -> None:
    entity = scene[entity_name]
    if callable(getattr(entity, "write_root_pose_to_sim", None)):
        root_state = as_torch(entity.data.default_root_state).clone()
        root_state[:, :3] = scene.env_origins + local_translations.to(
            device=root_state.device,
            dtype=root_state.dtype,
        )
        root_state[:, 3:7] = convert_quat(
            orientations_wxyz.to(device=root_state.device, dtype=root_state.dtype),
            to="xyzw",
        )
        root_state[:, 7:] = 0.0
        entity.write_root_pose_to_sim(root_state[:, :7])
        entity.write_root_velocity_to_sim(root_state[:, 7:])
        return

    # Static clutter is rendered from USD because collect.py disables RTX reads from Fabric
    # to avoid the disappearing robot issue. Keep both USD-local and Fabric/world state in sync.
    entity.set_local_poses(
        translations=local_translations,
        orientations=orientations_wxyz,
    )
    entity.set_world_poses(
        positions=scene.env_origins + local_translations,
        orientations=orientations_wxyz,
    )


def _park_rigid_object(scene: InteractiveScene, entity_name: str) -> None:
    entity = scene[entity_name]
    root_state = as_torch(entity.data.default_root_state).clone()
    root_state[:, :3] = torch.tensor(PARKED_ASSET_POS, device=root_state.device).view(1, 3)
    root_state[:, 3:7] = _identity_quaternion(root_state.device)
    root_state[:, 7:] = 0.0
    entity.write_root_pose_to_sim(root_state[:, :7])
    entity.write_root_velocity_to_sim(root_state[:, 7:])


def _park_extra_object(scene: InteractiveScene, entity_name: str) -> None:
    _set_extra_pose(scene, entity_name, PARKED_ASSET_POS)


def _clutter_entity_name(clutter_spec: ClutterObjectSpec) -> str:
    if clutter_spec.prim_name.startswith("clutter_"):
        return clutter_spec.prim_name

    prefix = "ClutterObject"
    if not clutter_spec.prim_name.startswith(prefix):
        raise ValueError(f"Unsupported clutter prim name: {clutter_spec.prim_name}")
    return f"clutter_{clutter_spec.prim_name.removeprefix(prefix)}"


def _reset_rigid_object_pose(
    scene: InteractiveScene,
    entity_name: str,
    pos_local: tuple[float, float, float],
    quat_wxyz: tuple[float, float, float, float],
) -> None:
    entity = scene[entity_name]
    root_state = as_torch(entity.data.default_root_state).clone()

    root_state[:, :3] = _local_position_tensor(scene, pos_local)
    root_state[:, 3:7] = _rigid_quaternion_xyzw_tensor(quat_wxyz, root_state.device)
    root_state[:, 7:] = 0.0

    entity.write_root_pose_to_sim(root_state[:, :7])
    entity.write_root_velocity_to_sim(root_state[:, 7:])


def assert_receptacle_reset_pose(
    scene: InteractiveScene,
    spec: PickPlaceTaskSpec,
    tolerance_m: float = 0.02,
) -> None:
    if spec.placement_target_pos_local is None:
        return

    receptacle = scene[spec.placement_target_name]
    actual_pos = as_torch(receptacle.data.root_pos_w)
    expected_pos = _local_position_tensor(scene, spec.placement_target_pos_local)

    _require_finite_tensor("placement_receptacle.actual_pos", actual_pos)
    _require_finite_tensor("placement_receptacle.expected_pos", expected_pos)
    error = torch.linalg.norm(actual_pos - expected_pos, dim=-1)
    _raise_if_bad_pose_error(
        message="Placement receptacle was not reset to the episode pose.",
        error=error,
        tolerance_m=tolerance_m,
        details=(
            f"name={spec.placement_target_name}, "
            f"expected={expected_pos.detach().cpu().tolist()}, "
            f"actual={actual_pos.detach().cpu().tolist()}"
        ),
    )

    velocity = as_torch(receptacle.data.root_vel_w)
    speed = torch.linalg.norm(velocity[:, :3], dim=-1)
    _raise_if_bad_speed(
        message="Placement receptacle velocity was not cleared during reset.",
        velocity=velocity,
        speed=speed,
        max_speed_m_s=1e-4,
        details=f"name={spec.placement_target_name}",
    )


def assert_reaching_target_reset_pose(
    scene: InteractiveScene,
    spec: ReachingTaskSpec,
    tolerance_m: float = 0.01,
    max_speed_m_s: float = 0.01,
) -> None:
    obj = scene[spec.object_name]
    actual_pos = as_torch(obj.data.root_pos_w)[:, :3]
    expected_pos = _local_position_tensor(scene, spec.object_pos_local)

    _require_finite_tensor("reaching_target.actual_pos", actual_pos)
    _require_finite_tensor("reaching_target.expected_pos", expected_pos)
    error = torch.linalg.norm(actual_pos - expected_pos, dim=-1)
    _raise_if_bad_pose_error(
        message="Reaching target was not stable after reset.",
        error=error,
        tolerance_m=tolerance_m,
        details=(
            f"name={spec.object_name}, expected={expected_pos.detach().cpu().tolist()}, "
            f"actual={actual_pos.detach().cpu().tolist()}"
        ),
    )

    velocity = as_torch(obj.data.root_vel_w)
    speed = torch.linalg.norm(velocity[:, :3], dim=-1)
    _raise_if_bad_speed(
        message="Reaching target has nonzero velocity after reset.",
        velocity=velocity,
        speed=speed,
        max_speed_m_s=max_speed_m_s,
        details=f"name={spec.object_name}",
    )


def reset_pick_place_objects(scene: InteractiveScene, spec: PickPlaceTaskSpec) -> None:
    """Reset the pick-place object to the task initial pose and zero velocity."""
    obj = scene[spec.object_name]

    root_state = as_torch(obj.data.default_root_state).clone()

    root_state[:, :3] = _local_position_tensor(scene, spec.object_pos_local)
    root_state[:, 3:7] = _rigid_quaternion_xyzw_tensor(spec.object_quat_wxyz, root_state.device)
    root_state[:, 7:] = 0.0

    obj.write_root_pose_to_sim(root_state[:, :7])
    obj.write_root_velocity_to_sim(root_state[:, 7:])


def reset_pick_place_receptacle(scene: InteractiveScene, spec: PickPlaceTaskSpec) -> None:
    """Reset the active receptacle to the episode pose."""
    if spec.placement_target_pos_local is None:
        return

    _reset_rigid_object_pose(
        scene=scene,
        entity_name=spec.placement_target_name,
        pos_local=spec.placement_target_pos_local,
        quat_wxyz=spec.placement_target_quat_wxyz,
    )


def reset_static_clutter(
    scene: InteractiveScene,
    clutter_specs: tuple[ClutterObjectSpec, ...],
) -> None:
    """Reset static clutter prims to their episode poses."""
    for clutter_spec in clutter_specs:
        _set_extra_pose(
            scene=scene,
            entity_name=_clutter_entity_name(clutter_spec),
            pos_local=clutter_spec.pos_local,
        )


def reset_pick_place_episode(
    sim: sim_utils.SimulationContext,
    scene: InteractiveScene,
    spec: PickPlaceTaskSpec,
    clutter_specs: tuple[ClutterObjectSpec, ...] = (),
    inactive_object_names: tuple[str, ...] = (),
    inactive_receptacle_names: tuple[str, ...] = (),
    inactive_clutter_names: tuple[str, ...] = (),
    reset_scene: bool = True,
) -> None:
    """Reset robot and task objects for one deterministic pick-place episode."""
    if reset_scene:
        scene.reset()

    reset_robot_to_default(scene)

    for object_name in inactive_object_names:
        _park_rigid_object(scene, object_name)

    for receptacle_name in inactive_receptacle_names:
        _park_rigid_object(scene, receptacle_name)

    for clutter_name in inactive_clutter_names:
        _park_extra_object(scene, clutter_name)

    reset_pick_place_objects(scene, spec)
    reset_pick_place_receptacle(scene, spec)
    reset_static_clutter(scene, clutter_specs)

    scene.write_data_to_sim()
    sim.step()

    # One physics step initializes handles; reapply all asset-bank poses before recording.
    for object_name in inactive_object_names:
        _park_rigid_object(scene, object_name)

    for receptacle_name in inactive_receptacle_names:
        _park_rigid_object(scene, receptacle_name)

    for clutter_name in inactive_clutter_names:
        _park_extra_object(scene, clutter_name)

    reset_pick_place_objects(scene, spec)
    reset_pick_place_receptacle(scene, spec)
    reset_static_clutter(scene, clutter_specs)

    scene.write_data_to_sim()
    scene.update(sim.get_physics_dt())

    assert_receptacle_reset_pose(scene, spec)
    _assert_static_extra_poses(
        scene,
        _single_static_extra_expected_translations(scene, clutter_specs, inactive_clutter_names),
    )


def reset_pick_place_vector_episode(
    sim: sim_utils.SimulationContext,
    scene: InteractiveScene,
    specs: tuple[PickPlaceTaskSpec, ...],
    clutter_specs_by_env: tuple[tuple[ClutterObjectSpec, ...], ...],
    all_object_names: tuple[str, ...],
    all_receptacle_names: tuple[str, ...],
    all_clutter_names: tuple[str, ...],
    active_env_count: int,
    reset_scene: bool = True,
) -> None:
    """Reset a vectorized pick-place scene with independent per-env task assets."""
    if len(specs) != scene.num_envs:
        raise ValueError(f"Expected {scene.num_envs} pick-place specs, got {len(specs)}.")
    if len(clutter_specs_by_env) != scene.num_envs:
        raise ValueError(
            f"Expected {scene.num_envs} clutter spec tuples, got {len(clutter_specs_by_env)}."
        )
    if active_env_count <= 0 or active_env_count > scene.num_envs:
        raise ValueError(
            f"active_env_count must be in [1, {scene.num_envs}], got {active_env_count}."
        )

    if reset_scene:
        scene.reset()

    reset_robot_to_default(scene)
    _reset_vector_pick_place_rigid_objects(scene, specs, all_object_names, is_receptacle=False)
    _reset_vector_pick_place_rigid_objects(scene, specs, all_receptacle_names, is_receptacle=True)
    static_clutter_expected = _reset_vector_static_clutter(scene, clutter_specs_by_env, all_clutter_names)

    scene.write_data_to_sim()
    sim.step()

    # Dynamic and static asset-bank handles can drift or remain in their spawn USD pose during init.
    # Snap every bank asset back exactly before recording.
    _reset_vector_pick_place_rigid_objects(scene, specs, all_object_names, is_receptacle=False)
    _reset_vector_pick_place_rigid_objects(scene, specs, all_receptacle_names, is_receptacle=True)
    static_clutter_expected = _reset_vector_static_clutter(scene, clutter_specs_by_env, all_clutter_names)

    scene.write_data_to_sim()
    scene.update(sim.get_physics_dt())
    _assert_vector_pick_place_reset_pose(scene, specs, active_env_count)
    _assert_static_extra_poses(scene, static_clutter_expected)


def _reset_vector_pick_place_rigid_objects(
    scene: InteractiveScene,
    specs: tuple[PickPlaceTaskSpec, ...],
    all_entity_names: tuple[str, ...],
    *,
    is_receptacle: bool,
) -> None:
    if not all_entity_names:
        raise ValueError("Vector pick-place reset requires at least one rigid entity name.")

    states_by_name = {}
    for entity_name in all_entity_names:
        entity = scene[entity_name]
        root_state = as_torch(entity.data.default_root_state).clone()
        root_state[:, :3] = torch.tensor(PARKED_ASSET_POS, device=root_state.device).view(1, 3)
        root_state[:, 3:7] = _identity_quaternion(root_state.device)
        root_state[:, 7:] = 0.0
        states_by_name[entity_name] = root_state

    for env_index, spec in enumerate(specs):
        entity_name = spec.placement_target_name if is_receptacle else spec.object_name
        if entity_name not in states_by_name:
            raise ValueError(f"Pick-place spec references object outside the asset bank: {entity_name!r}")

        if is_receptacle:
            if spec.placement_target_pos_local is None:
                continue
            pos_local = spec.placement_target_pos_local
            quat_wxyz = spec.placement_target_quat_wxyz
        else:
            pos_local = spec.object_pos_local
            quat_wxyz = spec.object_quat_wxyz

        root_state = states_by_name[entity_name]
        root_state[env_index, :3] = scene.env_origins[env_index] + torch.tensor(
            pos_local,
            device=root_state.device,
        )
        root_state[env_index, 3:7] = _rigid_quaternion_xyzw_tensor(quat_wxyz, root_state.device).view(4)
        root_state[env_index, 7:] = 0.0

    for entity_name, root_state in states_by_name.items():
        entity = scene[entity_name]
        entity.write_root_pose_to_sim(root_state[:, :7])
        entity.write_root_velocity_to_sim(root_state[:, 7:])


def _assert_vector_pick_place_reset_pose(
    scene: InteractiveScene,
    specs: tuple[PickPlaceTaskSpec, ...],
    active_env_count: int,
    tolerance_m: float = 0.02,
) -> None:
    for env_index, spec in enumerate(specs[:active_env_count]):
        for entity_name, pos_local in (
            (spec.object_name, spec.object_pos_local),
            (spec.placement_target_name, spec.placement_target_pos_local),
        ):
            if pos_local is None:
                continue
            entity = scene[entity_name]
            actual_pos = as_torch(entity.data.root_pos_w)[env_index, :3]
            expected_pos = scene.env_origins[env_index] + torch.tensor(
                pos_local,
                device=actual_pos.device,
                dtype=actual_pos.dtype,
            )
            _require_finite_tensor("vector_pick_place.actual_pos", actual_pos)
            _require_finite_tensor("vector_pick_place.expected_pos", expected_pos)
            error = torch.linalg.norm(actual_pos - expected_pos)
            _raise_if_bad_pose_error(
                message="Vector pick-place asset was not stable after reset.",
                error=error.view(1),
                tolerance_m=tolerance_m,
                details=(
                    f"env_index={env_index}, name={entity_name}, "
                    f"expected={expected_pos.detach().cpu().tolist()}, "
                    f"actual={actual_pos.detach().cpu().tolist()}"
                ),
            )

            velocity = as_torch(entity.data.root_vel_w)[env_index]
            speed = torch.linalg.norm(velocity[:3])
            _raise_if_bad_speed(
                message="Vector pick-place asset velocity was not cleared during reset.",
                velocity=velocity,
                speed=speed.view(1),
                max_speed_m_s=1e-4,
                details=f"env_index={env_index}, name={entity_name}",
            )


def reset_reaching_objects(scene: InteractiveScene, spec: ReachingTaskSpec) -> None:
    """Reset the reaching object to the task initial pose and zero velocity."""
    obj = scene[spec.object_name]

    root_state = as_torch(obj.data.default_root_state).clone()
    pos_local = torch.tensor(spec.object_pos_local, device=root_state.device).view(1, 3)

    root_state[:, :3] = scene.env_origins + pos_local
    root_state[:, 3:7] = _rigid_quaternion_xyzw_tensor((1.0, 0.0, 0.0, 0.0), root_state.device)
    root_state[:, 7:] = 0.0

    obj.write_root_pose_to_sim(root_state[:, :7])
    obj.write_root_velocity_to_sim(root_state[:, 7:])


def park_inactive_reaching_assets(
    scene: InteractiveScene,
    inactive_object_names: tuple[str, ...],
    inactive_clutter_names: tuple[str, ...],
) -> None:
    for object_name in inactive_object_names:
        _park_rigid_object(scene, object_name)

    for clutter_name in inactive_clutter_names:
        _park_extra_object(scene, clutter_name)


def reset_reaching_episode(
    sim: sim_utils.SimulationContext,
    scene: InteractiveScene,
    spec: ReachingTaskSpec,
    clutter_specs: tuple[ClutterObjectSpec, ...] = (),
    inactive_object_names: tuple[str, ...] = (),
    inactive_clutter_names: tuple[str, ...] = (),
    reset_scene: bool = True,
) -> None:
    """Reset robot and task objects for one deterministic reaching episode."""
    if reset_scene:
        scene.reset()

    reset_robot_to_default(scene)
    park_inactive_reaching_assets(scene, inactive_object_names, inactive_clutter_names)

    reset_reaching_objects(scene, spec)
    reset_static_clutter(scene, clutter_specs)

    scene.write_data_to_sim()
    sim.step()

    # After handles initialize, snap dynamic and static asset-bank poses back exactly.
    park_inactive_reaching_assets(scene, inactive_object_names, inactive_clutter_names)
    reset_reaching_objects(scene, spec)
    reset_static_clutter(scene, clutter_specs)

    scene.write_data_to_sim()
    scene.update(sim.get_physics_dt())
    assert_reaching_target_reset_pose(scene, spec)
    _assert_static_extra_poses(
        scene,
        _single_static_extra_expected_translations(scene, clutter_specs, inactive_clutter_names),
    )


def reset_reaching_vector_episode(
    sim: sim_utils.SimulationContext,
    scene: InteractiveScene,
    specs: tuple[ReachingTaskSpec, ...],
    clutter_specs_by_env: tuple[tuple[ClutterObjectSpec, ...], ...],
    all_object_names: tuple[str, ...],
    all_clutter_names: tuple[str, ...],
    active_env_count: int,
    reset_scene: bool = True,
) -> None:
    """Reset a vectorized reaching scene with independent per-env task assets."""
    if len(specs) != scene.num_envs:
        raise ValueError(f"Expected {scene.num_envs} reaching specs, got {len(specs)}.")
    if len(clutter_specs_by_env) != scene.num_envs:
        raise ValueError(
            f"Expected {scene.num_envs} clutter spec tuples, got {len(clutter_specs_by_env)}."
        )
    if active_env_count <= 0 or active_env_count > scene.num_envs:
        raise ValueError(
            f"active_env_count must be in [1, {scene.num_envs}], got {active_env_count}."
        )

    if reset_scene:
        scene.reset()

    reset_robot_to_default(scene)
    _reset_vector_reaching_objects(scene, specs, all_object_names)
    static_clutter_expected = _reset_vector_static_clutter(scene, clutter_specs_by_env, all_clutter_names)

    scene.write_data_to_sim()
    sim.step()

    # Dynamic and static asset-bank handles can drift or remain in their spawn USD pose during init.
    # Snap every bank asset back exactly before recording.
    _reset_vector_reaching_objects(scene, specs, all_object_names)
    static_clutter_expected = _reset_vector_static_clutter(scene, clutter_specs_by_env, all_clutter_names)

    scene.write_data_to_sim()
    scene.update(sim.get_physics_dt())
    _assert_vector_reaching_reset_pose(scene, specs, active_env_count)
    _assert_static_extra_poses(scene, static_clutter_expected)


def _reset_vector_reaching_objects(
    scene: InteractiveScene,
    specs: tuple[ReachingTaskSpec, ...],
    all_object_names: tuple[str, ...],
) -> None:
    if not all_object_names:
        raise ValueError("Vector reaching reset requires at least one object entity name.")

    states_by_name = {}
    for object_name in all_object_names:
        entity = scene[object_name]
        root_state = as_torch(entity.data.default_root_state).clone()
        root_state[:, :3] = torch.tensor(PARKED_ASSET_POS, device=root_state.device).view(1, 3)
        root_state[:, 3:7] = _identity_quaternion(root_state.device)
        root_state[:, 7:] = 0.0
        states_by_name[object_name] = root_state

    for env_index, spec in enumerate(specs):
        if spec.object_name not in states_by_name:
            raise ValueError(f"Reaching spec references object outside the asset bank: {spec.object_name!r}")
        root_state = states_by_name[spec.object_name]
        root_state[env_index, :3] = scene.env_origins[env_index] + torch.tensor(
            spec.object_pos_local,
            device=root_state.device,
        )
        root_state[env_index, 3:7] = _rigid_quaternion_xyzw_tensor(
            (1.0, 0.0, 0.0, 0.0),
            root_state.device,
        ).view(4)
        root_state[env_index, 7:] = 0.0

    for object_name, root_state in states_by_name.items():
        entity = scene[object_name]
        entity.write_root_pose_to_sim(root_state[:, :7])
        entity.write_root_velocity_to_sim(root_state[:, 7:])


def _reset_vector_static_clutter(
    scene: InteractiveScene,
    clutter_specs_by_env: tuple[tuple[ClutterObjectSpec, ...], ...],
    all_clutter_names: tuple[str, ...],
) -> dict[str, torch.Tensor]:
    local_translations_by_name = {
        clutter_name: torch.tensor(
            PARKED_ASSET_POS,
            device=scene.env_origins.device,
            dtype=scene.env_origins.dtype,
        ).view(1, 3).repeat(scene.num_envs, 1)
        for clutter_name in all_clutter_names
    }

    for env_index, clutter_specs in enumerate(clutter_specs_by_env):
        for clutter_spec in clutter_specs:
            entity_name = _clutter_entity_name(clutter_spec)
            if entity_name not in local_translations_by_name:
                raise ValueError(f"Clutter spec references object outside the asset bank: {entity_name!r}")
            local_translations_by_name[entity_name][env_index] = torch.tensor(
                clutter_spec.pos_local,
                device=scene.env_origins.device,
                dtype=scene.env_origins.dtype,
            )

    orientations = _identity_quaternion(scene.env_origins.device).repeat(scene.num_envs, 1)
    for entity_name, local_translations in local_translations_by_name.items():
        _set_extra_pose_tensors(scene, entity_name, local_translations, orientations)

    return {name: translations.clone() for name, translations in local_translations_by_name.items()}


def _assert_vector_reaching_reset_pose(
    scene: InteractiveScene,
    specs: tuple[ReachingTaskSpec, ...],
    active_env_count: int,
    tolerance_m: float = 0.01,
    max_speed_m_s: float = 0.01,
) -> None:
    for env_index, spec in enumerate(specs[:active_env_count]):
        obj = scene[spec.object_name]
        actual_pos = as_torch(obj.data.root_pos_w)[env_index, :3]
        expected_pos = scene.env_origins[env_index] + torch.tensor(
            spec.object_pos_local,
            device=actual_pos.device,
            dtype=actual_pos.dtype,
        )
        _require_finite_tensor("vector_reaching.actual_pos", actual_pos)
        _require_finite_tensor("vector_reaching.expected_pos", expected_pos)
        error = torch.linalg.norm(actual_pos - expected_pos)
        _raise_if_bad_pose_error(
            message="Vector reaching target was not stable after reset.",
            error=error.view(1),
            tolerance_m=tolerance_m,
            details=(
                f"env_index={env_index}, name={spec.object_name}, "
                f"expected={expected_pos.detach().cpu().tolist()}, "
                f"actual={actual_pos.detach().cpu().tolist()}"
            ),
        )

        velocity = as_torch(obj.data.root_vel_w)[env_index]
        speed = torch.linalg.norm(velocity[:3])
        _raise_if_bad_speed(
            message="Vector reaching target has nonzero velocity after reset.",
            velocity=velocity,
            speed=speed.view(1),
            max_speed_m_s=max_speed_m_s,
            details=f"env_index={env_index}, name={spec.object_name}",
        )
