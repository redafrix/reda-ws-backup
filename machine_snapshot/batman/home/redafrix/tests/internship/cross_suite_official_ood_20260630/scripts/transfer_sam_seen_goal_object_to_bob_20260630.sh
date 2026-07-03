#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630"
DEST="$ROOT/source_seen_goal_object_from_sam_20260630"
LOG="$ROOT/logs/sam_seen_transfer.log"
SRC="sam:/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626"

mkdir -p "$DEST" "$ROOT/logs"
{
  echo "started_at=$(date -Iseconds)"
  echo "src=$SRC"
  echo "dest=$DEST"
} >> "$LOG"

rsync -av --partial --append-verify \
  "$SRC/fiper_receding_samples.jsonl" \
  "$SRC/episode_summaries.jsonl" \
  "$SRC/run_manifest.json" \
  "$SRC/PIPELINE_MANIFEST.txt" \
  "$DEST/" >> "$LOG" 2>&1

{
  echo "done_at=$(date -Iseconds)"
  wc -l "$DEST/episode_summaries.jsonl" "$DEST/fiper_receding_samples.jsonl"
} >> "$LOG"
touch "$DEST/.TRANSFER_DONE"
