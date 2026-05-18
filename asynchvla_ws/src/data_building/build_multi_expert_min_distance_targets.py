#!/usr/bin/env python3
"""Stage 7 — Build multi-expert min-distance targets for an existing
multiseed candidate dataset.

For each candidate, this script computes alternative "true error" targets
that compare the candidate action against a pool of K expert actions from
similar contexts (instead of the single ground-truth expert for that
context_id). This addresses the "single-expert L2 is brittle when several
valid expert actions exist" weakness flagged in Stage 6/7.

Two pooling modes:

  --pool-mode train_only_same_task  (deployable)
      For ANY candidate, pool = (train_contexts, same task_name).
      For OOD splits the same task never appears in train, so the pool will
      be empty — multi-expert collapses to the original single-expert target.
      Reported as `multi_expert_pool_size=0`.

  --pool-mode same_split_same_task  (default; analysis-friendly)
      Pool = (candidate's own split's contexts, same task_name), excluding
      the candidate's own context_id. This lets us study whether allowing
      multiple valid experts reduces false high uncertainty for candidates
      that are correct but slightly different from the single canonical
      expert, including for the OOD split. NOT a deployable training target
      for non-train splits (training target is taken from rows whose split
      == 'train' anyway, so the practical leakage is only when computing
      analysis-mode targets on calib/test_id/test_ood for evaluation).

In all modes, K-nearest are picked by cosine similarity on
`pooled_vlm_features` (a SimVLA-derived, context-only feature; not a
circular target).

For each candidate we add the following keys:
  target_chunk_l2_single_expert (== existing true_chunk_l2_error, copied)
  target_chunk_min_l2_K5
  target_chunk_min_l2_K10
  target_chunk_min_l2_K20
  target_chunk_softmin_l2_K10  (log-sum-exp soft min, beta=4)
  target_chunk_mean_top3_l2_K10
  multi_expert_pool_size  (actual K used; may be < requested if pool is small)

Usage:
  python3 asynchvla_ws/src/data_building/build_multi_expert_min_distance_targets.py \
      --split-name holdout_libero_object \
      --candidate-dir asynchvla_ws/data/processed_stage5

Output files (per split):
  multiseed_candidate_<part>_multiexp.pt   — augmented candidates
  multiseed_multi_expert_summary.json      — counts and pool stats
"""

from __future__ import annotations

import argparse
import json
import math
import os
from collections import defaultdict
from pathlib import Path

import torch

REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
DATA_ROOT_DEFAULT = REDA_WS / "asynchvla_ws/data/processed_stage5"


def _load_candidates(p: Path):
    if not p.exists():
        return None
    return torch.load(p, map_location="cpu", weights_only=False)


def _extract_expert_pool(candidates):
    """Return per-task list of (context_id, expert_action_chunk[10,7], vlm[960])."""
    seen_ctx = set()
    pool = defaultdict(list)
    for row in candidates:
        ctx_id = row["context_id"]
        if ctx_id in seen_ctx:
            continue
        seen_ctx.add(ctx_id)
        pool[row["task_name"]].append(
            (
                ctx_id,
                row["target_expert_action_normalized"].float(),
                row["pooled_vlm_features"].float(),
            )
        )
    return pool


def _normalize(x: torch.Tensor) -> torch.Tensor:
    return x / x.norm(dim=-1, keepdim=True).clamp_min(1e-8)


def _topk_neighbors(query_vlm: torch.Tensor, pool_entries, k: int, exclude_ctx_id: str | None):
    """Return up to k (idx, action_chunk[10,7]) pairs of nearest expert
    actions in `pool_entries` by cosine similarity, excluding `exclude_ctx_id`.
    """
    if not pool_entries:
        return []
    ctx_ids = [e[0] for e in pool_entries]
    actions = torch.stack([e[1] for e in pool_entries])  # [P,10,7]
    vlms = torch.stack([e[2] for e in pool_entries])  # [P,960]
    qn = _normalize(query_vlm.unsqueeze(0))  # [1,960]
    vn = _normalize(vlms)
    sim = (qn @ vn.t()).squeeze(0)  # [P]
    if exclude_ctx_id is not None:
        for i, cid in enumerate(ctx_ids):
            if cid == exclude_ctx_id:
                sim[i] = -1e9
    top = torch.topk(sim, k=min(k, sim.numel()), largest=True)
    return [
        (idx.item(), actions[idx])
        for idx in top.indices
        if sim[idx].item() > -1e8
    ]


def _l2_chunk(a: torch.Tensor, b: torch.Tensor) -> float:
    """Mean-per-step L2 distance between two action chunks [10,7]."""
    return float(torch.linalg.vector_norm(a - b, dim=-1).mean())


