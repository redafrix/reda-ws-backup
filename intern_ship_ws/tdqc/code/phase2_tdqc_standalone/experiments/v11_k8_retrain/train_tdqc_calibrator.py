#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Sequence

import numpy as np
import torch
from torch.optim.lr_scheduler import CosineAnnealingLR, ReduceLROnPlateau, StepLR
from torch.utils.data import DataLoader, WeightedRandomSampler

from phase2_tdqc.dataset import (
    TDQCEpisodeDataset,
    TDQCFixedHorizonWindowDataset,
    add_all_deltas,
    add_temporal_features,
    apply_feature_stats,
    clip_episode_steps,
    collate_tdqc_fixed_windows,
    collate_tdqc_episodes,
    compute_feature_stats,
    load_tdqc_dataset,
    split_episodes,
)
from phase2_tdqc.metrics import binary_auroc, evaluate_calibrator
from phase2_tdqc.model import TDQCCalibrator, hard_update, mc_brier_loss, predict_tdqc_sequence, soft_update, td0_brier_loss


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Train Phase-2 SimVLA TDQC calibrator")
    parser.add_argument("--dataset_path", type=str, required=True)
    parser.add_argument("--external_val_dataset_path", type=str, default=None,
                        help="Optional held-out TDQC dataset used for checkpoint selection and early stopping.")
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--epochs", type=int, default=200)
    parser.add_argument("--batch_size", type=int, default=64)
    parser.add_argument("--lr", type=float, default=5e-5)
    parser.add_argument("--weight_decay", type=float, default=1e-4)
    parser.add_argument("--lr_scheduler", choices=("none", "step", "cosine", "plateau"), default="none")
    parser.add_argument("--lr_step_size", type=int, default=50)
    parser.add_argument("--lr_gamma", type=float, default=0.8)
    parser.add_argument("--lr_min", type=float, default=0.0)
    parser.add_argument("--hidden_dim", type=int, default=256)
    parser.add_argument("--num_layers", type=int, default=4)
    parser.add_argument("--dropout", type=float, default=0.15)
    parser.add_argument("--input_proj_dim", type=int, default=0,
                        help="Optional per-step feature encoder width before the RNN. 0 disables it.")
    parser.add_argument("--input_dropout", type=float, default=0.0,
                        help="Dropout applied to encoded per-step features before the RNN.")
    parser.add_argument("--use_gru", action="store_true")
    parser.add_argument("--use_attention", action="store_true")
    parser.add_argument("--attention_heads", type=int, default=4)
    parser.add_argument("--attention_dropout", type=float, default=None)
    parser.add_argument("--history_window", type=int, default=0,
                        help="If >0, predict each q_t from only the last N feature steps ending at t.")
    parser.add_argument("--window_eval_batch_size", type=int, default=512,
                        help="Chunk size for expanded sliding-window sequence evaluation. Lower reduces memory.")
    parser.add_argument("--max_episode_steps", type=int, default=0,
                        help="If >0, train/evaluate only on the first N steps of every episode.")
    parser.add_argument("--add_all_feature_deltas", action="store_true",
                        help="Append one-step deltas for every input feature before normalization.")
    parser.add_argument("--add_temporal_features", action="store_true",
                        help="Append delta/rolling/slope/spike features derived from mean_last_var.")
    parser.add_argument("--temporal_feature_source", type=str, default="mean_last_var")
    parser.add_argument("--val_ratio", type=float, default=0.2)
    parser.add_argument("--split_by_task", action="store_true")
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--target_update_freq", type=int, default=25,
                        help="Hard-copy target network every N optimizer steps. Ignored when --soft_target_tau > 0.")
    parser.add_argument("--soft_target_tau", type=float, default=0.0,
                        help="If >0, use EMA target update every step instead of hard updates.")
    parser.add_argument("--failure_weight", type=float, default=1.0)
    parser.add_argument("--success_weight", type=float, default=1.0)
    parser.add_argument("--loss_type", choices=("td0", "mc"), default="td0",
                        help="td0 uses TDQC bootstrapping; mc supervises every valid step with the final failure label.")
    parser.add_argument("--episode_balanced_loss", action="store_true",
                        help="Average TD loss per episode before averaging across the batch.")
    parser.add_argument("--fixed_horizon_steps", type=int, nargs="*", default=None,
                        help="Train direct failure prediction on windows ending at these absolute steps.")
    parser.add_argument("--fixed_horizon_balanced_sampler", action="store_true",
                        help="Balance fixed-horizon samples by horizon and success/failure label.")
    parser.add_argument("--fixed_horizon_aux_weight", type=float, default=0.0,
                        help="If >0, add fixed-horizon Brier loss to TDQC sequence loss.")
    parser.add_argument("--prefix_aux_steps", type=int, nargs="*", default=None,
                        help="Add supervised Brier loss on q_t at these absolute prefix steps.")
    parser.add_argument("--prefix_aux_weight", type=float, default=0.0,
                        help="Weight for the supervised prefix Brier auxiliary loss.")
    parser.add_argument("--selection_prefix_steps", type=int, nargs="*", default=None,
                        help="If set, select/early-stop on mean terminal Brier at these clipped prefixes.")
    parser.add_argument(
        "--selection_metric",
        choices=("seq_brier", "prefix_terminal_brier", "prefix_terminal_auroc"),
        default="seq_brier",
        help="Checkpoint selection metric. AUROC is maximized; Brier metrics are minimized.",
    )
    parser.add_argument("--early_stop_patience", type=int, default=0,
                        help="Stop after N epochs without val seq_brier improvement. 0 disables early stopping.")
    parser.add_argument("--early_stop_min_delta", type=float, default=0.0,
                        help="Minimum val seq_brier decrease required to reset early-stop patience.")
    parser.add_argument("--checkpoint_every_epochs", type=int, default=0,
                        help="If >0, also save checkpoint_epoch_XXXX.pt every N epochs.")
    parser.add_argument("--num_workers", type=int, default=0)
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    return parser.parse_args()


