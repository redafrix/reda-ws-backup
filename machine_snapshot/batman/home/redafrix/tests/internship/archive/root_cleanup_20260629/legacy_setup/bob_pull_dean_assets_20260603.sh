#!/usr/bin/env bash
set -euo pipefail

BOB_WS="/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
LOG="$BOB_WS/realtime_deployment/logs/bob_pull_dean_assets_20260603.log"
CKPT_DST="$BOB_WS/checkpoints/simvla_libero_uncertainty/ckpt-60000"
SMOL_DST="$BOB_WS/realtime_deployment/smolvlm_cache"
SSH_OPTS="ssh -o StrictHostKeyChecking=no -o ConnectTimeout=10 -o ServerAliveInterval=30 -o ServerAliveCountMax=20"

mkdir -p "$(dirname "$LOG")" "$CKPT_DST" "$SMOL_DST"
{
  echo "bob_pull_dean_assets started: $(date)"
  echo "host=$(hostname)"
  echo "--- ckpt pull"
} | tee "$LOG"

rsync -aP --partial --inplace -e "$SSH_OPTS" \
  dean@100.124.50.124:/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000/ \
  "$CKPT_DST/" 2>&1 | tee -a "$LOG"

echo "--- smolvlm pull" | tee -a "$LOG"
rsync -aPL --partial --inplace -e "$SSH_OPTS" \
  dean@100.124.50.124:/home/redafrix/.cache/huggingface/hub/models--HuggingFaceTB--SmolVLM-500M-Instruct/snapshots/a7da5b986cb59b408707209984f360a5f4ad7e47/ \
  "$SMOL_DST/" 2>&1 | tee -a "$LOG"

{
  echo "--- verification"
  stat -c '%n %s' "$CKPT_DST/model.safetensors"
  sha256sum "$CKPT_DST/model.safetensors"
  du -sh "$SMOL_DST"
  find "$SMOL_DST" -maxdepth 1 -type f -printf '%f %s\n' | sort
  echo "bob_pull_dean_assets finished: $(date)"
} | tee -a "$LOG"
