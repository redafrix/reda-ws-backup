# Master Experiment Index

Updated: 2026-06-19 by Codex full workspace audit plus OpenVLA experiment indexing.

This is the canonical reference for every campaign that produced results we cite or might cite. Each entry includes the trust verdict from the forensic audit where applicable.

---

## Online Evaluation Campaigns (Bob / pcrobot)

All campaigns below ran on Bob (`PCROBOTUBUNTU02`) using the SimVLA + LIBERO-PRO simulation stack.

### Campaign 1: In-Distribution Main Campaign (H10)
| Property | Value |
| :--- | :--- |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608` |
| **Date** | 2026-06-08 |
| **Suite** | `libero_goal_object` |
| **Tasks** | 3, 6, 8 |
| **Policies** | `original_simvla`, `modified_simvla`, `original_h10_risk_base`, `modified_h10_risk_topk8` |
| **Threshold** | `q95` (conformal, ~0.6155) |
| **Episodes per policy per task** | 100 (2 shards × 50) |
| **Status** | Task 3/6: **complete**. Task 8: **incomplete** (killed by supervisor). |
| **Trust** | Task 3/6 conservative: **TRUST**. Task 8: **DO_NOT_TRUST**. |

### Campaign 2: In-Distribution Task 3 Aggressive TopK8
| Property | Value |
| :--- | :--- |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608` |
| **Date** | 2026-06-08 |
| **Suite** | `libero_goal_object` |
| **Tasks** | 3 (also contains Task 6 aggressive runs) |
| **Policies** | `modified_h10_risk_topk8` |
| **Threshold** | `0.3` (aggressive manual override) |
| **Episodes** | 100 per task (2 shards × 50) |
| **Status** | **Complete** |
| **Trust** | **TRUST** (mechanically valid, in-distribution) |

### Campaign 3: In-Distribution Task 6 Old Detector Aggressive
| Property | Value |
| :--- | :--- |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608` |
| **Date** | 2026-06-08 |
| **Suite** | `libero_goal_object` |
| **Tasks** | 6 |
| **Policies** | `modified_h10_risk_topk8` (loaded old Dean detector, hash `0ea8e943...`) |
| **Threshold** | `0.3` (aggressive) |
| **Episodes** | 100 (2 shards × 50) |
| **Status** | **Complete** |
| **Trust** | **TRUST** (ablation, mechanically valid) |

### Campaign 4: OOD Goal-Swap Production
| Property | Value |
| :--- | :--- |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_ood_goal_object_and_swap_20260608` |
| **Date** | 2026-06-08 |
| **Suite** | `libero_goal_swap` |
| **Tasks** | 3, 6, 8 |
| **Policies** | `original_simvla`, `modified_simvla`, `risk_topk8` |
| **Threshold** | `0.3` (aggressive) |
| **Episodes** | 100 per policy per task (900 total) |
| **Status** | **Complete** |
| **Trust** | **DO_NOT_TRUST** (net negative: -2 successes) |

### Campaign 5: Invalid OOD Goal-Object Sweep (Diagnostic)
| Property | Value |
| :--- | :--- |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_20260609` |
| **Date** | 2026-06-09 |
| **Suite** | `libero_goal_object_ood` |
| **Tasks** | 0 (Aborted) |
| **Policies** | `original_simvla`, `modified_simvla`, `risk_topk8` |
| **Threshold** | `q95` (accidental default fallback) |
| **Status** | **Aborted & Invalidated** (SSH disconnect, incorrect threshold configuration) |
| **Trust** | **DO_NOT_TRUST** (diagnostic only) |

### Campaign 6: Corrected 10ep OOD Goal-Object Sweep (Aggressive-Fixed)
| Property | Value |
| :--- | :--- |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609` |
| **Date** | 2026-06-09 |
| **Suite** | `libero_goal_object_ood` |
| **Tasks** | 18 tasks (0-17) |
| **Policies** | `original_simvla`, `modified_simvla`, `modified_h10_risk_topk8` |
| **Threshold** | `0.3` (aggressive fixed controls) |
| **Episodes** | 10 per policy per task (540 total) |
| **Status** | **Complete** |
| **Trust** | **TRUST** (mechanically valid, but weak statistical signal due to N=10) |

