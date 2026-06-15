#!/usr/bin/env bash
set -euo pipefail
source "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"
export TOKENIZERS_PARALLELISM=false
export USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl PYTHONUNBUFFERED=1
export NVIDIA_TF32_OVERRIDE=0 CUBLAS_WORKSPACE_CONFIG=:4096:8
RUN_DIR="/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_bob_task7"
mkdir -p "$RUN_DIR/logs"
STATUS="$RUN_DIR/sequential_status.jsonl"
: > "$STATUS"
if pgrep -af 'run_dean_uncertainty_realtime_policy_v1.py' | grep -v grep | grep -v "$$" >/dev/null; then
  echo 'conflicting realtime runner already active' >&2
  pgrep -af 'run_dean_uncertainty_realtime_policy_v1.py' >&2
  exit 2
fi
printf '{"time":"%s","stage":"01_modified_simvla","event":"start"}\n' "$(date -Is)" >> "$STATUS"
set +e
"/usr/bin/python3" "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py" --config "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_bob_task7_01_modified_simvla.json" --policy simvla_only --num-episodes 12 > "$RUN_DIR/logs/01_modified_simvla.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"01_modified_simvla","event":"end","code":%s}\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi
printf '{"time":"%s","stage":"02_topk8_protective","event":"start"}\n' "$(date -Is)" >> "$STATUS"
set +e
"/usr/bin/python3" "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py" --config "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_bob_task7_02_topk8_protective.json" --policy risk_unc_topk8 --num-episodes 12 > "$RUN_DIR/logs/02_topk8_protective.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"02_topk8_protective","event":"end","code":%s}\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi
printf '{"time":"%s","stage":"03_topk8_balanced","event":"start"}\n' "$(date -Is)" >> "$STATUS"
set +e
"/usr/bin/python3" "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py" --config "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_bob_task7_03_topk8_balanced.json" --policy risk_unc_topk8 --num-episodes 12 > "$RUN_DIR/logs/03_topk8_balanced.log" 2>&1
code=$?
set -e
printf '{"time":"%s","stage":"03_topk8_balanced","event":"end","code":%s}\n' "$(date -Is)" "$code" >> "$STATUS"
if [[ "$code" -ne 0 ]]; then exit "$code"; fi
printf '{"time":"%s","event":"all_done"}\n' "$(date -Is)" >> "$STATUS"
