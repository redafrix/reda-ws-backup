#!/usr/bin/env bash
set -uo pipefail
mkdir -p '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status'
echo '[stage8] job libero_pro_pilot_bob attempt 1 start '$(date -Is)
bash -lc 'cd "/media/rootalkhatib/My Passport/reda_ws" && bash asynchvla_ws/scripts/stage8_run_libero_pro_pilot.sh'
rc=$?
echo '[stage8] job libero_pro_pilot_bob exit '$rc' at '$(date -Is)
if [ $rc -eq 0 ]; then touch '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/libero_pro_pilot_bob.json.done_marker'; else echo $rc > '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/libero_pro_pilot_bob.json.fail_marker'; fi
exit $rc