def make_scheduler(args: argparse.Namespace, optimizer: torch.optim.Optimizer):
    if args.lr_scheduler == "none":
        return None
    if args.lr_scheduler == "step":
        return StepLR(optimizer, step_size=args.lr_step_size, gamma=args.lr_gamma)
    if args.lr_scheduler == "cosine":
        return CosineAnnealingLR(optimizer, T_max=max(args.epochs, 1), eta_min=args.lr_min)
    if args.lr_scheduler == "plateau":
        return ReduceLROnPlateau(
            optimizer,
            mode="min",
            factor=args.lr_gamma,
            patience=max(args.lr_step_size, 1),
            min_lr=args.lr_min,
        )
    raise ValueError(f"Unknown lr_scheduler: {args.lr_scheduler}")


def make_loader(episodes, batch_size: int, shuffle: bool, num_workers: int) -> DataLoader:
    return DataLoader(
        TDQCEpisodeDataset(episodes),
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        collate_fn=collate_tdqc_episodes,
        drop_last=False,
    )


def prepare_episodes_for_training(
    episodes,
    feature_keys,
    args: argparse.Namespace,
):
    episodes = clip_episode_steps(episodes, args.max_episode_steps)
    if args.add_all_feature_deltas:
        episodes, feature_keys = add_all_deltas(episodes, feature_keys)
    if args.add_temporal_features:
        episodes, feature_keys = add_temporal_features(
            episodes,
            feature_keys,
            source_key=args.temporal_feature_source,
        )
    return episodes, feature_keys


