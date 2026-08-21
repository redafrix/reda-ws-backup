# Experiment 008: Canonical OOD400 TopK Primary Online Controller (A=q99, C=0.90)

## Metadata
- **Experiment ID**: `EXP-009`
- **Role**: `canonical_primary`
- **Thresholds**: $A = 0.8792325258255005$ (`q99 success`), $C = 0.90$, $M = 0.0$
- **Risk Model**: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2` (`00ad096a9ca38577366e992e1d7f8aa25b6f56f2f2bd7354abce1790baf890f1`)

## Results Summary
- **Episodes**: 400 / 400 (IDs `000000..000399`)
- **Successes**: 225 (56.25%)
- **Failures**: 175 (43.75%)
- **Delta vs Baseline**: **+2.50 pp (+10 episodes)**
- **Rescues (F -> S)**: 17
- **Regressions (S -> F)**: 7
- **Net Rescues**: +10
- **Total Interventions**: 87 (0.89% of decisions)
- **Episodes Touched**: 67 (16.75%)
