#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/rootalkhatib/test/reda_ws"
cd "$ROOT"
source asynchvla_ws/scripts/activate_simvla_sam.sh
export REDA_WS="$ROOT"
mkdir -p asynchvla_ws/stage8_ultimate/reports

SPLITS=(holdout_libero_object holdout_object_bowl holdout_libero_spatial)
VARIANTS=(context_gated_action context_gated_flowtrace action_only_flowtrace seed_relative_flowtrace flowtrace_only)

{
  echo "# Stage 8 Flowtrace Results"
  echo
  echo "Generated on Sam."
  echo
} > asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_results.md

for split in "${SPLITS[@]}"; do
  echo "[stage8] flowtrace experiments split=$split"
  timeout 14400 python3 asynchvla_ws/src/rater_stage7/run_stage7_flowtrace_experiments.py \
    --split "$split" \
    --variants "${VARIANTS[@]}" \
    --epochs 80 || echo "[stage8] WARN flowtrace failed split=$split"
done

find asynchvla_ws/outputs/reports/stage7 -maxdepth 1 -type f \( -name "*flowtrace*.md" -o -name "*flowtrace*.json" \) -exec cp {} asynchvla_ws/stage8_ultimate/reports/ \; 2>/dev/null || true

{
  echo "## Completed Splits"
  for split in "${SPLITS[@]}"; do echo "- \`$split\`"; done
  echo
  echo "## Stage 7/8 Flowtrace Reports"
  find asynchvla_ws/stage8_ultimate/reports -maxdepth 1 -type f -name "*flowtrace*" -printf "- \`%f\`\n" | sort
} >> asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_results.md
