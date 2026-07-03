import os
import sys
import json
import pickle
import argparse
import subprocess
import shutil
from pathlib import Path
import torch
import numpy as np
from PIL import Image

# Add SimVLA and LIBERO-PRO to import path
sys.path.append("/home/redafrix/SimVLA_modified")
sys.path.append("/home/redafrix/LIBERO-PRO")
sys.path.append("/home/dean/fiper_uncertainty_collection/src/data_collection_stage9")

from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor
from libero.libero import benchmark, get_libero_path
from libero.libero.envs import OffScreenRenderEnv
from sim_state_utils import set_state

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

    def __call__(self, image0: np.ndarray, image1: np.ndarray, device: torch.device) -> tuple[torch.Tensor, torch.Tensor]:
        img0 = self._to_tensor(image0)
        img1 = self._to_tensor(image1)
        pad = torch.zeros_like(img0)
        images = torch.stack([img0, img1, pad], dim=0).unsqueeze(0).to(device)
        image_mask = torch.tensor([[True, True, False]], device=device)
        return images, image_mask

def obs_images(obs: dict) -> tuple[np.ndarray, np.ndarray]:
    img = obs.get("agentview_image")
    wrist = obs.get("robot0_eye_in_hand_image")
    if img is None:
        img = np.zeros((128, 128, 3), dtype=np.uint8)
    if wrist is None:
        wrist = np.zeros_like(img)
    return np.ascontiguousarray(img[::-1, ::-1]), np.ascontiguousarray(wrist[::-1, ::-1])

