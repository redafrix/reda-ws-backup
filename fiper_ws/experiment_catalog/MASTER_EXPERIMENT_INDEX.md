# Master Experiment Index

Updated: 2026-07-03 by Codex cross-machine catalog consolidation.

This is the canonical reference for every campaign that produced results we cite or might cite. Each entry includes the trust verdict from the forensic audit where applicable.

> [!IMPORTANT]
> For new sessions, start with [CROSS_MACHINE_EXPERIMENT_MAP_20260703.md](CROSS_MACHINE_EXPERIMENT_MAP_20260703.md). It links this chronological index to the current Bob/Sam/Dean/local state, promoted models, official FIPER runs, OpenVLA, Pi0.5, Obsidian, Git status, and large-artifact manifest.

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

### SimVLA Plain-Goal to Goal-Object Offline OOD Test (Sam, 2026-06-22)

| Property | Value |
| :--- | :--- |
| **Experiment** | `simvla_goal_to_goal_object_ood_topk8_20260622` |
| **Output root** | `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_goal_to_goal_object_ood_topk8_20260622` |
| **Train source** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_uncertainty_final_5410ep_20260622/fiper_receding_samples.jsonl` |
| **OOD target** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_object_h10_continuous_flat_from_bob_20260622` |
| **Model schema** | H10 TopK8-style Transformer: history `16x21`, action `10x7`, static `51` (`action_stats_28 + ACE_7 + proprio_8 + selected_uncertainty_topk8_8`); no explicit task id or timestep input |
| **Train split** | 3,787 plain `libero_goal` episodes; 594,842 rows; 3,584 success / 203 failure episodes |
| **Validation split** | 812 plain `libero_goal` episodes; 127,939 rows; 768 success / 44 failure episodes |
| **Source test split** | 811 plain `libero_goal` episodes; 129,244 rows; 768 success / 43 failure episodes |
| **OOD test set** | 17,409 `libero_goal_object` episodes; 235,466 rows; 14,005 success / 3,404 failure episodes |
| **Best epoch** | 2 |
| **Source heldout result** | AUROC 0.9307, AUPRC 0.9051; at best-val-F1 threshold 0.6014: 17.06% episode false alarms, 97.67% failure detection |
| **Goal-object OOD result** | AUROC 0.7627, AUPRC 0.6998; at best-val-F1 threshold 0.6014: 4.59% episode false alarms, 78.91% failure detection, Det@25 0.15%, Det@50 7.61% |
| **Comparison to previous best offline detector** | Previous best reference (`v2_018_transformer_k16` score q95 K3): seen false alarm 15.44%, OOD false alarm 25.59%, OOD failure detection 95.24%, OOD Det@25 26.19%, OOD Det@50 85.71%, mean detection time 0.333. New plain-goal-trained detector: seen/source false alarm 17.06%, OOD false alarm 4.59%, OOD failure detection 78.91%, OOD Det@25 0.15%, OOD Det@50 7.61%, mean detection fraction 0.722. |
| **Report** | `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_goal_to_goal_object_ood_topk8_20260622/SIMVLA_GOAL_TO_GOAL_OBJECT_OOD_REPORT_20260622.md` |
| **Status** | Complete |
| **Trust** | **TRUST offline diagnostic**: source heldout is strong, but plain-goal to goal-object OOD transfer detects many failures late and is not a good online-ready detector without goal-object training data. |

### Official-FIPER Materialized-Code Run (Dean, 2026-06-22 to 2026-06-23)

| Property | Value |
| :--- | :--- |
| **Experiment** | `official_fiper_rndoe_entropy_fold00_20260622` |
| **Root** | `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622` |
| **Goal** | Run the closer-to-official FIPER RND/OE + entropy pipeline by materializing official-format `obs_embeddings.pt` and `action_preds.pt` from saved MuJoCo states and SimVLA/SmolVLM embeddings. |
| **Scripts** | `/home/dean/fiper_uncertainty_collection/scripts/materialize_official_fiper_fold00_obs_embeddings_sharded_20260622.py`; `/home/dean/fiper_uncertainty_collection/scripts/run_official_fiper_rndoe_entropy_fold00_20260622.py` |
| **Tensors** | Fully materialized: `obs_embeddings.pt=(170943,960)`, `action_preds.pt=(170943,9,10,7)` for both `libero_fold00` and `libero_fold00_hygiene` |
| **Report** | `fiper_ws/experiments/official_fiper_rndoe_entropy_fold00_20260622/reports/OFFICIAL_FIPER_FINAL_ABLATION_COMPARISON_VERIFIED_20260624.md` |
| **Status** | **Complete (Verified 2026-06-24)** |
| **Trust** | **TRUST as verified final official-FIPER ablation**. Forensic audit recomputed metrics from raw score trajectories across all 5 seeds on Dean. Confirms 100% RND-OE OOD Success FA due to visual saturation. Option B Fusion is best row with Success FA 38.9%, Failure Det 97.6%, Accuracy 79.4%, Det. Time 0.314, Det@25 52.4%, Det@50 78.6%. |



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

