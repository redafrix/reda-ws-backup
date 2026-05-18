#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/rootalkhatib/test/reda_ws"
cd "$ROOT"
source asynchvla_ws/scripts/activate_simvla_sam.sh
export REDA_WS="$ROOT"
mkdir -p asynchvla_ws/stage8_ultimate/reports

for q in 0.80 0.90 0.95; do
  echo "[stage8] calibration sweep target_coverage=$q"
  timeout 7200 python3 asynchvla_ws/src/calibration_stage8/run_calibration_sweep.py --target-coverage "$q" || echo "[stage8] WARN calibration q=$q failed"
  cp asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.md "asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_q${q}.md" 2>/dev/null || true
  cp asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.json "asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_q${q}.json" 2>/dev/null || true
done

{
  echo "# Stage 8 Calibration Mega Sweep"
  echo
  echo "Ran calibration sweeps for target coverage 0.80, 0.90, and 0.95 using available Stage 6/8 predictions."
  echo
  echo "## Reports"
  find asynchvla_ws/stage8_ultimate/reports -maxdepth 1 -type f -name "stage8_calibration*" -printf "- \`%f\`\n" | sort
  echo
  echo "LIBERO-PRO rollout-risk calibration will be added after sufficient rollout/progress labels exist."
} > asynchvla_ws/stage8_ultimate/reports/stage8_calibration_mega_sweep.md
