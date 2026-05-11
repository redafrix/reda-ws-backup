#!/bin/bash
set -e

# Configuration
EXP_DIR="experiments/v8_exp10_33d"
PYTHON="/home/redafrix/envs/simvla/bin/python"
PYTHONNOUSERSITE=1
export PYTHONPATH="${EXP_DIR}/code/"

# Ensure output dir exists
mkdir -p ${EXP_DIR}/runs/

echo "Starting Training for Exp 10 (33D features)..."
$PYTHON -u ${EXP_DIR}/code/phase2_tdqc/train_tdqc.py \
    --train_path data/v8_33d/v8_train.pt \
    --val_path data/v8_33d/v8_val.pt \
    --test_path data/v8_33d/v8_test.pt \
    --output_dir ${EXP_DIR}/runs/ \
    --epochs 500 \
    --early_stop_patience 40 \
    --batch_size 128 \
    --hidden_dim 256 --num_layers 2 --dropout 0.3 --weight_decay 0.05 \
    > ${EXP_DIR}/runs/training_log.txt 2>&1

echo "Training complete. Running Evaluations..."

# Run ID Eval
$PYTHON ${EXP_DIR}/code/eval_exp10.py --dataset data/v8_33d/v8_test.pt --name "In-Distribution"
# Run OOD Eval
$PYTHON ${EXP_DIR}/code/eval_exp10.py --dataset data/v8_33d/v8_unseen_obj_ood.pt --name "Out-of-Distribution"

# Final Report
echo "--- FINAL SUMMARY ---"
ID_BRIER=$(grep -oP '"brier": \K[\d.]+' ${EXP_DIR}/runs/results_in_distribution.json)
ID_AUC=$(grep -oP '"auc": \K[\d.]+' ${EXP_DIR}/runs/results_in_distribution.json)
OOD_BRIER=$(grep -oP '"brier": \K[\d.]+' ${EXP_DIR}/runs/results_out_of_distribution.json)
OOD_AUC=$(grep -oP '"auc": \K[\d.]+' ${EXP_DIR}/runs/results_out_of_distribution.json)
RATIO=$(echo "scale=4; $OOD_BRIER / $ID_BRIER" | bc)

echo "ID Brier: $ID_BRIER | ID AUC: $ID_AUC"
echo "OOD Brier: $OOD_BRIER | OOD AUC: $OOD_AUC"
echo "OOD/ID Brier Ratio: $RATIO"