def checkpoint_payload(
    *,
    model: TDQCCalibrator,
    input_dim: int,
    args: argparse.Namespace,
    feature_mean: torch.Tensor,
    feature_std: torch.Tensor,
    feature_keys,
    external_feature_keys,
    val_metrics,
    external_val_metrics,
    internal_prefix_metrics,
    external_prefix_metrics,
    selection_metric_name: str,
    selection_score: float,
    epoch: int,
) -> Dict[str, object]:
    return {
        "model_state_dict": model.state_dict(),
        "input_dim": input_dim,
        "hidden_dim": args.hidden_dim,
        "num_layers": args.num_layers,
        "dropout": args.dropout,
        "use_gru": args.use_gru,
        "use_attention": args.use_attention,
        "attention_heads": args.attention_heads,
        "attention_dropout": args.attention_dropout,
        "history_window": args.history_window,
        "input_proj_dim": args.input_proj_dim,
        "input_dropout": args.input_dropout,
        "window_eval_batch_size": args.window_eval_batch_size,
        "loss_type": args.loss_type,
        "episode_balanced_loss": args.episode_balanced_loss,
        "fixed_horizon_steps": args.fixed_horizon_steps,
        "fixed_horizon_balanced_sampler": args.fixed_horizon_balanced_sampler,
        "fixed_horizon_aux_weight": args.fixed_horizon_aux_weight,
        "prefix_aux_steps": args.prefix_aux_steps,
        "prefix_aux_weight": args.prefix_aux_weight,
        "selection_prefix_steps": args.selection_prefix_steps,
        "feature_mean": feature_mean,
        "feature_std": feature_std,
        "feature_keys": feature_keys,
        "external_feature_keys": external_feature_keys,
        "max_episode_steps": args.max_episode_steps,
        "add_all_feature_deltas": args.add_all_feature_deltas,
        "add_temporal_features": args.add_temporal_features,
        "temporal_feature_source": args.temporal_feature_source,
        "args": vars(args),
        "val_metrics": val_metrics,
        "external_val_metrics": external_val_metrics,
        "internal_prefix_metrics": internal_prefix_metrics,
        "external_prefix_metrics": external_prefix_metrics,
        "selection_metric": selection_metric_name,
        "selection_score": selection_score,
        "epoch": epoch,
    }


def make_fixed_horizon_loader(
    episodes,
    horizons: Sequence[int],
    batch_size: int,
    num_workers: int,
    *,
    window_size: int,
    balanced_sampler: bool,
) -> DataLoader:
    dataset = TDQCFixedHorizonWindowDataset(episodes, horizons, window_size=window_size)
    sampler = None
    shuffle = True
    if balanced_sampler:
        sampler = WeightedRandomSampler(
            dataset.balanced_weights(),
            num_samples=len(dataset),
            replacement=True,
        )
        shuffle = False
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        sampler=sampler,
        num_workers=num_workers,
        collate_fn=collate_tdqc_fixed_windows,
        drop_last=False,
    )


def fixed_horizon_brier_loss(batch: Dict[str, torch.Tensor], model: TDQCCalibrator, args: argparse.Namespace, device: torch.device) -> torch.Tensor:
    features = batch["features"].to(device)
    masks = batch["valid_masks"].to(device)
    failure = batch["failure"].to(device)
    q = model(features, masks)[:, -1]
    sample_weights = torch.where(
        failure > 0.5,
        torch.as_tensor(args.failure_weight, dtype=q.dtype, device=q.device),
        torch.as_tensor(args.success_weight, dtype=q.dtype, device=q.device),
    )
    per_sample = (q - failure).pow(2)
    return (per_sample * sample_weights).sum() / sample_weights.sum().clamp_min(1.0)


def prefix_supervised_brier_loss(
    q: torch.Tensor,
    failure: torch.Tensor,
    masks: torch.Tensor,
    args: argparse.Namespace,
) -> torch.Tensor:
    if not args.prefix_aux_steps or args.prefix_aux_weight <= 0.0:
        return torch.zeros((), dtype=q.dtype, device=q.device)

    losses = []
    weights = []
    for prefix in args.prefix_aux_steps:
        idx = int(prefix) - 1
        if idx < 0 or idx >= q.shape[1]:
            continue
        valid = masks[:, idx] > 0.5
        if not valid.any():
            continue
        pred = q[valid, idx]
        target = failure[valid]
        sample_weights = torch.where(
            target > 0.5,
            torch.as_tensor(args.failure_weight, dtype=q.dtype, device=q.device),
            torch.as_tensor(args.success_weight, dtype=q.dtype, device=q.device),
        )
        losses.append(((pred - target).pow(2) * sample_weights).sum())
        weights.append(sample_weights.sum())
    if not losses:
        return torch.zeros((), dtype=q.dtype, device=q.device)
    return torch.stack(losses).sum() / torch.stack(weights).sum().clamp_min(1.0)


