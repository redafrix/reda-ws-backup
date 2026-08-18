# Canonical Master Experiment Index (2026-08-18)

This document is the cross-machine high-level index for experimental campaigns across **Bob**, **Sam**, **Dean**, and **Batman**. Detailed LIBERO history remains in `fiper_ws/experiment_catalog/`; corrected Isaac Sim details are in `isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md`.

---

## 1. Summary of Experimental Campaign Phases

| Phase | Timeframe | Machine(s) | Focus | State of the Art / Outcome |
|---|---|---|---|---|
| **Phase 1: TDQC & Marathon Ideas** | Feb – May 2026 | Batman / Bob | Uncertainty parameterization, softplus deltas, Time-Blind MLP | **Idea 166**: 86.88% Recall / 7.31% FPR (85% OOD Recall / 0.27% FPR) |
| **Phase 2: LIBERO-PRO & Online Interventions** | May – July 2026 | Bob / Sam / Dean | Multi-suite closed-loop intervention, selected-cap policies | Mixed protocol-dependent gains; canonical details in `fiper_ws/experiment_catalog/` |
| **Phase 3: Pi0.5 Reaching Fine-Tuning** | July 2026 | Dean | Flow-matching policy fine-tuning on 4.4k Franka rollouts | Stable loss 0.0034 at step 30,000 |
| **Phase 4: Superseded Isaac H1 Collection** | July – Aug 2026 | Dean | Initial Isaac risk migration under receding-H1 execution | Historical only; superseded for intended H10 protocol |
| **Phase 5: Corrected True-H10 Seen4000 + V1 Detector** | Aug 2026 | Dean | 4,000 seen episodes, TopK8 temporal detector | **3908/4000 success; val AUROC 0.93449 / AUPRC 0.84945** |
| **Phase 6: Corrected Locked OOD150 Detector** | Aug 2026 | Dean | Offline failure detection on exact locked membership | **Step AUROC 0.91655 / AUPRC 0.98003** |
| **Phase 7: Definitive Active OOD150 Controller** | Aug 17–18 2026 | Dean | Live 9-candidate argmin-on-alarm controller | **75/150 vs 72/150 historical; 11 rescues / 8 regressions; 57 replacements** |
| **Phase 8: HARD1000 Enrichment** | Aug 18 2026 onward | Dean | Additional failure-enriched true-H10 collection | Resumed safely from preserved episode 249; ongoing, not yet a final result |

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

### Campaign 7: Dean Round 0 Broad IsaacLab Collection — H1 Historical
- **Root:** `/mnt/ai/projects/simvla_isaac_risk_collection_20260730/outputs/final_seen_round_000_seed20260730/`
- **Execution Mode:** Receding Horizon H1 (`receding_h1`).
- **Historical Outcome:** 4,000 episodes (3,922 successes / 78 failures / 731,418 decisions).
- **Scientific Status:** `SUPERSEDED_H1_EXECUTION`.
- **Trust Verdict:** Mechanically useful historical evidence only; do not pool with corrected H10 results.

### Campaign 8: Dean Locked OOD-150 — H1 Historical
- **Root:** `/mnt/ai/projects/simvla_isaac_risk_collection_20260730/outputs/final_locked_ood150_seed20260728/`
- **Historical Outcome:** 150 episodes (68 successes / 82 failures; 60,262 decisions).
- **Historical Detector Metrics:** step AUROC 0.8194 / AUPRC 0.9612.
- **Scientific Status:** `SUPERSEDED_H1_EXECUTION` for the intended H10 protocol.
- **Trust Verdict:** Preserve as history; do not use as the corrected H10 headline.

### Campaign 9: Dean Corrected True-H10 Seen4000
- **Root:** `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_000_seed20260730/` and frozen dataset `frozen_datasets/isaac_seen_h10_topk8_v1`.
- **Execution Mode:** `chunk_h10`.
- **Outcome:** 4,000 episodes = 3,908 successes / 92 failures; 75,603 frozen decision rows.
- **Split:** train 2,800 (64 fail), validation 600 (14 fail), test 600 (14 fail).
- **Model:** `isaac_h10_topk8_temporal_v1`.
- **Model SHA:** `ad049519746913c4c2ce1a0b57fb32ad5c3395f5bce6841648c68cc94f862b38`.
- **Normalization SHA:** `78c934b33e0536bd7cb6b7e5b1962da32305729f602d8269d3a38422841ce050`.
- **Validation:** AUROC `0.9344901338018652`; AUPRC `0.8494462695568447`; best epoch 6.
- **Trust Verdict:** `AUDITED_PRIMARY`.

