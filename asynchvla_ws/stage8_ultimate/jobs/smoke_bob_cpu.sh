#!/usr/bin/env bash
set -uo pipefail
mkdir -p '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status'
echo '[stage8] job smoke_bob_cpu attempt 1 start '$(date -Is)
cd "/media/rootalkhatib/My Passport/reda_ws" && mkdir -p asynchvla_ws/stage8_ultimate/results && echo bob_ok > asynchvla_ws/stage8_ultimate/results/smoke_bob_cpu.txt
rc=$?
echo '[stage8] job smoke_bob_cpu exit '$rc' at '$(date -Is)
if [ $rc -eq 0 ]; then touch '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_bob_cpu.json.done_marker'; else echo $rc > '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_bob_cpu.json.fail_marker'; fi
exit $rc

