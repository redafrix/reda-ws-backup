#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import torch

REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
SIMVLA_MODIFIED = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
CHECKPOINT = REDA_WS / "intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000"
LOCAL_BACKBONE = REDA_WS / "intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct"

sys.path.insert(0, str(SIMVLA_MODIFIED))


def gpu_memory(label: str) -> None:
    try:
        out = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=memory.used,memory.total,utilization.gpu",
                "--format=csv,noheader,nounits",
            ],
            text=True,
        ).strip()
        print(f"gpu_memory_{label}: {out} MiB_used,total,util_percent", flush=True)
    except Exception as exc:
        print(f"gpu_memory_{label}: unavailable: {type(exc).__name__}: {exc}", flush=True)


def main() -> None:
    os.environ.setdefault("HF_HOME", str(REDA_WS / "intern_ship_ws/assets/models/huggingface/.hf_cache"))
    os.environ.setdefault("TRANSFORMERS_CACHE", str(Path(os.environ["HF_HOME"]) / "transformers"))
    os.environ.setdefault("HF_HUB_CACHE", str(Path(os.environ["HF_HOME"]) / "hub"))

    print(f"python: {sys.executable}", flush=True)
    print(f"torch: {torch.__version__} cuda={torch.cuda.is_available()} cuda_version={torch.version.cuda}", flush=True)
    print(f"checkpoint: {CHECKPOINT}", flush=True)
    print(f"local_backbone: {LOCAL_BACKBONE}", flush=True)
    print(f"local_backbone_exists: {LOCAL_BACKBONE.exists()}", flush=True)
    gpu_memory("before")

    from models.configuration_smolvlm_vla import SmolVLMVLAConfig
    from models.modeling_smolvlm_vla import SmolVLMVLA

    config = SmolVLMVLAConfig.from_pretrained(str(CHECKPOINT))
    original_backbone = getattr(config, "smolvlm_model_path", None)
    config.smolvlm_model_path = str(LOCAL_BACKBONE)
    print(f"original_smolvlm_model_path: {original_backbone}", flush=True)
    print(f"effective_smolvlm_model_path: {config.smolvlm_model_path}", flush=True)

    model = SmolVLMVLA.from_pretrained(str(CHECKPOINT), config=config)
    model.eval()
    print("model_loaded: OK", flush=True)

    action_dim = getattr(getattr(model, "action_space", None), "dim_action", None)
    values = {
        "num_actions": getattr(model.config, "num_actions", None),
        "action_dim": action_dim,
        "action_mode": getattr(model.config, "action_mode", None),
        "num_views": getattr(model.config, "num_views", None),
        "image_size": getattr(model.config, "image_size", None),
        "use_proprio": getattr(model.config, "use_proprio", None),
        "predict_uncertainty": getattr(model.config, "predict_uncertainty", None),
        "model_type": getattr(model.config, "model_type", None),
        "smolvlm_model_path": getattr(model.config, "smolvlm_model_path", None),
    }
    print("config_values:", json.dumps(values, indent=2), flush=True)
    gpu_memory("after_cpu_load")

    if torch.cuda.is_available():
        model.to("cuda")
        torch.cuda.synchronize()
        print("model_to_cuda: OK", flush=True)
        gpu_memory("after_cuda_load")


if __name__ == "__main__":
    main()
