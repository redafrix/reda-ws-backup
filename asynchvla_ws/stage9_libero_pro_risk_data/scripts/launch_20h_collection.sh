#!/usr/bin/env bash
set -euo pipefail

ROLE="${1:-}"
if [[ -z "$ROLE" ]]; then
  host="$(hostname)"
  case "$host" in
    *05*|*sam*) ROLE="sam" ;;
    *) ROLE="bob" ;;
  esac
fi
MODE="${2:-${STAGE9_MODE:-collect}}"

if [[ "$ROLE" == "sam" ]]; then
  export REDA_WS="${REDA_WS:-/home/rootalkhatib/test/reda_ws}"
  cd "$REDA_WS"
  source "asynchvla_ws/scripts/activate_simvla_sam.sh"
  export PYTHONPATH="$REDA_WS/asynchvla_ws/src:$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified:$REDA_WS/intern_ship_ws/assets/repos/LIBERO-PRO:${PYTHONPATH:-}"
  export LIBERO_CONFIG_PATH="$REDA_WS/asynchvla_ws/temp_config"
else
  export REDA_WS="${REDA_WS:-/media/rootalkhatib/My Passport/reda_ws}"
  cd "$REDA_WS"
  source "asynchvla_ws/scripts/activate_simvla_bob.sh"
  export PYTHONPATH="$REDA_WS/asynchvla_ws/src:$REDA_WS/intern_ship_ws/assets/repos/LIBERO-PRO:${PYTHONPATH:-}"
  export LIBERO_CONFIG_PATH="$REDA_WS/asynchvla_ws/temp_config"
fi

export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
export OMP_NUM_THREADS="${OMP_NUM_THREADS:-8}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-8}"
export PYTHONUNBUFFERED=1

mkdir -p "asynchvla_ws/stage9_libero_pro_risk_data/logs"
log="asynchvla_ws/stage9_libero_pro_risk_data/logs/stage9_20h_watchdog_${ROLE}_$(date +%Y%m%d_%H%M%S).log"

extra=()
if [[ "$ROLE" == "sam" ]]; then
  extra+=(--enable-training)
fi

nohup python3 -u "asynchvla_ws/stage9_libero_pro_risk_data/scripts/stage9_20h_watchdog.py" \
  --role "$ROLE" \
  --mode "$MODE" \
  --workspace "$REDA_WS" \
  --duration-hours "${STAGE9_DURATION_HOURS:-20}" \
  --max-total-states "${STAGE9_MAX_TOTAL_STATES:-32}" \
  --max-parent-episodes "${STAGE9_MAX_PARENT_EPISODES:-12}" \
  --max-states-per-parent "${STAGE9_MAX_STATES_PER_PARENT:-4}" \
  --parent-roll-steps "${STAGE9_PARENT_ROLL_STEPS:-160}" \
  --terminal-horizon "${STAGE9_TERMINAL_HORIZON:-120}" \
  --min-train-samples "${STAGE9_MIN_TRAIN_SAMPLES:-5000}" \
  --bob-source "${STAGE9_BOB_SOURCE:-bob-stage9:/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/final_20h}" \
  "${extra[@]}" \
  > "$log" 2>&1 &

pid="$!"
echo "$pid" > "asynchvla_ws/stage9_libero_pro_risk_data/logs/stage9_20h_watchdog_${ROLE}.pid"
echo "Started Stage 9 20h watchdog role=$ROLE mode=$MODE pid=$pid log=$log"
