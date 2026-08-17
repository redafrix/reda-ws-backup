#!/usr/bin/env python3
"""Train one exact promoted H10/TopK8 temporal risk head on frozen seen data."""

from __future__ import annotations

import argparse
import copy
import json
import os
from pathlib import Path
import random
import shutil
import sys
import time
from typing import Any

import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import average_precision_score, roc_auc_score
from torch.utils.data import DataLoader, Dataset

PIPELINE = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE))

from common import (  # noqa: E402
    episode_metrics,
    load_stats,
    normalize,
    sha256_file,
    step_metrics,
    threshold_table,
    write_json_atomic,
)
from model import SeqRiskModel  # noqa: E402

PROMOTED_TRAINER = Path(
    "/media/redafrix/My Passport1/reda_ws/fiper_ws/"
    "cross_suite_official_ood_20260630/scripts/"
    "train_seen_goal_object_to_many_ood_20260630.py"
)
PROMOTED_TRAINER_SHA256 = (
    "5657b5d10ca67daf910a1e537e9b7a5743cacc86a8ff7ef13fbacf435007e89e"
)
DEFAULT_DATA = PIPELINE.parent / "frozen_datasets/isaac_seen_h10_topk8_v1"
DEFAULT_OUTPUT = PIPELINE.parent / "models/isaac_h10_topk8_temporal_v1"


class ArrayDataset(Dataset):
    def __init__(self, root: Path, stats: dict[str, dict[str, np.ndarray]]) -> None:
        history = np.load(root / "history.npy", mmap_mode="r")
        action = np.load(root / "action.npy", mmap_mode="r")
        static = np.load(root / "static.npy", mmap_mode="r")
        self.history, self.action, self.static = normalize(history, action, static, stats)
        self.label = np.asarray(np.load(root / "label.npy", mmap_mode="r"), dtype=np.float32)

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
        )


def move(batch: dict[str, torch.Tensor], device: torch.device) -> dict[str, torch.Tensor]:
    return {key: value.to(device, non_blocking=True) for key, value in batch.items()}


def predict(
    model: nn.Module,
    dataset: ArrayDataset,
    device: torch.device,
    batch_size: int,
    workers: int,
) -> np.ndarray:
    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=workers,
        pin_memory=True,
        persistent_workers=workers > 0,
    )
    outputs: list[np.ndarray] = []
    model.eval()
    with torch.no_grad():
        for batch, _ in loader:
            outputs.append(
                torch.sigmoid(model(move(batch, device))).detach().cpu().numpy()
            )
    return np.concatenate(outputs).astype(np.float32)


def load_row_identity(split_root: Path) -> tuple[list[str], np.ndarray]:
    episodes = json.loads((split_root / "episodes.json").read_text())
    index = np.load(split_root / "episode_index.npy", mmap_mode="r")
    decision = np.asarray(np.load(split_root / "decision_index.npy", mmap_mode="r"))
    ids = [str(episodes[int(value)]["episode_id"]) for value in index]
    return ids, decision


