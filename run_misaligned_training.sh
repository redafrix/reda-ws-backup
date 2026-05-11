#!/usr/bin/env bash
set -e
source $HOME/miniconda3/etc/profile.d/conda.sh
conda activate /home/redafrix/tests/intern_ship_research/intern_ship_ws/assets/envs/envs/simvla
export PYTHONNOUSERSITE=1
export WS_ROOT=/home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone
export PYTHONPATH=$WS_ROOT/code:$PYTHONPATH

echo "WS_ROOT: $WS_ROOT"
echo "PYTHONPATH: $PYTHONPATH"
echo "Device: cuda"

# Clean up old run
rm -rf $WS_ROOT/results/checkpoints/lstm_misaligned_500epochs/*

# Run training
python $WS_ROOT/code/phase2_tdqc/train_tdqc.py \
    --dataset_path $WS_ROOT/data/final_calibrated_3924rollouts_misaligned.pt \
    --output_dir $WS_ROOT/results/checkpoints/lstm_misaligned_500epochs \
    --epochs 500 \
    --lr 1e-4 \
    --device cuda
