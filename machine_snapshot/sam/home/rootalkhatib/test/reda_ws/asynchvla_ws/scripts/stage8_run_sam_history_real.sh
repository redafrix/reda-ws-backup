#!/usr/bin/env bash
set -euo pipefail
ROOT="${REDA_WS:-/home/rootalkhatib/test/reda_ws}"
cd "$ROOT"
source asynchvla_ws/scripts/activate_simvla_sam.sh
export REDA_WS="$ROOT"
mkdir -p asynchvla_ws/stage8_ultimate/reports
out=asynchvla_ws/stage8_ultimate/reports/stage8_history_real_results.md
{
  echo "# Stage 8 History Real Results"
  echo
  echo "Generated: $(date -Is)"
  echo
  echo "## Rollout Log Availability"
  find asynchvla_ws/stage8_ultimate/results -maxdepth 4 -type f \( -name "*.json" -o -name "*.jsonl" \) | head -200 || true
  echo
  echo "## Decision"
  echo "History models need sequential rollout logs with previous action/uncertainty/proprio. If only aggregate episode JSON is available on Sam, this job records the blocker and exits successfully as a truthful report."
} > "$out"
