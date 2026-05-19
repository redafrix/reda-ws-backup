from __future__ import annotations

import argparse
import json
import os
import random
import time
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch.utils.data import DataLoader

from training_stage9.stage9_dataset import Stage9RiskDataset, collate_stage9, parse_source_remaps
from training_stage9.stage9_eval import summarize_predictions, write_eval_report, write_predictions
from training_stage9.stage9_losses import compute_stage9_loss, risk_prob_from_outputs
from training_stage9.stage9_models import Stage9Dims, create_model, model_config


EVAL_SPLITS = ["calib", "test_seen_task", "test_unseen_task", "test_unseen_seed", "test_unseen_perturbation"]


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def move_batch(batch: dict[str, Any], device: torch.device) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in batch.items():
        out[key] = value.to(device) if torch.is_tensor(value) else value
    return out


def make_loader(dataset: Stage9RiskDataset, batch_size: int, shuffle: bool, workers: int) -> DataLoader:
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=workers,
        pin_memory=torch.cuda.is_available(),
        collate_fn=collate_stage9,
        drop_last=False,
    )


def evaluate_model(
    model: torch.nn.Module,
    loader: DataLoader,
    device: torch.device,
    target_mode: str,
    split_name: str,
    mc_dropout_passes: int = 0,
) -> list[dict[str, Any]]:
    model.eval()
    rows: list[dict[str, Any]] = []
    if mc_dropout_passes > 1:
        model.train()
    with torch.no_grad():
        for batch in loader:
            dev_batch = move_batch(batch, device)
            if mc_dropout_passes > 1:
                probs = []
                for _ in range(mc_dropout_passes):
                    probs.append(risk_prob_from_outputs(model(dev_batch), target_mode).detach().cpu())
                prob = torch.stack(probs).mean(dim=0).numpy()
                prob_std = torch.stack(probs).std(dim=0).numpy()
            else:
                prob_tensor = risk_prob_from_outputs(model(dev_batch), target_mode).detach().cpu()
                prob = prob_tensor.numpy()
                prob_std = np.zeros_like(prob)
            for i, sample_id in enumerate(batch["sample_id"]):
                rows.append(
                    {
                        "split": split_name,
                        "sample_id": sample_id,
                        "state_id": batch["state_id"][i],
                        "task_name": batch["task_name"][i],
                        "perturbation_type": batch["perturbation_type"][i],
                        "seed": batch["seed"][i],
                        "label": batch["label"][i],
                        "bad_subtype": batch["bad_subtype"][i],
                        "risk_prob": float(prob[i]),
                        "risk_prob_std": float(prob_std[i]),
                        "target_value": float(batch["target"][i].item()),
                        "weight": float(batch["weight"][i].item()),
                    }
                )
    model.train()
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--target-mode", required=True, choices=["clean_binary", "soft_labels", "soft_no_ambiguous", "ordinal", "subtype_multitask"])
    parser.add_argument("--source-remap", action="append")
    parser.add_argument("--epochs", type=int, default=8)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--lr", type=float, default=2e-4)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--num-workers", type=int, default=2)
    parser.add_argument("--max-train-samples", type=int)
    parser.add_argument("--max-eval-samples", type=int)
    parser.add_argument("--balanced-binary-train", action="store_true")
    parser.add_argument("--seed", type=int, default=9009)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--mc-dropout-passes", type=int, default=0)
    args = parser.parse_args()

    seed_everything(args.seed)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    source_remaps = parse_source_remaps(args.source_remap)
    device = torch.device(args.device if torch.cuda.is_available() or args.device == "cpu" else "cpu")

    train_dataset = Stage9RiskDataset(
        Path(args.split_dir) / "train.jsonl",
        args.target_mode,
        source_remaps,
        max_samples=args.max_train_samples,
        balance_binary=args.balanced_binary_train,
    )
    if len(train_dataset) == 0:
        raise RuntimeError("empty train dataset after target filtering")
    dims = Stage9Dims(
        flat_dim=train_dataset.flat_dim,
        context_action_dim=train_dataset.context_action_dim,
        action_flat_dim=train_dataset.action_flat_dim,
        action_steps=train_dataset.action_steps,
        action_dim=train_dataset.action_dim,
        history_steps=train_dataset.history_steps,
        history_dim=train_dataset.history_dim,
    )
    train_loader = make_loader(train_dataset, args.batch_size, True, args.num_workers)
    calib_dataset = Stage9RiskDataset(Path(args.split_dir) / "calib.jsonl", args.target_mode, source_remaps, max_samples=args.max_eval_samples)
    calib_loader = make_loader(calib_dataset, args.batch_size, False, args.num_workers)

    model = create_model(args.model, dims, args.target_mode).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scaler = torch.cuda.amp.GradScaler(enabled=device.type == "cuda")

    config = {
        "model": args.model,
        "target_mode": args.target_mode,
        "split_dir": args.split_dir,
        "output_dir": str(out_dir),
        "source_remap": args.source_remap or [],
        "epochs": args.epochs,
        "batch_size": args.batch_size,
        "lr": args.lr,
        "weight_decay": args.weight_decay,
        "max_train_samples": args.max_train_samples,
        "max_eval_samples": args.max_eval_samples,
        "balanced_binary_train": args.balanced_binary_train,
        "seed": args.seed,
        "device": str(device),
        "torch_version": torch.__version__,
        "cuda_name": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
        "model_config": model_config(args.model, args.target_mode, dims),
    }
    (out_dir / "config.json").write_text(json.dumps(config, indent=2, sort_keys=True, default=str) + "\n")

    history: list[dict[str, Any]] = []
    best_score = -1.0
    best_path = out_dir / "checkpoint.pt"
    start = time.time()
    for epoch in range(1, args.epochs + 1):
        model.train()
        losses: list[float] = []
        for batch in train_loader:
            batch = move_batch(batch, device)
            optimizer.zero_grad(set_to_none=True)
            with torch.cuda.amp.autocast(enabled=device.type == "cuda"):
                outputs = model(batch)
                loss, parts = compute_stage9_loss(outputs, batch, args.target_mode)
            scaler.scale(loss).backward()
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            scaler.step(optimizer)
            scaler.update()
            losses.append(float(loss.detach().cpu()))
        calib_rows = evaluate_model(model, calib_loader, device, args.target_mode, "calib")
        calib_metrics = summarize_predictions(calib_rows)["calib"]["clean_binary"]
        score = calib_metrics.get("auroc_bad")
        if score is None:
            score = -calib_metrics.get("brier", 1.0)
        epoch_row = {
            "epoch": epoch,
            "train_loss": float(np.mean(losses)) if losses else None,
            "calib_auroc_bad": calib_metrics.get("auroc_bad"),
            "calib_auprc_bad": calib_metrics.get("auprc_bad"),
            "calib_brier": calib_metrics.get("brier"),
            "seconds_elapsed": time.time() - start,
        }
        history.append(epoch_row)
        print(json.dumps(epoch_row, sort_keys=True), flush=True)
        if float(score) > best_score:
            best_score = float(score)
            torch.save(
                {
                    "model_state_dict": model.state_dict(),
                    "config": config,
                    "dims": dims.__dict__,
                    "best_score": best_score,
                    "epoch": epoch,
                },
                best_path,
            )

    checkpoint = torch.load(best_path, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"])
    all_predictions: list[dict[str, Any]] = []
    for split in EVAL_SPLITS:
        path = Path(args.split_dir) / f"{split}.jsonl"
        if not path.exists():
            continue
        dataset = Stage9RiskDataset(path, args.target_mode, source_remaps, max_samples=args.max_eval_samples)
        loader = make_loader(dataset, args.batch_size, False, args.num_workers)
        all_predictions.extend(evaluate_model(model, loader, device, args.target_mode, split))
    if args.mc_dropout_passes and args.mc_dropout_passes > 1:
        mc_rows: list[dict[str, Any]] = []
        for split in EVAL_SPLITS:
            path = Path(args.split_dir) / f"{split}.jsonl"
            if not path.exists():
                continue
            dataset = Stage9RiskDataset(path, args.target_mode, source_remaps, max_samples=args.max_eval_samples)
            loader = make_loader(dataset, args.batch_size, False, args.num_workers)
            mc_rows.extend(evaluate_model(model, loader, device, args.target_mode, split, mc_dropout_passes=args.mc_dropout_passes))
        write_predictions(out_dir / "predictions_mc_dropout.jsonl", mc_rows)
    metrics = {
        "history": history,
        "best_checkpoint": str(best_path),
        "best_score": best_score,
        "train_size": len(train_dataset),
        "splits": summarize_predictions(all_predictions),
    }
    (out_dir / "metrics.json").write_text(json.dumps(metrics, indent=2, sort_keys=True, default=str) + "\n")
    write_predictions(out_dir / "predictions.jsonl", all_predictions)
    write_eval_report(out_dir / "eval_report.md", config, metrics)
    print(json.dumps({"done": True, "output_dir": str(out_dir), "best_score": best_score}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
