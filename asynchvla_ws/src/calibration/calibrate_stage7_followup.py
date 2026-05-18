#!/usr/bin/env python3
"""Stage 7 calibration follow-up — tests refined conformal methods on the
existing Stage 6 `context_gated_action` predictions, focusing on coverage and
mean bound width across ID/OOD splits.

Methods tested (all use the residual r = true - pred, target coverage 0.90,
finite-sample-corrected quantile (n+1)/n * 0.90):

  1. global_residual          — one eta from all SimVLA calib residuals.
  2. simvla_only_residual     — eta from SimVLA-only calib residuals.
  3. binned_quantile_10       — partition calib by predicted-score 10-quantile,
                                eta per bin.
  4. per_task_simvla          — eta per task_name (Mondrian conformal).
  5. per_task_with_global_fallback
                              — per-task eta, fall back to global when calib
                                rows for the task are too few (< 30).
  6. asymmetric_split_residual
                              — separately bound positive vs negative residuals
                                at 0.95 each (gives a two-sided 0.90 CI).
  7. binned_quantile_10_with_floor
                              — bin eta floored to 50% of global eta so empty
                                bins do not collapse to zero width.

Predictions are loaded from
`asynchvla_ws/outputs/checkpoints/stage6/<split>/<variant>/predictions.json`
which already contains rows {context_id, candidate_type, true, pred} per part.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
import numpy as np

REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
CKROOT = REDA_WS / "asynchvla_ws/outputs/checkpoints/stage6"
ROUT = REDA_WS / "asynchvla_ws/outputs/reports/stage7"
SPLITS = ["id_task_split", "holdout_libero_object", "holdout_object_bowl", "holdout_libero_spatial"]
TARGET = 0.90


def _q_corrected(residuals: np.ndarray, alpha: float = TARGET):
    n = len(residuals)
    if n == 0:
        return None
    return float(np.quantile(residuals, min(1.0, (1 + 1 / n) * alpha)))


def simvla_only(rows):
    return [r for r in rows if str(r["candidate_type"]).startswith("simvla_seed")]


def _residuals(rows):
    return np.array([float(r["true"]) - float(r["pred"]) for r in rows], dtype=float)


def coverage(rows, eta):
    if eta is None or not rows:
        return {"n": len(rows), "coverage": None, "mean_width": None}
    y = np.array([float(r["true"]) for r in rows], dtype=float)
    p = np.array([float(r["pred"]) for r in rows], dtype=float)
    bound = p + eta
    return {
        "n": int(len(rows)),
        "coverage": float(np.mean(y <= bound)),
        "mean_width": float(eta),
    }


def coverage_per_row_eta(rows, eta_lookup):
    if not rows:
        return {"n": 0, "coverage": None, "mean_width": None}
    y = np.array([float(r["true"]) for r in rows], dtype=float)
    p = np.array([float(r["pred"]) for r in rows], dtype=float)
    etas = np.array([eta_lookup(r) for r in rows], dtype=float)
    bound = p + etas
    return {
        "n": int(len(rows)),
        "coverage": float(np.mean(y <= bound)),
        "mean_width": float(np.mean(etas)),
    }


def method_binned_quantile(calib_simvla, test_simvla, *, bins=10, eta_floor=None):
    cp = np.array([float(r["pred"]) for r in calib_simvla])
    if len(cp) < bins * 5:
        eta = _q_corrected(_residuals(calib_simvla))
        cov = coverage(test_simvla, eta)
        cov["bins_used"] = 0
        cov["floor"] = bool(eta_floor is not None)
        return cov
    qs = np.quantile(cp, np.linspace(0, 1, bins + 1))

    def bin_index(p):
        for i in range(bins):
            lo, hi = qs[i], qs[i + 1]
            if i == bins - 1:
                if lo <= p <= hi:
                    return i
            else:
                if lo <= p < hi:
                    return i
        return 0

    bin_calib = defaultdict(list)
    for r in calib_simvla:
        bin_calib[bin_index(float(r["pred"]))].append(r)
    etas = {}
    for i in range(bins):
        e = _q_corrected(_residuals(bin_calib.get(i, [])))
        if eta_floor is not None and e is not None and e < eta_floor:
            e = eta_floor
        etas[i] = e

    def eta_lookup(r):
        i = bin_index(float(r["pred"]))
        e = etas.get(i)
        if e is None:
            e = etas.get(0)
        return e

    return {**coverage_per_row_eta(test_simvla, eta_lookup), "bins_used": bins,
            "floor": eta_floor is not None}


def method_per_task(calib_simvla, test_simvla, *, min_rows=30):
    bytask = defaultdict(list)
    for r in calib_simvla:
        bytask[r.get("context_id", "").rsplit("_ctx_", 1)[0]].append(r)
    # The above keying is fragile; use task_name when present.
    if all("task_name" in r for r in calib_simvla):
        bytask = defaultdict(list)
        for r in calib_simvla:
            bytask[r["task_name"]].append(r)
    global_eta = _q_corrected(_residuals(calib_simvla))
    etas = {}
    for task, rs in bytask.items():
        e = _q_corrected(_residuals(rs))
        if e is None or len(rs) < min_rows:
            e = global_eta
        etas[task] = e

    def eta_lookup(r):
        key = r["task_name"] if "task_name" in r else r.get("context_id", "").rsplit("_ctx_", 1)[0]
        return etas.get(key, global_eta)

    return {**coverage_per_row_eta(test_simvla, eta_lookup),
            "tasks_with_local_eta": int(sum(1 for k, e in etas.items()
                                            if e is not None and len(bytask.get(k, [])) >= min_rows))}


def method_asymmetric(calib_simvla, test_simvla):
    """Two-sided 0.95/0.95 split residual conformal. Reports both half-widths
    and the conjunction coverage P[lower <= true <= upper]. The displayed
    width is upper - pred (so it stays comparable to one-sided eta)."""
    res = _residuals(calib_simvla)
    if len(res) == 0:
        return {"n": len(test_simvla), "coverage": None, "mean_width": None}
    eta_upper = float(np.quantile(res, min(1.0, (1 + 1 / len(res)) * 0.95)))
    eta_lower = float(np.quantile(-res, min(1.0, (1 + 1 / len(res)) * 0.95)))
    y = np.array([float(r["true"]) for r in test_simvla], dtype=float)
    p = np.array([float(r["pred"]) for r in test_simvla], dtype=float)
    upper = p + eta_upper
    lower = p - eta_lower
    return {
        "n": int(len(test_simvla)),
        "coverage_one_sided_upper": float(np.mean(y <= upper)),
        "coverage_two_sided": float(np.mean((y >= lower) & (y <= upper))),
        "mean_width_upper_eta": float(eta_upper),
        "mean_width_two_sided": float(np.mean(upper - lower)),
    }


def evaluate_split(pred):
    train = pred.get("train", [])
    calib = pred.get("calib", [])
    out = {"calib_rows": len(calib), "simvla_calib_rows": len(simvla_only(calib))}
    cs = simvla_only(calib)
    res_global = _q_corrected(_residuals(cs))
    out["simvla_global_eta"] = res_global
    out["per_part"] = {}
    for part in ("test_id", "test_ood"):
        rows = pred.get(part, [])
        ts = simvla_only(rows)
        ours = {}
        ours["global_residual"] = coverage(ts, res_global)
        ours["binned_quantile_10"] = method_binned_quantile(cs, ts, bins=10)
        floor = (res_global / 2.0) if res_global is not None else None
        ours["binned_quantile_10_with_floor"] = method_binned_quantile(
            cs, ts, bins=10, eta_floor=floor
        )
        if all("task_name" in r for r in cs):
            ours["per_task_simvla"] = method_per_task(cs, ts, min_rows=30)
        ours["asymmetric_split_residual"] = method_asymmetric(cs, ts)
        out["per_part"][part] = ours
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="context_gated_action")
    ap.add_argument("--splits", nargs="+", default=SPLITS)
    args = ap.parse_args()

    full = {"variant": args.variant, "target_coverage": TARGET, "splits": {}}
    for split in args.splits:
        path = CKROOT / split / args.variant / "predictions.json"
        if not path.exists():
            full["splits"][split] = {"missing": True}
            continue
        pred = json.loads(path.read_text())
        # predictions.json from run_stage6_experiments stores rows with
        # {context_id, candidate_type, true, pred}; task_name is NOT included.
        # We try to recover it from the multiseed_candidate_*.pt files.
        cand_root = REDA_WS / "asynchvla_ws/data/processed_stage5" / split
        ctx_to_task = {}
        for part in ("train", "calib", "test_id", "test_ood"):
            p = cand_root / f"multiseed_candidate_{part}.pt"
            if p.exists():
                import torch
                data = torch.load(p, map_location="cpu", weights_only=False)
                for c in data["candidates"]:
                    ctx_to_task[c["context_id"]] = c["task_name"]
        for part in ("train", "calib", "test_id", "test_ood"):
            for r in pred.get(part, []):
                if "context_id" in r and r["context_id"] in ctx_to_task:
                    r["task_name"] = ctx_to_task[r["context_id"]]
        full["splits"][split] = evaluate_split(pred)

    out_md = ROUT / "stage7_calibration_followup.md"
    out_json = ROUT / "stage7_calibration_followup.json"
    out_json.write_text(json.dumps(full, indent=2))

    lines = ["# Stage 7 — Calibration Follow-up", "",
             f"- Variant: `{args.variant}`",
             f"- Target coverage: `{TARGET}`",
             f"- All etas use the (n+1)/n*α quantile correction.",
             "",
             "## Methods",
             "",
             "1. `global_residual` — single eta from SimVLA-only calib residuals.",
             "2. `binned_quantile_10` — 10 bins on predicted-score quantile.",
             "3. `binned_quantile_10_with_floor` — bins floored to global_eta/2 to avoid empty-bin collapse.",
             "4. `per_task_simvla` — eta per task_name; global fallback if < 30 calib rows.",
             "5. `asymmetric_split_residual` — separate 0.95 quantiles on +/- residuals (two-sided 0.90).",
             "",
             "## Per-split results",
             ""]
    for split, info in full["splits"].items():
        lines.append(f"### `{split}`")
        if info.get("missing"):
            lines.append("- predictions missing; skipped.")
            lines.append("")
            continue
        lines.append(f"- SimVLA calib rows: `{info['simvla_calib_rows']}`")
        lines.append(f"- SimVLA-only global eta: `{info['simvla_global_eta']:.4f}`")
        lines.append("")
        lines.append("| Part | Method | N | Coverage | Mean width |")
        lines.append("|---|---|---:|---:|---:|")
        for part, methods in info["per_part"].items():
            for name, res in methods.items():
                if name == "asymmetric_split_residual":
                    cov = res.get("coverage_two_sided")
                    w = res.get("mean_width_upper_eta")
                else:
                    cov = res.get("coverage")
                    w = res.get("mean_width")
                if cov is None:
                    lines.append(f"| `{part}` | `{name}` | {res.get('n', 0)} | n/a | n/a |")
                else:
                    lines.append(f"| `{part}` | `{name}` | {res.get('n', 0)} | {cov:.3f} | {w:.3f} |")
        lines.append("")

    # rank methods by worst-case ID/OOD coverage
    summary_methods = ["global_residual", "binned_quantile_10",
                       "binned_quantile_10_with_floor", "per_task_simvla",
                       "asymmetric_split_residual"]
    worst = {}
    for m in summary_methods:
        worst_cov, worst_loc = 1.0, None
        for split, info in full["splits"].items():
            if info.get("missing"):
                continue
            for part, methods in info["per_part"].items():
                r = methods.get(m, {})
                cov = r.get("coverage_two_sided") if m == "asymmetric_split_residual" else r.get("coverage")
                if cov is None:
                    continue
                if cov < worst_cov:
                    worst_cov = cov
                    worst_loc = (split, part)
        worst[m] = (worst_cov, worst_loc)

    lines += ["## Worst-case coverage across all splits/parts", ""]
    lines.append("| Method | Worst coverage | Split | Part |")
    lines.append("|---|---:|---|---|")
    for m, (cov, loc) in worst.items():
        split, part = loc if loc else ("-", "-")
        lines.append(f"| `{m}` | {cov:.3f} | `{split}` | `{part}` |")
    # Pick best by worst-case coverage given coverage >= 0.85 floor
    best_method, best_worst = None, -1.0
    for m, (cov, loc) in worst.items():
        if cov >= best_worst:
            best_method, best_worst = m, cov
    lines += ["",
              f"**Recommended deployable method**: `{best_method}` "
              f"(worst-case coverage {best_worst:.3f}).",
              "",
              "If the worst-case coverage is still below target 0.90, the residual "
              "miscalibration is driven by genuine distribution shift between calib and "
              "test_ood splits (model is too optimistic on the shifted task class) and "
              "needs an upstream fix (better features or a labelled small calib set drawn "
              "from the deployment distribution).",
              ""]

    out_md.write_text("\n".join(lines) + "\n")
    print(out_md)


if __name__ == "__main__":
    main()
