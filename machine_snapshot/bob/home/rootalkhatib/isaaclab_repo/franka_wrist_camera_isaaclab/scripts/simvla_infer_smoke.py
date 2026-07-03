#!/usr/bin/env python3
"""Launch IsaacLab and run one in-process SimVLA action generation smoke check."""

from __future__ import annotations

import argparse
import importlib
from pathlib import Path
import sys

import numpy as np
import torch

REPO_SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(REPO_SRC))

from franka_wrist_camera_scene.app import launcher  # noqa: F401
from isaaclab.app import AppLauncher  # noqa: E402

from franka_wrist_camera_scene.simvla.geometry import SimVLAProprioSource, encode_simvla_proprio  # noqa: E402
from franka_wrist_camera_scene.simvla.image_preprocessing import preprocess_camera_views  # noqa: E402
from franka_wrist_camera_scene.simvla.runtime import SimVLARuntime, SimVLARuntimeConfig  # noqa: E402
from franka_wrist_camera_scene.utils.paths import load_yaml_config  # noqa: E402

FABRIC_RENDER_TRANSFORM_SETTING = "/rtx/hydra/readTransformsFromFabricInRenderDelegate"


def _append_kit_arg(existing: str, *tokens: str) -> str:
    parts = existing.split() if existing else []
    parts.extend(tokens)
    return " ".join(parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one SimVLA inference smoke check under IsaacLab.")
    parser.add_argument(
        "--eval_config",
        type=Path,
        default=Path("configs/eval_simvla_isaaclab_rotate180.yaml"),
        help="SimVLA eval config.",
    )
    parser.add_argument(
        "--prompt",
        default="reach the avocado",
        help="Language prompt for the smoke inference.",
    )
    parser.add_argument(
        "--allow_fabric_render_transforms",
        action="store_true",
        help="Allow RTX Hydra to read transforms directly from Fabric.",
    )
    parser.add_argument(
        "--skip_model_inference",
        action="store_true",
        help="Validate paths/config and launch IsaacLab, but do not load the checkpoint.",
    )
    AppLauncher.add_app_launcher_args(parser)
    args = parser.parse_args()
    args.enable_cameras = True
    if not args.allow_fabric_render_transforms:
        args.kit_args = _append_kit_arg(args.kit_args, f"--{FABRIC_RENDER_TRANSFORM_SETTING}=false")
    return args


def runtime_config(eval_cfg: dict, device: str) -> SimVLARuntimeConfig:
    cfg = eval_cfg["simvla"]
    return SimVLARuntimeConfig(
        simvla_repo_path=Path(cfg["repo_path"]),
        checkpoint_path=Path(cfg["checkpoint_path"]),
        smolvlm_model_path=Path(cfg["smolvlm_model_path"]),
        norm_stats_path=Path(cfg["norm_stats_path"]),
        device=device,
        action_mode=str(cfg.get("action_mode", "libero_joint")),
        num_actions=int(cfg.get("num_actions", 10)),
        inference_steps=int(cfg.get("inference_steps", 10)),
        predict_uncertainty=bool(cfg.get("predict_uncertainty", True)),
        num_action_samples=int(cfg.get("num_action_samples", 1)),
    )


def run_smoke_inference(eval_cfg: dict, prompt: str, device: str) -> None:
    simvla_cfg = eval_cfg["simvla"]
    runtime = SimVLARuntime(runtime_config(eval_cfg, device))
    print(f"[INFO] SimVLA checkpoint: {runtime.config.checkpoint_path}", flush=True)
    print(f"[INFO] SimVLA repo: {runtime.config.simvla_repo_path}", flush=True)
    print(f"[INFO] image_rotation={simvla_cfg['image_rotation']} device={device}", flush=True)
    runtime._require_paths()
    runtime._validate_checkpoint_config()
    if not prompt.strip():
        raise ValueError("Smoke prompt must be non-empty.")

    if bool(eval_cfg.get("skip_model_inference", False)):
        print("[INFO] Runtime path/config validation passed; model inference skipped.", flush=True)
        return

    print("[INFO] Loading SimVLA runtime...", flush=True)
    runtime.load()
    print("[INFO] SimVLA runtime loaded; running one action generation.", flush=True)
    raw_agent = np.zeros((480, 640, 3), dtype=np.uint8)
    raw_wrist = np.zeros((480, 640, 3), dtype=np.uint8)
    images = preprocess_camera_views(raw_agent, raw_wrist, str(simvla_cfg["image_rotation"]), device=runtime.device)
    proprio = encode_simvla_proprio(
        SimVLAProprioSource(
            ee_pos_w=np.array([0.5, 0.0, 1.1], dtype=np.float32),
            ee_quat_wxyz=np.array([1.0, 0.0, 0.0, 0.0], dtype=np.float32),
            env_origin_w=np.zeros(3, dtype=np.float32),
            commanded_finger_opening_m=0.04,
        )
    )
    output = runtime.infer(prompt, images.image_input, images.image_mask, proprio)
    print("[INFO] SimVLA inference smoke passed.", flush=True)
    print(f"[INFO] action_shape={output.actions.shape}", flush=True)
    print(f"[INFO] first_action={output.actions[0].tolist()}", flush=True)
    if output.uncertainty:
        print(f"[INFO] uncertainty_keys={sorted(output.uncertainty)}", flush=True)


def main() -> None:
    args = parse_args()
    preflight_python_dependencies()
    print(f"[INFO] Loading eval config: {args.eval_config}", flush=True)
    eval_cfg = load_yaml_config(args.eval_config)
    if args.skip_model_inference:
        eval_cfg = dict(eval_cfg)
        eval_cfg["skip_model_inference"] = True

    app_launcher = AppLauncher(args)
    simulation_app = app_launcher.app
    launcher.patch_physx_schema()
    try:
        device = args.device
        if device == "cuda" and not torch.cuda.is_available():
            raise RuntimeError("Requested CUDA device but torch.cuda.is_available() is false.")
        run_smoke_inference(eval_cfg, args.prompt, device)
    finally:
        simulation_app.close()


def preflight_python_dependencies() -> None:
    missing = []
    for module_name in ("transformers", "safetensors", "json_numpy"):
        try:
            importlib.import_module(module_name)
        except ImportError:
            missing.append(module_name)
    if missing:
        package_hint = ", ".join(missing)
        raise ModuleNotFoundError(f"Missing SimVLA inference dependencies: {package_hint}")


if __name__ == "__main__":
    main()
