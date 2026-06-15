#!/bin/bash
set -e

# Source env
source /home/rootalkhatib/test/reda_ws/asynchvla_ws/scripts/activate_simvla_sam.sh
cd /home/rootalkhatib/test/reda_ws/fiper_ws

campaign_config="configs/clean_temporal_41_44_campaign_v2.json"
device="cuda"
max_jobs=5
batch_size=256

# Array of split names and their refs directories
declare -A campaigns

# Target-object folds
campaigns["target_object_fold00"]="experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs"
campaigns["target_object_fold01"]="experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_01_holdout_butter_chocolate_pudding/datasets/refs"
campaigns["target_object_fold02"]="experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_02_holdout_cream_cheese_ketchup/datasets/refs"
campaigns["target_object_fold03"]="experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_03_holdout_milk_orange_juice/datasets/refs"
campaigns["target_object_fold04"]="experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_04_holdout_salad_dressing_tomato_sauce/datasets/refs"

# Global main
campaigns["global_main"]="experiments/prepared_20260527/00_global_main/datasets/refs"

# OOD task
campaigns["ood_task_8_9"]="experiments/prepared_20260527/01_ood_task_8_9/datasets/refs"

# OOD Perturbations
campaigns["ood_perturbation_mug"]="experiments/prepared_20260527/02_ood_perturbation_holdout_mug/datasets/refs"
campaigns["ood_perturbation_milk"]="experiments/prepared_20260527/02_ood_perturbation_holdout_milk/datasets/refs"
campaigns["ood_perturbation_object"]="experiments/prepared_20260527/02_ood_perturbation_holdout_object/datasets/refs"
campaigns["ood_perturbation_env"]="experiments/prepared_20260527/02_ood_perturbation_holdout_env/datasets/refs"

# OOD Families
campaigns["ood_family_spatial"]="experiments/prepared_20260527/03_ood_suite_family_holdout_spatial/datasets/refs"
campaigns["ood_family_object_family"]="experiments/prepared_20260527/03_ood_suite_family_holdout_object_family/datasets/refs"
campaigns["ood_family_goal"]="experiments/prepared_20260527/03_ood_suite_family_holdout_goal/datasets/refs"
campaigns["ood_family_10_family"]="experiments/prepared_20260527/03_ood_suite_family_holdout_10_family/datasets/refs"

# List of keys in ordered execution sequence (folds first, then global, then other splits)
ordered_keys=(
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

# Iterate and run each campaign
for name in "${ordered_keys[@]}"; do
    refs_dir="${campaigns[$name]}"
    output_dir="experiments/clean_temporal_41_44_${name}_20260527"
    echo "=========================================================="
    echo "LAUNCHING CAMPAIGN: $name"
    echo "Refs: $refs_dir"
    echo "Output: $output_dir"
    echo "=========================================================="
    
    python3 scripts/run_clean_temporal_risk_campaign_v2.py \
      --campaign-config "$campaign_config" \
      --refs-dir "$refs_dir" \
      --output-dir "$output_dir" \
      --device "$device" \
      --max-jobs "$max_jobs" \
      --batch-size "$batch_size"
done

echo "All campaigns finished!"
