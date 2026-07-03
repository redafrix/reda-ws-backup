#!/usr/bin/env python3
"""Closed-loop Pi0.5 reaching rollout in the IsaacLab tabletop scene."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np
import torch

REPO_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(REPO_SRC))

from franka_wrist_camera_scene.app import launcher  # noqa: F401
from isaaclab.app import AppLauncher  # noqa: E402
from franka_wrist_camera_scene.pi05.geometry import Pi05ControlScales  # noqa: E402
from franka_wrist_camera_scene.pi05.policy import (  # noqa: E402
    Pi05ActionPolicy,
    Pi05DroidActionPolicy,
    Pi05DroidControlScales,
    Pi05DroidJointCommand,
    Pi05LiveObservation,
)
from franka_wrist_camera_scene.pi05.runtime import Pi05RemoteRuntime, Pi05RemoteRuntimeConfig  # noqa: E402
from franka_wrist_camera_scene.utils.paths import load_yaml_config  # noqa: E402

FABRIC_RENDER_TRANSFORM_SETTING = "/rtx/hydra/readTransformsFromFabricInRenderDelegate"


def _append_kit_arg(existing: str, *tokens: str) -> str:
    parts = existing.split() if existing else []
    parts.extend(tokens)
    return " ".join(parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run closed-loop Pi0.5 reaching rollouts.")
    parser.add_argument("--rollout_config", type=Path, default=Path("configs/eval_pi05_reaching_bob_5ep.yaml"))
    parser.add_argument("--allow_fabric_render_transforms", action="store_true")
    AppLauncher.add_app_launcher_args(parser)
    args = parser.parse_args()
    args.enable_cameras = True
    if not args.allow_fabric_render_transforms:
        args.kit_args = _append_kit_arg(args.kit_args, f"--{FABRIC_RENDER_TRANSFORM_SETTING}=false")
    return args


def import_isaac_runtime_modules() -> None:
    """Import Isaac/PXR-touching modules after SimulationApp exists."""
    global sim_utils, Articulation, InteractiveScene, quat_apply
    global make_simulation_cfg, collection_configs_from_config
    global _apply_camera_resolution, _build_asset_bank, _configured_camera_resolution
    global _configured_state_record_stride, _current_arm_posture_bias, _episode_asset_names
    global _inactive_reaching_asset_names, _make_episode_plan, _make_reaching_recorder
    global _sample_all_scene_assets, validate_reaching_plan
    global GripperController, CartesianIKController, reset_reaching_episode, reaching_success_metrics
    global suite_metadata_from_config, PolicyCommand, set_dome_light, make_reaching_asset_bank_scene_cfg
    global ReachingTaskSpec, ReachingSamplingOptions, WorkspaceConstraint
    global parse_lighting_options, parse_xy_range, as_torch

    import isaaclab.sim as sim_utils
    from isaaclab.assets import Articulation
    from isaaclab.scene import InteractiveScene
    from isaaclab.utils.math import quat_apply

    from franka_wrist_camera_scene.app.simulation_config import make_simulation_cfg
    from franka_wrist_camera_scene.collection.configs import collection_configs_from_config
    from franka_wrist_camera_scene.collection.reaching import (
        _apply_camera_resolution,
        _build_asset_bank,
        _configured_camera_resolution,
        _configured_state_record_stride,
        _current_arm_posture_bias,
        _episode_asset_names,
        _inactive_reaching_asset_names,
        _make_episode_plan,
        _make_reaching_recorder,
        _sample_all_scene_assets,
        validate_reaching_plan,
    )
    from franka_wrist_camera_scene.control.gripper import GripperController
    from franka_wrist_camera_scene.control.ik import CartesianIKController
    from franka_wrist_camera_scene.episode.reset import reset_reaching_episode
    from franka_wrist_camera_scene.episode.success import reaching_success_metrics
    from franka_wrist_camera_scene.episode.suite import suite_metadata_from_config
    from franka_wrist_camera_scene.policies.scripted_base import PolicyCommand
    from franka_wrist_camera_scene.scene.lighting import set_dome_light
    from franka_wrist_camera_scene.scene.tabletop import make_reaching_asset_bank_scene_cfg
    from franka_wrist_camera_scene.tasks.reaching import ReachingTaskSpec
    from franka_wrist_camera_scene.tasks.sampling import (
        ReachingSamplingOptions,
        WorkspaceConstraint,
        parse_lighting_options,
        parse_xy_range,
    )
    from franka_wrist_camera_scene.utils.tensors import as_torch


def runtime_config(eval_cfg: dict) -> Pi05RemoteRuntimeConfig:
    cfg = eval_cfg["pi05"]
    return Pi05RemoteRuntimeConfig(
        host=str(cfg.get("host", "127.0.0.1")),
        port=int(cfg.get("port", 8005)),
        action_horizon=int(cfg.get("action_horizon", 10)),
        action_dim=int(cfg.get("action_dim", 7)),
        observation_schema=str(cfg.get("observation_schema", "libero")),
    )


def control_scales(eval_cfg: dict) -> Pi05ControlScales:
    cfg = eval_cfg["pi05"]
    return Pi05ControlScales(
        translation_scale_m=float(cfg.get("translation_scale_m", 0.05)),
        rotation_scale_rad=float(cfg.get("rotation_scale_rad", 0.5)),
        open_finger_m=float(cfg.get("open_finger_m", 0.04)),
        closed_finger_m=float(cfg.get("closed_finger_m", 0.0)),
    )


def droid_control_scales(eval_cfg: dict) -> Pi05DroidControlScales:
    cfg = eval_cfg["pi05"]
    return Pi05DroidControlScales(
        joint_velocity_scale_rad_s=float(cfg.get("joint_velocity_scale_rad_s", 1.0)),
        droid_control_fps=float(cfg.get("droid_control_fps", 15.0)),
        open_finger_m=float(cfg.get("open_finger_m", 0.04)),
        closed_finger_m=float(cfg.get("closed_finger_m", 0.0)),
        gripper_open_threshold=float(cfg.get("gripper_open_threshold", 0.5)),
    )


def rollout_collection_config(rollout_cfg: dict) -> dict:
    collection_cfg = collection_configs_from_config(load_yaml_config(rollout_cfg["collection_config"]))[0]
    for key in (
        "output_dir",
        "start_episode_id",
        "num_episodes",
        "num_envs",
        "max_steps",
            "settle_time_s",
        "record_cameras",
        "record_depth",
        "camera_width",
        "camera_height",
        "camera_fps",
        "state_record_fps",
    ):
        if key in rollout_cfg:
            collection_cfg[key] = rollout_cfg[key]
    if int(collection_cfg.get("num_envs", 1)) != 1:
        raise ValueError("Pi0.5 rollout currently requires num_envs=1.")
    return collection_cfg


def make_sampling_options(collection_cfg: dict) -> tuple[ReachingTaskSpec, ReachingSamplingOptions]:
    pose_randomization = collection_cfg["pose_randomization"]
    object_xy_range = parse_xy_range(pose_randomization["object_xy_range"])
    lighting_options = parse_lighting_options(collection_cfg["lighting_randomization"])
    base_spec_kwargs = {}
    if "success_threshold_m" in collection_cfg:
        base_spec_kwargs["success_threshold_m"] = float(collection_cfg["success_threshold_m"])
    if "max_success_target_displacement_m" in collection_cfg:
        base_spec_kwargs["max_success_target_displacement_m"] = float(collection_cfg["max_success_target_displacement_m"])
    base_spec = ReachingTaskSpec(**base_spec_kwargs)
    return base_spec, ReachingSamplingOptions(
        object_xy_range=object_xy_range,
        object_origin_xy=base_spec.object_pos_local[:2],
        workspace=WorkspaceConstraint(
            robot_base_xy=tuple(float(value) for value in pose_randomization["workspace"]["robot_base_xy"]),
            max_distance_m=float(pose_randomization["workspace"]["max_distance_m"]),
            max_sampling_attempts=int(pose_randomization["workspace"]["max_sampling_attempts"]),
        ),
        lighting=lighting_options,
    )


def camera_rgb(scene: InteractiveScene, camera_name: str) -> np.ndarray:
    rgb = scene[camera_name].data.output["rgb"][0].detach().cpu().numpy()[..., :3]
    return np.clip(rgb, 0, 255).astype(np.uint8).copy()


def make_live_observation(
    scene: InteractiveScene,
    robot: Articulation,
    ee_body_id: int,
    instruction: str,
    commanded_opening_m: float,
) -> Pi05LiveObservation:
    ee_pose = as_torch(robot.data.body_pose_w)[0, ee_body_id]
    joint_pos = as_torch(robot.data.joint_pos)[0, :7].detach().cpu().numpy().astype(np.float32)
    gripper_position = np.array([np.clip(commanded_opening_m / 0.04, 0.0, 1.0)], dtype=np.float32)
    return Pi05LiveObservation(
        language_instruction=instruction,
        agent_rgb=camera_rgb(scene, "agent_camera"),
        wrist_rgb=camera_rgb(scene, "wrist_camera"),
        ee_pos_w=ee_pose[:3].detach().cpu().numpy(),
        ee_quat_wxyz=ee_pose[3:7].detach().cpu().numpy(),
        env_origin_w=scene.env_origins[0].detach().cpu().numpy(),
        commanded_finger_opening_m=commanded_opening_m,
        joint_position=joint_pos,
        gripper_position=gripper_position,
    )


def target_reach_pos_w(scene: InteractiveScene, spec: ReachingTaskSpec) -> torch.Tensor:
    obj = scene[spec.object_name]
    obj_pos_w = as_torch(obj.data.root_pos_w)[:, :3]
    reach_offset = torch.tensor(spec.object_reach_offset_local, device=obj_pos_w.device).view(1, 3)
    return obj_pos_w + reach_offset


def run_pi05_reaching_episode(
    *,
    sim: sim_utils.SimulationContext,
    scene: InteractiveScene,
    robot: Articulation,
    ik: CartesianIKController,
    gripper: GripperController,
    pi05_policy: Pi05ActionPolicy | Pi05DroidActionPolicy,
    arm_joint_ids: list[int],
    collection_cfg: dict,
    episode_id: int,
    episode_plan,
    scene_assets,
    asset_bank,
    output_dir: Path,
    simulation_app,
    suite,
    seed: int,
) -> Path:
    asset_names = _episode_asset_names(asset_bank, scene_assets)
    inactive_object_names, inactive_clutter_names = _inactive_reaching_asset_names(asset_bank, asset_names)
    reset_reaching_episode(
        sim=sim,
        scene=scene,
        spec=episode_plan.spec,
        clutter_specs=episode_plan.clutter_specs,
        inactive_object_names=inactive_object_names,
        inactive_clutter_names=inactive_clutter_names,
        reset_scene=False,
    )
    set_dome_light(scene, episode_plan.sample.light_intensity, episode_plan.sample.light_color)
    ik.reset()
    ik.set_posture_bias(_current_arm_posture_bias(robot, gain=episode_plan.spec.posture_bias_gain))
    pi05_policy.reset()

    sim_dt = sim.get_physics_dt()
    camera_interval_steps = max(1, round(1.0 / (int(collection_cfg["camera_fps"]) * sim_dt)))
    state_record_stride = _configured_state_record_stride(collection_cfg, sim_dt)
    recorder = _make_reaching_recorder(
        output_dir=output_dir,
        episode_id=episode_id,
        plan=episode_plan,
        scene_assets=scene_assets,
        sim_dt=sim_dt,
        ee_body_id=ik.end_effector_body_id,
        max_steps=int(collection_cfg["max_steps"]),
        record_cameras=bool(collection_cfg["record_cameras"]),
        record_depth=bool(collection_cfg["record_depth"]),
        camera_width=int(collection_cfg["camera_width"]),
        camera_height=int(collection_cfg["camera_height"]),
        camera_fps=int(collection_cfg["camera_fps"]),
        state_record_stride=state_record_stride,
        suite=suite,
        seed=seed,
        env_index=None,
    )
    recorder.validate_output_path()

    latched_reach_pos_w = target_reach_pos_w(scene, episode_plan.spec).detach().clone()
    sim_time_s = 0.0
    step = 0
    camera_tick = 0
    settle_steps = 0
    max_settle_steps = int(float(collection_cfg["settle_time_s"]) / sim_dt)
    current_cmd: PolicyCommand | None = None
    commanded_opening_m = 0.04
    completed = False

    while simulation_app.is_running() and step < int(collection_cfg["max_steps"]):
        if step % camera_interval_steps == 0:
            scene["agent_camera"].update(sim_dt, force_recompute=True)
            scene["wrist_camera"].update(sim_dt, force_recompute=True)
            obs = make_live_observation(
                scene=scene,
                robot=robot,
                ee_body_id=ik.end_effector_body_id,
                instruction=episode_plan.spec.instruction,
                commanded_opening_m=commanded_opening_m,
            )
            current_cmd = pi05_policy.step(obs, camera_tick=camera_tick)
            if isinstance(current_cmd, Pi05DroidJointCommand):
                commanded_opening_m = float(current_cmd.recorder_command.finger_opening_m)
            else:
                commanded_opening_m = float(current_cmd.finger_opening_m)
            camera_tick += 1

        if current_cmd is None:
            raise RuntimeError("Pi0.5 policy did not produce a pose command.")
        if not isinstance(current_cmd, Pi05DroidJointCommand) and current_cmd.target_quat_w is None:
            raise RuntimeError("Pi0.5 policy did not produce a pose command.")

        if isinstance(current_cmd, Pi05DroidJointCommand):
            robot.set_joint_position_target(current_cmd.target_joint_pos, joint_ids=arm_joint_ids)
            record_cmd = current_cmd.recorder_command
        else:
            ik.set_target_pose(current_cmd.target_pos_w, current_cmd.target_quat_w)
            ik.apply(scene, robot)
            record_cmd = current_cmd
        gripper.set_width(record_cmd.finger_opening_m)
        gripper.apply(robot)
        scene.write_data_to_sim()
        recorder.record_step(scene, record_cmd, step, sim_time_s)
        if bool(collection_cfg["record_cameras"]) and step % camera_interval_steps == 0:
            recorder.record_cameras_step(scene, step, sim_time_s, refresh=False)

        sim.step()
        sim_time_s += sim_dt
        step += 1
        scene.update(sim_dt)

        metrics = reaching_success_metrics(
            scene=scene,
            spec=episode_plan.spec,
            target_reach_pos_w=latched_reach_pos_w,
        )
        if bool(metrics.success[0].item()):
            settle_steps += 1
            if settle_steps >= max_settle_steps:
                completed = True
                break
        else:
            settle_steps = 0

    metrics = reaching_success_metrics(
        scene=scene,
        spec=episode_plan.spec,
        target_reach_pos_w=latched_reach_pos_w,
    )
    success = bool(metrics.success[0].item())
    success_mode = "failure"
    if bool(metrics.reached_latched_target[0].item()):
        success_mode = "latched_target"
    elif bool((metrics.reached_live_target & metrics.target_displacement_ok)[0].item()):
        success_mode = "live_target_with_small_displacement"

    saved_dir = recorder.save(success, success_mode=success_mode)
    print(
        f"[INFO] Pi0.5 episode {episode_id} success={success} mode={success_mode} "
        f"completed={completed} steps={step} instruction={episode_plan.spec.instruction!r}",
        flush=True,
    )
    if not success:
        write_failure_json(saved_dir, episode_id, episode_plan, scene, robot, ik.end_effector_body_id, metrics, latched_reach_pos_w, scene_assets)
    return saved_dir


def write_failure_json(
    saved_dir: Path,
    episode_id: int,
    episode_plan,
    scene: InteractiveScene,
    robot: Articulation,
    ee_body_id: int,
    metrics,
    latched_reach_pos_w: torch.Tensor,
    scene_assets,
) -> None:
    ee_pose_w = as_torch(robot.data.body_pose_w)[:, ee_body_id]
    tcp_offset_local = torch.tensor(episode_plan.spec.tcp_offset_local, device=ee_pose_w.device).view(1, 3)
    tcp_pos_w = ee_pose_w[:, :3] + quat_apply(ee_pose_w[:, 3:7], tcp_offset_local.expand(ee_pose_w.shape[0], -1))
    obj_pos_w = as_torch(scene[episode_plan.spec.object_name].data.root_pos_w)
    reach_offset = torch.tensor(episode_plan.spec.object_reach_offset_local, device=obj_pos_w.device).view(1, 3)
    failure = {
        "episode_id": episode_id,
        "task_name": "reaching",
        "policy": "pi05_libero",
        "instruction": episode_plan.spec.instruction,
        "object_category_id": scene_assets.object_context.category_id,
        "object_variant_id": scene_assets.object_context.variant_id,
        "object_label": scene_assets.object_context.label,
        "object_final_pos_w": obj_pos_w[0].detach().cpu().tolist(),
        "tcp_final_pos_w": tcp_pos_w[0].detach().cpu().tolist(),
        "latched_target_reach_pos_w": latched_reach_pos_w[0].detach().cpu().tolist(),
        "live_target_reach_pos_w": (obj_pos_w[:, :3] + reach_offset)[0].detach().cpu().tolist(),
        "target_displacement_m": float(metrics.target_displacement_m[0].item()),
        "final_tcp_distance_to_latched_target_m": float(metrics.latched_distance_m[0].item()),
        "final_tcp_distance_to_live_target_m": float(metrics.live_distance_m[0].item()),
        "success_threshold_m": episode_plan.spec.success_threshold_m,
        "max_success_target_displacement_m": episode_plan.spec.max_success_target_displacement_m,
    }
    (saved_dir / "failure.json").write_text(json.dumps(failure, indent=2), encoding="utf-8")


def run_rollouts(args: argparse.Namespace, simulation_app) -> None:
    rollout_cfg = load_yaml_config(args.rollout_config)
    collection_cfg = rollout_collection_config(rollout_cfg)
    pi05_eval_cfg = load_yaml_config(rollout_cfg["pi05"]["eval_config"])
    seed = int(collection_cfg["seed"])
    output_dir = Path(collection_cfg["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    _, sampling_options = make_sampling_options(collection_cfg)
    start_episode_id = int(collection_cfg["start_episode_id"])
    num_episodes = int(collection_cfg["num_episodes"])
    episode_ids = list(range(start_episode_id, start_episode_id + num_episodes))
    scene_assets_by_episode = _sample_all_scene_assets(collection_cfg, seed, episode_ids)
    asset_bank = _build_asset_bank(scene_assets_by_episode)
    first_id = episode_ids[0]
    first_assets = scene_assets_by_episode[first_id]
    first_names = _episode_asset_names(asset_bank, first_assets)
    first_plan = _make_episode_plan(collection_cfg, first_assets, seed, first_id, sampling_options, first_names)
    validate_reaching_plan(collection_cfg, first_assets, first_plan)

    scene_cfg = make_reaching_asset_bank_scene_cfg(
        target_usd_paths=asset_bank.target_usd_paths,
        clutter_usd_paths=asset_bank.clutter_usd_paths,
        initial_target_name=first_names.object_name,
        initial_clutter_names=first_names.clutter_names,
        initial_clutter_specs=first_plan.clutter_specs,
        num_envs=1,
        env_spacing=float(collection_cfg.get("env_spacing", 5.0)),
    )
    camera_width, camera_height = _configured_camera_resolution(collection_cfg)
    _apply_camera_resolution(
        scene_cfg,
        camera_width,
        camera_height,
        record_depth=bool(collection_cfg["record_depth"]),
        camera_fps=int(collection_cfg["camera_fps"]),
    )

    runtime = Pi05RemoteRuntime(runtime_config(pi05_eval_cfg))
    print("[INFO] Connecting Pi0.5 remote runtime for closed-loop rollout...", flush=True)
    runtime.load()
    if runtime.config.observation_schema == "droid":
        pi05_policy = Pi05DroidActionPolicy(
            runtime=runtime,
            replan_steps=int(pi05_eval_cfg["pi05"].get("replan_steps", 8)),
            command_device=args.device,
            control_scales=droid_control_scales(pi05_eval_cfg),
        )
    else:
        pi05_policy = Pi05ActionPolicy(
            runtime=runtime,
            replan_steps=int(pi05_eval_cfg["pi05"].get("replan_steps", 10)),
            command_device=args.device,
            control_scales=control_scales(pi05_eval_cfg),
        )

    sim = sim_utils.SimulationContext(make_simulation_cfg(args.device, use_fabric=bool(collection_cfg.get("use_fabric", True))))
    scene = InteractiveScene(scene_cfg)
    ik = CartesianIKController(pose_error_weights=(1.0, 1.0, 1.0, 8.0, 8.0, 8.0))
    gripper = GripperController()
    sim.reset()
    sim.set_camera_view(eye=[2.2, -2.2, 1.9], target=[0.55, 0.0, 1.20])
    robot = scene["robot"]
    ik.bind(scene, robot)
    gripper.bind(scene, robot)
    arm_joint_ids, _ = robot.find_joints("panda_joint.*")
    suite = suite_metadata_from_config(collection_cfg)

    plans = {first_id: first_plan}
    for episode_id in episode_ids:
        assets = scene_assets_by_episode[episode_id]
        names = _episode_asset_names(asset_bank, assets)
        plan = plans.get(episode_id)
        if plan is None:
            plan = _make_episode_plan(collection_cfg, assets, seed, episode_id, sampling_options, names)
            validate_reaching_plan(collection_cfg, assets, plan)
        print(
            f"[INFO] Starting Pi0.5 reaching episode {episode_id}: "
            f"instruction={plan.spec.instruction!r}, target_label={assets.object_context.label!r}",
            flush=True,
        )
        run_pi05_reaching_episode(
            sim=sim,
            scene=scene,
            robot=robot,
            ik=ik,
            gripper=gripper,
            pi05_policy=pi05_policy,
            arm_joint_ids=arm_joint_ids,
            collection_cfg=collection_cfg,
            episode_id=episode_id,
            episode_plan=plan,
            scene_assets=assets,
            asset_bank=asset_bank,
            output_dir=output_dir,
            simulation_app=simulation_app,
            suite=suite,
            seed=seed,
        )


def main() -> None:
    args = parse_args()
    app_launcher = AppLauncher(args)
    simulation_app = app_launcher.app
    launcher.patch_physx_schema()
    import_isaac_runtime_modules()
    try:
        run_rollouts(args, simulation_app)
    finally:
        simulation_app.close()


if __name__ == "__main__":
    main()
