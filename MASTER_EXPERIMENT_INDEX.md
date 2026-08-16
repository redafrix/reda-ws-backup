# Canonical Master Experiment Index (2026-08-16)

This document is the single source of truth for all experimental campaigns across **Bob**, **Sam**, **Dean**, and **Batman**. Every entry records its physical parameters, trust status, and role in the U-VOWEL publication.

---

## 1. Summary of Experimental Campaign Phases

| Phase | Timeframe | Machine(s) | Focus | State of the Art / Outcome |
|---|---|---|---|---|
| **Phase 1: TDQC & Marathon Ideas** | Feb – May 2026 | Batman / Bob | Uncertainty parameterization, softplus deltas, Time-Blind MLP | **Idea 166**: 86.88% Recall / 7.31% FPR (85% OOD Recall / 0.27% FPR) |
| **Phase 2: LIBERO-PRO & Online Interventions** | May – July 2026 | Bob / Sam | Multi-suite closed-loop intervention, fallback policies | Robust multi-task success gains across Spatial, Goal, Object suites |
| **Phase 3: Pi0.5 Reaching Fine-Tuning** | July 2026 | Dean | Flow matching policy fine-tuning on 4.4k Franka rollouts | Stable loss 0.0034 at step 30,000 |
| **Phase 4: Round 0 Broad IsaacLab Collection** | July – Aug 2026 | Dean | 4,000-episode seen collection, dual-threshold resolution | **98.05% Seen Success**, 2cm vs 4cm precision near-miss breakdown |
| **Phase 5: TopK8 SeqRiskModel & Locked OOD-150** | Aug 2026 | Dean | Temporal transformer risk head evaluation | **OOD Step AUROC: 0.8194, AUPRC: 0.9612** |
| **Phase 6: True-H10 Execution Migration** | Aug 13–16 2026 | Dean | Fresh chunk_h10 execution workspace | **3,737 / 4,000 committed episodes (93.43%)**, 97.7% success |

---

## 2. Detailed Campaign Records & Trust Status

### Campaign 1: Bob In-Distribution Main Campaign (H10)
- **Root:** `/media/redafrix/My Passport1/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608`
- **Suite:** `libero_goal_object` (Tasks 3, 6, 8)
- **Policies:** `original_simvla`, `modified_simvla`, `original_h10_risk_base`, `modified_h10_risk_topk8`
- **Threshold:** `q95` (conformal ~0.6155)
- **Status:** Tasks 3 & 6 complete; Task 8 killed by supervisor.
- **Trust Verdict:** Tasks 3 & 6: `TRUST` | Task 8: `DO_NOT_TRUST`.

### Campaign 2: Bob In-Distribution Task 3 Aggressive TopK8
- **Root:** `/media/redafrix/My Passport1/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608`
- **Suite:** `libero_goal_object` (Task 3)
- **Threshold:** `0.3` (aggressive manual override)
- **Trust Verdict:** `TRUST` (mechanically valid, in-distribution).

### Campaign 3: Bob In-Distribution Task 6 Old Detector Aggressive
- **Root:** `/media/redafrix/My Passport1/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608`
- **Suite:** `libero_goal_object` (Task 6)
- **Trust Verdict:** `TRUST` (ablation, mechanically valid).

### Campaign 4: Bob Heldout Hard Task 8
- **Root:** `/media/redafrix/My Passport1/reda_ws/fiper_ws/trash/h10_heldout_hard_task8_20260608`
- **Suite:** `libero_goal_object` (Task 8)
- **Trust Verdict:** `TRUST`.

### Campaign 5: Bob Official OOD Proof Campaign
- **Root:** `/media/redafrix/My Passport1/reda_ws/fiper_ws/trash/h10_goal_object_ood_proof_20260608`
- **Suite:** `libero_goal_object` OOD tasks
- **Trust Verdict:** `TRUST`.

### Campaign 6: Dean Pi0.5 Reaching Pose v1 Fine-Tuning (30k Steps)
- **Root:** `/mnt/ai/pi05/training/reaching_pose_v1_4400_pi05_fullpose_v3/`
- **Architecture:** Pi0.5 Flow Matching Backbone
- **Output:** `production_v1_loss_0_30000_final.png`
- **Trust Verdict:** `TRUST` (valid training progression).

### Campaign 7: Dean Round 0 Broad IsaacLab Collection (4,000 Episodes)
- **Root:** `/mnt/ai/projects/simvla_isaac_risk_collection_20260730/outputs/final_seen_round_000_seed20260730/`
- **Execution Mode:** Receding Horizon H1 (`receding_h1`)
- **Outcome:** 4,000 episodes (3,922 successes / 78 failures / 731,418 decisions).
- **Audit:** `exhaustive_audit.json` (PASS), `ROUND_ROWS_COMPRESSED` (PASS).
- **Scientific Status:** `SUPERSEDED_H1_EXECUTION` (historically vital; superceded by chunk H10 for action chunking parity).

### Campaign 8: Dean Locked OOD-150 Risk Evaluation
- **Root:** `/mnt/ai/projects/simvla_isaac_risk_collection_20260730/outputs/final_locked_ood150_seed20260728/`
- **Outcome:** 150 episodes (68 successes, 82 genuine failures/timeouts, 60,262 decisions).
- **Model Evaluated:** Round-0 TopK8 `SeqRiskModel`
- **Results:** **OOD Step AUROC: 0.8194, OOD Step AUPRC: 0.9612**.
- **Trust Verdict:** `TRUST` (official benchmark evaluation).

### Campaign 9: Dean Fresh True-H10 Execution Collection (Active)
- **Root:** `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_000_seed20260730/`
- **Execution Mode:** True Chunk H10 (`chunk_h10`)
- **Current Progress:** 3,737 / 4,000 committed episodes (97.70% success / 2.30% failure).
- **Trust Verdict:** `ACTIVE_PRIMARY`.
