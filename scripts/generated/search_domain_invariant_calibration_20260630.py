#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

SEEN = Path("/tmp/seen_val_risk_entropy_sequences_20260630.json")
OOD = Path("/tmp/ood180_risk_entropy_sequences_20260630.json")
OUT = Path("/tmp/domain_invariant_calibration_search_20260630.json")


def load(path: Path):
    return json.loads(path.read_text())["episodes"]


def arr(ep, key):
    return np.asarray(ep[key], dtype=np.float64)


def score_series(ep, signal, family, base_k=3, margin=0.0, window=3):
    x = arr(ep, signal)
    if len(x) == 0:
        return np.asarray([], dtype=np.float64)
    k = min(max(1, base_k), len(x))
    base = float(np.median(x[:k]))
    mad = float(np.median(np.abs(x[:k] - base))) + 1e-6
    if family == "raw":
        s = x
    elif family == "drift":
        s = x - base - margin
    elif family == "zdrift":
        s = (x - base) / mad - margin
    elif family == "slope":
        prev = np.concatenate([[x[0]], x[:-1]])
        s = x - prev - margin
    elif family == "ema_drift":
        ema = np.zeros_like(x)
        ema[0] = x[0]
        for i in range(1, len(x)):
            ema[i] = 0.8 * ema[i - 1] + 0.2 * x[i - 1]
        s = x - ema - margin
    elif family == "local_jump":
        s = np.zeros_like(x)
        for i in range(len(x)):
            j0 = max(0, i - window)
            s[i] = x[i] - np.median(x[j0:i + 1]) - margin
    else:
        raise ValueError(family)
    return np.maximum(0.0, s)


def episode_stat(ep, cfg):
    sr = score_series(ep, "risk", cfg["risk_family"], cfg["base_k"], cfg["risk_margin"], cfg["window"])
    se = score_series(ep, "entropy", cfg["entropy_family"], cfg["base_k"], cfg["entropy_margin"], cfg["window"])
    if cfg["combine"] == "risk":
        v = sr
    elif cfg["combine"] == "entropy":
        v = se
    elif cfg["combine"] == "sum":
        v = sr + cfg["alpha"] * se
    elif cfg["combine"] == "and_min":
        v = np.minimum(sr, cfg["alpha"] * se)
    elif cfg["combine"] == "risk_gate_entropy":
        v = sr * (se > 0)
    else:
        raise ValueError(cfg["combine"])
    if cfg["aggregate"] == "mass":
        return float(np.sum(v))
    if cfg["aggregate"] == "max":
        return float(np.max(v)) if len(v) else 0.0
    if cfg["aggregate"] == "top3mean":
        if len(v) == 0:
            return 0.0
        vv = np.sort(v)[-min(3, len(v)):]
        return float(np.mean(vv))
    raise ValueError(cfg["aggregate"])


def first_alarm(ep, cfg, threshold):
    sr = score_series(ep, "risk", cfg["risk_family"], cfg["base_k"], cfg["risk_margin"], cfg["window"])
    se = score_series(ep, "entropy", cfg["entropy_family"], cfg["base_k"], cfg["entropy_margin"], cfg["window"])
    if cfg["combine"] == "risk":
        v = sr
    elif cfg["combine"] == "entropy":
        v = se
    elif cfg["combine"] == "sum":
        v = sr + cfg["alpha"] * se
    elif cfg["combine"] == "and_min":
        v = np.minimum(sr, cfg["alpha"] * se)
    elif cfg["combine"] == "risk_gate_entropy":
        v = sr * (se > 0)
    else:
        raise ValueError(cfg["combine"])
    if cfg["aggregate"] == "mass":
        c = np.cumsum(v)
    elif cfg["aggregate"] == "max":
        c = np.maximum.accumulate(v)
    elif cfg["aggregate"] == "top3mean":
        vals = []
        top = []
        for vi in v:
            top.append(float(vi))
            top = sorted(top)[-3:]
            vals.append(float(np.mean(top)))
        c = np.asarray(vals)
    else:
        raise ValueError(cfg["aggregate"])
    hit = np.flatnonzero(c >= threshold)
    return None if len(hit) == 0 else int(hit[0])


