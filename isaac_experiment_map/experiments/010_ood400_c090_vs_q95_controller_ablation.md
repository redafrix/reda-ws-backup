# Experiment 010: OOD400 Controller Comparative Analysis: C090 vs Q95 Symmetric

## Metadata
- **Experiment ID**: `EXP-011`
- **Role**: `canonical_ablation`
- **Purpose**: Direct paired comparison between sparse emergency controller (C090) and symmetric efficiency controller (Q95).

## Paired Comparison Matrix (400 episodes)
- **Both Succeed**: 211 episodes
- **C090 Only Succeeds**: 14 episodes
- **Q95 Only Succeeds**: 13 episodes
- **Both Fail**: 162 episodes
- **Success Delta**: Q95 achieves 56.00% vs C090 achieving 56.25% (-0.25 pp, -1 episode).

## Key Conclusions
1. Primary C090 provides maximum absolute task success (56.25% / +2.50 pp).
2. Q95 Symmetric provides 2.6x higher intervention efficiency (3.33 interventions/rescue vs 8.70 for C090) with 65.5% fewer candidate substitutions.