def add_prefix(metrics: Dict[str, float], prefix: str) -> Dict[str, float]:
    return {f"{prefix}_{key}": value for key, value in metrics.items()}


@torch.no_grad()
def evaluate_prefix_selection(
    model: TDQCCalibrator,
    episodes,
    prefixes: Sequence[int],
    batch_size: int,
    num_workers: int,
    device: torch.device,
) -> Dict[str, float]:
    rows = []
    for prefix in prefixes:
        eligible = []
        for ep in episodes:
            features = np.asarray(ep["features"], dtype=np.float32)
            if features.shape[0] >= prefix:
                clipped = dict(ep)
                clipped["features"] = features[:prefix]
                eligible.append(clipped)
        if not eligible:
            continue
        loader = make_loader(eligible, batch_size, False, num_workers)
        labels = []
        terminal_scores = []
        max_scores = []
        for batch in loader:
            features = batch["features"].to(device)
            masks = batch["valid_masks"].to(device)
            lengths = batch["lengths"].to(device)
            failure = batch["failure"].detach().cpu().numpy()
            q = predict_tdqc_sequence(
                model,
                features,
                masks,
                window_batch_size=getattr(model, "window_eval_batch_size", None),
            ).detach().cpu().numpy()
            for i in range(q.shape[0]):
                L = int(lengths[i].item())
                if L <= 0:
                    continue
                labels.append(float(failure[i]))
                terminal_scores.append(float(q[i, L - 1]))
                max_scores.append(float(q[i, :L].max()))

        labels_np = np.asarray(labels, dtype=np.float32)
        terminal_np = np.asarray(terminal_scores, dtype=np.float32)
        max_np = np.asarray(max_scores, dtype=np.float32)
        terminal_preds = terminal_np >= 0.5
        targets = labels_np >= 0.5
        max_preds = max_np >= 0.5
        rows.append(
            {
                "prefix": int(prefix),
                "terminal_brier": float(np.mean((terminal_np - labels_np) ** 2)),
                "terminal_auroc": binary_auroc(terminal_np, labels_np),
                "terminal_accuracy": float((terminal_preds == targets).mean()),
                "max_brier": float(np.mean((max_np - labels_np) ** 2)),
                "max_auroc": binary_auroc(max_np, labels_np),
                "max_accuracy": float((max_preds == targets).mean()),
            }
        )

    if not rows:
        return {
            "prefix_terminal_brier": float("nan"),
            "prefix_terminal_auroc": float("nan"),
            "prefix_terminal_accuracy": float("nan"),
            "prefix_max_brier": float("nan"),
            "prefix_max_auroc": float("nan"),
            "prefix_max_accuracy": float("nan"),
        }
    return {
        "prefix_terminal_brier": float(np.mean([r["terminal_brier"] for r in rows])),
        "prefix_terminal_auroc": float(np.nanmean([r["terminal_auroc"] for r in rows])),
        "prefix_terminal_accuracy": float(np.mean([r["terminal_accuracy"] for r in rows])),
        "prefix_max_brier": float(np.mean([r["max_brier"] for r in rows])),
        "prefix_max_auroc": float(np.nanmean([r["max_auroc"] for r in rows])),
        "prefix_max_accuracy": float(np.mean([r["max_accuracy"] for r in rows])),
    }


