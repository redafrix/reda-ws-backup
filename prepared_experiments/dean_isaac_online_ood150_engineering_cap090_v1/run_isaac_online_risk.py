#!/usr/bin/env python3
"""Closed-loop Isaac SimVLA H10 + TopK8 risk argmin-cap online evaluator."""

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

WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
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

from online_isaac_runtime import OnlineRiskPlanner, OnlineRiskDecisionPlan, OnlineRiskSelector  # noqa: E402
from risk_collection.rounds import (  # noqa: E402
    ROUND_SCHEDULE_VERSION,
    balanced_round_robin_order,
    global_episode_id,
    scene_family_id,
    schedule_sha256,
)
from risk_collection.smoke_safety import (  # noqa: E402
    validate_forced_timeout_smoke_request,
)
from risk_collection.storage import EpisodeStore  # noqa: E402
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
            command = (entry / "cmdline").read_bytes().replace(b"\0", b" ").decode()
        except (OSError, UnicodeDecodeError):
            continue
        if needle in command and int(entry.name) != os.getpid():
            matches.append((int(entry.name), command.strip()))
    return matches


def require_gpu_safe() -> None:
    trainers = process_matches("scripts/train_grad_accum.py")
    if trainers:
        raise RuntimeError(f"pi0.5 trainer is active; refusing CUDA/Isaac launch: {trainers}")
    rollouts = (
        process_matches("simvla_reaching_rollout.py")
        + process_matches("collect_isaac_risk.py")
        + process_matches("run_isaac_online_risk.py")
    )
    if rollouts:
        raise RuntimeError(f"another Isaac/SimVLA collector is active: {rollouts}")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_snapshot(path: Path) -> dict[str, Any]:
    def git(*arguments: str) -> str:
        result = subprocess.run(
            ["git", "-C", str(path), *arguments],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()

    status = git("status", "--short", "--untracked-files=no")
    return {
        "path": str(path.resolve()),
        "commit": git("rev-parse", "HEAD"),
        "dirty": bool(status),
        "dirty_state_sha256": hashlib.sha256(status.encode("utf-8")).hexdigest(),
    }


def workspace_source_hashes() -> dict[str, str]:
    paths: list[Path] = [Path(__file__).resolve()]
    for relative_root in ("src", "configs", "schemas"):
        root = WORKSPACE / relative_root
        paths.extend(
            path
            for path in root.rglob("*")
            if path.is_file()
            and "__pycache__" not in path.parts
            and path.suffix in {".py", ".sh", ".yaml", ".json"}
        )
    return {
        str(path.relative_to(WORKSPACE)): sha256_file(path)
        for path in sorted(set(paths))
    }


def build_run_manifest(
    *,
    args: argparse.Namespace,
    run_cfg: dict[str, Any],
    collection_cfg: dict[str, Any],
    eval_cfg: dict[str, Any],
    raw_manifest: dict[str, Any],
    manifest: Any,
    scheduled_benchmark_ids: list[int],
) -> dict[str, Any]:
    checkpoint_path = Path(eval_cfg["simvla"]["checkpoint_path"]).resolve()
    checkpoint_config_path = checkpoint_path / "config.json"
    checkpoint_config = json.loads(checkpoint_config_path.read_text())
    norm_path = Path(eval_cfg["simvla"]["norm_stats_path"]).resolve()
    eval_config_path = Path(run_cfg["simvla"]["eval_config"]).resolve()
    collection_config_path = Path(run_cfg["collection_config"]).resolve()
    source_manifest_path = Path(raw_manifest["provenance"]["source_manifest"]).resolve()
    collection_partitions = Counter(
        str(item.get("risk_split", "unassigned")) for item in raw_manifest["episodes"]
    )
    max_sim_steps = int(collection_cfg["max_steps"])
    decimation = 4
    if max_sim_steps != 2400:
        raise RuntimeError(
            f"corrected risk collection requires max_steps=2400, got {max_sim_steps}"
        )
    if max_sim_steps % decimation:
        raise RuntimeError("max_steps must be divisible by control decimation")
    if float(collection_cfg["success_threshold_m"]) != 0.02:
        raise RuntimeError("corrected collection requires a 0.02 m threshold")
    if float(collection_cfg["settle_time_s"]) != 0.2:
        raise RuntimeError("corrected collection requires a 0.2 s settle time")

    round_enabled = args.round_id is not None
    round_payload = {
        "enabled": round_enabled,
        "round_id": int(args.round_id) if round_enabled else None,
        "round_kind": str(args.round_kind) if round_enabled else None,
        "master_seed": int(args.round_master_seed) if round_enabled else None,
        "global_episode_id_format": (
            "r{round_id:03d}_s{source_episode_id:06d}" if round_enabled else None
        ),
        "scene_family_key": "scene_fingerprint_sha256",
        "schedule": {
            "version": ROUND_SCHEDULE_VERSION if args.balanced_order else "manifest_order",
            "balanced_round_robin": bool(args.balanced_order),
            "benchmark_episode_ids_sha256": schedule_sha256(
                scheduled_benchmark_ids,
                version=(
                    ROUND_SCHEDULE_VERSION
                    if args.balanced_order
                    else "manifest_order"
                ),
            ),
            "episode_count": len(scheduled_benchmark_ids),
        },
    }

    return {
        "schema_version": "simvla_isaac_risk_run_v3_h10_timeout2400",
        "round": round_payload,
        "execution_mode": args.execution_mode,
        "episode_cap": len(raw_manifest["episodes"]),
        "manifest_path": str(args.manifest.resolve()),
        "manifest_sha256": sha256_file(args.manifest),
        "manifest_fingerprint_sha256": manifest.manifest_fingerprint_sha256,
        "source_manifest_path": str(source_manifest_path),
        "source_manifest_sha256": sha256_file(source_manifest_path),
        "run_config_path": str(args.run_config.resolve()),
        "run_config_sha256": sha256_file(args.run_config),
        "collection_config_path": str(collection_config_path),
        "collection_config_sha256": sha256_file(collection_config_path),
        "evaluation_config_path": str(eval_config_path),
        "evaluation_config_sha256": sha256_file(eval_config_path),
        "collector_source_path": str(Path(__file__).resolve()),
        "collector_source_sha256": sha256_file(Path(__file__).resolve()),
        "checkpoint": {
            "path": str(checkpoint_path),
            "model_path": str(checkpoint_path / "model.safetensors"),
            "model_sha256": sha256_file(checkpoint_path / "model.safetensors"),
            "recorded_model_sha256": eval_cfg["simvla"][
                "checkpoint_model_sha256"
            ],
            "config_path": str(checkpoint_config_path),
            "config_sha256": sha256_file(checkpoint_config_path),
            "architecture_identity": {
                "architectures": checkpoint_config.get("architectures"),
                "model_type": checkpoint_config.get("model_type"),
                "action_mode": eval_cfg["simvla"]["action_mode"],
                "num_actions": int(eval_cfg["simvla"]["num_actions"]),
                "action_dim": 7,
            },
            "uncertainty_mode": "softplus_raw_variance",
        },
        "normalization": {
            "path": str(norm_path),
            "sha256": sha256_file(norm_path),
        },
        "codebases": {
            "simvla": git_snapshot(
                Path(eval_cfg["simvla"]["repo_path"]).resolve()
            ),
            "isaac": git_snapshot(PINNED_ISAAC),
            "isolated_workspace_source_sha256": workspace_source_hashes(),
        },
        "timing": {
            "max_sim_steps": max_sim_steps,
            "physics_hz": 120,
            "control_hz": 30,
            "camera_hz": 30,
            "state_hz": 30,
            "decimation": decimation,
            "control_ticks_per_replan": 10,
            "max_control_ticks": max_sim_steps // decimation,
            "max_decision_rows": max_sim_steps // (decimation * 10),
        },
        "success": {
            "threshold_m": float(collection_cfg["success_threshold_m"]),
            "dwell_settle_time_s": float(collection_cfg["settle_time_s"]),
        },
        "policy": {
            "action_horizon": 10,
            "action_dim": 7,
            "main_candidate_count": 1,
            "ace_alternative_count": 8,
            "ace_metric_style": "new_training",
            "ace_feature_names": list(ACE_7D_KEYS),
            "policy_sampling_seed": int(collection_cfg["policy_sampling_seed"]),
            "candidate_seed_rule": (
                "sha256('simvla-isaac-risk-v1|global_seed|source_episode_id|"
                "decision_index|candidate_index')[:16] modulo (2**31-1)"
            ),
        },
        "risk_features": {
            "feature_49d_key_order": list(UNCERTAINTY_49D_KEYS),
            "topk8_indices": list(TOPK8_INDICES),
            "static_layout": "action_stats_28 + ace_7 + proprio_8 + topk_8 = 51",
            "history_layout": "16 x (proprio_8 + first_executed_env_action_7 + ace_first6) = 16 x 21",
            "history_snapshot_timing": "pre-action",
            "history_executed_action_semantics": "first action of the previously executed H10 chunk",
        },
        "cameras": {
            "order": ["agent_camera", "wrist_camera", "padded_third_camera"],
            "dataset_mapping": ["agent_rgb", "wrist_rgb", "absent"],
            "padded_camera_policy": "third camera is zeros and invalid/masked",
        },
        "execution": {
            "mode": "chunk_h10",
            "prediction": "H10",
            "replan_steps": 10,
            "applied_actions_per_replan": 10,
            "terminal_success_may_end_final_chunk_early": True,
        },
        "splits": {
            "collection_manifest_partition_seed": 123,
            "collection_manifest_partition_counts": dict(
                sorted(collection_partitions.items())
            ),
            "collection_manifest_partition_semantics": (
                "non-authoritative category-balanced collection partition only"
            ),
            "saved_row_scientific_split": (
                "synthetic_smoke"
                if args.force_timeout_smoke
                else "unassigned_seen"
            ),
            "final_risk_split_seed": 20260622,
            "final_risk_split_ratios": {
                "train": 0.70,
                "calibration": 0.15,
                "test": 0.15,
            },
            "final_risk_split_group_key": "scene_family_id",
            "final_risk_split_group_key_fallback": "scene_fingerprint_sha256",
            "final_risk_split_stratification": "episode success/failure outcome",
            "ood150_semantics": "final test only",
        },
        "infrastructure": {
            "retries_after_first_attempt": int(
                collection_cfg.get("infrastructure_retry_count", 2)
            ),
            "errors_are_training_labels": False,
            "stop_marker": "STOP_AFTER_CURRENT_EPISODE",
        },
        "synthetic_smoke": {
            "forced_timeout_enabled": bool(args.force_timeout_smoke),
            "success_termination_suppressed": bool(args.force_timeout_smoke),
            "training_eligible": False if args.force_timeout_smoke else None,
            "allowed_output_root": str(
                (WORKSPACE / "smokes_timeout2400").resolve()
            ),
        },
        "ood150_used_for_training": False,
        "ood150_used_for_calibration": False,
    }


def load_manifest_scene_assets(
    base: Any,
    collection_cfg: dict[str, Any],
    episodes: list[Any],
) -> dict[int, Any]:
    """Resolve the exact target and clutter assets recorded by the manifest."""
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
                f"manifest asset resolution mismatch: expected={expected_key}, "
                f"actual={actual_key}"
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


def parse_args() -> argparse.Namespace:
    require_gpu_safe()
    from isaaclab.app import AppLauncher

    parser = argparse.ArgumentParser()
    parser.add_argument("--run-config", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--risk-model-root", type=Path, required=True)
    parser.add_argument("--risk-normalization", type=Path, required=True)
    parser.add_argument("--main-threshold", default=None)
    parser.add_argument("--selected-cap", default=None)
    parser.add_argument("--controller-config", type=Path, default=None, help="Path to frozen controller JSON config")
    parser.add_argument("--online-mode", choices=("shadow", "active"), required=True)
    parser.add_argument("--online-role", choices=("shadow", "dev", "holdout", "full150"), required=True)
    parser.add_argument("--protocol-id", required=True)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--count", type=int)
    parser.add_argument("--round-id", type=int)
    parser.add_argument("--round-kind", choices=("broad", "enrichment"))
    parser.add_argument("--round-master-seed", type=int)
    parser.add_argument(
        "--balanced-order",
        action="store_true",
        help="interleave seen categories/clutter strata without changing membership",
    )
    parser.add_argument(
        "--execution-mode",
        choices=("chunk_h10",),
        required=True,
        help="H10 production invariant: execute all ten predicted actions before replanning",
    )
    parser.add_argument("--inference-only", action="store_true")
    parser.add_argument("--save-video", action="store_true")
    parser.add_argument("--max-steps", type=int)
    parser.add_argument(
        "--force-timeout-smoke",
        action="store_true",
        help=(
            "TEST ONLY: suppress success termination and run exactly 2400 "
            "simulator steps; output is restricted to smokes_timeout2400"
        ),
    )
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
    if args.offset < 0 or (args.count is not None and args.count <= 0):
        parser.error("invalid manifest shard")
    round_values = (args.round_id, args.round_kind, args.round_master_seed)
    if any(value is not None for value in round_values) and not all(
        value is not None for value in round_values
    ):
        parser.error(
            "--round-id, --round-kind, and --round-master-seed must be provided together"
        )
    if args.round_id is not None:
        if args.round_id < 0 or args.round_id > 999:
            parser.error("--round-id must be between 0 and 999")
        if args.force_timeout_smoke:
            parser.error("production round identity is incompatible with synthetic smoke")
        if not args.balanced_order:
            parser.error("production rounds require --balanced-order")
    try:
        validate_forced_timeout_smoke_request(
            enabled=bool(args.force_timeout_smoke),
            output_dir=args.output_dir,
            smoke_root=WORKSPACE / "smokes_timeout2400",
            count=args.count,
            execution_mode=args.execution_mode,
            inference_only=bool(args.inference_only),
            max_steps_override=args.max_steps,
        )
    except ValueError as error:
        parser.error(str(error))
    return args


def make_video_writer(path: Path, width: int = 1120, height: int = 480):
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
        "10",
        "-i",
        "-",
        "-an",
        "-c:v",
        "libx264",
        "-crf",
        "18",
        "-pix_fmt",
        "yuv420p",
        str(path),
    ]
    return subprocess.Popen(command, stdin=subprocess.PIPE)


def write_video_frame(writer: Any, agent: np.ndarray, wrist: np.ndarray) -> None:
    from PIL import Image

    wrist_resized = np.asarray(
        Image.fromarray(wrist).resize((480, 480), Image.Resampling.BICUBIC)
    )
    frame = np.concatenate([agent, wrist_resized], axis=1)
    if frame.shape != (480, 1120, 3):
        raise RuntimeError(f"unexpected review video frame shape: {frame.shape}")
    assert writer.stdin is not None
    writer.stdin.write(np.ascontiguousarray(frame).tobytes())


def close_video_writer(writer: Any) -> None:
    if writer is None:
        return
    assert writer.stdin is not None
    writer.stdin.close()
    return_code = writer.wait(timeout=60)
    if return_code != 0:
        raise RuntimeError(f"ffmpeg exited with {return_code}")


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
    run_store: EpisodeStore,
    manifest_fingerprint: str,
    scientific_risk_split: str,
    collection_manifest_partition: str,
    global_id: str,
    round_provenance: dict[str, Any],
    raw_manifest_entry: dict[str, Any],
    force_timeout_smoke: bool,
    save_video: bool,
    inference_only: bool,
    selector: OnlineRiskSelector,
    online_mode: str,
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
        global_seed=int(collection_cfg["policy_sampling_seed"]),
        source_episode_id=source_episode_id,
        state_mean=state_mean,
        state_std=state_std,
        verify_single_runtime_parity=inference_only,
    )
    integrator = PersistentPoseCommandIntegrator()
    integrator_ready = False
    sim_dt = sim.get_physics_dt()
    timing = base.validate_simvla_rollout_timing(collection_cfg, sim_dt)
    latched_target = base.target_reach_pos_w(scene, episode_plan.spec).detach().clone()
    max_settle_steps = int(float(collection_cfg["settle_time_s"]) / sim_dt)
    settle_steps = 0
    completed = False
    completed_step: int | None = None
    natural_success_observed = False
    natural_success_step: int | None = None
    minimum_distance = float("inf")
    step = 0
    control_tick = 0
    current_plan: OnlineRiskDecisionPlan | None = None
    current_actions: np.ndarray | None = None
    current_action_index = 0
    current_executed: list[np.ndarray] = []
    current_command: PolicyCommand | None = None
    decisions: list[tuple[OnlineRiskDecisionPlan, np.ndarray]] = []
    writer = (
        make_video_writer(run_store.root / "videos" / f"{episode_id}.mp4")
        if save_video
        else None
    )

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
                    if inference_only:
                        write_json = {
                            "inference_only": True,
                            "episode_id": episode_id,
                            "main_seed": current_plan.main_seed,
                            "nine_seeds_unique": len(
                                {current_plan.main_seed, *current_plan.ace_seeds}
                            )
                            == 9,
                            "main_chunk_shape": list(
                                current_plan.main_chunk_env.shape
                            ),
                            "ace_chunk_shape": list(
                                current_plan.ace_chunks_env.shape
                            ),
                            "uncertainty_shape": list(
                                current_plan.uncertainty_49d.shape
                            ),
                            "vlm_encoding_count": current_plan.vlm_encoding_count,
                            "online_candidate_scores": current_plan.candidate_scores.tolist(),
                            "online_selected_candidate_index": int(current_plan.selection.selected_index),
                            "online_selection_reason": current_plan.selection.reason,
                            "single_runtime_parity_max_abs": (
                                current_plan.single_runtime_parity_max_abs
                            ),
                            "candidate0_single_runtime_parity": (
                                current_plan.single_runtime_parity_max_abs is not None
                                and current_plan.single_runtime_parity_max_abs <= 1e-5
                            ),
                        }
                        run_store.update_status(write_json)
                        return True, 0
                    if execution_mode != "chunk_h10":
                        raise RuntimeError(
                            f"H10 workspace refuses execution mode {execution_mode!r}"
                        )
                    current_actions = (
                        current_plan.main_chunk_env
                        if online_mode == "shadow"
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

                if writer is not None and control_tick % 3 == 1:
                    write_video_frame(
                        writer,
                        base.camera_rgb(scene, "agent_camera"),
                        base.camera_rgb(scene, "wrist_camera"),
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
            if bool(metrics.success[0].item()):
                settle_steps += 1
                if settle_steps >= max_settle_steps:
                    if not natural_success_observed:
                        natural_success_observed = True
                        natural_success_step = step
                    if force_timeout_smoke:
                        pass
                    else:
                        completed = True
                        completed_step = step
                        break
            else:
                settle_steps = 0
    finally:
        close_video_writer(writer)

    if (
        not completed
        and step < int(collection_cfg["max_steps"])
        and not simulation_app.is_running()
    ):
        raise RuntimeError(
            "SimulationApp stopped before success or the configured timeout; "
            "this is an infrastructure error, not a failure label"
        )

    if force_timeout_smoke and step != 2400:
        raise RuntimeError(
            f"forced-timeout smoke must execute exactly 2400 steps, got {step}"
        )

    finish_current_decision()
    outcome = (
        "failure_or_timeout"
        if force_timeout_smoke
        else ("success" if completed else "failure_or_timeout")
    )
    label = 0 if outcome == "success" else 1
    raw_scene = raw_manifest_entry["scene"]
    fingerprint = str(raw_manifest_entry["scene_fingerprint_sha256"])
    training_eligible = (
        round_provenance["round_id"] is not None
        and not force_timeout_smoke
        and collection_manifest_partition != "ood_smoke"
    )
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
        "policy_sampling_seed": int(collection_cfg["policy_sampling_seed"]),
        "source_episode_id": source_episode_id,
        "source_benchmark_episode_id": int(
            raw_manifest_entry["benchmark_episode_id"]
        ),
        "global_episode_id": episode_id,
        "round_id": round_provenance["round_id"],
        "round_kind": round_provenance["round_kind"],
        "round_master_seed": round_provenance["round_master_seed"],
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
        "risk_split": scientific_risk_split,
        "collection_manifest_partition": collection_manifest_partition,
        "instruction": episode_plan.spec.instruction,
        "camera_mapping": {
            "agent_camera": "agent_rgb",
            "wrist_camera": "wrist_rgb",
            "padded_third_camera": "absent",
        },
        "agent_camera_shape": list(base.camera_rgb(scene, "agent_camera").shape),
        "wrist_camera_shape": list(base.camera_rgb(scene, "wrist_camera").shape),
        "target_category_id": scene_assets.object_context.category_id,
        "target_variant_id": scene_assets.object_context.variant_id,
        "target_label": scene_assets.object_context.label,
        "target_source_name": str(raw_scene["target"]["source_name"]),
        "controller_contract_fingerprint_sha256": (
            runtime.config.pose_controller_fingerprint_sha256
        ),
        "contract_fingerprint_sha256": runtime.config.contract_fingerprint_sha256,
        "deployable_inputs_exclude_outcome": True,
        "deployable_inputs_exclude_task_id_seed_timestep_reward": True,
        "ood_excluded_from_training": collection_manifest_partition == "ood_smoke",
        "synthetic_smoke": bool(force_timeout_smoke),
        "training_eligible": training_eligible,
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
    summary = {
        "schema_version": "simvla_isaac_risk_episode_summary_v1",
        "episode_id": episode_id,
        "source_episode_id": source_episode_id,
        "source_benchmark_episode_id": int(
            raw_manifest_entry["benchmark_episode_id"]
        ),
        "global_episode_id": episode_id,
        "round_id": round_provenance["round_id"],
        "round_kind": round_provenance["round_kind"],
        "round_master_seed": round_provenance["round_master_seed"],
        "scene_family_id": scene_family_id(fingerprint),
        "scene_fingerprint_sha256": fingerprint,
        "official_scene_sampler_seed": int(collection_cfg["seed"]),
        "scene_reset_seed": int(collection_cfg["seed"]),
        "policy_sampling_seed": int(collection_cfg["policy_sampling_seed"]),
        "target_category_id": scene_assets.object_context.category_id,
        "target_variant_id": scene_assets.object_context.variant_id,
        "target_label": scene_assets.object_context.label,
        "target_position_index": int(raw_scene["target_position_index"]),
        "clutter_position_index": int(raw_scene["clutter_position_index"]),
        "clutter_cardinality": len(clutter_description),
        "clutter_description": clutter_description,
        "risk_split": scientific_risk_split,
        "collection_manifest_partition": collection_manifest_partition,
        "execution_mode": execution_mode,
        "outcome": outcome,
        "risk_label": label,
        "success": outcome == "success",
        "synthetic_smoke": bool(force_timeout_smoke),
        "success_termination_suppressed": bool(force_timeout_smoke),
        "natural_success_observed": natural_success_observed,
        "natural_success_step": natural_success_step,
        "strict_success_threshold_m": float(
            episode_plan.spec.success_threshold_m
        ),
        "settle_time_s": float(collection_cfg["settle_time_s"]),
        "completed_step": completed_step,
        "simulation_steps": step,
        "control_ticks": control_tick,
        "decision_rows": len(rows),
        "minimum_tcp_distance_m": minimum_distance,
        "instruction": episode_plan.spec.instruction,
        "online_policy": "simvla_h10_topk8_argmin_on_alarm_cap",
        "online_mode": online_mode,
        "online_action_modifications_count": sum(
            int(plan.selection.selected_index != 0) for plan, _sequence in decisions
        ) if online_mode == "active" else 0,
        "online_proposed_modifications_count": sum(
            int(plan.selection.proposed_modification) for plan, _sequence in decisions
        ),
        "online_changed_decision_indices": [
            int(plan.decision_index) for plan, _sequence in decisions
            if online_mode == "active" and plan.selection.selected_index != 0
        ],
        "online_first_modification_decision_index": next(
            (int(plan.decision_index) for plan, _sequence in decisions
             if online_mode == "active" and plan.selection.selected_index != 0),
            None,
        ),
        "online_risk_main_score_max": max(
            (float(plan.selection.main_score) for plan, _sequence in decisions),
            default=0.0,
        ),
        "online_risk_selected_score_mean": float(np.mean([
            float(plan.selection.selected_score) for plan, _sequence in decisions
        ])) if decisions else 0.0,
        "manifest_fingerprint_sha256": manifest_fingerprint,
        "training_eligible": training_eligible,
        "scientific_split_pending": scientific_risk_split == "unassigned_seen",
    }
    run_store.finalize_episode(episode_id, rows, summary)
    return completed, len(rows)


def run_collection(args: argparse.Namespace, simulation_app: Any) -> None:
    base = load_pinned_rollout()
    run_cfg = base.load_yaml_config(args.run_config)
    run_cfg["benchmark_manifest"] = str(args.manifest.resolve())
    run_cfg["output_dir"] = str(args.output_dir.resolve())
    if args.max_steps is not None:
        run_cfg["max_steps"] = int(args.max_steps)
    collection_cfg = base.rollout_collection_config(run_cfg)
    if args.round_id is not None:
        expected_output_name = (
            f"final_seen_h10_round_{int(args.round_id):03d}_seed"
            f"{int(collection_cfg['policy_sampling_seed'])}"
        )
        expected_root = (WORKSPACE / "outputs" / expected_output_name).resolve()
        if args.output_dir.resolve() != expected_root:
            raise RuntimeError(
                "production round output must be the exact immutable round path: "
                f"{expected_root}"
            )
        if args.round_kind == "broad" and (
            args.offset != 0
            or args.count != len(json.loads(args.manifest.read_text())["episodes"])
        ):
            raise RuntimeError(
                "production broad round must select the complete manifest with offset 0"
            )
    if args.force_timeout_smoke:
        if int(collection_cfg["max_steps"]) != 2400:
            raise RuntimeError("forced-timeout smoke requires config max_steps=2400")
        if not args.output_dir.resolve().is_relative_to(
            (WORKSPACE / "smokes_timeout2400").resolve()
        ):
            raise RuntimeError("forced-timeout smoke escaped its isolated output root")
    eval_cfg = base.load_yaml_config(run_cfg["simvla"]["eval_config"])
    base.validate_eval_config(eval_cfg)
    base.validate_collection_contract(collection_cfg, eval_cfg)
    seed = int(collection_cfg["seed"])

    raw_manifest = json.loads(args.manifest.read_text())
    manifest = base.load_benchmark_manifest(args.manifest)
    raw_by_output_id = {
        int(item["benchmark_episode_id"]): item for item in raw_manifest["episodes"]
    }
    selected = list(manifest.shard(args.offset, args.count))
    if args.balanced_order:
        selected_by_benchmark_id = {
            int(episode.benchmark_episode_id): episode for episode in selected
        }
        raw_selected = [
            raw_by_output_id[benchmark_id]
            for benchmark_id in selected_by_benchmark_id
        ]
        ordered_benchmark_ids = balanced_round_robin_order(raw_selected)
        selected = [selected_by_benchmark_id[value] for value in ordered_benchmark_ids]
    else:
        ordered_benchmark_ids = [
            int(episode.benchmark_episode_id) for episode in selected
        ]
    run_manifest = build_run_manifest(
        args=args,
        run_cfg=run_cfg,
        collection_cfg=collection_cfg,
        eval_cfg=eval_cfg,
        raw_manifest=raw_manifest,
        manifest=manifest,
        scheduled_benchmark_ids=ordered_benchmark_ids,
    )
    if args.controller_config is not None:
        controller_payload = json.loads(args.controller_config.read_text())
        main_threshold_name = str(controller_payload["main_threshold_name"])
        main_threshold_val = float(controller_payload["main_threshold_value"])
        selected_cap_name = str(controller_payload["alternative_cap_name"])
        selected_cap_val = float(controller_payload["alternative_cap_value"])
        min_delta_val = float(controller_payload.get("min_delta", 0.0))
        controller_config_sha256 = sha256_file(args.controller_config)
    else:
        threshold_payload = json.loads((args.risk_model_root / "thresholds.json").read_text())
        if args.main_threshold not in threshold_payload or args.selected_cap not in threshold_payload:
            raise RuntimeError("online thresholds must be named entries from seen thresholds.json or provided via --controller-config")
        main_threshold_name = args.main_threshold
        main_threshold_val = float(threshold_payload[args.main_threshold])
        selected_cap_name = args.selected_cap
        selected_cap_val = float(threshold_payload[args.selected_cap])
        min_delta_val = 0.0
        controller_config_sha256 = None

    run_manifest["online_risk_intervention"] = {
        "protocol_id": args.protocol_id,
        "online_mode": args.online_mode,
        "online_role": args.online_role,
        "controller": "LIBERO-final-style TopK8 argmin_on_alarm + selected-risk cap",
        "selection_rule": "argmin_on_alarm",
        "selection_min_margin": min_delta_val,
        "main_threshold_name": main_threshold_name,
        "main_threshold": main_threshold_val,
        "selected_cap_name": selected_cap_name,
        "selected_score_cap": selected_cap_val,
        "controller_config_path": str(args.controller_config.resolve()) if args.controller_config else None,
        "controller_config_sha256": controller_config_sha256,
        "risk_model_root": str(args.risk_model_root.resolve()),
        "risk_model_sha256": sha256_file(args.risk_model_root / "model.pt"),
        "risk_normalization": str(args.risk_normalization.resolve()),
        "risk_normalization_sha256": sha256_file(args.risk_normalization),
        "thresholds_sha256": sha256_file(args.risk_model_root / "thresholds.json"),
        "detector_threshold_values_are_seen_derived": True,
        "ood_dev_used_for_controller_pair_selection": args.online_role == "dev",
        "ood_holdout_used_for_controller_pair_selection": False,
        "execution_horizon": 10,
        "candidate_count": 9,
        "ace_alternative_count": 8,
        "topk8_indices": list(TOPK8_INDICES),
    }
    store = EpisodeStore(args.output_dir, run_manifest)
    completed_ids = store.completed_episode_ids()
    round_id = int(args.round_id) if args.round_id is not None else None

    def output_episode_id(source_episode_id: int) -> str:
        if round_id is None:
            return f"{source_episode_id:06d}"
        return global_episode_id(round_id, source_episode_id)

    selected = [
        episode
        for episode in selected
        if output_episode_id(int(episode.source_episode_id)) not in completed_ids
    ]
    if not selected:
        store.update_status(
            {"state": "complete", "completed_episodes": len(completed_ids)}
        )
        return

    source_ids = [int(episode.source_episode_id) for episode in selected]
    round_provenance = {
        "round_id": round_id,
        "round_kind": str(args.round_kind) if args.round_kind is not None else None,
        "round_master_seed": (
            int(args.round_master_seed)
            if args.round_master_seed is not None
            else None
        ),
    }
    scene_assets_by_episode = load_manifest_scene_assets(
        base, collection_cfg, selected
    )
    asset_bank = base._build_asset_bank(scene_assets_by_episode)
    first_id = source_ids[0]
    first_assets = scene_assets_by_episode[first_id]
    first_names = base._episode_asset_names(asset_bank, first_assets)
    base_spec, sampling_options = base.make_sampling_options(collection_cfg)
    first_plan = base._make_episode_plan(
        collection_cfg,
        base_spec,
        first_assets,
        seed,
        first_id,
        sampling_options,
        first_names,
    )
    base.validate_reaching_plan(collection_cfg, first_assets, first_plan)
    first_entry = selected[0]
    base.require_scene_matches_manifest(first_entry, first_assets, first_plan)

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
        print(
            f"FRANKA_ASSET_RELOCATION_FIX={ISAAC_6_LEGACY_FRANKA_USD}",
            flush=True,
        )
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

    runtime = base.SimVLARuntime(base.build_runtime_config(eval_cfg, args.device))
    runtime.load()
    norm_payload = json.loads(Path(runtime.config.norm_stats_path).read_text())
    state_mean = np.asarray(
        norm_payload["norm_stats"]["state"]["mean"], dtype=np.float32
    )
    state_std = np.asarray(
        norm_payload["norm_stats"]["state"]["std"], dtype=np.float32
    )
    if args.controller_config is not None:
        selector = OnlineRiskSelector(
            controller_config_path=args.controller_config,
            model_path=args.risk_model_root / "model.pt",
            normalization_path=args.risk_normalization,
            device=args.device,
        )
    else:
        # Fallback to creating a temp controller config or loading by threshold names
        temp_controller_cfg = Path("/tmp/temp_controller_config.json")
        temp_controller_cfg.write_text(json.dumps({
            "schema_version": "isaac_online_engineering_controller_v1",
            "main_threshold_name": args.main_threshold,
            "main_threshold_value": main_threshold_val,
            "alternative_cap_name": args.selected_cap,
            "alternative_cap_value": selected_cap_val,
            "min_delta": 0.0,
            "model_sha256": sha256_file(args.risk_model_root / "model.pt"),
            "normalization_sha256": sha256_file(args.risk_normalization),
        }, indent=2))
        selector = OnlineRiskSelector(
            controller_config_path=temp_controller_cfg,
            model_path=args.risk_model_root / "model.pt",
            normalization_path=args.risk_normalization,
            device=args.device,
        )
    if selector.model_sha256 != run_manifest["online_risk_intervention"]["risk_model_sha256"]:
        raise RuntimeError("risk model changed between manifest creation and load")

    sim = base.sim_utils.SimulationContext(
        base.make_simulation_cfg(
            args.device, use_fabric=bool(collection_cfg.get("use_fabric", True))
        )
    )
    scene = base.InteractiveScene(scene_cfg)
    pose_contract = base.parse_reaching_pose_contract(
        collection_cfg["pose_controller"]
    )
    ready_ik, ik = base.create_shared_reaching_ik_controllers(pose_contract)
    gripper = base.GripperController()
    sim.reset()
    sim.set_camera_view(eye=[2.2, -2.2, 1.9], target=[0.55, 0.0, 1.20])
    robot = scene["robot"]
    ready_ik.bind(scene, robot)
    ik.bind(scene, robot)
    gripper.bind(scene, robot)

    plans = {first_id: first_plan}
    for index, episode in enumerate(selected):
        source_id = int(episode.source_episode_id)
        episode_global_id = output_episode_id(source_id)
        if store.stop_after_current_episode_requested():
            store.update_status(
                {
                    "state": "paused_before_episode",
                    "next_source_episode_id": source_id,
                    "next_global_episode_id": episode_global_id,
                    "round_id": round_id,
                    "completed_episodes": len(store.completed_episode_ids()),
                    "execution_mode": args.execution_mode,
                }
            )
            print(
                f"STOP_AFTER_CURRENT_EPISODE honored before source_episode_id={source_id}",
                flush=True,
            )
            return
        assets = scene_assets_by_episode[source_id]
        names = base._episode_asset_names(asset_bank, assets)
        plan = plans.get(source_id)
        if plan is None:
            plan = base._make_episode_plan(
                collection_cfg,
                base_spec,
                assets,
                seed,
                source_id,
                sampling_options,
                names,
            )
            base.validate_reaching_plan(collection_cfg, assets, plan)
        base.require_scene_matches_manifest(episode, assets, plan)
        raw_entry = raw_by_output_id[int(episode.benchmark_episode_id)]
        collection_manifest_partition = str(
            raw_entry.get("risk_split", "unassigned")
        )
        scientific_risk_split = (
            "synthetic_smoke"
            if args.force_timeout_smoke
            else "ood_final_test"
            if collection_manifest_partition == "ood_smoke"
            else "unassigned_seen"
        )
        store.update_status(
            {
                "state": "running",
                "current_source_episode_id": source_id,
                "current_global_episode_id": episode_global_id,
                "round_id": round_id,
                "remaining_in_shard": len(selected) - index,
                "completed_episodes": len(store.completed_episode_ids()),
                "execution_mode": args.execution_mode,
            }
        )
        retries_after_first = int(
            collection_cfg.get("infrastructure_retry_count", 2)
        )
        if retries_after_first < 0 or retries_after_first > 10:
            raise ValueError("infrastructure_retry_count must be between 0 and 10")
        episode_result: tuple[bool, int] | None = None
        first_persistent_attempt = store.next_error_attempt(source_id)
        for local_attempt in range(1, retries_after_first + 2):
            persistent_attempt = first_persistent_attempt + local_attempt - 1
            try:
                episode_result = run_episode(
                    base=base,
                    sim=sim,
                    scene=scene,
                    robot=robot,
                    ready_ik=ready_ik,
                    ik=ik,
                    gripper=gripper,
                    runtime=runtime,
                    collection_cfg=collection_cfg,
                    episode=episode,
                    episode_plan=plan,
                    scene_assets=assets,
                    asset_bank=asset_bank,
                    simulation_app=simulation_app,
                    state_mean=state_mean,
                    state_std=state_std,
                    execution_mode=args.execution_mode,
                    run_store=store,
                    manifest_fingerprint=manifest.manifest_fingerprint_sha256,
                    scientific_risk_split=scientific_risk_split,
                    collection_manifest_partition=collection_manifest_partition,
                    global_id=episode_global_id,
                    round_provenance=round_provenance,
                    raw_manifest_entry=raw_entry,
                    force_timeout_smoke=bool(args.force_timeout_smoke),
                    save_video=args.save_video,
                    inference_only=args.inference_only,
                    selector=selector,
                    online_mode=args.online_mode,
                )
                break
            except Exception as error:
                error_traceback = traceback.format_exc()
                store.discard_uncommitted_episode(episode_global_id)
                error_path = store.record_episode_error(
                    {
                        "schema_version": (
                            "simvla_isaac_risk_infrastructure_error_v1"
                        ),
                        "source_episode_id": source_id,
                        "global_episode_id": episode_global_id,
                        "round_id": round_id,
                        "round_kind": round_provenance["round_kind"],
                        "round_master_seed": round_provenance[
                            "round_master_seed"
                        ],
                        "attempt": persistent_attempt,
                        "attempt_in_this_process": local_attempt,
                        "max_attempts_in_this_process": retries_after_first + 1,
                        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                        "exception_type": type(error).__name__,
                        "exception_message": str(error),
                        "traceback": error_traceback,
                        "scene_fingerprint_sha256": raw_entry[
                            "scene_fingerprint_sha256"
                        ],
                        "manifest_fingerprint_sha256": (
                            manifest.manifest_fingerprint_sha256
                        ),
                        "run_config_sha256": run_manifest["run_config_sha256"],
                        "collector_source_sha256": run_manifest[
                            "collector_source_sha256"
                        ],
                        "contract_fingerprint_sha256": (
                            runtime.config.contract_fingerprint_sha256
                        ),
                    }
                )
                print(
                    "INFRASTRUCTURE_EPISODE_ERROR "
                    f"source_episode_id={source_id} "
                    f"attempt={local_attempt}/{retries_after_first + 1} "
                    f"record={error_path}",
                    flush=True,
                )
                if local_attempt <= retries_after_first:
                    print(
                        f"RETRYING_SOURCE_EPISODE source_episode_id={source_id}",
                        flush=True,
                    )
        if episode_result is None:
            store.update_status(
                {
                    "state": "infrastructure_error_skipped",
                    "source_episode_id": source_id,
                    "global_episode_id": episode_global_id,
                    "round_id": round_id,
                    "completed_episodes": len(store.completed_episode_ids()),
                    "execution_mode": args.execution_mode,
                    "training_rows_written": False,
                    "risk_label_written": False,
                }
            )
            print(
                "SOURCE_EPISODE_EXCLUDED_INFRASTRUCTURE_ERROR "
                f"source_episode_id={source_id}",
                flush=True,
            )
            if store.stop_after_current_episode_requested():
                return
            continue
        success, rows = episode_result
        print(
            f"RISK_EPISODE_FINALIZED source_episode_id={source_id} "
            f"global_episode_id={episode_global_id} "
            f"success={success} decision_rows={rows}",
            flush=True,
        )
        if args.inference_only:
            return
        if store.stop_after_current_episode_requested():
            store.update_status(
                {
                    "state": "paused_after_current_episode",
                    "last_completed_source_episode_id": source_id,
                    "last_completed_global_episode_id": episode_global_id,
                    "round_id": round_id,
                    "completed_episodes": len(store.completed_episode_ids()),
                    "execution_mode": args.execution_mode,
                }
            )
            print(
                f"STOP_AFTER_CURRENT_EPISODE honored after source_episode_id={source_id}",
                flush=True,
            )
            return
    store.update_status(
        {
            "state": "complete",
            "round_id": round_id,
            "completed_episodes": len(store.completed_episode_ids()),
            "execution_mode": args.execution_mode,
        }
    )


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
