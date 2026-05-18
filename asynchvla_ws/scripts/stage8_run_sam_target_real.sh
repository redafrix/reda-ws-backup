#!/usr/bin/env bash
set -euo pipefail
ROOT="${REDA_WS:-/home/rootalkhatib/test/reda_ws}"
cd "$ROOT"
source asynchvla_ws/scripts/activate_simvla_sam.sh
export REDA_WS="$ROOT"
mkdir -p asynchvla_ws/stage8_ultimate/reports
SPLITS=(holdout_libero_object holdout_object_bowl holdout_libero_spatial holdout_libero_goal holdout_object_cabinet holdout_scene_kitchen_scene2)
TARGETS=(target_chunk_l2_single_expert target_chunk_min_l2_K5 target_chunk_min_l2_K10 target_chunk_min_l2_K20 target_chunk_softmin_l2_K10 target_chunk_mean_top3_l2_K10)
VARIANTS=(action_only_baseline context_gated_action seed_relative_pairwise per_step_error_head)
out=asynchvla_ws/stage8_ultimate/reports/stage8_target_sweep_real_results.md
{
  echo "# Stage 8 Target Sweep Real Results"
  echo
  echo "Generated: $(date -Is)"
  echo
  echo "Multi-expert targets are built using train-only same-task pools unless unavailable; wrappers exit nonzero on failures."
  echo
} > "$out"
for split in "${SPLITS[@]}"; do
  if [ ! -d "asynchvla_ws/data/processed_stage5/$split" ]; then
    echo "- skipped missing split $split" >> "$out"
    continue
  fi
  echo "[stage8] build targets split=$split"
  timeout 10800 python3 asynchvla_ws/src/data_building/build_multi_expert_min_distance_targets.py --split-name "$split" --parts train calib test_id test_ood --pool-mode train_only_same_task
  echo "[stage8] target experiments split=$split"
  timeout 21600 python3 asynchvla_ws/src/rater_stage7/run_stage7_multi_expert_target_experiments.py --split "$split" --targets "${TARGETS[@]}" --variants "${VARIANTS[@]}" --epochs "${STAGE8_EPOCHS:-80}"
  cp asynchvla_ws/outputs/reports/stage7/stage7_multi_expert_target_${split}.* asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true
  echo "- completed $split" >> "$out"
done
{
  echo
  echo "## Reports"
  find asynchvla_ws/stage8_ultimate/reports -maxdepth 1 -type f \( -name "*target*" -o -name "*multi_expert*" \) -printf "- \`%f\`\n" | sort
} >> "$out"
