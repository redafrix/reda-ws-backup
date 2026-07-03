# 🚀 EXHAUSTIVE TECHNICAL REPORT: FIPER High-Diversity Sweep Deployment

**Date:** Friday, May 22, 2026
**Full File Path:** `/home/redafrix/tests/internship/BOB_FIX_HANDOVER.md`
**Nodes:** Sam (PCROBOTUBUNTU05) & Bob (PCROBOTUBUNTU02)
**User:** `rootalkhatib`

---

## 1. STRATEGIC MISSION & GOALS

### The "High-Diversity Sweep" Logic
The primary goal was to deploy a new data collection strategy for the FIPER (Failure Prediction) campaign. Previous collections focused on high-volume sequential episodes per task. This session transitioned to a **Round-Robin Sweep** strategy:
- **Main Goal:** Maximize environmental and task diversity in the first 24 hours of collection.
- **Mechanism:** Instead of 200 episodes for Task 1, then 200 for Task 2, the collector now performs `Sweep 1 (Task 1, Task 2... Task N)`, then `Sweep 2`, etc.
- **Scope:** 12 LIBERO-PRO suites assigned across two high-performance nodes (Sam and Bob).

### Technical Constraints
- **ACE Candidates:** Reduced from 64 to **8** to prioritize speed over candidate precision (since we are executing the first action only).
- **Timeouts:** Episode timeout reduced to **300 steps** (down from 400) to prune "stuck" episodes.
- **Execution:** Receding Horizon (1st action only) using the SimVLA-modified model.

---

## 2. CHRONOLOGICAL EXECUTION LOG

### Phase 1: Sam Deployment (Success)
1.  **Code Deployment:** Created `collect_fiper_receding_all_outcomes_v2.py` with nested suite/task loops.
2.  **Environment Check:** Verified Sam's internal NVMe environment at `/home/rootalkhatib/envs/simvla`.
3.  **Launch:** Executed `fiper_sweep_sam.sh`.
    - **Instance A (Mug Suites):** Successfully launched (PID 3182724).
    - **Instance B (Milk Suites):** Successfully launched (PID 3182725).
4.  **Verification:** Confirmed logs are generating in `.../stage9_libero_pro_risk_data/campaigns/fiper_sweep_20260522`.

### Phase 2: Bob Deployment (Initial Blockers)
Bob's workspace is located on an external SSD (`/media/rootalkhatib/My Passport/`). This introduced significant shell and Python pathing issues.

1.  **Space in Path:** Shell scripts failed to parse the space in "My Passport".
    - **Fix:** Created `/tmp/bob_libero_pro`, `/tmp/bob_site_packages`, and `/tmp/bob_src` as **symlinks** pointing to the real paths on the SSD.
2.  **The Numba/Coverage Crisis:** 
    - **Error:** `AttributeError: module 'coverage' has no attribute 'types'` inside `numba`.
    - **Root Cause:** Bob's system Python was loading an ancient `coverage` version (6.2) from `/usr/lib/python3/dist-packages` instead of the one required by `robosuite`.
    - **Fix:** Manually `rsync`'d `coverage` (7.13.0) from Batman's local site-packages to Bob's `/tmp/bob_site_packages`.
3.  **NumPy/Matplotlib Collision:**
    - **Error:** `ImportError: numpy.core.multiarray failed to import` and `AttributeError: _ARRAY_API not found`.
    - **Root Cause:** A mismatch between compiled C-extensions in Bob's synced `site-packages` and the system's `matplotlib`.
    - **Fix:** Synced `matplotlib` (3.10.8) and a fresh `numpy` (2.2.6) from Sam to Bob using a `tar` pipe over SSH.

### Phase 3: The "Torch Corruption" Investigation
During import testing, Bob reported a `libpng16` error and a `MatplotlibBackend` error in `sympy`.

1.  **Audit:** Discovered Bob's `torch` directory was **15GB**, while Sam's was only **1.6GB**. This suggested Bob's external drive had a corrupted or bloated installation.
2.  **Resolution:** 
    - Renamed Bob's `torch` to `torch_old`.
    - `rsync`'d a verified `torch` (2.5.1+cu121) from Batman to Bob.
    - Verified size on Bob dropped back to 1.6GB.

### Phase 4: Current Dependency "Handoff" State
Bob is currently failing on the final set of ML imports.
- **Last Error:** `ModuleNotFoundError: No module named 'transformers.configuration_utils'`.
- **Reason:** The sync was incomplete. `transformers`, `accelerate`, `timm`, and `tokenizers` are still missing from the local site-packages.
- **Network Hurdle:** Sam cannot SSH into Bob directly (`Temporary failure in name resolution`), so all syncs must be "bridged" through Batman (the machine running this session).

---

## 3. ARCHITECTURAL OVERVIEW (FOR THE NEXT SESSION)

### Bob's Hybrid File System
Bob is a Frankenstein of paths. You MUST use these variables in your shell:
- `LIBERO_PRO_PATH="/tmp/bob_libero_pro"`
- `SITE_PACKAGES="/tmp/bob_site_packages"`
- `SRC_PATH="/tmp/bob_src"`
- `SIMVLA_PATH="/tmp/bob_simvla"` (New symlink needed for `SimVLA_modified`)

### The `PYTHONPATH` Requirement
To run the collector on Bob, the `PYTHONPATH` must be exactly:
`export PYTHONPATH="${SIMVLA_PATH}:${LIBERO_PRO_PATH}:${SRC_PATH}:${SITE_PACKAGES}:${PYTHONPATH}"`

---

## 4. ACTION ITEMS FOR CONTINUATION

### Step 1: Complete the "Great Sync"
Finish syncing the remaining ML libraries from Sam to Bob. Since Sam can't see Bob, do it in two steps:
1. `ssh sam "tar -czf - -C /home/rootalkhatib/envs/simvla/lib/python3.10/site-packages transformers tokenizers huggingface_hub safetensors accelerate diffusers timm einops peft pydantic" > /tmp/ml_stack.tar.gz`
2. `ssh pcrobot "tar -xzf - -C /tmp/bob_site_packages" < /tmp/ml_stack.tar.gz`

### Step 2: Establish the SimVLA Symlink
Bob's collector depends on `models.modeling_smolvlm_vla`.
`ssh pcrobot "ln -sf '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified' /tmp/bob_simvla"`

### Step 3: The Final Validation
Run the following check. If it prints "ALL OK", you are ready to launch.
```bash
ssh pcrobot "export PYTHONPATH='/tmp/bob_simvla:/tmp/bob_libero_pro:/tmp/bob_src:/tmp/bob_site_packages'; /usr/bin/python3 -c 'import torch; import transformers; from data_collection_stage9.collect_fiper_receding_all_outcomes_v2 import main; print(\"ALL OK\")'"
```

### Step 4: Launch Bob
`ssh pcrobot "cd /tmp/bob_src && bash stage9_v2_tools/scripts/fiper_sweep_bob.sh"`

---

## 5. RECENT TERMINAL TRACES (FOR DEBUGGING)

**Last failed trace on Bob:**
```python
ImportError: cannot import name 'MatplotlibBackend' from 'sympy.plotting.backends.matplotlibbackend' (unknown location)
ModuleNotFoundError: No module named 'history_buffer'
ModuleNotFoundError: No module named 'models'
```
*Note: I fixed the `MatplotlibBackend` by syncing `sympy`, but `models` and `history_buffer` require the `SimVLA_modified` path to be in `PYTHONPATH`.*

---

**END OF REPORT**