### Campaign 7: 100ep OOD Goal-Object Sweep (Aggressive-Fixed)
| Property | Value |
| :--- | :--- |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609` |
| **Date** | 2026-06-09 |
| **Suite** | `libero_goal_object_ood` |
| **Tasks** | 18 tasks (0-17) |
| **Policies** | `original_simvla`, `modified_simvla`, `risk_topk8` |
| **Threshold** | `0.3` (aggressive fixed controls) |
| **Episodes** | 100 per policy per task (5,400 total) |
| **Status** | **Complete** |
| **Result** | original 1,668/1,800 (92.67%), modified 1,718/1,800 (95.44%), risk_topk8 1,713/1,800 (95.17%) |
| **Trust** | **TRUST** (mechanically valid, but net negative vs modified baseline: 24 rescues / 29 regressions, -5) |

### Campaign 8: 100ep OOD Goal-Object Sweep (Threshold 0.5)
| Property | Value |
| :--- | :--- |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_0.5_20260610` |
| **Date** | 2026-06-10 |
| **Suite** | `libero_goal_object_ood` |
| **Tasks** | 18 tasks (0-17) |
| **Policies** | `modified_h10_risk_topk8` only, compared against Campaign 7 baselines using the same seeds 10-109 |
| **Threshold** | `0.5` |
| **Episodes** | 100 per task (1,800 total) |
| **Status** | **Complete** |
| **Result** | risk_topk8 1,718/1,800 (95.44%), paired vs modified baseline 21 rescues / 21 regressions, net 0 |
| **Trust** | **TRUST** (mechanically valid; reduced regressions but did not outperform modified baseline globally) |

