import argparse
import json
import os
import pickle
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import torch
from PIL import Image

sys.path.append("/home/redafrix/SimVLA_modified")
sys.path.append("/home/redafrix/LIBERO-PRO")
sys.path.append("/home/dean/fiper_uncertainty_collection/src/data_collection_stage9")

from libero.libero import benchmark, get_libero_path
from libero.libero.envs import OffScreenRenderEnv
from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor
from sim_state_utils import set_state

BASE_DIR = Path("/home/dean/fiper_uncertainty_collection")
EXP_DIR = BASE_DIR / "experiments" / "official_fiper_rndoe_entropy_fold00_20260622"
REFS_DIR = (
    BASE_DIR
    / "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/"
    / "fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs"
)
SHARD_DIR = EXP_DIR / "materialized_shards"
DATA_ROOT = EXP_DIR / "official_fiper_data"
MIRROR_DIR = BASE_DIR / "data" / "states_mirror_sharded"
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


def obs_images(obs: dict):
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
    
    # 1. Start with problem_folder and known aliases
    folder_candidates = [task.problem_folder]
    if task.problem_folder == "libero_goal_object_ood":
        folder_candidates.append("libero_goal_object_ood_temp")
    if task.problem_folder == "libero_spatial_object":
        folder_candidates.append("libero_spatial")
    if task.problem_folder == "libero_object_env":
        folder_candidates.append("libero_object")
    if task.problem_folder == "libero_object_object":
        folder_candidates.append("libero_object_object")

    # 2. Try to find the file in candidates
    bddl_path = None
    for folder in folder_candidates:
        candidate = bddl_root / folder / task.bddl_file
        if candidate.exists():
            bddl_path = candidate
            break

    # 3. Recursive search if not found
    if bddl_path is None:
        print(f"[Resolver] Direct search failed for {suite} task {task_id}. Searching recursively under {bddl_root} for {task.bddl_file}...")
        recursive_matches = list(bddl_root.glob(f"**/{task.bddl_file}"))
        if recursive_matches:
            matches_str = [str(p) for p in recursive_matches]
            print(f"[Resolver] Found {len(recursive_matches)} recursive matches: {matches_str}")
            
            best_match = None
            best_score = -1
            for match in recursive_matches:
                match_dir = match.parent.name
                if match_dir in folder_candidates:
                    score = 100 - folder_candidates.index(match_dir)
                elif match_dir.startswith(task.problem_folder) or task.problem_folder.startswith(match_dir):
                    score = 10
                else:
                    score = 0
                if score > best_score:
                    best_score = score
                    best_match = match
            
            if best_match:
                bddl_path = best_match
                print(f"[Resolver] Selected best match: {bddl_path} (score={best_score})")
            else:
                bddl_path = recursive_matches[0]
                print(f"[Resolver] Selected fallback match: {bddl_path}")

    # 4. If still not found, raise Error
    if bddl_path is None:
        checked_candidates = [str(bddl_root / f / task.bddl_file) for f in folder_candidates]
        raise FileNotFoundError(
            f"could not resolve BDDL files for {suite} task {task_id}.\n"
            f"BDDL Filename: {task.bddl_file}\n"
            f"Checked direct candidates:\n" + "\n".join(checked_candidates) + "\n"
            f"Recursive search under {bddl_root} returned no matches."
        )

    print(f"[Resolver] Successfully resolved BDDL path: {bddl_path}")
    env = OffScreenRenderEnv(
        bddl_file_name=str(bddl_path),
        camera_heights=int(resolution),
        camera_widths=int(resolution),
    )
    env.seed(42)
    return env


def load_split_rows():
    all_split_rows = {}
    episodes_map = {}
    for split in SPLITS:
        rows = []
        with (REFS_DIR / f"{split}.rows.jsonl").open() as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                rows.append(row)
        all_split_rows[split] = rows
        for idx, row in enumerate(rows):
            episodes_map.setdefault(row["episode_key"], []).append((split, idx, row))
    return all_split_rows, episodes_map, list(episodes_map.keys())


def shard_path(start_batch: int, end_batch: int) -> Path:
    return SHARD_DIR / f"shard_batches_{start_batch:04d}_{end_batch:04d}.pt"


