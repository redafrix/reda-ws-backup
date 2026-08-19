# Current Main Isaac Protocol & Model Lock

## 1. Current Main Dataset
- **CURRENT MAIN DATASET**: `isaac_seen4904_h10_3cm350_exact_v1`
- **ONE unified dataset**: 4,904 episodes (4,387 success, 517 failure, 96,813 rows).
- **TRAIN/VAL/TEST split**: Stratified by binary outcome label ONLY (seed 20260819).
- **source_campaign**: Provenance metadata only. Not used for split assignment, validation metrics, or official test sets.

## 2. Current Main Risk Model
- **CURRENT MAIN MODEL**: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2` (SeqRiskModel, width 128, 3 layers, 4 heads, pos_weight=4.3453, trained on 3,433 episodes).
- **CURRENT MAIN TEST**: Single locked test split (736 episodes: 658 success, 78 failure).

## 3. Current Task Protocol
- Distance threshold: `0.030 m` (3.0 cm)
- Control rate: `30 Hz`
- Maximum horizon: `350 control ticks` (11.6667 s)
- Execution: `H10` (10 actions per query, `decision_index <= 34`)
- **NO DWELL / NO SETTLE TIME**: First control tick where `tcp_target_distance_m <= 0.030` terminates immediately as **SUCCESS** (0).
- If tick 350 is reached without entering $\le 0.030$ m, the episode terminates as **FAILURE/TIMEOUT** (1).

## 4. Superseded Models & History
- Previous source-stratified training commit (`ac305eef...` / `isaac_seen4904_h10_topk8_temporal_3cm350_v1`): **SUPERSEDED**.
- Old 2cm / 600-tick / dwell results: **HISTORICAL ONLY**.
