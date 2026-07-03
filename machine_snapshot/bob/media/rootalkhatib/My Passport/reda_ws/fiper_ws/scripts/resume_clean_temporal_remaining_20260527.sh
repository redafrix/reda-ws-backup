#!/bin/bash
set -u

WORKSPACE="/home/rootalkhatib/test/reda_ws/fiper_ws"
ENV_SCRIPT="/home/rootalkhatib/test/reda_ws/asynchvla_ws/scripts/activate_simvla_sam.sh"
CAMPAIGN_CONFIG="configs/clean_temporal_41_44_campaign_v2.json"
DEVICE="cuda"
MAX_JOBS=5
BATCH_SIZE=256
MAIN_SWEEP_PID="${1:-}"

cd "$WORKSPACE" || exit 1
mkdir -p logs

echo "=== resume_clean_temporal_remaining_20260527 started: $(date -Is) ==="
if [[ -n "$MAIN_SWEEP_PID" ]]; then
  echo "Waiting for main sweep PID ${MAIN_SWEEP_PID} to exit before resuming missing campaigns."
  while kill -0 "$MAIN_SWEEP_PID" 2>/dev/null; do
    sleep 60
  done
  echo "Main sweep PID ${MAIN_SWEEP_PID} is no longer running: $(date -Is)"
else
  echo "No main sweep PID supplied; checking missing campaigns immediately."
fi

source "$ENV_SCRIPT"

declare -A CAMPAIGNS
CAMPAIGNS["target_object_fold00"]="experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs"
CAMPAIGNS["target_object_fold01"]="experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_01_holdout_butter_chocolate_pudding/datasets/refs"
CAMPAIGNS["target_object_fold02"]="experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_02_holdout_cream_cheese_ketchup/datasets/refs"
CAMPAIGNS["target_object_fold03"]="experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_03_holdout_milk_orange_juice/datasets/refs"
CAMPAIGNS["target_object_fold04"]="experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_04_holdout_salad_dressing_tomato_sauce/datasets/refs"
CAMPAIGNS["global_main"]="experiments/prepared_20260527/00_global_main/datasets/refs"
CAMPAIGNS["ood_task_8_9"]="experiments/prepared_20260527/01_ood_task_8_9/datasets/refs"
CAMPAIGNS["ood_perturbation_mug"]="experiments/prepared_20260527/02_ood_perturbation_holdout_mug/datasets/refs"
CAMPAIGNS["ood_perturbation_milk"]="experiments/prepared_20260527/02_ood_perturbation_holdout_milk/datasets/refs"
CAMPAIGNS["ood_perturbation_object"]="experiments/prepared_20260527/02_ood_perturbation_holdout_object/datasets/refs"
CAMPAIGNS["ood_perturbation_env"]="experiments/prepared_20260527/02_ood_perturbation_holdout_env/datasets/refs"
CAMPAIGNS["ood_family_spatial"]="experiments/prepared_20260527/03_ood_suite_family_holdout_spatial/datasets/refs"
CAMPAIGNS["ood_family_object_family"]="experiments/prepared_20260527/03_ood_suite_family_holdout_object_family/datasets/refs"
CAMPAIGNS["ood_family_goal"]="experiments/prepared_20260527/03_ood_suite_family_holdout_goal/datasets/refs"
CAMPAIGNS["ood_family_10_family"]="experiments/prepared_20260527/03_ood_suite_family_holdout_10_family/datasets/refs"

ORDERED_KEYS=(
  "target_object_fold00"
  "target_object_fold01"
  "target_object_fold02"
  "target_object_fold03"
  "target_object_fold04"
  "global_main"
  "ood_task_8_9"
  "ood_perturbation_mug"
  "ood_perturbation_milk"
  "ood_perturbation_object"
  "ood_perturbation_env"
  "ood_family_spatial"
  "ood_family_object_family"
  "ood_family_goal"
  "ood_family_10_family"
)

for name in "${ORDERED_KEYS[@]}"; do
  refs_dir="${CAMPAIGNS[$name]}"
  output_dir="experiments/clean_temporal_41_44_${name}_20260527"
  completed=$(find "$output_dir/jobs" -mindepth 2 -maxdepth 2 -name summary.json 2>/dev/null | wc -l)
  echo "Campaign ${name}: completed summaries ${completed}/${MAX_JOBS}"
  if [[ "$completed" -ge "$MAX_JOBS" ]]; then
    echo "Skipping ${name}; already complete."
    continue
  fi
  echo "Resuming ${name}: $(date -Is)"
  python3 scripts/run_clean_temporal_risk_campaign_v2.py \
    --campaign-config "$CAMPAIGN_CONFIG" \
    --refs-dir "$refs_dir" \
    --output-dir "$output_dir" \
    --device "$DEVICE" \
    --max-jobs "$MAX_JOBS" \
    --batch-size "$BATCH_SIZE"
  status=$?
  echo "Campaign ${name} exit status: ${status}"
done

echo "Refreshing final summaries: $(date -Is)"
python3 scripts/summarize_clean_temporal_41_44_campaign_v2.py
python3 scripts/analyze_clean_temporal_partial_results_v1.py
echo "=== resume_clean_temporal_remaining_20260527 finished: $(date -Is) ==="