def run_shard(args):
    os.environ["MUJOCO_GL"] = "egl"
    os.environ["PYOPENGL_PLATFORM"] = "egl"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    SHARD_DIR.mkdir(parents=True, exist_ok=True)
    out_path = shard_path(args.start_batch, args.end_batch)
    if out_path.exists() and not args.overwrite:
        print(f"[skip] shard exists: {out_path}", flush=True)
        return

    all_split_rows, episodes_map, episodes_list = load_split_rows()
    total_batches = (len(episodes_list) - 1) // args.batch_size + 1
    if args.start_batch < 0 or args.end_batch >= total_batches or args.start_batch > args.end_batch:
        raise ValueError(f"invalid batch range {args.start_batch}..{args.end_batch}; total_batches={total_batches}")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}", flush=True)
    print("Loading VLA model...", flush=True)
    model = SmolVLMVLA.from_pretrained("/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000").to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained("HuggingFaceTB/SmolVLM-500M-Instruct")
    image_preprocessor = ImagePreprocessor(384)
    benchmark_dict = benchmark.get_benchmark_dict()

    shard = {
        "start_batch": args.start_batch,
        "end_batch": args.end_batch,
        "batch_size": args.batch_size,
        "split_indices": {split: [] for split in SPLITS},
        "obs_embeddings": {split: [] for split in SPLITS},
        "action_preds": {split: [] for split in SPLITS},
    }

    env_cache = {}
    MIRROR_DIR.mkdir(parents=True, exist_ok=True)

    try:
        for batch_no in range(args.start_batch, args.end_batch + 1):
            start = batch_no * args.batch_size
            batch_eps = episodes_list[start : start + args.batch_size]
            print(f"\nProcessing batch {batch_no + 1}/{total_batches} (episodes: {len(batch_eps)})", flush=True)

            batch_rows = []
            files_to_copy = set()
            src_lines_needed = {}
            for ep_key in batch_eps:
                for split, idx, row in episodes_map[ep_key]:
                    src = row["source_jsonl"]
                    line_idx = int(row["line_no"]) - 1
                    src_lines_needed.setdefault(src, {}).setdefault(line_idx, []).append((split, idx, row))

            for src, line_map in src_lines_needed.items():
                with (BASE_DIR / src).open() as f:
                    for f_idx, line in enumerate(f):
                        if f_idx in line_map:
                            source_row = json.loads(line)
                            for split, idx, row in line_map[f_idx]:
                                batch_rows.append((split, idx, row, source_row))
                                files_to_copy.add(source_row["current"]["sim_state_path"])

            temp_list_path = BASE_DIR / f"temp_rsync_list_shard_{os.getpid()}.txt"
            with temp_list_path.open("w") as f:
                for p in sorted(files_to_copy):
                    f.write(p.lstrip("/") + "\n")
            print(f"Rsyncing {len(files_to_copy)} state files from Bob and Sam...", flush=True)
            res_bob = subprocess.run(
                ["rsync", "-a", "--ignore-missing-args", f"--files-from={temp_list_path}", "bob:/", str(MIRROR_DIR) + "/"],
                capture_output=True,
                text=True,
            )
            res_sam = subprocess.run(
                ["rsync", "-a", "--ignore-missing-args", f"--files-from={temp_list_path}", "sam:/", str(MIRROR_DIR) + "/"],
                capture_output=True,
                text=True,
            )
            temp_list_path.unlink(missing_ok=True)
            
            missing_files = []
            for p in files_to_copy:
                local_path = MIRROR_DIR / p.lstrip("/")
                if not local_path.exists():
                    missing_files.append(p)
            
            if missing_files:
                print(f"ERROR: Failed to copy {len(missing_files)} state files from Bob and Sam! Missing files:\n" + "\n".join(missing_files), flush=True)
                print("Bob stdout:", res_bob.stdout, flush=True)
                print("Bob stderr:", res_bob.stderr, flush=True)
                print("Sam stdout:", res_sam.stdout, flush=True)
                print("Sam stderr:", res_sam.stderr, flush=True)
                raise RuntimeError("rsync state transfer failed")
            
            print(f"Successfully transferred all {len(files_to_copy)} state files.", flush=True)

            task_groups = {}
            for item in batch_rows:
                split, _idx, row, _source_row = item
                task_groups.setdefault((row["suite"], int(row["task_id"])), []).append(item)

            for (suite, task_id), items in task_groups.items():
                env_key = (suite, task_id)
                if env_key not in env_cache:
                    print(f"Initializing OffScreenRenderEnv for {suite} task {task_id}...", flush=True)
                    env = make_env(benchmark_dict, suite, task_id, 384)
                    env.reset()
                    env_cache[env_key] = env
                env = env_cache[env_key]

                for split, idx, row, source_row in items:
                    local_state_path = MIRROR_DIR / source_row["current"]["sim_state_path"].lstrip("/")
                    npz = np.load(local_state_path, allow_pickle=True)
                    state_dict = {
                        "kind": str(npz["kind"]),
                        "flat": npz["flat"],
                        "env_runtime": None,
                        "sim_runtime": None,
                    }
                    set_state(env, state_dict, hard_reset=False)
                    obs = env.env._get_observations()
                    before_img, before_wrist = obs_images(obs)
                    images_t, mask_t = image_preprocessor(before_img, before_wrist, device)
                    lang_t = processor.encode_language([row["task_instruction"]])
                    input_ids = lang_t["input_ids"].to(device)
                    with torch.inference_mode():
                        enc = model.forward_vlm_efficient(images_t, mask_t, input_ids)
                    vlm_feat = enc["vlm_features"].mean(dim=1).squeeze(0).cpu().numpy().astype(np.float32)

                    main_chunk = source_row["main_candidate_action_chunk_normalized"]
                    ace_chunks = source_row["ace_candidate_chunks_normalized"]
                    if len(ace_chunks) < 8:
                        ace_chunks = list(ace_chunks) + [main_chunk] * (8 - len(ace_chunks))
                    elif len(ace_chunks) > 8:
                        ace_chunks = ace_chunks[:8]
                    action_preds = np.asarray([main_chunk] + list(ace_chunks), dtype=np.float32)

                    shard["split_indices"][split].append(idx)
                    shard["obs_embeddings"][split].append(vlm_feat)
                    shard["action_preds"][split].append(action_preds)

            shutil.rmtree(MIRROR_DIR, ignore_errors=True)
            MIRROR_DIR.mkdir(parents=True, exist_ok=True)
    finally:
        shutil.rmtree(MIRROR_DIR, ignore_errors=True)

    for split in SPLITS:
        shard["split_indices"][split] = np.asarray(shard["split_indices"][split], dtype=np.int64)
        shard["obs_embeddings"][split] = np.asarray(shard["obs_embeddings"][split], dtype=np.float32)
        shard["action_preds"][split] = np.asarray(shard["action_preds"][split], dtype=np.float32)
    tmp_path = out_path.with_suffix(".tmp")
    torch.save(shard, tmp_path)
    tmp_path.replace(out_path)
    print(f"[done] wrote {out_path}", flush=True)


