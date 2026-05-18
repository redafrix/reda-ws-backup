#!/usr/bin/env bash
set -uo pipefail
mkdir -p '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status'
echo '[stage8] job smoke_dependency_child attempt 1 start '$(date -Is)
cd "/media/rootalkhatib/My Passport/reda_ws" && cat asynchvla_ws/stage8_ultimate/results/smoke_bob_cpu.txt > asynchvla_ws/stage8_ultimate/results/smoke_dependency_child.txt
rc=$?
echo '[stage8] job smoke_dependency_child exit '$rc' at '$(date -Is)
if [ $rc -eq 0 ]; then touch '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_dependency_child.json.done_marker'; else echo $rc > '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_dependency_child.json.fail_marker'; fi
exit $rc

