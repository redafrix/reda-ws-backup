#!/usr/bin/env bash
set -euo pipefail

# Experiment setup
EXP_ROOT="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v9_exp03"
# ENV_PYTHON="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/envs/simvla/bin/python"
ENV_PYTHON="/usr/bin/python3"

export PYTHONPATH="$EXP_ROOT/code:${PYTHONPATH:-}"

cd "$EXP_ROOT"

"$ENV_PYTHON" "$EXP_ROOT/code/phase2_tdqc/train_tdqc.py" \
  --train_path "$EXP_ROOT/data/v9_train.pt" \
  --val_path "$EXP_ROOT/data/v9_val.pt" \
  --test_path "$EXP_ROOT/data/v9_test.pt" \
  --output_dir "$EXP_ROOT/runs/" \
  --hidden_dim 256 \
  --num_layers 2 \
  --dropout 0.05 \
  --batch_size 64 \
  --epochs 500 \
  --lr 1e-4 \
  --weight_decay 1e-2 \
  --seed 0 \
  --early_stop_patience 20 \
  --device "cuda"
