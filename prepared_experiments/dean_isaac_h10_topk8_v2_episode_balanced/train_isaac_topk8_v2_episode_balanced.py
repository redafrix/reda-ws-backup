#!/usr/bin/env python3
"""Train H10/TopK8 temporal risk V2 with episode-balanced/class-balanced BCE.

Scientific delta vs V1:
- same frozen Seen4000 data/splits/normalization/architecture/optimizer recipe/seed
- replace row-derived pos_weight BCE with inverse-episode-duration + episode-class-balanced row multipliers
- select checkpoint by Seen-validation episode-balanced AUPRC
- derive primary thresholds from Seen validation with episode-balanced row weights

No Isaac/Omniverse is launched by this script.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import random
import sys
import time
from typing import Any

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import (
    average_precision_score,
    precision_recall_curve,
    roc_auc_score,
)
from torch.utils.data import DataLoader, Dataset

DEFAULT_W = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
DEFAULT_PIPELINE = DEFAULT_W / "risk_head_pipeline"
DEFAULT_DATA = DEFAULT_W / "frozen_datasets/isaac_seen_h10_topk8_v1"
DEFAULT_V1 = DEFAULT_W / "models/isaac_h10_topk8_temporal_v1"
DEFAULT_OUTPUT = DEFAULT_W / "models/isaac_h10_topk8_temporal_v2_episode_balanced"

EXPECTED_DATASET_MANIFEST_SHA256 = "8e3b7f4929fce4a648f174735ec9c0530966cf4e8a93a66a3e793432a5be4859"
EXPECTED_NORMALIZATION_SHA256 = "78c934b33e0536bd7cb6b7e5b1962da32305729f602d8269d3a38422841ce050"
EXPECTED_V1_MODEL_SHA256 = "ad049519746913c4c2ce1a0b57fb32ad5c3395f5bce6841648c68cc94f862b38"
EXPECTED_COUNTS = {
    "train": {"episodes": 2800, "failures": 64, "successes": 2736, "rows": 52825},
    "validation": {"episodes": 600, "failures": 14, "successes": 586, "rows": 11410},
    "test": {"episodes": 600, "failures": 14, "successes": 586, "rows": 11368},
}


def sha256_file(path: Path) -> str:
    import hashlib

    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def write_json_atomic(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def weighted_quantile(values: np.ndarray, weights: np.ndarray, q: float) -> float:
    values = np.asarray(values, dtype=np.float64)
    weights = np.asarray(weights, dtype=np.float64)
    if values.size == 0:
        return 0.5
    if not (0.0 <= q <= 1.0):
        raise ValueError(q)
    if values.shape != weights.shape:
        raise ValueError("weighted_quantile shape mismatch")
    if np.any(weights < 0) or not np.isfinite(weights).all():
        raise ValueError("invalid weighted_quantile weights")
    order = np.argsort(values, kind="mergesort")
    v = values[order]
    w = weights[order]
    cumulative = np.cumsum(w)
    total = float(cumulative[-1])
    if total <= 0:
        raise ValueError("weighted_quantile zero total weight")
    target = q * total
    index = int(np.searchsorted(cumulative, target, side="left"))
    index = min(index, len(v) - 1)
    return float(v[index])


def weighted_threshold_table(labels: np.ndarray, scores: np.ndarray, row_weights: np.ndarray) -> dict[str, float]:
    y = labels.astype(np.int32)
    w = np.asarray(row_weights, dtype=np.float64)
    precision, recall, thresholds = precision_recall_curve(y, scores, sample_weight=w)
    f1 = 2 * precision * recall / np.maximum(precision + recall, 1e-12)
    if len(thresholds):
        index = int(np.nanargmax(f1[: len(thresholds)]))
        best = float(thresholds[index])
    else:
        best = 0.5
    success = y == 0
    return {
        "best_val_f1": best,
        "q90_success": weighted_quantile(scores[success], w[success], 0.90),
        "q95_success": weighted_quantile(scores[success], w[success], 0.95),
        "q99_success": weighted_quantile(scores[success], w[success], 0.99),
        "fixed_0.5": 0.5,
    }


def unweighted_threshold_table(labels: np.ndarray, scores: np.ndarray) -> dict[str, float]:
    y = labels.astype(np.int32)
    precision, recall, thresholds = precision_recall_curve(y, scores)
    f1 = 2 * precision * recall / np.maximum(precision + recall, 1e-12)
    if len(thresholds):
        index = int(np.nanargmax(f1[: len(thresholds)]))
        best = float(thresholds[index])
    else:
        best = 0.5
    success_scores = scores[y == 0]
    return {
        "best_val_f1": best,
        "q90_success": float(np.quantile(success_scores, 0.90)) if len(success_scores) else 0.5,
        "q95_success": float(np.quantile(success_scores, 0.95)) if len(success_scores) else 0.5,
        "q99_success": float(np.quantile(success_scores, 0.99)) if len(success_scores) else 0.5,
        "fixed_0.5": 0.5,
    }


def metric_bundle(labels: np.ndarray, scores: np.ndarray, episode_weights: np.ndarray) -> dict[str, float]:
    y = labels.astype(np.int32)
    return {
        "query_auprc": float(average_precision_score(y, scores)),
        "query_auroc": float(roc_auc_score(y, scores)),
        "episode_balanced_auprc": float(average_precision_score(y, scores, sample_weight=episode_weights)),
        "episode_balanced_auroc": float(roc_auc_score(y, scores, sample_weight=episode_weights)),
    }


def delta_bundle(v1: dict[str, float], v2: dict[str, float]) -> dict[str, float]:
    return {key: float(v2[key] - v1[key]) for key in v1.keys()}


def temporal_calibration(episode_ids: list[str], labels: np.ndarray, scores: np.ndarray, q95: float) -> dict[str, Any]:
    by_episode: dict[str, list[tuple[float, float]]] = {}
    for episode, label, score in zip(episode_ids, labels, scores, strict=True):
        by_episode.setdefault(episode, []).append((float(label), float(score)))
    success_mass: list[float] = []
    success_streak: list[int] = []
    for values in by_episode.values():
        if max(label for label, _ in values) >= 0.5:
            continue
        mass = 0.0
        streak = maximum_streak = 0
        for _, score in values:
            mass += max(0.0, score - q95)
            streak = streak + 1 if score >= q95 else 0
            maximum_streak = max(maximum_streak, streak)
        success_mass.append(mass)
        success_streak.append(maximum_streak)
    quantiles = (0.90, 0.95, 0.99)
    return {
        "base_row_threshold": "episode_balanced_q95_success",
        "conformal_mass": {
            f"q{int(q*100)}_success_final_mass": float(np.quantile(success_mass, q)) if success_mass else 0.0
            for q in quantiles
        },
        "hysteresis": {
            f"q{int(q*100)}_success_max_consecutive": int(np.ceil(np.quantile(success_streak, q))) if success_streak else 1
            for q in quantiles
        },
        "calibration_episode_count": len(by_episode),
        "calibration_success_episode_count": len(success_mass),
        "ood_used": False,
    }


def episode_structure(split_root: Path, labels: np.ndarray) -> dict[str, Any]:
    episode_index = np.asarray(np.load(split_root / "episode_index.npy", mmap_mode="r"), dtype=np.int64)
    episodes = json.loads((split_root / "episodes.json").read_text())
    if len(episode_index) != len(labels):
        raise RuntimeError(f"row mismatch in {split_root}")
    n_episodes = len(episodes)
    counts = np.bincount(episode_index, minlength=n_episodes).astype(np.int64)
    if len(counts) != n_episodes or np.any(counts <= 0):
        raise RuntimeError(f"empty/missing episode rows in {split_root}")
    episode_labels = np.full(n_episodes, np.nan, dtype=np.float64)
    for ep in range(n_episodes):
        values = np.unique(labels[episode_index == ep])
        if len(values) != 1:
            raise RuntimeError(f"mixed labels inside episode index {ep} in {split_root}: {values}")
        episode_labels[ep] = float(values[0])
    failures = episode_labels >= 0.5
    successes = ~failures
    row_counts = counts[episode_index].astype(np.float64)
    metric_weights = 1.0 / row_counts
    episode_ids = [str(episodes[int(value)]["episode_id"]) for value in episode_index]
    decision_index = np.asarray(np.load(split_root / "decision_index.npy", mmap_mode="r"), dtype=np.int64)
    return {
        "episode_index": episode_index,
        "episode_ids": episode_ids,
        "decision_index": decision_index,
        "counts": counts,
        "row_counts": row_counts,
        "episode_labels": episode_labels,
        "failure_mask_episode": failures,
        "success_mask_episode": successes,
        "n_episodes": int(n_episodes),
        "n_failures": int(failures.sum()),
        "n_successes": int(successes.sum()),
        "metric_weights": metric_weights,
    }


def train_row_multipliers(structure: dict[str, Any], labels: np.ndarray) -> tuple[np.ndarray, dict[str, Any]]:
    n_rows = len(labels)
    n_fail = structure["n_failures"]
    n_success = structure["n_successes"]
    row_counts = structure["row_counts"]
    positive = labels >= 0.5
    raw = np.empty(n_rows, dtype=np.float64)
    raw[~positive] = 0.5 / (n_success * row_counts[~positive])
    raw[positive] = 0.5 / (n_fail * row_counts[positive])
    multiplier = n_rows * raw

    ep_index = structure["episode_index"]
    ep_labels = structure["episode_labels"]
    per_episode_raw = np.bincount(ep_index, weights=raw, minlength=structure["n_episodes"])
    success_ep_weights = per_episode_raw[ep_labels < 0.5]
    failure_ep_weights = per_episode_raw[ep_labels >= 0.5]
    counts = structure["counts"]
    success_counts = counts[ep_labels < 0.5]
    failure_counts = counts[ep_labels >= 0.5]

    expected_success_ep = 0.5 / n_success
    expected_failure_ep = 0.5 / n_fail
    atol = 1e-10
    checks = {
        "success_raw_weight_sum": float(raw[~positive].sum()),
        "failure_raw_weight_sum": float(raw[positive].sum()),
        "all_success_episode_weights_equal": bool(np.allclose(success_ep_weights, expected_success_ep, atol=atol, rtol=0)),
        "all_failure_episode_weights_equal": bool(np.allclose(failure_ep_weights, expected_failure_ep, atol=atol, rtol=0)),
        "success_class_weight_sum_half": bool(abs(raw[~positive].sum() - 0.5) <= atol),
        "failure_class_weight_sum_half": bool(abs(raw[positive].sum() - 0.5) <= atol),
        "multiplier_mean_one": bool(abs(multiplier.mean() - 1.0) <= atol),
    }
    audit = {
        "schema_version": "isaac_h10_topk8_v2_weighting_audit_v1",
        "train_rows": int(n_rows),
        "success_rows": int((~positive).sum()),
        "failure_rows": int(positive.sum()),
        "success_episodes": int(n_success),
        "failure_episodes": int(n_fail),
        "success_rows_per_episode": {
            "min": int(success_counts.min()),
            "mean": float(success_counts.mean()),
            "max": int(success_counts.max()),
        },
        "failure_rows_per_episode": {
            "min": int(failure_counts.min()),
            "mean": float(failure_counts.mean()),
            "max": int(failure_counts.max()),
        },
        "success_raw_weight_sum": float(raw[~positive].sum()),
        "failure_raw_weight_sum": float(raw[positive].sum()),
        "per_success_episode_raw_weight": {
            "min": float(success_ep_weights.min()),
            "mean": float(success_ep_weights.mean()),
            "max": float(success_ep_weights.max()),
            "expected": float(expected_success_ep),
        },
        "per_failure_episode_raw_weight": {
            "min": float(failure_ep_weights.min()),
            "mean": float(failure_ep_weights.mean()),
            "max": float(failure_ep_weights.max()),
            "expected": float(expected_failure_ep),
        },
        "row_multiplier": {
            "min": float(multiplier.min()),
            "mean": float(multiplier.mean()),
            "max": float(multiplier.max()),
            "formula": "N_train_rows * 0.5 / (N_class_episodes * T_i)",
        },
        "checks": checks,
        "audit_pass": bool(all(checks.values())),
    }
    if not audit["audit_pass"]:
        raise RuntimeError("episode weighting audit failed")
    return multiplier.astype(np.float32), audit


def assert_expected_split(name: str, structure: dict[str, Any], rows: int) -> None:
    expected = EXPECTED_COUNTS[name]
    actual = {
        "episodes": structure["n_episodes"],
        "failures": structure["n_failures"],
        "successes": structure["n_successes"],
        "rows": rows,
    }
    if actual != expected:
        raise RuntimeError(f"{name} frozen split counts changed: expected={expected} actual={actual}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pipeline-root", type=Path, default=DEFAULT_PIPELINE)
    parser.add_argument("--dataset-root", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--v1-model-root", type=Path, default=DEFAULT_V1)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch-size", type=int, default=512)
    parser.add_argument("--lr", type=float, default=2e-4)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20260622)
    parser.add_argument("--cuda-memory-fraction", type=float, default=0.10)
    args = parser.parse_args()

    if (args.epochs, args.batch_size, args.lr, args.weight_decay, args.seed) != (10, 512, 2e-4, 1e-4, 20260622):
        raise ValueError("V2 controlled ablation must preserve V1 optimization recipe and seed")
    if not (0.01 <= args.cuda_memory_fraction <= 0.25):
        raise ValueError("cuda memory fraction outside frozen safety range")

    sys.path.insert(0, str(args.pipeline_root.resolve()))
    from common import episode_metrics, load_stats, normalize, step_metrics  # type: ignore
    from model import SeqRiskModel  # type: ignore

    dataset_manifest = args.dataset_root / "dataset_manifest.json"
    normalization = args.dataset_root / "normalization.json"
    if sha256_file(dataset_manifest) != EXPECTED_DATASET_MANIFEST_SHA256:
        raise RuntimeError("frozen dataset manifest hash mismatch")
    if sha256_file(normalization) != EXPECTED_NORMALIZATION_SHA256:
        raise RuntimeError("normalization hash mismatch")
    if not (args.dataset_root / "FROZEN_AND_VALIDATED").is_file():
        raise RuntimeError("frozen dataset validation marker missing")
    if sha256_file(args.v1_model_root / "model.pt") != EXPECTED_V1_MODEL_SHA256:
        raise RuntimeError("V1 model hash mismatch")
    if not torch.cuda.is_available() or os.environ.get("CUDA_VISIBLE_DEVICES") == "":
        raise RuntimeError("CUDA required to preserve V1 execution backend")

    torch.cuda.set_per_process_memory_fraction(args.cuda_memory_fraction, device=0)
    device = torch.device("cuda:0")

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)

    stats = load_stats(normalization)

    class ArrayDataset(Dataset):
        def __init__(self, root: Path, row_multiplier: np.ndarray | None = None) -> None:
            history = np.load(root / "history.npy", mmap_mode="r")
            action = np.load(root / "action.npy", mmap_mode="r")
            static = np.load(root / "static.npy", mmap_mode="r")
            self.history, self.action, self.static = normalize(history, action, static, stats)
            self.label = np.asarray(np.load(root / "label.npy", mmap_mode="r"), dtype=np.float32)
            if row_multiplier is None:
                self.row_multiplier = np.ones(len(self.label), dtype=np.float32)
            else:
                if len(row_multiplier) != len(self.label):
                    raise RuntimeError("row multiplier length mismatch")
                self.row_multiplier = np.asarray(row_multiplier, dtype=np.float32)

        def __len__(self) -> int:
            return int(self.label.shape[0])

        def __getitem__(self, index: int):
            return (
                {
                    "history": torch.from_numpy(self.history[index]),
                    "action": torch.from_numpy(self.action[index]),
                    "static": torch.from_numpy(self.static[index]),
                },
                torch.as_tensor(self.label[index], dtype=torch.float32),
                torch.as_tensor(self.row_multiplier[index], dtype=torch.float32),
            )

    def move(batch: dict[str, torch.Tensor]) -> dict[str, torch.Tensor]:
        return {key: value.to(device, non_blocking=True) for key, value in batch.items()}

    def predict(model: nn.Module, dataset: ArrayDataset) -> np.ndarray:
        loader = DataLoader(dataset, batch_size=args.batch_size * 4, shuffle=False, num_workers=args.workers, pin_memory=True, persistent_workers=args.workers > 0)
        outputs: list[np.ndarray] = []
        model.eval()
        with torch.no_grad():
            for batch, _, _ in loader:
                outputs.append(torch.sigmoid(model(move(batch))).detach().cpu().numpy())
        return np.concatenate(outputs).astype(np.float32)

    train_labels = np.asarray(np.load(args.dataset_root / "train" / "label.npy", mmap_mode="r"), dtype=np.float32)
    val_labels = np.asarray(np.load(args.dataset_root / "validation" / "label.npy", mmap_mode="r"), dtype=np.float32)
    test_labels = np.asarray(np.load(args.dataset_root / "test" / "label.npy", mmap_mode="r"), dtype=np.float32)
    train_structure = episode_structure(args.dataset_root / "train", train_labels)
    val_structure = episode_structure(args.dataset_root / "validation", val_labels)
    test_structure = episode_structure(args.dataset_root / "test", test_labels)
    assert_expected_split("train", train_structure, len(train_labels))
    assert_expected_split("validation", val_structure, len(val_labels))
    assert_expected_split("test", test_structure, len(test_labels))

    multipliers, weighting_audit = train_row_multipliers(train_structure, train_labels)

    output = args.output_root.resolve()
    if output == args.v1_model_root.resolve():
        raise RuntimeError("V2 output cannot overwrite V1")
    output.mkdir(parents=True, exist_ok=True)
    write_json_atomic(output / "WEIGHTING_AUDIT.json", weighting_audit)

    training_config = {
        "schema_version": "isaac_h10_topk8_v2_training_config_v1",
        "scientific_delta": "episode-balanced/class-balanced BCE and episode-balanced Seen-validation checkpoint selection only",
        "dataset_manifest_sha256": sha256_file(dataset_manifest),
        "normalization_sha256": sha256_file(normalization),
        "v1_model_sha256": sha256_file(args.v1_model_root / "model.pt"),
        "pipeline_model_py_sha256": sha256_file(args.pipeline_root / "model.py"),
        "pipeline_common_py_sha256": sha256_file(args.pipeline_root / "common.py"),
        "architecture": {"model": "SeqRiskModel", "history_shape": [16, 21], "action_shape": [10, 7], "static_dim": 51, "width": 128, "layers": 3, "heads": 4, "ffn": 512, "dropout": 0.1},
        "optimization": {"optimizer": "AdamW", "lr": args.lr, "weight_decay": args.weight_decay, "epochs": args.epochs, "batch_size": args.batch_size, "gradient_clip_norm": 1.0, "seed": args.seed, "loss": "episode-balanced class-balanced BCE", "old_v1_pos_weight_used": False},
        "device": "cuda:0",
        "cuda_memory_fraction_cap": args.cuda_memory_fraction,
        "ood150_used_for_training_or_selection": False,
        "ood400_used": False,
        "hard1000_used_for_training": False,
    }
    write_json_atomic(output / "TRAINING_CONFIG.json", training_config)

    train = ArrayDataset(args.dataset_root / "train", multipliers)
    validation = ArrayDataset(args.dataset_root / "validation")
    test = ArrayDataset(args.dataset_root / "test")

    model = SeqRiskModel().to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    state_path = output / "last_training_state.pt"
    history: list[dict[str, Any]] = []
    best_metric = -1.0
    best_epoch = 0
    best_state: dict[str, torch.Tensor] | None = None
    start_epoch = 1
    if state_path.is_file():
        state = torch.load(state_path, map_location="cpu", weights_only=False)
        model.load_state_dict(state["model"])
        optimizer.load_state_dict(state["optimizer"])
        history = list(state["history"])
        best_metric = float(state["best_episode_balanced_auprc"])
        best_epoch = int(state["best_epoch"])
        best_state = state["best_state"]
        start_epoch = int(state["completed_epoch"]) + 1

    started = time.time()
    val_metric_weights = val_structure["metric_weights"]
    for epoch in range(start_epoch, args.epochs + 1):
        generator = torch.Generator().manual_seed(args.seed + epoch)
        loader = DataLoader(train, batch_size=args.batch_size, shuffle=True, generator=generator, num_workers=args.workers, pin_memory=True, persistent_workers=args.workers > 0, drop_last=False)
        model.train()
        weighted_loss_sum = 0.0
        seen_rows = 0
        epoch_start = time.time()
        for batch, labels, row_multiplier in loader:
            optimizer.zero_grad(set_to_none=True)
            batch = move(batch)
            labels = labels.to(device, non_blocking=True)
            row_multiplier = row_multiplier.to(device, non_blocking=True)
            logits = model(batch)
            query_loss = F.binary_cross_entropy_with_logits(logits, labels, reduction="none")
            loss = torch.mean(query_loss * row_multiplier)
            if not torch.isfinite(loss):
                raise RuntimeError(f"nonfinite V2 training loss in epoch {epoch}")
            loss.backward()
            gradient_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            if not torch.isfinite(gradient_norm):
                raise RuntimeError(f"nonfinite gradient norm in epoch {epoch}")
            optimizer.step()
            weighted_loss_sum += float((query_loss.detach() * row_multiplier).sum().cpu())
            seen_rows += int(labels.numel())

        val_scores = predict(model, validation)
        metrics = metric_bundle(validation.label, val_scores, val_metric_weights)
        record = {
            "epoch": epoch,
            "train_episode_balanced_class_balanced_loss": weighted_loss_sum / max(1, seen_rows),
            "validation_query_auprc": metrics["query_auprc"],
            "validation_query_auroc": metrics["query_auroc"],
            "validation_episode_balanced_auprc": metrics["episode_balanced_auprc"],
            "validation_episode_balanced_auroc": metrics["episode_balanced_auroc"],
            "epoch_seconds": time.time() - epoch_start,
            "rows_per_second": len(train) / max(1e-9, time.time() - epoch_start),
        }
        history.append(record)
        print("RISK_V2_TRAIN_EPOCH_JSON=" + json.dumps(record, sort_keys=True), flush=True)
        if metrics["episode_balanced_auprc"] > best_metric:
            best_metric = metrics["episode_balanced_auprc"]
            best_epoch = epoch
            best_state = {key: value.detach().cpu().clone() for key, value in model.state_dict().items()}
        temporary = state_path.with_suffix(".tmp")
        torch.save({"completed_epoch": epoch, "model": model.state_dict(), "optimizer": optimizer.state_dict(), "history": history, "best_episode_balanced_auprc": best_metric, "best_epoch": best_epoch, "best_state": best_state}, temporary)
        temporary.replace(state_path)

    if best_state is None:
        raise RuntimeError("V2 training did not produce a best checkpoint")
    model.load_state_dict(best_state)
    model_path = output / "model.pt"
    torch.save(model.state_dict(), model_path)

    val_scores = predict(model, validation)
    test_scores = predict(model, test)
    primary_thresholds = weighted_threshold_table(validation.label, val_scores, val_structure["metric_weights"])
    legacy_thresholds = unweighted_threshold_table(validation.label, val_scores)
    temporal = temporal_calibration(val_structure["episode_ids"], validation.label, val_scores, primary_thresholds["q95_success"])

    write_json_atomic(output / "thresholds.json", primary_thresholds)
    write_json_atomic(output / "legacy_query_thresholds.json", legacy_thresholds)
    write_json_atomic(output / "temporal_thresholds.json", temporal)

    v2_val_metrics = metric_bundle(validation.label, val_scores, val_structure["metric_weights"])
    v2_test_metrics = metric_bundle(test.label, test_scores, test_structure["metric_weights"])

    v1_model = SeqRiskModel().to(device)
    v1_model.load_state_dict(torch.load(args.v1_model_root / "model.pt", map_location="cpu"))
    v1_val_scores = predict(v1_model, validation)
    v1_test_scores = predict(v1_model, test)
    v1_val_metrics = metric_bundle(validation.label, v1_val_scores, val_structure["metric_weights"])
    v1_test_metrics = metric_bundle(test.label, v1_test_scores, test_structure["metric_weights"])

    v1_saved_thresholds = json.loads((args.v1_model_root / "thresholds.json").read_text())
    v1_episode_balanced_thresholds = weighted_threshold_table(validation.label, v1_val_scores, val_structure["metric_weights"])

    comparison = {
        "schema_version": "isaac_h10_topk8_v1_v2_seen_comparison_v1",
        "identical_frozen_dataset_manifest_sha256": sha256_file(dataset_manifest),
        "identical_normalization_sha256": sha256_file(normalization),
        "v1": {"model_sha256": sha256_file(args.v1_model_root / "model.pt"), "training_objective": "query-row-weighted BCE with row-derived pos_weight", "saved_seen_thresholds": v1_saved_thresholds, "recomputed_episode_balanced_seen_thresholds_for_analysis_only": v1_episode_balanced_thresholds},
        "v2": {"model_sha256": sha256_file(model_path), "training_objective": "episode-balanced class-balanced BCE", "primary_seen_thresholds": primary_thresholds, "legacy_query_seen_thresholds": legacy_thresholds},
        "seen_validation": {"v1": v1_val_metrics, "v2": v2_val_metrics, "delta_v2_minus_v1": delta_bundle(v1_val_metrics, v2_val_metrics)},
        "seen_test": {"v1": v1_test_metrics, "v2": v2_test_metrics, "delta_v2_minus_v1": delta_bundle(v1_test_metrics, v2_test_metrics)},
        "v2_checkpoint_selection": "highest Seen-validation episode-balanced AUPRC",
        "ood150_used_for_training_selection_or_thresholding": False,
        "ood400_touched": False,
    }
    write_json_atomic(output / "V1_V2_SEEN_COMPARISON.json", comparison)

    results: dict[str, Any] = {
        "schema_version": "simvla_isaac_topk8_training_result_v2_episode_balanced",
        "architecture": training_config["architecture"],
        "optimization": training_config["optimization"],
        "dataset_root": str(args.dataset_root.resolve()),
        "dataset_manifest_sha256": sha256_file(dataset_manifest),
        "normalization_path": str(normalization.resolve()),
        "normalization_sha256": sha256_file(normalization),
        "weighting_audit": weighting_audit,
        "best_epoch": best_epoch,
        "best_validation_episode_balanced_auprc": best_metric,
        "history": history,
        "primary_episode_balanced_thresholds": primary_thresholds,
        "legacy_query_thresholds": legacy_thresholds,
        "temporal_calibration": temporal,
        "seen_validation_metrics": v2_val_metrics,
        "seen_test_metrics": v2_test_metrics,
        "seen_threshold_results": {"validation": {}, "test": {}},
        "ood150_used_for_training_or_selection": False,
        "ood400_used": False,
        "hard1000_used_for_training": False,
        "runtime_seconds": time.time() - started,
    }
    for name, threshold in primary_thresholds.items():
        results["seen_threshold_results"]["validation"][name] = {
            "query": step_metrics(validation.label, val_scores, float(threshold)),
            "episode": episode_metrics(val_structure["episode_ids"], val_structure["decision_index"], validation.label, val_scores, float(threshold)),
        }
        results["seen_threshold_results"]["test"][name] = {
            "query": step_metrics(test.label, test_scores, float(threshold)),
            "episode": episode_metrics(test_structure["episode_ids"], test_structure["decision_index"], test.label, test_scores, float(threshold)),
        }
    write_json_atomic(output / "TRAINING_HISTORY.json", history)
    write_json_atomic(output / "results.json", results)
    np.savez_compressed(output / "seen_scores.npz", validation_labels=validation.label, validation_scores=val_scores, validation_episode_weights=val_structure["metric_weights"], test_labels=test.label, test_scores=test_scores, test_episode_weights=test_structure["metric_weights"], v1_validation_scores=v1_val_scores, v1_test_scores=v1_test_scores)

    manifest = {
        "schema_version": "simvla_isaac_topk8_model_manifest_v2_episode_balanced",
        "model_path": str(model_path),
        "model_sha256": sha256_file(model_path),
        "results_sha256": sha256_file(output / "results.json"),
        "thresholds_sha256": sha256_file(output / "thresholds.json"),
        "legacy_query_thresholds_sha256": sha256_file(output / "legacy_query_thresholds.json"),
        "normalization_sha256": sha256_file(normalization),
        "dataset_manifest_sha256": sha256_file(dataset_manifest),
        "best_epoch": best_epoch,
        "best_validation_episode_balanced_auprc": best_metric,
        "selection_metric": "Seen-validation episode-balanced AUPRC",
        "ood150_used": False,
        "ood400_used": False,
        "training_complete": True,
    }
    write_json_atomic(output / "model_manifest.json", manifest)
    (output / "TRAINING_COMPLETE").write_text("complete\n")
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
