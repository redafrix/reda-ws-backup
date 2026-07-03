#!/usr/bin/env bash
set -euo pipefail

WS="/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623"
RUNNER="$WS/src/run_pi05_official_ood_selected_cap_20260625.py"
EVAL="$WS/src/eval_pi05_official_ood_two_heads_20260625.py"
SEEDS="$WS/configs/pi05_official_ood_100_seed_list_20260625.json"
ONLINE_ROOT="$WS/online_evals/pi05_official_ood_18task_100ep_basic_then_selected_cap_q95mass02_20260625"
OFFLINE_OUT="$WS/offline_risk_experiments/pi05_official_ood_18task_100ep_two_heads_eval_20260625"
LOG_DIR="$WS/logs/pi05_official_ood_18task_100ep_basic_then_selected_cap_q95mass02_20260625"

mkdir -p "$LOG_DIR"
cd "$WS"
source /home/rootalkhatib/pi05_openpi_20260623_env/bin/activate

export XLA_PYTHON_CLIENT_PREALLOCATE=false
export XLA_PYTHON_CLIENT_ALLOCATOR=platform
export PYTHONUNBUFFERED=1

COMMON_ARGS=(
  --output-root "$ONLINE_ROOT"
  --task-ids "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17"
  --seed-list-file "$SEEDS"
  --max-steps 300
  --mass-threshold 0.2
  --selection-mode selected_cap
  --selection-main-threshold 0.7218163013458249
  --selection-min-margin 0.005
  --selection-strong-margin 0.02
  --selection-max-selected-score 0.95
)

echo "[pipeline] $(date) starting official Pi0.5 OOD 18-task run"
echo "[pipeline] online root: $ONLINE_ROOT"
echo "[pipeline] offline out: $OFFLINE_OUT"
echo "[pipeline] seed list: $SEEDS"

echo "[pipeline] $(date) phase 1/3: pi05_basic_h10"
python3 -u "$RUNNER" "${COMMON_ARGS[@]}" --policies pi05_basic_h10 2>&1 | tee -a "$LOG_DIR/basic.log"

echo "[pipeline] $(date) phase 2/3: pi05_risk_selected_cap_topk8_h10"
python3 -u "$RUNNER" "${COMMON_ARGS[@]}" --policies pi05_risk_selected_cap_topk8_h10 2>&1 | tee -a "$LOG_DIR/risk_selected_cap.log"

echo "[pipeline] $(date) phase 3/3: offline two-head evaluation"
python3 -u "$EVAL" --online-root "$ONLINE_ROOT" --out-dir "$OFFLINE_OUT" 2>&1 | tee -a "$LOG_DIR/offline_eval.log"

echo "[pipeline] $(date) completed"
