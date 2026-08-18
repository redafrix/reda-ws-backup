#!/usr/bin/env python3
"""Compare frozen V1 and frozen V2 score arrays on identical locked OOD150 rows."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score


def metrics(labels: np.ndarray, scores: np.ndarray, episode_weights: np.ndarray) -> dict[str, float]:
    y = labels.astype(np.int32)
    return {
        "query_auprc": float(average_precision_score(y, scores)),
        "query_auroc": float(roc_auc_score(y, scores)),
        "episode_balanced_auprc": float(average_precision_score(y, scores, sample_weight=episode_weights)),
        "episode_balanced_auroc": float(roc_auc_score(y, scores, sample_weight=episode_weights)),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--ood-dataset-root", type=Path, required=True)
    p.add_argument("--v1-eval-root", type=Path, required=True)
    p.add_argument("--v2-eval-root", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()

    episode_index = np.asarray(np.load(args.ood_dataset_root / "episode_index.npy", mmap_mode="r"), dtype=np.int64)
    counts = np.bincount(episode_index)
    if np.any(counts <= 0):
        raise RuntimeError("OOD150 episode index has empty episode")
    row_weights = 1.0 / counts[episode_index]

    v1_npz = np.load(args.v1_eval_root / "scores.npz")
    v2_npz = np.load(args.v2_eval_root / "scores.npz")
    v1_labels = np.asarray(v1_npz["labels"], dtype=np.float32)
    v2_labels = np.asarray(v2_npz["labels"], dtype=np.float32)
    v1_scores = np.asarray(v1_npz["scores"], dtype=np.float32)
    v2_scores = np.asarray(v2_npz["scores"], dtype=np.float32)

    if not np.array_equal(v1_labels, v2_labels):
        raise RuntimeError("V1/V2 OOD150 labels differ")
    if len(v1_labels) != len(episode_index):
        raise RuntimeError("OOD150 score rows do not match dataset episode_index")

    v1 = metrics(v1_labels, v1_scores, row_weights)
    v2 = metrics(v2_labels, v2_scores, row_weights)
    delta = {key: float(v2[key] - v1[key]) for key in v1}

    payload = {
        "schema_version": "isaac_h10_topk8_v1_v2_ood150_comparison_v1",
        "rows": int(len(v1_labels)),
        "episodes": int(len(counts)),
        "v1": v1,
        "v2": v2,
        "delta_v2_minus_v1": delta,
        "same_rows_verified": True,
        "development_evidence_only": True,
        "used_for_v2_training": False,
        "used_for_v2_checkpoint_selection": False,
        "used_for_v2_threshold_selection": False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
