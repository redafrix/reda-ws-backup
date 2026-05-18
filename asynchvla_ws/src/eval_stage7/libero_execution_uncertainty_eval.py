#!/usr/bin/env python3
"""Stage 7 — in-process LIBERO execution + uncertainty rollout.

Modes:
  A passive       — execute SimVLA seed0, log rater uncertainty + reward + success
  B deliberation  — at each replan, score N seeds with rater, execute lowest-pred
  C switch_proxy  — execute seed0 normally, log per-step accepted/rejected under
                    a learned threshold and compare per-step error vs progress

Tiny by default: 1 task suite, 1 task, 3 episodes per mode. Set `--num-episodes`
larger only after a clean run.

Requires (Bob):
  export LIBERO_CONFIG_PATH=/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_bob
  export MUJOCO_GL=egl
  export PYOPENGL_PLATFORM=egl
  source asynchvla_ws/scripts/activate_simvla_bob.sh
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import traceback
from pathlib import Path
from typing import List, Dict, Any

import numpy as np
import torch

REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
SIM = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
CKPT_DEFAULT = REDA_WS / "intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000"
BACK_DEFAULT = REDA_WS / "intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct"

sys.path.insert(0, str(REDA_WS / "asynchvla_ws/src"))
sys.path.insert(0, str(SIM))

from features_stage6.build_features import (  # noqa: E402
    feature_vector,
    build_seed_stats,
)
from rater_stage6.models import (  # noqa: E402
    MLPRegressor,
    ContextGatedActionFixed,
)
from simvla_trace.trace import generate_actions_trace  # noqa: E402
from models.modeling_smolvlm_vla import SmolVLMVLA  # noqa: E402
from models.processing_smolvlm_vla import SmolVLMVLAProcessor  # noqa: E402
from models.configuration_smolvlm_vla import SmolVLMVLAConfig  # noqa: E402

# LIBERO comes in last so the import-side warnings about config paths don't
# pollute earlier output.
from libero.libero import benchmark, get_libero_path  # noqa: E402
from libero.libero.envs import OffScreenRenderEnv  # noqa: E402
from torchvision import transforms  # noqa: E402
from PIL import Image  # noqa: E402


def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
    if quat[3] > 1.0:
        quat[3] = 1.0
    elif quat[3] < -1.0:
        quat[3] = -1.0
    den = np.sqrt(1.0 - quat[3] * quat[3])
    if math.isclose(den, 0.0):
        return np.zeros(3)
    return (quat[:3] * 2.0 * math.acos(quat[3])) / den


def load_simvla(ckpt: Path, smolvlm: Path, device: torch.device, norm_stats_path: Path = None):
    cfg = SmolVLMVLAConfig.from_pretrained(str(ckpt))
    cfg.smolvlm_model_path = str(smolvlm)
    model = SmolVLMVLA.from_pretrained(str(ckpt), config=cfg)
    model = model.to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained(str(smolvlm))
    candidates = []
    if norm_stats_path is not None:
        candidates.append(Path(norm_stats_path))
    candidates += [
        ckpt / "norm_stats.json",
        Path(SIM) / "norm_stats/libero_norm.json",
    ]
    for cand in candidates:
        if cand and cand.exists() and hasattr(model, "action_space"):
            try:
                model.action_space.load_norm_stats(str(cand))
                print(f"[setup] loaded norm_stats from {cand}", flush=True)
                break
            except Exception as exc:
                print(f"[setup] norm_stats load failed for {cand}: {exc}", flush=True)
    else:
        print("[setup] WARNING no norm_stats loaded", flush=True)
    return model, processor


def load_rater(ckpt_path: Path, device: torch.device):
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    kind = ckpt["kind"]
    in_dim = int(ckpt["input_dim"])
    if kind == "gated":
        # context_gated_action: context_dim hard-coded to 968 in run_stage6_experiments.py
        context_dim = 968
        model = ContextGatedActionFixed(context_dim, in_dim - context_dim, hidden=384)
    elif kind == "mlp":
        model = MLPRegressor(in_dim, hidden=256, depth=2)
    elif kind in ("mlp_big", "mlp_big_pairwise"):
        model = MLPRegressor(in_dim, hidden=384, depth=3)
    else:
        raise NotImplementedError(f"kind={kind} not supported for rollout")
    model.load_state_dict(ckpt["state_dict"])
    model.to(device).eval()
    mu = ckpt["input_mean"].to(device)
    sd = ckpt["input_std"].to(device)
    return {
        "model": model,
        "feature_mode": ckpt["feature_mode"],
        "kind": kind,
        "mu": mu,
        "sd": sd,
        "input_dim": in_dim,
    }


def preprocess_images(image0: np.ndarray, image1: np.ndarray, image_size: int = 384):
    transform = transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])
    img0_t = transform(Image.fromarray(image0.astype(np.uint8)))
    img1_t = transform(Image.fromarray(image1.astype(np.uint8)))
    padding = torch.zeros_like(img0_t)
    images = torch.stack([img0_t, img1_t, padding], dim=0)
    image_mask = torch.tensor([[True, True, False]])
    return images.unsqueeze(0), image_mask


def libero_obs_to_state(obs: dict) -> np.ndarray:
    """LIBERO obs → SimVLA state (8D), matching libero_client.py concat order."""
    ee_pos = obs.get("robot0_eef_pos", np.zeros(3))
    ee_quat = obs.get("robot0_eef_quat", np.array([0.0, 0.0, 0.0, 1.0]))
    grip_qpos = obs.get("robot0_gripper_qpos", np.zeros(2))
    axang = _quat2axisangle(ee_quat.copy())
    state = np.concatenate([ee_pos, axang, grip_qpos])[:8]
    if state.size < 8:
        state = np.pad(state, (0, 8 - state.size))
    return state.astype(np.float32)


def get_libero_images(obs: dict, resolution: int = 256):
    img = obs.get("agentview_image", None)
    wrist = obs.get("robot0_eye_in_hand_image", None)
    if img is None or wrist is None:
        # fallback to zeros
        img = np.zeros((resolution, resolution, 3), dtype=np.uint8)
        wrist = np.zeros((resolution, resolution, 3), dtype=np.uint8)
    # Match the original libero_client.py convention: LIBERO renders images
    # flipped on both axes from the model's training convention.
    img = np.ascontiguousarray(img[::-1, ::-1])
    wrist = np.ascontiguousarray(wrist[::-1, ::-1])
    return img, wrist


def run_simvla_seed(model, processor, prompt: str, image0: np.ndarray, image1: np.ndarray,
                    state: np.ndarray, seed: int, device: torch.device, steps: int = 10):
    images, image_mask = preprocess_images(image0, image1)
    images = images.to(device)
    image_mask = image_mask.to(device)
    lang = processor.encode_language([prompt])
    lang = {k: v.to(device) for k, v in lang.items()}
    proprio = torch.tensor(state, dtype=torch.float32, device=device).unsqueeze(0)
    out = generate_actions_trace(
        model,
        input_ids=lang["input_ids"],
        image_input=images,
        image_mask=image_mask,
        proprio=proprio,
        steps=steps,
        seed=seed,
        return_initial_noise=False,
        return_flow_trace=False,
    )
    normalized = out["generated_normalized_action"][0].detach().cpu()  # [T,D]
    postproc = out["generated_postprocessed_action"][0].detach().cpu().numpy()  # [T,D]
    pooled_vlm = out.get("pooled_vlm_features")
    if pooled_vlm is None:
        # fall back: pool vlm_features
        pooled_vlm = out.get("vlm_features").mean(dim=1)[0].detach().cpu()
    else:
        pooled_vlm = pooled_vlm[0].detach().cpu()
    return {
        "normalized_action": normalized,
        "postprocessed_action": postproc,
        "pooled_vlm": pooled_vlm,
        "proprio": torch.tensor(state, dtype=torch.float32),
    }


def score_candidates(rater: dict, seed_outputs: List[dict], context_id: str) -> List[float]:
    """Build features for each seed candidate, run rater, return predicted error per seed."""
    # Pseudo rows
    rows = []
    for i, out in enumerate(seed_outputs):
        rows.append({
            "context_id": context_id,
            "candidate_type": f"simvla_seed{i}",
            "candidate_action_normalized": out["normalized_action"],
            "pooled_vlm_features": out["pooled_vlm"],
            "proprio": out["proprio"],
        })
    seed_stats = build_seed_stats(rows)
    mode = rater["feature_mode"]
    xs = [feature_vector(r, mode, seed_stats) for r in rows]
    x = torch.stack(xs).to(rater["mu"].device)
    xn = (x - rater["mu"]) / rater["sd"]
    with torch.no_grad():
        pred = rater["model"](xn)
        if pred.ndim > 1:
            pred = pred.squeeze(-1)
        scores = pred.detach().cpu().numpy().tolist()
    return scores


def run_episode(env, processor, simvla_model, rater, *, prompt: str, max_steps: int,
                replan_steps: int, num_seeds: int, mode: str, device: torch.device,
                ep_idx: int, seed: int, init_state=None):
    log: List[Dict[str, Any]] = []
    env.reset()
    if init_state is not None:
        obs = env.set_init_state(init_state)
    else:
        obs = env.reset()
    # warm-up: a few zero actions to let env settle (matches libero_client)
    for _ in range(10):
        obs, _, done, info = env.step(np.array([0, 0, 0, 0, 0, 0, -1], dtype=np.float32))
    success = False
    chosen_chunk = None
    chunk_idx = 0
    chunk_scores = []
    t0 = time.time()
    for step in range(max_steps):
        if chosen_chunk is None or chunk_idx >= replan_steps:
            # replan
            img, wrist = get_libero_images(obs)
            state = libero_obs_to_state(obs)
            seed_outs = []
            for s in range(num_seeds):
                so = run_simvla_seed(simvla_model, processor, prompt, img, wrist, state,
                                     seed=s, device=device)
                seed_outs.append(so)
            scores = score_candidates(rater, seed_outs, context_id=f"ep{ep_idx}_step{step}")
            seed0_unc = float(scores[0])
            threshold = float(getattr(run_episode, "unc_threshold", 1.75))
            reject_seed0 = bool(seed0_unc > threshold)
            if mode in ("A_passive", "D_low_uncertainty_reject_log", "C_switch"):
                chosen_seed = 0
            elif mode == "B_deliberation":
                chosen_seed = int(np.argmin(scores))
            elif mode == "C_random_seed":
                chosen_seed = int(np.random.default_rng(seed + step).integers(0, num_seeds))
            elif mode == "E_conservative_switch_proxy":
                chosen_seed = int(np.argmin(scores)) if reject_seed0 else 0
            else:
                raise ValueError(f"unknown mode {mode}")
            chosen_chunk = seed_outs[chosen_seed]["postprocessed_action"]
            chunk_scores = scores
            chunk_idx = 0
            log.append({
                "step": step,
                "kind": "replan",
                "scores": [float(s) for s in scores],
                "chosen_seed": int(chosen_seed),
                "seed0_uncertainty": float(scores[0]),
                "uncertainty_threshold": float(threshold),
                "seed0_rejected_by_threshold": bool(reject_seed0),
                "mode": mode,
            })
        action = chosen_chunk[chunk_idx].astype(np.float32)
        obs, reward, done, info = env.step(action)
        
        # Action stats for debug
        a_min, a_max = float(np.min(action)), float(np.max(action))
        a_mean = float(np.mean(action))
        a_norm = float(np.linalg.norm(action))
        gripper = float(action[6])
        
        log.append({
            "step": step,
            "kind": "exec",
            "chunk_idx": int(chunk_idx),
            "action_stats": {
                "min": a_min, "max": a_max, "mean": a_mean, "l2": a_norm, "gripper": gripper,
                "val": action.tolist()[:7]
            },
            "chosen_seed_unc": float(chunk_scores[0]) if chunk_scores else None,
            "reward": float(reward),
            "done": bool(done),
        })
        chunk_idx += 1
        if done:
            success = bool(reward > 0.0 or done)
            break
    walltime = time.time() - t0
    return {
        "ep_idx": ep_idx,
        "mode": mode,
        "seed": seed,
        "success": bool(success),
        "steps": int(step + 1),
        "walltime_sec": round(walltime, 2),
        "trace": log,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simvla-ckpt", default=str(CKPT_DEFAULT))
    ap.add_argument("--smolvlm", default=str(BACK_DEFAULT))
    ap.add_argument("--norm-stats", default=str(SIM / "norm_stats/libero_norm.json"))
    ap.add_argument("--rater-ckpt", default=str(REDA_WS / "asynchvla_ws/outputs/checkpoints/stage6/holdout_libero_object/context_gated_action/model.pt"))
    ap.add_argument("--task-suite", default="libero_spatial")
    ap.add_argument("--task-id", type=int, default=0)
    ap.add_argument("--num-episodes", type=int, default=3)
    ap.add_argument("--max-steps", type=int, default=200)
    ap.add_argument("--replan-steps", type=int, default=5)
    ap.add_argument("--num-seeds", type=int, default=5)
    ap.add_argument("--modes", nargs="+", default=["A_passive", "B_deliberation"])
    ap.add_argument("--unc-threshold", type=float, default=1.75)
    ap.add_argument("--resolution", type=int, default=256)
    ap.add_argument("--out", type=str, default=None)
    args = ap.parse_args()

    os.environ.setdefault("LIBERO_CONFIG_PATH",
                          str(REDA_WS / "asynchvla_ws/configs/libero_bob"))
    os.environ.setdefault("MUJOCO_GL", "egl")
    os.environ.setdefault("PYOPENGL_PLATFORM", "egl")

    run_episode.unc_threshold = float(args.unc_threshold)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[setup] device={device}", flush=True)

    print("[setup] loading SimVLA", flush=True)
    simvla_model, processor = load_simvla(Path(args.simvla_ckpt), Path(args.smolvlm), device,
                                          norm_stats_path=Path(args.norm_stats))
    print("[setup] loading rater", flush=True)
    rater = load_rater(Path(args.rater_ckpt), device)
    print(f"[setup] rater feature_mode={rater['feature_mode']} kind={rater['kind']} in_dim={rater['input_dim']}", flush=True)

    bd = benchmark.get_benchmark_dict()
    if args.task_suite not in bd:
        raise SystemExit(f"unknown suite {args.task_suite}, available={list(bd.keys())}")
    b = bd[args.task_suite]()
    task = b.get_task(args.task_id)
    initial_states = b.get_task_init_states(args.task_id)
    print(f"[task] {task.language!r}, {len(initial_states)} init states",
          flush=True)
    bddl_path = Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
    env_args = {"bddl_file_name": str(bddl_path),
                "camera_heights": args.resolution, "camera_widths": args.resolution}

    results = {
        "task_suite": args.task_suite,
        "task_id": args.task_id,
        "task_language": task.language,
        "episodes": [],
    }
    for mode in args.modes:
        print(f"[mode] {mode}", flush=True)
        for ep in range(args.num_episodes):
            env = OffScreenRenderEnv(**env_args)
            env.seed(int(7 + ep))
            init_state = initial_states[ep % len(initial_states)]
            try:
                res = run_episode(env, processor, simvla_model, rater,
                                  prompt=task.language,
                                  max_steps=args.max_steps,
                                  replan_steps=args.replan_steps,
                                  num_seeds=args.num_seeds,
                                  mode=mode,
                                  device=device,
                                  ep_idx=ep,
                                  seed=int(7 + ep),
                                  init_state=init_state)
            except Exception:
                traceback.print_exc()
                res = {"ep_idx": ep, "mode": mode, "success": False, "error": traceback.format_exc()}
            finally:
                try:
                    env.close()
                except Exception:
                    pass
            print(f"  ep{ep} mode={mode} success={res.get('success')} steps={res.get('steps')}", flush=True)
            results["episodes"].append(res)

    out_path = args.out or str(
        REDA_WS / "asynchvla_ws/outputs/reports/stage7"
        / f"stage7_libero_execution_tiny_{args.task_suite}_t{args.task_id}.json"
    )
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(json.dumps(results, indent=2))
    print(f"[done] wrote {out_path}")


if __name__ == "__main__":
    main()
