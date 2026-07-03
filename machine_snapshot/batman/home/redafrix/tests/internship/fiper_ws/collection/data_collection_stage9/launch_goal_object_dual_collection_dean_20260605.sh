#!/usr/bin/env bash
set -euo pipefail

ROOT=/home/dean/fiper_goal_object_collection_20260605
SRC="$ROOT/src"
PYTHON=/home/redafrix/miniconda3/envs/simvla/bin/python
COLLECTOR="$SRC/collect_goal_object_dual_mode_dean_v1.py"
VALIDATOR="$SRC/validate_goal_object_dual_collection.py"
BUNDLE="$ROOT/libero_goal_object_reproduction_bundle_20260605"
EXACT_PLAN="$BUNDLE/verification/episode_identity_table.csv"
CONTINUOUS_PLAN="$ROOT/plans/libero_goal_object_continuous_plan_100000_seed2026060501.csv"
RUN_ROOT="$ROOT/runs/production_20260605"
EXACT_ROOT="$RUN_ROOT/exact_200"
CONTINUOUS_ROOT="$RUN_ROOT/continuous_100000"
REPORT_ROOT="$ROOT/reports/production_20260605"

mkdir -p "$EXACT_ROOT/receding/worker_0" "$EXACT_ROOT/chunk10/worker_0"
mkdir -p "$CONTINUOUS_ROOT/receding/worker_0" "$CONTINUOUS_ROOT/chunk10/worker_0"
mkdir -p "$RUN_ROOT/logs" "$REPORT_ROOT"

export CUDA_VISIBLE_DEVICES=0
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export USE_TF=0
export TRANSFORMERS_NO_TF=1
export USE_FLAX=0
export TOKENIZERS_PARALLELISM=false
export OMP_NUM_THREADS=4

COMMON=(
  --bundle-root "$BUNDLE"
  --worker-index 0
  --worker-count 1
  --max-timesteps 250
  --warmup 10
  --ace-candidates 8
  --action-horizon 10
  --model-denoise-steps 10
  --history-k 8
  --minimum-free-gb 12
  --resume
)

run_exact() {
  local mode=$1
  "$PYTHON" "$COLLECTOR" "${COMMON[@]}" \
    --phase exact \
    --execution-mode "$mode" \
    --episode-plan "$EXACT_PLAN" \
    --out-dir "$EXACT_ROOT/$mode/worker_0" \
    --save-images \
    --save-states \
    --full-json-queries \
    >>"$RUN_ROOT/logs/exact_${mode}.log" 2>&1
}

validate_exact() {
  local mode=$1
  "$PYTHON" "$VALIDATOR" \
    --plan "$EXACT_PLAN" \
    --run-root "$EXACT_ROOT/$mode" \
    --execution-mode "$mode" \
    --expected-episodes 200 \
    --report "$REPORT_ROOT/exact_${mode}_validation.json"
}

run_continuous() {
  local mode=$1
  "$PYTHON" "$COLLECTOR" "${COMMON[@]}" \
    --phase continuous \
    --execution-mode "$mode" \
    --episode-plan "$CONTINUOUS_PLAN" \
    --out-dir "$CONTINUOUS_ROOT/$mode/worker_0" \
    >>"$RUN_ROOT/logs/continuous_${mode}.log" 2>&1
}

printf '{"state":"launcher_started","timestamp":"%s","pid":%s}\n' "$(date --iso-8601=seconds)" "$$" >"$RUN_ROOT/launcher_status.json"

if [[ ! -f "$EXACT_ROOT/EXACT_200_VALIDATED_AND_PROTECTED.json" ]]; then
  run_exact receding &
  PID_EXACT_RECEDING=$!
  run_exact chunk10 &
  PID_EXACT_CHUNK=$!
  printf 'exact_receding_pid=%s\nexact_chunk10_pid=%s\n' "$PID_EXACT_RECEDING" "$PID_EXACT_CHUNK" >"$RUN_ROOT/current_pids.txt"
  wait "$PID_EXACT_RECEDING"
  wait "$PID_EXACT_CHUNK"

  validate_exact receding
  validate_exact chunk10
  "$PYTHON" -c "import json,pathlib,datetime; p=pathlib.Path('$EXACT_ROOT/EXACT_200_VALIDATED_AND_PROTECTED.json'); p.write_text(json.dumps({'state':'validated','episodes_per_mode':200,'validated_at':datetime.datetime.now().astimezone().isoformat(),'receding_report':'$REPORT_ROOT/exact_receding_validation.json','chunk10_report':'$REPORT_ROOT/exact_chunk10_validation.json'},indent=2)+'\n')"
  chmod -R a-w "$EXACT_ROOT/receding" "$EXACT_ROOT/chunk10"
fi

printf '{"state":"continuous_starting","timestamp":"%s","pid":%s}\n' "$(date --iso-8601=seconds)" "$$" >"$RUN_ROOT/launcher_status.json"
run_continuous receding &
PID_CONTINUOUS_RECEDING=$!
run_continuous chunk10 &
PID_CONTINUOUS_CHUNK=$!
printf 'continuous_receding_pid=%s\ncontinuous_chunk10_pid=%s\n' "$PID_CONTINUOUS_RECEDING" "$PID_CONTINUOUS_CHUNK" >"$RUN_ROOT/current_pids.txt"
wait "$PID_CONTINUOUS_RECEDING"
wait "$PID_CONTINUOUS_CHUNK"

printf '{"state":"continuous_completed","timestamp":"%s","pid":%s}\n' "$(date --iso-8601=seconds)" "$$" >"$RUN_ROOT/launcher_status.json"
