#!/usr/bin/env bash
set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

DATASET_PATH="${DATASET_PATH:-$WS_ROOT/outputs/runs/tdqc_dataset/phase1_uncertainty_rollouts.pt}"
CKPT="${CKPT:-$WS_ROOT/outputs/runs/tdqc_calibrator/lstm_td0/best.pt}"

python phase2_tdqc/eval_tdqc.py \
  --dataset_path "$DATASET_PATH" \
  --ckpt "$CKPT" \
  --batch_size 64
