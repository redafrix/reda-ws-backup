#!/usr/bin/env python3
"""Run the one locked OOD-150 evaluation with seen-validation calibration."""

from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import sys
from typing import Any

import numpy as np
import torch
from sklearn.metrics import average_precision_score, roc_auc_score
from torch.utils.data import DataLoader, Dataset

PIPELINE = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE))
from common import episode_metrics, load_stats, normalize, sha256_file, step_metrics, write_json_atomic  # noqa: E402
from model import SeqRiskModel  # noqa: E402


class EvalDataset(Dataset):
    def __init__(self, root: Path, normalization: Path) -> None:
        stats = load_stats(normalization)
        self.history, self.action, self.static = normalize(
            np.load(root / "history.npy", mmap_mode="r"),
            np.load(root / "action.npy", mmap_mode="r"),
            np.load(root / "static.npy", mmap_mode="r"),
            stats,
        )
        self.label = np.asarray(np.load(root / "label.npy", mmap_mode="r"), dtype=np.float32)

    def __len__(self) -> int:
        return len(self.label)

    def __getitem__(self, index: int):
        return {
            "history": torch.from_numpy(self.history[index]),
            "action": torch.from_numpy(self.action[index]),
            "static": torch.from_numpy(self.static[index]),
        }


def predict(model: SeqRiskModel, dataset: EvalDataset, workers: int) -> np.ndarray:
    loader = DataLoader(
        dataset,
        batch_size=2048,
        shuffle=False,
        num_workers=workers,
        pin_memory=True,
        persistent_workers=workers > 0,
    )
    outputs = []
    model.eval()
    with torch.no_grad():
        for batch in loader:
            batch = {key: value.cuda(non_blocking=True) for key, value in batch.items()}
            outputs.append(torch.sigmoid(model(batch)).cpu().numpy())
    return np.concatenate(outputs).astype(np.float32)


def identity(root: Path) -> tuple[list[str], np.ndarray]:
    episodes = json.loads((root / "episodes.json").read_text())
    episode_index = np.load(root / "episode_index.npy", mmap_mode="r")
    decisions = np.asarray(np.load(root / "decision_index.npy", mmap_mode="r"))
    return [episodes[int(index)]["episode_id"] for index in episode_index], decisions


