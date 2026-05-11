#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path


def main() -> int:
    ROOT = Path(__file__).parents[2]
    parser = argparse.ArgumentParser(description="Workspace-side SimVLA server wrapper with local backbone paths.")
    parser.add_argument(
        "--repo",
        default=str(ROOT / "simvla/code/SimVLA"),
        help="Path to unchanged SimVLA clone.",
    )
    parser.add_argument(
        "--checkpoint",
        default=str(ROOT / "assets/models/huggingface/SimVLA-LIBERO"),
        help="Path to local SimVLA checkpoint.",
    )
    parser.add_argument(
        "--smolvlm_model",
        default=str(ROOT / "assets/models/huggingface/SmolVLM-500M-Instruct"),
        help="Path to local SmolVLM backbone.",
    )
    parser.add_argument(
        "--norm_stats",
        default=str(ROOT / "simvla/code/SimVLA/norm_stats/libero_norm.json"),
        help="Path to norm stats JSON.",
    )
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    checkpoint = Path(args.checkpoint).resolve()
    smolvlm = Path(args.smolvlm_model).resolve()
    norm_stats = Path(args.norm_stats).resolve()

    os.environ.setdefault("PYTHONNOUSERSITE", "1")
    sys.path.insert(0, str(repo))

    import evaluation.libero.serve_smolvlm_libero as server
    from models.modeling_smolvlm_vla import SmolVLMVLA
    from models.processing_smolvlm_vla import SmolVLMVLAProcessor

    server.logger.info(f"Loading SimVLA from {checkpoint} with local SmolVLM backbone {smolvlm}...")

    server.model = SmolVLMVLA.from_pretrained(
        str(checkpoint),
        smolvlm_model_path=str(smolvlm),
    )
    server.model = server.model.to(server.device)
    server.model.eval()

    server.processor = SmolVLMVLAProcessor.from_pretrained(str(smolvlm))

    if norm_stats.exists():
        server.logger.info(f"Loading norm stats from: {norm_stats}")
        server.model.action_space.load_norm_stats(str(norm_stats))
    else:
        server.logger.warning("No norm stats found at %s", norm_stats)

    server.logger.info(f"Starting local-path SimVLA server on {args.host}:{args.port}")
    asyncio.run(server.serve(args.host, args.port))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
