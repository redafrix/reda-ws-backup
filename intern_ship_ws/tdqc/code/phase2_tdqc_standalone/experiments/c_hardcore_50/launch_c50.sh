#!/bin/bash
cd "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/c_hardcore_50/"

IDEAS=("1" "2" "4" "7" "22" "23" "29" "45" "47")

for IDEA in "${IDEAS[@]}"
do
    echo "Launching Idea $IDEA in background"
    nohup python3 marathon_c_50.py --idea $IDEA > logs/idea_$IDEA.log 2>&1 &
    sleep 2
done

echo "All ideas launched via nohup. Check logs/ directory for status."
