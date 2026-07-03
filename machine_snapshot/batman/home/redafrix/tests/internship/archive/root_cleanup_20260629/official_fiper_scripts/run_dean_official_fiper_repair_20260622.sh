#!/usr/bin/env bash
set -u

BASE=/home/dean/fiper_uncertainty_collection
PY=/home/redafrix/miniconda3/envs/simvla/bin/python
SCRIPT="$BASE/scripts/materialize_official_fiper_fold00_obs_embeddings_sharded_20260622.py"
RUNNER="$BASE/scripts/run_official_fiper_rndoe_entropy_fold00_20260622.py"
SUMMARIZER="$BASE/scripts/summarize_official_fiper_results_20260622.py"
EXP="$BASE/experiments/official_fiper_rndoe_entropy_fold00_20260622"
SHARD_DIR="$EXP/materialized_shards"
LOG_DIR="$BASE/logs/official_fiper_repair_20260622"

mkdir -p "$SHARD_DIR" "$LOG_DIR"
cd "$BASE" || exit 1

TOTAL_BATCHES=105
BATCH_SIZE=10
MAX_ATTEMPTS=3

run_one_batch() {
  local batch="$1"
  local shard
  local log
  shard="$SHARD_DIR/shard_batches_$(printf '%04d' "$batch")_$(printf '%04d' "$batch").pt"
  log="$LOG_DIR/shard_$(printf '%04d' "$batch")_$(printf '%04d' "$batch").log"

  if [ -s "$shard" ]; then
    echo "[skip] single-batch shard exists: $shard"
    return 0
  fi

  local attempt=1
  while [ "$attempt" -le "$MAX_ATTEMPTS" ]; do
    echo "[run] batch $batch attempt $attempt"
    rm -f "$shard.tmp"
    set +e
    PYTHONUNBUFFERED=1 "$PY" -u "$SCRIPT" shard \
      --start-batch "$batch" \
      --end-batch "$batch" \
      --batch-size "$BATCH_SIZE" \
      2>&1 | tee "$log.attempt${attempt}"
    local rc=${PIPESTATUS[0]}
    set -e

    if [ -s "$shard" ]; then
      echo "[ok] wrote $shard (python rc=$rc)"
      cat "$log.attempt${attempt}" >> "$log"
      return 0
    fi

    echo "[warn] missing shard after batch $batch attempt $attempt (python rc=$rc)"
    cat "$log.attempt${attempt}" >> "$log"
    attempt=$((attempt + 1))
    sleep 5
  done

  echo "[fatal] failed to produce $shard after $MAX_ATTEMPTS attempts"
  return 1
}

echo "[preflight] existing shards:"
find "$SHARD_DIR" -maxdepth 1 -type f -name 'shard_batches_*.pt' -printf '%f %s bytes\n' | sort

# Existing valid multi-batch shards cover batches 0..14.
for batch in $(seq 15 $((TOTAL_BATCHES - 1))); do
  run_one_batch "$batch" || exit 1
done

echo "[merge]"
PYTHONUNBUFFERED=1 "$PY" -u "$SCRIPT" merge 2>&1 | tee "$LOG_DIR/merge.log" || exit 1

echo "[validate]"
PYTHONUNBUFFERED=1 "$PY" -u "$SCRIPT" validate 2>&1 | tee "$LOG_DIR/validate.log" || exit 1

echo "[official eval]"
PYTHONUNBUFFERED=1 "$PY" -u "$RUNNER" 2>&1 | tee "$LOG_DIR/official_eval.log" || exit 1

echo "[summarize]"
PYTHONUNBUFFERED=1 "$PY" -u "$SUMMARIZER" 2>&1 | tee "$LOG_DIR/summarize.log" || exit 1

echo "OFFICIAL_FIPER_REPAIR_COMPLETE"
