#!/usr/bin/env bash
set -euo pipefail

# Path Configuration
WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUTPUT_DIR="$WS_ROOT/outputs/runs/sweep_test_3_lr_1e-4"
LOG_FILE="$OUTPUT_DIR/sweep_test_3.log"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# Training Parameters for Test 3
export LEARNING_RATE=1e-4
export BATCH_SIZE=32
export ITERS=2000
export WARMUP_STEPS=1000
export WEIGHT_DECAY=0.0
export FREEZE_MODE=action_heads_only
export FREEZE_STEPS=2000  # Keep VLM and Transformer Core frozen for the entire 2000 iterations
export OUTPUT_DIR="$OUTPUT_DIR"

# Uncertainty and Schedule Settings
export PREDICT_UNCERTAINTY=true
export USE_COSINE_DECAY=true

# Checkpointing and Logging
export SAVE_INTERVAL=2000
export LOG_INTERVAL=10

# Weights and Data
export PRETRAINED_CKPT="$WS_ROOT/assets/models/huggingface/SimVLA-LIBERO"

# Start training and log everything to the run directory
echo "=========================================================="
echo "🚀 Starting LR Sweep Test 3: LR=1e-4"
echo "Output Dir: $OUTPUT_DIR"
echo "Log File:   $LOG_FILE"
echo "=========================================================="

cd "$WS_ROOT"
"$WS_ROOT/simvla/scripts/run_simvla_wrist_finetune.sh" 2>&1 | tee -a "$LOG_FILE"

echo "=========================================================="
echo "✅ Test 3 Completed"
echo "=========================================================="