**H10 TopK8 metric caveat found 2026-06-23:** the saved H10 `unc_topk8` model metrics contain seen/train/val/calib buckets only. In its `metrics.json`, `success_test_ood` and `failure_eval_ood` have 0 episodes. Any H10 OOD detector-only result must therefore come from a separate evaluation artifact, not from the model directory itself.

### Sam H10 TopK8 on Official 18-Task `libero_goal_object_ood` Offline Audit (2026-06-23)

| Property | Value |
| :--- | :--- |
| **Experiment ID** | `simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace` |
| **Dataset** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622` |
| **Dataset contents** | 180 episodes: 10 per task across official 18-task `libero_goal_object_ood`; 149 successes, 31 failures; H10 main action chunks, 8 ACE candidates, 49D uncertainty, timeout 800 |
| **Detector** | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8` |
| **Schema** | H10 TopK8 detector: history `16x21`, action `10x7`, static `51`; selected uncertainty dims `[6,21,25,27,23,2,26,24]`; no explicit task id/timestep input |
| **Important correction** | Initial evaluator used a mismatched ACE formula and misleading any-row/mass interpretation. Corrected evaluator now uses the same ACE formula as online `run_policy_matrix.py`, then reports old-style K-window metrics plus mass sweeps. |
| **Saved report** | `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace/SELECTED_CAP_TOPK8_OFFLINE_LIBERO_GOAL_OBJECT_OOD_180EP_20260622.md` |
| **Saved K-window JSON** | `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace/k_window_metrics_same_style.json` |
| **Trust** | **TRUST detector-only diagnostic after ACE correction**. Do not interpret as online selected-cap replay; it is an offline detector threshold/calibration audit. |

Key corrected detector-only metrics on the official 18-task OOD dataset:

| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `score_q95_K3` | 95.3% | 100.0% | 100.0% | 100.0% | 100.0% | 0.028 | 0.0% |
| `score_q99_K3` | 60.4% | 100.0% | 45.2% | 90.3% | 96.8% | 0.142 | 0.0% |
| saved `score_q95_mass_0.15` | 96.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.027 | 0.0% |
| `score_q95_mass_10` | 34.9% | 100.0% | 12.9% | 93.5% | 96.8% | 0.157 | 0.0% |
| `score_q95_mass_20` | 20.8% | 96.8% | 3.2% | 90.3% | 96.8% | 0.166 | 3.2% |
| `score_q95_mass_50` | 2.7% | 96.8% | 0.0% | 16.1% | 90.3% | 0.288 | 3.2% |

Interpretation: the model/dataset are H10-aligned and the detector still separates failures, but the saved H10 conformal mass threshold `0.15` is badly under-calibrated for this official 18-task OOD detector-only setting. Raising mass threshold improves false alarms while preserving high detection; this is a calibration issue, not evidence that the H10 dataset is invalid.

### Sam H10 TopK8 on Official 18-Task `libero_goal_object_ood` Derived Cap-300 Audit (2026-06-23)

