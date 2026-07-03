#!/usr/bin/env bash
set -u
cd /home/redafrix/SimVLA_modified/evaluation/libero
RUN_DIR="$1"
PORT=8123
SEED=31
for suite in libero_goal libero_10; do
  echo "[$(date '+%F %T')] starting ${suite}" | tee -a "$RUN_DIR/master.log"
  TASK_SUITE="$suite" \
  NUM_TRIALS=10 \
  SEED="$SEED" \
  PORT="$PORT" \
  NO_VIDEO=true \
  VIDEO_OUT="$RUN_DIR" \
  UNCERTAINTY_LOG="$RUN_DIR/${suite}_uncertainty.jsonl" \
  conda run -n libero ./run_libero_pro_eval.sh > "$RUN_DIR/${suite}.log" 2>&1
  rc=$?
  echo "[$(date '+%F %T')] finished ${suite} rc=${rc}" | tee -a "$RUN_DIR/master.log"
  rg -n "Total success rate|Task [0-9]+:" "$RUN_DIR/${suite}.log" | tail -20 >> "$RUN_DIR/master.log" || true
  SEED=$((SEED + 100))
done
