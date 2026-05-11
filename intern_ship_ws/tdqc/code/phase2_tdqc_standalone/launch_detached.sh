#!/bin/bash
cd "/media/redafrix/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone"
nohup ./auto_run_exp10.sh > experiments/v8_exp10_33d/runs/nohup_launch.log 2>&1 &
echo $! > experiments/v8_exp10_33d/runs/last_pid.txt
echo "Experiment 10 launched in background with PID $(cat experiments/v8_exp10_33d/runs/last_pid.txt)"
