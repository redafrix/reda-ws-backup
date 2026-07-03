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
OUT_ROOT = MODEL_DIR.parent / "unc_topk8_risk_entropy_fusion_seen_calibration_20260630"
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


def compute_cell_size(calib_eids: set[str]) -> np.ndarray:
    chunks = []
    used = 0
    for row in read_jsonl(QUERY_PATH):
        if str(row["episode_id"]) not in calib_eids:
            continue
        a = action_preds(row)
        chunks.append(a.reshape(-1, a.shape[-1]))
        used += 1
    positions = np.concatenate(chunks, axis=0)
    ranges = positions.max(axis=0) - positions.min(axis=0)
    max_range = float(ranges.max())
    ranges = np.where(ranges == 0, max_range, ranges)
    print(f"[entropy] cell-size rows={used}", flush=True)
    return (ranges * 0.01).astype(np.float32)


def build_entropy_map(target_eids: set[str], cell_size: np.ndarray) -> dict[tuple[str, int], float]:
    out = {}
    seen = 0
    for row in read_jsonl(QUERY_PATH):
        eid = str(row["episode_id"])
        if eid not in target_eids:
            continue
        out[(eid, int(row["timestep"]))] = entropy_score(action_preds(row), cell_size)
        seen += 1
        if seen % 10000 == 0:
            print(f"[entropy] scored rows={seen}", flush=True)
    print(f"[entropy] scored total={seen}", flush=True)
    return out


def group_rows(risk_scores, ent_scores, ids, timesteps, episodes):
    groups = defaultdict(list)
    for r, e, eid, t in zip(risk_scores, ent_scores, ids, timesteps):
        groups[eid].append((int(t), float(r), float(e)))
    for vals in groups.values():
        vals.sort(key=lambda x: x[0])
    return groups


def metrics(groups, episodes, rule):
    succ = fail = fa = det = det10 = det25 = det50 = 0
    times = []
    for eid, vals in groups.items():
        meta = episodes[eid]
        hit = rule(vals)
        if meta.success:
            succ += 1
            fa += hit is not None
        else:
            fail += 1
            if hit is not None:
                det += 1
                frac = vals[hit][0] / max(1, meta.num_steps)
                times.append(frac)
                det10 += frac <= 0.10
                det25 += frac <= 0.25
                det50 += frac <= 0.50
    return {
        "success_episodes": succ,
        "failure_episodes": fail,
        "success_fa": fa / max(1, succ),
        "failure_det": det / max(1, fail),
        "det_at_10": det10 / max(1, fail),
        "det_at_25": det25 / max(1, fail),
        "det_at_50": det50 / max(1, fail),
        "mean_time": float(np.mean(times)) if times else None,
        "never": 1.0 - det / max(1, fail),
        "false_alarm_count": int(fa),
        "detected_failure_count": int(det),
    }


def mass_rule(risk_row, risk_mass, ent_row=None, ent_mass=None, mode="risk", alpha=1.0, fusion_threshold=None):
    def rule(vals):
        rm = em = 0.0
        rh = eh = None
        for i, (_t, r, e) in enumerate(vals):
            rm += max(0.0, r - risk_row)
            if ent_row is not None:
                em += max(0.0, e - ent_row)
            if mode == "soft" and fusion_threshold is not None and rm + alpha * em >= fusion_threshold:
                return i
            if rh is None and rm >= risk_mass:
                rh = i
            if ent_row is not None and ent_mass is not None and eh is None and em >= ent_mass:
                eh = i
            if mode == "risk" and rh is not None:
                return rh
            if mode == "entropy" and eh is not None:
                return eh
            if mode == "and" and rh is not None and eh is not None:
                return max(rh, eh)
            if mode == "or" and (rh is not None or eh is not None):
                return min(x for x in [rh, eh] if x is not None)
        return None
    return rule


def final_fusion_masses(groups, risk_row, ent_row, alpha):
    vals = []
    for ep_vals in groups.values():
        rm = em = 0.0
        for _t, r, e in ep_vals:
            rm += max(0.0, r - risk_row)
            em += max(0.0, e - ent_row)
        vals.append(rm + alpha * em)
    return np.asarray(vals, dtype=np.float64)


