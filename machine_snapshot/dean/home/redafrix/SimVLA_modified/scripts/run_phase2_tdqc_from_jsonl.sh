#!/usr/bin/env bash
set -euo pipefail

JSONL_PATH="${1:?Usage: $0 path/to/uncertainty_log.jsonl [output_name]}"
NAME="${2:-$(basename "${JSONL_PATH}" .jsonl)}"

DATASET_DIR="runs/tdqc_datasets"
OUTPUT_DIR="runs/tdqc_calibrator/${NAME}"
DATASET_PATH="${DATASET_DIR}/${NAME}_tdqc.pt"

mkdir -p "${DATASET_DIR}" "${OUTPUT_DIR}"

python -m phase2_tdqc.convert_uncertainty_jsonl_to_tdqc \
  --input_jsonl "${JSONL_PATH}" \
  --output_path "${DATASET_PATH}"

python -m phase2_tdqc.train_tdqc_calibrator \
  --dataset_path "${DATASET_PATH}" \
  --output_dir "${OUTPUT_DIR}" \
  --epochs 100 \
  --batch_size 32 \
  --lr 1e-4 \
  --hidden_dim 64 \
  --target_update_freq 25