### Campaign 9: 100ep OOD Goal-Object Sweep (q95 Threshold)
| Property | Value |
| :--- | :--- |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_q95_20260610` |
| **Date** | 2026-06-10 |
| **Suite** | `libero_goal_object_ood` |
| **Tasks** | 18 tasks (0-17) |
| **Policies** | `modified_h10_risk_topk8` only, compared against Campaign 7 baselines after completion |
| **Threshold** | `q95` / `0.6155413389205933` |
| **Episodes** | 100 per task target (1,800 total target) |
| **Status** | **Complete** |
| **Result** | q95 risk 1,710/1,800 (95.00%), paired vs modified baseline 10 rescues / 18 regressions, net -8 |
| **Trust** | **TRUST** (mechanically valid, net negative vs modified baseline) |

---

## Online Evaluation Campaigns (Sam)

### Sam V2 Adaptive-Horizon Diagnostics (OOD Goal-Object, N=10)
| Variant | Root | Policies | Result vs modified SimVLA baseline | Trust |
| :--- | :--- | :--- | :--- | :--- |
| **V2 flawed diagnostic** | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2_adaptive_horizon_20260610` | modified baseline + flawed adaptive horizon | Invalidated: omitted ACE candidate generation and collapsed to H1 on early OOD states | **DO_NOT_TRUST** |
| **V2B feature-preserving H1** | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2b_feature_preserving_adaptive_horizon_20260610` | modified baseline + q95 adaptive H1/H10 | baseline 171/180 (95.00%), V2B 167/180 (92.78%), 2 rescues / 6 regressions, net -4 | **TRUST diagnostic, HURTS** |
| **V2C feature-preserving H5** | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2c_h5_adaptive_horizon_20260610` | q95 adaptive H5/H10 only | V2C 169/180 (93.89%), 1 rescue / 3 regressions, net -2 | **TRUST diagnostic, HURTS** |
| **V2D commit-gate** | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_topk8_v2d_commit_gate_20260610` | q95 first5/tail5 commit gate only | V2D 168/180 (93.33%), 6 rescues / 9 regressions, net -3 | **TRUST diagnostic, HURTS** |

Meaning: all three corrected adaptive-horizon ideas were mechanically valid diagnostics, but none outperformed the fixed H10 modified SimVLA baseline on the 18-task OOD goal-object 10-seed benchmark.


## Online Evaluation Campaigns (Dean)

### Canonical 4-Policy Comparison (Dean, Task 0)
| Property | Value |
| :--- | :--- |
| **Root** | `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604` |
| **Date** | 2026-06-04 |
| **Suite** | `libero_object_object` Task 0 |
| **Policies** | original_simvla (14%), modified_simvla (22%), risk_base (25%), risk_topk8 (20%) |
| **Episodes** | 100 per policy |
| **Status** | **Complete** |
| **Trust** | **TRUST** (historically audited) |

### Dean Three-Policy Runs (Various Tasks)
| Run | Task | Policies | Episodes | Status |
| :--- | :--- | :--- | :--- | :--- |
| `dean_three_policy_seen_object_task7_100eps_20260602` | Task 7 (seen) | simvla, risk_base, risk_topk8 | 100 each | Complete |
| `dean_three_policy_unseen_object_task8_100eps_20260602` | Task 8 (unseen) | simvla, risk_base, risk_topk8 | 100 each | Complete |
| `dean_three_policy_seen_object_task0_100eps_20260603` | Task 0 (seen) | simvla, risk_topk8 | 100 each | Complete |
| `conservative_topk8_midrange_pilot_20260605_dean_task8` | Task 8 | simvla, topk8 (protective), topk8 (balanced) | Partial | Pilot |
| `tuned_topk8_pilot_20260605_dean_task8` | Task 8 | topk8 (moderate), topk8 (active) | Partial | Pilot |

### Dean OOD Selected-Cap Gate Diagnostic (10ep Complete)
| Property | Value |
| :--- | :--- |
| **Root** | `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_10ep_20260610` |
| **Date** | 2026-06-10 |
| **Suite** | `libero_goal_object_ood` using generated `_temp` BDDL fallback copied from Bob/Sam |
| **Tasks** | 18 tasks (0-17) |
| **Policies** | `modified_simvla` fixed H10 baseline vs `risk_topk8` selected-cap gate |
| **Gate** | main threshold 0.3, min margin 0.02, strong margin 0.05, `selection_max_selected_score=0.4` |
| **Seeds** | 200-209, paired across both policies |
| **Status** | **Complete** |
| **Result** | modified baseline 170/180 (94.44%), selected-cap risk 176/180 (97.78%), 7 rescues / 1 regression, net +6 |
| **Trust** | **TRUST diagnostic** (mechanically valid N=10 per task; promising but requires 100ep confirmation) |

### Dean OOD Selected-Cap Gate 100ep Confirmation (Complete)
| Property | Value |
| :--- | :--- |
| **Root** | `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_100ep_20260610` |
| **Date** | 2026-06-10 |
| **Suite** | `libero_goal_object_ood` using generated `_temp` BDDL fallback copied from Bob/Sam |
| **Tasks** | 18 tasks (0-17) |
| **Policies** | `modified_simvla` fixed H10 baseline vs `risk_topk8` selected-cap gate |
| **Gate** | main threshold 0.3, min margin 0.02, strong margin 0.05, `selection_max_selected_score=0.4` |
| **Seeds** | 300-399, paired across both policies |
| **Status** | **Complete** |
| **Result** | modified 1,726/1,800 (95.89%) vs selected-cap 1,741/1,800 (96.72%); paired 38 rescues / 23 regressions, net +15 |
| **Forensic audit** | `source_reports/dean/reports/DEAN_SELECTED_CAP_FINAL_ANALYSIS_20260611.md` |
| **Trust** | **TRUST** mechanically valid and globally positive on this OOD suite |

### Dean OOD Selected-Cap Delay30 100ep Replication (Complete)
| Property | Value |
| :--- | :--- |
| **Root** | `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_delay30_100ep_20260611` |
| **Date** | 2026-06-11 |
| **Suite** | `libero_goal_object_ood` using the same generated OOD assets |
| **Tasks** | 18 tasks (0-17) |
| **Policies** | `modified_simvla` fixed H10 baseline vs `risk_topk8` selected-cap gate with delayed interventions |
| **Gate** | same selected-cap gate plus `selection_min_timestep=30` |
| **Seeds** | 400-499, paired across both policies and disjoint from prior OOD online sweeps |
| **Status** | **Complete** |
| **Result** | modified 1,721/1,800 (95.61%) vs selected-cap delay30 1,718/1,800 (95.44%); paired 19 rescues / 22 regressions, net -3 |
| **Forensic audit** | `source_reports/dean/reports/DEAN_SELECTED_CAP_DELAY30_FINAL_ANALYSIS_20260612.md` |
| **Purpose** | Test whether suppressing replacements before query 3 reduces regressions while preserving rescues |
| **Trust** | **TRUST mechanically valid, but negative vs paired baseline** |

### Dean OOD Selected-Cap Margin 0.10 Diagnostic (Complete)
| Property | Value |
| :--- | :--- |
| **Root** | `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_m10_10ep_20260610` |
| **Date** | 2026-06-10 |
| **Suite** | `libero_goal_object_ood` using generated `_temp` BDDL fallback copied from Bob/Sam |
| **Tasks** | 18 tasks (0-17) |
| **Policies** | `risk_topk8` selected-cap margin-0.10 only, compared after completion against the existing 10ep modified SimVLA baseline from `selected_cap_t03_c04_10ep_20260610` |
| **Gate** | main threshold 0.3, min margin 0.10, strong margin 0.05, `selection_max_selected_score=0.4` |
| **Seeds** | 200-209, matching the 10ep selected-cap diagnostic baseline |
| **Status** | **Complete** |
| **Result** | m10 175/180 vs modified baseline 170/180 and m02 selected-cap 176/180. m10 had 5 rescues / 0 regressions vs baseline, but was net -1 vs m02. |
| **Purpose** | Test whether a larger required risk reduction lowers regressions while preserving rescues. |
| **Trust** | **TRUST diagnostic** (mechanically valid conservative ablation; not selected for scaling because it underperformed m02 by 1 success) |

---

## Historical Campaigns (Pre-H10, Bob)

### Bob OOD Selected-Cap 10ep Comparison (Complete)
| Property | Value |
| :--- | :--- |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_selected_cap_10ep_comparison_20260611` |
| **Date** | 2026-06-11 |
| **Suite** | `libero_goal_object_ood` |
| **Tasks** | 18 tasks (0-17) |
| **Seeds** | 0-9, matching the corrected Bob 10ep OOD baseline sweep |
| **New Policies** | `risk_topk8_selected_cap`, `risk_topk8_selected_cap_delay30` |
| **Execution** | Sequential, one job at a time, tmux `bob_selected_cap_only_10ep_20260611`; `threshold_05/q95` partial files in this root are diagnostic only and should be ignored |
| **Comparison Sources** | Existing Bob corrected 10ep OOD sweep provides Original SimVLA, Modified SimVLA, and threshold 0.3 baselines |
| **Status** | **Complete** |
| **Result** | selected-cap 169/180 (93.89%), paired +1 vs Modified; selected-cap delay30 167/180 (92.78%), paired -1 vs Modified |
| **Trust** | **TRUST diagnostic; selected-cap did not beat TopK8 threshold 0.3 on the same seeds** |

