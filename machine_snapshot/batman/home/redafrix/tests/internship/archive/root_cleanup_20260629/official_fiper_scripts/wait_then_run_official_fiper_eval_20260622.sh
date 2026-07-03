#!/usr/bin/env bash
set -euo pipefail

BASE=/home/dean/fiper_uncertainty_collection
PY=/home/redafrix/miniconda3/envs/simvla/bin/python
VALIDATE_LOG="$BASE/logs/official_fiper_sharded_20260622/validate.log"
RUN_LOG="$BASE/logs/official_fiper_rndoe_fold00_20260622.log"
SUMMARY_SCRIPT="$BASE/scripts/summarize_official_fiper_results_20260622.py"

echo "[waiter] waiting for sharded materialization validation: $VALIDATE_LOG"
while true; do
  if [ -f "$VALIDATE_LOG" ] && grep -q "VALIDATION_PASS" "$VALIDATE_LOG"; then
    echo "[waiter] validation passed"
    break
  fi
  if ! tmux has-session -t official_fiper_sharded_materialize_20260622 2>/dev/null; then
    echo "[waiter] materialization tmux is gone and validation has not passed"
    exit 2
  fi
  sleep 120
done

cd "$BASE"
echo "[waiter] launching official FIPER evaluation"
PYTHONUNBUFFERED=1 "$PY" -u "$BASE/scripts/run_official_fiper_rndoe_entropy_fold00_20260622.py" 2>&1 | tee "$RUN_LOG"

echo "[waiter] writing summary report"
"$PY" "$SUMMARY_SCRIPT"
echo "[waiter] done"
