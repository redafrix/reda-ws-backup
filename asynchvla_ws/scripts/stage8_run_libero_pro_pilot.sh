#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws"
cd "$ROOT"
source "asynchvla_ws/scripts/activate_simvla_bob.sh"
export PYTHONPATH="$ROOT/intern_ship_ws/assets/repos/LIBERO-PRO:${PYTHONPATH:-}"
export LIBERO_CONFIG_PATH="$ROOT/asynchvla_ws/configs/libero_pro_bob"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl

OUT_DIR="asynchvla_ws/stage8_ultimate/results/libero_pro_pilot"
mkdir -p "$OUT_DIR"

SUITES=(
  "libero_object_with_mug"
  "libero_goal_lan"
  "libero_goal_object"
  "libero_object_env"
)
TASKS=(0 1 2)
MODES=(A_passive B_deliberation C_random_seed D_low_uncertainty_reject_log E_conservative_switch_proxy)

for suite in "${SUITES[@]}"; do
  for task in "${TASKS[@]}"; do
    out="$OUT_DIR/${suite}_task${task}.json"
    echo "[stage8] LIBERO-PRO pilot suite=$suite task=$task out=$out"
    timeout 7200 python3 asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py \
      --task-suite "$suite" \
      --task-id "$task" \
      --num-episodes 5 \
      --max-steps 600 \
      --modes "${MODES[@]}" \
      --resolution 128 \
      --unc-threshold 1.75 \
      --out "$out" || echo "[stage8] WARN failed suite=$suite task=$task"
  done
done

python3 asynchvla_ws/scripts/stage8_summarize_rollouts.py \
  --input-dir "$OUT_DIR" \
  --out-md asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_pilot_results.md \
  --title "Stage 8 LIBERO-PRO Pilot Results"