---

### Bob OOD Selected-Cap 100ep Comparison (Complete)
| Property | Value |
| :--- | :--- |
| **Root** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_selected_cap_100ep_comparison_20260611` |
| **Date** | 2026-06-11 |
| **Suite** | `libero_goal_object_ood` |
| **Tasks** | 18 tasks (0-17) |
| **Seeds** | 10-109, matching the existing Bob 100ep OOD baseline campaign |
| **New Policies** | `risk_topk8_selected_cap`, `risk_topk8_selected_cap_delay30` |
| **Comparison Sources** | Existing Bob 100ep OOD campaign provides Original SimVLA, Modified SimVLA, and TopK8 threshold 0.3 |
| **Execution** | Sequential, one job at a time, tmux `bob_selected_cap_only_100ep_20260611` |
| **Status** | **Complete** |
| **Result** | selected-cap 1,713/1,800 (95.17%), paired -5 vs Modified; selected-cap delay30 1,723/1,800 (95.72%), paired +5 vs Modified |
| **Forensic audit** | `source_reports/bob/reports/BOB_SELECTED_CAP_100EP_FINAL_ANALYSIS_20260612.md` |
| **Trust** | **TRUST mechanically valid; delay30 is small positive on Bob but not reproduced on Dean** |

---

### Sam Timeout800 OOD Selected-Cap 100ep Comparison (Complete)
| Property | Value |
| :--- | :--- |
| **Root** | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_selected_cap_timeout800_20260615` |
| **Date** | 2026-06-15 to 2026-06-16 |
| **Suite** | `libero_goal_object_ood` using generated OOD assets |
| **Tasks** | 18 tasks (0-17) |
| **Seeds** | 10-109, paired across all three policies |
| **Policies** | `original_simvla`, `modified_simvla`, `risk_topk8_selected_cap` |
| **Execution** | H10 with `max_steps=800`; sequential full sweep on Sam |
| **Gate** | selected-cap: main threshold 0.3, min margin 0.02, strong margin 0.05, selected risk cap 0.4 |
| **Status** | **Complete** |
| **Result** | Original 1,716/1,800 (95.33%); Modified 1,744/1,800 (96.89%); selected-cap 1,754/1,800 (97.44%). Paired selected-cap: +38 vs Original and +10 vs Modified. |
| **Forensic audit** | `source_reports/sam/reports/SAM_TIMEOUT800_SELECTED_CAP_100EP_FINAL_ANALYSIS_20260616.md` |
| **Trust** | **TRUST mechanically valid; positive result under extended 800-step timeout, not directly comparable to 300-step runs** |

