#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/rootalkhatib/test/reda_ws"
cd "$ROOT"
source asynchvla_ws/scripts/activate_simvla_sam.sh
export REDA_WS="$ROOT"
mkdir -p asynchvla_ws/stage8_ultimate/reports

SPLITS=(holdout_libero_object holdout_object_bowl holdout_libero_spatial)
TARGETS=(single_l2 min_k5 min_k10 min_k20 softmin pairwise_rank bad_top30)
VARIANTS=(context_gated_action seed_relative_pairwise per_step_error_head)

{
  echo "# Stage 8 Target Comparison"
  echo
  echo "Generated on Sam."
  echo
} > asynchvla_ws/stage8_ultimate/reports/stage8_target_comparison.md

for split in "${SPLITS[@]}"; do
  echo "[stage8] building multi-expert targets split=$split"
  timeout 7200 python3 asynchvla_ws/src/data_building/build_multi_expert_min_distance_targets.py \
    --split-name "$split" --parts train calib test_id test_ood --pool-mode train_only_same_task || true
  echo "[stage8] target experiments split=$split"
  timeout 14400 python3 asynchvla_ws/src/rater_stage7/run_stage7_multi_expert_target_experiments.py \
    --split "$split" --targets "${TARGETS[@]}" --variants "${VARIANTS[@]}" --epochs 80 || echo "[stage8] WARN target failed split=$split"
done

find asynchvla_ws/outputs/reports/stage7 -maxdepth 1 -type f \( -name "*target*.md" -o -name "*target*.json" -o -name "*multi_expert*.md" -o -name "*multi_expert*.json" \) -exec cp {} asynchvla_ws/stage8_ultimate/reports/ \; 2>/dev/null || true

{
  echo "## Completed Splits"
  for split in "${SPLITS[@]}"; do echo "- \`$split\`"; done
  echo
  echo "## Reports"
  find asynchvla_ws/stage8_ultimate/reports -maxdepth 1 -type f \( -name "*target*" -o -name "*multi_expert*" \) -printf "- \`%f\`\n" | sort
  echo
  echo "Progress/success targets are deferred until rollout logs are available."
} >> asynchvla_ws/stage8_ultimate/reports/stage8_target_comparison.md
