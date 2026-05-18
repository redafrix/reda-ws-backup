#!/usr/bin/env bash
set -uo pipefail
mkdir -p /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status
echo '[stage8] job architecture_loss_sweep_sam attempt 1 start '$(date -Is)
bash -lc 'cd "/home/rootalkhatib/test/reda_ws" && bash asynchvla_ws/scripts/stage8_run_sam_architecture_sweep.sh'
rc=$?
echo '[stage8] job architecture_loss_sweep_sam exit '$rc' at '$(date -Is)
if [ $rc -eq 0 ]; then touch /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/architecture_loss_sweep_sam.json.done_marker; else echo $rc > /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/architecture_loss_sweep_sam.json.fail_marker; fi
exit $rc

