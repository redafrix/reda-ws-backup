#!/usr/bin/env bash
set -euo pipefail

ROOT=/home/dean/fiper_goal_object_collection_20260605
PYTHON=/home/redafrix/miniconda3/envs/simvla/bin/python
SCRIPT="$ROOT/src/collect_goal_object_dual_mode_dean_v1.py"
BUNDLE="$ROOT/libero_goal_object_reproduction_bundle_20260605"
PLAN="$BUNDLE/verification/episode_identity_table.csv"
RUN_ROOT="$ROOT/runs/parallel_benchmark"

if [[ -e "$RUN_ROOT" ]]; then
  mv "$RUN_ROOT" "${RUN_ROOT}_archive_$(date +%Y%m%d_%H%M%S)"
fi
mkdir -p "$RUN_ROOT/receding" "$RUN_ROOT/chunk10"

COMMON=(
  --phase exact
  --bundle-root "$BUNDLE"
  --episode-plan "$PLAN"
  --stop-after-episodes 1
  --minimum-free-gb 10
)

export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export USE_TF=0
export TRANSFORMERS_NO_TF=1
export USE_FLAX=0

"$PYTHON" "$SCRIPT" "${COMMON[@]}" \
  --execution-mode receding \
  --max-timesteps 100 \
  --out-dir "$RUN_ROOT/receding" \
  >"$RUN_ROOT/receding.log" 2>&1 &
PID_RECEDING=$!

"$PYTHON" "$SCRIPT" "${COMMON[@]}" \
  --execution-mode chunk10 \
  --max-timesteps 250 \
  --out-dir "$RUN_ROOT/chunk10" \
  >"$RUN_ROOT/chunk10.log" 2>&1 &
PID_CHUNK=$!

printf 'receding_pid=%s\nchunk10_pid=%s\n' "$PID_RECEDING" "$PID_CHUNK" >"$RUN_ROOT/pids.txt"
wait "$PID_RECEDING"
wait "$PID_CHUNK"
