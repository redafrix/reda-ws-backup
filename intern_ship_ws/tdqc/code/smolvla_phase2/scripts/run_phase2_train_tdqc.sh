#!/usr/bin/env bash
set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

DATASET_PATH="${DATASET_PATH:-$WS_ROOT/outputs/runs/tdqc_dataset/phase1_uncertainty_rollouts.pt}"
OUTPUT_DIR="${OUTPUT_DIR:-$WS_ROOT/outputs/runs/tdqc_calibrator/lstm_td0}"

python phase2_tdqc/train_tdqc.py \
  --dataset_path "$DATASET_PATH" \
  --output_dir "$OUTPUT_DIR" \
  --hidden_dim 128 \
  --num_layers 1 \
  --dropout 0.05 \
  --batch_size 64 \
  --epochs 200 \
  --lr 1e-4 \
  --weight_decay 1e-2 \
  --target_update_freq 100 \
  --train_ratio 0.8 \
  --seed 0
