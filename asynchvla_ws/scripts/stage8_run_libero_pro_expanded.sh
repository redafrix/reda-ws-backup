#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws"
cd "$ROOT"
source "asynchvla_ws/scripts/activate_simvla_bob.sh"
export PYTHONPATH="$ROOT/intern_ship_ws/assets/repos/LIBERO-PRO:${PYTHONPATH:-}"
export LIBERO_CONFIG_PATH="$ROOT/asynchvla_ws/configs/libero_pro_bob"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl

EPISODES="${STAGE8_EPISODES:-5}"
OUT_DIR="asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_${EPISODES}eps"
mkdir -p "$OUT_DIR"

# Use suites that have local pruned init states. Avoid libero_object_env,
# which failed in the pilot because init files were missing.
SUITES=(
  "libero_object_with_mug"
  "libero_object_with_red_box"
  "libero_object_with_blue_stick"
  "libero_object_temp_x0.1"
  "libero_object_temp_x0.3"
  "libero_spatial_with_mug"
  "libero_spatial_with_red_box"
  "libero_goal_with_mug"
  "libero_goal_with_red_box"
  "libero_10_with_mug"
)
TASKS=(0 1 2 3 4)
MODES=(A_passive B_deliberation C_random_seed D_low_uncertainty_reject_log)

for suite in "${SUITES[@]}"; do
  for task in "${TASKS[@]}"; do
    out="$OUT_DIR/${suite}_task${task}.json"
    if [ -s "$out" ]; then
      echo "[stage8] skip existing $out"
      continue
    fi
    echo "[stage8] LIBERO-PRO expanded episodes=$EPISODES suite=$suite task=$task out=$out"
    timeout 14400 python3 asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py \
      --task-suite "$suite" \
      --task-id "$task" \
      --num-episodes "$EPISODES" \
      --max-steps 600 \
      --modes "${MODES[@]}" \
      --resolution 128 \
      --unc-threshold 1.75 \
      --out "$out" || echo "[stage8] WARN failed suite=$suite task=$task"
  done
done

python3 asynchvla_ws/scripts/stage8_summarize_rollouts.py \
  --input-dir "$OUT_DIR" \
  --out-md asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_expanded_rollout_results.md \
  --title "Stage 8 LIBERO-PRO Expanded Rollout Results (${EPISODES} episodes/task)"
