# Receding Dataset Inventory & Validation Report

This report contains validation metrics for all Sam receding-horizon and consolidated Bob datasets.

## Dataset: sam_instance_A
- **Path:** `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_receding_all_outcomes_20260521_165452/data/instance_A/fiper_receding_samples.jsonl`
- **Row Count:** 4082
- **Episode Count:** 16
- **Success Episodes / Rows:** 9 / 1282
- **Failure/Timeout Episodes / Rows:** 7 / 2800
- **Episode Lengths (Min/Mean/Max):** 72 / 255.1 / 400
- **Confirm `ace_replay_used == false`:** `True`
- **Confirm 64 ACE Candidate Chunks:** `True`
- **Confirm First Action Executed:** `True`
- **Corrupt Rows:** 0
- **Unique Main Seeds:** 4082
- **Unique ACE Seeds:** 261224
- **Missing Fields:** None

### Rows per Suite/Task
| Suite:Task | Rows |
|---|---|
| libero_spatial_with_mug:task_0 | 4082 |

### ACE Candidate Count Distribution
| Candidates | Rows |
|---|---|
| 64 | 4082 |

========================================

## Dataset: sam_instance_B
- **Path:** `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_receding_all_outcomes_20260521_165452/data/instance_B/fiper_receding_samples.jsonl`
- **Row Count:** 4227
- **Episode Count:** 20
- **Success Episodes / Rows:** 15 / 2227
- **Failure/Timeout Episodes / Rows:** 5 / 2000
- **Episode Lengths (Min/Mean/Max):** 107 / 211.3 / 400
- **Confirm `ace_replay_used == false`:** `True`
- **Confirm 64 ACE Candidate Chunks:** `True`
- **Confirm First Action Executed:** `True`
- **Corrupt Rows:** 0
- **Unique Main Seeds:** 4227
- **Unique ACE Seeds:** 270515
- **Missing Fields:** None

### Rows per Suite/Task
| Suite:Task | Rows |
|---|---|
| libero_goal_with_mug:task_0 | 4227 |

### ACE Candidate Count Distribution
| Candidates | Rows |
|---|---|
| 64 | 4227 |

========================================

## Dataset: bob_instance_A
- **Path:** `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/consolidated_bob_data/instance_A/fiper_receding_samples.jsonl`
- **Row Count:** 4047
- **Episode Count:** 14
- **Success Episodes / Rows:** 5 / 447
- **Failure/Timeout Episodes / Rows:** 9 / 3600
- **Episode Lengths (Min/Mean/Max):** 75 / 289.1 / 400
- **Confirm `ace_replay_used == false`:** `True`
- **Confirm 64 ACE Candidate Chunks:** `True`
- **Confirm First Action Executed:** `True`
- **Corrupt Rows:** 0
- **Unique Main Seeds:** 4047
- **Unique ACE Seeds:** 258988
- **Missing Fields:** None

### Rows per Suite/Task
| Suite:Task | Rows |
|---|---|
| libero_spatial_with_mug:task_0 | 4047 |

### ACE Candidate Count Distribution
| Candidates | Rows |
|---|---|
| 64 | 4047 |

========================================

## Dataset: bob_instance_B
- **Path:** `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/consolidated_bob_data/instance_B/fiper_receding_samples.jsonl`
- **Row Count:** 4110
- **Episode Count:** 24
- **Success Episodes / Rows:** 21 / 2910
- **Failure/Timeout Episodes / Rows:** 3 / 1200
- **Episode Lengths (Min/Mean/Max):** 110 / 171.2 / 400
- **Confirm `ace_replay_used == false`:** `True`
- **Confirm 64 ACE Candidate Chunks:** `True`
- **Confirm First Action Executed:** `True`
- **Corrupt Rows:** 0
- **Unique Main Seeds:** 4110
- **Unique ACE Seeds:** 263025
- **Missing Fields:** None

### Rows per Suite/Task
| Suite:Task | Rows |
|---|---|
| libero_goal_with_mug:task_0 | 4110 |

### ACE Candidate Count Distribution
| Candidates | Rows |
|---|---|
| 64 | 4110 |

========================================
