#!/bin/bash
IDEAS=(301 302 303 304 305 306 307 308 310 311)
mkdir -p runs
for ID in ${IDEAS[@]}
do
    echo "=================================================="
    echo "STARTING MARATHON IDEA: $ID"
    echo "=================================================="
    python3 -u marathon_b_series.py --idea_id $ID
    echo "FINISHED MARATHON IDEA: $ID"
    echo ""
done