| Property | Value |
| :--- | :--- |
| **Experiment ID** | `simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace` |
| **Derived dataset** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623` |
| **Source dataset** | `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622` |
| **Derivation rule** | Keep rows with `timestep < 300`; label success only if original episode succeeded before 300 steps; any episode reaching 300 is failure. This is a derived offline dataset, not a fresh collection. |
| **Counts** | 180 episodes, 143 successes, 37 failures, 28,031 rows. Six original max-800 successes became cap-300 failures. |
| **Detector** | Same H10 TopK8 detector as above: `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8` |
| **Result path** | `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace` |
| **Report** | `/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace/SIMVLA_H10_TOPK8_OFFICIAL_OOD_CAP300_AUDIT_20260623.md` |
| **Trust** | **TRUST derived detector-only diagnostic**. Use only for cap-300 offline threshold sensitivity; do not treat it as a separately collected 300-step rollout dataset. |

Key cap-300 detector-only metrics:

| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `score_q95_K3` | 95.1% | 100.0% | 62.2% | 100.0% | 100.0% | 0.083 | 0.0% |
| `score_q99_K3` | 60.1% | 89.2% | 2.7% | 21.6% | 86.5% | 0.272 | 10.8% |
| saved `score_q95_mass_0.15` | 95.8% | 100.0% | 62.2% | 100.0% | 100.0% | 0.081 | 0.0% |
| `score_q95_mass_10` | 33.6% | 91.9% | 2.7% | 13.5% | 86.5% | 0.338 | 8.1% |
| `score_q95_mass_20` | 18.9% | 91.9% | 0.0% | 0.0% | 83.8% | 0.437 | 8.1% |
| `score_q95_mass_50` | 0.0% | 83.8% | 0.0% | 0.0% | 0.0% | 0.693 | 16.2% |

Extended Dean sweep added 2026-06-29 using the same cap-300 labels and saved TopK8 row scores:

| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `fixed_0.5_mass_30` | 17.5% | 91.9% | 0.0% | 0.0% | 83.8% | 0.445 | 8.1% |
| `fixed_0.5_mass_40` | 15.4% | 91.9% | 0.0% | 0.0% | 48.6% | 0.514 | 8.1% |
| `q99_mass_2` | 1.4% | 83.8% | 0.0% | 0.0% | 27.0% | 0.548 | 16.2% |

Extended sweep report: `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_cap300_extended_sweep_20260629/TOPK8_OOD180_CAP300_EXTENDED_SWEEP_20260629.md`.

---

## Data Collection Campaigns

| Campaign | Host | Date | Episodes | Mode | Suite | Status |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| FIPER sweep eternal | Bob + Sam | 2026-05-27 | ~734K rows | Receding | Multi-suite | Frozen |
| Dean object uncertainty | Dean | 2026-05-29 | 4,257 | Receding | Multi-suite | Frozen |
| Goal-object production | Dean | 2026-06-05 | 200 (exact) + 17K+ (cont.) | Chunk10 + Receding | libero_goal_object | exact_200 frozen; continuous growing |
| SimVLA goal uncertainty collection | Sam | 2026-06-19 to 2026-06-22 | 5,410 frozen | Receding H10, 8 ACE, 49D uncertainty | `libero_goal` | Frozen/validated at `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_goal_uncertainty_final_5410ep_20260622`; exactly 541 episodes per task |
| OpenVLA old plain-goal dataset | Bob | 2026-06-16 | 6,009 | OpenVLA H8 receding | plain `libero_goal` | Retained diagnostic/source dataset; folder name is misleading |
| OpenVLA final goal-object dataset | Bob | 2026-06-18 | 1,890 | OpenVLA H8 receding | `libero_goal_object` | Frozen final OpenVLA risk training dataset |
| Pi0.5 frozen goal-object dataset | Bob | 2026-06-25 | 4,090 | Pi0.5 H10 receding | `libero_goal_object` | Frozen/validated at `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/datasets/pi05_libero_goal_object_h10_risk_frozen_20260625` |

---

## Running Experiments

| Experiment ID | Host | Status | Description |
| :--- | :--- | :--- | :--- |
| `simvla_goal_to_goal_object_ood_topk8_20260622` | Sam | COMPLETE as of 2026-06-22 | Offline diagnostic: train H10 TopK8-style SimVLA risk head on frozen plain `libero_goal` dataset and test full transferred `libero_goal_object` dataset. Source heldout strong; OOD AUROC 0.7627, AUPRC 0.6998, failure detection late. |
| `openvla_ood_basic_vs_risk_100ep_20260618` | Bob | COMPLETE as of 2026-06-22 | OpenVLA basic vs OpenVLA risk-horizon on `libero_goal_object_ood`, seeds 10-109, 18 tasks. Final result: basic H8 976/1,800 = 54.22%; adaptive risk H1/8 1,014/1,800 = 56.33%; net +38 successes. |
| `openvla_ood_basic_h1_100ep_20260619` | Bob | RESUMED/RUNNING as of 2026-06-29 09:45 CEST | Fixed-H1 OpenVLA baseline on the same `libero_goal_object_ood` suite, tasks, seeds 10-109, and max steps. It was interrupted at 1,720/1,800 rows; Codex relaunched the same script/output root in tmux `openvla_ood_basic_h1_100ep_20260619`. Resume log confirms `1720/1800 already complete` and first resumed episode `[1721/1800] policy=openvla_basic_h1 task=17 seed=30`. |
| `simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622` | Sam | COMPLETE; corrected offline audit added 2026-06-23 | Official 18-task `libero_goal_object_ood` offline dataset: 180 episodes, H10 action chunks, 8 ACE candidates, 49D uncertainty, timeout 800. Collection used modified SimVLA `ckpt-60000`, not risk-aware policy. Corrected H10 TopK8 detector-only audit shows saved threshold is under-calibrated on this official OOD set; see section above. |
| `official_fiper_goal_object_ood_ablation_20260625_no_retrain_audit_20260626` | Dean | COMPLETE as of 2026-06-26 | Clean no-retrain/no-recalibration official FIPER ablation on the same 180ep official `libero_goal_object_ood` dataset used for H10 TopK8. Dataset validation: 180 OOD test episodes = 149 successes + 31 failures, 0 calib/test overlap, 0 ID/OOD overlap. Official FIPER entropy, RND-OE, and fusion all false-alarm on 100% of OOD successes while detecting 100% of failures. H10 TopK8 threshold sweep on the same rows shows saved `q95_mass_0.15` is under-calibrated (96.0% FA / 100.0% Det), but `q95_mass_20` gives 20.8% FA / 96.8% Det and `q95_mass_50` gives 2.7% FA / 96.8% Det. Combined audit: `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_audited_threshold_sweep/AUDITED_TOPK8_AND_OFFICIAL_FIPER_OOD_REPORT_20260626.md`. |
| `simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623` | Sam | COMPLETE; derived offline audit added 2026-06-23 | Cap-300 derivative of the official 18-task OOD dataset. 180 episodes, 143 successes, 37 failures. Same H10 TopK8 detector audit shows stricter horizon reduces useful early detection for mass policies; `q95_mass_20` gives 18.9% FA, 91.9% Det, Det@25 0.0%, Det@50 83.8%. |
| `h10_topk8_seen_and_distinct_ood_calibration_audit_20260629` | Bob + Dean | COMPLETE as of 2026-06-29 | No-retrain calibration audit for the saved H10 TopK8 detector. Bob recomputed thresholds using only seen `libero_goal_object` calibration/validation buckets; Dean applied them to official OOD180. Seen-only calibration did not solve transfer: best actual-max800 row reported was `q99_seen_success_FA010` with 57.7% Success FA / 100.0% Failure Det / Det@25 90.3%. A separate non-test OOD calibration using `selected_cap_t03_c04_100ep_20260610` also remained high-FA: about 53.7% Success FA / 100.0% Failure Det. Reports: `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260629_seen_calibrated_thresholds/H10_TOPK8_SEEN_CALIBRATED_ON_OFFICIAL_OOD180_20260629.md` and `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260629_distinct_ood_calibration/H10_TOPK8_DISTINCT_OOD_CALIBRATION_ON_OOD180_20260629.md`. |
| `pi05_goal_object_h10_risk_20260625` | Bob | COMPLETE as of 2026-06-25 | Offline H10 SeqRiskModel training on frozen Pi0.5 `libero_goal_object` dataset. Val-calibrated thresholds: best F1 0.4800, q95 0.7218. Test AUROC 0.9534, AUPRC 0.9728. Episode False Alarm at q95_mass_10 is 2.98% with 99.21% Failure Detection. |
| `pi05_official_goal_swap_10task_50ep_basic_then_selected_cap_q95mass02_20260625` | Bob | COMPLETE as of 2026-06-26 | Official `libero_goal_swap` 10-task online and offline audit, 50 paired seeds/task, max 300, H10. Online: basic 161/500 = 32.20%; selected-cap risk 166/500 = 33.20%, net +5. Risk policy made 1,306 action changes across 383/500 episodes; 1,017 changes occurred in failed episodes. Offline detector-only threshold sweep with old-with-task9 risk head shows no strong operating point on `goal_swap`: `q95_mass_1` gives Basic-source FA 31.06% / Det 83.19% and Risk-source FA 33.13% / Det 85.03%; `q95_mass_1.25` lowers FA to about 20% but detection falls to about 81%. |
| `simvla_official_libero_goal_object_h10_basic_500ep_20260626` | Bob | COMPLETE as of 2026-06-26 | Official SimVLA checkpoint, fixed H10 execution, official byte-identical `libero_goal_object` BDDL/init copied into separate `libero_goal_object_official` folders without touching local active `libero_goal_object`. Completed 500/500 episodes = 50 init states per task with no `(task_id, initial_state_index)` duplicates and no run errors. Final success: 422/500 = 84.40%. Per-task SR: task0 98%, task1 98%, task2 100%, task3 26%, task4 98%, task5 100%, task6 70%, task7 100%, task8 98%, task9 56%. Output: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_basic_500ep_20260626`. |
| `pi05_official_ood_18task_100ep_basic_then_selected_cap_q95mass02_20260625` | Bob | COMPLETE as of 2026-06-27; re-audited 2026-06-29 | Official `libero_goal_object_ood` 18-task online + offline audit, 100 paired seeds/task, max 300, H10. Online JSONL audit: basic 1,754/1,800 = 97.44%; selected-cap risk 1,736/1,800 = 96.44%, net -18. Risk policy made 759 action changes across 529/1,800 episodes. Offline two-head result path: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_ood_18task_100ep_two_heads_eval_20260625`. |
| `strict_official_fiper_ood180_20260630` | Dean | RUNNING as of 2026-06-30 16:45 CEST | Strict official-FIPER rerun on the already materialized 180-episode `libero_goal_object_ood` test dataset. Uses a fresh clean clone of `learnsyslab/fiper` at commit `13d79c5c3069def843e454787ff128defc249838`; only a runtime `.pt` loader-key compatibility monkeypatch is applied. RND-OE is trained fresh on calibration ID successes only; OOD rows are test-only. Validation passed: 830 rollouts, 52,087 steps, 150 ID calibration successes, 180 OOD tests = 149 successes + 31 failures, 0 calibration/test overlap, 0 ID/OOD overlap. Tmux: `strict_official_fiper_ood180_20260630`; output root: `/home/dean/fiper_uncertainty_collection/experiments/strict_official_fiper_ood180_20260630`. |
| `cross_suite_official_ood_20260630` | Bob + Sam | COMPLETE as of 2026-07-01 05:48 CEST | Cross-suite official OOD offline campaign for H10 TopK8 vs official FIPER evidence. Sam official seen `libero_goal_object_official` H10 uncertainty collection is fully transferred to Bob as `source_seen_goal_object_from_sam_20260630`: 4,469 episodes, 48.66GB samples, H10, 8 ACE candidates, 49D uncertainty, saved states, and official BDDL/init metadata. Do not use the abandoned Bob mini source `/datasets/source_seen_goal_object_hf_official_1000` because it has only 12 episodes. Bob supervisor tmux `cross_suite_official_ood_20260630` completed official-file-validated OOD suite collection and train/eval with modified SimVLA `ckpt-60000`, H10, 8 ACE candidates, 49D uncertainty, saved MuJoCo states, and max 300 timeout. Live-row audit verified real JSONL rows: main chunk `[10,7]`, ACE chunks `[8,10,7]`, uncertainty `[49]`, finite values, and nonempty history after timestep 10. Completed datasets: `libero_goal_swap` 100ep, `libero_goal_task` 100ep, `libero_goal_object_ood` 180ep, `libero_spatial_object` 100ep, `libero_object_object` 100ep, `libero_10_object` 100ep. Summary report: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/CROSS_SUITE_OFFICIAL_OOD_SUMMARY_20260630.md`. Root: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630`. Supervisor log: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/logs/supervisor.log`. |
| `simvla_h10_topk8_official_goal_object_seen_main_20260701` | Bob | COMPLETE as of 2026-07-01 | Promoted main cross-suite H10 TopK8 SeqRiskModel. Selected from the repeated same-source trainings by highest source validation AUPRC only, no OOD target performance used for selection. Source experiment: `train_seen_goal_object_eval_goal_swap_100`; selected source val AUPRC 0.9369, val AUROC 0.9345, epoch 1. Training source: Sam official `libero_goal_object_official` seen dataset at `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl`. Promoted model path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/models/simvla_h10_topk8_official_goal_object_seen_main_20260701`. Single-checkpoint OOD eval path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/eval_promoted_single_model_all_ood_20260701`. |
| `official_fiper_seen_goal_object_train_eval_20260701` | Bob | COMPLETE as of 2026-07-02 audit | Official FIPER seen calibration baseline on official `libero_goal_object`. Dataset: 900 rollouts, 194,643 steps, 150 successful seen calibration rollouts, 250 seen held-out test rollouts. Official repo commit `13d79c5c3069def843e454787ff128defc249838`; method classes unchanged, with only dataset-adapter and runtime compatibility patches. RND-OE trained for seeds 0,1,2,42,43. Best seen q95 operating points are now recorded in the Obsidian addendum and will be reused for cross-suite OOD without OOD recalibration. Output: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_train_eval_20260701`. |
| `official_fiper_seen_thresholds_cross_suite_ood_20260702` | Bob | COMPLETE as of 2026-07-02 | Official FIPER cross-suite OOD application using seen-only thresholds. It materialized each collected OOD dataset (`goal_object_ood_180`, `goal_swap_100`, `goal_task_100`, `spatial_object_100`, `object_object_100`, `libero10_object_100`) into official FIPER tensors, built combined datasets with 150 seen calibration successes plus OOD test rollouts, reused seen RND checkpoints, and reported the exact seen-selected q95 operating points. No OOD calibration and no OOD threshold tuning. Key result: official RND-OE remains unstable under domain shift, often false-alarming 100% on OOD successes; entropy/fusion transfer varies strongly by suite. Report: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_thresholds_cross_suite_ood_20260702/OFFICIAL_FIPER_SEEN_THRESHOLDS_CROSS_SUITE_OOD_20260702.md`; aggregate CSV: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_thresholds_cross_suite_ood_20260702/official_fiper_seen_thresholds_cross_suite_ood_aggregate.csv`. |

### Pi0.5 Official `libero_goal_swap` 50ep Detailed Result (2026-06-26)

| Property | Value |
| :--- | :--- |
| **Online root** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_official_goal_swap_10task_50ep_basic_then_selected_cap_q95mass02_20260625` |
| **Offline result path** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_goal_swap_10task_50ep_two_heads_eval_20260625` |
| **Threshold sweep JSON** | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_official_goal_swap_10task_50ep_two_heads_eval_20260625/old_with_task9_q95_mass_threshold_sweep_20260626.json` |
| **Dataset records** | Saved in per-policy `episode_summaries.jsonl`, `query_records.jsonl`, and `step_records.jsonl` under the online root |
| **Trust** | TRUST complete online run + detector-only offline threshold audit. Selected-cap is active but only modestly positive on this suite. |

