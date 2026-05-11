#!/bin/bash

# Experiment: Transformer v5 (Honest Dynamics)
# Goal: Eliminate Step 0 cheating via Relative Feature Mapping and Sinusoidal PE.

export PYTHONPATH=$PYTHONPATH:$(pwd)
source activate_simvla.sh

DATASET_PATH="../../../data/v8_balanced/v8_train.pt"
OUTPUT_DIR="../outputs_v1"

echo "🚀 Launching Transformer v5 (Honest Dynamics)..."
echo "Upgrades: Relative Mapping (x-x0), Sinusoidal PE, TD Loss, AdamW 1e-4, No Truncation."

python train_tdqc.py \
    --dataset_path "$DATASET_PATH" \
    --output_dir "$OUTPUT_DIR" \
    --hidden_dim 256 \
    --num_layers 4 \
    --n_heads 8 \
    --dropout 0.1 \
    --batch_size 64 \
    --epochs 200 \
    --lr 1e-4 \
    --warmup_epochs 5 \
    --weight_decay 1e-2 \
    --target_update_freq 100 \
    --seed 0 \
    --patience 30
