from __future__ import annotations
# import matplotlib
# matplotlib.use("Agg")
# import matplotlib
# matplotlib.use("Agg")
#!/usr/bin/env python3

import argparse
import json
from pathlib import Path
from typing import Any

# # import matplotlib.pyplot as plt
import numpy as np
import torch
from torch.utils.data import DataLoader

from phase2_tdqc.dataset import (
    TDQCEpisodeDataset,
    add_all_deltas,
    add_temporal_features,
    apply_feature_stats,
    clip_episode_steps,
    collate_tdqc_episodes,
    load_tdqc_dataset,
)
from phase2_tdqc.metrics import binary_auroc, evaluate_calibrator
from phase2_tdqc.model import TDQCCalibrator, predict_tdqc_sequence


def binary_accuracy(scores: np.ndarray, labels: np.ndarray, threshold: float = 0.5) -> float:
    preds = scores >= threshold
    targets = labels >= 0.5
    return float((preds == targets).mean())


def balanced_binary_accuracy(scores: np.ndarray, labels: np.ndarray, threshold: float = 0.5) -> float:
    preds = scores >= threshold
    targets = labels >= 0.5
    positives = targets
    negatives = ~targets
    recalls = []
    if positives.any():
        recalls.append(float((preds[positives] == targets[positives]).mean()))
    if negatives.any():
        recalls.append(float((preds[negatives] == targets[negatives]).mean()))
    return float(np.mean(recalls)) if recalls else float("nan")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Evaluate TDQC checkpoints on fixed prefixes")
    parser.add_argument("--dataset_path", required=True)
    parser.add_argument("--checkpoint", action="append", required=True,
                        help="Checkpoint path. Can be passed multiple times.")
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--prefix_steps", type=int, nargs="+", default=[50, 70, 100, 120])
    parser.add_argument("--max_episode_steps", type=int, default=None,
                        help="Override checkpoint first-N clipping. Omit to use the checkpoint setting.")
    parser.add_argument("--accuracy_threshold", type=float, default=0.5)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    return parser.parse_args()


def load_model(ckpt_path: str | Path, device: torch.device) -> tuple[TDQCCalibrator, dict[str, Any]]:
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    model = TDQCCalibrator(
        input_dim=int(ckpt["input_dim"]),
        hidden_dim=int(ckpt["hidden_dim"]),
        num_layers=int(ckpt["num_layers"]),
        dropout=float(ckpt["dropout"]),
        use_gru=bool(ckpt.get("use_gru", False)),
        use_attention=bool(ckpt.get("use_attention", False)),
        attention_heads=int(ckpt.get("attention_heads", 4)),
        attention_dropout=ckpt.get("attention_dropout", None),
        history_window=int(ckpt.get("history_window", 0)),
        input_proj_dim=int(ckpt.get("input_proj_dim", 0)),
        input_dropout=float(ckpt.get("input_dropout", 0.0)),
    ).to(device)
    model.load_state_dict(ckpt["model_state_dict"])
    model.window_eval_batch_size = int(ckpt.get("window_eval_batch_size", 256))
    model.eval()
    return model, ckpt


def prepare_episodes(dataset_path: str | Path, ckpt: dict[str, Any], max_episode_steps: int | None) -> list[dict[str, Any]]:
    dataset = load_tdqc_dataset(dataset_path)
    episodes = dataset["episodes"]
    feature_keys = dataset.get("feature_keys")
    clip_steps = ckpt.get("max_episode_steps", 0) if max_episode_steps is None else max_episode_steps
    episodes = clip_episode_steps(episodes, int(clip_steps or 0))
    if ckpt.get("add_all_feature_deltas", False):
        episodes, feature_keys = add_all_deltas(episodes, feature_keys)
    if ckpt.get("add_temporal_features", False):
        episodes, feature_keys = add_temporal_features(
            episodes,
            feature_keys,
            source_key=ckpt.get("temporal_feature_source", "mean_last_var"),
        )
    return apply_feature_stats(
        episodes,
        ckpt["feature_mean"].detach().cpu() if torch.is_tensor(ckpt["feature_mean"]) else ckpt["feature_mean"],
        ckpt["feature_std"].detach().cpu() if torch.is_tensor(ckpt["feature_std"]) else ckpt["feature_std"],
    )


