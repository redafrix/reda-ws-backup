from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import numpy as np


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -50.0, 50.0)))


def auroc(y: np.ndarray, score: np.ndarray) -> float | None:
    y = np.asarray(y).astype(int)
    score = np.asarray(score).astype(float)
    pos = y == 1
    neg = y == 0
    if pos.sum() == 0 or neg.sum() == 0:
        return None
    order = np.argsort(score)
    ranks = np.empty_like(order, dtype=np.float64)
    ranks[order] = np.arange(1, len(score) + 1)
    return float((ranks[pos].sum() - pos.sum() * (pos.sum() + 1) / 2.0) / (pos.sum() * neg.sum()))


def auprc(y: np.ndarray, score: np.ndarray) -> float | None:
    y = np.asarray(y).astype(int)
    score = np.asarray(score).astype(float)
    if y.sum() == 0:
        return None
    order = np.argsort(-score)
    yy = y[order]
    tp = np.cumsum(yy)
    precision = tp / (np.arange(len(yy)) + 1)
    return float((precision * yy).sum() / max(1, yy.sum()))


def ece_score(y: np.ndarray, prob: np.ndarray, bins: int = 15) -> float | None:
    y = np.asarray(y).astype(float)
    prob = np.asarray(prob).astype(float)
    if len(y) == 0:
        return None
    ece = 0.0
    for i in range(bins):
        lo, hi = i / bins, (i + 1) / bins
        mask = (prob >= lo) & ((prob < hi) if i < bins - 1 else (prob <= hi))
        if mask.any():
            ece += float(mask.mean() * abs(prob[mask].mean() - y[mask].mean()))
    return ece


def brier(y: np.ndarray, prob: np.ndarray) -> float | None:
    if len(y) == 0:
        return None
    return float(np.mean((np.asarray(prob).astype(float) - np.asarray(y).astype(float)) ** 2))


def nll(y: np.ndarray, prob: np.ndarray) -> float | None:
    if len(y) == 0:
        return None
    p = np.clip(np.asarray(prob).astype(float), 1e-6, 1 - 1e-6)
    yy = np.asarray(y).astype(float)
    return float(-np.mean(yy * np.log(p) + (1.0 - yy) * np.log(1.0 - p)))


def threshold_metrics(y: np.ndarray, prob: np.ndarray, thresholds: list[float] | None = None) -> dict[str, Any]:
    y = np.asarray(y).astype(int)
    prob = np.asarray(prob).astype(float)
    thresholds = thresholds or [0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9]
    out: dict[str, Any] = {}
    for thr in thresholds:
        pred_bad = prob >= thr
        tp = int(((pred_bad == 1) & (y == 1)).sum())
        fp = int(((pred_bad == 1) & (y == 0)).sum())
        tn = int(((pred_bad == 0) & (y == 0)).sum())
        fn = int(((pred_bad == 0) & (y == 1)).sum())
        out[f"{thr:.2f}"] = {
            "tp": tp,
            "fp": fp,
            "tn": tn,
            "fn": fn,
            "precision_bad": float(tp / max(1, tp + fp)),
            "recall_bad": float(tp / max(1, tp + fn)),
            "accepted_count": int((~pred_bad).sum()),
            "accepted_bad_count": fn,
            "accepted_bad_leakage": float(fn / max(1, int((~pred_bad).sum()))),
            "good_strong_kept_rate": float(tn / max(1, tn + fp)),
        }
    return out


