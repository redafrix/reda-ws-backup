#!/bin/bash
cd /home/rootalkhatib/marathon_c50/
mkdir -p logs runs

# Redemption Batch (3 and 5)
for i in 3 5
do
    echo "Starting Redemption Idea $i..."
    python3 marathon_100.py --idea "$i" >> logs/marathon_master.log 2>&1
    echo "Finished Redemption Idea $i."
done

# Resume Sequence (51 to 100)
for i in {51..100}
do
    echo "Starting Marathon Idea $i / 100..."
    python3 marathon_100.py --idea "$i" >> logs/marathon_master.log 2>&1
    echo "Finished Marathon Idea $i."
done

echo "REORDERED MARATHON COMPLETED!"
