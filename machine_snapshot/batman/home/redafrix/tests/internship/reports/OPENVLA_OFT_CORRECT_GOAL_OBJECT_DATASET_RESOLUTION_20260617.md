# OpenVLA-OFT Corrected Goal-Object Dataset Resolution Report

**Date:** June 17, 2026  
**Workspace:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616`  
**Target Suite:** `libero_goal_object` (10 tasks)

---

## 1. Task Suite Comparison: `libero_goal` vs. `libero_goal_object`

The incorrect collection job was launched on the standard `libero_goal` suite, which uses tasks from standard LIBERO-100.
The correct task suite required for training the SimVLA/FIPER risk detector is `libero_goal_object` (from LIBERO-PRO). The two suites have entirely disjoint task sets:

### `libero_goal_object` (10 Tasks, Correct Target)
- **Task 0:** `open the middle drawer of the cabinet`
- **Task 1:** `put the bowl on the stove`
- **Task 2:** `put the wine bottle on top of the cabinet`
- **Task 3:** `open the top drawer and put the bowl inside`
- **Task 4:** `put the bowl on top of the cabinet`
- **Task 5:** `push the plate to the front of the stove`
- **Task 6:** `put the cream cheese in the bowl`
- **Task 7:** `turn on the stove`
- **Task 8:** `put the bowl on the plate`
- **Task 9:** `put the wine bottle on the rack`

---

## 2. BDDL and Init Roots Resolution

Through auditing the configuration directories and files in `fiper_ws` and `asynchvla_ws`, the correct LIBERO-PRO environment config path has been resolved:
- **`LIBERO_CONFIG_PATH`**: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob`
- **Resolved BDDL Root**: `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/bddl_files/libero_goal_object`
- **Resolved Init Root**: `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/init_files/libero_goal_object`

Without explicitly defining `LIBERO_CONFIG_PATH`, standard libero loads from the system-wide site-packages path, causing BDDL definition KeyErrors (e.g. `KeyError: 'wine_rack_stand_1_top_region'`). Setting the environment variable forces the environment wrapper to correctly reference the LIBERO-PRO workspace paths.

---

## 3. Seed Resets & Initial State Indexing Plan

To align with the baseline data sweeps, the dataset collector utilizes the following convention:
1. **Reset Seeds**: A deterministic sequence where `reset_seed = 100000 + round_idx` is used for environment initialization. For each round `r`, all 10 tasks in the sweep share the same seed.
2. **Initial State Indexing**: The initial state for each task is selected from the pre-recorded 50 initial states using:
   ```python
   initial_state = init_states[round_idx % len(init_states)]
   ```

---

## 4. History Window & Feature Schema Details

The dataset records are designed to support sequence transformer risk models while cleanly omitting SimVLA uncertainty features (`ACE_AVAILABLE = NO`, `SIMVLA_UNCERTAINTY_FEATURES_AVAILABLE = NO`).

### Rolling History Buffer (Size K=8)
For each environment timestep `t`:
- `prev_proprio_states`: list of last 8 proprioception vectors (each of length 8).
- `prev_executed_actions`: list of last 8 actual actions executed (each of length 7).
- `prev_query_action_statistics`: list of last 8 action chunks' statistics.

### OpenVLA Action-Stat Features
Because OpenVLA-OFT evaluates with a native prediction and execution horizon of 8, we calculate and log the following statistics for the full predicted chunk of 8 actions at each query:
- `mean`: Average predicted action value.
- `std`: Standard deviation of the action chunk.
- `min`/`max`: Boundary values in the predicted chunk.
- `l1_norm`: L1 norm of the predicted actions.
- `l2_norm`: L2 (Euclidean) norm of the predicted actions.

This provides the downstream risk model with full observability of policy behavior without faking any SimVLA-specific ACE inputs.
