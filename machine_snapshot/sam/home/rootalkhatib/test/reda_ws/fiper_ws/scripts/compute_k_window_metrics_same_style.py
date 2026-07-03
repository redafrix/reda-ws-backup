#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np


def import_eval_module(path: Path):
    spec = importlib.util.spec_from_file_location("ood_eval_mod", str(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def summarize_threshold(rows, scores, *, mode: str, threshold: float, k: int = 1, mass_threshold: float = 0.0):
    by_ep = defaultdict(list)
    for r, score in zip(rows, scores):
        by_ep[r.episode_id].append((r, float(score)))

    succ = fail = fa = det = det10 = det25 = det50 = never = 0
    det_fracs = []
    per_task = defaultdict(Counter)

    for _eid, vals in by_ep.items():
        vals.sort(key=lambda x: x[0].timestep)
        y = max(v[0].y for v in vals)
        task = vals[0][0].task_id
        first_idx = None

        if mode == "k":
            run = 0
            for i, (_row, score) in enumerate(vals):
                if score >= threshold:
                    run += 1
                    if run >= k:
                        first_idx = i - k + 1
                        break
                else:
                    run = 0
        elif mode == "mass":
            mass = 0.0
            for i, (_row, score) in enumerate(vals):
                mass += max(0.0, score - threshold)
                if mass >= mass_threshold:
                    first_idx = i
                    break
        else:
            raise ValueError(mode)

        n = max(1, len(vals))
        if y >= 0.5:
            fail += 1
            per_task[task]["fail"] += 1
            if first_idx is None:
                never += 1
            else:
                det += 1
                per_task[task]["det"] += 1
                frac = (first_idx + 1) / n
                det_fracs.append(frac)
                if frac <= 0.10:
                    det10 += 1
                if frac <= 0.25:
                    det25 += 1
                if frac <= 0.50:
                    det50 += 1
        else:
            succ += 1
            per_task[task]["succ"] += 1
            if first_idx is not None:
                fa += 1
                per_task[task]["fa"] += 1

    return {
        "success_eps": succ,
        "failure_eps": fail,
        "false_alarm_count": fa,
        "detected_count": det,
        "fa": fa / max(1, succ),
        "det": det / max(1, fail),
        "det10": det10 / max(1, fail),
        "det25": det25 / max(1, fail),
        "det50": det50 / max(1, fail),
        "mean_time": float(np.mean(det_fracs)) if det_fracs else None,
        "never": never / max(1, fail),
        "per_task": {str(k): dict(v) for k, v in sorted(per_task.items())},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset-root", required=True, type=Path)
    ap.add_argument("--eval-script", required=True, type=Path)
    ap.add_argument("--scores-npz", required=True, type=Path)
    ap.add_argument("--results-json", required=True, type=Path)
    ap.add_argument("--out-json", required=True, type=Path)
    args = ap.parse_args()

    mod = import_eval_module(args.eval_script)
    rows_path, summaries_path = mod.find_dataset_files(args.dataset_root)
    rows = mod.load_rows(rows_path, summaries_path)
    scores = np.load(args.scores_npz)["scores"].astype(np.float32)
    if len(rows) != len(scores):
        raise RuntimeError(f"row/score mismatch: rows={len(rows)} scores={len(scores)}")
    results = json.loads(args.results_json.read_text())
    thresholds = results["thresholds"]
    q95 = float(thresholds["q95"])
    q99 = float(thresholds.get("q99", np.quantile(scores, 0.99)))
    conformal_mass = float(thresholds.get("conformal_mass", 0.15))

    out = {}
    for th_name, th in [("q95", q95), ("q99", q99)]:
        for k in [1, 2, 3, 5, 10]:
            out[f"score_{th_name}_K{k}"] = summarize_threshold(rows, scores, mode="k", threshold=float(th), k=k)
    out["score_q95_mass_conformal_0p15"] = summarize_threshold(rows, scores, mode="mass", threshold=q95, mass_threshold=conformal_mass)
    for mass in [1, 5, 10, 20, 50, 100]:
        out[f"score_q95_mass_{mass}"] = summarize_threshold(rows, scores, mode="mass", threshold=q95, mass_threshold=float(mass))

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    for key in ["score_q95_K3", "score_q99_K3", "score_q95_mass_conformal_0p15", "score_q95_mass_10", "score_q95_mass_20", "score_q95_mass_50"]:
        m = out[key]
        print(
            f"{key:32s} FA={100*m['fa']:.1f}% Det={100*m['det']:.1f}% "
            f"Det10={100*m['det10']:.1f}% Det25={100*m['det25']:.1f}% Det50={100*m['det50']:.1f}% "
            f"Mean={m['mean_time']} Never={100*m['never']:.1f}%"
        )


if __name__ == "__main__":
    main()