Online success:

| Policy | Done | Success | Fail | Success Rate |
| :--- | ---: | ---: | ---: | ---: |
| `pi05_basic_h10` | 500 | 161 | 339 | 32.20% |
| `pi05_risk_selected_cap_topk8_h10` | 500 | 166 | 334 | 33.20% |

Per-task online success:

| Task | Instruction | Basic SR | Risk SR | Delta |
| ---: | :--- | :---: | :---: | ---: |
| 0 | open the middle drawer of the cabinet | 0/50 = 0.00% | 0/50 = 0.00% | 0 |
| 1 | put the bowl on the stove | 41/50 = 82.00% | 41/50 = 82.00% | 0 |
| 2 | put the wine bottle on top of the cabinet | 0/50 = 0.00% | 0/50 = 0.00% | 0 |
| 3 | open the top drawer and put the bowl inside | 48/50 = 96.00% | 49/50 = 98.00% | +1 |
| 4 | put the bowl on top of the cabinet | 0/50 = 0.00% | 0/50 = 0.00% | 0 |
| 5 | push the plate to the front of the stove | 0/50 = 0.00% | 0/50 = 0.00% | 0 |
| 6 | put the cream cheese in the bowl | 0/50 = 0.00% | 0/50 = 0.00% | 0 |
| 7 | turn on the stove | 50/50 = 100.00% | 49/50 = 98.00% | -1 |
| 8 | put the bowl on the plate | 22/50 = 44.00% | 26/50 = 52.00% | +4 |
| 9 | put the wine bottle on the rack | 0/50 = 0.00% | 1/50 = 2.00% | +1 |

