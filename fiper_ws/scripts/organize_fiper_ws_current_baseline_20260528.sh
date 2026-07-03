#!/usr/bin/env bash
# Script to organize fiper_ws around the current baseline v2_018_transformer_k16.
set -euo pipefail

BASE_DIR="/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
cd "$BASE_DIR"

SRC_DIR="experiments/clean_temporal_nextgen_v2_full_all_20260527"
DST_DIR="experiments/current_baseline_v2_018_20260528"

echo "Creating curated directory..."
mkdir -p "$DST_DIR"

sub_experiments=(
  "00_global_main"
  "01_ood_task_8_9"
  "02_ood_perturbation_holdout_milk"
  "02_ood_perturbation_holdout_mug"
  "02_ood_perturbation_holdout_object"
  "fold_00_holdout_alphabet_soup_bbq_sauce"
  "fold_01_holdout_butter_chocolate_pudding"
  "fold_02_holdout_cream_cheese_ketchup"
  "fold_03_holdout_milk_orange_juice"
  "fold_04_holdout_salad_dressing_tomato_sauce"
)

for subexp in "${sub_experiments[@]}"; do
  echo "Copying curated job for $subexp..."
  mkdir -p "$DST_DIR/$subexp/jobs/v2_018_transformer_k16"
  
  # Copy metadata files if they exist
  for f in campaign_summary.csv campaign_summary.json CAMPAIGN_TOPLINE_REPORT.md campaign_config.json; do
    if [ -f "$SRC_DIR/$subexp/$f" ]; then
      cp "$SRC_DIR/$subexp/$f" "$DST_DIR/$subexp/$f"
    fi
  done
  
  # Copy job files
  if [ -d "$SRC_DIR/$subexp/jobs/v2_018_transformer_k16" ]; then
    cp -r "$SRC_DIR/$subexp/jobs/v2_018_transformer_k16/." "$DST_DIR/$subexp/jobs/v2_018_transformer_k16/"
  else
    echo "Warning: Job v2_018_transformer_k16 not found in $subexp!"
  fi
done

# Copy global validation report
if [ -f "$SRC_DIR/NEXTGEN_V2_VALIDATION_REPORT.md" ]; then
  cp "$SRC_DIR/NEXTGEN_V2_VALIDATION_REPORT.md" "$DST_DIR/NEXTGEN_V2_VALIDATION_REPORT.md"
fi

echo "Curated baseline folder created successfully."

# Step 5: Archive the old 44-job tree
echo "Archiving legacy experiments..."
mkdir -p archive/legacy_experiments_20260528
mv "$SRC_DIR" archive/legacy_experiments_20260528/clean_temporal_nextgen_v2_full_all_20260527

echo "Done organizing fiper_ws."