def accepted_risk_table(y: np.ndarray, prob: np.ndarray, accept_fracs: list[float] | None = None) -> dict[str, Any]:
    y = np.asarray(y).astype(int)
    prob = np.asarray(prob).astype(float)
    accept_fracs = accept_fracs or [0.90, 0.75, 0.50, 0.25]
    order = np.argsort(prob)
    out: dict[str, Any] = {}
    total_bad_rate = float(y.mean()) if len(y) else 0.0
    for frac in accept_fracs:
        k = max(1, int(round(len(y) * frac)))
        accepted = order[:k]
        rejected = order[k:]
        accepted_bad = int(y[accepted].sum())
        rejected_bad = int(y[rejected].sum()) if len(rejected) else 0
        out[f"accept_{int(frac * 100)}pct"] = {
            "accepted_count": int(k),
            "accepted_bad_count": accepted_bad,
            "accepted_bad_leakage": float(accepted_bad / max(1, k)),
            "rejected_count": int(len(rejected)),
            "rejected_bad_count": rejected_bad,
            "rejected_bad_rate": float(rejected_bad / max(1, len(rejected))),
            "rejected_bad_enrichment": float((rejected_bad / max(1, len(rejected))) / max(1e-9, total_bad_rate)),
            "risk_threshold": float(prob[accepted].max()) if len(accepted) else None,
        }
    return out


def binary_metrics(labels: list[str], probs: list[float], include_uncertain_as_safe: bool = False) -> dict[str, Any]:
    selected_y: list[int] = []
    selected_p: list[float] = []
    for label, prob in zip(labels, probs):
        if label == "VALIDATED_BAD":
            selected_y.append(1)
            selected_p.append(prob)
        elif label == "GOOD_STRONG" or include_uncertain_as_safe:
            selected_y.append(0)
            selected_p.append(prob)
    y = np.asarray(selected_y, dtype=np.int64)
    p = np.asarray(selected_p, dtype=np.float64)
    return {
        "n": int(len(y)),
        "bad_count": int(y.sum()) if len(y) else 0,
        "bad_rate": float(y.mean()) if len(y) else None,
        "auroc_bad": auroc(y, p),
        "auprc_bad": auprc(y, p),
        "brier": brier(y, p),
        "ece": ece_score(y, p),
        "nll": nll(y, p),
        "threshold_metrics": threshold_metrics(y, p) if len(y) else {},
        "accepted_risk": accepted_risk_table(y, p) if len(y) else {},
    }


def subtype_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_subtype: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_subtype[str(row.get("bad_subtype") or "unknown")].append(row)
    out: dict[str, Any] = {}
    for subtype, items in by_subtype.items():
        labels = [str(x["label"]) for x in items]
        probs = [float(x["risk_prob"]) for x in items]
        out[subtype] = binary_metrics(labels, probs, include_uncertain_as_safe=True)
    return out


def summarize_predictions(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_split: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_split[str(row.get("split") or "unknown")].append(row)
    summary: dict[str, Any] = {}
    for split, items in by_split.items():
        labels = [str(x["label"]) for x in items]
        probs = [float(x["risk_prob"]) for x in items]
        summary[split] = {
            "label_counts": dict(Counter(labels)),
            "clean_binary": binary_metrics(labels, probs, include_uncertain_as_safe=False),
            "bad_vs_all_non_bad": binary_metrics(labels, probs, include_uncertain_as_safe=True),
            "subtype": subtype_metrics(items),
        }
    return summary


def write_predictions(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True, default=str) + "\n")


def read_predictions(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open() as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_eval_report(path: Path, config: dict[str, Any], metrics: dict[str, Any]) -> None:
    lines = [
        "# Stage 9 Risk Model Eval",
        "",
        "## Config",
        "",
        "```json",
        json.dumps(config, indent=2, sort_keys=True, default=str),
        "```",
        "",
        "## Metrics",
        "",
    ]
    for split, values in metrics.get("splits", {}).items():
        clean = values.get("clean_binary", {})
        all_non_bad = values.get("bad_vs_all_non_bad", {})
        lines.extend(
            [
                f"### {split}",
                "",
                f"- labels: `{values.get('label_counts')}`",
                f"- clean AUROC BAD: `{clean.get('auroc_bad')}`",
                f"- clean AUPRC BAD: `{clean.get('auprc_bad')}`",
                f"- clean Brier: `{clean.get('brier')}`",
                f"- all-label accepted BAD leakage @ accept 90%: `{(all_non_bad.get('accepted_risk') or {}).get('accept_90pct', {}).get('accepted_bad_leakage')}`",
                "",
            ]
        )
    path.write_text("\n".join(lines) + "\n")


def finite_or_none(value: Any) -> Any:
    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        return None
    return value
