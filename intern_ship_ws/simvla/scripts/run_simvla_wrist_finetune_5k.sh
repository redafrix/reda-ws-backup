#!/usr/bin/env bash
set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$WS_ROOT"

# Memory-safe training profile validated on this machine:
# - batch size 1
# - 2 dataloader workers
# - keep backbone frozen for the whole run
# - train for 5000 steps

ITERS=5000 \
FREEZE_STEPS=5000 \
BATCH_SIZE=1 \
NUM_WORKERS=2 \
SAVE_INTERVAL=1000 \
LOG_INTERVAL=20 \
OUTPUT_DIR="$WS_ROOT/outputs/runs/simvla_libero_wrist_only_5k" \
"$WS_ROOT/simvla/scripts/run_simvla_wrist_finetune.sh"