def temporal_metrics(
    episode_ids: list[str],
    labels: np.ndarray,
    scores: np.ndarray,
    row_threshold: float,
    *,
    mode: str,
    aggregate_threshold: float,
) -> dict[str, Any]:
    grouped: dict[str, list[tuple[float, float]]] = defaultdict(list)
    for episode, label, score in zip(episode_ids, labels, scores, strict=True):
        grouped[episode].append((float(label), float(score)))
    success = failure = false_alarm = detected = det10 = det25 = det50 = never = 0
    fractions = []
    for values in grouped.values():
        label = max(value[0] for value in values)
        first = None
        mass = 0.0
        streak = 0
        for index, (_, score) in enumerate(values):
            if mode == "mass":
                mass += max(0.0, score - row_threshold)
                alarm = mass >= aggregate_threshold
            elif mode == "hysteresis":
                streak = streak + 1 if score >= row_threshold else 0
                alarm = streak >= int(aggregate_threshold)
            else:
                raise ValueError(mode)
            if first is None and alarm:
                first = index
        if label >= 0.5:
            failure += 1
            if first is None:
                never += 1
            else:
                detected += 1
                fraction = (first + 1) / len(values)
                fractions.append(fraction)
                det10 += int(fraction <= 0.10)
                det25 += int(fraction <= 0.25)
                det50 += int(fraction <= 0.50)
        else:
            success += 1
            false_alarm += int(first is not None)
    return {
        "mode": mode,
        "row_threshold": row_threshold,
        "aggregate_threshold": aggregate_threshold,
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-root", type=Path, required=True)
    parser.add_argument("--seen-dataset-root", type=Path, required=True)
    parser.add_argument("--ood-dataset-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    output = args.output_root.resolve()
    if (output / "LOCKED_OOD150_EVALUATION_COMPLETE").is_file():
        print((output / "results.json").read_text())
        return 0
    if not (args.model_root / "TRAINING_COMPLETE").is_file():
        raise RuntimeError("risk model training is not complete")
    if not (args.ood_dataset_root / "EVAL_DATASET_COMPLETE").is_file():
        raise RuntimeError("locked OOD evaluation arrays are incomplete")
    if not torch.cuda.is_available():
        raise RuntimeError("locked evaluation requires CUDA")
    output.mkdir(parents=True, exist_ok=True)
    normalization = args.seen_dataset_root / "normalization.json"
    dataset = EvalDataset(args.ood_dataset_root, normalization)
    model = SeqRiskModel().cuda()
    model.load_state_dict(torch.load(args.model_root / "model.pt", map_location="cpu"))
    scores = predict(model, dataset, args.workers)
    labels = dataset.label
    episode_ids, decisions = identity(args.ood_dataset_root)
    thresholds = json.loads((args.model_root / "thresholds.json").read_text())
    temporal = json.loads((args.model_root / "temporal_thresholds.json").read_text())
    results: dict[str, Any] = {
        "schema_version": "simvla_isaac_topk8_locked_ood150_evaluation_v1",
        "model_path": str((args.model_root / "model.pt").resolve()),
        "model_sha256": sha256_file(args.model_root / "model.pt"),
        "normalization_path": str(normalization.resolve()),
        "normalization_sha256": sha256_file(normalization),
        "thresholds_path": str((args.model_root / "thresholds.json").resolve()),
        "thresholds_sha256": sha256_file(args.model_root / "thresholds.json"),
        "ood_dataset_manifest_sha256": sha256_file(args.ood_dataset_root / "manifest.json"),
        "episodes": len(set(episode_ids)),
        "rows": len(labels),
        "step_auroc": float(roc_auc_score(labels.astype(int), scores)),
        "step_auprc": float(average_precision_score(labels.astype(int), scores)),
        "threshold_results": {},
        "temporal_results": {},
        "model_selection_used_ood": False,
        "normalization_used_ood": False,
        "threshold_calibration_used_ood": False,
    }
    for name, threshold in thresholds.items():
        results["threshold_results"][name] = {
            "step": step_metrics(labels, scores, float(threshold)),
            "episode": episode_metrics(
                episode_ids, decisions, labels, scores, float(threshold)
            ),
        }
    q95 = float(thresholds["q95_success"])
    for name, value in temporal["conformal_mass"].items():
        results["temporal_results"][f"mass_{name}"] = temporal_metrics(
            episode_ids, labels, scores, q95, mode="mass", aggregate_threshold=float(value)
        )
    for name, value in temporal["hysteresis"].items():
        results["temporal_results"][f"hysteresis_{name}"] = temporal_metrics(
            episode_ids, labels, scores, q95, mode="hysteresis", aggregate_threshold=float(value)
        )
    np.savez_compressed(output / "scores.npz", labels=labels, scores=scores)
    write_json_atomic(output / "results.json", results)
    report = [
        "# Isaac Seen to Locked OOD-150 Final Evaluation",
        "",
        "The model, normalization, and all thresholds were fixed using seen data before this one locked evaluation.",
        "",
        f"- OOD episodes: `{results['episodes']}`",
        f"- OOD rows: `{results['rows']}`",
        f"- Step AUROC: `{results['step_auroc']:.6f}`",
        f"- Step AUPRC: `{results['step_auprc']:.6f}`",
        "",
        "OOD_USED_FOR_TRAINING=NO",
        "OOD_USED_FOR_MODEL_SELECTION=NO",
        "OOD_USED_FOR_THRESHOLD_CALIBRATION=NO",
    ]
    (output / "ISAAC_SEEN_TO_OOD150_FINAL_EVAL_REPORT.md").write_text("\n".join(report) + "\n")
    (output / "LOCKED_OOD150_EVALUATION_COMPLETE").write_text("complete\n")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
