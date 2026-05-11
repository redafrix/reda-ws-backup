#!/usr/bin/env bash
# run_uncertainty_server.sh
set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ENV_PATH="$WS_ROOT/assets/envs/simvla"
HOST="0.0.0.0"

# Priorities: 
# 1. Environment variable if set
# 2. Hardcoded fallback
CHECKPOINT_VAR="${CHECKPOINT:-$WS_ROOT/outputs/runs/sweep_test_3_lr_1e-4/ckpt-2000}"
PORT_VAR="${PORT:-8001}"

REPO="$WS_ROOT/simvla/code/SimVLA_modified"
SMOLVLM_MODEL="$WS_ROOT/assets/models/huggingface/SmolVLM-500M-Instruct"
NORM_STATS="$WS_ROOT/outputs/temp/libero_wrist_norm.json"

export PYTHONNOUSERSITE=1
export PYTHONPATH="$REPO:$PYTHONPATH"

echo "=========================================================="
echo "🚀 Launching Uncertainty-Aware SimVLA Server"
echo "Checkpoint: $CHECKPOINT_VAR"
echo "Port: $PORT_VAR"
echo "=========================================================="

cd "$WS_ROOT"
exec "$ENV_PATH/bin/python" "$WS_ROOT/simvla/scripts/serve_simvla_local.py" \
  --repo "$REPO" \
  --checkpoint "$CHECKPOINT_VAR" \
  --smolvlm_model "$SMOLVLM_MODEL" \
  --norm_stats "$NORM_STATS" \
  --host "$HOST" \
  --port "$PORT_VAR"