def temporal_calibration(
    episode_ids: list[str], labels: np.ndarray, scores: np.ndarray, q95: float
) -> dict[str, Any]:
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
        "base_row_threshold": "q95_success",
        "conformal_mass": {
            f"q{int(q*100)}_success_final_mass": float(np.quantile(success_mass, q))
            if success_mass
            else 0.0
            for q in quantiles
        },
        "hysteresis": {
            f"q{int(q*100)}_success_max_consecutive": int(
                np.ceil(np.quantile(success_streak, q))
            )
            if success_streak
            else 1
            for q in quantiles
        },
        "calibration_episode_count": len(by_episode),
        "calibration_success_episode_count": len(success_mass),
        "ood_used": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch-size", type=int, default=512)
    parser.add_argument("--lr", type=float, default=2e-4)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20260622)
    args = parser.parse_args()
    if (args.epochs, args.batch_size, args.lr, args.weight_decay) != (
        10,
        512,
        2e-4,
        1e-4,
    ):
        raise ValueError("production training must preserve the promoted recipe")
    if sha256_file(PROMOTED_TRAINER) != PROMOTED_TRAINER_SHA256:
        raise RuntimeError("authoritative promoted trainer hash changed")
    if not (args.dataset_root / "FROZEN_AND_VALIDATED").is_file():
        raise RuntimeError("frozen dataset has not passed its commit gate")
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is required for the production risk-head trainer")
    if os.environ.get("CUDA_VISIBLE_DEVICES") == "":
        raise RuntimeError("CUDA was explicitly disabled")

    output = args.output_root.resolve()
    output.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PROMOTED_TRAINER, output / "promoted_trainer_reference.py")
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    device = torch.device("cuda:0")
    stats = load_stats(args.dataset_root / "normalization.json")
    train = ArrayDataset(args.dataset_root / "train", stats)
    validation = ArrayDataset(args.dataset_root / "validation", stats)
    test = ArrayDataset(args.dataset_root / "test", stats)
    train_labels = train.label
    negative = float((train_labels < 0.5).sum())
    positive = float((train_labels >= 0.5).sum())
    positive_weight = max(1.0, negative / max(1.0, positive))

    model = SeqRiskModel().to(device)
    loss_fn = nn.BCEWithLogitsLoss(
        pos_weight=torch.tensor([positive_weight], device=device)
    )
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=args.lr, weight_decay=args.weight_decay
    )
    state_path = output / "last_training_state.pt"
    history: list[dict[str, Any]] = []
    best_auprc = -1.0
    best_epoch = 0
    best_state: dict[str, torch.Tensor] | None = None
    start_epoch = 1
    if state_path.is_file():
        state = torch.load(state_path, map_location="cpu", weights_only=False)
        model.load_state_dict(state["model"])
        optimizer.load_state_dict(state["optimizer"])
        history = list(state["history"])
        best_auprc = float(state["best_auprc"])
        best_epoch = int(state["best_epoch"])
        best_state = state["best_state"]
        start_epoch = int(state["completed_epoch"]) + 1

    started = time.time()
    for epoch in range(start_epoch, args.epochs + 1):
        generator = torch.Generator().manual_seed(args.seed + epoch)
        loader = DataLoader(
            train,
            batch_size=args.batch_size,
            shuffle=True,
            generator=generator,
            num_workers=args.workers,
            pin_memory=True,
            persistent_workers=args.workers > 0,
            drop_last=False,
        )
        model.train()
        losses: list[float] = []
        epoch_start = time.time()
        for batch, labels in loader:
            optimizer.zero_grad(set_to_none=True)
            batch = move(batch, device)
            labels = labels.to(device, non_blocking=True)
            loss = loss_fn(model(batch), labels)
            if not torch.isfinite(loss):
                raise RuntimeError(f"nonfinite training loss in epoch {epoch}")
            loss.backward()
            gradient_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            if not torch.isfinite(gradient_norm):
                raise RuntimeError(f"nonfinite gradient norm in epoch {epoch}")
            optimizer.step()
            losses.append(float(loss.detach().cpu()))
        validation_scores = predict(
            model, validation, device, args.batch_size * 4, args.workers
        )
        validation_labels = validation.label.astype(np.int32)
        validation_auprc = float(
            average_precision_score(validation_labels, validation_scores)
        )
        validation_auroc = float(roc_auc_score(validation_labels, validation_scores))
        record = {
            "epoch": epoch,
            "train_loss": float(np.mean(losses)),
            "validation_auprc": validation_auprc,
            "validation_auroc": validation_auroc,
            "epoch_seconds": time.time() - epoch_start,
            "rows_per_second": len(train) / max(1e-9, time.time() - epoch_start),
        }
        history.append(record)
        print("RISK_TRAIN_EPOCH_JSON=" + json.dumps(record, sort_keys=True), flush=True)
        if validation_auprc > best_auprc:
            best_auprc = validation_auprc
            best_epoch = epoch
            best_state = {
                key: value.detach().cpu().clone()
                for key, value in model.state_dict().items()
            }
        temporary = state_path.with_suffix(".tmp")
        torch.save(
            {
                "completed_epoch": epoch,
                "model": model.state_dict(),
                "optimizer": optimizer.state_dict(),
                "history": history,
                "best_auprc": best_auprc,
                "best_epoch": best_epoch,
                "best_state": best_state,
            },
            temporary,
        )
        temporary.replace(state_path)
    if best_state is None:
        raise RuntimeError("training did not produce a best validation checkpoint")
    model.load_state_dict(best_state)
    model_path = output / "model.pt"
    torch.save(model.state_dict(), model_path)

    validation_scores = predict(model, validation, device, args.batch_size * 4, args.workers)
    test_scores = predict(model, test, device, args.batch_size * 4, args.workers)
    thresholds = threshold_table(validation.label, validation_scores)
    validation_ids, validation_decisions = load_row_identity(args.dataset_root / "validation")
    test_ids, test_decisions = load_row_identity(args.dataset_root / "test")
    temporal = temporal_calibration(
        validation_ids, validation.label, validation_scores, thresholds["q95_success"]
    )
    results: dict[str, Any] = {
        "schema_version": "simvla_isaac_topk8_training_result_v1",
        "architecture": {
            "model": "one SeqRiskModel",
            "history_shape": [16, 21],
            "action_shape": [10, 7],
            "static_dim": 51,
            "width": 128,
            "layers": 3,
            "heads": 4,
            "ffn": 512,
            "dropout": 0.1,
        },
        "optimization": {
            "loss": "weighted BCEWithLogitsLoss",
            "positive_weight": positive_weight,
            "optimizer": "AdamW",
            "lr": args.lr,
            "weight_decay": args.weight_decay,
            "epochs": args.epochs,
            "batch_size": args.batch_size,
            "gradient_clip_norm": 1.0,
            "selection": "highest seen-validation AUPRC",
            "training_seed": args.seed,
        },
        "promoted_trainer": {
            "path": str(PROMOTED_TRAINER),
            "sha256": PROMOTED_TRAINER_SHA256,
        },
        "dataset_root": str(args.dataset_root.resolve()),
        "dataset_manifest_sha256": sha256_file(args.dataset_root / "dataset_manifest.json"),
        "normalization_path": str((args.dataset_root / "normalization.json").resolve()),
        "normalization_sha256": sha256_file(args.dataset_root / "normalization.json"),
        "best_epoch": best_epoch,
        "best_validation_auprc": best_auprc,
        "history": history,
        "thresholds": thresholds,
        "temporal_calibration": temporal,
        "seen_validation": {},
        "seen_test": {},
        "ood150_used_for_training_or_selection": False,
        "runtime_seconds": time.time() - started,
    }
    for name, threshold in thresholds.items():
        results["seen_validation"][name] = {
            "step": step_metrics(validation.label, validation_scores, threshold),
            "episode": episode_metrics(
                validation_ids,
                validation_decisions,
                validation.label,
                validation_scores,
                threshold,
            ),
        }
        results["seen_test"][name] = {
            "step": step_metrics(test.label, test_scores, threshold),
            "episode": episode_metrics(
                test_ids, test_decisions, test.label, test_scores, threshold
            ),
        }
    write_json_atomic(output / "thresholds.json", thresholds)
    write_json_atomic(output / "temporal_thresholds.json", temporal)
    write_json_atomic(output / "results.json", results)
    np.savez_compressed(
        output / "seen_scores.npz",
        validation_labels=validation.label,
        validation_scores=validation_scores,
        test_labels=test.label,
        test_scores=test_scores,
    )
    manifest = {
        "schema_version": "simvla_isaac_topk8_model_manifest_v1",
        "model_path": str(model_path),
        "model_sha256": sha256_file(model_path),
        "results_sha256": sha256_file(output / "results.json"),
        "thresholds_sha256": sha256_file(output / "thresholds.json"),
        "normalization_sha256": sha256_file(args.dataset_root / "normalization.json"),
        "best_epoch": best_epoch,
        "best_validation_auprc": best_auprc,
        "ood150_used": False,
        "training_complete": True,
    }
    write_json_atomic(output / "model_manifest.json", manifest)
    (output / "TRAINING_COMPLETE").write_text("complete\n")
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