def backup_existing_processed(task_out_dir: Path):
    if not task_out_dir.exists():
        return
    marker = task_out_dir / "metadata.pkl"
    if not marker.exists():
        return
    backup = task_out_dir.parent / f"processed_rollouts_backup_before_sharded_{os.getpid()}"
    if backup.exists():
        shutil.rmtree(backup)
    shutil.move(str(task_out_dir), str(backup))
    print(f"Backed up existing processed_rollouts to {backup}", flush=True)


def merge_shards(args):
    all_split_rows, _episodes_map, _episodes_list = load_split_rows()
    obs_by_split = {split: np.zeros((len(rows), 960), dtype=np.float32) for split, rows in all_split_rows.items()}
    action_by_split = {split: np.zeros((len(rows), 9, 10, 7), dtype=np.float32) for split, rows in all_split_rows.items()}
    seen = {split: np.zeros((len(rows),), dtype=bool) for split, rows in all_split_rows.items()}
    shard_files = sorted(SHARD_DIR.glob("shard_batches_*.pt"))
    if not shard_files:
        raise RuntimeError(f"no shard files found in {SHARD_DIR}")
    print(f"Merging {len(shard_files)} shard files", flush=True)
    for path in shard_files:
        shard = torch.load(path, map_location="cpu", weights_only=False)
        for split in SPLITS:
            idxs = np.asarray(shard["split_indices"][split], dtype=np.int64)
            if idxs.size == 0:
                continue
            if seen[split][idxs].any():
                raise RuntimeError(f"duplicate split indices in {path} split={split}")
            obs = np.asarray(shard["obs_embeddings"][split], dtype=np.float32)
            act = np.asarray(shard["action_preds"][split], dtype=np.float32)
            if obs.shape != (len(idxs), 960):
                raise RuntimeError(f"bad obs shape {obs.shape} in {path} split={split}")
            if act.shape != (len(idxs), 9, 10, 7):
                raise RuntimeError(f"bad action shape {act.shape} in {path} split={split}")
            obs_by_split[split][idxs] = obs
            action_by_split[split][idxs] = act
            seen[split][idxs] = True

    missing = {split: int((~mask).sum()) for split, mask in seen.items()}
    if any(missing.values()):
        raise RuntimeError(f"cannot merge incomplete shards; missing rows: {missing}")

    for split in SPLITS:
        if not np.isfinite(obs_by_split[split]).all():
            raise RuntimeError(f"non-finite obs in {split}")
        if not np.isfinite(action_by_split[split]).all():
            raise RuntimeError(f"non-finite actions in {split}")

    for task_name in ["libero_fold00", "libero_fold00_hygiene"]:
        task_out_dir = DATA_ROOT / task_name / "processed_rollouts"
        backup_existing_processed(task_out_dir)
        task_out_dir.mkdir(parents=True, exist_ok=True)

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

        for split in SPLITS:
            ep_rows = {}
            for r_idx, row in enumerate(all_split_rows[split]):
                ep_rows.setdefault(row["episode_key"], []).append((r_idx, row))
            for ep_key, items in ep_rows.items():
                items.sort(key=lambda x: x[1]["timestep"])
                starts.append(offset)
                episode_keys.append(ep_key)
                for r_idx, _row in items:
                    all_obs.append(obs_by_split[split][r_idx])
                    all_actions.append(action_by_split[split][r_idx])
                offset += len(items)
                ends.append(offset)
                is_success = "success" in split
                is_ood = "ood" in split
                success.append(is_success)
                failed.append(not is_success)
                id_labels.append(not is_ood)
                ood_labels.append(is_ood)
                if task_name == "libero_fold00":
                    is_calib = split == "success_calib_seen"
                    is_test = split in ["success_test_seen", "success_test_ood", "failure_test_seen", "failure_eval_ood"]
                else:
                    is_calib = split == "success_train_seen"
                    is_test = split in ["success_test_seen", "success_test_ood", "failure_test_seen", "failure_eval_ood"]
                calibration.append(is_calib)
                test.append(is_test)
                rollout_idx += 1

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
        torch.save(stacked_obs, task_out_dir / "obs_embeddings.pt")
        torch.save(stacked_actions, task_out_dir / "action_preds.pt")
        with (task_out_dir / "metadata.pkl").open("wb") as f:
            pickle.dump(metadata, f)
        print(
            f"Saved {task_name}: obs={tuple(stacked_obs.shape)} actions={tuple(stacked_actions.shape)} "
            f"rollouts={metadata['num_rollouts']} steps={metadata['num_steps']} "
            f"calib={int(metadata['calibration_rollout_labels'].sum())} test={int(metadata['test_rollout_labels'].sum())}",
            flush=True,
        )