def augment_candidates(candidates, expert_pool, ks=(5, 10, 20), softmin_K=10, top3_K=10):
    """Augment each candidate dict with multi-expert L2 targets.

    `expert_pool` is a {task_name: [(ctx_id, action_chunk, vlm)]} dict. The
    caller decides what data went into the pool (train-only vs same-split).
    Self-context is always excluded.
    """
    softmin_beta = 4.0
    out = []
    pool_size_counts = []
    for row in candidates:
        task = row["task_name"]
        cand_action = row["candidate_action_normalized"].float()
        vlm = row["pooled_vlm_features"].float()
        pool = expert_pool.get(task, [])
        exclude_ctx = row["context_id"]
        K_max = max(ks + (softmin_K, top3_K))
        nbrs = _topk_neighbors(vlm, pool, K_max, exclude_ctx)
        K_actual = len(nbrs)
        pool_size_counts.append(K_actual)
        # distances candidate_action vs every neighbor expert
        if K_actual == 0:
            # fallback: keep single-expert target only
            row = {**row,
                   "target_chunk_l2_single_expert": float(row["true_chunk_l2_error"]),
                   "multi_expert_pool_size": 0,
                   }
            for k in ks:
                row[f"target_chunk_min_l2_K{k}"] = float(row["true_chunk_l2_error"])
            row[f"target_chunk_softmin_l2_K{softmin_K}"] = float(row["true_chunk_l2_error"])
            row[f"target_chunk_mean_top3_l2_K{top3_K}"] = float(row["true_chunk_l2_error"])
            out.append(row)
            continue
        # compute distances (per-step L2 averaged across 10 steps)
        nbr_actions = torch.stack([a for _, a in nbrs])  # [K_actual,10,7]
        diffs = nbr_actions - cand_action.unsqueeze(0)
        per_step_l2 = torch.linalg.vector_norm(diffs, dim=-1)  # [K_actual,10]
        chunk_l2 = per_step_l2.mean(dim=1)  # [K_actual]
        chunk_l2_sorted, _ = torch.sort(chunk_l2)
        new_row = {**row}
        new_row["target_chunk_l2_single_expert"] = float(row["true_chunk_l2_error"])
        new_row["multi_expert_pool_size"] = int(K_actual)
        for k in ks:
            sub = chunk_l2[: k] if K_actual >= k else chunk_l2
            new_row[f"target_chunk_min_l2_K{k}"] = float(sub.min())
        sub = chunk_l2[: softmin_K] if K_actual >= softmin_K else chunk_l2
        # softmin via -1/β log sum exp(-β x_i)
        x = sub
        new_row[f"target_chunk_softmin_l2_K{softmin_K}"] = float(
            -1.0 / softmin_beta * torch.logsumexp(-softmin_beta * x, dim=0)
        )
        sub_top3 = chunk_l2_sorted[: min(3, K_actual)]
        new_row[f"target_chunk_mean_top3_l2_K{top3_K}"] = float(sub_top3.mean())
        out.append(new_row)
    summary = {
        "num_rows": len(out),
        "pool_size_min": int(min(pool_size_counts)) if pool_size_counts else 0,
        "pool_size_max": int(max(pool_size_counts)) if pool_size_counts else 0,
        "pool_size_mean": float(sum(pool_size_counts) / max(1, len(pool_size_counts))),
        "rows_with_empty_pool": int(sum(1 for k in pool_size_counts if k == 0)),
    }
    return out, summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split-name", required=True)
    ap.add_argument(
        "--candidate-dir",
        type=Path,
        default=DATA_ROOT_DEFAULT,
        help="processed_stage5 root containing <split>/multiseed_candidate_*.pt",
    )
    ap.add_argument(
        "--parts",
        nargs="+",
        default=["train", "calib", "test_id", "test_ood"],
    )
    ap.add_argument(
        "--pool-mode",
        choices=["same_split_same_task", "train_only_same_task"],
        default="same_split_same_task",
        help="Source of expert pool. same_split: per-split, same task (analysis). "
             "train_only: train-only, same task (deployable; OOD pool may be empty).",
    )
    args = ap.parse_args()

    split_dir = args.candidate_dir / args.split_name
    if not split_dir.exists():
        raise SystemExit(f"No split dir {split_dir}")

    # Pre-load any data we may need
    cached = {p: _load_candidates(split_dir / f"multiseed_candidate_{p}.pt") for p in args.parts}
    if cached.get("train") is None:
        raise SystemExit(f"Missing train candidates in {split_dir}")

    summary = {
        "split": args.split_name,
        "pool_mode": args.pool_mode,
        "per_part": {},
    }

    if args.pool_mode == "train_only_same_task":
        shared_pool = _extract_expert_pool(cached["train"]["candidates"])
        pool_counts = {k: len(v) for k, v in shared_pool.items()}
        summary["expert_pool_total_contexts"] = sum(pool_counts.values())
        summary["expert_pool_unique_tasks"] = len(pool_counts)
        summary["expert_pool_per_task"] = pool_counts
    else:
        shared_pool = None

    for part in args.parts:
        data = cached.get(part)
        if data is None:
            print(f"  skip {part}: missing")
            continue
        if args.pool_mode == "train_only_same_task":
            pool = shared_pool
        else:  # same_split_same_task
            pool = _extract_expert_pool(data["candidates"])
            pc = {k: len(v) for k, v in pool.items()}
            summary["per_part"].setdefault(part, {})["pool_per_task"] = pc
            summary["per_part"][part]["pool_total_contexts"] = sum(pc.values())
        augmented, stats = augment_candidates(data["candidates"], pool)
        src_p = split_dir / f"multiseed_candidate_{part}.pt"
        out_path = split_dir / f"multiseed_candidate_{part}_multiexp.pt"
        torch.save(
            {
                "schema_version": "multiseed_candidate_multiexp_v1",
                "source_candidate": str(src_p),
                "num_contexts": data["num_contexts"],
                "num_candidates": data["num_candidates"],
                "candidates": augmented,
            },
            out_path,
        )
        summary["per_part"].setdefault(part, {}).update({
            "rows": stats["num_rows"],
            "pool_size_min": stats["pool_size_min"],
            "pool_size_max": stats["pool_size_max"],
            "pool_size_mean": round(stats["pool_size_mean"], 2),
            "rows_with_empty_pool": stats["rows_with_empty_pool"],
            "out_path": str(out_path),
        })
        print(f"  wrote {out_path}  rows={stats['num_rows']}  K_mean={stats['pool_size_mean']:.1f}")

    sumpath = split_dir / "multiseed_multi_expert_summary.json"
    sumpath.write_text(json.dumps(summary, indent=2))
    print("summary:", sumpath)


if __name__ == "__main__":
    main()