Action modification summary:

| Group | Episodes | Action Changes | Changed Episodes | Avg Changes / Episode |
| :--- | ---: | ---: | ---: | ---: |
| All risk episodes | 500 | 1306 | 383 | 2.61 |
| Successful risk episodes | 166 | 289 | 127 | 1.74 |
| Failed risk episodes | 334 | 1017 | 256 | 3.04 |

Matched same-seed breakdown: 18 rescues, 13 regressions, 148 both-success, 321 both-fail. Net online gain is +5 successes.


### Cross-Suite Official OOD Campaign ETA/Provenance Snapshot (2026-06-30 14:44 CEST)

| Item | Status |
| :--- | :--- |
| Running sessions | `cross_suite_official_ood_20260630` |
| OOD target total | 680 episodes: goal-swap 100, goal-task 100, goal-object-OOD 180, spatial-object 100, object-object 100, LIBERO-10-object 100 |
| Current stage | Collecting `goal_swap_100`; observed timeout episodes take about 103-104s each at max 300 steps |
| ETA | Worst-case if most episodes timeout: about 18-20h for collection, plus training/eval. Faster if later suites produce successes before 300 steps. |
| Seen source | Sam `libero_goal_object_official`, transferred to Bob as `source_seen_goal_object_from_sam_20260630`; 4,469 episodes. Verified 20/20 BDDL/init SHA256 match against Hugging Face `zhouxueyang/LIBERO-Pro`. |
| HF official target suites | `libero_goal_swap`, `libero_goal_task`, `libero_spatial_object`, `libero_object_object`, `libero_10_object` |
| Local extra OOD target | `libero_goal_object_ood`; not in HF LIBERO-Pro, but preflight passed 18/18 using `libero_goal_object_ood_temp` BDDL + `libero_goal_object_ood` init states |
| FIPER readiness | New OOD datasets save states plus action candidates, so they can be materialized into official FIPER tensors later. |
| Data audit warning | Ignore abandoned `/datasets/source_seen_goal_object_hf_official_1000` for training; it contains only 12 episodes and was a stopped Bob recollection/smoke artifact. |

