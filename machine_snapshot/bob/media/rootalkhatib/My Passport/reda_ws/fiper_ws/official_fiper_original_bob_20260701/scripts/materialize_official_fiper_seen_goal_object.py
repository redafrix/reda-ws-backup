import argparse
import json
import os
import pickle
import sys
from pathlib import Path
from typing import Dict, List

import numpy as np
import torch
from PIL import Image

# Runtime paths are supplied by activate_simvla_bob.sh, but keep explicit fallbacks.
REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
SIMVLA_ROOT = REDA_WS / "intern_ship_ws" / "simvla" / "code" / "SimVLA_modified"
LIBERO_ROOT = REDA_WS / "intern_ship_ws" / "assets" / "repos" / "LIBERO-PRO"
STAGE9_ROOT = REDA_WS / "fiper_ws" / "collection" / "data_collection_stage9"
STAGE9_TOOLS = REDA_WS / "fiper_ws" / "stage9_v2_tools"
for p in [SIMVLA_ROOT, LIBERO_ROOT, STAGE9_ROOT, STAGE9_TOOLS]:
    sys.path.insert(0, str(p))

# Newer torch defaults can break legacy HF checkpoints.
_orig_load = torch.load
def _torch_load_compat(*args, **kwargs):
    kwargs.setdefault("weights_only", False)
    return _orig_load(*args, **kwargs)
torch.load = _torch_load_compat

from libero.libero.envs import OffScreenRenderEnv
from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor
from sim_state_utils import set_state
from libero_pro_env_utils import obs_images

ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701")
SUBSET = ROOT / "seen_goal_object_fiper_subset"
ROWS_PATH = SUBSET / "selected_rows.jsonl"
EPISODES_PATH = SUBSET / "selected_episodes.json"
STATE_STAGING = Path("/home/rootalkhatib/states_temp")
OUT_DIR = ROOT / "official_fiper_data" / "libero_goal_object_official" / "processed_rollouts"
CACHE_DIR = ROOT / "cache" / "seen_goal_object_official"
CHECKPOINT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000")
SMOLVLM_PATH = "HuggingFaceTB/SmolVLM-500M-Instruct"

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

def episode_split_map() -> Dict[str, str]:
    data = json.loads(EPISODES_PATH.read_text())
    if isinstance(data, dict) and "episodes" in data:
        pairs = []
        for item in data["episodes"]:
            eid = item.get("episode_id") or item.get("id")
            pairs.append((eid, item))
    elif isinstance(data, dict):
        pairs = list(data.items())
    elif isinstance(data, list):
        pairs = []
        for item in data:
            eid = item.get("episode_id") or item.get("id")
            pairs.append((eid, item))
    else:
        raise RuntimeError(f"unknown selected_episodes format: {type(data)}")
    out = {}
    for eid, item in pairs:
        split = item.get("split") or item.get("selected_split") or item.get("use")
        if not eid or not split:
            raise RuntimeError(f"bad episode item: eid={eid} item={item}")
        if eid in out:
            raise RuntimeError(f"duplicate episode in selected_episodes: {eid}")
        out[eid] = split
    return out

def load_state(path: Path) -> dict:
    z = np.load(path, allow_pickle=True)
    kind = str(z["kind"])
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
        pad = np.repeat(main[None, :, :], 8 - ace.shape[0], axis=0)
        ace = np.concatenate([ace, pad], axis=0)
    elif ace.shape[0] > 8:
        ace = ace[:8]
    return np.concatenate([main[None, :, :], ace], axis=0).astype(np.float32)

def make_env_for_row(row: dict):
    meta = row.get("metadata", {})
    bddl = meta.get("bddl_path")
    if not bddl:
        raise RuntimeError(f"missing metadata.bddl_path for {row['episode_id']}")
    # The source path may come from Sam; map it to Bob's LIBERO-PRO root.
    filename = Path(bddl).name
    folder = meta.get("resolved_problem_folder") or meta.get("declared_problem_folder") or "libero_goal_object_official"
    bddl_path = LIBERO_ROOT / "libero" / "libero" / "bddl_files" / folder / filename
    if not bddl_path.exists():
        raise FileNotFoundError(f"missing mapped bddl {bddl_path} from source {bddl}")
    env = OffScreenRenderEnv(bddl_file_name=str(bddl_path), camera_heights=384, camera_widths=384)
    env.seed(42)
    return env, str(bddl_path)

