#!/usr/bin/env bash
set -euo pipefail

ROOT=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
FIRST="$ROOT/automation/FIRST_RISK_TRAIN_AND_LOCKED_EVAL_COMPLETE"
STOP_MAIN="$ROOT/automation/STOP_PIPELINE_AFTER_CURRENT_EPISODE"

test -f "$FIRST"
touch "$STOP_MAIN"
exec "$ROOT/automation/hard1000_pipeline_tmux.sh" ensure