### Promoted Single-Checkpoint OOD Result (2026-07-01)

This table uses one fixed checkpoint, `simvla_h10_topk8_official_goal_object_seen_main_20260701`, selected by source validation AUPRC only. Threshold values are carried from the same source validation calibration. The “best per dataset” row is diagnostic because it chooses among seen-calibrated threshold rules after seeing each OOD dataset.

| Dataset | Threshold | Value | Success FA | Failure Det | Det@25 | Det@50 | Mean Time |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| `goal_swap_100` | `q99_success` | 0.9976 | 0.00% | 49.48% | 9.28% | 29.90% | 0.489 |
| `goal_task_100` | `best_val_f1` | 0.3560 | 0.00% | 93.33% | 54.44% | 87.78% | 0.210 |
| `goal_object_ood_180` | `q95_success` | 0.9054 | 20.14% | 92.68% | 26.83% | 73.17% | 0.334 |
| `spatial_object_100` | `q95_success` | 0.9054 | 60.22% | 100.00% | 100.00% | 100.00% | 0.079 |
| `object_object_100` | `q95_success` | 0.9054 | 34.92% | 81.08% | 75.68% | 81.08% | 0.030 |
| `libero10_object_100` | `q99_success` | 0.9976 | 13.04% | 22.08% | 0.00% | 6.49% | 0.641 |

