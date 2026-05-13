#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path

import torch

REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
TRACE = REDA_WS / "asynchvla_ws/data/debug/trace_debug.pt"
OUT = REDA_WS / "asynchvla_ws/data/debug/candidate_debug.pt"


def l2_errors(candidate: torch.Tensor, expert: torch.Tensor):
    per_step = torch.linalg.vector_norm(candidate - expert, dim=-1)
    return per_step, float(per_step.mean())


def add_row(rows, ctx, candidate_type: str, action: torch.Tensor):
    expert = ctx["expert_normalized_action"]
    per_step, chunk = l2_errors(action, expert)
    rows.append({
        "context_id": ctx["context_id"],
        "sample_id": ctx["sample_id"],
        "task_name": ctx["task_name"],
        "source_hdf5": ctx["source_hdf5"],
        "language_instruction": ctx["language_instruction"],
        "candidate_type": candidate_type,
        "candidate_action_normalized": action.detach().clone().cpu(),
        "target_expert_action_normalized": expert.detach().clone().cpu(),
        "true_per_step_l2_error": per_step.detach().clone().cpu(),
        "true_chunk_l2_error": chunk,
        "pooled_vlm_features": ctx["pooled_vlm_features"].detach().clone().cpu(),
        "proprio": ctx["proprio"].detach().clone().cpu(),
        "split": ctx.get("split", "debug_id"),
    })


def far_index(indices, current_pos):
    if not indices:
        return None
    return max(indices, key=lambda j: abs(j - current_pos))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument("--small-noise", type=float, default=0.10)
    parser.add_argument("--large-noise", type=float, default=0.75)
    args = parser.parse_args()
    g = torch.Generator().manual_seed(args.seed)
    payload = torch.load(TRACE, map_location="cpu")
    samples = payload["samples"]
    task_to_indices = defaultdict(list)
    for i, s in enumerate(samples):
        task_to_indices[s["task_name"]].append(i)
    all_indices = list(range(len(samples)))
    rows = []
    for i, ctx in enumerate(samples):
        expert = ctx["expert_normalized_action"]
        add_row(rows, ctx, "expert_action", expert)
        add_row(rows, ctx, "simvla_seed0", ctx["generated_normalized_action"])
        add_row(rows, ctx, "perturb_small", expert + args.small_noise * torch.randn(expert.shape, generator=g))
        add_row(rows, ctx, "perturb_large", expert + args.large_noise * torch.randn(expert.shape, generator=g))
        same_candidates = [j for j in task_to_indices[ctx["task_name"]] if j != i]
        j = far_index(same_candidates, i)
        if j is not None:
            add_row(rows, ctx, "same_task_far", samples[j]["expert_normalized_action"])
        other_candidates = [j for j in all_indices if samples[j]["task_name"] != ctx["task_name"]]
        k = other_candidates[(i * 37) % len(other_candidates)] if other_candidates else None
        if k is not None:
            add_row(rows, ctx, "other_demo_or_other_task", samples[k]["expert_normalized_action"])
    out = {
        "schema_version": "candidate_debug_v1",
        "source_trace": str(TRACE),
        "num_contexts": len(samples),
        "num_candidates": len(rows),
        "seed": args.seed,
        "small_noise": args.small_noise,
        "large_noise": args.large_noise,
        "candidates": rows,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    torch.save(out, OUT)
    print(f"saved {len(rows)} candidates for {len(samples)} contexts to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
