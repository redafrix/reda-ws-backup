#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import entropy as shannon_entropy

BASE = Path("/home/dean/fiper_uncertainty_collection")
OOD_ROWS = BASE / "data/simvla_goal_object_ood_ablation_20260625/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622/fiper_receding_samples.jsonl"
RISK_SCORES = BASE / "experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626/scores.npz"
CELL_SOURCE = Path("/tmp/seen_val_risk_entropy_sequences_20260630.json")
OUT = Path("/tmp/ood180_risk_entropy_sequences_20260630.json")


def read_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def action_preds(row: dict) -> np.ndarray:
    return np.asarray([row["main_candidate_action_chunk_normalized"]] + list(row["ace_candidate_chunks_normalized"]), dtype=np.float32)


def entropy_endpoints(endpoints: np.ndarray, cell_size: np.ndarray) -> float:
    endpoints = np.asarray(endpoints, dtype=np.float32)
    mins = endpoints[:, :3].min(axis=0)
    maxs = endpoints[:, :3].max(axis=0)
    buf = 0.01 * (maxs - mins)
    mins -= buf
    maxs += buf
    cs = np.maximum(cell_size[:3], 1e-8)
    grids = [np.arange(mins[i], maxs[i] + cs[i], cs[i]) for i in range(3)]
    dims = [max(len(g) - 1, 1) for g in grids]
    idxs = [np.clip(np.digitize(endpoints[:, i], grids[i]) - 1, 0, dims[i] - 1) for i in range(3)]
    counts = np.zeros(tuple(dims), dtype=np.int32)
    for i in range(len(endpoints)):
        counts[idxs[0][i], idxs[1][i], idxs[2][i]] += 1
    return float(shannon_entropy(counts.reshape(-1), base=2))


def entropy_score(actions: np.ndarray, cell_size: np.ndarray) -> float:
    return float(np.mean([entropy_endpoints(actions[:, i, :], cell_size) for i in range(actions.shape[1])]))


def main():
    cell_size = np.asarray(json.loads(CELL_SOURCE.read_text())["cell_size"], dtype=np.float32)
    risk_scores = np.load(RISK_SCORES)["scores"]
    by_ep = defaultdict(lambda: {"episode_id": None, "label": 0, "num_steps": 0, "bucket": "ood180", "t": [], "risk": [], "entropy": []})
    for i, row in enumerate(read_jsonl(OOD_ROWS)):
        eid = str(row.get("episode_id") or row.get("episode_uid"))
        rec = by_ep[eid]
        rec["episode_id"] = eid
        rec["label"] = 1 if bool(row.get("parent_failed_or_timeout")) else 0
        rec["num_steps"] = max(rec["num_steps"], int(row.get("timestep", i)))
        rec["t"].append(int(row.get("timestep", i)))
        rec["risk"].append(float(risk_scores[i]))
        rec["entropy"].append(entropy_score(action_preds(row), cell_size))
        if i and i % 10000 == 0:
            print(f"[ood] rows={i}", flush=True)
    for rec in by_ep.values():
        order = np.argsort(rec["t"]).tolist()
        for k in ["t", "risk", "entropy"]:
            rec[k] = [rec[k][i] for i in order]
    OUT.write_text(json.dumps({"cell_size": cell_size.tolist(), "episodes": list(by_ep.values())}) + "\n")
    print(f"[done] {OUT} eps={len(by_ep)}", flush=True)


if __name__ == "__main__":
    main()
