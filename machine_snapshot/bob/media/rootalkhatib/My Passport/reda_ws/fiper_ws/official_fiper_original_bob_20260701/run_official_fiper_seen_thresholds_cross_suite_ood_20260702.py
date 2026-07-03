#!/usr/bin/env python3
"""Evaluate official FIPER seen-calibrated thresholds on cross-suite OOD sets.

Protocol:
- Use the already materialized official FIPER seen goal-object dataset for
  calibration rollouts only.
- Materialize each OOD JSONL dataset into official FIPER tensors.
- Build a combined dataset per OOD set: seen calibration successes + OOD test.
- Reuse the official RND checkpoints trained on seen calibration, one per seed.
- Run the official EvaluationManager/method classes unchanged, then report only
  the operating points selected on the seen held-out run.
"""

from __future__ import annotations

import copy
import csv
import gc
import json
import os
import pickle
import shutil
import sys
import argparse
from pathlib import Path
from typing import Iterable

import numpy as np
import torch
from PIL import Image

if not hasattr(np, "bool"):
    np.bool = np.bool_  # type: ignore[attr-defined]


ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701")
FIPER_REPO = ROOT / "repos" / "fiper"
SEEN_TASK = "libero_goal_object_official"
SEEN_PROCESSED = ROOT / "official_fiper_data" / SEEN_TASK / "processed_rollouts"
SEEN_RND = ROOT / "official_fiper_data" / SEEN_TASK / "rnd_models" / "rnd_oe"
CROSS_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630")
DATASETS_ROOT = CROSS_ROOT / "datasets"
RUN_ROOT = ROOT / "official_fiper_seen_thresholds_cross_suite_ood_20260702"
OOD_MATERIALIZED_ROOT = RUN_ROOT / "ood_materialized"
COMBINED_ROOT = RUN_ROOT / "official_fiper_data"
REPORT = RUN_ROOT / "OFFICIAL_FIPER_SEEN_THRESHOLDS_CROSS_SUITE_OOD_20260702.md"

REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
SIMVLA_ROOT = REDA_WS / "intern_ship_ws" / "simvla" / "code" / "SimVLA_modified"
LIBERO_ROOT = REDA_WS / "intern_ship_ws" / "assets" / "repos" / "LIBERO-PRO"
STAGE9_ROOT = REDA_WS / "fiper_ws" / "collection" / "data_collection_stage9"
STAGE9_TOOLS = REDA_WS / "fiper_ws" / "stage9_v2_tools"
CHECKPOINT = REDA_WS / "fiper_ws" / "checkpoints" / "simvla_libero_uncertainty" / "ckpt-60000"
SMOLVLM_PATH = "HuggingFaceTB/SmolVLM-500M-Instruct"

DATASET_NAMES = [
    "goal_object_ood_180",
    "goal_swap_100",
    "goal_task_100",
    "spatial_object_100",
    "object_object_100",
    "libero10_object_100",
]

SEEDS = [0, 1, 2, 42, 43]
METHODS = ["entropy", "rnd_oe"]
COMBINED = {
    1: {
        "m1": {"name": "rnd_oe", "window_sizes": None, "quantiles": None},
        "m2": {"name": "entropy", "window_sizes": None, "quantiles": None},
        "operation": "and",
    }
}

SELECTED_OPERATING_POINTS = [
    ("entropy", "ct_quantile", "15", "seen-best entropy ct_quantile"),
    ("entropy", "tvt_quantile", "50", "seen-best entropy tvt_quantile"),
    ("entropy", "tvt_cp_band", "50", "seen-best entropy tvt_cp_band"),
    ("rnd_oe", "ct_quantile", "3", "seen-best rnd_oe ct_quantile"),
    ("rnd_oe", "tvt_quantile", "1", "seen-best rnd_oe tvt_quantile"),
    ("rnd_oe", "tvt_cp_band", "11", "seen-best rnd_oe tvt_cp_band"),
    ("rnd_oe_and_entropy", "ct_quantile", "1", "seen-best fusion ct_quantile"),
    ("rnd_oe_and_entropy", "tvt_quantile", "1/50", "seen-best fusion tvt_quantile"),
    ("rnd_oe_and_entropy", "tvt_cp_band", "11/50", "seen-best fusion tvt_cp_band"),
]


def setup_imports():
    for p in [SIMVLA_ROOT, LIBERO_ROOT, STAGE9_ROOT, STAGE9_TOOLS]:
        sys.path.insert(0, str(p))
    sys.path.insert(0, str(FIPER_REPO))

    os.environ.setdefault("MUJOCO_GL", "egl")
    os.environ.setdefault("PYOPENGL_PLATFORM", "egl")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    torch.set_float32_matmul_precision("high")


