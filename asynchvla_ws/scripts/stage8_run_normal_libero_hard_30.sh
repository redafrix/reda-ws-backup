#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws"
cd "$ROOT"
source "asynchvla_ws/scripts/activate_simvla_bob.sh"
export LIBERO_CONFIG_PATH="$ROOT/asynchvla_ws/configs/libero_bob"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl

EPISODES="${STAGE8_EPISODES:-30}"
OUT_DIR="asynchvla_ws/stage8_ultimate/results/normal_libero_hard_${EPISODES}eps"
mkdir -p "$OUT_DIR"

TASKS=(
  "libero_spatial 5"
  "libero_goal 0"
  "libero_goal 9"
  "libero_goal 2"
  "libero_10 0"
  "libero_10 1"
  "libero_object 0"
)
MODES=(A_passive B_deliberation C_random_seed D_low_uncertainty_reject_log)

for spec in "${TASKS[@]}"; do
  suite="${spec% *}"
  task="${spec#* }"
  out="$OUT_DIR/${suite}_task${task}.json"
  if [ -s "$out" ]; then
    echo "[stage8] skip existing $out"
    continue
  fi
  echo "[stage8] normal LIBERO hard episodes=$EPISODES suite=$suite task=$task out=$out"
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

python3 asynchvla_ws/scripts/stage8_summarize_rollouts.py \
  --input-dir "$OUT_DIR" \
  --out-md asynchvla_ws/stage8_ultimate/reports/stage8_normal_libero_hard_task_results.md \
  --title "Stage 8 Normal LIBERO Hard-Task Results (${EPISODES} episodes/task)"
