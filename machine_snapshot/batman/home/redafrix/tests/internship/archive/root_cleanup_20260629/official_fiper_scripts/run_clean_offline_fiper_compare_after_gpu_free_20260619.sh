#!/usr/bin/env bash
set -euo pipefail

FIPER_ROOT="/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
OUT_DIR="$FIPER_ROOT/experiments/clean_offline_original_fiper_vs_v2018_fold00_20260619"
LOG_DIR="$FIPER_ROOT/logs/clean_offline_original_fiper_vs_v2018_fold00_20260619"
REFS_DIR="$FIPER_ROOT/experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs"
ACTIVATE="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"

mkdir -p "$LOG_DIR"
echo "[launcher] started $(date -Is)" | tee -a "$LOG_DIR/launcher.log"
echo "[launcher] waiting for GPU memory <= 3000 MiB" | tee -a "$LOG_DIR/launcher.log"

while true; do
  used="$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -n 1 | tr -d ' ')"
  util="$(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits | head -n 1 | tr -d ' ')"
  echo "[launcher] $(date -Is) gpu_used_mib=$used gpu_util_pct=$util" | tee -a "$LOG_DIR/launcher.log"
  if [[ "$used" =~ ^[0-9]+$ ]] && [ "$used" -le 3000 ]; then
    break
  fi
  sleep 300
done

echo "[launcher] starting clean offline comparison $(date -Is)" | tee -a "$LOG_DIR/launcher.log"
cd "$FIPER_ROOT"
source "$ACTIVATE"
python3 -u scripts/run_offline_original_fiper_vs_v2018_clean_compare.py \
  --refs-dir "$REFS_DIR" \
  --base-dir "$FIPER_ROOT" \
  --output-dir "$OUT_DIR" \
  --device cuda \
  --seed 42 \
  --rnd-epochs 20 \
  --batch-size 384 \
  --v2018-max-epochs 120 \
  --v2018-patience 18 \
  --force \
  2>&1 | tee "$LOG_DIR/run.log"

echo "[launcher] finished $(date -Is)" | tee -a "$LOG_DIR/launcher.log"