---

## Deep Coverage Audit Addendum (2026-07-03)

This addendum records experiment families recovered by the 2026-07-03 deep cross-host/archive scan. Full audit report: `DEEP_EXPERIMENT_COVERAGE_AUDIT_20260703.md`. Compact machine-readable summary: `manifests/deep_audit_summary_20260703.json`.

### Audit Scope

| Host | Reduced experiment-like roots | Filtered roots not clearly covered before | Notes |
| :--- | ---: | ---: | :--- |
| Bob | 1747 | 44 | Includes Pi0.5 subruns, OpenVLA smokes, historical FIPER/SimVLA campaign roots, cross-suite per-dataset eval roots. |
| Batman/local | 909 | 347 | Mostly archives and copied project material; contains Stage6-9 reports/scripts, official-FIPER scripts, Pi0.5/OpenVLA scripts, video-smoke material, and old Isaac folders. |
| Dean | 146 | 53 | Includes `fiper_goal_object_collection_20260605` and TDQC/legacy SimVLA roots under `/home/redafrix/SimVLA_modified/folderu`. |
| Sam | 86 | 1 | Adds video/manual-review reels for goal/OOD rollouts. |

### Recovered Or Strengthened Families

| Family | Host | Path | Current interpretation |
| :--- | :--- | :--- | :--- |
| Bob risk matrix campaign | Bob | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/bob_risk_matrix_campaign_20260605` | Historical isolated comparison of `base` 43D detector vs `unc_topk8` 51D detector; records fairness controls, queue/resume state, smoke dependencies, and compatibility matrix. |
| Clean v2_018 audit rerun | Bob | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/re_run_v2_018_audit_20260624` | Clean bridge report for original-FIPER-style baselines vs `v2_018_transformer_k16`; selected `score q95 K3` row gives seen FA 16.2%, OOD FA 26.1%, OOD failure detection 95.2%. |
| Old goal-object-OOD full sweep/audit | Bob | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/libero_goal_object_ood_full_sweep_20260609` and `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/libero_goal_object_ood_audit_20260609` | Historical OOD setup evidence and task/path audit. Parsed audit production summaries include 18 rows, 17 successes. |
| Pi0.5 OOD smoke and 10ep | Bob | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_smoke_20260625` and `..._10ep_20260625` | Smoke: 2 rows/policy. 10ep full OOD18: 180 rows for basic and 180 for risk; both parsed as 176/180 success. |
| Pi0.5 local no-task9 risk head | Bob | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_no_task9_20260625` and `/datasets/pi05_libero_goal_object_h10_risk_frozen_no_task9_20260625` | Rebuilt after local task9 rack issue. Dataset has 3681 episodes, 3298 successes, 383 failures across tasks 0..8. |
| Pi0.5 40ep threshold/always-lowest probes | Bob | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_ood_q95mass1_loose_task9_task12_40ep_timeout300_20260625`, `...q95mass02...`, `...always_lowest_task13_task14...` | Threshold-behavior probes before the larger official OOD/swap campaigns. Keep as diagnostic, not final evidence. |
| Pi0.5 official OOD18 100ep | Bob | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_official_ood_18task_100ep_basic_then_selected_cap_q95mass02_20260625` | Parsed JSONL: basic 1754/1800 success, risk selected-cap 1736/1800 success. |
| Pi0.5 official goal-swap 50ep | Bob | `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_official_goal_swap_10task_50ep_basic_then_selected_cap_q95mass02_20260625` | Parsed JSONL: basic 161/500 success, risk selected-cap 166/500 success; risk made 1306 action changes. |
| OpenVLA smokes and H1 follow-up | Bob | `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals` | OpenVLA H1 follow-up now parses as 1800/1800 rows, 1022 successes. Older “1720/1800 interrupted” text is stale unless a newer live check contradicts this. |
| Dean goal-object collection workspace | Dean | `/home/dean/fiper_goal_object_collection_20260605` | Major historical source: exact_200 chunk10 162/200 success, exact_200 receding 153/200, continuous chunk10 14005/17409, continuous receding 2072/2745. Includes smoke, benchmark, and reproduction bundle folders. |
| Dean TDQC / SimVLA legacy roots | Dean | `/home/redafrix/SimVLA_modified/folderu/evaluation/libero/eval_libero_pro` and `/home/redafrix/SimVLA_modified/folderu/runs/tdqc_calibrator` | Legacy TDQC calibration/evaluation evidence. Do not mix with current H10 TopK8 claims unless explicitly studying historical TDQC. |
| Sam video review reels | Sam | `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/video_reels_libero_goal_and_ood_20260616` | Manual/visual review provenance, including OOD selected-cap and goal-object manifests. |
| Local archived scripts/reports | Batman | `/home/redafrix/tests/internship/archive/root_cleanup_20260629` and `/home/redafrix/tests/internship/archive/root_cleanup_second_pass_20260602` | Contains Pi0.5/OpenVLA/official-FIPER scripts, video-smoke artifacts, old Isaac material, and Stage6-9 Codex reports. Treat as archived provenance, not active source roots. |

### Corrections From This Audit

- `CROSS_MACHINE_EXPERIMENT_MAP_20260703.md`, `HOST_WORKSPACE_MAP.md`, and `GIT_SYNC_PLAN_20260703.md` were stale about Git being broken. Git is now repaired and branch-per-host catalog branches have been pushed.
- The old host manifests under `fiper_ws/experiment_catalog/manifests` are historical June snapshots; they are not complete current inventories.
- Heavy raw scan outputs from this audit remain in `/tmp/internship_deep_audit_20260703` and were not committed. The durable substitute is `DEEP_EXPERIMENT_COVERAGE_AUDIT_20260703.md` plus `manifests/deep_audit_summary_20260703.json`.


## Current Main Isaac 3cm350 Risk Model & Conformal Results (2026-08-19)

Canonical record: [`ISAAC_MAIN_3CM350_20260819.md`](ISAAC_MAIN_3CM350_20260819.md) and [`../../isaac_experiment_map/CURRENT_MAIN_ISAAC_RESULTS_20260819.md`](../../isaac_experiment_map/CURRENT_MAIN_ISAAC_RESULTS_20260819.md).

- Protocol: 3 cm threshold, 350 control ticks, 30 Hz, H10 execution, **NO DWELL**.
- Dataset: `isaac_seen4904_h10_3cm350_exact_v1` (4,904 episodes: 4,387 success, 517 failure, 96,813 rows; 96 timing-unresolvable episodes excluded).
- Split: Unified label-stratified 70/15/15 (Train: 3,433 eps; Val: 735 eps; Test: 736 eps; seed 20260819).
- Model: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2` (SeqRiskModel, 128 width, 3 layers, 4 heads, pos_weight=4.3453).
- Locked internal TEST (736 eps / 14,526 rows): query AUROC **0.9408** / AUPRC **0.8748**, episode-balanced AUROC **0.9987** / AUPRC **0.9782**.
- Conformal Best Val F1 Threshold (`0.5791`): **100.0% Failure Detection**, **7.60% Success False Alarm**.
- Scope: Locked internal TEST split. New-protocol OOD evaluation is pending.

