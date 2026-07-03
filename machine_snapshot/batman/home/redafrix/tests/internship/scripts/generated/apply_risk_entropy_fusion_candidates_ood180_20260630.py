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
CANDIDATES = Path("/tmp/risk_entropy_seen_fusion_candidates.json")
OUT = BASE / "experiments/h10_ood_risk_models_20260610/evaluation_ood_20260630_risk_entropy_fusion_seen_calibrated"


def read_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def action_preds(row: dict) -> np.ndarray:
    return np.asarray([row["main_candidate_action_chunk_normalized"]] + list(row["ace_candidate_chunks_normalized"]), dtype=np.float32)


def entropy_endpoints(endpoints: np.ndarray, cell_size: np.ndarray) -> float:
    endpoints = np.asarray(endpoints, dtype=np.float32)
    x_min, x_max = endpoints[:, 0].min(), endpoints[:, 0].max()
    y_min, y_max = endpoints[:, 1].min(), endpoints[:, 1].max()
    z_min, z_max = endpoints[:, 2].min(), endpoints[:, 2].max()
    x_buffer = 0.01 * (x_max - x_min)
    y_buffer = 0.01 * (y_max - y_min)
    z_buffer = 0.01 * (z_max - z_min)
    x_min -= x_buffer
    x_max += x_buffer
    y_min -= y_buffer
    y_max += y_buffer
    z_min -= z_buffer
    z_max += z_buffer
    cs = np.maximum(cell_size[:3], 1e-8)
    x_grid = np.arange(x_min, x_max + cs[0], cs[0])
    y_grid = np.arange(y_min, y_max + cs[1], cs[1])
    z_grid = np.arange(z_min, z_max + cs[2], cs[2])
    ix = np.clip(np.digitize(endpoints[:, 0], x_grid) - 1, 0, max(len(x_grid) - 2, 0))
    iy = np.clip(np.digitize(endpoints[:, 1], y_grid) - 1, 0, max(len(y_grid) - 2, 0))
    iz = np.clip(np.digitize(endpoints[:, 2], z_grid) - 1, 0, max(len(z_grid) - 2, 0))
    counts = np.zeros((max(len(x_grid) - 1, 1), max(len(y_grid) - 1, 1), max(len(z_grid) - 1, 1)), dtype=np.int32)
    for i in range(len(endpoints)):
        counts[ix[i], iy[i], iz[i]] += 1
    return float(shannon_entropy(counts.reshape(-1), base=2))


def entropy_score(actions: np.ndarray, cell_size: np.ndarray) -> float:
    return float(np.mean([entropy_endpoints(actions[:, i, :], cell_size) for i in range(actions.shape[1])]))


def make_rule(c):
    rr = float(c["risk_row"])
    rm = float(c["risk_mass"])
    er = c.get("entropy_row")
    em = c.get("entropy_mass")
    er = None if er is None else float(er)
    em = None if em is None else float(em)
    mode = c["mode"]
    alpha = float(c.get("alpha", 1.0))
    fusion_threshold = c.get("fusion_threshold")
    fusion_threshold = None if fusion_threshold is None else float(fusion_threshold)
    def rule(vals):
        risk_mass = ent_mass = 0.0
        rh = eh = None
        for i, (_t, _y, r, e) in enumerate(vals):
            risk_mass += max(0.0, r - rr)
            if er is not None:
                ent_mass += max(0.0, e - er)
            if mode == "soft" and fusion_threshold is not None and risk_mass + alpha * ent_mass >= fusion_threshold:
                return i
            if rh is None and risk_mass >= rm:
                rh = i
            if er is not None and em is not None and eh is None and ent_mass >= em:
                eh = i
            if mode == "risk" and rh is not None:
                return rh
            if mode == "and" and rh is not None and eh is not None:
                return max(rh, eh)
        return None
    return rule


def eval_rule(by_ep, rule):
    succ = fail = fa = det = d10 = d25 = d50 = never = 0
    times = []
    for vals in by_ep.values():
        vals.sort(key=lambda x: x[0])
        y = max(v[1] for v in vals)
        hit = rule(vals)
        n = len(vals)
        if y:
            fail += 1
            if hit is None:
                never += 1
            else:
                det += 1
                frac = (hit + 1) / max(1, n)
                times.append(frac)
                d10 += frac <= 0.10
                d25 += frac <= 0.25
                d50 += frac <= 0.50
        else:
            succ += 1
            fa += hit is not None
    return {
        "success_fa": fa / max(1, succ),
        "failure_det": det / max(1, fail),
        "det_at_10": d10 / max(1, fail),
        "det_at_25": d25 / max(1, fail),
        "det_at_50": d50 / max(1, fail),
        "mean_time": float(np.mean(times)) if times else None,
        "never": never / max(1, fail),
        "success_episodes": succ,
        "failure_episodes": fail,
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cand = json.loads(CANDIDATES.read_text())
    cell_size = np.asarray(cand["cell_size"], dtype=np.float32)
    risk_scores = np.load(RISK_SCORES)["scores"]
    by_ep = defaultdict(list)
    for i, row in enumerate(read_jsonl(OOD_ROWS)):
        eid = str(row.get("episode_id") or row.get("episode_uid"))
        y = 1 if bool(row.get("parent_failed_or_timeout")) else 0
        t = int(row.get("timestep", i))
        ent = entropy_score(action_preds(row), cell_size)
        by_ep[eid].append((t, y, float(risk_scores[i]), ent))
    rows = []
    for c in cand["candidates"]:
        rows.append({"policy": c["policy"], "seen_success": c["seen_success"], "seen_failure": c["seen_failure"], "ood": eval_rule(by_ep, make_rule(c)), "params": c})
    rows.sort(key=lambda r: (r["ood"]["failure_det"] - r["ood"]["success_fa"], r["ood"]["failure_det"], r["ood"]["det_at_25"]), reverse=True)
    (OUT / "risk_entropy_fusion_ood180_results.json").write_text(json.dumps({"source_candidates": str(CANDIDATES), "results": rows}, indent=2, sort_keys=True) + "\n")
    lines = [
        "# Seen-Calibrated Risk + Entropy Fusion Applied to OOD180",
        "",
        "| Policy | Seen FA | Seen Det | OOD FA | OOD Det | Det@25 | Det@50 | Mean Time | Never |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows[:40]:
        ss, sf, oo = r["seen_success"], r["seen_failure"], r["ood"]
        lines.append(f"| `{r['policy']}` | {100*ss['success_fa']:.1f}% | {100*sf['failure_det']:.1f}% | {100*oo['success_fa']:.1f}% | {100*oo['failure_det']:.1f}% | {100*oo['det_at_25']:.1f}% | {100*oo['det_at_50']:.1f}% | {oo['mean_time']} | {100*oo['never']:.1f}% |")
    (OUT / "RISK_ENTROPY_FUSION_OOD180_RESULTS_20260630.md").write_text("\n".join(lines) + "\n")
    print(OUT / "RISK_ENTROPY_FUSION_OOD180_RESULTS_20260630.md")
    print("\n".join(lines[:25]))


if __name__ == "__main__":
    main()
