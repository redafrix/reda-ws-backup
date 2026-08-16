"""Shared immutable TopK8 feature, normalization, and metric contract."""

from __future__ import annotations

from collections import defaultdict
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

import numpy as np

TOPK8_INDICES = (6, 21, 25, 27, 23, 2, 26, 24)
HISTORY_SHAPE = (16, 21)
ACTION_SHAPE = (10, 7)
STATIC_DIM = 51
FEATURE_SCHEMA_VERSION = "simvla_isaac_topk8_h10_v1"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json_atomic(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def action_statistics(action: np.ndarray) -> np.ndarray:
    action = np.asarray(action, dtype=np.float32)
    if action.shape != ACTION_SHAPE:
        raise ValueError(f"action shape {action.shape} != {ACTION_SHAPE}")
    return np.concatenate(
        [action[0], action.mean(axis=0), action.std(axis=0), action[-1] - action[0]]
    ).astype(np.float32)


def feature_tensors(row: dict[str, Any]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    history = np.asarray(row["history"], dtype=np.float32)
    action = np.asarray(row["main_candidate_action_chunk_normalized"], dtype=np.float32)
    ace = np.asarray(row["ace_features_7d"], dtype=np.float32)
    proprio = np.asarray(row["current"]["proprio"], dtype=np.float32)
    uncertainty = np.asarray(row["simvla_uncertainty_49d"], dtype=np.float32)
    if history.shape != HISTORY_SHAPE:
        raise ValueError(f"history shape {history.shape} != {HISTORY_SHAPE}")
    if action.shape != ACTION_SHAPE:
        raise ValueError(f"action shape {action.shape} != {ACTION_SHAPE}")
    if ace.shape != (7,) or proprio.shape != (8,) or uncertainty.shape != (49,):
        raise ValueError(
            f"invalid static inputs: ace={ace.shape} proprio={proprio.shape} "
            f"uncertainty={uncertainty.shape}"
        )
    static = np.concatenate(
        [action_statistics(action), ace, proprio, uncertainty[list(TOPK8_INDICES)]]
    ).astype(np.float32)
    if static.shape != (STATIC_DIM,):
        raise RuntimeError(f"static shape {static.shape} != {(STATIC_DIM,)}")
    for name, value in (("history", history), ("action", action), ("static", static)):
        if not np.isfinite(value).all():
            raise ValueError(f"nonfinite {name} feature")
    return history, action, static


def fit_normalization(
    history: np.ndarray, action: np.ndarray, static: np.ndarray
) -> dict[str, dict[str, np.ndarray]]:
    stats = {
        "history": {
            "mean": np.asarray(history.mean(axis=(0, 1), keepdims=True), dtype=np.float32),
            "std": np.asarray(history.std(axis=(0, 1), keepdims=True), dtype=np.float32),
        },
        "action": {
            "mean": np.asarray(action.mean(axis=(0, 1), keepdims=True), dtype=np.float32),
            "std": np.asarray(action.std(axis=(0, 1), keepdims=True), dtype=np.float32),
        },
        "static": {
            "mean": np.asarray(static.mean(axis=0, keepdims=True), dtype=np.float32),
            "std": np.asarray(static.std(axis=0, keepdims=True), dtype=np.float32),
        },
    }
    for values in stats.values():
        values["std"] = np.maximum(values["std"], 1e-6)
        if not all(np.isfinite(value).all() for value in values.values()):
            raise ValueError("nonfinite training normalization")
    return stats


def serialize_stats(
    stats: dict[str, dict[str, np.ndarray]], *, provenance: dict[str, Any]
) -> dict[str, Any]:
    return {
        "schema_version": "simvla_isaac_topk8_training_normalization_v1",
        "feature_schema_version": FEATURE_SCHEMA_VERSION,
        "fit_split": "train",
        "provenance": provenance,
        "stats": {
            name: {key: value.tolist() for key, value in values.items()}
            for name, values in stats.items()
        },
    }


def load_stats(path: Path) -> dict[str, dict[str, np.ndarray]]:
    payload = json.loads(path.read_text())
    raw = payload.get("stats", payload)
    return {
        name: {key: np.asarray(value, dtype=np.float32) for key, value in values.items()}
        for name, values in raw.items()
    }


def normalize(
    history: np.ndarray,
    action: np.ndarray,
    static: np.ndarray,
    stats: dict[str, dict[str, np.ndarray]],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return (
        ((history - stats["history"]["mean"]) / stats["history"]["std"]).astype(np.float32),
        ((action - stats["action"]["mean"]) / stats["action"]["std"]).astype(np.float32),
        ((static - stats["static"]["mean"]) / stats["static"]["std"]).astype(np.float32),
    )


def threshold_table(labels: np.ndarray, scores: np.ndarray) -> dict[str, float]:
    from sklearn.metrics import precision_recall_curve

    precision, recall, thresholds = precision_recall_curve(labels.astype(int), scores)
    f1 = 2 * precision * recall / np.maximum(precision + recall, 1e-9)
    if len(thresholds):
        index = int(np.nanargmax(f1[: len(thresholds)]))
        best = float(thresholds[index])
    else:
        best = 0.5
    success = scores[labels < 0.5]
    return {
        "best_val_f1": best,
        "q90_success": float(np.quantile(success, 0.90)) if len(success) else 0.5,
        "q95_success": float(np.quantile(success, 0.95)) if len(success) else 0.5,
        "q99_success": float(np.quantile(success, 0.99)) if len(success) else 0.5,
        "fixed_0.5": 0.5,
    }


def step_metrics(labels: np.ndarray, scores: np.ndarray, threshold: float) -> dict[str, Any]:
    from sklearn.metrics import accuracy_score, average_precision_score, f1_score, roc_auc_score

    y = labels.astype(np.int32)
    prediction = (scores >= threshold).astype(np.int32)
    tp = int(((prediction == 1) & (y == 1)).sum())
    tn = int(((prediction == 0) & (y == 0)).sum())
    fp = int(((prediction == 1) & (y == 0)).sum())
    fn = int(((prediction == 0) & (y == 1)).sum())
    return {
        "auroc": float(roc_auc_score(y, scores)) if len(set(y.tolist())) == 2 else 0.5,
        "auprc": float(average_precision_score(y, scores)) if len(set(y.tolist())) == 2 else float(y.mean()),
        "f1": float(f1_score(y, prediction, zero_division=0)),
        "accuracy": float(accuracy_score(y, prediction)),
        "fpr": fp / max(1, fp + tn),
        "fnr": fn / max(1, fn + tp),
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
    }


def episode_metrics(
    episode_ids: Iterable[str],
    decision_indices: Iterable[int],
    labels: np.ndarray,
    scores: np.ndarray,
    threshold: float,
) -> dict[str, Any]:
    grouped: dict[str, list[tuple[int, float, float]]] = defaultdict(list)
    for episode, decision, label, score in zip(
        episode_ids, decision_indices, labels, scores, strict=True
    ):
        grouped[str(episode)].append((int(decision), float(label), float(score)))
    success = failure = false_alarm = detected = det10 = det25 = det50 = never = 0
    fractions: list[float] = []
    for values in grouped.values():
        values.sort()
        label = max(item[1] for item in values)
        hits = [index for index, item in enumerate(values) if item[2] >= threshold]
        if label >= 0.5:
            failure += 1
            if hits:
                detected += 1
                fraction = (hits[0] + 1) / len(values)
                fractions.append(fraction)
                det10 += int(fraction <= 0.10)
                det25 += int(fraction <= 0.25)
                det50 += int(fraction <= 0.50)
            else:
                never += 1
        else:
            success += 1
            false_alarm += int(bool(hits))
    return {
        "episodes": len(grouped),
        "success_episodes": success,
        "failure_episodes": failure,
        "episode_success_false_alarm_rate": false_alarm / max(1, success),
        "failure_detection_rate": detected / max(1, failure),
        "det_at_10": det10 / max(1, failure),
        "det_at_25": det25 / max(1, failure),
        "det_at_50": det50 / max(1, failure),
        "mean_detection_fraction": float(np.mean(fractions)) if fractions else None,
        "never_count": never,
    }
