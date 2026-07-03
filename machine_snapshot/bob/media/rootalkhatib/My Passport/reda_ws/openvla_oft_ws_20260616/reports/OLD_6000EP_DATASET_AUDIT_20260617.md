# Dataset Audit: Old ~6000 Episode Dataset

This audit report summarizes the key statistics, features, and task specifications of the old dataset identified for training the offline risk baseline model.

---

## 1. Metadata and Paths
* **Dataset Directory:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded`
* **Suite Name:** `libero_goal` (Note: This is the plain `libero_goal` suite, not the `libero_goal_object` / pro suite. This run is used for offline diagnostic risk-model training only).
* **Model Used:** `moojink/openvla-7b-oft-finetuned-libero-goal`
* **Prediction Horizon ($H$):** 8
* **Temporal Window Size ($K$):** 8
* **Feature Schema:**
  - **ACE_AVAILABLE:** NO
  - **SIMVLA_UNCERTAINTY_FEATURES_AVAILABLE:** NO
  - **OPENVLA_ACTION_STAT_FEATURES_AVAILABLE:** YES

---

## 2. Line Counts & Completeness
* **Episode Summaries (`episode_summaries.jsonl`):** 6,009 rows
* **Query Records (`query_records.jsonl`):** 101,550 rows
* **Step Records (`step_records.jsonl`):** 791,525 rows

---

## 3. Outcomes & Task Distribution
* **Total Episodes:** 6,009
* **Successful Episodes:** 5,828 (97.0%)
* **Failed Episodes:** 181 (3.0%)

### Task Distribution
All tasks in the 10-task suite have a balanced distribution of ~600 episodes:
1. `open the middle drawer of the cabinet`: 601 episodes
2. `open the top drawer and put the bowl inside`: 601 episodes
3. `push the plate to the front of the stove`: 601 episodes
4. `put the bowl on the plate`: 601 episodes
5. `put the bowl on the stove`: 601 episodes
6. `put the bowl on top of the cabinet`: 601 episodes
7. `put the cream cheese in the bowl`: 601 episodes
8. `put the wine bottle on the rack`: 600 episodes
9. `put the wine bottle on top of the cabinet`: 601 episodes
10. `turn on the stove`: 601 episodes

---

## 4. Assessment for Risk Model Training
* **Episode success/failure labels:** Present and verified.
* **Per-query / Per-step records:** Fully complete and aligned.
* **Executed actions & Proprio:** Available at every step.
* **History fields:** The `history` field in `step_records.jsonl` contains a rolling window of size $K=8$ of previous proprio states, executed actions, and query action statistics.
* **Safety to Use:** The dataset contains all necessary fields for training a risk classifier. Due to the high success rate (97%), care must be taken to address class imbalance (3% failure rate) during model training.