def main():
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
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

    success_val = rows_by_bucket["success_val_seen"]
    failure_val = rows_by_bucket["failure_val_seen"]
    calib_eids = {r.episode_id for r in rows_by_bucket["success_calib_seen"]}
    target_eids = {r.episode_id for r in success_val} | {r.episode_id for r in failure_val}

    cell_size = compute_cell_size(calib_eids)
    ent_map = build_entropy_map(target_eids, cell_size)

    stats = load_norm(MODEL_DIR / "normalization.json")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = mod.SeqRiskModel(hist_dim=21, action_dim=7, static_dim=51, width=128, layers=3, heads=4, dropout=0.1, static_input_dropout=0.0).to(device)
    model.load_state_dict(torch.load(MODEL_DIR / "model.pt", map_location=device))
    model.eval()

    scored = {}
    for name, rows in [("success_val_seen", success_val), ("failure_val_seen", failure_val)]:
        print(f"[risk] scoring {name} rows={len(rows)} eps={len(set(r.episode_id for r in rows))}", flush=True)
        scores, _y, ids, ts = mod.score_rows(model, stats, rows, VARIANT, args.batch_size, device)
        ent = np.asarray([ent_map[(eid, int(t))] for eid, t in zip(ids, ts)], dtype=np.float32)
        scored[name] = (scores, ent, ids, ts)

    success_groups = group_rows(*scored["success_val_seen"], episodes)
    failure_groups = group_rows(*scored["failure_val_seen"], episodes)
    both_groups = {**success_groups, **failure_groups}

    calib_ent_scores = []
    for row in read_jsonl(QUERY_PATH):
        if str(row["episode_id"]) in calib_eids:
            calib_ent_scores.append(entropy_score(action_preds(row), cell_size))
    calib_ent_scores = np.asarray(calib_ent_scores)

    risk_rows = {
        "risk_q95": float(json.loads((MODEL_DIR / "thresholds.json").read_text())["q95"]),
        "risk_q99": float(json.loads((MODEL_DIR / "thresholds.json").read_text())["q99"]),
    }
    ent_rows = {
        "ent_q75": float(np.quantile(calib_ent_scores, 0.75)),
        "ent_q90": float(np.quantile(calib_ent_scores, 0.90)),
        "ent_q95": float(np.quantile(calib_ent_scores, 0.95)),
    }
    risk_masses = [0.056, 0.1, 0.2, 0.5, 1.0, 2.0]
    ent_masses = [0.0, 0.02, 0.05, 0.1, 0.15, 0.25, 0.5]

    candidates = []
    for rn, rr in risk_rows.items():
        for rm in risk_masses:
            candidates.append((f"{rn}_mass_{rm:g}", rn, rr, rm, None, None, None, "risk"))
            for en, er in ent_rows.items():
                for em in ent_masses:
                    candidates.append((f"{rn}_mass_{rm:g}_AND_{en}_mass_{em:g}", rn, rr, rm, en, er, em, "and"))

    # Soft fusion: cumulative risk excess plus alpha times cumulative entropy excess.
    # Thresholds are chosen only from seen validation successes/failures.
    soft_candidates = []
    for rn, rr in risk_rows.items():
        for en, er in ent_rows.items():
            for alpha in [0.1, 0.25, 0.5, 1.0, 2.0]:
                succ_final = final_fusion_masses(success_groups, rr, er, alpha)
                fail_final = final_fusion_masses(failure_groups, rr, er, alpha)
                grid = np.unique(np.concatenate([
                    np.quantile(succ_final, np.linspace(0, 1, 301)),
                    np.quantile(fail_final, np.linspace(0, 1, 301)),
                    np.asarray([0.02, 0.05, 0.1, 0.15, 0.25, 0.5, 1, 2, 5, 10, 20, 50], dtype=np.float64),
                ]))
                for target_fa in [0.01, 0.025, 0.05, 0.10]:
                    th = float(np.quantile(succ_final, 1.0 - target_fa))
                    soft_candidates.append((f"soft_{rn}_{en}_a{alpha:g}_FA{int(target_fa*1000):03d}", rn, rr, 0.0, en, er, None, "soft", alpha, th))


    rows = []
    all_candidates = [(name, rn, rr, rm, en, er, em, mode, 1.0, None) for name, rn, rr, rm, en, er, em, mode in candidates]
    all_candidates.extend(soft_candidates)
    for name, rn, rr, rm, en, er, em, mode, alpha, fusion_threshold in all_candidates:
        rule = mass_rule(rr, rm, er, em, mode, alpha=alpha, fusion_threshold=fusion_threshold)
        ms = metrics(success_groups, episodes, rule)
        mf = metrics(failure_groups, episodes, rule)
        score = (mf["failure_det"] - ms["success_fa"], mf["failure_det"], mf["det_at_25"], -(mf["mean_time"] or 999), -ms["success_fa"])
        rows.append({
            "policy": name, "risk_row_name": rn, "risk_row": rr, "risk_mass": rm,
            "entropy_row_name": en, "entropy_row": er, "entropy_mass": em, "mode": mode,
            "alpha": alpha, "fusion_threshold": fusion_threshold,
            "seen_success": ms, "seen_failure": mf, "selection_score": score,
        })

    rows.sort(key=lambda x: x["selection_score"], reverse=True)
    out = {
        "protocol": "candidate fusion thresholds selected only from seen validation success/failure",
        "cell_size": cell_size.tolist(),
        "risk_rows": risk_rows,
        "entropy_rows": ent_rows,
        "candidate_count": len(rows),
        "candidates": rows,
    }
    (OUT_ROOT / "risk_entropy_seen_fusion_candidates.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    lines = ["# Seen-Calibrated Risk + Entropy Fusion Candidates", "", "| Policy | Seen Success FA | Seen Failure Det | Det@25 | Det@50 | Mean Time |", "|---|---:|---:|---:|---:|---:|"]
    for r in rows[:120]:
        ms, mf = r["seen_success"], r["seen_failure"]
        lines.append(f"| `{r['policy']}` | {100*ms['success_fa']:.1f}% | {100*mf['failure_det']:.1f}% | {100*mf['det_at_25']:.1f}% | {100*mf['det_at_50']:.1f}% | {mf['mean_time']} |")
    (OUT_ROOT / "RISK_ENTROPY_SEEN_FUSION_CANDIDATES_20260630.md").write_text("\n".join(lines) + "\n")
    print(f"[done] {OUT_ROOT}", flush=True)


if __name__ == "__main__":
    main()
