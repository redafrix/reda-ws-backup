"""Trainer for Isaac Mimic H10 Single-Head monitor across seeds 0..4."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import random
import time
from typing import Any, Dict, List

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from .constants import (
    BATCH_SIZE,
    EPOCHS,
    EXPERIMENT_NAME,
    GRAD_CLIP_NORM,
    LR,
    SEEDS,
    WEIGHT_DECAY,
)
from .dataset import IsaacMimicWindowDataset
from .metrics import compute_row_metrics
from .model import MimicH10RiskMonitor


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def train_single_seed(
    derived_dataset_dir: Path | str,
    output_dir: Path | str,
    seed: int,
    device: torch.device,
) -> Dict[str, Any]:
    derived_dir = Path(derived_dataset_dir)
    out_dir = Path(output_dir) / f'seed_{seed}'
    out_dir.mkdir(parents=True, exist_ok=True)

    set_seed(seed)

    # Load arrays
    raw_scalars = np.load(derived_dir / 'raw/scalar37.npy')
    raw_horizon = np.load(derived_dir / 'raw/horizon10x6.npy')
    labels = np.load(derived_dir / 'labels.npy')
    episode_indices = np.load(derived_dir / 'episode_index.npy')
    decision_indices = np.load(derived_dir / 'decision_index.npy')
    split_indices = np.load(derived_dir / 'split_index.npy')

    with open(derived_dir / 'normalization.json') as f:
        norm_params = json.load(f)

    train_row_idx = np.where(split_indices == 0)[0]
    val_row_idx = np.where(split_indices == 1)[0]

    train_labels = labels[train_row_idx]
    n_pos = int(np.sum(train_labels == 1))
    n_neg = int(np.sum(train_labels == 0))
    pos_weight_val = float(n_neg / max(1, n_pos))
    pos_weight = torch.tensor([pos_weight_val], device=device, dtype=torch.float32)

    train_dataset = IsaacMimicWindowDataset(
        raw_scalars, raw_horizon, labels, episode_indices, decision_indices, norm_params, row_indices=train_row_idx
    )
    val_dataset = IsaacMimicWindowDataset(
        raw_scalars, raw_horizon, labels, episode_indices, decision_indices, norm_params, row_indices=val_row_idx
    )

    train_generator = torch.Generator().manual_seed(seed)
    train_loader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        generator=train_generator,
        drop_last=False,
        num_workers=0,
    )
    val_loader = DataLoader(
        val_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        drop_last=False,
        num_workers=0,
    )

    model = MimicH10RiskMonitor().to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    best_val_auprc = -1.0
    best_epoch = -1
    best_checkpoint_path = out_dir / 'best_model.pt'

    epoch_logs = []

    for epoch in range(1, EPOCHS + 1):
        model.train()
        total_loss = 0.0
        train_preds, train_targets = [], []

        for b_s, b_h, b_y in train_loader:
            b_s = b_s.to(device)
            b_h = b_h.to(device)
            b_y = b_y.to(device)

            optimizer.zero_grad()
            logits = model(b_s, b_h)
            loss = criterion(logits, b_y)
            loss.backward()

            nn.utils.clip_grad_norm_(model.parameters(), max_norm=GRAD_CLIP_NORM)
            optimizer.step()

            total_loss += float(loss.item()) * len(b_y)
            train_preds.extend(torch.sigmoid(logits).detach().cpu().numpy())
            train_targets.extend(b_y.detach().cpu().numpy())

        train_loss = total_loss / len(train_dataset)
        train_metrics = compute_row_metrics(train_targets, train_preds)

        model.eval()
        val_loss = 0.0
        val_preds, val_targets = [], []

        with torch.no_grad():
            for b_s, b_h, b_y in val_loader:
                b_s = b_s.to(device)
                b_h = b_h.to(device)
                b_y = b_y.to(device)

                logits = model(b_s, b_h)
                loss = criterion(logits, b_y)

                val_loss += float(loss.item()) * len(b_y)
                val_preds.extend(torch.sigmoid(logits).cpu().numpy())
                val_targets.extend(b_y.cpu().numpy())

        val_loss = val_loss / len(val_dataset)
        val_metrics = compute_row_metrics(val_targets, val_preds)

        epoch_record = {
            'epoch': epoch,
            'train_loss': train_loss,
            'train_auroc': train_metrics['auroc'],
            'train_auprc': train_metrics['auprc'],
            'val_loss': val_loss,
            'val_auroc': val_metrics['auroc'],
            'val_auprc': val_metrics['auprc'],
        }
        epoch_logs.append(epoch_record)

        torch.save(
            {
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'val_auprc': val_metrics['auprc'],
                'seed': seed,
            },
            out_dir / f'checkpoint_epoch_{epoch:02d}.pt',
        )

        if val_metrics['auprc'] > best_val_auprc:
            best_val_auprc = val_metrics['auprc']
            best_epoch = epoch
            torch.save(
                {
                    'epoch': epoch,
                    'model_state_dict': model.state_dict(),
                    'val_auprc': val_metrics['auprc'],
                    'val_auroc': val_metrics['auroc'],
                    'seed': seed,
                },
                best_checkpoint_path,
            )

    training_manifest = {
        'seed': seed,
        'best_epoch': best_epoch,
        'best_val_auprc': best_val_auprc,
        'pos_weight': pos_weight_val,
        'n_pos_train': n_pos,
        'n_neg_train': n_neg,
        'runtime_environment': {
            'torch_version': torch.__version__,
            'cuda_available': torch.cuda.is_available(),
            'cuda_version': torch.version.cuda if torch.cuda.is_available() else None,
            'device_name': torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'cpu',
        },
        'epoch_logs': epoch_logs,
    }

    with open(out_dir / 'training_summary.json', 'w') as f:
        json.dump(training_manifest, f, indent=2)

    return training_manifest


def main() -> None:
    parser = argparse.ArgumentParser(description='Train Isaac Mimic H10 Single-Head Risk Monitor')
    parser.add_argument('--derived_dir', type=str, required=True, help='Path to derived dataset directory')
    parser.add_argument('--output_dir', type=str, required=True, help='Path to output model directory')
    parser.add_argument('--seeds', type=int, nargs='+', default=list(SEEDS), help='List of seeds to train')
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    args = parser.parse_args()

    dev = torch.device(args.device)
    print(f'Training on device: {dev}, seeds: {args.seeds}')

    for s in args.seeds:
        print(f'=== Starting Training Seed {s} ===')
        res = train_single_seed(args.derived_dir, args.output_dir, s, dev)
        b_ep = res['best_epoch']
        b_val = res['best_val_auprc']
        print(f'Seed {s} Done! Best Epoch: {b_ep}, Val AUPRC: {b_val:.4f}')


if __name__ == '__main__':
    main()
