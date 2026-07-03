import argparse
import json
import os
import pickle
import sys
import shutil
from pathlib import Path
import numpy as np
import torch
from PIL import Image

# Monkeypatch torch.load to avoid weights_only error in newer PyTorch
orig_load = torch.load
torch.load = lambda *args, **kwargs: orig_load(*args, **{**kwargs, "weights_only": False})


sys.path.append("/home/redafrix/SimVLA_modified")
sys.path.append("/home/redafrix/LIBERO-PRO")
sys.path.append("/home/dean/fiper_uncertainty_collection/src/data_collection_stage9")

from libero.libero import benchmark, get_libero_path
from libero.libero.envs import OffScreenRenderEnv
from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor
from sim_state_utils import set_state
from libero_pro_env_utils import obs_images, obs_to_proprio

BASE_DIR = Path("/home/dean/fiper_uncertainty_collection")
EXP_DIR = BASE_DIR / "experiments" / "official_fiper_goal_object_ood_ablation_20260625"
DATA_ROOT = EXP_DIR / "official_fiper_data"
CACHE_DIR = EXP_DIR / "cache"
OOD_BDDL_ROOT = Path("/home/dean/LIBERO-PRO/libero/libero/bddl_files")
VLM_MICRO_BATCH = int(os.environ.get("FIPER_VLM_MICRO_BATCH", "4"))

IN_DOMAIN_ROOT = Path("/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/worker_0")
IN_DOMAIN_QUERY_SAMPLES = IN_DOMAIN_ROOT / "stratified_query_samples_50train_15calib_per_task.jsonl"
OOD_ROOT = Path("/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622")

SPLITS = [
    "success_train_seen",
    "success_calib_seen",
    "success_test_seen",
    "success_test_ood",
    "failure_test_seen",
    "failure_eval_ood",
]

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

    def __call__(self, image0: np.ndarray, image1: np.ndarray, device: torch.device):
        img0 = self._to_tensor(image0)
        img1 = self._to_tensor(image1)
        pad = torch.zeros_like(img0)
        images = torch.stack([img0, img1, pad], dim=0).unsqueeze(0).to(device)
        image_mask = torch.tensor([[True, True, False]], device=device)
        return images, image_mask

def encode_vlm_features(model, processor, episode_images, task_instruction, device):
    """Encode episode images in small batches to avoid CUDA OOM/fragmentation."""
    episode_obs = []
    if len(episode_images) == 0:
        return episode_obs

    input_ids_single = processor.encode_language([task_instruction])["input_ids"].to(device)
    for start in range(0, len(episode_images), VLM_MICRO_BATCH):
        batch_images = episode_images[start:start + VLM_MICRO_BATCH]
        images_batched = torch.cat(batch_images, dim=0)
        mask_batched = torch.tensor([[True, True, False]], device=device).repeat(len(batch_images), 1)
        input_ids_batched = input_ids_single.repeat(len(batch_images), 1)

        with torch.inference_mode():
            enc = model.forward_vlm_efficient(images_batched, mask_batched, input_ids_batched)
        vlm_feats = enc["vlm_features"].mean(dim=1).cpu().numpy().astype(np.float32)
        for vlm_feat in vlm_feats:
            episode_obs.append(vlm_feat)

        del images_batched, mask_batched, input_ids_batched, enc
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    return episode_obs