@torch.no_grad()
def prefix_metrics(
    model: TDQCCalibrator,
    episodes: list[dict[str, Any]],
    prefix: int,
    device: torch.device,
    batch_size: int,
    accuracy_threshold: float,
) -> dict[str, float | int]:
    eligible = []
    for ep in episodes:
        features = np.asarray(ep["features"], dtype=np.float32)
        if features.shape[0] >= prefix:
            new_ep = dict(ep)
            new_ep["features"] = features[:prefix]
            eligible.append(new_ep)

    if not eligible:
        return {
            "prefix": prefix,
            "episodes": 0,
            "successes": 0,
            "failures": 0,
            "terminal_brier": float("nan"),
            "terminal_auroc": float("nan"),
            "terminal_accuracy": float("nan"),
            "terminal_balanced_accuracy": float("nan"),
            "max_brier": float("nan"),
            "max_auroc": float("nan"),
            "max_accuracy": float("nan"),
            "max_balanced_accuracy": float("nan"),
        }

    loader = DataLoader(
        TDQCEpisodeDataset(eligible),
        batch_size=batch_size,
        shuffle=False,
        collate_fn=collate_tdqc_episodes,
    )

    labels = []
    terminal_scores = []
    max_scores = []
    for batch in loader:
        features = batch["features"].to(device)
        masks = batch["valid_masks"].to(device)
        failure = batch["failure"].cpu().numpy()
        q = predict_tdqc_sequence(
            model,
            features,
            masks,
            window_batch_size=getattr(model, "window_eval_batch_size", None),
        ).detach().cpu().numpy()
        valid = masks.detach().cpu().numpy()
        for i in range(q.shape[0]):
            L = int(valid[i].sum())
            labels.append(float(failure[i]))
            terminal_scores.append(float(q[i, L - 1]))
            max_scores.append(float(q[i, :L].max()))

    labels_np = np.asarray(labels, dtype=np.float32)
    terminal_np = np.asarray(terminal_scores, dtype=np.float32)
    max_np = np.asarray(max_scores, dtype=np.float32)
    return {
        "prefix": prefix,
        "episodes": int(len(labels_np)),
        "successes": int((labels_np < 0.5).sum()),
        "failures": int((labels_np > 0.5).sum()),
        "terminal_brier": float(np.mean((terminal_np - labels_np) ** 2)),
        "terminal_auroc": binary_auroc(terminal_np, labels_np),
        "terminal_accuracy": binary_accuracy(terminal_np, labels_np, accuracy_threshold),
        "terminal_balanced_accuracy": balanced_binary_accuracy(terminal_np, labels_np, accuracy_threshold),
        "max_brier": float(np.mean((max_np - labels_np) ** 2)),
        "max_auroc": binary_auroc(max_np, labels_np),
        "max_accuracy": binary_accuracy(max_np, labels_np, accuracy_threshold),
        "max_balanced_accuracy": balanced_binary_accuracy(max_np, labels_np, accuracy_threshold),
        "terminal_success_mean": float(terminal_np[labels_np < 0.5].mean()) if (labels_np < 0.5).any() else float("nan"),
        "terminal_failure_mean": float(terminal_np[labels_np > 0.5].mean()) if (labels_np > 0.5).any() else float("nan"),
        "max_success_mean": float(max_np[labels_np < 0.5].mean()) if (labels_np < 0.5).any() else float("nan"),
        "max_failure_mean": float(max_np[labels_np > 0.5].mean()) if (labels_np > 0.5).any() else float("nan"),
    }


def checkpoint_label(path: str | Path, ckpt: dict[str, Any]) -> str:
    epoch = ckpt.get("epoch")
    if epoch is not None:
        return f"epoch_{int(epoch):04d}"
    return Path(path).stem


