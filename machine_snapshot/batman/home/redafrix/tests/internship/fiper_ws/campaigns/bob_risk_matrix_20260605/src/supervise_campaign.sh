#!/usr/bin/env bash
set -uo pipefail

CAMPAIGN_ROOT="${1:?campaign root required}"
MANIFEST="${2:?manifest required}"
PYTHON_BIN="${PYTHON_BIN:-/usr/bin/python3}"
LOG="$CAMPAIGN_ROOT/logs/supervisor.log"

mkdir -p "$CAMPAIGN_ROOT/logs" "$CAMPAIGN_ROOT/state"

while true; do
  printf '[%s] scheduler start\n' "$(date -Is)" >> "$LOG"
  "$PYTHON_BIN" "$CAMPAIGN_ROOT/src/campaign_scheduler.py" --manifest "$MANIFEST" >> "$LOG" 2>&1
  code=$?
  printf '[%s] scheduler exit code=%s\n' "$(date -Is)" "$code" >> "$LOG"
  if [[ -f "$CAMPAIGN_ROOT/state/campaign_complete.json" ]]; then
    exit "$code"
  fi
  sleep 60
done