def make_env(benchmark_dict, suite, task_id, resolution):
    bench = benchmark_dict[suite]()
    task = bench.get_task(task_id)
    bddl_root = Path(get_libero_path("bddl_files"))
    folder_candidates = [task.problem_folder]
    if task.problem_folder == "libero_goal_object_ood":
        folder_candidates.append("libero_goal_object_ood_temp")
    if task.problem_folder == "libero_spatial_object":
        folder_candidates.append("libero_spatial")
        
    bddl_path = None
    for folder in folder_candidates:
        candidate_bddl = bddl_root / folder / task.bddl_file
        if candidate_bddl.exists():
            bddl_path = candidate_bddl
            break
            
    if bddl_path is None:
        raise FileNotFoundError(f"could not resolve BDDL files for {suite} task {task_id}")
        
    env_args = {
        "bddl_file_name": str(bddl_path),
        "camera_heights": int(resolution),
        "camera_widths": int(resolution),
    }
    env = OffScreenRenderEnv(**env_args)
    env.seed(42)
    return env

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true", help="Run in smoke test mode on a small subset")
    args = parser.parse_args()
    
    # Configure environment
    os.environ["MUJOCO_GL"] = "egl"
    os.environ["PYOPENGL_PLATFORM"] = "egl"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}", flush=True)
    
    # Load model and processor
    checkpoint = "/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000"
    print(f"Loading VLA model from {checkpoint}...", flush=True)
    model = SmolVLMVLA.from_pretrained(checkpoint).to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained("HuggingFaceTB/SmolVLM-500M-Instruct")
    image_preprocessor = ImagePreprocessor(384)
    
    benchmark_dict = benchmark.get_benchmark_dict()
    
    refs_dir = Path("/home/dean/fiper_uncertainty_collection/experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs")
    base_dir = Path("/home/dean/fiper_uncertainty_collection")
    mirror_dir = base_dir / "data" / "states_mirror"
    mirror_dir.mkdir(parents=True, exist_ok=True)
    
    splits = [
        "success_train_seen",
        "success_calib_seen",
        "success_test_seen",
        "success_test_ood",
        "failure_test_seen",
        "failure_eval_ood"
    ]
    
    # 1. Parse splits and row mappings
    all_split_rows = {}
    total_rows = 0
    unique_episodes = set()
    
    for split in splits:
        ref_path = refs_dir / f"{split}.rows.jsonl"
        print(f"Loading split reference: {ref_path.name}...", flush=True)
        rows = []
        with ref_path.open() as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                rows.append(row)
                unique_episodes.add(row["episode_key"])
                
        if args.smoke:
            # Smoke test: pick 1 episode
            first_ep = rows[0]["episode_key"]
            rows = [r for r in rows if r["episode_key"] == first_ep]
            print(f"Smoke test split {split} restricted to episode {first_ep} ({len(rows)} rows)", flush=True)
            
        all_split_rows[split] = rows
        total_rows += len(rows)
        
    print(f"Total rows to process: {total_rows}", flush=True)
    print(f"Total unique episodes: {len(unique_episodes)}", flush=True)
    
    # Pre-allocate output buffers
    obs_embeddings_by_split = {split: np.zeros((len(rows), 960), dtype=np.float32) for split, rows in all_split_rows.items()}
    action_preds_by_split = {split: np.zeros((len(rows), 9, 10, 7), dtype=np.float32) for split, rows in all_split_rows.items()}
    
    # Track the global step index for each split to write back processed steps
    split_counters = {split: 0 for split in splits}
    
    # Group processing by episode to copy state files
    # Create mapping of episode_key -> list of (split_name, split_idx, ref_row)
    episodes_map = {}
    for split, rows in all_split_rows.items():
        for idx, row in enumerate(rows):
            episodes_map.setdefault(row["episode_key"], []).append((split, idx, row))
            
    episodes_list = list(episodes_map.keys())
    print(f"Grouping into {len(episodes_list)} episodes for chunked transfer.", flush=True)
    
    env_cache = {}
    
    # Process episodes in batches (e.g. 10 episodes at a time)
    batch_size = 10 if not args.smoke else 1
    for b_idx in range(0, len(episodes_list), batch_size):
        batch_eps = episodes_list[b_idx:b_idx+batch_size]
        print(f"\nProcessing batch {b_idx // batch_size + 1}/{(len(episodes_list) - 1) // batch_size + 1} (episodes: {len(batch_eps)})", flush=True)
        
        # A. Collect required state files and rows for this batch
        batch_rows = [] # list of (split, idx, ref_row, source_row)
        files_to_copy = set()
        
        # Load the source jsonl lines
        # Group by source_jsonl to open files once
        src_lines_needed = {}
        for ep_key in batch_eps:
            for split, idx, row in episodes_map[ep_key]:
                src = row["source_jsonl"]
                line_idx = int(row["line_no"]) - 1
                src_lines_needed.setdefault(src, {}).setdefault(line_idx, []).append((split, idx, row))
                
        for src, line_map in src_lines_needed.items():
            src_path = base_dir / src
            with src_path.open() as f:
                for f_idx, line in enumerate(f):
                    if f_idx in line_map:
                        source_row = json.loads(line)
                        for split, idx, row in line_map[f_idx]:
                            batch_rows.append((split, idx, row, source_row))
                            files_to_copy.add(source_row["current"]["sim_state_path"])
                            
        # B. Sync state files from Bob to local states_mirror
        # Write files list (relative to root)
        temp_list_path = base_dir / "temp_rsync_list.txt"
        with temp_list_path.open("w") as f:
            for p in sorted(files_to_copy):
                # Remove leading slash
                f.write(p.lstrip("/") + "\n")
                
        print(f"Rsyncing {len(files_to_copy)} state files from Bob...", flush=True)
        # Run rsync command
        cmd = [
            "rsync", "-a",
            f"--files-from={temp_list_path}",
            "bob:/",
            str(mirror_dir) + "/"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print("Rsync failed!", flush=True)
            print("Stdout:", res.stdout, flush=True)
            print("Stderr:", res.stderr, flush=True)
            raise RuntimeError("rsync state transfer failed")
            
        # Remove temp list
        temp_list_path.unlink()
        
        # C. Reconstruct embeddings for each row
        # Group by (suite, task_id) to reuse environment
        task_groups = {}
        for item in batch_rows:
            split, idx, row, source_row = item
            suite = row["suite"]
            task_id = int(row["task_id"])
            task_groups.setdefault((suite, task_id), []).append(item)
            
        for (suite, task_id), items in task_groups.items():
            # Get env
            env_key = (suite, task_id)
            if env_key not in env_cache:
                print(f"Initializing OffScreenRenderEnv for {suite} task {task_id}...", flush=True)
                env = make_env(benchmark_dict, suite, task_id, 384)
                env.reset()
                env_cache[env_key] = env
            env = env_cache[env_key]
            
            # Reconstruct states
            for split, idx, row, source_row in items:
                # Load local path of state
                orig_state_path = source_row["current"]["sim_state_path"]
                local_state_path = mirror_dir / orig_state_path.lstrip("/")
                
                # Reconstruct MuJoCo state dictionary
                # The state was saved as npz compressed
                npz = np.load(local_state_path, allow_pickle=True)
                
                state_dict = {
                    "kind": str(npz["kind"]),
                    "flat": npz["flat"],
                    "env_runtime": None,
                    "sim_runtime": None
                }
                        
                # Set environment state
                set_state(env, state_dict, hard_reset=False)
                
                # Render cameras
                obs = env.env._get_observations()
                before_img, before_wrist = obs_images(obs)
                
                # Prepare image inputs
                images_t, mask_t = image_preprocessor(before_img, before_wrist, device)
                lang = row["task_instruction"]
                lang_t = processor.encode_language([lang])
                input_ids = lang_t["input_ids"].to(device)
                
                # Run VLM forward to get embedding
                with torch.inference_mode():
                    enc = model.forward_vlm_efficient(images_t, mask_t, input_ids)
                    
                # Mean-pool along sequence dimension (dim 1)
                vlm_feat = enc["vlm_features"].mean(dim=1).squeeze(0).cpu().numpy()
                obs_embeddings_by_split[split][idx] = vlm_feat
                
                # Materialize action_preds [9, 10, 7]
                main_chunk = source_row["main_candidate_action_chunk_normalized"]
                ace_chunks = source_row["ace_candidate_chunks_normalized"]
                
                # Verify and align number of chunks to 9 (1 main + 8 ACE)
                if len(ace_chunks) < 8:
                    print(f"Warning: episode {row['episode_key']} timestep {row['timestep']} has only {len(ace_chunks)} ACE chunks. Padding...", flush=True)
                    padded_ace = list(ace_chunks)
                    while len(padded_ace) < 8:
                        padded_ace.append(main_chunk)
                    ace_chunks = padded_ace
                elif len(ace_chunks) > 8:
                    ace_chunks = ace_chunks[:8]
                    
                action_preds = [main_chunk] + ace_chunks
                action_preds_by_split[split][idx] = np.array(action_preds, dtype=np.float32)
                
        # D. Delete rsync mirror folder to reclaim disk space
        shutil.rmtree(mirror_dir)
        mirror_dir.mkdir(parents=True, exist_ok=True)
        
    print("\nProcessing complete! Saving datasets...", flush=True)
    
    # 2. Write official processed rollout datasets
    # Two tasks: libero_fold00 and libero_fold00_hygiene
    # Both tasks have identical arrays, but different metadata split assignments!
    for task_name in ["libero_fold00", "libero_fold00_hygiene"]:
        task_out_dir = Path(f"/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622/official_fiper_data/{task_name}/processed_rollouts")
        task_out_dir.mkdir(parents=True, exist_ok=True)
        
        # Flatten all splits into a single continuous sequence of episodes
        # The FIPER dataset expects:
        # - episode_start_indices, episode_end_indices defining all episodes in the flat arrays
        # - boolean masks indicating which episode belongs to calibration/test/success/failure/id/ood
        
        all_obs_embeddings = []
        all_action_preds = []
        
        episode_start_indices = []
        episode_end_indices = []
        
        calibration_rollout_labels = []
        test_rollout_labels = []
        successful_rollout_labels = []
        failed_rollout_labels = []
        id_rollout_labels = []
        ood_rollout_labels = []
        
        current_step_offset = 0
        rollout_idx = 0
        
        # We will loop over splits and reconstruct the episode groups
        for split in splits:
            rows = all_split_rows[split]
            if not rows:
                continue
                
            # Group by episode_key
            ep_rows = {}
            for r_idx, r in enumerate(rows):
                ep_rows.setdefault(r["episode_key"], []).append((r_idx, r))
                
            for ep_key, item_list in ep_rows.items():
                # Sort by timestep to be safe
                item_list.sort(key=lambda x: x[1]["timestep"])
                ep_length = len(item_list)
                
                # Fetch arrays for this episode
                for r_idx, r in item_list:
                    all_obs_embeddings.append(obs_embeddings_by_split[split][r_idx])
                    all_action_preds.append(action_preds_by_split[split][r_idx])
                    
                episode_start_indices.append(current_step_offset)
                episode_end_indices.append(current_step_offset + ep_length)
                current_step_offset += ep_length
                
                # Determine labels for this episode
                # Success/Failure
                is_success = "success" in split
                successful_rollout_labels.append(is_success)
                failed_rollout_labels.append(not is_success)
                
                # ID/OOD
                is_ood = "ood" in split
                id_rollout_labels.append(not is_ood)
                ood_rollout_labels.append(is_ood)
                
                # Calibration/Test split labeling
                # For libero_fold00 (official semantics):
                # - calibration contains success_calib_seen
                # - test contains success_test_seen, success_test_ood, failure_test_seen, failure_eval_ood
                if task_name == "libero_fold00":
                    is_calib = (split == "success_calib_seen")
                    # Note: FIPER code will train on calibration, so train_seen is not included in calibration/test if we only calibrate on calib_seen
                    # To keep it consistent, we map:
                    # - train_seen is NOT used for testing (is_test = False) or calibration (is_calib = False) unless we evaluate it. Let's make it is_test = False, is_calib = False.
                    is_test = (split in ["success_test_seen", "success_test_ood", "failure_test_seen", "failure_eval_ood"])
                else:
                    # For libero_fold00_hygiene:
                    # - calibration contains success_train_seen (to train RND)
                    # - test contains success_test_seen, success_test_ood, failure_test_seen, failure_eval_ood
                    is_calib = (split == "success_train_seen")
                    is_test = (split in ["success_test_seen", "success_test_ood", "failure_test_seen", "failure_eval_ood"])
                    
                calibration_rollout_labels.append(is_calib)
                test_rollout_labels.append(is_test)
                
                rollout_idx += 1
                
        # Stack all tensors
        stacked_obs = torch.tensor(np.array(all_obs_embeddings, dtype=np.float32))
        stacked_actions = torch.tensor(np.array(all_action_preds, dtype=np.float32))
        
        # Save tensors
        torch.save(stacked_obs, task_out_dir / "obs_embeddings.pt")
        torch.save(stacked_actions, task_out_dir / "action_preds.pt")
        
        # Build metadata pkl
        metadata = {
            "episode_start_indices": np.array(episode_start_indices, dtype=np.int64),
            "episode_end_indices": np.array(episode_end_indices, dtype=np.int64),
            "calibration_rollout_labels": np.array(calibration_rollout_labels, dtype=bool),
            "test_rollout_labels": np.array(test_rollout_labels, dtype=bool),
            "successful_rollout_labels": np.array(successful_rollout_labels, dtype=bool),
            "failed_rollout_labels": np.array(failed_rollout_labels, dtype=bool),
            "id_rollout_labels": np.array(id_rollout_labels, dtype=bool),
            "ood_rollout_labels": np.array(ood_rollout_labels, dtype=bool),
            "num_steps": current_step_offset,
            "num_rollouts": rollout_idx,
            "episode_lengths": np.array(episode_end_indices, dtype=np.int64) - np.array(episode_start_indices, dtype=np.int64),
            "num_robots": 1,
            "actions": {
                "action_dim": 7,
                "action_mapping": {
                    "position": [0, 1, 2],
                    "rotation": [3, 4, 5],
                    "gripper": [6]
                }
            },
            "available_tensors": ["action_preds", "obs_embeddings"]
        }
        
        with (task_out_dir / "metadata.pkl").open("wb") as f:
            pickle.dump(metadata, f)
            
        print(f"Saved dataset for task {task_name}: steps={metadata['num_steps']}, rollouts={metadata['num_rollouts']}", flush=True)
        
    print("Done materializing all datasets!", flush=True)

if __name__ == "__main__":
    main()
