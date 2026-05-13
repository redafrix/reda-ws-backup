#!/bin/bash
cd "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/c_hardcore_50/"
mkdir -p logs runs
for i in {1..50}
do
    echo "Starting Marathon Idea $i / 50..."
    python3 marathon_c_50.py --idea "$i" >> logs/marathon_master.log 2>&1
    echo "Finished Marathon Idea $i."
done
echo "ALL 50 MARATHON IDEAS COMPLETED!"