### Campaign 10: Dean Corrected Locked Historical OOD150 Detector
- **Root:** `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_locked_h10_ood150_seed20260728/`.
- **Membership:** 150 episodes = 72 successes / 78 failures; 5,887 decision rows.
- **Detector:** candidate-0/current-main V1 risk detector.
- **Step Metrics:** AUROC `0.9165517741946905`; AUPRC `0.9800307261831581`.
- **Selected Seen Threshold:** `best_val_f1 = 0.7990124225616455`.
- **At selected threshold:** 1.3889% success false alarms; 100% failure detection; Det@10 6.4103%; Det@25 39.7436%; Det@50 100%.
- **Trust Verdict:** `AUDITED_PRIMARY_OFFLINE`.
- **Interpretation:** detector evidence only; not nine independently supervised candidate outcomes.

### Campaign 11: Dean Definitive Active OOD150 Engineering Controller
- **Root:** `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/online_evals/isaac_ood150_engineering_cap090_v1/runs/definitive_full150`.
- **Evidence:** `prepared_experiments/dean_isaac_online_ood150_engineering_cap090_v1/`.
- **Controller:** `A=0.7990124225616455`, `C=0.9`, `M=0.0`, live 9-candidate argmin-on-alarm.
- **Provenance:** A is Seen-calibrated; C is selected from preserved live OOD-development 9-candidate decisions.
- **Membership:** exact 150/150; no missing, extra, or duplicate IDs; historical membership exact.
- **Historical Baseline:** 72/150 (48.0%).
- **Active:** **75/150 (50.0%)**, net **+3 / +2.0 pp**.
- **Paired:** 11 rescues / 8 regressions / 64 persisted success / 67 persisted failure.
- **Controller Activity:** 5,757 decisions; 3,327 alarms; 57 accepted replacements across 36 episodes; all eight alternative indices used.
- **Parity:** 0 selection mismatches; 0 execution mismatches; max action diff 0.0.
- **Trust Verdict:** `AUDITED_FINAL_ENGINEERING_EVAL`.
- **Important:** because C used OOD-development behavior, this is not a pristine untouched holdout for controller hyperparameter selection.

### Campaign 12: Dean HARD1000 True-H10 Enrichment
- **Root:** `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_002_seed20260804`.
- **Pre-OOD preserved state:** 249 committed episodes.
- **Resume audit:** original 249 identity snapshot SHA `12dcd6f6c3d24b0bb271879f3f75deb04774cc727252b9ba31dd120d75197bc9`; Stage 8 verified count 250 with new source ID 776.
- **Later sanity state:** 255/1000 with 255 unique source/global IDs and original 249 unchanged.
- **Trust Verdict:** `ACTIVE_COLLECTION_NOT_FINAL_RESULT`.

---

## 3. Isaac Invalidated / Excluded Evidence

- Commit `70327b4b31bde35c01fda29a807f9100b5295a62`: `INVALID_DO_NOT_USE` for historical nine-candidate alternative-score/pair calibration. Candidates 1–8 were reconstructed using candidate-0 diffusion-trace features because alternative traces were not archived. Correction commit: `86f5baf3281596df2305409499fc9e0c21d119ed`.
- Failed zero-intervention run using `C=q90_success=0.2370966076850891`: useful controller-development diagnostic only; no scientific active-controller outcome claim.
- Do not claim the Isaac V1 detector was trained on nine independently labeled counterfactual candidates.

## 4. Canonical Corrected Isaac Entry Point

See [`isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md`](isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md).

Final evidence commits on branch `experiment/dean-isaac-online-ood150-20260817`:

- `840d9b4ae44a9f83cd90d19ce663c7d5f3a7c442`
- `556aa351ba107d2f28d91582cc1b5f602f87fecf`
- `06d9d55c0c2a166719c4aaae0534cf973689f93e`
