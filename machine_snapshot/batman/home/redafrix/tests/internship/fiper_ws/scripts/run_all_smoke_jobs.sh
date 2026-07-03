#!/usr/bin/env bash
set -euo pipefail

# Sourcing Bob's environment setup
source "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"

cd "/media/rootalkhatib/My Passport/reda_ws/fiper_ws"

OUTPUT_ROOT="/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/clean_temporal_nextgen_smoke_20260527"
mkdir -p "$OUTPUT_ROOT"

# Lists of datasets to run all model families on
ALL_JOBS_DATASETS=(
  "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_01_holdout_butter_chocolate_pudding/datasets/refs"
  "experiments/prepared_20260527/02_ood_perturbation_holdout_object/datasets/refs"
)

# Lists of datasets to run one representative model family on
SINGLE_JOB_DATASETS=(
  "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs"
  "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_02_holdout_cream_cheese_ketchup/datasets/refs"
  "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_03_holdout_milk_orange_juice/datasets/refs"
  "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_04_holdout_salad_dressing_tomato_sauce/datasets/refs"
  "experiments/prepared_20260527/01_ood_task_8_9/datasets/refs"
  "experiments/prepared_20260527/02_ood_perturbation_holdout_mug/datasets/refs"
  "experiments/prepared_20260527/02_ood_perturbation_holdout_milk/datasets/refs"
  "experiments/prepared_20260527/02_ood_perturbation_holdout_env/datasets/refs"
  "experiments/prepared_20260527/03_ood_suite_family_holdout_spatial/datasets/refs"
  "experiments/prepared_20260527/03_ood_suite_family_holdout_object_family/datasets/refs"
  "experiments/prepared_20260527/03_ood_suite_family_holdout_goal/datasets/refs"
  "experiments/prepared_20260527/03_ood_suite_family_holdout_10_family/datasets/refs"
  "experiments/prepared_20260527/00_global_main/datasets/refs"
)

echo "=== Running ALL jobs on target splits ==="
for refs in "${ALL_JOBS_DATASETS[@]}"; do
  split_name=$(basename "$(dirname "$(dirname "$refs")")")
  echo "--- Split: $split_name (All 7 Jobs) ---"
  $PYTHON_BIN scripts/run_clean_temporal_nextgen_campaign_v1.py \
    --campaign-config configs/clean_temporal_nextgen_campaign_v1.json \
    --refs-dir "$refs" \
    --output-dir "$OUTPUT_ROOT/$split_name" \
    --base-dir "." \
    --device cuda \
    --max-epochs 1 \
    --max-train-rows 10000 \
    --max-calib-rows 4000 \
    --max-eval-rows 4000 \
    --batch-size 256 \
    --seed 42
done

echo "=== Running ONE model on remaining splits ==="
for refs in "${SINGLE_JOB_DATASETS[@]}"; do
  split_name=$(basename "$(dirname "$(dirname "$refs")")")
  echo "--- Split: $split_name (ng_041_tcn_k8_score_only) ---"
  $PYTHON_BIN scripts/run_clean_temporal_nextgen_campaign_v1.py \
    --campaign-config configs/clean_temporal_nextgen_campaign_v1.json \
    --refs-dir "$refs" \
    --output-dir "$OUTPUT_ROOT/$split_name" \
    --base-dir "." \
    --device cuda \
    --max-epochs 1 \
    --max-train-rows 10000 \
    --max-calib-rows 4000 \
    --max-eval-rows 4000 \
    --batch-size 256 \
    --seed 42 \
    --only-job ng_041_tcn_k8_score_only
done

echo "=== Smoke campaign finished successfully ==="
