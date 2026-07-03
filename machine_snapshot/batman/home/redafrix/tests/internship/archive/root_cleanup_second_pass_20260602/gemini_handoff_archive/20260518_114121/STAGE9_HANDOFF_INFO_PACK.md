# STAGE 9 HANDOFF INFO PACK — SimVLA / LIBERO-PRO Action-Risk Data

Generated: `2026-05-18T11:43:12`
Hostname: `Bob` (Remote)
Git Status: Clean (No modifications in this session)

## SECTION 1 — Current status summary

Stage 9 has successfully built the infrastructure for same-state counterfactual data collection using LIBERO-PRO and SimVLA, but it is **NOT ready for final large-scale collection**.

### Status Overview
- **Implementation:** Complete 4-class evidence-based labeler, target/goal parser, counterfactual execution harness, and validation suite.
- **Rule Validation:** 10/10 synthetic rule unit tests PASS. Logic is semantically correct.
- **System Integrity:** Reset determinism and SimVLA seed diversity are verified.
- **Pilot Quality:** **FAIL**. The latest real SimVLA pilot collapsed to two classes (`GOOD_WEAK` and `AMBIGUOUS`).
- **LABELER_READY_FOR_FINAL_COLLECTION:** **NO**.

### Current Label Distribution (Latest Pilot: `harder_later_state_v3`)
- `GOOD_STRONG`: 0
- `GOOD_WEAK`: 166
- `BAD`: 0
- `AMBIGUOUS`: 122
- **Total Samples:** 288

