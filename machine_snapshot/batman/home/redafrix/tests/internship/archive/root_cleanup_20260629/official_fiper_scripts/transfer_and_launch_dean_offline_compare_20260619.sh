#!/usr/bin/env bash
set -euo pipefail

KEY=/tmp/id_dean_reda
KNOWN=/tmp/known_hosts_dean_reda
DEAN="dean@100.124.50.124"
SSH_BASE=(ssh -i "$KEY" -o StrictHostKeyChecking=no -o UserKnownHostsFile="$KNOWN")
ARCHIVE=/tmp/fiper_compare_payload_20260619.tgz
REMOTE_ROOT=/home/dean/fiper_uncertainty_collection
REMOTE_ARCHIVE="$REMOTE_ROOT/fiper_compare_payload_20260619.tgz"
REMOTE_OUT="$REMOTE_ROOT/experiments/clean_offline_original_fiper_vs_v2018_fold00_20260619"
REMOTE_LOG="$REMOTE_ROOT/logs/clean_offline_original_fiper_vs_v2018_fold00_20260619"
PY=/home/redafrix/miniconda3/envs/simvla/bin/python
REFS="$REMOTE_ROOT/experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs"
LOG=/tmp/transfer_and_launch_dean_offline_compare_20260619.log

exec > >(tee -a "$LOG") 2>&1

echo "[chain] start $(date -Is)"
ls -lh "$ARCHIVE"
"${SSH_BASE[@]}" "$DEAN" "mkdir -p '$REMOTE_ROOT' '$REMOTE_LOG'"

echo "[chain] rsync archive to Dean $(date -Is)"
attempt=0
until rsync -avP --partial --append-verify --timeout=120 \
    -e "ssh -i $KEY -o StrictHostKeyChecking=no -o UserKnownHostsFile=$KNOWN" \
    "$ARCHIVE" "$DEAN:$REMOTE_ARCHIVE"; do
  attempt=$((attempt + 1))
  echo "[chain] rsync attempt $attempt failed $(date -Is); retrying in 20s"
  sleep 20
done

echo "[chain] extract archive on Dean $(date -Is)"
"${SSH_BASE[@]}" "$DEAN" \
  "cd '$REMOTE_ROOT' && tar -xzf '$REMOTE_ARCHIVE' && rm -f '$REMOTE_ARCHIVE' && '$PY' -m py_compile scripts/run_offline_original_fiper_vs_v2018_clean_compare.py scripts/run_clean_temporal_nextgen_campaign_v2.py"

echo "[chain] write Dean launch script $(date -Is)"
"${SSH_BASE[@]}" "$DEAN" "cat > '$REMOTE_ROOT/scripts/launch_clean_offline_fiper_compare_20260619.sh' <<'REMOTE_EOF'
#!/usr/bin/env bash
set -euo pipefail
cd /home/dean/fiper_uncertainty_collection
/home/redafrix/miniconda3/envs/simvla/bin/python -u scripts/run_offline_original_fiper_vs_v2018_clean_compare.py \
  --refs-dir /home/dean/fiper_uncertainty_collection/experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs \
  --base-dir /home/dean/fiper_uncertainty_collection \
  --output-dir /home/dean/fiper_uncertainty_collection/experiments/clean_offline_original_fiper_vs_v2018_fold00_20260619 \
  --device cuda \
  --seed 42 \
  --rnd-epochs 20 \
  --batch-size 384 \
  --v2018-max-epochs 120 \
  --v2018-patience 18 \
  --force \
  2>&1 | tee /home/dean/fiper_uncertainty_collection/logs/clean_offline_original_fiper_vs_v2018_fold00_20260619/run.log
REMOTE_EOF
chmod +x '$REMOTE_ROOT/scripts/launch_clean_offline_fiper_compare_20260619.sh'"

echo "[chain] launch Dean tmux $(date -Is)"
"${SSH_BASE[@]}" "$DEAN" \
  "tmux has-session -t dean_clean_offline_fiper_compare_20260619 2>/dev/null && tmux kill-session -t dean_clean_offline_fiper_compare_20260619 || true; tmux new-session -d -s dean_clean_offline_fiper_compare_20260619 'bash $REMOTE_ROOT/scripts/launch_clean_offline_fiper_compare_20260619.sh'"

echo "[chain] launched $(date -Is)"
"${SSH_BASE[@]}" "$DEAN" \
  "tmux ls | grep dean_clean_offline_fiper_compare_20260619; tail -n 5 '$REMOTE_LOG/run.log' 2>/dev/null || true; df -h /home/dean | tail -1"
echo "[chain] done $(date -Is)"
