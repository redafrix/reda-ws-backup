#!/usr/bin/env bash
set -euo pipefail
ROOT="${REDA_WS:-/home/rootalkhatib/test/reda_ws}"
cd "$ROOT"
source asynchvla_ws/scripts/activate_simvla_sam.sh
export REDA_WS="$ROOT"
mkdir -p asynchvla_ws/stage8_ultimate/reports
out=asynchvla_ws/stage8_ultimate/reports/stage8_calibration_mega_sweep_results.md
{
  echo "# Stage 8 Calibration Mega Sweep Results"
  echo
  echo "Generated: $(date -Is)"
  echo
} > "$out"
for q in 0.80 0.90 0.95; do
  echo "[stage8] calibration q=$q"
  timeout 10800 python3 asynchvla_ws/src/calibration_stage8/run_calibration_sweep.py --target-coverage "$q"
  cp asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.md "asynchvla_ws/stage8_ultimate/reports/stage8_calibration_real_q${q}.md"
  cp asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.json "asynchvla_ws/stage8_ultimate/reports/stage8_calibration_real_q${q}.json" 2>/dev/null || true
  echo "- completed q=$q" >> "$out"
done
{
  echo
  echo "## Methods Covered By Current Implementation"
  echo "- global residual conformal"
  echo "- SimVLA-only residual conformal"
  echo "- affine + residual"
  echo "- target coverages 0.80 / 0.90 / 0.95"
  echo
  echo "## Still Analysis/Pending If Not Implemented In Code"
  echo "- isotonic, Platt/logistic, ensemble, CV+, small-OOD pool repetitions require code additions if absent from run_calibration_sweep.py."
  echo
  find asynchvla_ws/stage8_ultimate/reports -maxdepth 1 -type f -name "stage8_calibration*" -printf "- \`%f\`\n" | sort
} >> "$out"
cp "$out" asynchvla_ws/stage8_ultimate/reports/stage8_calibration_best_deployable_method.md
