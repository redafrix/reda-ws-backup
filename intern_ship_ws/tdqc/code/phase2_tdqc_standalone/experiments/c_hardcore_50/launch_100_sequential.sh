#!/bin/bash
cd /home/rootalkhatib/marathon_c50/
mkdir -p logs runs
for i in {1..100}
do
    echo "Starting Marathon Idea $i / 100..."
    python3 marathon_100.py --idea "$i" >> logs/marathon_master.log 2>&1
    echo "Finished Marathon Idea $i."
done
echo "ALL 100 MARATHON IDEAS COMPLETED!"

echo "Starting Redemption Batch (Ideas 3 and 5)..."
python3 marathon_100.py --idea "3" >> logs/marathon_master.log 2>&1
python3 marathon_100.py --idea "5" >> logs/marathon_master.log 2>&1
echo "REDEMPTION COMPLETE. ALL 102 TESTS FINISHED!"
