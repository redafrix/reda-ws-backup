# Current Main Isaac Protocol & Model Lock

## 1. Protocol Definition
- **CURRENT MAIN ISAAC SOURCE**: `isaac_seen4904_h10_3cm350_exact_v1`
- **CURRENT MAIN SUCCESS PROTOCOL**:
  - Distance threshold: `0.030 m` (3.0 cm)
  - Control rate: `30 Hz`
  - Maximum horizon: `350 control ticks` (11.6667 s)
  - H10 execution: 10 actions per query (maximum 35 decision rows, `decision_index <= 34`)
  - **NO DWELL / NO SETTLE TIME**: First control tick where `tcp_target_distance_m <= 0.030` terminates immediately as **SUCCESS**.
  - If tick 350 is reached without entering $\le 0.030$ m, the episode terminates as **FAILURE/TIMEOUT**.
- **CURRENT MAIN RISK MODEL**: `isaac_seen4904_h10_topk8_temporal_3cm350_v1` (SeqRiskModel, 128 width, 3 layers, 4 heads, pos_weight=4.3443, trained on 4,904 exact episodes).

## 2. Historical Context & Future Compatibility
- **OLD 2cm / 600-tick / dwell results**: HISTORICAL ONLY.
- **Future Evaluation Compatibility Rule**:
  - Existing old-protocol evaluations (such as legacy OOD150/controller evaluations) remain preserved as historical benchmarks.
  - Any future Isaac evaluation (online, OOD150, OOD400, or real-time) evaluating this new model must use the exact current 3cm / 350-tick / no-dwell binary reaching protocol.
