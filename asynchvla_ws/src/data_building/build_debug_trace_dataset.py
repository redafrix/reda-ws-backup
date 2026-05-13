#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

import torch

REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
SIMVLA_MODIFIED = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
CHECKPOINT = REDA_WS / "intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000"
LOCAL_BACKBONE = REDA_WS / "intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct"
LIBERO_ROOT = REDA_WS / "intern_ship_ws/assets/data/libero_datasets"
OUT_PATH = REDA_WS / "asynchvla_ws/data/debug/trace_debug.pt"
META_DIR = REDA_WS / "asynchvla_ws/data/debug/metas"

sys.path.insert(0, str(REDA_WS / "asynchvla_ws/src"))
sys.path.insert(0, str(SIMVLA_MODIFIED))

from datasets.dataset_smolvlm import SmolVLMDataReader  # noqa: E402
from models.configuration_smolvlm_vla import SmolVLMVLAConfig  # noqa: E402
from models.modeling_smolvlm_vla import SmolVLMVLA  # noqa: E402
from models.processing_smolvlm_vla import SmolVLMVLAProcessor  # noqa: E402
from simvla_trace.trace import generate_actions_trace  # noqa: E402


def parse_task(path: Path) -> str:
    task = path.stem
    if task.endswith("_demo"):
        task = task[:-5]
    m = re.search(r"SCENE\d+_", task)
    if m:
        task = task[m.end():]
    return task.replace("_", " ")


def write_one_meta(h5_path: Path, idx: int) -> Path:
    META_DIR.mkdir(parents=True, exist_ok=True)
    meta_path = META_DIR / f"trace_meta_{idx:03d}.json"
    meta = {
        "dataset_name": "libero_hdf5",
        "data_dir": str(LIBERO_ROOT),
        "datalist": [{"path": str(h5_path), "task": parse_task(h5_path), "subset": h5_path.parent.name}],
        "num_episodes": 1,
        "observation_key": ["obs/agentview_rgb", "obs/eye_in_hand_rgb"],
        "action_key": "actions",
        "state_dim": 8,
        "action_dim": 7,
        "fps": 10,
    }
    meta_path.write_text(json.dumps(meta, indent=2) + "\n")
    return meta_path


def load_model():
    config = SmolVLMVLAConfig.from_pretrained(str(CHECKPOINT))
    config.smolvlm_model_path = str(LOCAL_BACKBONE)
    model = SmolVLMVLA.from_pretrained(str(CHECKPOINT), config=config)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device).eval()
    return model, device


def to_cpu(x):
    if torch.is_tensor(x):
        return x.detach().cpu()
    return x


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-samples", type=int, default=200)
    parser.add_argument("--min-samples", type=int, default=50)
    parser.add_argument("--num-tasks", type=int, default=8)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--steps", type=int, default=10)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    h5_files = sorted(LIBERO_ROOT.glob("**/*.hdf5"), key=lambda p: p.stat().st_size)
    if not h5_files:
        raise FileNotFoundError(f"No HDF5 files under {LIBERO_ROOT}")
    selected = h5_files[: max(1, args.num_tasks)]
    per_file_cap = max(1, math.ceil(args.max_samples / len(selected)))

    model, device = load_model()
    processor = SmolVLMVLAProcessor.from_pretrained(str(LOCAL_BACKBONE))

    samples = []
    global_idx = 0
    for file_idx, h5_path in enumerate(selected):
        if len(samples) >= args.max_samples:
            break
        meta_path = write_one_meta(h5_path, file_idx)
        ds = SmolVLMDataReader(
            metas_path=str(meta_path),
            num_actions=10,
            num_views=3,
            training=False,
            action_mode="libero_joint",
            image_size=384,
        )
        local_count = 0
        for local_idx, sample in enumerate(ds):
            if len(samples) >= args.max_samples or local_count >= per_file_cap:
                break
            input_ids = processor.encode_language(sample["language_instruction"])["input_ids"].to(device)
            image_input = sample["image_input"].unsqueeze(0).to(device=device, dtype=torch.float32)
            image_mask = sample["image_mask"].unsqueeze(0).to(device=device)
            proprio = sample["proprio"].unsqueeze(0).to(device=device, dtype=torch.float32)
            expert_post = sample["action"].unsqueeze(0).to(device=device, dtype=torch.float32)
            expert_norm = model.action_space.normalize_action(expert_post) if hasattr(model.action_space, "normalize_action") else expert_post
            trace = generate_actions_trace(
                model,
                input_ids=input_ids,
                image_input=image_input,
                image_mask=image_mask,
                proprio=proprio,
                steps=args.steps,
                seed=args.seed,
                return_initial_noise=False,
            )
            gen_norm = trace["generated_normalized_action"]
            per_step = torch.linalg.vector_norm(gen_norm - expert_norm, dim=-1).squeeze(0)
            chunk = per_step.mean()
            item = {
                "sample_id": f"debug_{global_idx:06d}",
                "context_id": f"ctx_{global_idx:06d}",
                "task_name": parse_task(h5_path),
                "task_id": h5_path.stem,
                "demo_id": None,
                "source_hdf5": str(h5_path),
                "source_local_index": int(local_idx),
                "language_instruction": sample["language_instruction"],
                "proprio": to_cpu(proprio.squeeze(0)),
                "pooled_vlm_features": to_cpu(trace["pooled_vlm_features"].squeeze(0)),
                "generated_normalized_action": to_cpu(gen_norm.squeeze(0)),
                "generated_postprocessed_action": to_cpu(trace["generated_postprocessed_action"].squeeze(0)),
                "expert_normalized_action": to_cpu(expert_norm.squeeze(0)),
                "expert_postprocessed_action": to_cpu(expert_post.squeeze(0)),
                "per_step_l2_error_normalized": to_cpu(per_step),
                "chunk_l2_error_normalized": float(chunk.detach().cpu()),
                "seed": int(args.seed),
                "split": "debug_id",
            }
            samples.append(item)
            global_idx += 1
            local_count += 1
            if len(samples) % 25 == 0:
                print(f"collected {len(samples)} samples")

    if len(samples) < args.min_samples:
        raise RuntimeError(f"Collected only {len(samples)} samples, below minimum {args.min_samples}")
    payload = {
        "schema_version": "trace_debug_v1",
        "checkpoint": str(CHECKPOINT),
        "local_backbone": str(LOCAL_BACKBONE),
        "num_samples": len(samples),
        "num_requested": args.max_samples,
        "seed": args.seed,
        "steps": args.steps,
        "samples": samples,
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    torch.save(payload, OUT_PATH)
    print(f"saved {len(samples)} samples to {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
