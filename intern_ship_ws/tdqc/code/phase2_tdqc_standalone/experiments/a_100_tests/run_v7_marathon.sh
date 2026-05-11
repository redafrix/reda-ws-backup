#!/bin/bash
BASE_DIR="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests"
DATA="$BASE_DIR/../../data/v8_balanced/v8_train.pt"
TEST_DATA="$BASE_DIR/../../data/v8_balanced/v8_test.pt"
OOD_DATA="$BASE_DIR/../../data/v8_balanced/v8_unseen_obj_ood.pt"
LOG_DIR="$BASE_DIR/logs_marathon_v7"

mkdir -p "$LOG_DIR"

# User specified: 500 epochs, 100 patience
EPOCHS=500
PATIENCE=100

for i in {145..194}; do
    IDEA="idea_$i"
    echo "=== STARTING $IDEA ==="
    cd "$BASE_DIR/$IDEA"
    
    # Training
    if [ ! -f "runs/best.pt" ]; then
        echo "--- Training $IDEA ---"
        python3 -u train.py --dataset_path "$DATA" --output_dir runs --epochs $EPOCHS --patience $PATIENCE > "$LOG_DIR/$IDEA.log" 2>&1
    fi
    
    # Eval
    if [ -f "runs/best.pt" ]; then
        echo "--- Evaluating $IDEA ---"
        python3 -u -m phase2_tdqc.eval_tdqc --dataset_path "$TEST_DATA" --ckpt runs/best.pt >> "$LOG_DIR/$IDEA.log" 2>&1
        python3 -u -m phase2_tdqc.eval_tdqc --dataset_path "$OOD_DATA" --ckpt runs/best.pt >> "$LOG_DIR/$IDEA.log" 2>&1
    fi
done
