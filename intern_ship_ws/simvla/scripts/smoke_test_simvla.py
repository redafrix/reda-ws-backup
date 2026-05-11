#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def main() -> int:
    ROOT = Path(__file__).parents[2]
    parser = argparse.ArgumentParser(description="Smoke-test unchanged SimVLA from the cloned repo.")
    parser.add_argument(
        "--repo",
        default=str(ROOT / "simvla/code/SimVLA"),
        help="Path to the unchanged SimVLA clone.",
    )
    parser.add_argument(
        "--checkpoint",
        default=str(ROOT / "assets/models/huggingface/SimVLA-LIBERO"),
        help="Path to the downloaded SimVLA checkpoint.",
    )
    parser.add_argument(
        "--smolvlm",
        default=str(ROOT / "assets/models/huggingface/SmolVLM-500M-Instruct"),
        help="Path to the downloaded SmolVLM backbone.",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    checkpoint = Path(args.checkpoint).resolve()
    smolvlm = Path(args.smolvlm).resolve()

    print(f"repo: {repo}")
    print(f"checkpoint: {checkpoint}")
    print(f"smolvlm: {smolvlm}")

    if not repo.is_dir():
        raise FileNotFoundError(f"Missing repo: {repo}")
    if not checkpoint.is_dir():
        raise FileNotFoundError(f"Missing checkpoint: {checkpoint}")
    if not smolvlm.is_dir():
        raise FileNotFoundError(f"Missing SmolVLM model: {smolvlm}")

    sys.path.insert(0, str(repo))

    import torch
    import transformers

    print(f"torch: {torch.__version__}")
    print(f"torch.cuda.is_available: {torch.cuda.is_available()}")
    print(f"transformers: {transformers.__version__}")

    try:
        import flash_attn  # noqa: F401
        print("flash_attn: available")
    except Exception as exc:  # pragma: no cover - diagnostic only
        print(f"flash_attn: unavailable ({type(exc).__name__}: {exc})")

    from models.modeling_smolvlm_vla import SmolVLMVLA
    from models.processing_smolvlm_vla import SmolVLMVLAProcessor

    model = SmolVLMVLA.from_pretrained(
        str(checkpoint),
        smolvlm_model_path=str(smolvlm),
    )
    processor = SmolVLMVLAProcessor.from_pretrained(str(smolvlm))

    print(f"loaded model class: {type(model).__name__}")
    print(f"loaded processor class: {type(processor).__name__}")
    print(f"config.smolvlm_model_path: {model.config.smolvlm_model_path}")
    print(f"config.num_actions: {model.config.num_actions}")
    print(f"config.image_size: {model.config.image_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