## Historical Corrected True-H10 Isaac Sim Result (2026-08-18)

Canonical record: [`ISAAC_RESULTS_20260818.md`](ISAAC_RESULTS_20260818.md) and [`../../isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md`](../../isaac_experiment_map/FINAL_ISAAC_RESULTS_20260818.md).

- Seen4000: **4000 episodes**, **3908 success / 92 failure**, **75,603 decision rows**.
- V1 validation AUROC/AUPRC: **0.9344901338 / 0.8494462696**.
- Locked historical true-H10 OOD150 detector: **72 success / 78 failure**, **5,887 rows**, step **AUROC 0.9165517742 / AUPRC 0.9800307262**.
- Main detector threshold: `best_val_f1 = 0.7990124225616455`, calibrated on Seen validation.
- Definitive active controller: `A=0.7990124225616455`, `C=0.9`, `M=0.0`.
- Active result: **75/150 (50.0%)** versus historical same-membership **72/150 (48.0%)**, net **+3 episodes / +2.0 percentage points**.
- Paired: **11 rescues / 8 regressions / 64 persisted successes / 67 persisted failures**.
- Controller audit: **57 accepted replacements** across **36/150 episodes**, **0 selection mismatches**, **0 execution mismatches**, max selected-vs-executed action difference **0.0**.
- Exact membership: 150 expected / 150 actual / 150 unique, no missing, extra, or duplicate IDs; historical membership exact.
- `A` is Seen-calibrated. `C=0.9` is engineering-development-informed from preserved live nine-candidate OOD-development decisions, so the final 150 is **not** a pristine untouched holdout for controller hyperparameter selection.
- V1 is a current/main H10 proposal failure detector with multi-sample ACE/disagreement context; it was **not** trained on nine independently supervised counterfactual candidate outcomes.
- HARD1000 resumed safely from the preserved 249-episode state and is ongoing; intermediate HARD1000 counts are **not** final results.
- Commit `70327b4b31bde35c01fda29a807f9100b5295a62` is **invalid for historical candidate-wise alternative scores** because candidates 1–8 diffusion traces were not archived. Correction commit: `86f5baf3281596df2305409499fc9e0c21d119ed`.
