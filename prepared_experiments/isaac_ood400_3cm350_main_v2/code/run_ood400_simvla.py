#!/usr/bin/env python3
"""Unified OOD400 SimVLA Baseline & TopK Active Controller Runner for IsaacLab.

Features:
- Strict 3cm / 350 control tick (1400 simulation steps @ 120Hz/30Hz/decimation 4)
- Immediate success termination on first substep with distance <= 0.030m (NO DWELL, settle_time_s=0.0)
- Policy sampling seed: 20260812
- Candidate 0 executed in baseline mode with shadow scoring
- Argmin-on-alarm candidate replacement in online active mode
- Low-storage agent camera RGB video recording (320x240 @ 5 FPS, H264 CRF 30)
- Full summary logging with exact <=3cm crossing fields
- Decision row logging with 16x21 history, 10x7 action, 51 static features
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback
from typing import Any

import numpy as np

WORKSPACE = Path(os.environ.get("SIMVLA_ISAAC_H10_WORKSPACE", "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813"))
PINNED_ISAAC = Path(
    "/mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab"
)
PINNED_ISAAC_SCRIPT = PINNED_ISAAC / "scripts/simvla_reaching_rollout.py"
ISAAC_6_LEGACY_FRANKA_USD = (
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/6.0/"
    "Isaac/IsaacLab/Robots/FrankaEmika/Legacy/panda_instanceable.usd"
)
sys.path.insert(0, str(WORKSPACE / "src"))
sys.path.insert(0, str(PINNED_ISAAC / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ood400_runtime import (  # noqa: E402
    OnlineRiskDecisionPlan,
    OOD400EpisodeStore,
    OnlineRiskPlanner,
    OnlineRiskSelector,
    sha256_file,
)
from risk_collection.rounds import (  # noqa: E402
    ROUND_SCHEDULE_VERSION,
    balanced_round_robin_order,
    global_episode_id,
    scene_family_id,
    schedule_sha256,
)
# from risk_collection.storage import EpisodeStore
from risk_collection.constants import (  # noqa: E402
    ACE_7D_KEYS,
    TOPK8_INDICES,
    UNCERTAINTY_49D_KEYS,
)


def process_matches(needle: str) -> list[tuple[int, str]]:
    matches = []
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        try:
            command = (entry / "cmdline").read_bytes().replace(bytes([0]), b" ").decode()
        except (OSError, UnicodeDecodeError):
            continue
        if needle in command and int(entry.name) != os.getpid():
            matches.append((int(entry.name), command.strip()))
    return matches


def require_gpu_safe() -> None:
    trainers = process_matches("scripts/train_grad_accum.py")
    if trainers:
        raise RuntimeError(f"trainer is active; refusing CUDA/Isaac launch: {trainers}")


def load_pinned_rollout() -> Any:
    spec = importlib.util.spec_from_file_location("pinned_simvla_rollout", PINNED_ISAAC_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load pinned rollout: {PINNED_ISAAC_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(spec.name, None)
        raise
    module.import_isaac_runtime_modules()
    return module


def load_manifest_scene_assets(
    base: Any,
    collection_cfg: dict[str, Any],
    episodes: list[Any],
) -> dict[int, Any]:
    from franka_wrist_camera_scene.collection.reaching import ReachingSceneAssets
    from franka_wrist_camera_scene.scene.object_context import (
        load_catalog_object_context,
    )

    target_sources = {
        str(source["name"]): source for source in collection_cfg["target_sources"]
    }
    clutter_cfg = collection_cfg["clutter"]
    clutter_sources = {
        str(source["name"]): {**clutter_cfg, **source}
        for source in clutter_cfg["sources"]
    }

    def resolve_context(item: dict[str, Any], source_cfg: dict[str, Any]) -> Any:
        context = load_catalog_object_context(
            catalog_config=str(source_cfg["catalog_config"]),
            geometry_config=str(source_cfg["geometry_config"]),
            category_id=str(item["category_id"]),
            variant_id=str(item["variant_id"]),
            split=str(source_cfg["split"]),
            role=str(source_cfg["role"]),
            required_affordances=tuple(source_cfg["required_affordances"]),
            required_grasp_strategy=str(source_cfg["required_grasp_strategy"]),
        )
        expected_key = (str(item["category_id"]), str(item["variant_id"]))
        actual_key = (context.category_id, context.variant_id)
        if actual_key != expected_key:
            raise RuntimeError(
                f"manifest asset resolution mismatch: expected={expected_key}, actual={actual_key}"
            )
        expected_label = str(item["label"])
        if context.label != expected_label:
            context = replace(context, label=expected_label)
        return context

    resolved: dict[int, Any] = {}
    for episode in episodes:
        scene = episode.scene
        source_id = int(episode.source_episode_id)
        target = scene["target"]
        target_source_name = str(target["source_name"])
        if target_source_name not in target_sources:
            raise KeyError(
                f"unknown target source {target_source_name!r} in episode {source_id}"
            )
        object_context = resolve_context(
            target, target_sources[target_source_name]
        )

        clutter_contexts = []
        for expected_slot, item in enumerate(scene["clutter"]):
            if int(item["slot_index"]) != expected_slot:
                raise ValueError(
                    f"episode {source_id} has non-contiguous clutter slots: "
                    f"expected={expected_slot}, actual={item['slot_index']}"
                )
            source_name = str(item["source_name"])
            if source_name not in clutter_sources:
                raise KeyError(
                    f"unknown clutter source {source_name!r} in episode {source_id}"
                )
            clutter_contexts.append(
                (
                    source_name,
                    resolve_context(item, clutter_sources[source_name]),
                )
            )
        resolved[source_id] = ReachingSceneAssets(
            object_context=object_context,
            clutter_contexts=tuple(clutter_contexts),
            target_source_name=target_source_name,
        )
    return resolved


def make_agent_video_writer(path: Path, width: int = 320, height: int = 240):
    path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-f",
        "rawvideo",
        "-pixel_format",
        "rgb24",
        "-video_size",
        f"{width}x{height}",
        "-framerate",
        "5",
        "-i",
        "-",
        "-an",
        "-c:v",
        "libx264",
        "-crf",
        "30",
        "-preset",
        "veryfast",
        "-pix_fmt",
        "yuv420p",
        str(path),
    ]
    return subprocess.Popen(command, stdin=subprocess.PIPE)


def write_agent_video_frame(writer: Any, agent: np.ndarray) -> None:
    from PIL import Image

    resized = np.asarray(
        Image.fromarray(agent).resize((320, 240), Image.Resampling.BILINEAR)
    )
    if resized.shape != (240, 320, 3):
        raise RuntimeError(f"unexpected video frame shape: {resized.shape}")
    assert writer.stdin is not None
    writer.stdin.write(np.ascontiguousarray(resized).tobytes())


def close_video_writer(writer: Any) -> None:
    if writer is None:
        return
    assert writer.stdin is not None
    try:
        writer.stdin.close()
        return_code = writer.wait(timeout=30)
        if return_code != 0:
            print(f"Warning: ffmpeg exited with {return_code}", file=sys.stderr)
    except Exception as e:
        print(f"Warning closing video writer: {e}", file=sys.stderr)


def decision_to_row(
    *,
    episode_id: str,
    execution_mode: str,
    plan: OnlineRiskDecisionPlan,
    sequence: np.ndarray,
    outcome: str,
    label: int | None,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schema_version": "simvla_isaac_risk_collection_v1",
        "episode_id": episode_id,
        "decision_index": plan.decision_index,
        "execution_mode": execution_mode,
        "main_seed": int(plan.main_seed),
        "ace_candidate_seeds": [int(value) for value in plan.ace_seeds],
        "main_candidate_action_chunk_normalized": plan.main_chunk_normalized.tolist(),
        "main_candidate_action_chunk_env": plan.main_chunk_env.tolist(),
        "ace_candidate_chunks_normalized": plan.ace_chunks_normalized.tolist(),
        "ace_candidate_chunks_env": plan.ace_chunks_env.tolist(),
        "ace_features_7d": plan.ace.tolist(),
        "executed_action": sequence[0].tolist(),
        "executed_action_sequence": sequence.tolist(),
        "simvla_uncertainty_49d": plan.uncertainty_49d.tolist(),
        "simvla_uncertainty_delta_49d": plan.uncertainty_delta_49d.tolist(),
        "simvla_uncertainty_raw": plan.uncertainty_raw,
        "history": plan.history.tolist(),
        "current": {"proprio": plan.proprio.tolist()},
        "online_risk": {
            "candidate_scores": plan.candidate_scores.tolist(),
            "candidate_uncertainty_49d": plan.candidate_uncertainty_49d.tolist(),
            "selected_candidate_index": int(plan.selection.selected_index),
            "selection_reason": plan.selection.reason,
            "main_score": float(plan.selection.main_score),
            "selected_score": float(plan.selection.selected_score),
            "best_alternative_index": int(plan.selection.best_alternative_index),
            "best_alternative_score": float(plan.selection.best_alternative_score),
            "proposed_modification": bool(plan.selection.proposed_modification),
            "selected_candidate_action_chunk_normalized": plan.selected_chunk_normalized.tolist(),
            "selected_candidate_action_chunk_env": plan.selected_chunk_env.tolist(),
        },
        "parent_episode_outcome": outcome,
        "parent_episode_risk_label": label,
        "metadata": {
            **metadata,
            "vlm_encoding_count": plan.vlm_encoding_count,
        },
    }


def parse_args() -> argparse.Namespace:
    require_gpu_safe()
    from isaaclab.app import AppLauncher

    parser = argparse.ArgumentParser()
    parser.add_argument("--run-config", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--mode", choices=("baseline", "online"), default="baseline")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--count", type=int)
    parser.add_argument(
        "--execution-mode",
        choices=("chunk_h10",),
        default="chunk_h10",
        help="H10 production invariant: execute all ten predicted actions before replanning",
    )
    parser.add_argument("--risk-model-path", type=Path, required=True)
    parser.add_argument("--risk-normalization", type=Path, required=True)
    parser.add_argument("--main-threshold", type=float, default=0.579133152961731)
    parser.add_argument("--selected-cap", type=float, default=0.90)
    parser.add_argument("--main-threshold-name", type=str, default="Best F1")
    parser.add_argument("--selected-cap-name", type=str, default="engineering_cap_0.90")
    parser.add_argument("--save-video", action="store_true", default=True)

    AppLauncher.add_app_launcher_args(parser)
    args = parser.parse_args()
    args.enable_cameras = True
    fabric_setting = "/rtx/hydra/readTransformsFromFabricInRenderDelegate"
    args.kit_args = " ".join(
        part
        for part in (
            str(getattr(args, "kit_args", "") or ""),
            f"--{fabric_setting}=false",
        )
        if part
    )
    return args


def run_episode(
    *,
    base: Any,
    sim: Any,
    scene: Any,
    robot: Any,
    ready_ik: Any,
    ik: Any,
    gripper: Any,
    runtime: Any,
    collection_cfg: dict[str, Any],
    episode: Any,
    episode_plan: Any,
    scene_assets: Any,
    asset_bank: Any,
    simulation_app: Any,
    state_mean: np.ndarray,
    state_std: np.ndarray,
    execution_mode: str,
    run_store: OOD400EpisodeStore,
    manifest_fingerprint: str,
    global_id: str,
    raw_manifest_entry: dict[str, Any],
    selector: OnlineRiskSelector,
    mode: str,
    save_video: bool,
) -> tuple[bool, int]:
    import torch
    from franka_wrist_camera_scene.policies.scripted_base import PolicyCommand
    from franka_wrist_camera_scene.simvla.geometry import SimVLAProprioSource
    from franka_wrist_camera_scene.simvla.reaching_pose_v1 import (
        PersistentPoseCommandIntegrator,
    )

    source_episode_id = int(episode.source_episode_id)
    episode_id = global_id
    asset_names = base._episode_asset_names(asset_bank, scene_assets)
    inactive_objects, inactive_clutter = base._inactive_reaching_asset_names(
        asset_bank, asset_names
    )
    base.reset_reaching_episode(
        sim=sim,
        scene=scene,
        spec=episode_plan.spec,
        clutter_specs=episode_plan.clutter_specs,
        inactive_object_names=inactive_objects,
        inactive_clutter_names=inactive_clutter,
        reset_scene=False,
    )
    base.set_dome_light(
        scene, episode_plan.sample.light_intensity, episode_plan.sample.light_color
    )
    pose_contract = base.parse_reaching_pose_contract(collection_cfg["pose_controller"])
    canonical_quat_world_xyzw = base.canonical_quaternion_world_xyzw(
        base.as_torch(robot.data.root_pose_w)[:, 3:7], pose_contract
    )
    ready_ik.reset()
    posture = base.configured_posture_bias(pose_contract)
    ready_ik.set_posture_bias(posture)
    base.move_robot_to_raised_ready_pose(
        sim=sim,
        scene=scene,
        robot=robot,
        ik=ready_ik,
        gripper=gripper,
        ee_body_id=ready_ik.end_effector_body_id,
        height_offset_m=float(collection_cfg["robot_ready_height_offset_m"]),
        finger_opening_m=episode_plan.spec.closed_finger_m,
        duration_s=pose_contract.ready_duration_s,
        target_quat_world_xyzw=canonical_quat_world_xyzw,
    )
    base.require_canonical_initial_orientation(
        robot, ik.end_effector_body_id, canonical_quat_world_xyzw, pose_contract
    )
    ik.reset()
    ik.set_posture_bias(posture)

    planner = OnlineRiskPlanner(
        runtime,
        selector=selector,
        image_rotation="none",
        global_seed=int(collection_cfg.get("policy_sampling_seed", 20260812)),
        source_episode_id=source_episode_id,
        state_mean=state_mean,
        state_std=state_std,
    )
    integrator = PersistentPoseCommandIntegrator()
    integrator_ready = False
    sim_dt = sim.get_physics_dt()
    timing = base.validate_simvla_rollout_timing(collection_cfg, sim_dt)
    latched_target = base.target_reach_pos_w(scene, episode_plan.spec).detach().clone()

    completed = False
    completed_step: int | None = None
    first_3cm_crossing_physics_step: int | None = None
    first_3cm_crossing_control_tick: int | None = None
    first_3cm_crossing_decision_index: int | None = None
    first_3cm_crossing_action_offset_inside_H10: int | None = None
    minimum_distance = float("inf")
    step = 0
    control_tick = 0
    current_plan: OnlineRiskDecisionPlan | None = None
    current_actions: np.ndarray | None = None
    current_action_index = 0
    current_executed: list[np.ndarray] = []
    current_command: PolicyCommand | None = None
    decisions: list[tuple[OnlineRiskDecisionPlan, np.ndarray]] = []
    video_path = run_store.root / "videos" / f"{episode_id}.mp4"
    writer = make_agent_video_writer(video_path) if save_video else None

    def finish_current_decision() -> None:
        nonlocal current_plan, current_executed
        if current_plan is None or not current_executed:
            return
        sequence = np.stack(current_executed).astype(np.float32)
        planner.commit_executed(current_plan, sequence)
        decisions.append((current_plan, sequence))
        current_plan = None
        current_executed = []

    try:
        while simulation_app.is_running() and step < int(collection_cfg["max_steps"]):
            if step % timing.camera_interval_steps == 0:
                scene["agent_camera"].update(sim_dt, force_recompute=True)
                scene["wrist_camera"].update(sim_dt, force_recompute=True)

            is_control_tick = step % timing.control_decimation == 0
            if is_control_tick:
                if current_actions is None or current_action_index >= len(current_actions):
                    finish_current_decision()
                    observation = base.make_live_observation(
                        scene=scene,
                        robot=robot,
                        ee_body_id=ik.end_effector_body_id,
                        instruction=episode_plan.spec.instruction,
                    )
                    if not integrator_ready:
                        integrator.reset(
                            SimVLAProprioSource(
                                ee_pos_w=observation.ee_pos_w,
                                ee_quat_wxyz=observation.ee_quat_wxyz,
                                robot_base_pos_w=observation.robot_base_pos_w,
                                robot_base_quat_wxyz=observation.robot_base_quat_wxyz,
                                finger_opening_m=observation.finger_opening_m,
                            )
                        )
                        integrator_ready = True
                    current_plan = planner.plan(observation)
                    if execution_mode != "chunk_h10":
                        raise RuntimeError(f"H10 workspace refuses execution mode {execution_mode!r}")

                    current_actions = (
                        current_plan.main_chunk_env
                        if mode == "baseline"
                        else current_plan.selected_chunk_env
                    )
                    current_action_index = 0
                    current_executed = []

                assert current_actions is not None and current_plan is not None
                action = current_actions[current_action_index].copy()
                decoded = integrator.decode(action)
                current_executed.append(action)
                current_action_index += 1
                current_command = PolicyCommand(
                    target_pos_w=torch.as_tensor(
                        decoded.target_pos_w,
                        dtype=torch.float32,
                        device=robot.device,
                    ).view(1, 3),
                    target_quat_w=torch.as_tensor(
                        decoded.target_quat_wxyz,
                        dtype=torch.float32,
                        device=robot.device,
                    ).view(1, 4),
                    finger_opening_m=float(decoded.finger_opening_m),
                )
                control_tick += 1

                if writer is not None and control_tick % 6 == 1:
                    write_agent_video_frame(
                        writer,
                        base.camera_rgb(scene, "agent_camera"),
                    )

            if current_command is None:
                raise RuntimeError("no controller command is available")
            target_quat_xyzw = torch.as_tensor(
                base.quat_wxyz_to_xyzw(
                    current_command.target_quat_w.detach().cpu().numpy()
                ),
                device=robot.device,
                dtype=torch.float32,
            )
            ik.set_target_pose(current_command.target_pos_w, target_quat_xyzw)
            ik.apply(scene, robot)
            gripper.set_width(current_command.finger_opening_m)
            gripper.apply(robot)
            scene.write_data_to_sim()
            sim.step()
            step += 1
            scene.update(sim_dt)
            metrics = base.reaching_success_metrics(
                scene=scene,
                spec=episode_plan.spec,
                target_reach_pos_w=latched_target,
            )
            distance = float(metrics.latched_distance_m[0].item())
            minimum_distance = min(minimum_distance, distance)

            # IMMEDIATE SUCCESS TERMINATION (NO DWELL)
            if distance <= 0.030:
                if first_3cm_crossing_physics_step is None:
                    first_3cm_crossing_physics_step = step
                    first_3cm_crossing_control_tick = control_tick
                    first_3cm_crossing_decision_index = (
                        current_plan.decision_index if current_plan is not None else 0
                    )
                    first_3cm_crossing_action_offset_inside_H10 = max(
                        0, current_action_index - 1
                    )
                completed = True
                completed_step = step
                break
    finally:
        close_video_writer(writer)

    if (
        not completed
        and step < int(collection_cfg["max_steps"])
        and not simulation_app.is_running()
    ):
        raise RuntimeError(
            "SimulationApp stopped before success or timeout; infrastructure failure"
        )

    finish_current_decision()
    outcome = "success" if completed else "failure_or_timeout"
    label = 0 if completed else 1
    raw_scene = raw_manifest_entry["scene"]
    fingerprint = str(raw_manifest_entry["scene_fingerprint_sha256"])

    clutter_description = [
        {
            "slot_index": int(item["slot_index"]),
            "source_name": str(item["source_name"]),
            "category_id": str(item["category_id"]),
            "variant_id": str(item["variant_id"]),
            "label": str(item["label"]),
            "pos_local": [float(value) for value in item["pos_local"]],
        }
        for item in raw_scene["clutter"]
    ]

    metadata = {
        "checkpoint_model_sha256": runtime.config.checkpoint_model_sha256,
        "uncertainty_parameterization": runtime.config.uncertainty_parameterization,
        "manifest_fingerprint_sha256": manifest_fingerprint,
        "policy_sampling_seed": int(collection_cfg.get("policy_sampling_seed", 20260812)),
        "source_episode_id": source_episode_id,
        "source_benchmark_episode_id": int(raw_manifest_entry["benchmark_episode_id"]),
        "global_episode_id": episode_id,
        "scene_family_id": scene_family_id(fingerprint),
        "scene_fingerprint_sha256": fingerprint,
        "official_scene_sampler_seed": int(collection_cfg["seed"]),
        "scene_reset_seed": int(collection_cfg["seed"]),
        "scene_seed_inputs": [int(collection_cfg["seed"]), source_episode_id],
        "target_position_index": int(raw_scene["target_position_index"]),
        "clutter_position_index": int(raw_scene["clutter_position_index"]),
        "clutter_cardinality": len(clutter_description),
        "clutter_description": clutter_description,
        "target_source_name": str(raw_scene["target"]["source_name"]),
        "risk_split": "ood_test",
        "instruction": episode_plan.spec.instruction,
        "target_category_id": scene_assets.object_context.category_id,
        "target_variant_id": scene_assets.object_context.variant_id,
        "target_label": scene_assets.object_context.label,
        "first_3cm_crossing_physics_step": first_3cm_crossing_physics_step,
        "first_3cm_crossing_control_tick": first_3cm_crossing_control_tick,
        "first_3cm_crossing_decision_index": first_3cm_crossing_decision_index,
        "first_3cm_crossing_action_offset_inside_H10": first_3cm_crossing_action_offset_inside_H10,
        "completed_physics_step": completed_step if completed else step,
        "completed_control_tick": control_tick,
        "number_of_queries": len(decisions),
        "controller_mode": mode,
    }

    summary = {
        "episode_id": episode_id,
        "source_episode_id": source_episode_id,
        "source_benchmark_episode_id": int(raw_manifest_entry["benchmark_episode_id"]),
        "global_episode_id": episode_id,
        "execution_mode": execution_mode,
        "outcome": outcome,
        "success": bool(completed),
        "risk_label": int(label),
        "minimum_tcp_distance_m": float(minimum_distance),
        "strict_success_threshold_m": 0.030,
        "control_ticks": control_tick,
        "simulation_steps": completed_step if completed else step,
        "decision_rows": len(decisions),
        "first_3cm_crossing_physics_step": first_3cm_crossing_physics_step,
        "first_3cm_crossing_control_tick": first_3cm_crossing_control_tick,
        "first_3cm_crossing_decision_index": first_3cm_crossing_decision_index,
        "first_3cm_crossing_action_offset_inside_H10": first_3cm_crossing_action_offset_inside_H10,
        "completed_physics_step": completed_step if completed else step,
        "completed_control_tick": control_tick,
        "number_of_queries": len(decisions),
        "scene_fingerprint_sha256": fingerprint,
        "manifest_fingerprint_sha256": manifest_fingerprint,
        "instruction": episode_plan.spec.instruction,
        "target_category_id": scene_assets.object_context.category_id,
        "target_variant_id": scene_assets.object_context.variant_id,
        "target_label": scene_assets.object_context.label,
        "target_position_index": int(raw_scene["target_position_index"]),
        "clutter_position_index": int(raw_scene["clutter_position_index"]),
        "clutter_cardinality": len(clutter_description),
        "clutter_description": clutter_description,
        "risk_split": "ood_test",
        "official_scene_sampler_seed": int(collection_cfg["seed"]),
        "policy_sampling_seed": int(collection_cfg.get("policy_sampling_seed", 20260812)),
        "scene_reset_seed": int(collection_cfg["seed"]),
        "schema_version": "simvla_isaac_risk_episode_summary_v2_3cm350",
    }

    rows = [
        decision_to_row(
            episode_id=episode_id,
            execution_mode=execution_mode,
            plan=plan,
            sequence=sequence,
            outcome=outcome,
            label=label,
            metadata=metadata,
        )
        for plan, sequence in decisions
    ]

    run_store.save_episode(
        episode_id=episode_id,
        summary=summary,
        decisions=rows,
    )
    return completed, len(rows)


def run_collection(args: argparse.Namespace, simulation_app: Any) -> None:
    base = load_pinned_rollout()
    import yaml
    from franka_wrist_camera_scene.simvla.ood_benchmark import load_benchmark_manifest
    from franka_wrist_camera_scene.utils.paths import load_yaml_config

    run_cfg = load_yaml_config(args.run_config)
    collection_cfg_path = Path(run_cfg["collection_config"]).resolve()
    raw_collection_cfg = yaml.safe_load(collection_cfg_path.read_text())
    collection_cfg = raw_collection_cfg["collections"][int(run_cfg.get("collection_index", 0))]

    # Force protocol invariants
    collection_cfg["max_steps"] = 1400  # 350 control ticks * 4 decimation
    collection_cfg["success_threshold_m"] = 0.030
    collection_cfg["settle_time_s"] = 0.0
    collection_cfg["policy_sampling_seed"] = 20260812
    collection_cfg["clutter"]["count_options"] = [4, 5, 6, 7, 8, 9, 10, 11, 12]

    eval_cfg = base.load_yaml_config(run_cfg["simvla"]["eval_config"])
    manifest = load_benchmark_manifest(args.manifest)
    raw_manifest = json.loads(args.manifest.read_text())
    raw_manifest_entries = {
        int(item["benchmark_episode_id"]): item for item in raw_manifest["episodes"]
    }

    selector = OnlineRiskSelector(
        model_path=args.risk_model_path,
        normalization_path=args.risk_normalization,
        main_threshold=args.main_threshold,
        selected_score_cap=args.selected_cap,
        main_threshold_name=args.main_threshold_name,
        selected_cap_name=args.selected_cap_name,
    )

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    run_store = OOD400EpisodeStore(output_dir)

    selected = list(manifest.shard(args.offset, args.count))
    scene_assets_map = load_manifest_scene_assets(base, collection_cfg, selected)
    asset_bank = base._build_asset_bank(scene_assets_map)

    first_id = int(selected[0].source_episode_id)
    first_assets = scene_assets_map[first_id]
    first_names = base._episode_asset_names(asset_bank, first_assets)
    base_spec, sampling_options = base.make_sampling_options(collection_cfg)
    first_plan = base._make_episode_plan(
        collection_cfg,
        base_spec,
        first_assets,
        int(collection_cfg["seed"]),
        first_id,
        sampling_options,
        first_names,
    )

    scene_cfg = base.make_reaching_asset_bank_scene_cfg(
        target_usd_paths=asset_bank.target_usd_paths,
        clutter_usd_paths=asset_bank.clutter_usd_paths,
        initial_target_name=first_names.object_name,
        initial_clutter_names=first_names.clutter_names,
        initial_clutter_specs=first_plan.clutter_specs,
        num_envs=1,
        env_spacing=float(collection_cfg.get("env_spacing", 5.0)),
    )
    configured_robot_usd = str(scene_cfg.robot.spawn.usd_path)
    if (
        configured_robot_usd.endswith("/FrankaEmika/panda_instanceable.usd")
        and "/6.0/" in configured_robot_usd
    ):
        scene_cfg.robot.spawn.usd_path = ISAAC_6_LEGACY_FRANKA_USD

    camera_width, camera_height = base._configured_camera_resolution(collection_cfg)
    agent_width, agent_height, wrist_width, wrist_height = (
        base._configured_camera_resolutions(collection_cfg)
    )
    base._apply_camera_resolution(
        scene_cfg,
        camera_width,
        camera_height,
        record_depth=False,
        camera_fps=int(collection_cfg["camera_fps"]),
        agent_width=agent_width,
        agent_height=agent_height,
        wrist_width=wrist_width,
        wrist_height=wrist_height,
    )

    runtime = base.SimVLARuntime(base.build_runtime_config(eval_cfg, "cuda:0"))
    runtime.load()
    norm_payload = json.loads(Path(runtime.config.norm_stats_path).read_text())
    state_mean = np.asarray(norm_payload["norm_stats"]["state"]["mean"], dtype=np.float32)
    state_std = np.asarray(norm_payload["norm_stats"]["state"]["std"], dtype=np.float32)

    sim = base.sim_utils.SimulationContext(
        base.make_simulation_cfg(
            "cuda:0", use_fabric=bool(collection_cfg.get("use_fabric", True))
        )
    )
    scene = base.InteractiveScene(scene_cfg)
    pose_contract = base.parse_reaching_pose_contract(collection_cfg["pose_controller"])
    ready_ik, ik = base.create_shared_reaching_ik_controllers(pose_contract)
    gripper = base.GripperController()
    sim.reset()
    sim.set_camera_view(eye=[2.2, -2.2, 1.9], target=[0.55, 0.0, 1.20])
    robot = scene["robot"]
    ready_ik.bind(scene, robot)
    ik.bind(scene, robot)
    gripper.bind(scene, robot)

    print(f"=== Starting OOD400 run mode={args.mode} [{args.offset}..{args.offset + len(selected)}] ({len(selected)} eps) ===", flush=True)
    print(f"  Model: {args.risk_model_path} (SHA: {selector.model_sha256[:16]}...)", flush=True)
    print(f"  Norm: {args.risk_normalization} (SHA: {selector.normalization_sha256[:16]}...)", flush=True)
    print(f"  A = {selector.main_threshold:.6f} ({selector.main_threshold_name}), C = {selector.selected_score_cap:.4f}", flush=True)
    print(f"  Output: {output_dir}", flush=True)

    existing_summaries = set()
    if (output_dir / "episode_summaries.jsonl").exists():
        for line in (output_dir / "episode_summaries.jsonl").read_text().splitlines():
            if line.strip():
                try:
                    d = json.loads(line)
                    existing_summaries.add(d["episode_id"])
                except Exception:
                    pass
    print(f"  Already completed in output_dir: {len(existing_summaries)} episodes", flush=True)

    successes = 0
    failures = 0
    total_rows = 0
    plans = {first_id: first_plan}

    for ep_idx, ep in enumerate(selected):
        bench_id = int(ep.benchmark_episode_id)
        global_id_str = f"{bench_id:06d}"
        if global_id_str in existing_summaries:
            print(f"[{ep_idx+1}/{len(selected)}] Skipping already-complete episode {global_id_str}", flush=True)
            continue

        raw_entry = raw_manifest_entries[bench_id]
        scene_assets = scene_assets_map[ep.source_episode_id]

        plan = plans.get(ep.source_episode_id)
        if plan is None:
            names = base._episode_asset_names(asset_bank, scene_assets)
            plan = base._make_episode_plan(
                collection_cfg,
                base_spec,
                scene_assets,
                int(collection_cfg["seed"]),
                ep.source_episode_id,
                sampling_options,
                names,
            )

        t0 = time.time()
        succ, rows = run_episode(
            base=base,
            sim=sim,
            scene=scene,
            robot=robot,
            ready_ik=ready_ik,
            ik=ik,
            gripper=gripper,
            runtime=runtime,
            collection_cfg=collection_cfg,
            episode=ep,
            episode_plan=plan,
            scene_assets=scene_assets,
            asset_bank=asset_bank,
            simulation_app=simulation_app,
            state_mean=state_mean,
            state_std=state_std,
            execution_mode=args.execution_mode,
            run_store=run_store,
            manifest_fingerprint=manifest.manifest_fingerprint_sha256,
            global_id=global_id_str,
            raw_manifest_entry=raw_entry,
            selector=selector,
            mode=args.mode,
            save_video=args.save_video,
        )
        elapsed = time.time() - t0
        if succ:
            successes += 1
        else:
            failures += 1
        total_rows += rows

        res_str = "SUCCESS" if succ else "FAILURE"
        print(
            f"[{ep_idx+1}/{len(selected)}] Ep {global_id_str} (bench {bench_id:03d}) -> {res_str} | "
            f"{rows} rows | {elapsed:.2f}s | running: {successes}S/{failures}F",
            flush=True,
        )

    print("=== Run Completed Successfully ===", flush=True)
    print(f"Total processed: {successes + failures}, Successes: {successes}, Failures: {failures}, Total rows: {total_rows}", flush=True)


def main() -> int:
    args = parse_args()
    from franka_wrist_camera_scene.app import launcher
    from isaaclab.app import AppLauncher

    app_launcher = AppLauncher(args)
    simulation_app = app_launcher.app
    launcher.patch_physx_schema()
    try:
        run_collection(args, simulation_app)
    except BaseException:
        traceback.print_exc()
        return 1
    finally:
        simulation_app.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
