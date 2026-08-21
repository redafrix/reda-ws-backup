# Current Main Isaac Results & OOD400 Controller Campaign Evidence — 2026-08-21

> [!NOTE]
> **Scope Statement**: This document defines the authoritative canonical results for the Isaac Sim Franka Reaching benchmark under the locked `PROTO-ISAAC-3CM350-H10-V1` protocol, incorporating the Seen4904 main risk model training, OOD150 transfer evaluation, and the complete 400-episode OOD400 online controller campaign (Baseline, Primary C090, and Secondary Q95 Symmetric Ablation).

---

## 1. Executive Summary Table (Canonical OOD400 Campaign)

| Evaluation Stream | Controller Configuration | Episodes | Successes | Success Rate | Delta vs Baseline | Rescues (F $\rightarrow$ S) | Regressions (S $\rightarrow$ F) | Net Rescues | Total Interventions | Episodes Touched | Interventions / Net Rescue |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Canonical Baseline** | Uncontrolled ($c_0$ always) | 400 | 215 | **53.75%** | Baseline | N/A | N/A | N/A | 0 | 0 (0.00%) | N/A |
| **Primary Online TopK** | $A=0.879233, C=0.90, M=0.0$ | 400 | 225 | **56.25%** | **+2.50 pp (+10)** | 17 | 7 | **+10** | 87 (0.89%) | 67 (16.75%) | 8.70 |
| **Secondary Q95 Symmetric** | $A=C=0.664321, M=0.0$ | 400 | 224 | **56.00%** | **+2.25 pp (+9)** | 16 | 7 | **+9** | 30 (0.31%) | 28 (7.00%) | **3.33** |

---

## 2. Direct Cross-Controller Comparison: C090 Primary vs Q95 Symmetric

The secondary Q95 symmetric ablation was predeclared to evaluate a single-threshold symmetric design where alternative candidate replacement requires returning below the same alarm threshold ($A = C = 0.664321$).

### Episode Matrix (400 Matched Episodes)
- **Both Succeed**: 211 episodes
- **C090 Only Succeeds**: 14 episodes
- **Q95 Only Succeeds**: 13 episodes
- **Both Fail**: 162 episodes
- **Success Delta**: Q95 achieves 56.00% vs C090 achieving 56.25% ($-0.25\text{ pp}$, $-1\text{ net episode}$).

### Key Scientific Findings
1. **Primary Peak Success**: Primary C090 achieves the maximum absolute success rate (**56.25%**, $+2.50\text{ pp}$ over baseline), demonstrating that allowing higher-risk alternative substitutions up to $C=0.90$ rescues additional challenging trajectories.
2. **Symmetric Intervention Efficiency**: Q95 Symmetric reduces substitutions by **65.52%** (30 vs 87 interventions) and touches only 28 episodes (vs 67 for C090) while preserving nearly identical net gains ($+9$ vs $+10$ net rescues).
3. **Efficiency Multiplier**: Q95 requires only **3.33 interventions per net rescued episode** (compared to **8.70** for C090), representing a **2.6x improvement in intervention efficiency**.

---

## 3. Protocol & System Invariants

- **Task**: Franka reaching in Isaac Sim.
- **Success Distance**: $\le 0.030\text{ m}$ (3.0 cm) on first crossing $\implies$ immediate SUCCESS.
- **Timeout**: 350 control ticks (1,400 physics steps at 120 Hz) without success $\implies$ FAILURE.
- **Control Rate**: 30 Hz control rate, 120 Hz physics, decimation 4, Horizon $H=10$.
- **SimVLA Checkpoint**: `68b3e8dc73b0e0ee19e9b7e8d12d2d6ab24a341e824722ffeaebd1091ea2ebcd`
- **OOD400 Benchmark Manifest**: `264dae5a7de872e5aee0a9554f88adfe7af3d38b5a7e29fd7f9b3e0d1c10da41`
- **Risk Model Weights**: `00ad096a9ca38577366e992e1d7f8aa25b6f56f2f2bd7354abce1790baf890f1`
- **Feature Normalization**: `6fbd2b221c4490c975e3e1492c96a9e879a586f0b3a4c4eaf97ea05920960341`

---

## 4. Machine-Readable Catalog Links
All data is indexed in `isaac_experiment_map/catalog/`:
- `experiments.jsonl`: Comprehensive JSONL record of all 20 canonical, historical, and quarantined experiments.
- `experiment_results.csv`: Flat tabular summary.
- `metrics_long.csv`: Long/tidy format metric table.
- `paired_comparisons.csv`: Paired outcome matrices.
- `analysis_ready/ood400_episode_results.csv`: 1,200 episode outcome rows.
- `analysis_ready/ood400_decision_summary.csv`: 19,514 online decision queries.
