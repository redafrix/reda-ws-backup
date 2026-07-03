#!/usr/bin/env bash
set -euo pipefail
source "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"
export TOKENIZERS_PARALLELISM=false
export USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl PYTHONUNBUFFERED=1
export NVIDIA_TF32_OVERRIDE=0 CUBLAS_WORKSPACE_CONFIG=:4096:8

RUN_DIR="/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/tuned_topk8_pilot_20260605_bob_task7"
mkdir -p "$RUN_DIR/logs"
STATUS="$RUN_DIR/sequential_status.jsonl"
: > "$STATUS"

# Stage 04_topk8_moderate_active
printf '{"time":"%s","stage":"04_topk8_moderate_active","event":"start"}\n' "$(date -Is)" >> "$STATUS"
set +e
"/usr/bin/python3" "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py" \
  --config "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/configs/tuned_topk8_pilot_20260605_bob_task7_04_topk8_moderate_active.json" \
  --policy risk_unc_topk8 --num-episodes 12 > "$RUN_DIR/logs/04_topk8_moderate_active.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"04_topk8_moderate_active","event":"end","code":%s}\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi

# Stage 05_topk8_highly_active
printf '{"time":"%s","stage":"05_topk8_highly_active","event":"start"}\n' "$(date -Is)" >> "$STATUS"
set +e
"/usr/bin/python3" "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py" \
  --config "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/configs/tuned_topk8_pilot_20260605_bob_task7_05_topk8_highly_active.json" \
  --policy risk_unc_topk8 --num-episodes 12 > "$RUN_DIR/logs/05_topk8_highly_active.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"05_topk8_highly_active","event":"end","code":%s}\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi

printf '{"time":"%s","event":"all_done"}\n' "$(date -Is)" >> "$STATUS"
