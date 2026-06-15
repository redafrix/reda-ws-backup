#!/usr/bin/env bash
set -euo pipefail

export TOKENIZERS_PARALLELISM=false
export USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl PYTHONUNBUFFERED=1
export NVIDIA_TF32_OVERRIDE=0 CUBLAS_WORKSPACE_CONFIG=:4096:8

RUN_DIR="/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/tuned_topk8_pilot_20260605_dean_task8"
mkdir -p "$RUN_DIR/logs"
STATUS="$RUN_DIR/sequential_status.jsonl"
: > "$STATUS"

if pgrep -af 'run_dean_uncertainty_realtime_policy_v1.py' | grep -v grep | grep -v "$$" >/dev/null; then
  echo 'conflicting realtime runner already active' >&2
  pgrep -af 'run_dean_uncertainty_realtime_policy_v1.py' >&2
  exit 2
fi

# Stage 04_topk8_moderate
printf '{"time":"%s","stage":"04_topk8_moderate","event":"start"}\n' "$(date -Is)" >> "$STATUS"
set +e
"/home/redafrix/miniconda3/envs/simvla/bin/python" "/home/dean/fiper_uncertainty_collection/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py" \
  --config "/home/dean/fiper_uncertainty_collection/realtime_deployment/configs/tuned_topk8_pilot_20260605_dean_task8_04_topk8_moderate.json" \
  --policy risk_unc_topk8 --num-episodes 12 > "$RUN_DIR/logs/04_topk8_moderate.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"04_topk8_moderate","event":"end","code":%s}\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi

# Stage 05_topk8_active
printf '{"time":"%s","stage":"05_topk8_active","event":"start"}\n' "$(date -Is)" >> "$STATUS"
set +e
"/home/redafrix/miniconda3/envs/simvla/bin/python" "/home/dean/fiper_uncertainty_collection/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py" \
  --config "/home/dean/fiper_uncertainty_collection/realtime_deployment/configs/tuned_topk8_pilot_20260605_dean_task8_05_topk8_active.json" \
  --policy risk_unc_topk8 --num-episodes 12 > "$RUN_DIR/logs/05_topk8_active.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"05_topk8_active","event":"end","code":%s}\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi

printf '{"time":"%s","event":"all_done"}\n' "$(date -Is)" >> "$STATUS"
