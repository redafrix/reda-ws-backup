#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/rootalkhatib/test/reda_ws"
cd "$ROOT"
source asynchvla_ws/scripts/activate_simvla_sam.sh
export REDA_WS="$ROOT"
mkdir -p asynchvla_ws/stage8_ultimate/reports

SPLITS=(id_task_split holdout_libero_object holdout_object_bowl holdout_libero_spatial)
VARIANTS=(action_only_baseline full_old_baseline context_gated_action seed_relative_rater seed_relative_pairwise per_step_error_head full_engineered_mlp full_engineered_simvla_focused seed_relative_simvla_focused)

{
  echo "# Stage 8 Model Sweep Results"
  echo
  echo "Generated on Sam."
  echo
} > asynchvla_ws/stage8_ultimate/reports/stage8_model_sweep_results.md

for split in "${SPLITS[@]}"; do
  echo "[stage8] architecture sweep split=$split"
  timeout 21600 python3 asynchvla_ws/src/rater_stage6/run_stage6_experiments.py \
    --split "$split" --variants "${VARIANTS[@]}" --epochs 120 --out-prefix "stage8_arch_${split}" || echo "[stage8] WARN arch sweep failed split=$split"
done

cp asynchvla_ws/outputs/reports/stage6/stage8_arch_*.md asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true
cp asynchvla_ws/outputs/reports/stage6/stage8_arch_*.json asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true

{
  echo "## Completed Splits"
  for split in "${SPLITS[@]}"; do echo "- \`$split\`"; done
  echo
  echo "## Reports"
  find asynchvla_ws/stage8_ultimate/reports -maxdepth 1 -type f -name "stage8_arch_*" -printf "- \`%f\`\n" | sort
} >> asynchvla_ws/stage8_ultimate/reports/stage8_model_sweep_results.md
