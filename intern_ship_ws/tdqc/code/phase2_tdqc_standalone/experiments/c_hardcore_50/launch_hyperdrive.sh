#!/bin/bash
cd /home/rootalkhatib/marathon_c50/
mkdir -p logs runs

# Define the queue of remaining ideas
# (Starting with 3 and 5, then skipping 1,2,4,6-50, resuming 51-100)
QUEUE=(3 5)
for i in {51..100}
do
    QUEUE+=($i)
done

MAX_PARALLEL=3
COUNT=0

for idea in "${QUEUE[@]}"
do
    echo "[Hyper-Drive] Launching Idea $idea..."
    python3 marathon_100.py --idea "$idea" >> "logs/idea_$idea.log" 2>&1 &
    
    ((COUNT++))
    
    if (( COUNT % MAX_PARALLEL == 0 )); then
        echo "[Hyper-Drive] Waiting for batch to complete..."
        wait
    fi
done

wait
echo "HYPER-DRIVE MARATHON COMPLETED!"
