# Frozen Offline Derived Dataset: isaac_seen5000_h10_derived_3cm350_v1

## Overview
This directory freezes the offline derived 5,000-episode source dataset combining 4,000 Seen Round-0 episodes and 1,000 Hard Round-2 episodes under the 3.0 cm / 350-control-tick protocol prefix (`decision_index <= 34`).

## Key Dataset Statistics
- **Total Episodes**: 5,000
- **Seen Episodes**: 4,000
- **Hard Episodes**: 1,000
- **Total Retained Rows**: 100,173 (Seen: 73,303, Hard: 26,870)
- **Exact Labels**: 4,387 success, 517 failure, 96 ambiguous
- **Heuristic Labels**: 4,482 success, 518 failure
- **Feature Parity**: Checked 73,303 rows against frozen Seen4000 V1 dataset (`max_abs_diff = 0.0` across history, action, static).

## Source Datasets on Dean
- Seen4000: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_000_seed20260730`
- Hard1000: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_002_seed20260804`
- Frozen Derived Target: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/isaac_seen5000_h10_derived_3cm350_v1`
