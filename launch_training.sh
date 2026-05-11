#!/usr/bin/env bash
source intern_ship_ws/activate_mamba.sh
cd intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v8_exp12_mamba
python train_tdqc.py \
    --dataset_path "../../data/v7_22d/v7_22d_train.pt" \
    --output_dir "./outputs/production_v1" \
    --epochs 200 \
    --batch_size 64 \
    --early_stopping_patience 30 \
    2>&1 | tee ./outputs/production_v1/training.log
