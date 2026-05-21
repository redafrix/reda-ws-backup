#!/usr/bin/env bash
# train_rnd_success_only.sh - wrapper for RND training and conformal threshold calibration
set -euo pipefail

CAMPAIGN_DIR="/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/success_only_fiper_20260521_102354"
FIPER_WS="/home/rootalkhatib/test/reda_ws/fiper_ws"

source "/home/rootalkhatib/test/reda_ws/asynchvla_ws/scripts/activate_simvla_sam.sh"
export PYTHONPATH="${FIPER_WS}:${PYTHONPATH:-}"

echo "=== Training RND-OE on Train Success ID split ==="
python3 -u -m stage9_fiper_bridge.train_rnd_oe \
  --jsonl "${CAMPAIGN_DIR}/datasets/train_success_id.jsonl" \
  --out-dir "${CAMPAIGN_DIR}/fiper/rnd_success_only" \
  --hidden-dim 256 \
  --output-dim 128 \
  --epochs 30 \
  --batch-size 512 \
  --lr 0.001 \
  --max-risk 0.20 \
  --min-conf 0.80

echo "=== Calibrating Conformal Thresholds on Calib Success ID split ==="
python3 -u -c "
import json
import numpy as np
from pathlib import Path
from stage9_fiper_bridge.train_rnd_oe import score_samples

model_path = Path('${CAMPAIGN_DIR}/fiper/rnd_success_only/rnd_oe_success_only.pt')
calib_path = Path('${CAMPAIGN_DIR}/datasets/calib_success_id.jsonl')

print(f'Loading calib samples from {calib_path}')
with calib_path.open() as f:
    samples = [json.loads(line) for line in f if line.strip()]

print(f'Scoring {len(samples)} calib samples...')
scored = score_samples(model_path, samples)

# Save calib scores
calib_scores_path = Path('${CAMPAIGN_DIR}/fiper/rnd_success_only/rnd_scores_calib.jsonl')
with calib_scores_path.open('w') as f:
    for s in scored:
        f.write(json.dumps(s) + '\n')
print(f'Saved calib scores to {calib_scores_path}')

# Compute thresholds strictly on calib set
rnd_vals = np.array([s['rnd_score'] for s in scored])
thresholds = {
    'q90': float(np.quantile(rnd_vals, 0.90)),
    'q95': float(np.quantile(rnd_vals, 0.95)),
    'q99': float(np.quantile(rnd_vals, 0.99)),
    'mean': float(rnd_vals.mean()),
    'std': float(rnd_vals.std()),
    'min': float(rnd_vals.min()),
    'max': float(rnd_vals.max())
}

thresh_path = Path('${CAMPAIGN_DIR}/fiper/rnd_success_only/rnd_conformal_thresholds.json')
thresh_path.write_text(json.dumps(thresholds, indent=2) + '\n')
print('Calibrated Thresholds (from calib_success_id only):')
print(json.dumps(thresholds, indent=2))
"

echo "=== RND-OE training and threshold calibration complete ==="
