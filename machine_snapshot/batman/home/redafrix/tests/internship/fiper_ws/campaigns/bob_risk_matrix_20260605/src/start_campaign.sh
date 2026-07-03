#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/bob_risk_matrix_campaign_20260605"
SESSION="bob_risk_matrix_20260605"

for _ in $(seq 1 60); do
  [[ -f "$ROOT/manifests/campaign_manifest.json" ]] && break
  sleep 30
done

[[ -f "$ROOT/manifests/campaign_manifest.json" ]] || exit 1
tmux has-session -t "$SESSION" 2>/dev/null && exit 0
tmux new-session -d -s "$SESSION" -c "$ROOT" \
  "bash '$ROOT/src/supervise_campaign.sh' '$ROOT' '$ROOT/manifests/campaign_manifest.json'"
