#!/usr/bin/env bash
set -uo pipefail
mkdir -p '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status' '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status'
echo '[stage8] job smoke_retry_failure attempt 2 start '$(date -Is)
bash -lc 'cd "/media/rootalkhatib/My Passport/reda_ws"; f=asynchvla_ws/stage8_ultimate/results/smoke_retry_counter.txt; n=0; [ -f "$f" ] && n=$(cat "$f"); n=$((n+1)); echo $n > "$f"; if [ "$n" -lt 2 ]; then echo intentional_fail; exit 7; fi; echo retry_ok > asynchvla_ws/stage8_ultimate/results/smoke_retry_success.txt'
rc=$?
echo '[stage8] job smoke_retry_failure exit '$rc' at '$(date -Is)
if [ $rc -eq 0 ]; then touch '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_retry_failure.json.done_marker'; else echo $rc > '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_retry_failure.json.fail_marker'; fi
exit $rc

