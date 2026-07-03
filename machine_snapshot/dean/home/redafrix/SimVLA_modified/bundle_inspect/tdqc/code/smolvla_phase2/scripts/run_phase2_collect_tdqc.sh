#!/usr/bin/env bash
set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
PHASE2_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_PATH="$WS_ROOT/assets/envs/simvla"

# Config
PHASE1_CKPT="${PHASE1_CKPT:-$WS_ROOT/outputs/runs/simvla_libero_uncertainty/ckpt-60000}"
SMOLVLM_MODEL="$WS_ROOT/assets/models/huggingface/SmolVLM-500M-Instruct"
NORM_STATS="$WS_ROOT/outputs/temp/libero_wrist_norm.json"
PORT="${PORT:-8001}"
OUTPUT_PATH="${OUTPUT_PATH:-$WS_ROOT/outputs/runs/tdqc_dataset/task5_uncertainty_100rollouts.pt}"

export PYTHONPATH="$PHASE2_ROOT:$PYTHONPATH"

echo "=========================================================="
echo "🚀 Phase 2: Starting TDQC Data Collection"
echo "Checkpoint: $PHASE1_CKPT"
echo "Output: $OUTPUT_PATH"
echo "Port: $PORT"
echo "=========================================================="

# 1. Start Patched Server in background
echo "Starting TDQC Policy Server..."
"$ENV_PATH/bin/python" "$PHASE2_ROOT/phase2_tdqc/serve_tdqc_collection.py" \
  --checkpoint "$PHASE1_CKPT" \
  --smolvlm_model "$SMOLVLM_MODEL" \
  --norm_stats "$NORM_STATS" \
  --port "$PORT" &
SERVER_PID=$!

# Cleanup on exit
trap "kill $SERVER_PID" EXIT

# Wait for server
echo "Waiting for server to load weights (approx 20s)..."
sleep 25

# 2. Start Collection Client
echo "Starting LIBERO Rollouts..."
"$ENV_PATH/bin/python" "$PHASE2_ROOT/phase2_tdqc/collect_tdqc_rollouts.py" \
  --host "127.0.0.1" \
  --port "$PORT" \
  --task_suite "libero_spatial" \
  --task_id 5 \
  --num_rollouts 100 \
  --output_path "$OUTPUT_PATH"

echo "✅ Data collection complete."
