#!/usr/bin/env bash
# run_uncertainty_lr_sweep.sh
set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LRS=("8e-5" "5e-5" "2e-5" "1e-5")

# Ensure we are in the workspace
cd "$WS_ROOT"

for LR in "${LRS[@]}"; do
    echo "=========================================================="
    echo "🚀 Starting test with LEARNING_RATE=$LR"
    echo "=========================================================="
    
    # Configuration based on your confirmed details:
    # - action_heads_only: frozen VLM and Core
    # - batch_size 32
    # - no weight decay
    # - warmup 1000 steps (ramp to full LR at midpoint)
    # - save only at the end (2000 steps)
    # - start from original SimVLA weights each time
    
    env ITERS=2000 \
        WARMUP_STEPS=1000 \
        FREEZE_STEPS=2000 \
        FREEZE_MODE=action_heads_only \
        BATCH_SIZE=32 \
        LEARNING_RATE="$LR" \
        WEIGHT_DECAY=0.0 \
        SAVE_INTERVAL=2000 \
        LOG_INTERVAL=10 \
        PREDICT_UNCERTAINTY=true \
        OUTPUT_DIR="$WS_ROOT/outputs/runs/uncertainty_sweep_lr_$LR" \
        "$WS_ROOT/simvla/scripts/run_simvla_wrist_finetune.sh"
    
    echo "✅ Finished test for LR=$LR"
    echo "----------------------------------------------------------"
done

echo "🎉 All LR sweep tests completed!"
