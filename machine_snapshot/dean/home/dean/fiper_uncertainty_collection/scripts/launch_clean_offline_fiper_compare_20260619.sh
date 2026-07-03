#!/usr/bin/env bash
set -euo pipefail
cd /home/dean/fiper_uncertainty_collection
/home/redafrix/miniconda3/envs/simvla/bin/python -u scripts/run_offline_original_fiper_vs_v2018_clean_compare.py   --refs-dir /home/dean/fiper_uncertainty_collection/experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs   --base-dir /home/dean/fiper_uncertainty_collection   --output-dir /home/dean/fiper_uncertainty_collection/experiments/clean_offline_original_fiper_vs_v2018_fold00_20260619   --device cuda   --seed 42   --rnd-epochs 20   --batch-size 384   --v2018-max-epochs 120   --v2018-patience 18   --force   2>&1 | tee /home/dean/fiper_uncertainty_collection/logs/clean_offline_original_fiper_vs_v2018_fold00_20260619/run.log
