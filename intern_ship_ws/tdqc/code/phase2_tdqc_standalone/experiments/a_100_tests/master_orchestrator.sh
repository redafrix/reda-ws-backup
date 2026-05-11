#!/bin/bash

# Master Orchestrator for the 100-Experiment TDQC Marathon (PRODUCTION 1000-EPOCH RUN)
# This script runs 100 tests back-to-back for 1000 epochs each.

BASE_DIR="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests"
LOG_DIR="$BASE_DIR/logs_marathon"
mkdir -p "$LOG_DIR"

RUN_LOG="$LOG_DIR/marathon_production.log"
echo "Starting 100-Experiment PRODUCTION Marathon (1000 Epochs) at $(date)" > "$RUN_LOG"

# Environment
PYTHON_PATH="python3"

# Dataset paths
TRAIN_DATASET="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt"
TEST_DATASET="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_test.pt"
OOD_DATASET="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_unseen_obj_ood.pt"

for i in $(seq -f "%03g" 1 100); do
    IDEA_DIR="$BASE_DIR/idea_$i"
    IDEA_LOG="$LOG_DIR/idea_$i.log"
    
    # Check if already completed (optional, but good for resume)
    if [ -f "$IDEA_DIR/runs/granular_results.json" ]; then
         # Check if it was a production run (1000 epochs)
         # For simplicity, we assume if it exists in logs_marathon it is fine.
         echo "Skipping Idea $i as it already has results." | tee -a "$RUN_LOG"
         continue # Uncomment if you want to allow resume. User asked to launch it now, 
         # but resume is safer in case of connection loss.
    fi

    echo "--------------------------------------------------" | tee -a "$RUN_LOG"
    echo "Launching Idea $i at $(date)..." | tee -a "$RUN_LOG"
    
    if [ ! -d "$IDEA_DIR" ]; then
        echo "ERROR: Directory $IDEA_DIR not found. Skipping." | tee -a "$RUN_LOG"
        continue
    fi
    
    cd "$IDEA_DIR"
    # Clean up previous runs
    rm -rf "$IDEA_DIR/runs"
    mkdir -p "$IDEA_DIR/runs"

    # Run training
    echo "Running Training for Idea $i (1000 Epochs)..." | tee -a "$RUN_LOG"
    PYTHONUNBUFFERED=1 "$PYTHON_PATH" -u train.py \
        --dataset_path "$TRAIN_DATASET" \
        --output_dir "$IDEA_DIR/runs" \
        --epochs 1000 \
        --device "cuda" 2>&1 | tee "$IDEA_LOG"
    
    TRAIN_EXIT_CODE=$?
    
    if [ $TRAIN_EXIT_CODE -ne 0 ]; then
        echo "FAILED: Idea $i Training crashed with exit code $TRAIN_EXIT_CODE. Check $IDEA_LOG" | tee -a "$RUN_LOG"
    else
        echo "SUCCESS: Idea $i Training completed." | tee -a "$RUN_LOG"
        
        # Run Evaluation
        echo "Running Granular Evaluation for Idea $i..." | tee -a "$RUN_LOG"
        PYTHONUNBUFFERED=1 "$PYTHON_PATH" -u "$BASE_DIR/eval_v8_granular.py" \
            --checkpoint "$IDEA_DIR/runs/best.pt" \
            --test_dataset "$TEST_DATASET" \
            --ood_dataset "$OOD_DATASET" \
            --output_file "$IDEA_DIR/runs/granular_results.json" 2>&1 | tee -a "$IDEA_LOG"
        
        EVAL_EXIT_CODE=$?
        if [ $EVAL_EXIT_CODE -ne 0 ]; then
            echo "FAILED: Idea $i Evaluation crashed with exit code $EVAL_EXIT_CODE." | tee -a "$RUN_LOG"
        else
            echo "SUCCESS: Idea $i Evaluation completed." | tee -a "$RUN_LOG"
        fi
    fi
    
    cd "$BASE_DIR"
done

echo "100-Experiment Marathon Finished at $(date)" | tee -a "$RUN_LOG"
"$PYTHON_PATH" final_ranker.py | tee -a "$RUN_LOG"
