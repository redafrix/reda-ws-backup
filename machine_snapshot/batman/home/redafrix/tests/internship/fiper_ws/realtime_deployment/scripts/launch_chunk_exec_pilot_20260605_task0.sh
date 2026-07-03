#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
RUN_DIR="$ROOT/realtime_deployment/runs/chunk_exec_pilot_20260605_bob_task0"
mkdir -p "$RUN_DIR/logs"
STATUS="$RUN_DIR/sequential_status.jsonl"
: > "$STATUS"

cd "$ROOT"
source "../asynchvla_ws/scripts/activate_simvla_bob.sh"

export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export USE_TF=0
export TRANSFORMERS_NO_TF=1
export USE_FLAX=0
export TOKENIZERS_PARALLELISM=false
export PYTHONUNBUFFERED=1
export NVIDIA_TF32_OVERRIDE=0
export CUBLAS_WORKSPACE_CONFIG=:4096:8

if pgrep -af "run_.*_simvla_chunk_exec_.*.py" | grep -v grep | grep -v "$$" >/dev/null; then
  echo "conflicting realtime runner already active" >&2
  pgrep -af "run_.*_simvla_chunk_exec_.*.py" >&2
  exit 2
fi

# 01_baseline
printf '{"time":"%s","stage":"01_baseline","event":"start"}\n' "$(date -Is)" >> "$STATUS"
set +e
python3 "$ROOT/realtime_deployment/scripts/run_baseline_simvla_chunk_exec_v2.py" \
  --config "$ROOT/realtime_deployment/configs/chunk_exec_pilot_20260605_bob_task0_baseline.json" \
  --worker-id bob_baseline \
  --num-episodes 10 > "$RUN_DIR/logs/01_baseline.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"01_baseline","event":"end","code":%s}\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi

# 02_risk_topk8
printf '{"time":"%s","stage":"02_risk_topk8","event":"start"}\n' "$(date -Is)" >> "$STATUS"
set +e
python3 "$ROOT/realtime_deployment/scripts/run_riskaware_simvla_chunk_exec_topk8_v2_chunk.py" \
  --config "$ROOT/realtime_deployment/configs/chunk_exec_pilot_20260605_bob_task0_risk_topk8.json" \
  --policy risk_unc_topk8 \
  --num-episodes 10 > "$RUN_DIR/logs/02_risk_topk8.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"02_risk_topk8","event":"end","code":%s}\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi

printf '{"time":"%s","event":"all_done"}\n' "$(date -Is)" >> "$STATUS"
