#!/usr/bin/env bash
set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$WS_ROOT"

# Validated configuration for this machine:
# - wrist-only LIBERO
# - released SimVLA-code LIBERO dataset scope
#   (libero_10, goal, object, spatial, libero_90)
# - action-heads-only training
# - batch size 32
# - 2 dataloader workers
# - total 10000 steps
# - checkpoints at step 5001 and final step 10000

ITERS=10000 \
FREEZE_STEPS=10000 \
FREEZE_MODE=action_heads_only \
BATCH_SIZE=32 \
NUM_WORKERS=2 \
SAVE_INTERVAL=5001 \
LOG_INTERVAL=20 \
SUBSETS="libero_10 libero_goal libero_object libero_spatial libero_90" \
OUTPUT_DIR="$WS_ROOT/outputs/runs/simvla_libero_actionheads_bs32_10k" \
"$WS_ROOT/simvla/scripts/run_simvla_wrist_finetune.sh"
