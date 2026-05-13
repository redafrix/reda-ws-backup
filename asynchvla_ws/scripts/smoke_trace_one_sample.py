#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import torch

REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
SIMVLA_MODIFIED = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
CHECKPOINT = REDA_WS / "intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000"
LOCAL_BACKBONE = REDA_WS / "intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct"
LIBERO_ROOT = REDA_WS / "intern_ship_ws/assets/data/libero_datasets"
DEBUG_META = REDA_WS / "asynchvla_ws/data/debug/one_libero_meta.json"
REPORT = REDA_WS / "asynchvla_ws/outputs/reports/trace_one_sample_smoke.md"

sys.path.insert(0, str(REDA_WS / "asynchvla_ws/src"))
sys.path.insert(0, str(SIMVLA_MODIFIED))

from datasets.dataset_smolvlm import SmolVLMDataReader  # noqa: E402
from models.configuration_smolvlm_vla import SmolVLMVLAConfig  # noqa: E402
from models.modeling_smolvlm_vla import SmolVLMVLA  # noqa: E402
from models.processing_smolvlm_vla import SmolVLMVLAProcessor  # noqa: E402
from simvla_trace.trace import generate_actions_trace  # noqa: E402


def shape_of(value):
    if torch.is_tensor(value):
        return {"shape": list(value.shape), "dtype": str(value.dtype), "device": str(value.device)}
    if isinstance(value, (tuple, list)):
        return list(value)
    return value


def build_debug_meta() -> Path:
    h5_files = sorted(LIBERO_ROOT.glob("**/*.hdf5"), key=lambda p: p.stat().st_size)
    if not h5_files:
        raise FileNotFoundError(f"No HDF5 files under {LIBERO_ROOT}")
    h5_path = h5_files[0]
    task = h5_path.stem
    if task.endswith("_demo"):
        task = task[:-5]
    m = re.search(r"SCENE\d+_", task)
    if m:
        task = task[m.end():]
    task = task.replace("_", " ")
    meta = {
        "dataset_name": "libero_hdf5",
        "data_dir": str(LIBERO_ROOT),
        "datalist": [{"path": str(h5_path), "task": task, "subset": h5_path.parent.name}],
        "num_episodes": 1,
        "observation_key": ["obs/agentview_rgb", "obs/eye_in_hand_rgb"],
        "action_key": "actions",
        "state_dim": 8,
        "action_dim": 7,
        "fps": 10,
    }
    DEBUG_META.write_text(json.dumps(meta, indent=2) + "\n")
    return h5_path


def load_one_sample():
    h5_path = build_debug_meta()
    ds = SmolVLMDataReader(
        metas_path=str(DEBUG_META),
        num_actions=10,
        num_views=3,
        training=False,
        action_mode="libero_joint",
        image_size=384,
    )
    return h5_path, next(iter(ds))


def load_model():
    config = SmolVLMVLAConfig.from_pretrained(str(CHECKPOINT))
    config.smolvlm_model_path = str(LOCAL_BACKBONE)
    model = SmolVLMVLA.from_pretrained(str(CHECKPOINT), config=config)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()
    return model, device


def main() -> int:
    h5_path, sample = load_one_sample()
    model, device = load_model()
    processor = SmolVLMVLAProcessor.from_pretrained(str(LOCAL_BACKBONE))
    input_ids = processor.encode_language(sample["language_instruction"])["input_ids"].to(device)
    image_input = sample["image_input"].unsqueeze(0).to(device=device, dtype=torch.float32)
    image_mask = sample["image_mask"].unsqueeze(0).to(device=device)
    proprio = sample["proprio"].unsqueeze(0).to(device=device, dtype=torch.float32)
    expert_postprocessed = sample["action"].unsqueeze(0).to(device=device, dtype=torch.float32)
    if hasattr(model.action_space, "normalize_action"):
        expert_normalized = model.action_space.normalize_action(expert_postprocessed)
    else:
        expert_normalized = expert_postprocessed

    trace0 = generate_actions_trace(
        model,
        input_ids=input_ids,
        image_input=image_input,
        image_mask=image_mask,
        proprio=proprio,
        steps=10,
        seed=0,
        return_initial_noise=False,
    )
    trace1 = generate_actions_trace(
        model,
        input_ids=input_ids,
        image_input=image_input,
        image_mask=image_mask,
        proprio=proprio,
        steps=10,
        seed=1,
        return_initial_noise=False,
    )

    gen0 = trace0["generated_normalized_action"]
    gen1 = trace1["generated_normalized_action"]
    actions_differ = not torch.allclose(gen0, gen1)
    per_step_l2 = torch.linalg.vector_norm(gen0 - expert_normalized, dim=-1).squeeze(0)
    chunk_l2_mean = per_step_l2.mean()
    post_per_step_l2 = torch.linalg.vector_norm(trace0["generated_postprocessed_action"] - expert_postprocessed, dim=-1).squeeze(0)

    results = {
        "checkpoint": str(CHECKPOINT),
        "local_backbone": str(LOCAL_BACKBONE),
        "hdf5": str(h5_path),
        "language_instruction": sample["language_instruction"],
        "input_ids": shape_of(input_ids),
        "image_input": shape_of(image_input),
        "image_mask": shape_of(image_mask),
        "proprio": shape_of(proprio),
        "expert_postprocessed_action": shape_of(expert_postprocessed),
        "expert_normalized_action": shape_of(expert_normalized),
        "generated_normalized_action_seed0": shape_of(trace0["generated_normalized_action"]),
        "generated_postprocessed_action_seed0": shape_of(trace0["generated_postprocessed_action"]),
        "pooled_vlm_features_seed0": shape_of(trace0["pooled_vlm_features"]),
        "vlm_feature_shape_seed0": shape_of(trace0["vlm_feature_shape"]),
        "proprio_norm_seed0": shape_of(trace0["proprio_norm"]),
        "seed0": trace0["seed"],
        "seed1": trace1["seed"],
        "num_flow_steps": trace0["num_flow_steps"],
        "actions_differ_between_seed0_seed1": bool(actions_differ),
        "normalized_action_error_per_step_l2": [float(x) for x in per_step_l2.detach().cpu()],
        "normalized_action_error_chunk_l2_mean": float(chunk_l2_mean.detach().cpu()),
        "postprocessed_action_error_per_step_l2": [float(x) for x in post_per_step_l2.detach().cpu()],
        "postprocessed_action_error_chunk_l2_mean": float(post_per_step_l2.mean().detach().cpu()),
        "first_flow_step": trace0["flow_steps"][0] if trace0["flow_steps"] else None,
        "last_flow_step": trace0["flow_steps"][-1] if trace0["flow_steps"] else None,
    }

    lines = [
        "# Trace One Sample Smoke Test",
        "",
        "Status: `OK`",
        "",
        "## Results",
        "",
        "```json",
        json.dumps(results, indent=2),
        "```",
        "",
        "## Alignment",
        "",
        "The expert target is `sample['action']`, already `[10,7]` after the official loader slices `abs_trajectory[1:]`. The trace generated normalized action is `[1,10,7]`; normalized error is computed after `model.action_space.normalize_action(sample['action'])`.",
    ]
    REPORT.write_text("\n".join(lines) + "\n")
    print("trace_one_sample_smoke: OK")
    for key, value in results.items():
        print(key, value)
    print("report", REPORT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