def import_simvla_stack():
    setup_imports()

    orig_load = torch.load

    def torch_load_compat(*args, **kwargs):
        kwargs.setdefault("weights_only", False)
        return orig_load(*args, **kwargs)

    torch.load = torch_load_compat

    from libero.libero.envs import OffScreenRenderEnv
    from models.modeling_smolvlm_vla import SmolVLMVLA
    from models.processing_smolvlm_vla import SmolVLMVLAProcessor
    from sim_state_utils import set_state
    from libero_pro_env_utils import obs_images

    return OffScreenRenderEnv, SmolVLMVLA, SmolVLMVLAProcessor, set_state, obs_images


def import_official_fiper():
    setup_imports()
    os.chdir(FIPER_REPO)
    import evaluation.utils as eval_utils
    from datasets.rollout_datasets import ProcessedRolloutDataset
    from evaluation import EvaluationManager
    from shared_utils.hydra_utils import load_config
    from shared_utils.utility_functions import get_required_tensors, set_seed

    def robust_confusion_matrix(failures_detected, successful_rollouts):
        failures_detected = np.asarray(failures_detected, dtype=bool)
        successful_rollouts = np.asarray(successful_rollouts, dtype=bool)
        if failures_detected.shape != successful_rollouts.shape:
            raise ValueError("Length and shape of failures_detected and successful_rollouts must be the same.")
        fp = np.sum(failures_detected & successful_rollouts)
        tn = np.sum(~failures_detected & successful_rollouts)
        tp = np.sum(failures_detected & ~successful_rollouts)
        fn = np.sum(~failures_detected & ~successful_rollouts)
        return tp, tn, fp, fn

    eval_utils._calculate_confusion_matrix = robust_confusion_matrix
    return ProcessedRolloutDataset, EvaluationManager, load_config, get_required_tensors, set_seed


class ImagePreprocessor:
    def __init__(self, image_size: int = 384):
        self.image_size = int(image_size)
        self.mean = torch.tensor([0.485, 0.456, 0.406], dtype=torch.float32).view(3, 1, 1)
        self.std = torch.tensor([0.229, 0.224, 0.225], dtype=torch.float32).view(3, 1, 1)

    def _to_tensor(self, image: np.ndarray) -> torch.Tensor:
        pil = Image.fromarray(image.astype(np.uint8)).resize((self.image_size, self.image_size), Image.BILINEAR)
        arr = np.asarray(pil, dtype=np.float32) / 255.0
        if arr.ndim == 2:
            arr = np.repeat(arr[..., None], 3, axis=-1)
        if arr.shape[-1] > 3:
            arr = arr[..., :3]
        tensor = torch.from_numpy(np.ascontiguousarray(arr)).permute(2, 0, 1)
        return (tensor - self.mean) / self.std

    def __call__(self, image0: np.ndarray, image1: np.ndarray, device: torch.device) -> torch.Tensor:
        img0 = self._to_tensor(image0)
        img1 = self._to_tensor(image1)
        pad = torch.zeros_like(img0)
        return torch.stack([img0, img1, pad], dim=0).unsqueeze(0).to(device)


def iter_episode_rows(rows_path: Path) -> Iterable[tuple[str, list[dict]]]:
    current_eid = None
    buf: list[dict] = []
    seen = set()
    with rows_path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            row = json.loads(line)
            eid = row["episode_id"]
            if current_eid is None:
                current_eid = eid
            if eid != current_eid:
                if current_eid in seen:
                    raise RuntimeError(f"episode rows are non-contiguous: {current_eid}")
                seen.add(current_eid)
                buf.sort(key=lambda r: int(r["timestep"]))
                yield current_eid, buf
                current_eid = eid
                buf = []
            buf.append(row)
    if current_eid is not None:
        if current_eid in seen:
            raise RuntimeError(f"episode rows are non-contiguous: {current_eid}")
        buf.sort(key=lambda r: int(r["timestep"]))
        yield current_eid, buf


def load_state(path: Path) -> dict:
    z = np.load(path, allow_pickle=True)
    kind = str(z["kind"]) if "kind" in z.files else "flat"
    if "flat" in z.files:
        return {"kind": kind, "flat": z["flat"], "env_runtime": None, "sim_runtime": None}
    if "state" in z.files:
        return {"kind": kind, "state": z["state"], "env_runtime": None, "sim_runtime": None}
    raise RuntimeError(f"unsupported state npz keys for {path}: {z.files}")