def encode_episode(model, processor, preproc, rows: List[dict], device: torch.device, micro_batch: int):
    if not rows:
        return [], []
    env = None
    try:
        env, bddl_path = make_env_for_row(rows[0])
        lang = rows[0]["task_instruction"]
        input_ids_single = processor.encode_language([lang])["input_ids"].to(device)
        obs_feats = []
        actions = []

        pending_images = []

        def flush_pending():
            nonlocal pending_images, obs_feats
            if not pending_images:
                return
            batch_imgs = torch.cat(pending_images, dim=0)
            mask = torch.tensor([[True, True, False]], device=device).repeat(batch_imgs.shape[0], 1)
            input_ids = input_ids_single.repeat(batch_imgs.shape[0], 1)
            with torch.inference_mode():
                enc = model.forward_vlm_efficient(batch_imgs, mask, input_ids)
            feats = enc["vlm_features"].mean(dim=1).detach().cpu().numpy().astype(np.float32)
            obs_feats.extend(list(feats))
            del batch_imgs, mask, input_ids, enc
            pending_images = []
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

        for row in rows:
            state_name = Path(row["current"].get("sim_state_path_sam_original") or row["current"]["sim_state_path"]).name
            state_path = STATE_STAGING / state_name
            if not state_path.exists():
                raise FileNotFoundError(f"missing staging state {state_path}")
            set_state(env, load_state(state_path), hard_reset=False)
            obs_data = env.env._get_observations()
            before_img, before_wrist = obs_images(obs_data)
            pending_images.append(preproc(before_img, before_wrist, device))
            actions.append(action_preds_from_row(row))
            if len(pending_images) >= max(1, int(micro_batch)):
                flush_pending()
        flush_pending()
        return obs_feats, actions
    finally:
        if env is not None:
            try:
                env.close()
            except Exception:
                pass

def iter_episode_rows(path: Path):
    current_eid = None
    buf = []
    seen = set()
    with path.open("r", encoding="utf-8") as f:
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

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--micro-batch", type=int, default=int(os.environ.get("FIPER_VLM_MICRO_BATCH", "8")))
    ap.add_argument("--limit-episodes", type=int, default=0)
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    os.environ.setdefault("MUJOCO_GL", "egl")
    os.environ.setdefault("PYOPENGL_PLATFORM", "egl")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    torch.set_float32_matmul_precision("high")

    if OUT_DIR.exists() and any(OUT_DIR.iterdir()) and not args.overwrite:
        raise SystemExit(f"Output dir already nonempty: {OUT_DIR}. Use --overwrite to replace.")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    split_by_ep = episode_split_map()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[startup] device={device} micro_batch={args.micro_batch}", flush=True)
    print(f"[startup] loading model {CHECKPOINT}", flush=True)
    model = SmolVLMVLA.from_pretrained(str(CHECKPOINT)).to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained(SMOLVLM_PATH)
    preproc = ImagePreprocessor(384)

    obs_parts = []
    action_parts = []
    starts, ends, keys = [], [], []
    calib, test, success, failed, id_labels, ood_labels = [], [], [], [], [], []
    offset = 0
    counts = {}

    for ep_idx, (eid, rows) in enumerate(iter_episode_rows(ROWS_PATH), 1):
        if args.limit_episodes and ep_idx > args.limit_episodes:
            break
        split = split_by_ep.get(eid)
        if split is None:
            raise RuntimeError(f"episode {eid} present in rows but not selected_episodes")
        cache_file = CACHE_DIR / f"{eid}.pkl"
        if cache_file.exists():
            with cache_file.open("rb") as f:
                cache = pickle.load(f)
            ep_obs = cache["obs"]
            ep_actions = cache["actions"]
            print(f"[{ep_idx}] cache {eid} split={split} steps={len(ep_obs)}", flush=True)
        else:
            print(f"[{ep_idx}] process {eid} split={split} steps={len(rows)} task={rows[0]['task_id']}", flush=True)
            ep_obs, ep_actions = encode_episode(model, processor, preproc, rows, device, args.micro_batch)
            with cache_file.open("wb") as f:
                pickle.dump({"obs": ep_obs, "actions": ep_actions}, f)
        if len(ep_obs) != len(ep_actions) or len(ep_obs) != len(rows):
            raise RuntimeError(f"episode length mismatch for {eid}: obs={len(ep_obs)} actions={len(ep_actions)} rows={len(rows)}")
        starts.append(offset)
        obs_parts.extend(ep_obs)
        action_parts.extend(ep_actions)
        offset += len(ep_obs)
        ends.append(offset)
        keys.append(eid)
        counts[split] = counts.get(split, 0) + 1
        is_success = split in {"train_success", "calib_success", "seen_test_success"}
        is_test = split in {"seen_test_success", "seen_test_failure"}
        calib.append(split == "calib_success")
        test.append(is_test)
        success.append(is_success)
        failed.append(not is_success)
        id_labels.append(True)
        ood_labels.append(False)

    print("[save] stacking tensors", flush=True)
    obs_tensor = torch.tensor(np.asarray(obs_parts, dtype=np.float32))
    action_tensor = torch.tensor(np.asarray(action_parts, dtype=np.float32))
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
        "split_counts": counts,
        "source_rows": str(ROWS_PATH),
        "state_staging": str(STATE_STAGING),
        "checkpoint": str(CHECKPOINT),
        "action_space_note": "action_preds built from normalized SimVLA main_candidate_action_chunk_normalized + ace_candidate_chunks_normalized, matching prior official-FIPER materializations",
    }
    torch.save(obs_tensor, OUT_DIR / "obs_embeddings.pt")
    torch.save(action_tensor, OUT_DIR / "action_preds.pt")
    with (OUT_DIR / "metadata.pkl").open("wb") as f:
        pickle.dump(metadata, f)
    report = {
        "obs_shape": list(obs_tensor.shape),
        "action_shape": list(action_tensor.shape),
        "num_rollouts": len(keys),
        "num_steps": int(offset),
        "split_counts": counts,
        "output_dir": str(OUT_DIR),
    }
    (ROOT / "MATERIALIZATION_SUMMARY.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2), flush=True)

if __name__ == "__main__":
    main()
