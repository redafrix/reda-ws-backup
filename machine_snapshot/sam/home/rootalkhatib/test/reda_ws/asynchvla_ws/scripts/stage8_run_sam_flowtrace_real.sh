#!/usr/bin/env bash
set -euo pipefail
ROOT="${REDA_WS:-/home/rootalkhatib/test/reda_ws}"
cd "$ROOT"
source asynchvla_ws/scripts/activate_simvla_sam.sh
export REDA_WS="$ROOT"
mkdir -p asynchvla_ws/stage8_ultimate/reports asynchvla_ws/stage8_ultimate/logs
SPLITS=(holdout_libero_object holdout_object_bowl holdout_libero_spatial)
VARIANTS=(context_gated_action_no_flow context_gated_action_plus_flow action_only_plus_flow seed_relative_plus_flow flow_only)
out=asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_real_results.md
{
  echo "# Stage 8 Flowtrace Real Results"
  echo
  echo "Generated: $(date -Is)"
  echo
  echo "This wrapper builds flowtrace trace/candidate datasets, then trains flowtrace variants. It exits nonzero if any split fails."
  echo
} > "$out"
for split in "${SPLITS[@]}"; do
  echo "[stage8] build flowtrace trace split=$split"
  timeout 21600 python3 asynchvla_ws/src/data_building/build_flowtrace_multiseed_dataset.py \
    --split-manifest "asynchvla_ws/data/splits/${split}.json" \
    --split-name "$split" \
    --max-contexts "${STAGE8_FLOW_MAX_TRAIN:-250}" \
    --max-calib "${STAGE8_FLOW_MAX_CALIB:-80}" \
    --max-test-id "${STAGE8_FLOW_MAX_TEST_ID:-80}" \
    --max-test-ood "${STAGE8_FLOW_MAX_TEST_OOD:-80}" \
    --cap-per-file "${STAGE8_FLOW_CAP_PER_FILE:-20}" \
    --steps "${STAGE8_FLOW_STEPS:-6}" \
    --simvla-seeds 0 1 2 3 4
  echo "[stage8] build flowtrace candidate split=$split"
  timeout 3600 python3 asynchvla_ws/src/data_building/build_flowtrace_candidate_dataset.py --split-name "$split"
  echo "[stage8] train flowtrace split=$split"
  timeout 21600 python3 asynchvla_ws/src/rater_stage7/run_stage7_flowtrace_experiments.py --split "$split" --variants "${VARIANTS[@]}" --epochs "${STAGE8_EPOCHS:-100}"
  cp "asynchvla_ws/outputs/reports/stage7/stage7_flowtrace_${split}.md" asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true
  cp "asynchvla_ws/outputs/reports/stage7/stage7_flowtrace_${split}.json" asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true
  echo "- completed $split" >> "$out"
done
{
  echo
  echo "## Reports"
  find asynchvla_ws/stage8_ultimate/reports -maxdepth 1 -type f -name "*flowtrace*" -printf "- \`%f\`\n" | sort
} >> "$out"