def main():
    os.environ["MUJOCO_GL"] = "egl"
    os.environ["PYOPENGL_PLATFORM"] = "egl"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}", flush=True)
    print("Loading VLA model...", flush=True)
    model = SmolVLMVLA.from_pretrained("/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000").to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained("HuggingFaceTB/SmolVLM-500M-Instruct")
    image_preprocessor = ImagePreprocessor(384)
    benchmark_dict = benchmark.get_benchmark_dict()

    # Group in-domain filtered query sample rows by episode
    in_domain_rows_by_ep = {}
    with open(IN_DOMAIN_QUERY_SAMPLES) as f:
        for line_idx, line in enumerate(f):
            if not line.strip():
                continue
            row = json.loads(line)
            ep_id = row["episode_id"]
            in_domain_rows_by_ep.setdefault(ep_id, []).append(row)

    # Sort each episode's rows by timestep
    for ep_id in in_domain_rows_by_ep:
        in_domain_rows_by_ep[ep_id].sort(key=lambda x: x["timestep"])

    in_domain_summaries = {}
    with open(IN_DOMAIN_ROOT / "episode_summaries.jsonl") as f:
        for line in f:
            if line.strip():
                row = json.loads(line)
                in_domain_summaries[row["episode_id"]] = row

    # Determine a stratified in-domain split: 50 train successes + 15
    # calibration successes per task. This prevents task composition leakage
    # from lexicographic episode ordering.
    print("Determining stratified in-domain splits...", flush=True)
    eps_by_task = {}
    for ep_id in sorted(in_domain_rows_by_ep):
        summary = in_domain_summaries[ep_id]
        if not bool(summary.get("success", False)):
            continue
        task_id = int(summary["task_id"])
        eps_by_task.setdefault(task_id, []).append(ep_id)

    expected_tasks = list(range(10))
    missing_tasks = [t for t in expected_tasks if len(eps_by_task.get(t, [])) < 65]
    if missing_tasks:
        counts = {t: len(eps_by_task.get(t, [])) for t in expected_tasks}
        raise RuntimeError(f"Not enough success episodes per task for stratified 50/15 split: {counts}")

    train_eps = []
    calib_eps = []
    for task_id in expected_tasks:
        eps = sorted(eps_by_task[task_id])
        train_eps.extend(eps[:50])
        calib_eps.extend(eps[50:65])

    train_eps_set = set(train_eps)
    calib_eps_set = set(calib_eps)
    assert len(train_eps) == 500, len(train_eps)
    assert len(calib_eps) == 150, len(calib_eps)
    assert not train_eps_set.intersection(calib_eps_set)
    print(f"Split: {len(train_eps)} train, {len(calib_eps)} calib. Zero overlap: True", flush=True)
    print("Train per-task counts:", {t: sum(int(in_domain_summaries[e]["task_id"]) == t for e in train_eps) for t in expected_tasks}, flush=True)
    print("Calib per-task counts:", {t: sum(int(in_domain_summaries[e]["task_id"]) == t for e in calib_eps) for t in expected_tasks}, flush=True)

    # Group OOD query samples by episode
    ood_rows_by_ep = {}
    with open(OOD_ROOT / "fiper_receding_samples.jsonl") as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            ep_id = row["episode_id"]
            ood_rows_by_ep.setdefault(ep_id, []).append(row)

    # Sort OOD rows by timestep
    for ep_id in ood_rows_by_ep:
        ood_rows_by_ep[ep_id].sort(key=lambda x: x["timestep"])

    ood_outcomes = {}
    with open(OOD_ROOT / "episode_summaries.jsonl") as f:
        for line in f:
            if line.strip():
                row = json.loads(line)
                ood_outcomes[row["episode_id"]] = row["success"]

    split_episodes = {
        "success_train_seen": train_eps,
        "success_calib_seen": calib_eps,
        "success_test_seen": [],
        "success_test_ood": [ep_id for ep_id, succ in ood_outcomes.items() if succ],
        "failure_test_seen": [],
        "failure_eval_ood": [ep_id for ep_id, succ in ood_outcomes.items() if not succ],
    }


    # Process all splits into lists
    all_obs = []
    all_actions = []
    starts = []
    ends = []
    calibration = []
    test = []
    success = []
    failed = []
    id_labels = []
    ood_labels = []
    offset = 0
    rollout_idx = 0
    episode_keys = []

    def get_ep_task_key(ep, split_name):
        if "seen" in split_name:
            summary = in_domain_summaries[ep]
            return (summary["suite"], int(summary["task_id"]))
        else:
            rows = ood_rows_by_ep[ep]
            return (rows[0]["suite"], int(rows[0]["task_id"]))

    for split in SPLITS:
        ep_ids = split_episodes[split]
        # Sort by task key
        ep_ids = sorted(ep_ids, key=lambda ep: get_ep_task_key(ep, split))
        print(f"\nProcessing split {split} (episodes: {len(ep_ids)})", flush=True)
        
        current_task_key = None
        env = None
        
        for idx, ep_id in enumerate(ep_ids):
            task_key = get_ep_task_key(ep_id, split)
            print(f"Episode {idx+1}/{len(ep_ids)}: {ep_id} (Task key: {task_key})", flush=True)
            starts.append(offset)
            episode_keys.append(ep_id)

            cache_file = CACHE_DIR / f"{split}_{ep_id}.pkl"
            if cache_file.exists():
                try:
                    with open(cache_file, "rb") as f:
                        cache_data = pickle.load(f)
                    episode_obs = cache_data["obs"]
                    episode_actions = cache_data["actions"]
                    print(f"Episode {idx+1}/{len(ep_ids)}: {ep_id} (Loaded from cache)", flush=True)
                    all_obs.extend(episode_obs)
                    all_actions.extend(episode_actions)
                    offset += len(episode_obs)
                    ends.append(offset)
                    
                    is_success = "success" in split
                    is_ood = "ood" in split
                    success.append(is_success)
                    failed.append(not is_success)
                    id_labels.append(not is_ood)
                    ood_labels.append(is_ood)
                    calibration.append(split == "success_calib_seen")
                    test.append(is_ood)
                    rollout_idx += 1
                    continue
                except Exception as e:
                    print(f"Cache load failed for {ep_id}: {e}. Reprocessing...", flush=True)

            episode_obs = []
            episode_actions = []

            is_in_domain = "seen" in split
            if is_in_domain:
                # In-domain: Reconstruct from simulator rollout
                summary = in_domain_summaries[ep_id]
                npz_path = summary["npz_path"]
                npz_data = np.load(npz_path, allow_pickle=True)
                executed_actions = npz_data["executed_actions"]
                query_timesteps = npz_data["query_timesteps"]
                query_proprio = npz_data["query_proprio"]
                main_chunks_normalized = npz_data["main_chunks_normalized"]
                ace_chunks_normalized = npz_data["ace_chunks_normalized"]

                # Parse metadata JSON
                metadata_path = summary["metadata_path"]
                with open(metadata_path) as f:
                    meta = json.load(f)
                bddl_rel = meta["episode"]["bddl_relative_path"]
                init_rel = meta["episode"]["init_state_file_relative_path"]
                initial_state_index = meta["episode"]["initial_state_index"]
                task_id = meta["episode"]["task_id"]
                suite = meta["episode"]["task_suite_name"]
                task_instruction = meta["task_instruction"]

                bundle_root = Path("/home/dean/fiper_goal_object_collection_20260605/libero_goal_object_reproduction_bundle_20260605")
                bddl_path = bundle_root / bddl_rel
                init_path = bundle_root / init_rel

                # Check task switch
                if task_key != current_task_key or env is None:
                    if env is not None:
                        env.close()
                    print(f"Creating environment for {suite} task {task_id}...", flush=True)
                    env = OffScreenRenderEnv(
                        bddl_file_name=str(bddl_path),
                        camera_heights=384,
                        camera_widths=384,
                    )
                    env.seed(42)
                    current_task_key = task_key
                    init_states = torch.load(init_path, map_location="cpu")
                
                obs = env.reset()
                env.set_init_state(init_states[initial_state_index])

                # Warmup: 10 steps
                for _ in range(10):
                    obs, _, _, _ = env.step(np.array([0, 0, 0, 0, 0, 0, -1], dtype=np.float32))

                episode_images = []
                for t in range(len(executed_actions)):
                    if t % 10 == 0:
                        obs_data = env.env._get_observations()
                        before_img, before_wrist = obs_images(obs_data)

                        # Match proprio for verification
                        env_proprio = obs_to_proprio(obs_data)
                        ref_proprio = query_proprio[t // 10]
                        dist = np.max(np.abs(env_proprio - ref_proprio))
                        if dist > 1e-3:
                            print(f"Proprio mismatch at t={t} ep={ep_id} dist={dist:.6f}", flush=True)

                        img_t, mask_t = image_preprocessor(before_img, before_wrist, device)
                        episode_images.append(img_t)

                        main_chunk = main_chunks_normalized[t // 10]
                        ace_chunk = ace_chunks_normalized[t // 10]
                        if len(ace_chunk) < 8:
                            ace_chunk = list(ace_chunk) + [main_chunk] * (8 - len(ace_chunk))
                        elif len(ace_chunk) > 8:
                            ace_chunk = ace_chunk[:8]
                        action_preds = np.asarray([main_chunk] + list(ace_chunk), dtype=np.float32)
                        episode_actions.append(action_preds)

                    obs, _, _, _ = env.step(executed_actions[t])

                episode_obs.extend(encode_vlm_features(model, processor, episode_images, task_instruction, device))

            else:
                # OOD: Reconstruct using saved state NPZs
                rows = ood_rows_by_ep[ep_id]
                
                suite = rows[0]["suite"]
                task_id = int(rows[0]["task_id"])
                
                # Check task switch
                if task_key != current_task_key or env is None:
                    if env is not None:
                        env.close()
                    bench = benchmark_dict[suite]()
                    task = bench.get_task(task_id)
                    bddl_root = OOD_BDDL_ROOT
                    folder_candidates = [task.problem_folder]
                    if task.problem_folder == "libero_goal_object_ood":
                        folder_candidates.append("libero_goal_object_ood_temp")
                    if task.problem_folder == "libero_spatial_object":
                        folder_candidates.append("libero_spatial")
                    bddl_p = None
                    for folder in folder_candidates:
                        candidate = bddl_root / folder / task.bddl_file
                        if candidate.exists():
                            bddl_p = candidate
                            break
                    if bddl_p is None:
                        raise FileNotFoundError(f"could not resolve BDDL files for {suite} task {task_id}")
                    
                    print(f"Creating environment for OOD {suite} task {task_id}...", flush=True)
                    env = OffScreenRenderEnv(
                        bddl_file_name=str(bddl_p),
                        camera_heights=384,
                        camera_widths=384,
                    )
                    env.seed(42)
                    current_task_key = task_key
                
                episode_images = []
                for row in rows:
                    task_instruction = row["task_instruction"]
                    sim_state_path = row["current"]["sim_state_path"]
                    filename = os.path.basename(sim_state_path)
                    local_state_path = OOD_ROOT / "states" / filename

                    npz = np.load(local_state_path, allow_pickle=True)
                    state_dict = {
                        "kind": str(npz["kind"]),
                        "flat": npz["flat"],
                        "env_runtime": None,
                        "sim_runtime": None,
                    }
                    set_state(env, state_dict, hard_reset=False)

                    obs_data = env.env._get_observations()
                    before_img, before_wrist = obs_images(obs_data)
                    img_t, mask_t = image_preprocessor(before_img, before_wrist, device)
                    episode_images.append(img_t)

                    main_chunk = row["main_candidate_action_chunk_normalized"]
                    ace_chunk = row["ace_candidate_chunks_normalized"]
                    if len(ace_chunk) < 8:
                        ace_chunk = list(ace_chunk) + [main_chunk] * (8 - len(ace_chunk))
                    elif len(ace_chunk) > 8:
                        ace_chunk = ace_chunk[:8]
                    action_preds = np.asarray([main_chunk] + list(ace_chunk), dtype=np.float32)
                    episode_actions.append(action_preds)

                episode_obs.extend(encode_vlm_features(model, processor, episode_images, task_instruction, device))

            assert len(episode_obs) > 0
            # Save to cache
            CACHE_DIR.mkdir(parents=True, exist_ok=True)
            with open(cache_file, "wb") as f:
                pickle.dump({"obs": episode_obs, "actions": episode_actions}, f)

            all_obs.extend(episode_obs)
            all_actions.extend(episode_actions)
            offset += len(episode_obs)
            ends.append(offset)

            # Metadata properties for this rollout
            is_success = "success" in split
            is_ood = "ood" in split
            success.append(is_success)
            failed.append(not is_success)
            id_labels.append(not is_ood)
            ood_labels.append(is_ood)
            calibration.append(split == "success_calib_seen")
            test.append(is_ood)  # test set for our offline ablation is strictly OOD
            rollout_idx += 1

        if env is not None:
            env.close()

    # Save materialized files to official_fiper_data/libero_fold00/processed_rollouts/
    out_dir = DATA_ROOT / "libero_fold00" / "processed_rollouts"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    stacked_obs = torch.tensor(np.asarray(all_obs, dtype=np.float32))
    stacked_actions = torch.tensor(np.asarray(all_actions, dtype=np.float32))
    metadata = {
        "episode_start_indices": np.asarray(starts, dtype=np.int64),
        "episode_end_indices": np.asarray(ends, dtype=np.int64),
        "calibration_rollout_labels": np.asarray(calibration, dtype=bool),
        "test_rollout_labels": np.asarray(test, dtype=bool),
        "successful_rollout_labels": np.asarray(success, dtype=bool),
        "failed_rollout_labels": np.asarray(failed, dtype=bool),
        "id_rollout_labels": np.asarray(id_labels, dtype=bool),
        "ood_rollout_labels": np.asarray(ood_labels, dtype=bool),
        "num_steps": int(offset),
        "num_rollouts": int(rollout_idx),
        "episode_lengths": np.asarray(ends, dtype=np.int64) - np.asarray(starts, dtype=np.int64),
        "num_robots": 1,
        "actions": {
            "action_dim": 7,
            "action_mapping": {"position": [0, 1, 2], "rotation": [3, 4, 5], "gripper": [6]},
        },
        "available_tensors": ["action_preds", "obs_embeddings"],
        "episode_keys": episode_keys,
    }
    torch.save(stacked_obs, out_dir / "obs_embeddings.pt")
    torch.save(stacked_actions, out_dir / "action_preds.pt")
    with (out_dir / "metadata.pkl").open("wb") as f:
        pickle.dump(metadata, f)

    print("\nDataset Materialization Completed Successfully!", flush=True)
    print(f"Saved to {out_dir}", flush=True)
    print(f"Tensors shape: obs={stacked_obs.shape}, actions={stacked_actions.shape}", flush=True)
    print(f"Num rollouts: {metadata['num_rollouts']}, Num steps: {metadata['num_steps']}", flush=True)
    print(f"Calibration successes: {metadata['calibration_rollout_labels'].sum()}", flush=True)
    print(f"Test episodes (OOD): {metadata['test_rollout_labels'].sum()}", flush=True)

if __name__ == "__main__":
    main()
