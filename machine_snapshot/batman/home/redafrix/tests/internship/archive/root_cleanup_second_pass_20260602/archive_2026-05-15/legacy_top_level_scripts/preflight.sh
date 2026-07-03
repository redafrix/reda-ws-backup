#!/bin/bash
WS="/media/rootalkhatib/My Passport/reda_ws"
REPORT="${WS}/asynchvla_ws/outputs/reports/stage5_preflight.md"

mkdir -p "${WS}/asynchvla_ws/outputs/reports"

cat << 'EOF' > "$REPORT"
# Stage 5 Preflight Report

EOF

echo "**1. Current date/time:** $(date)" >> "$REPORT"
echo "**2. Hostname:** $(hostname)" >> "$REPORT"
echo "**3. Current user:** $(whoami)" >> "$REPORT"
echo "**4. Current working directory:** $WS" >> "$REPORT"

cd "$WS" || exit 1
echo "**5. Current git branch:** $(git branch --show-current)" >> "$REPORT"
echo "**6. Git status:**" >> "$REPORT"
echo '```text' >> "$REPORT"
git status --short >> "$REPORT"
echo '```' >> "$REPORT"

echo "**7. Activation test:**" >> "$REPORT"
source asynchvla_ws/scripts/activate_simvla_bob.sh > /dev/null 2>&1
if [ $? -eq 0 ]; then
  echo "Activation works." >> "$REPORT"
else
  echo "Activation failed." >> "$REPORT"
fi

echo "**8. which python:** $(which python3)" >> "$REPORT"
echo "**9. python --version:** $(python3 --version)" >> "$REPORT"

echo "**10. Torch/CUDA availability:**" >> "$REPORT"
python3 -c "import torch; print(f'Torch: {torch.__version__}, CUDA: {torch.cuda.is_available()}')" >> "$REPORT" 2>&1

echo "**11. SimVLA checkpoint exists:**" >> "$REPORT"
if [ -d "intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000" ]; then echo "Yes"; else echo "No"; fi >> "$REPORT"

echo "**12. Stage 4 processed data exists (Checking splits dir for Stage 4 data):**" >> "$REPORT"
if [ -d "asynchvla_ws/data/splits" ]; then echo "Yes"; else echo "No"; fi >> "$REPORT"

echo "**13. Split manifests exist:**" >> "$REPORT"
ls asynchvla_ws/data/splits/*.json >/dev/null 2>&1 && echo "Yes" || echo "No" >> "$REPORT"

echo "**14. Disk space:**" >> "$REPORT"
echo '```text' >> "$REPORT"
df -h . >> "$REPORT"
echo '```' >> "$REPORT"

cat "$REPORT"
