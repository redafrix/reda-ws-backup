#!/usr/bin/env bash
set -uo pipefail
mkdir -p /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status
echo '[stage8] job stage8_sam_calibration_sweep attempt 1 start '$(date -Is)
bash -lc 'cd "/home/rootalkhatib/test/reda_ws" && source asynchvla_ws/scripts/activate_simvla_sam.sh && export REDA_WS="/home/rootalkhatib/test/reda_ws" && python3 asynchvla_ws/src/calibration_stage8/run_calibration_sweep.py && cp asynchvla_ws/stage8_ultimate/reports/stage8_calibration*.md asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true'
rc=$?
echo '[stage8] job stage8_sam_calibration_sweep exit '$rc' at '$(date -Is)
if [ $rc -eq 0 ]; then touch /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/stage8_sam_calibration_sweep.json.done_marker; else echo $rc > /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/stage8_sam_calibration_sweep.json.fail_marker; fi
exit $rc