def main() -> None:
    args = parse_args()
    torch.manual_seed(args.seed)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device(args.device)

    dataset_obj = load_tdqc_dataset(args.dataset_path)
    episodes = dataset_obj["episodes"]
    feature_keys = dataset_obj.get("feature_keys", None)
    episodes, feature_keys = prepare_episodes_for_training(episodes, feature_keys, args)
    train_eps, val_eps = split_episodes(
        episodes,
        val_ratio=args.val_ratio,
        seed=args.seed,
        split_by_task=args.split_by_task,
    )

    feature_mean, feature_std = compute_feature_stats(train_eps)
    train_eps = apply_feature_stats(train_eps, feature_mean, feature_std)
    val_eps = apply_feature_stats(val_eps, feature_mean, feature_std)
    external_val_eps = None
    external_feature_keys = None
    if args.external_val_dataset_path is not None:
        external_dataset_obj = load_tdqc_dataset(args.external_val_dataset_path)
        external_episodes = external_dataset_obj["episodes"]
        external_feature_keys = external_dataset_obj.get("feature_keys", None)
        external_episodes, external_feature_keys = prepare_episodes_for_training(
            external_episodes,
            external_feature_keys,
            args,
        )
        external_val_eps = apply_feature_stats(
            external_episodes,
            feature_mean,
            feature_std,
        )

    input_dim = int(train_eps[0]["features"].shape[-1])
    use_fixed_horizon_training = bool(args.fixed_horizon_steps) and args.fixed_horizon_aux_weight <= 0.0
    use_hybrid_training = bool(args.fixed_horizon_steps) and args.fixed_horizon_aux_weight > 0.0
    if (use_fixed_horizon_training or use_hybrid_training) and args.history_window <= 0:
        raise ValueError("--fixed_horizon_steps requires --history_window > 0")
    fixed_horizon_loader = (
        make_fixed_horizon_loader(
            train_eps,
            args.fixed_horizon_steps,
            args.batch_size,
            args.num_workers,
            window_size=args.history_window,
            balanced_sampler=args.fixed_horizon_balanced_sampler,
        )
        if args.fixed_horizon_steps
        else None
    )
    train_loader = fixed_horizon_loader if use_fixed_horizon_training else make_loader(train_eps, args.batch_size, True, args.num_workers)
    val_loader = make_loader(val_eps, args.batch_size, False, args.num_workers)
    external_val_loader = (
        make_loader(external_val_eps, args.batch_size, False, args.num_workers)
        if external_val_eps is not None
        else None
    )

    model = TDQCCalibrator(
        input_dim=input_dim,
        hidden_dim=args.hidden_dim,
        num_layers=args.num_layers,
        dropout=args.dropout,
        use_gru=args.use_gru,
        use_attention=args.use_attention,
        attention_heads=args.attention_heads,
        attention_dropout=args.attention_dropout,
        history_window=args.history_window,
        input_proj_dim=args.input_proj_dim,
        input_dropout=args.input_dropout,
    ).to(device)
    model.window_eval_batch_size = args.window_eval_batch_size
    target_model = TDQCCalibrator(
        input_dim=input_dim,
        hidden_dim=args.hidden_dim,
        num_layers=args.num_layers,
        dropout=args.dropout,
        use_gru=args.use_gru,
        use_attention=args.use_attention,
        attention_heads=args.attention_heads,
        attention_dropout=args.attention_dropout,
        history_window=args.history_window,
        input_proj_dim=args.input_proj_dim,
        input_dropout=args.input_dropout,
    ).to(device)
    target_model.window_eval_batch_size = args.window_eval_batch_size
    hard_update(target_model, model)
    target_model.eval()

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = make_scheduler(args, optimizer)

    best_val = float("inf")
    best_path = output_dir / "tdqc_calibrator_best.pt"
    global_step = 0
    epochs_without_improvement = 0
    history = []
    fixed_horizon_iter = iter(fixed_horizon_loader) if use_hybrid_training and fixed_horizon_loader is not None else None

    for epoch in range(1, args.epochs + 1):
        model.train()
        running = []
        for batch in train_loader:
            features = batch["features"].to(device)
            masks = batch["valid_masks"].to(device)
            failure = batch["failure"].to(device)
            if use_fixed_horizon_training:
                loss = fixed_horizon_brier_loss(batch, model, args, device)
            else:
                lengths = batch["lengths"].to(device)
                online_q = predict_tdqc_sequence(
                    model,
                    features,
                    masks,
                    window_batch_size=args.window_eval_batch_size,
                )
                if args.loss_type == "mc":
                    loss, logs = mc_brier_loss(
                        online_q,
                        failure,
                        masks,
                        lengths,
                        failure_weight=args.failure_weight,
                        success_weight=args.success_weight,
                        episode_balanced=args.episode_balanced_loss,
                    )
                else:
                    with torch.no_grad():
                        target_q = predict_tdqc_sequence(
                            target_model,
                            features,
                            masks,
                            window_batch_size=args.window_eval_batch_size,
                        )

                    loss, logs = td0_brier_loss(
                        online_q,
                        target_q,
                        failure,
                        masks,
                        lengths,
                        failure_weight=args.failure_weight,
                        success_weight=args.success_weight,
                        episode_balanced=args.episode_balanced_loss,
                    )
                if args.prefix_aux_steps and args.prefix_aux_weight > 0.0:
                    loss = loss + args.prefix_aux_weight * prefix_supervised_brier_loss(
                        online_q,
                        failure,
                        masks,
                        args,
                    )
                if use_hybrid_training and fixed_horizon_loader is not None:
                    try:
                        fixed_batch = next(fixed_horizon_iter)
                    except StopIteration:
                        fixed_horizon_iter = iter(fixed_horizon_loader)
                        fixed_batch = next(fixed_horizon_iter)
                    fixed_loss = fixed_horizon_brier_loss(fixed_batch, model, args, device)
                    loss = loss + args.fixed_horizon_aux_weight * fixed_loss
            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()

            global_step += 1
            if not use_fixed_horizon_training and args.loss_type == "td0":
                if args.soft_target_tau > 0.0:
                    soft_update(target_model, model, args.soft_target_tau)
                elif global_step % args.target_update_freq == 0:
                    hard_update(target_model, model)

            running.append(float(loss.detach().cpu()))

        train_loss = sum(running) / max(len(running), 1)
        val_metrics = evaluate_calibrator(model, val_loader, device)
        external_val_metrics = (
            evaluate_calibrator(model, external_val_loader, device)
            if external_val_loader is not None
            else None
        )
        internal_prefix_metrics = (
            evaluate_prefix_selection(
                model,
                val_eps,
                args.selection_prefix_steps,
                args.batch_size,
                args.num_workers,
                device,
            )
            if args.selection_prefix_steps
            else None
        )
        external_prefix_metrics = (
            evaluate_prefix_selection(
                model,
                external_val_eps,
                args.selection_prefix_steps,
                args.batch_size,
                args.num_workers,
                device,
            )
            if args.selection_prefix_steps and external_val_eps is not None
            else None
        )
        selection_metrics = external_val_metrics if external_val_metrics is not None else val_metrics
        selection_prefix_metrics = external_prefix_metrics if external_prefix_metrics is not None else internal_prefix_metrics
        selection_source = "external" if external_val_metrics is not None else "internal"
        if args.selection_metric == "seq_brier":
            selection_metric_name = f"{selection_source}_seq_brier" if external_val_metrics is not None else "seq_brier"
            selection_score = selection_metrics["seq_brier"]
            selection_improves = lambda score, best: score < best - args.early_stop_min_delta
        elif args.selection_metric == "prefix_terminal_brier":
            if selection_prefix_metrics is None:
                raise ValueError("--selection_metric prefix_terminal_brier requires --selection_prefix_steps")
            selection_metric_name = f"{selection_source}_prefix_terminal_brier"
            selection_score = selection_prefix_metrics["prefix_terminal_brier"]
            selection_improves = lambda score, best: score < best - args.early_stop_min_delta
        elif args.selection_metric == "prefix_terminal_auroc":
            if selection_prefix_metrics is None:
                raise ValueError("--selection_metric prefix_terminal_auroc requires --selection_prefix_steps")
            selection_metric_name = f"{selection_source}_prefix_terminal_auroc"
            selection_score = selection_prefix_metrics["prefix_terminal_auroc"]
            selection_improves = lambda score, best: score > best + args.early_stop_min_delta
        else:
            raise ValueError(f"Unknown selection metric: {args.selection_metric}")
        if scheduler is not None:
            if args.lr_scheduler == "plateau":
                scheduler.step(-selection_score if args.selection_metric.endswith("auroc") else selection_score)
            else:
                scheduler.step()
        row: Dict[str, float | int] = {
            "epoch": epoch,
            "train_loss": train_loss,
            "train_td0_loss": train_loss if args.loss_type == "td0" else None,
            "train_mc_loss": train_loss if args.loss_type == "mc" else None,
            "loss_type": args.loss_type,
            "lr": optimizer.param_groups[0]["lr"],
            "selection_score": selection_score,
            "selection_metric": selection_metric_name,
            "selection_source": selection_source,
            **(
                add_prefix(val_metrics, "internal")
                if external_val_metrics is not None
                else val_metrics
            ),
        }
        if internal_prefix_metrics is not None:
            row.update(add_prefix(internal_prefix_metrics, "internal"))
        if external_val_metrics is not None:
            row.update(add_prefix(external_val_metrics, "external"))
        if external_prefix_metrics is not None:
            row.update(add_prefix(external_prefix_metrics, "external"))
        history.append(row)
        print(json.dumps(row, sort_keys=True))

        if epoch == 1 and args.selection_metric.endswith("auroc"):
            best_val = float("-inf")
        improved = selection_improves(selection_score, best_val)
        if improved:
            best_val = selection_score
            epochs_without_improvement = 0
            torch.save(
                checkpoint_payload(
                    model=model,
                    input_dim=input_dim,
                    args=args,
                    feature_mean=feature_mean,
                    feature_std=feature_std,
                    feature_keys=feature_keys,
                    external_feature_keys=external_feature_keys,
                    val_metrics=val_metrics,
                    external_val_metrics=external_val_metrics,
                    internal_prefix_metrics=internal_prefix_metrics,
                    external_prefix_metrics=external_prefix_metrics,
                    selection_metric_name=selection_metric_name,
                    selection_score=selection_score,
                    epoch=epoch,
                ),
                best_path,
            )
        else:
            epochs_without_improvement += 1

        if args.checkpoint_every_epochs > 0 and epoch % args.checkpoint_every_epochs == 0:
            torch.save(
                checkpoint_payload(
                    model=model,
                    input_dim=input_dim,
                    args=args,
                    feature_mean=feature_mean,
                    feature_std=feature_std,
                    feature_keys=feature_keys,
                    external_feature_keys=external_feature_keys,
                    val_metrics=val_metrics,
                    external_val_metrics=external_val_metrics,
                    internal_prefix_metrics=internal_prefix_metrics,
                    external_prefix_metrics=external_prefix_metrics,
                    selection_metric_name=selection_metric_name,
                    selection_score=selection_score,
                    epoch=epoch,
                ),
                output_dir / f"checkpoint_epoch_{epoch:04d}.pt",
            )

        if args.early_stop_patience > 0 and epochs_without_improvement >= args.early_stop_patience:
            print(
                f"Early stopping at epoch {epoch}: no {selection_metric_name} improvement "
                f"for {epochs_without_improvement} epochs"
            )
            break

    with open(output_dir / "train_history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
    with open(output_dir / "feature_stats.json", "w", encoding="utf-8") as f:
        json.dump(
            {
                "feature_keys": feature_keys,
                "mean": feature_mean.tolist(),
                "std": feature_std.tolist(),
                "max_episode_steps": args.max_episode_steps,
                "add_all_feature_deltas": args.add_all_feature_deltas,
                "add_temporal_features": args.add_temporal_features,
                "temporal_feature_source": args.temporal_feature_source,
            },
            f,
            indent=2,
        )

    print(f"Best checkpoint: {best_path}")
    print(f"Best selection {selection_metric_name}: {best_val:.6f}")


if __name__ == "__main__":
    main()
