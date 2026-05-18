#!/usr/bin/env bash
set -uo pipefail
mkdir -p '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status'
echo '[stage8] job stage8_final_report_bob attempt 1 start '$(date -Is)
bash -lc 'cd "/media/rootalkhatib/My Passport/reda_ws" && python3 asynchvla_ws/scripts/stage8_write_final_report.py'
rc=$?
echo '[stage8] job stage8_final_report_bob exit '$rc' at '$(date -Is)
if [ $rc -eq 0 ]; then touch '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/stage8_final_report_bob.json.done_marker'; else echo $rc > '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/stage8_final_report_bob.json.fail_marker'; fi
exit $rc

