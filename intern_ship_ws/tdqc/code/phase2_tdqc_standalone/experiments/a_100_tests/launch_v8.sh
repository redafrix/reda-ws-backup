#!/bin/bash
# Marathon V8: Foreground Execution

BASE_DIR="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests"
LOG_DIR="$BASE_DIR/logs_marathon_v8"
mkdir -p "$LOG_DIR"

DATA_TRAIN="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_train.pt"
DATA_TEST="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_test.pt"
DATA_OOD="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_balanced/v8_unseen_obj_ood.pt"

# Only kill OLD training processes, not the current launcher
pkill -f train_tdqc.py || true

for i in {200..249}
do
    IDEA="idea_$i"
    if [ ! -d "$BASE_DIR/$IDEA" ]; then continue; fi
    
    echo "--------------------------------------------------"
    echo "STARTING $IDEA"
    echo "--------------------------------------------------"
    
    cd "$BASE_DIR/$IDEA"
    export PYTHONPATH=$PYTHONPATH:.
    
    # Run in foreground, outputting to console AND log
    PYTHONUNBUFFERED=1 python3 phase2_tdqc/train_tdqc.py --dataset_path "$DATA_TRAIN" --output_dir runs 2>&1 | tee "$LOG_DIR/${IDEA}_train.log"
    
    if [ -f "runs/best.pt" ]; then
        echo "$IDEA: Evaluation Starting..."
        python3 ../comprehensive_eval.py --dataset_path "$DATA_TEST" --ckpt runs/best.pt | tee -a "$LOG_DIR/${IDEA}_eval_test.log"
        python3 ../comprehensive_eval.py --dataset_path "$DATA_OOD" --ckpt runs/best.pt | tee -a "$LOG_DIR/${IDEA}_eval_ood.log"
    else
        echo "$IDEA: FAILED (No checkpoint found)"
    fi
done
echo "Marathon V8 Complete!"