def plot_metrics(rows: list[dict[str, Any]], output_dir: Path) -> None:
    if not rows:
        return
    prefixes = sorted({int(r["prefix"]) for r in rows})
    metrics = ["terminal_brier", "terminal_auroc", "terminal_accuracy", "terminal_balanced_accuracy"]
    for prefix in prefixes:
        subset = [r for r in rows if int(r["prefix"]) == prefix]
        subset.sort(key=lambda r: int(r["epoch"]))
        epochs = [int(r["epoch"]) for r in subset]
        fig, axes = plt.subplots(2, 2, figsize=(11, 7))
        for ax, metric in zip(axes.ravel(), metrics):
            ax.plot(epochs, [r[metric] for r in subset], marker="o")
            ax.set_title(f"{metric} @ first {prefix} steps")
            ax.set_xlabel("Checkpoint epoch")
            ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(output_dir / f"prefix_{prefix}_checkpoint_metrics.png", dpi=160)
        plt.close(fig)

        fig, axes = plt.subplots(2, 2, figsize=(11, 7))
        for ax, metric in zip(
            axes.ravel(),
            ["max_brier", "max_auroc", "max_accuracy", "max_balanced_accuracy"],
        ):
            ax.plot(epochs, [r[metric] for r in subset], marker="o")
            ax.set_title(f"{metric} @ first {prefix} steps")
            ax.set_xlabel("Checkpoint epoch")
            ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(output_dir / f"prefix_{prefix}_max_checkpoint_metrics.png", dpi=160)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(epochs, [r["terminal_success_mean"] for r in subset], marker="o", label="success mean risk")
        ax.plot(epochs, [r["terminal_failure_mean"] for r in subset], marker="o", label="failure mean risk")
        ax.set_title(f"Terminal risk separation @ first {prefix} steps")
        ax.set_xlabel("Checkpoint epoch")
        ax.set_ylabel("Risk")
        ax.grid(True, alpha=0.3)
        ax.legend()
        fig.tight_layout()
        fig.savefig(output_dir / f"prefix_{prefix}_terminal_risk_separation.png", dpi=160)
        plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    for prefix in prefixes:
        subset = [r for r in rows if int(r["prefix"]) == prefix]
        subset.sort(key=lambda r: int(r["epoch"]))
        ax.plot(
            [int(r["epoch"]) for r in subset],
            [r["terminal_auroc"] for r in subset],
            marker="o",
            label=f"terminal AUROC @ {prefix}",
        )
    ax.set_xlabel("Checkpoint epoch")
    ax.set_ylabel("AUROC")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "prefix_terminal_auroc_comparison.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    for prefix in prefixes:
        subset = [r for r in rows if int(r["prefix"]) == prefix]
        subset.sort(key=lambda r: int(r["epoch"]))
        ax.plot(
            [int(r["epoch"]) for r in subset],
            [r["terminal_accuracy"] for r in subset],
            marker="o",
            label=f"terminal accuracy @ {prefix}",
        )
    ax.set_xlabel("Checkpoint epoch")
    threshold = rows[0].get("accuracy_threshold", 0.5)
    ax.set_ylabel(f"Accuracy @ {threshold:g}")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "prefix_terminal_accuracy_comparison.png", dpi=160)
    plt.close(fig)


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device(args.device)

    rows = []
    for ckpt_path in args.checkpoint:
        model, ckpt = load_model(ckpt_path, device)
        episodes = prepare_episodes(args.dataset_path, ckpt, args.max_episode_steps)
        full_loader = DataLoader(
            TDQCEpisodeDataset(episodes),
            batch_size=args.batch_size,
            shuffle=False,
            collate_fn=collate_tdqc_episodes,
        )
        full_metrics = evaluate_calibrator(model, full_loader, device)
        label = checkpoint_label(ckpt_path, ckpt)
        for prefix in args.prefix_steps:
            row = prefix_metrics(
                model,
                episodes,
                prefix,
                device,
                args.batch_size,
                args.accuracy_threshold,
            )
            row.update(
                {
                    "checkpoint": str(ckpt_path),
                    "label": label,
                    "epoch": int(ckpt.get("epoch", -1)),
                    "accuracy_threshold": args.accuracy_threshold,
                    "full_seq_brier": full_metrics["seq_brier"],
                    "full_terminal_brier": full_metrics["terminal_brier"],
                    "full_terminal_auroc": full_metrics["terminal_auroc"],
                    "full_max_brier": full_metrics["max_brier"],
                    "full_max_auroc": full_metrics["max_auroc"],
                }
            )
            rows.append(row)

    with open(output_dir / "prefix_eval_metrics.json", "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)
    # plot_metrics(rows, output_dir)
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