def action_preds_from_row(row: dict) -> np.ndarray:
    main = np.asarray(row["main_candidate_action_chunk_normalized"], dtype=np.float32)
    ace = np.asarray(row["ace_candidate_chunks_normalized"], dtype=np.float32)
    if main.shape != (10, 7):
        raise RuntimeError(f"bad main action shape {main.shape} for {row['episode_id']} t={row['timestep']}")
    if ace.ndim != 3 or ace.shape[1:] != (10, 7):
        raise RuntimeError(f"bad ace action shape {ace.shape} for {row['episode_id']} t={row['timestep']}")
    if ace.shape[0] < 8:
        ace = np.concatenate([ace, np.repeat(main[None, :, :], 8 - ace.shape[0], axis=0)], axis=0)
    elif ace.shape[0] > 8:
        ace = ace[:8]
    return np.concatenate([main[None, :, :], ace], axis=0).astype(np.float32)


def resolve_bddl(row: dict) -> Path:
    meta = row.get("metadata", {})
    bddl = meta.get("bddl_path") or meta.get("resolved_bddl_path")
    if not bddl:
        raise RuntimeError(f"missing metadata.bddl_path for {row['episode_id']}")
    filename = Path(bddl).name
    folders = []
    for key in ["resolved_problem_folder", "declared_problem_folder", "problem_folder"]:
        val = meta.get(key)
        if val and val not in folders:
            folders.append(val)
    suite = row.get("suite")
    aliases = {
        "libero_goal_object_ood": ["libero_goal_object_ood", "libero_goal_object_ood_temp"],
        "libero_goal_swap": ["libero_goal_swap"],
        "libero_goal_task": ["libero_goal_task"],
        "libero_spatial_object": ["libero_spatial_object", "libero_spatial"],
        "libero_object_object": ["libero_object_object"],
        "libero_10_object": ["libero_10_object", "libero_10"],
    }
    for val in aliases.get(suite, []):
        if val not in folders:
            folders.append(val)
    root = LIBERO_ROOT / "libero" / "libero" / "bddl_files"
    for folder in folders:
        p = root / folder / filename
        if p.exists():
            return p
    matches = list(root.glob(f"**/{filename}"))
    if matches:
        return matches[0]
    raise FileNotFoundError(f"could not resolve BDDL {filename}; folders={folders}; root={root}")


def make_env_for_row(row: dict, OffScreenRenderEnv):
    bddl_path = resolve_bddl(row)
    env = OffScreenRenderEnv(bddl_file_name=str(bddl_path), camera_heights=384, camera_widths=384)
    env.seed(42)
    return env


def state_path_for_row(row: dict, dataset_root: Path) -> Path:
    current = row.get("current", {})
    candidates = []
    for key in ["sim_state_path", "state_path"]:
        if current.get(key):
            candidates.append(Path(current[key]))
    for p in candidates:
        if p.exists():
            return p
        mapped = dataset_root / "states" / p.name
        if mapped.exists():
            return mapped
    fallback = dataset_root / "states" / f"{row['episode_id']}_t{int(row['timestep']):04d}.npz"
    if fallback.exists():
        return fallback
    if candidates:
        name = candidates[0].name
        matches = list((dataset_root / "states").glob(name))
        if matches:
            return matches[0]
    raise FileNotFoundError(f"missing state for {row['episode_id']} t={row['timestep']}")


def encode_episode(model, processor, preproc, rows, dataset_root, device, micro_batch, stack):
    OffScreenRenderEnv, _, _, set_state, obs_images = stack
    env = None
    try:
        env = make_env_for_row(rows[0], OffScreenRenderEnv)
        lang = rows[0]["task_instruction"]
        input_ids_single = processor.encode_language([lang])["input_ids"].to(device)
        obs_feats = []
        actions = []
        pending = []

        def flush():
            nonlocal pending, obs_feats
            if not pending:
                return
            batch_imgs = torch.cat(pending, dim=0)
            mask = torch.tensor([[True, True, False]], device=device).repeat(batch_imgs.shape[0], 1)
            input_ids = input_ids_single.repeat(batch_imgs.shape[0], 1)
            with torch.inference_mode():
                enc = model.forward_vlm_efficient(batch_imgs, mask, input_ids)
            feats = enc["vlm_features"].mean(dim=1).detach().cpu().numpy().astype(np.float32)
            obs_feats.extend(list(feats))
            pending = []
            del batch_imgs, mask, input_ids, enc
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

        for row in rows:
            set_state(env, load_state(state_path_for_row(row, dataset_root)), hard_reset=False)
            obs_data = env.env._get_observations()
            before_img, before_wrist = obs_images(obs_data)
            pending.append(preproc(before_img, before_wrist, device))
            actions.append(action_preds_from_row(row))
            if len(pending) >= max(1, int(micro_batch)):
                flush()
        flush()
        return obs_feats, actions
    finally:
        if env is not None:
            try:
                env.close()
            except Exception:
                pass


