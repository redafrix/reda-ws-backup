# Implementation Plan: LIBERO-PRO Perturbation Setup

## Phase 1: Script Deployment and Initial Baseline Execution
- **Agent**: `coder`
- **Objective**: Write and deploy a Python script to Bob and Sam that systematically smoke-tests every LIBERO-PRO suite and logs the results to a JSON file. Run the script to establish the baseline failure state.
- **Tasks**:
  1. Create `smoke_test_libero.py`.
  2. Deploy it to Bob and Sam.
  3. Execute it using the respective conda environments.
  4. Fetch the resulting JSON reports.

## Phase 2: Asset and Configuration Troubleshooting
- **Agent**: `debugger`
- **Objective**: Analyze the baseline reports, locate missing assets/configs, and apply fixes (symlinks, copies, path corrections) across both machines.
- **Tasks**:
  1. Parse the JSON reports to categorize failures.
  2. Search for missing `.xml`, `.obj`, and `.pruned_init` files on both machines.
  3. Apply symlinks or copies where files are found.
  4. Fix configuration pathing issues if present.

## Phase 3: Verification and Final Reporting
- **Agent**: `technical_writer`
- **Objective**: Re-run the smoke tests to verify fixes and compile the final Markdown report.
- **Tasks**:
  1. Re-run `smoke_test_libero.py` on Bob and Sam.
  2. Analyze the final JSON reports.
  3. Generate `/home/redafrix/tests/internship/gemini_handoff_current/STAGE9_LIBERO_PRO_ALL_PERTURBATIONS_SETUP_REPORT.md` conforming exactly to the user's requested format.