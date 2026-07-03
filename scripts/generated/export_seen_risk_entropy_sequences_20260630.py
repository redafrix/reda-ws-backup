#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch
from scipy.stats import entropy as shannon_entropy

ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608")
TRAIN_SCRIPT = ROOT / "src/train_frozen_detectors_h10_proof.py"
RUN_ROOT = ROOT / "inputs/datasets/continuous_chunk10_flat"
QUERY_PATH = RUN_ROOT / "worker_0/query_samples.jsonl"
MODEL_DIR = ROOT / "models/h10_continuous/all_tasks_random/unc_topk8"
OUT = Path("/tmp/seen_val_risk_entropy_sequences_20260630.json")
VARIANT = "unc_topk8"
SPLIT = "all_tasks_random"

spec = importlib.util.spec_from_file_location("h10train", str(TRAIN_SCRIPT))
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


def read_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def load_norm(path: Path):
    raw = json.loads(path.read_text())
    return {k: {kk: np.asarray(vv, dtype=np.float32) for kk, vv in val.items()} for k, val in raw.items()}


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


def compute_cell_size(calib_eids: set[str]) -> np.ndarray:
    chunks = []
    for row in read_jsonl(QUERY_PATH):
        if str(row["episode_id"]) in calib_eids:
            a = action_preds(row)
            chunks.append(a.reshape(-1, a.shape[-1]))
    positions = np.concatenate(chunks, axis=0)
    ranges = positions.max(axis=0) - positions.min(axis=0)
    max_range = float(ranges.max())
    ranges = np.where(ranges == 0, max_range, ranges)
    return (ranges * 0.01).astype(np.float32)


def build_entropy_map(target_eids: set[str], cell_size: np.ndarray) -> dict[tuple[str, int], float]:
    out = {}
    n = 0
    for row in read_jsonl(QUERY_PATH):
        eid = str(row["episode_id"])
        if eid not in target_eids:
            continue
        out[(eid, int(row["timestep"]))] = entropy_score(action_preds(row), cell_size)
        n += 1
        if n % 10000 == 0:
            print(f"[entropy] {n}", flush=True)
    print(f"[entropy] total={n}", flush=True)
    return out


def main():
    cfg = json.loads((MODEL_DIR / "config.json").read_text())
    seed = int(cfg.get("seed", 2026060801))
    args = SimpleNamespace(
        width=128, layers=3, heads=4, dropout=0.1, unc_raw_static_dropout=0.0,
        batch_size=2048, seed=seed,
        train_success_limit=1000000, train_failure_limit=1000000,
        val_success_limit=1000000, val_failure_limit=1000000,
        calib_success_limit=1000000, test_success_limit=1000000,
        test_failure_limit=1000000, ood_success_limit=1000000, ood_failure_limit=1000000,
    )
    limits = {k: getattr(args, k + "_limit") for k in [
        "train_success", "train_failure", "val_success", "val_failure", "calib_success",
        "test_success", "test_failure", "ood_success", "ood_failure"
    ]}
    episodes = mod.load_episode_meta(RUN_ROOT, "libero_goal_object")
    buckets = mod.make_split_assignments(episodes, SPLIT, seed, limits)
    rows_by_bucket = mod.build_rows_for_split(RUN_ROOT, episodes, buckets, history_steps=16, cadence="native", stride=10)
    target_rows = rows_by_bucket["success_val_seen"] + rows_by_bucket["failure_val_seen"]
    target_eids = {r.episode_id for r in target_rows}
    calib_eids = {r.episode_id for r in rows_by_bucket["success_calib_seen"]}
    cell_size = compute_cell_size(calib_eids)
    ent_map = build_entropy_map(target_eids, cell_size)

    stats = load_norm(MODEL_DIR / "normalization.json")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = mod.SeqRiskModel(hist_dim=21, action_dim=7, static_dim=51, width=128, layers=3, heads=4, dropout=0.1, static_input_dropout=0.0).to(device)
    model.load_state_dict(torch.load(MODEL_DIR / "model.pt", map_location=device))
    model.eval()

    out_eps = {}
    for bucket in ["success_val_seen", "failure_val_seen"]:
        rows = rows_by_bucket[bucket]
        print(f"[risk] {bucket} rows={len(rows)} eps={len(set(r.episode_id for r in rows))}", flush=True)
        scores, _y, ids, ts = mod.score_rows(model, stats, rows, VARIANT, args.batch_size, device)
        for s, eid, t in zip(scores, ids, ts):
            meta = episodes[eid]
            rec = out_eps.setdefault(eid, {
                "episode_id": eid,
                "label": 0 if meta.success else 1,
                "num_steps": int(meta.num_steps),
                "bucket": bucket,
                "t": [],
                "risk": [],
                "entropy": [],
            })
            ti = int(t)
            rec["t"].append(ti)
            rec["risk"].append(float(s))
            rec["entropy"].append(float(ent_map[(eid, ti)]))
    for rec in out_eps.values():
        order = np.argsort(rec["t"]).tolist()
        for k in ["t", "risk", "entropy"]:
            rec[k] = [rec[k][i] for i in order]
    OUT.write_text(json.dumps({"cell_size": cell_size.tolist(), "episodes": list(out_eps.values())}) + "\n")
    print(f"[done] {OUT} eps={len(out_eps)}", flush=True)


if __name__ == "__main__":
    main()