def materialize_ood_dataset(name: str, micro_batch: int) -> Path:
    dataset_root = DATASETS_ROOT / name
    out_dir = OOD_MATERIALIZED_ROOT / name / "processed_rollouts"
    if (out_dir / "obs_embeddings.pt").exists() and (out_dir / "action_preds.pt").exists() and (out_dir / "metadata.pkl").exists():
        print(f"[materialize:{name}] reuse {out_dir}", flush=True)
        return out_dir

    rows_path = dataset_root / "fiper_receding_samples.jsonl"
    if not rows_path.exists():
        raise FileNotFoundError(rows_path)
    out_dir.mkdir(parents=True, exist_ok=True)
    cache_dir = RUN_ROOT / "cache" / name
    cache_dir.mkdir(parents=True, exist_ok=True)

    stack = import_simvla_stack()
    _, SmolVLMVLA, SmolVLMVLAProcessor, _, _ = stack
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[materialize:{name}] device={device} loading {CHECKPOINT}", flush=True)
    model = SmolVLMVLA.from_pretrained(str(CHECKPOINT)).to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained(SMOLVLM_PATH)
    preproc = ImagePreprocessor(384)

    obs_parts, action_parts = [], []
    starts, ends, keys = [], [], []
    success, failed = [], []
    task_ids, instructions = [], []
    offset = 0

    for ep_idx, (eid, rows) in enumerate(iter_episode_rows(rows_path), 1):
        cache_file = cache_dir / f"{eid}.pkl"
        if cache_file.exists():
            with cache_file.open("rb") as f:
                cache = pickle.load(f)
            ep_obs, ep_actions = cache["obs"], cache["actions"]
            print(f"[materialize:{name}:{ep_idx}] cache {eid} steps={len(ep_obs)}", flush=True)
        else:
            print(f"[materialize:{name}:{ep_idx}] process {eid} steps={len(rows)} task={rows[0]['task_id']}", flush=True)
            ep_obs, ep_actions = encode_episode(model, processor, preproc, rows, dataset_root, device, micro_batch, stack)
            with cache_file.open("wb") as f:
                pickle.dump({"obs": ep_obs, "actions": ep_actions}, f)
        if len(ep_obs) != len(ep_actions) or len(ep_obs) != len(rows):
            raise RuntimeError(f"length mismatch {eid}: obs={len(ep_obs)} actions={len(ep_actions)} rows={len(rows)}")
        starts.append(offset)
        obs_parts.extend(ep_obs)
        action_parts.extend(ep_actions)
        offset += len(ep_obs)
        ends.append(offset)
        keys.append(eid)
        is_success = rows[-1].get("episode_outcome") == "success" or bool(rows[-1].get("parent_episode_success", False))
        success.append(is_success)
        failed.append(not is_success)
        task_ids.append(int(rows[0]["task_id"]))
        instructions.append(rows[0].get("task_instruction", ""))

    obs_tensor = torch.tensor(np.asarray(obs_parts, dtype=np.float32))
    action_tensor = torch.tensor(np.asarray(action_parts, dtype=np.float32))
    metadata = {
        "episode_start_indices": np.asarray(starts, dtype=np.int64),
        "episode_end_indices": np.asarray(ends, dtype=np.int64),
        "calibration_rollout_labels": np.zeros(len(keys), dtype=bool),
        "test_rollout_labels": np.ones(len(keys), dtype=bool),
        "successful_rollout_labels": np.asarray(success, dtype=bool),
        "failed_rollout_labels": np.asarray(failed, dtype=bool),
        "id_rollout_labels": np.zeros(len(keys), dtype=bool),
        "ood_rollout_labels": np.ones(len(keys), dtype=bool),
        "num_steps": int(offset),
        "num_rollouts": int(len(keys)),
        "episode_lengths": np.asarray(ends, dtype=np.int64) - np.asarray(starts, dtype=np.int64),
        "num_robots": 1,
        "actions": {"action_dim": 7, "action_mapping": {"position": [0, 1, 2], "rotation": [3, 4, 5], "gripper": [6]}},
        "available_tensors": ["action_preds", "obs_embeddings"],
        "episode_keys": keys,
        "task_ids": np.asarray(task_ids, dtype=np.int64),
        "instructions": instructions,
        "source_rows": str(rows_path),
        "source_dataset_root": str(dataset_root),
        "checkpoint": str(CHECKPOINT),
    }
    torch.save(obs_tensor, out_dir / "obs_embeddings.pt")
    torch.save(action_tensor, out_dir / "action_preds.pt")
    with (out_dir / "metadata.pkl").open("wb") as f:
        pickle.dump(metadata, f)
    summary = {
        "dataset": name,
        "obs_shape": list(obs_tensor.shape),
        "action_shape": list(action_tensor.shape),
        "num_rollouts": len(keys),
        "num_steps": int(offset),
        "success": int(np.asarray(success, dtype=bool).sum()),
        "failure": int(np.asarray(failed, dtype=bool).sum()),
    }
    (out_dir.parent / "MATERIALIZATION_SUMMARY.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2), flush=True)
    del model, processor, obs_tensor, action_tensor
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    gc.collect()
    return out_dir


def concat_seen_calib_and_ood(name: str, ood_processed: Path) -> Path:
    task_name = f"seen_calib_plus_{name}"
    task_data = COMBINED_ROOT / task_name
    processed = task_data / "processed_rollouts"
    if (processed / "obs_embeddings.pt").exists() and (processed / "action_preds.pt").exists() and (processed / "metadata.pkl").exists():
        print(f"[combine:{name}] reuse {processed}", flush=True)
    else:
        processed.mkdir(parents=True, exist_ok=True)
        seen_meta = pickle.load(open(SEEN_PROCESSED / "metadata.pkl", "rb"))
        ood_meta = pickle.load(open(ood_processed / "metadata.pkl", "rb"))
        seen_obs = torch.load(SEEN_PROCESSED / "obs_embeddings.pt", map_location="cpu", weights_only=True)
        seen_act = torch.load(SEEN_PROCESSED / "action_preds.pt", map_location="cpu", weights_only=True)
        ood_obs = torch.load(ood_processed / "obs_embeddings.pt", map_location="cpu", weights_only=True)
        ood_act = torch.load(ood_processed / "action_preds.pt", map_location="cpu", weights_only=True)

        obs_parts, act_parts = [], []
        starts, ends, keys = [], [], []
        calib, test, success, failed, id_labels, ood_labels = [], [], [], [], [], []
        offset = 0

        seen_calib_idx = np.flatnonzero(np.asarray(seen_meta["calibration_rollout_labels"], dtype=bool))
        for idx in seen_calib_idx:
            s = int(seen_meta["episode_start_indices"][idx])
            e = int(seen_meta["episode_end_indices"][idx])
            obs_parts.append(seen_obs[s:e])
            act_parts.append(seen_act[s:e])
            starts.append(offset)
            offset += e - s
            ends.append(offset)
            keys.append(f"seen_calib::{seen_meta['episode_keys'][idx]}")
            calib.append(True); test.append(False); success.append(True); failed.append(False); id_labels.append(True); ood_labels.append(False)

        for idx, key in enumerate(ood_meta["episode_keys"]):
            s = int(ood_meta["episode_start_indices"][idx])
            e = int(ood_meta["episode_end_indices"][idx])
            obs_parts.append(ood_obs[s:e])
            act_parts.append(ood_act[s:e])
            starts.append(offset)
            offset += e - s
            ends.append(offset)
            keys.append(f"{name}::{key}")
            is_success = bool(ood_meta["successful_rollout_labels"][idx])
            calib.append(False); test.append(True); success.append(is_success); failed.append(not is_success); id_labels.append(False); ood_labels.append(True)

        obs_tensor = torch.cat(obs_parts, dim=0).contiguous()
        act_tensor = torch.cat(act_parts, dim=0).contiguous()
        metadata = {
            "episode_start_indices": np.asarray(starts, dtype=np.int64),
            "episode_end_indices": np.asarray(ends, dtype=np.int64),
            "calibration_rollout_labels": np.asarray(calib, dtype=bool),
            "test_rollout_labels": np.asarray(test, dtype=bool),
            "successful_rollout_labels": np.asarray(success, dtype=bool),
            "failed_rollout_labels": np.asarray(failed, dtype=bool),
            "id_rollout_labels": np.asarray(id_labels, dtype=bool),
            "ood_rollout_labels": np.asarray(ood_labels, dtype=bool),
            "num_steps": int(offset),
            "num_rollouts": int(len(keys)),
            "episode_lengths": np.asarray(ends, dtype=np.int64) - np.asarray(starts, dtype=np.int64),
            "num_robots": 1,
            "actions": {"action_dim": 7, "action_mapping": {"position": [0, 1, 2], "rotation": [3, 4, 5], "gripper": [6]}},
            "available_tensors": ["action_preds", "obs_embeddings"],
            "episode_keys": keys,
            "source_seen_processed": str(SEEN_PROCESSED),
            "source_ood_processed": str(ood_processed),
        }
        torch.save(obs_tensor, processed / "obs_embeddings.pt")
        torch.save(act_tensor, processed / "action_preds.pt")
        with (processed / "metadata.pkl").open("wb") as f:
            pickle.dump(metadata, f)
        del seen_obs, seen_act, ood_obs, ood_act, obs_tensor, act_tensor

    rnd_dst = task_data / "rnd_models" / "rnd_oe"
    rnd_dst.mkdir(parents=True, exist_ok=True)
    for ckpt in SEEN_RND.glob("*.ckpt"):
        dst = rnd_dst / ckpt.name
        if not dst.exists():
            shutil.copy2(ckpt, dst)
    return task_data


def ensure_task_config(task_name: str) -> Path:
    cfg_path = FIPER_REPO / "configs" / "task" / f"{task_name}.yaml"
    cfg_path.write_text(
        f"""defaults:
  - base

name: "{task_name}"
description: "Official FIPER adapter: seen LIBERO goal_object calibration plus OOD test"
type: simulation

environment:
  name: "{task_name}"
  ts: 0.1
  max_episode_steps: 300
  fail_on_error: true
  fail_after_steps: 300

observation_space:
  observation_type: "embedding"
  observation_dim: 960

state_space:
  state_dim: 0
  state_types:
  state_bounds:
  state_mapping:
    position:
    rotation:
    velocity:

action_space:
  action_type: "continuous"
  actions:
    dim: 7
    action_bounds:
    action_mapping:
      position: [0, 1, 2]
      rotation: [3, 4, 5]
      velocity:
      gripper: [6]
  action_pred:
    format: "(batch_size, prediction_horizon, action_dim)"
    action_prediction_horizon: 10
    batch_size: 9
    shape: (${{task.action_space.action_pred.batch_size}}, ${{task.action_space.action_pred.action_prediction_horizon}}, ${{task.action_space.actions.dim}})
  action_execution_horizon: 10
""",
        encoding="utf-8",
    )
    return cfg_path


def load_dataset(ProcessedRolloutDataset, task_data: Path, required_tensors):
    processed = task_data / "processed_rollouts"
    metadata = pickle.load(open(processed / "metadata.pkl", "rb"))
    obs_embeddings = torch.load(processed / "obs_embeddings.pt", map_location="cpu", weights_only=True)
    action_preds = torch.load(processed / "action_preds.pt", map_location="cpu", weights_only=True)
    metadata = dict(metadata)
    metadata["available_tensors"] = ["obs_embeddings", "action_preds"]
    dataset = ProcessedRolloutDataset(
        task_data_path=str(task_data),
        base_config_path=str(FIPER_REPO / "configs"),
        required_tensors=required_tensors,
        optional_tensors=[],
        normalize_tensors={
            "obs_embeddings": False,
            "action_preds": False,
            "rgb_images": True,
            "actions": False,
            "states": False,
            "mode": "gaussian",
            "range_eps": 1e-5,
            "limits": [-1, 1],
            "fit_offset": True,
        },
    )
    dataset.data = {"metadata": metadata, "obs_embeddings": obs_embeddings, "action_preds": action_preds}
    dataset.dataset_loaded = True
    dataset.normalizer = {}
    dataset._assert_metadata()
    dataset._assert_tensor("obs_embeddings", shape=(960,))
    dataset._assert_tensor("action_preds", shape=(9, 10, 7))
    return dataset


def alarm_metrics(scores_by_episode, success_mask):
    success_mask = np.asarray(success_mask, dtype=bool)
    failure_mask = ~success_mask
    alarms, det_fracs = [], []
    for scores in scores_by_episode:
        arr = np.asarray(scores, dtype=np.float64)
        hit = np.flatnonzero(arr > 1.0)
        alarms.append(hit.size > 0)
        det_fracs.append(float(hit[0]) / max(1, len(arr)) if hit.size else np.nan)
    alarms = np.asarray(alarms, dtype=bool)
    det_fracs = np.asarray(det_fracs, dtype=np.float64)
    fail_hits = alarms & failure_mask
    fail_total = max(1, int(failure_mask.sum()))
    succ_total = max(1, int(success_mask.sum()))
    detected_fracs = det_fracs[fail_hits]
    return {
        "success_false_alarm": float((alarms & success_mask).sum() / succ_total),
        "failure_detection": float(fail_hits.sum() / fail_total),
        "det_at_10": float(np.sum(detected_fracs <= 0.10) / fail_total),
        "det_at_25": float(np.sum(detected_fracs <= 0.25) / fail_total),
        "det_at_50": float(np.sum(detected_fracs <= 0.50) / fail_total),
        "mean_time": float(np.nanmean(detected_fracs)) if detected_fracs.size else float("nan"),
        "never": float((failure_mask & ~alarms).sum() / fail_total),
    }


def summarize_selected(seed: int, results: dict) -> list[dict]:
    rows = []
    for method, style, window, label in SELECTED_OPERATING_POINTS:
        result = results[method]
        success_mask = np.asarray(result["successful_test_rollouts"], dtype=bool)
        q = "0.95"
        qkey = 0.95
        scores_map = result["test_scores_by_threshold"]
        if style not in scores_map or qkey not in scores_map[style]:
            raise KeyError(f"missing style/q for {method} {style} {qkey}")
        available = {str(k): k for k in scores_map[style][qkey].keys()}
        if window not in available:
            raise KeyError(f"missing window {window} for {method} {style}; available={sorted(available)}")
        scores = scores_map[style][qkey][available[window]]
        m = alarm_metrics(scores, success_mask)
        rows.append({"seed": seed, "method": method, "threshold_style": style, "quantile": q, "window": window, "label": label, **m})
    return rows


def aggregate(rows: list[dict]) -> list[dict]:
    groups = {}
    for row in rows:
        groups.setdefault((row["dataset"], row["method"], row["threshold_style"], row["window"], row["label"]), []).append(row)
    metric_keys = ["success_false_alarm", "failure_detection", "det_at_10", "det_at_25", "det_at_50", "mean_time", "never"]
    out = []
    for key, vals in groups.items():
        row = {"dataset": key[0], "method": key[1], "threshold_style": key[2], "window": key[3], "label": key[4], "n_seeds": len(vals)}
        for metric in metric_keys:
            row[metric] = float(np.nanmean([v[metric] for v in vals]))
        out.append(row)
    out.sort(key=lambda r: (r["dataset"], r["method"], r["threshold_style"], r["window"]))
    return out


def write_csv(path: Path, rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def fmt_pct(x: float) -> str:
    return "N/A" if np.isnan(x) else f"{100*x:.1f}%"


def write_report(agg_rows: list[dict], validations: dict):
    lines = [
        "# Official FIPER Seen-Calibrated Cross-Suite OOD Evaluation",
        "",
        "## Protocol",
        "",
        "- Calibration data: official seen `libero_goal_object` success rollouts only.",
        "- Test data: each OOD dataset is test-only; no OOD calibration and no OOD threshold tuning.",
        "- RND checkpoints: reused the official FIPER RND-OE checkpoints trained on seen calibration for seeds 0, 1, 2, 42, 43.",
        "- Method code: official FIPER `EvaluationManager` and method classes are used; this script is only a dataset/materialization adapter.",
        "- Reported rows: the exact q95 operating points selected from the seen held-out FIPER table.",
        "",
        "## Dataset Validation",
        "",
        "| Dataset | Episodes | Success | Failure | Rows |",
        "|---|---:|---:|---:|---:|",
    ]
    for name in DATASET_NAMES:
        v = validations[name]
        lines.append(f"| `{name}` | {v['episodes']} | {v['success']} | {v['failure']} | {v['rows']} |")
    for name in DATASET_NAMES:
        rows = [r for r in agg_rows if r["dataset"] == name]
        lines += [
            "",
            f"## `{name}`",
            "",
            "| Method | Threshold | Window | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for r in rows:
            mt = "N/A" if np.isnan(r["mean_time"]) else f"{r['mean_time']:.3f}"
            lines.append(
                f"| `{r['method']}` | `{r['threshold_style']}` | `{r['window']}` | "
                f"{fmt_pct(r['success_false_alarm'])} | {fmt_pct(r['failure_detection'])} | "
                f"{fmt_pct(r['det_at_10'])} | {fmt_pct(r['det_at_25'])} | {fmt_pct(r['det_at_50'])} | {mt} | {fmt_pct(r['never'])} |"
            )
    lines += [
        "",
        "## Output Files",
        "",
        f"- Aggregate CSV: `{RUN_ROOT / 'official_fiper_seen_thresholds_cross_suite_ood_aggregate.csv'}`",
        f"- Per-seed CSV: `{RUN_ROOT / 'official_fiper_seen_thresholds_cross_suite_ood_per_seed.csv'}`",
        "",
        "## Flags",
        "",
        "- `NO_OOD_CALIBRATION = YES`",
        "- `NO_OOD_THRESHOLD_TUNING = YES`",
        "- `SEEN_CALIBRATION_ONLY = YES`",
        "- `RND_CHECKPOINTS_REUSED = YES`",
        "- `OFFICIAL_FIPER_METHOD_CLASSES_USED = YES`",
        "- `RUN_COMPLETE = YES`",
        "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def validate_task(task_data: Path) -> dict:
    meta = pickle.load(open(task_data / "processed_rollouts" / "metadata.pkl", "rb"))
    return {
        "episodes": int(meta["num_rollouts"]),
        "rows": int(meta["num_steps"]),
        "calibration": int(np.asarray(meta["calibration_rollout_labels"], dtype=bool).sum()),
        "test": int(np.asarray(meta["test_rollout_labels"], dtype=bool).sum()),
        "success": int((np.asarray(meta["test_rollout_labels"], dtype=bool) & np.asarray(meta["successful_rollout_labels"], dtype=bool)).sum()),
        "failure": int((np.asarray(meta["test_rollout_labels"], dtype=bool) & np.asarray(meta["failed_rollout_labels"], dtype=bool)).sum()),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--micro-batch",
        type=int,
        default=int(os.environ.get("FIPER_VLM_MICRO_BATCH", "32")),
        help="VLM image micro-batch size used during embedding materialization.",
    )
    args = parser.parse_args()
    RUN_ROOT.mkdir(parents=True, exist_ok=True)
    ProcessedRolloutDataset, EvaluationManager, load_config, get_required_tensors, set_seed = import_official_fiper()
    required_tensors, _ = get_required_tensors(METHODS, str(FIPER_REPO / "configs"))
    required_tensors = list(dict.fromkeys(required_tensors))
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    all_rows = []
    validations = {}

    for name in DATASET_NAMES:
        print(f"========== DATASET {name} ==========", flush=True)
        ood_processed = materialize_ood_dataset(name, micro_batch=args.micro_batch)
        task_data = concat_seen_calib_and_ood(name, ood_processed)
        task_name = task_data.name
        ensure_task_config(task_name)
        validations[name] = validate_task(task_data)
        print(f"[validate:{name}] {validations[name]}", flush=True)
        task_cfg = load_config("task", task_name, return_only_subdict=False, base_config_dir=str(FIPER_REPO / "configs"))

        results_dir = task_data / "results"
        if results_dir.exists():
            shutil.rmtree(results_dir)

        for seed in SEEDS:
            set_seed(seed)
            print(f"[eval:{name}] seed={seed}", flush=True)
            dataset = load_dataset(ProcessedRolloutDataset, task_data, required_tensors)
            evaluator = EvaluationManager(str(FIPER_REPO / "configs"), str(task_data), dataset, device=device, seed=seed)
            results = evaluator.evaluate(METHODS, combine_methods=True, combined_methods=copy.deepcopy(COMBINED))
            seed_rows = summarize_selected(seed, results)
            for row in seed_rows:
                row["dataset"] = name
            all_rows.extend(seed_rows)
            write_csv(RUN_ROOT / "official_fiper_seen_thresholds_cross_suite_ood_per_seed.partial.csv", all_rows)
            del results, evaluator, dataset
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            gc.collect()

    agg_rows = aggregate(all_rows)
    write_csv(RUN_ROOT / "official_fiper_seen_thresholds_cross_suite_ood_per_seed.csv", all_rows)
    write_csv(RUN_ROOT / "official_fiper_seen_thresholds_cross_suite_ood_aggregate.csv", agg_rows)
    (RUN_ROOT / "VALIDATION_SUMMARY.json").write_text(json.dumps(validations, indent=2), encoding="utf-8")
    write_report(agg_rows, validations)
    print(f"[done] wrote {REPORT}", flush=True)


if __name__ == "__main__":
    main()
