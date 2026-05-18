#!/usr/bin/env bash
set -uo pipefail
mkdir -p /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status
echo '[stage8] job stage8_sam_model_sweep attempt 1 start '$(date -Is)
bash -lc 'cd "/home/rootalkhatib/test/reda_ws" && source asynchvla_ws/scripts/activate_simvla_sam.sh && export REDA_WS="/home/rootalkhatib/test/reda_ws" && mkdir -p asynchvla_ws/stage8_ultimate/reports && for split in holdout_libero_object holdout_object_bowl holdout_libero_spatial; do timeout 14400 python3 asynchvla_ws/src/rater_stage6/run_stage6_experiments.py --split "$split" --variants action_only_baseline full_old_baseline context_gated_action seed_relative_pairwise per_step_error_head full_engineered_simvla_focused --epochs 80 --out-prefix stage8_${split}_model_sweep || echo "WARN model_sweep failed $split"; done; cp asynchvla_ws/outputs/reports/stage6/stage8_*_model_sweep.md asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true; cp asynchvla_ws/outputs/reports/stage6/stage8_*_model_sweep.json asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true'
rc=$?
echo '[stage8] job stage8_sam_model_sweep exit '$rc' at '$(date -Is)
if [ $rc -eq 0 ]; then touch /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/stage8_sam_model_sweep.json.done_marker; else echo $rc > /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/stage8_sam_model_sweep.json.fail_marker; fi
exit $rc