---

### Goal-Object Chunk10 Diagnostic (Bob, 2026-06-05)
| Property | Value |
| :--- | :--- |
| **Roots** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/goal_object_modified_simvla_chunk10_100_20260605`; `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/goal_object_official_simvla_chunk10_100_20260605` |
| **Suite** | `libero_goal_object` exact reproduction bundle, tasks 0-9, init rows 0-9 |
| **Policies** | modified SimVLA `ckpt-60000`; official/original SimVLA `YuankaiLuo_SimVLA-LIBERO` |
| **Execution** | Chunk10 open-loop, no risk detector, no ACE candidates, no uncertainty features |
| **Episodes** | 100 per policy |
| **Result** | modified 80/100, official 78/100; paired modified vs official 8 rescues / 6 regressions, net +2 |
| **Trust** | **TRUST diagnostic** (mechanically valid launch and raw JSONL verified; historical, not risk-aware evidence) |

### Four-Task Campaign (Bob, 2026-05-29 to 2026-06-01)
| Property | Value |
| :--- | :--- |
| **Tasks** | Task 7 (seen), Task 8 (OOD), fold00 Task 2 (seen butter), fold00 Task 0 (unseen alphabet soup) |
| **Policies** | modified_simvla vs modified_simvla + base risk detector |
| **Total Episodes** | 1,881 paired |
| **Net Gain** | +56 net successes (+3.0 pts) |
| **Status** | **Complete** |
| **Trust** | **TRUST** (historically audited, but pre-H10 execution mode) |

> [!WARNING]
> **Labeling Correction:** Older reports incorrectly called the no-risk policy "vanilla SimVLA." Both sides used the modified `ckpt-60000` checkpoint. The comparison is modified SimVLA vs modified SimVLA + base risk detector, **not** original vs modified.

---

## Offline Detector Training Campaigns

### OpenVLA-OFT Offline Risk Models (Bob, 2026-06-17 to 2026-06-19)

See [OPENVLA_EXPERIMENT_MAP_20260619.md](OPENVLA_EXPERIMENT_MAP_20260619.md) for the complete OpenVLA workspace map. These experiments are not SimVLA/FIPER detector runs: OpenVLA has native horizon 8, no ACE uncertainty candidate generator, and uses OpenVLA action/proprio/history features.

| Experiment | Training data | Test data | Key result | Status |
| :--- | :--- | :--- | :--- | :--- |
| `openvla_old6000_risk_base_20260617` | 6,009 old plain `libero_goal` episodes | old heldout split | 800-step model: AUROC 0.9953, AUPRC 0.9909, best-F1 threshold 0.7100 | Complete |
| `openvla_old6000_risk_base_20260617_cut300` | same old plain `libero_goal` data, failed episodes capped at 300 | old heldout split | 300-step model: best-F1 threshold 0.8700; lower false alarms in-domain, weaker OOD transfer | Complete |
| `openvla_final1890_risk_20260618` | final cleaned `libero_goal_object` dataset, 1,890 episodes | internal split | Current final OpenVLA goal-object risk model; online runner uses `model_300steps.pt` and validation Q95 threshold 0.8049 | Current |
| `openvla_old6000_to_goal_object_ood_20260619` | old plain-goal 800-step model | old heldout plus full final goal-object dataset | Goal-object OOD at threshold 0.7100: AUROC 0.8302, 15.63% episode false alarms, 100% failure detected | Complete |
| `openvla_old6000_cut300_to_goal_object_ood_20260619` | old plain-goal 300-step model | old heldout plus full final goal-object dataset | Goal-object OOD at threshold 0.8700: AUROC 0.6782, 22.11% episode false alarms, 84.50% failure detected | Complete |
| `openvla_risk_input_forensic_audit_20260619` | checkpoint/code audit | final1890 + old6000 Transformer checkpoints | Transformer risk heads have no explicit task id or timestep inputs: `static_dim=43`, `history_dim=21`; old MLP/GRU baselines had leaked 25D task/timestep inputs but are not used online | Complete |
| `openvla_focused_horizon_diagnostic_20260619` | online focused diagnostic | task 8 seeds 11/18/19/22/25 and task 2 seeds 12/14/27/43/49 | Basic H=8: 0/10; Basic H=1: 3/10; adaptive risk H=1/8: 10/10 on same seeds | Complete |

### Dean Detector Training (2026-06-01/02)
| Experiment | Split | Detectors Produced |
| :--- | :--- | :--- |
| `dean_all_tasks_full_uncertainty_test_20260601` | all_tasks_random | base, unc_raw |
| `dean_ood_last2_taskids_full_v1_20260601` | ood_last2_taskids_full | base, unc_raw |
| `dean_uncertainty_topk_feature_sweep_v1_20260602` | all_tasks_full + ood | topk8, topk16, topk32 |

### Bob H10 Detector Training (2026-06-08)
| Experiment | Split | Detectors Produced | Best Epoch | q95 |
| :--- | :--- | :--- | :---: | :---: |
| H10 base | h10_continuous (all_tasks_random) | `base` (hash `802413d2...`) | 8 | 0.822 |
| H10 TopK8 | h10_continuous (all_tasks_random) | `unc_topk8` (hash `687b5d35...`) | 14 | 0.615 |

---

## Data Collection Campaigns

| Campaign | Host | Date | Episodes | Mode | Suite | Status |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| FIPER sweep eternal | Bob + Sam | 2026-05-27 | ~734K rows | Receding | Multi-suite | Frozen |
| Dean object uncertainty | Dean | 2026-05-29 | 4,257 | Receding | Multi-suite | Frozen |
| Goal-object production | Dean | 2026-06-05 | 200 (exact) + 17K+ (cont.) | Chunk10 + Receding | libero_goal_object | exact_200 frozen; continuous growing |
| SimVLA goal uncertainty collection | Sam | 2026-06-19 | target 10,000 | Receding H10, 8 ACE, 49D uncertainty | `libero_goal` | RUNNING in tmux `simvla_goal_uncertainty_10000ep_20260619`; output root `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/simvla_goal_uncertainty_2000ep_20260619` |
| OpenVLA old plain-goal dataset | Bob | 2026-06-16 | 6,009 | OpenVLA H8 receding | plain `libero_goal` | Retained diagnostic/source dataset; folder name is misleading |
| OpenVLA final goal-object dataset | Bob | 2026-06-18 | 1,890 | OpenVLA H8 receding | `libero_goal_object` | Frozen final OpenVLA risk training dataset |

---

## Running Experiments

| Experiment ID | Host | Status | Description |
| :--- | :--- | :--- | :--- |
| `simvla_goal_uncertainty_10000ep_20260619` | Sam | RUNNING as of 2026-06-19 launch | Modified SimVLA `ckpt-60000` plain `libero_goal` collection for goal-to-goal-object offline OOD risk training. Target 10,000 episodes, tasks 0-9 round-robin, max timeout 800, H10 action chunks, 8 ACE candidates, 49D uncertainty fields. |
| `openvla_ood_basic_vs_risk_100ep_20260618` | Bob | RUNNING/resumed as of 2026-06-19 snapshot | OpenVLA basic vs OpenVLA risk-horizon on `libero_goal_object_ood`, seeds 10-109, 18 tasks. Resume snapshot: paused safely at 2,686/3,600, then resumed from task 8 seed 96. Basic is complete; risk is still partial, so do not cite final risk result until all 1,800 risk episodes complete. |
| `openvla_ood_basic_h1_100ep_20260619` | Bob | SCHEDULED as of 2026-06-19 | Full fixed-H1 OpenVLA baseline on the exact same `libero_goal_object_ood` tasks/seeds/max-steps as `openvla_ood_basic_vs_risk_100ep_20260618`. Waiter tmux `openvla_wait_then_basic_h1_20260619` will launch tmux `openvla_ood_basic_h1_100ep_20260619` only after the current run reaches 3,600 summary rows. |
