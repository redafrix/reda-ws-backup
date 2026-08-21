# Experiment 009: Canonical OOD400 TopK Secondary Symmetric Ablation (A=C=q95)

## Metadata
- **Experiment ID**: `EXP-010`
- **Role**: `canonical_ablation`
- **Thresholds**: $A = C = 0.6643207669258118$ (`seen_q95`), $M = 0.0$
- **Design**: Symmetric one-threshold controller requiring replacement candidate to return below the same alarm boundary.

## Results Summary
- **Episodes**: 400 / 400 (IDs `000000..000399`)
- **Successes**: 224 (56.00%)
- **Failures**: 176 (44.00%)
- **Delta vs Baseline**: **+2.25 pp (+9 episodes)**
- **Rescues (F -> S)**: 16
- **Regressions (S -> F)**: 7
- **Net Rescues**: +9
- **Total Interventions**: 30 (0.31% of decisions)
- **Episodes Touched**: 28 (7.00%)
- **Interventions per Net Rescue**: 3.33 (2.6x more efficient than C090)
