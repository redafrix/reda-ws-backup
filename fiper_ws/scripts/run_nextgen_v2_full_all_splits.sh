#!/usr/bin/env bash
set -euo pipefail

source "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"
cd "/media/rootalkhatib/My Passport/reda_ws/fiper_ws"

PYTHON_BIN="${PYTHON_BIN:-python3}"
CONFIG="configs/clean_temporal_nextgen_campaign_v2.json"
OUTPUT_ROOT="experiments/clean_temporal_nextgen_v2_full_all_20260527"
LOG_DIR="logs/nextgen_v2_full_all_20260527"
mkdir -p "$OUTPUT_ROOT" "$LOG_DIR"

REFS_DIRS=(
  "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs"
  "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_01_holdout_butter_chocolate_pudding/datasets/refs"
  "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_02_holdout_cream_cheese_ketchup/datasets/refs"
  "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_03_holdout_milk_orange_juice/datasets/refs"
  "experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_04_holdout_salad_dressing_tomato_sauce/datasets/refs"
  "experiments/prepared_20260527/00_global_main/datasets/refs"
  "experiments/prepared_20260527/01_ood_task_8_9/datasets/refs"
  "experiments/prepared_20260527/02_ood_perturbation_holdout_mug/datasets/refs"
  "experiments/prepared_20260527/02_ood_perturbation_holdout_milk/datasets/refs"
  "experiments/prepared_20260527/02_ood_perturbation_holdout_object/datasets/refs"
  "experiments/prepared_20260527/02_ood_perturbation_holdout_env/datasets/refs"
  "experiments/prepared_20260527/03_ood_suite_family_holdout_spatial/datasets/refs"
  "experiments/prepared_20260527/03_ood_suite_family_holdout_object_family/datasets/refs"
  "experiments/prepared_20260527/03_ood_suite_family_holdout_goal/datasets/refs"
  "experiments/prepared_20260527/03_ood_suite_family_holdout_10_family/datasets/refs"
)

for refs in "${REFS_DIRS[@]}"; do
  split_name="$(basename "$(dirname "$(dirname "$refs")")")"
  log_file="$LOG_DIR/${split_name}.log"
  echo "=== FULL ${split_name} ===" | tee "$log_file"
  "$PYTHON_BIN" scripts/run_clean_temporal_nextgen_campaign_v2.py \
    --campaign-config "$CONFIG" \
    --refs-dir "$refs" \
    --output-dir "$OUTPUT_ROOT/$split_name" \
    --base-dir "." \
    --device cuda \
    --max-epochs "${NEXTGEN_MAX_EPOCHS:-120}" \
    --patience "${NEXTGEN_PATIENCE:-18}" \
    --batch-size "${NEXTGEN_BATCH_SIZE:-384}" \
    --seed 42 \
    --force 2>&1 | tee -a "$log_file"

  "$PYTHON_BIN" scripts/validate_nextgen_v2_campaign.py \
    --config "$CONFIG" \
    --output-root "$OUTPUT_ROOT" \
    --expected-splits "$refs" 2>&1 | tee -a "$log_file"
done

"$PYTHON_BIN" scripts/validate_nextgen_v2_campaign.py \
  --config "$CONFIG" \
  --output-root "$OUTPUT_ROOT" \
  --expected-splits "${REFS_DIRS[@]}"

echo "=== NEXTGEN V2 FULL ALL SPLITS COMPLETE ==="
