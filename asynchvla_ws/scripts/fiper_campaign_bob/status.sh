#!/bin/bash
echo "Checking Bob PIDs..."
ps -p 1100550 1100551
echo "Checking logs tail..."
tail -n 20 "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/logs/instance_A.log" "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/logs/instance_B.log"
echo "Disk usage:"
df -h "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_receding_all_outcomes_bob_20260521_170310"
