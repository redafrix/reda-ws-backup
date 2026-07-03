#!/bin/bash
# run_100_libero.sh
export PYTHONPATH=$PYTHONPATH:$(pwd)
ENV_PYTHON="/home/rootalkhatib/envs/simvla/bin/python"
SUITE="libero_spatial"
TASK_ID=0
NUM_EPISODES=100
OUTPUT_DIR="eval_results_100"
mkdir -p $OUTPUT_DIR

echo "Starting 100 episodes for $SUITE task $TASK_ID..."

for i in $(seq 0 $((NUM_EPISODES-1)))
do
    echo "Running Episode $i..."
    $ENV_PYTHON simvla/scripts/run_libero_single_task_eval.py \
        --task_suite $SUITE \
        --task_id $TASK_ID \
        --episode_index $i \
        --video_path "$OUTPUT_DIR/episode_$i.mp4" \
        --summary_path "$OUTPUT_DIR/episode_$i.json" \
        --port 8000
done

echo "Benchmark complete. Results in $OUTPUT_DIR"
