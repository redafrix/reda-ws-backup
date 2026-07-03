#!/usr/bin/env bash
set -euo pipefail

BASE=/home/dean/fiper_uncertainty_collection
PY=/home/redafrix/miniconda3/envs/simvla/bin/python
SCRIPT="$BASE/scripts/materialize_official_fiper_fold00_obs_embeddings_sharded_20260622.py"
LOG_DIR="$BASE/logs/official_fiper_sharded_20260622"
mkdir -p "$LOG_DIR"

TOTAL_BATCHES=105
BATCHES_PER_PROCESS=5
BATCH_SIZE=10

cd "$BASE"

for START in $(seq 0 "$BATCHES_PER_PROCESS" $((TOTAL_BATCHES - 1))); do
  END=$((START + BATCHES_PER_PROCESS - 1))
  if [ "$END" -ge "$TOTAL_BATCHES" ]; then
    END=$((TOTAL_BATCHES - 1))
  fi
  SHARD="$BASE/experiments/official_fiper_rndoe_entropy_fold00_20260622/materialized_shards/shard_batches_$(printf '%04d' "$START")_$(printf '%04d' "$END").pt"
  if [ -s "$SHARD" ]; then
    echo "[skip] existing shard $SHARD"
    continue
  fi
  echo "[run] batches $START..$END"
  set +e
  PYTHONUNBUFFERED=1 "$PY" -u "$SCRIPT" shard --start-batch "$START" --end-batch "$END" --batch-size "$BATCH_SIZE" \
    2>&1 | tee "$LOG_DIR/shard_$(printf '%04d' "$START")_$(printf '%04d' "$END").log"
  RC=${PIPESTATUS[0]}
  set -e
  if [ "$RC" -ne 0 ]; then
    if [ -s "$SHARD" ]; then
      echo "[warn] shard process returned $RC after writing $SHARD; continuing"
    else
      echo "[error] shard process returned $RC and $SHARD is missing"
      exit "$RC"
    fi
  fi
done

echo "[merge]"
PYTHONUNBUFFERED=1 "$PY" -u "$SCRIPT" merge 2>&1 | tee "$LOG_DIR/merge.log"

echo "[validate]"
PYTHONUNBUFFERED=1 "$PY" -u "$SCRIPT" validate 2>&1 | tee "$LOG_DIR/validate.log"

echo "[done] materialization shards merged and validated"
