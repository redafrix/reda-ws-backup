#!/usr/bin/env bash
set -euo pipefail
ROOT="${REDA_WS:-/home/rootalkhatib/test/reda_ws}"
cd "$ROOT"
source asynchvla_ws/scripts/activate_simvla_sam.sh
export REDA_WS="$ROOT"
mkdir -p asynchvla_ws/stage8_ultimate/reports
SPLITS=(id_task_split holdout_libero_object holdout_object_bowl holdout_libero_spatial holdout_libero_goal holdout_object_cabinet holdout_scene_kitchen_scene2)
VARIANTS=(action_only_baseline full_old_baseline context_gated_action seed_relative_rater seed_relative_pairwise per_step_error_head full_engineered_mlp full_engineered_simvla_focused seed_relative_simvla_focused heteroscedastic_head heteroscedastic_simvla_focused)
out=asynchvla_ws/stage8_ultimate/reports/stage8_architecture_loss_big_sweep_results.md
{
  echo "# Stage 8 Architecture/Loss Big Sweep Results"
  echo
  echo "Generated: $(date -Is)"
  echo
  echo "Variants: ${VARIANTS[*]}"
  echo
} > "$out"
for split in "${SPLITS[@]}"; do
  if [ ! -d "asynchvla_ws/data/processed_stage5/$split" ]; then echo "- skipped missing $split" >> "$out"; continue; fi
  echo "[stage8] arch big split=$split"
  timeout 28800 python3 asynchvla_ws/src/rater_stage6/run_stage6_experiments.py --split "$split" --variants "${VARIANTS[@]}" --epochs "${STAGE8_EPOCHS:-160}" --out-prefix "stage8_big_arch_${split}"
  cp asynchvla_ws/outputs/reports/stage6/stage8_big_arch_${split}.* asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true
  echo "- completed $split" >> "$out"
done
{
  echo
  echo "## Quantile heads"
  timeout 28800 python3 asynchvla_ws/src/rater_stage8/run_stage8_quantile_heads.py --splits holdout_libero_object holdout_object_bowl holdout_libero_spatial holdout_libero_goal --epochs "${STAGE8_QUANTILE_EPOCHS:-120}"
  echo
  echo "## Reports"
  find asynchvla_ws/stage8_ultimate/reports -maxdepth 1 -type f \( -name "stage8_big_arch_*" -o -name "stage8_quantile*" \) -printf "- \`%f\`\n" | sort
} >> "$out"