def eval_cfg(eps, cfg, threshold):
    succ = fail = fa = det = d10 = d25 = d50 = never = 0
    times = []
    for ep in eps:
        hit = first_alarm(ep, cfg, threshold)
        n = max(1, len(ep["t"]))
        if ep["label"]:
            fail += 1
            if hit is None:
                never += 1
            else:
                det += 1
                frac = (hit + 1) / n
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
    seen = load(SEEN)
    ood = load(OOD)
    seen_s = [e for e in seen if e["label"] == 0]
    seen_f = [e for e in seen if e["label"] == 1]
    configs = []
    for risk_family in ["raw", "drift", "zdrift", "ema_drift"]:
        for entropy_family in ["raw", "drift", "zdrift", "ema_drift"]:
            for combine in ["risk", "entropy", "sum", "and_min"]:
                for aggregate in ["mass", "max"]:
                    for base_k in [1, 3, 5]:
                        for alpha in [0.25, 1, 4]:
                            if combine in ["risk", "entropy"] and alpha != 1:
                                continue
                            configs.append({
                                "risk_family": risk_family,
                                "entropy_family": entropy_family,
                                "combine": combine,
                                "aggregate": aggregate,
                                "base_k": base_k,
                                "window": 3,
                                "alpha": alpha,
                                "risk_margin": 0.0,
                                "entropy_margin": 0.0,
                            })
    results = []
    for cfg in configs:
        succ_stats = np.asarray([episode_stat(e, cfg) for e in seen_s], dtype=np.float64)
        if not np.any(np.isfinite(succ_stats)):
            continue
        for target_fa in [0.01, 0.025, 0.05, 0.10]:
            th = float(np.quantile(succ_stats, 1.0 - target_fa))
            ms = eval_cfg(seen_s, cfg, th)
            mf = eval_cfg(seen_f, cfg, th)
            mo = eval_cfg(ood, cfg, th)
            results.append({"cfg": cfg, "threshold": th, "target_fa": target_fa, "seen_success": ms, "seen_failure": mf, "ood": mo})
    results.sort(key=lambda r: (
        r["ood"]["failure_det"] - r["ood"]["success_fa"],
        r["ood"]["failure_det"],
        r["seen_failure"]["failure_det"],
        -r["ood"]["success_fa"],
    ), reverse=True)
    OUT.write_text(json.dumps({"results": results}, indent=2, sort_keys=True) + "\n")
    print("TOP OOD RAW")
    for r in results[:20]:
        print_line(r)
    print("\nFILTERED seen_det>=0.85 seen_fa<=0.10")
    filt = [r for r in results if r["seen_failure"]["failure_det"] >= 0.85 and r["seen_success"]["success_fa"] <= 0.10]
    filt.sort(key=lambda r: (r["ood"]["failure_det"] - r["ood"]["success_fa"], r["ood"]["failure_det"], -r["ood"]["success_fa"]), reverse=True)
    for r in filt[:30]:
        print_line(r)


def print_line(r):
    c = r["cfg"]
    ss, sf, oo = r["seen_success"], r["seen_failure"], r["ood"]
    name = f"{c['combine']}:{c['aggregate']}:r={c['risk_family']}:e={c['entropy_family']}:k={c['base_k']}:a={c['alpha']}:fa={r['target_fa']}"
    print(
        name,
        "th", round(r["threshold"], 4),
        "seenFA", round(100 * ss["success_fa"], 1),
        "seenDet", round(100 * sf["failure_det"], 1),
        "oodFA", round(100 * oo["success_fa"], 1),
        "oodDet", round(100 * oo["failure_det"], 1),
        "d25", round(100 * oo["det_at_25"], 1),
        "d50", round(100 * oo["det_at_50"], 1),
        "mean", oo["mean_time"],
    )


if __name__ == "__main__":
    main()
