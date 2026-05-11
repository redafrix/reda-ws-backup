#!/usr/bin/env bash
source intern_ship_ws/activate_mamba.sh
cd intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v8_exp12_mamba
python train_tdqc.py \
    --dataset_path "../../data/v8_balanced/v8_train.pt" \
    --val_path "../../data/v8_balanced/v8_val.pt" \
    --test_path "../../data/v8_balanced/v8_test.pt" \
    --output_dir "./outputs/v8_mamba_mc_v1" \
    --epochs 500 \
    --batch_size 64 \
    --early_stopping_patience 40 \
    2>&1 | tee ./outputs/v8_mamba_mc_v1/training.log
