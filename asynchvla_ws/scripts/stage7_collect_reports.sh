#!/usr/bin/env bash
set -euo pipefail
ROOT=${ROOT:-"/media/rootalkhatib/My Passport/reda_ws"}
LOCAL=${LOCAL:-"/home/redafrix/tests/internship/codex_reports/stage7"}
mkdir -p "$LOCAL"
cd "$ROOT"
find asynchvla_ws/outputs/reports/stage7 -maxdepth 1 -type f \( -name "*.md" -o -name "*.json" \) -print0 | while IFS= read -r -d "" f; do
  cp "$f" "$LOCAL/$(basename "$f")"
done
for f in asynchvla_ws/ASYNCVLA_SIMVLA_STAGE7_EXECUTION_AND_ROBUSTNESS_REPORT.md; do
  if [[ -f "$f" ]]; then cp "$f" "/home/redafrix/tests/internship/codex_reports/$(basename "$f")"; fi
done