### The Blocker
The labeler no longer accepts "EEF approach to any object" as strong evidence (it's now `GOOD_WEAK`). Because the current collector samples rollout steps linearly, it mostly captures the early approach phase where SimVLA actions are valid but don't yet achieve task-relevant object/goal progress or clear failures. We lack a **phase-selective state sampler** to capture the high-information events (grasp, lift, transport, place, and failure-prone moments).

---

## SECTION 2 — File tree and code locations

### Source Code (`asynchvla_ws/src/data_collection_stage9/`)
- `task_parser.py`: Extracts target object and goal/receptacle from task language.
- `label_rules.py`: The core labeling logic (v6).
- `outcome_metrics.py`: Computes delta distances and height changes.
- `collect_counterfactual_dataset.py`: Main loop for same-state reset and SimVLA action evaluation.
- `run_rule_unit_tests.py`: Harness for synthetic rule validation.
- `sim_state_utils.py`: MuJoCo state serialization/deserialization.
- `history_buffer.py`: Manages the K-step history window for SimVLA input.
- `simvla_candidate_sampler.py`: Interfaces with the SimVLA model to get diverse action seeds.

### Data & Reports (`asynchvla_ws/stage9_libero_pro_risk_data/`)
- `data/pilot/`: Stores `.jsonl` samples and `.pt` history.
- `reports/`: Markdown reports for every validation step.
- `visual_debug/`: Before/after images for every labeled sample.
- `schemas/`: Sample and evidence JSON schemas.

---

## SECTION 3 — Current labeler details

**Rule Version:** `stage9_rules_v6_four_class_evidence`

### Label Classes & Evidence
1. **`GOOD_STRONG`**:
   - Success within horizon H.
   - Target object moved closer to goal (`target_to_goal_delta < -0.025`).
   - Target object lifted (`target_height_delta > 0.025`).
   - Task-correct motion (`target_motion > 0.045` with goal alignment).

2. **`GOOD_WEAK`**:
   - EEF approaches target object (`target_to_eef_delta < -0.020`).
   - Gripper closes near target.
   - Small target motion below strong thresholds.

3. **`BAD`**:
   - Target object drop (`height_drop > 0.10`).
   - Target moved away from goal (`delta > 0.06`).
   - EEF moved away from target during approach.
   - Stuck/No progress (zero reward AND zero motion for H).

4. **`AMBIGUOUS`**:
   - Target parsing failed.
   - Conflicting evidence.
   - Only non-target objects moved.
   - Signal insufficient for classification.

### Decision Logic
- **Priority:** `BAD` > `GOOD_STRONG` > `GOOD_WEAK` > `AMBIGUOUS`.
- **Target Awareness:** Rules are restricted to the parsed `target_base` object.
- **Evidence Requirement:** `GOOD_STRONG` and `BAD` require significant evidence; anything else falls to `GOOD_WEAK` or `AMBIGUOUS`.

---

## SECTION 4 — Task parsing / goal parsing status

### Target Parser (`task_parser.py`)
- **Mechanism:** Combines task language (regex/keyword) with environment observation keys.
- **Capabilities:** Identifies the `target_base` (e.g., `alphabet_soup_1`) and `goal_base` (e.g., `basket_1`).
- **Success Rate:** High on simple "Pick and Place" or "Open" tasks.
- **Parsed Metadata Example:**
  ```json
  {
    "target_base": "alphabet_soup_1",
    "goal_base": "basket_1",
    "relation": "place_or_put",
    "parse_confidence": "MEDIUM"
  }
  ```
- **Limitations:** Fails on complex spatial relations ("between X and Y") or tasks where the goal is a vague "table".

---

## SECTION 5 — Simulator signals available

Confirmed signals accessible via `robosuite` wrappers:
- **`reward`**: Summed over horizon H.
- **`success`**: Final state check.
- **`eef_pos`**: End-effector 3D position.
- **`gripper_qpos`**: Open/closed status.
- **`object_pos`**: 3D positions of all objects in scene.
- **`target_height`**: Z-coordinate of the parsed target.
- **`contacts`**: Raw MuJoCo contact list (currently diagnostic only).
- **`sim_state`**: Full `mujoco_flat` state for resets.
- **`images`**: `agentview` and `eye_in_hand` (Before and After saved).

---

## SECTION 6 — Rule unit tests

Summary of `stage9_rule_unit_test_summary.md`:
- **Result:** 10/10 PASS.
- **Tests Covered:**
  1. `success`: Triggers `GOOD_STRONG`.
  2. `eef_approach`: Triggers `GOOD_WEAK`.
  3. `wrong_object`: Triggers `AMBIGUOUS`.
  4. `object_lift`: Triggers `GOOD_STRONG`.
  5. `object_drop`: Triggers `BAD`.
  6. `goal_distance`: Triggers `GOOD_STRONG`.
  7. `no_progress`: Triggers `BAD`.
  8. `contact`: Triggers `AMBIGUOUS` (not confident yet).
  9. `gripper_relation`: Triggers `GOOD_WEAK`.
  10. `mixed_signal`: Triggers `BAD` (Bad overrides Good).

---

## SECTION 7 — Current pilot dataset details

- **Path:** `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/harder_later_state_v3`
- **Stats:** 288 samples from 36 unique states (8 seeds each).
- **Tasks:** `libero_object_with_mug`, `libero_spatial_with_mug`, `libero_goal_with_mug` (Task IDs 0 & 1).
- **Configuration:** Horizon $H=20$, History $K=8$.
- **Sample Schema:**
  - `metadata`: suite, task, seed, step.
  - `history`: $K \times (image, proprio)$.
  - `candidate_action`: SimVLA raw action.
  - `outcome`: $\Delta$ distances, $\Delta$ height, reward_sum.
  - `label`: Class name + reason evidence.

---

## SECTION 8 — Visual/debug artifacts

- **Before Images:** Saved for every sample.
- **After Images:** Saved for every sample (recently added).
- **Folders:** Grouped by pilot name under `visual_debug/`.
- **Finding Examples:** The visual report `stage9_visual_label_debug_v3.md` provides links to `GOOD_WEAK` and `AMBIGUOUS` examples.

---

## SECTION 9 — Collection logic and current weakness

### Current Logic
- Rollout a parent episode using SimVLA.
- Sample states at fixed intervals (e.g., every 20 or 40 steps).
- Reset simulator to each state and execute $N$ different seeds for $H$ steps.
- Label based on $H$-step outcome.

### The Weakness
- **Linear Sampling:** Uniformly sampling steps misses the critical "inflection points" of the task.
- **No Phase Awareness:** Does not know if it's currently grasping or transporting.
- **Consequence:** 90% of samples are "approaching target", which results in `GOOD_WEAK` and produces a dataset that doesn't help the model distinguish between strong success and risk.

---

## SECTION 10 — LIBERO-PRO task availability

Available suites confirmed on Bob:
- `libero_object_with_mug`
- `libero_spatial_with_mug`
- `libero_goal_with_mug`
- `libero_goal_lan`
- `libero_goal_object`
- `libero_object_env`

Tasks used in Stage 9: Primarily Task ID 0 and 1 from the first three suites.

---

## SECTION 11 — Commands used so far / commands available

### Rule Validation (Safe/Tiny)
```bash
python3 -m data_collection_stage9.run_rule_unit_tests
```

### Pilot Collection (Longer/Long)
```bash
python3 -m data_collection_stage9.collect_counterfactual_dataset \
  --suites libero_object_with_mug libero_spatial_with_mug libero_goal_with_mug \
  --task-ids 0 1 --states-per-task 6 --simvla-seeds 0 1 2 3 4 5 6 7 \
  --horizon 20 --history-k 8 --parent-roll-steps 40 \
  --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/harder_later_state_v3 --save-images
```

### Analysis (Safe/Tiny)
```bash
python3 -m data_collection_stage9.analyze_dataset_quality --input-dir <path>
```

---

## SECTION 12 — What ChatGPT should decide next

### The Problem
We have the labeling **engine** but we lack the **fuel** (diverse high-information states).

### Recommended Next Steps
1. **Implement Phase-Selective Sampling:**
   - Modify `collect_counterfactual_dataset.py` to use a phase classifier.
   - Define phases in `outcome_metrics.py`: `APPROACH`, `GRASP`, `LIFT`, `TRANSPORT`, `PLACE`.
   - Sample $N$ states per phase instead of $N$ states per episode.
2. **Improve Target/Goal Parsing:**
   - Enhance `task_parser.py` to handle more LIBERO-PRO tasks, especially those where the goal is not a named object (e.g., "the plate").
3. **Verify with a "Balanced" Pilot:**
   - The next success criterion should be a pilot with at least 15% `GOOD_STRONG` and 15% `BAD` labels.

### Files to Modify
- `asynchvla_ws/src/data_collection_stage9/collect_counterfactual_dataset.py`
- `asynchvla_ws/src/data_collection_stage9/outcome_metrics.py`

---
**Handoff Path:** `/home/redafrix/tests/internship/gemini_handoff_current/STAGE9_HANDOFF_INFO_PACK.md`
**Archive Path:** `/home/redafrix/tests/internship/gemini_handoff_archive/20260518_114121/STAGE9_HANDOFF_INFO_PACK.md`
