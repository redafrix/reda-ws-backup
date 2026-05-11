#!/usr/bin/env bash
# train_v7_fixed_v3.sh

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXP_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Activate the environment
source "$SCRIPT_DIR/activate_simvla.sh"

# Define paths
DATASET_PATH="/media/redafrix/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt"
OUTPUT_DIR="$EXP_ROOT/outputs_v1"

# Ensure output directory exists (script will now handle safety)
mkdir -p "$OUTPUT_DIR"

echo "Starting Retraining of Transformer v4 (MC Loss)..."
echo "Upgrades: CausalConv1D + ALiBi + QK-Norm + Learnable Temp + Random Truncation + MC Loss"
echo "Optimizer: AdamW (Standard)"
echo "Output Directory: $OUTPUT_DIR"

# Run training in background with nohup
# Using python -u for unbuffered output
nohup python -u "$SCRIPT_DIR/train_tdqc.py" \
    --dataset_path "$DATASET_PATH" \
    --output_dir "$OUTPUT_DIR" \
    --hidden_dim 256 \
    --num_layers 4 \
    --n_heads 8 \
    --dropout 0.1 \
    --batch_size 64 \
    --epochs 600 \
    --lr 1e-4 \
    --patience 100 \
    --device cuda > "$OUTPUT_DIR/training.log" 2>&1 &

echo "Training started in background. PID: $!"
echo "Follow logs with: tail -f $OUTPUT_DIR/training.log"