def validate():
    for task_name in ["libero_fold00", "libero_fold00_hygiene"]:
        task_out_dir = DATA_ROOT / task_name / "processed_rollouts"
        obs = torch.load(task_out_dir / "obs_embeddings.pt", map_location="cpu", weights_only=False)
        act = torch.load(task_out_dir / "action_preds.pt", map_location="cpu", weights_only=False)
        with (task_out_dir / "metadata.pkl").open("rb") as f:
            metadata = pickle.load(f)
        print(f"\n{task_name}", flush=True)
        print(f"obs_embeddings {tuple(obs.shape)} action_preds {tuple(act.shape)}", flush=True)
        print(
            "rollouts", metadata["num_rollouts"],
            "steps", metadata["num_steps"],
            "calib", int(metadata["calibration_rollout_labels"].sum()),
            "test", int(metadata["test_rollout_labels"].sum()),
            "success", int(metadata["successful_rollout_labels"].sum()),
            "failed", int(metadata["failed_rollout_labels"].sum()),
            "id", int(metadata["id_rollout_labels"].sum()),
            "ood", int(metadata["ood_rollout_labels"].sum()),
            flush=True,
        )
        assert obs.shape == (metadata["num_steps"], 960)
        assert act.shape == (metadata["num_steps"], 9, 10, 7)
        assert torch.isfinite(obs).all()
        assert torch.isfinite(act).all()
        assert metadata["available_tensors"] == ["action_preds", "obs_embeddings"]
        starts = metadata["episode_start_indices"]
        ends = metadata["episode_end_indices"]
        assert len(starts) == metadata["num_rollouts"]
        assert len(ends) == metadata["num_rollouts"]
        assert starts[0] == 0
        assert ends[-1] == metadata["num_steps"]
        assert np.all(ends > starts)
        assert np.all(starts[1:] == ends[:-1])
    print("\nVALIDATION_PASS", flush=True)


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="mode", required=True)
    shard = sub.add_parser("shard")
    shard.add_argument("--start-batch", type=int, required=True)
    shard.add_argument("--end-batch", type=int, required=True)
    shard.add_argument("--batch-size", type=int, default=10)
    shard.add_argument("--overwrite", action="store_true")
    sub.add_parser("merge")
    sub.add_parser("validate")
    args = parser.parse_args()
    if args.mode == "shard":
        run_shard(args)
    elif args.mode == "merge":
        merge_shards(args)
    elif args.mode == "validate":
        validate()


if __name__ == "__main__":
    main()
