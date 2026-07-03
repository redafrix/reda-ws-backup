# Design Document: LIBERO-PRO Perturbation Validation and Setup

## Objective
Make every available LIBERO-PRO perturbation suite work on both Bob (`/media/rootalkhatib/My Passport/reda_ws`) and Sam (`/home/rootalkhatib/test/reda_ws`) for future SimVLA data collection.

## Scope
- Discover all registered suites.
- Run a minimal smoke test (init, reset, get instruction, 1 action step) for every task in every suite on both machines.
- Identify failures (missing XML/OBJ, missing `.pruned_init`, incorrect config paths).
- Apply safe fixes (symlinking, copying, path correction).
- Generate a comprehensive status report.
- STRICTLY NO training, NO long data collection, NO overwriting datasets.

## Architecture & Implementation Strategy
1. **Smoke Testing Script (`smoke_test_suites.py`)**: A standalone python script to be executed on Bob and Sam. It will iterate over the suites identified in `libero.benchmark.__init__.py` and attempt to load each environment. The script will catch exceptions and output a structured JSON report detailing success or the specific type of failure for each task.
2. **Analysis and Fix Generation**: The orchestrator/agents will parse the JSON reports.
    - For path issues: Correct configuration files or environment variables.
    - For missing assets: Deep search both machines. If found, symlink or copy them into the correct location.
    - For missing init files: Search for them or investigate safe generation scripts if available in the repo.
3. **Verification**: Re-run the smoke test script to confirm fixes.
4. **Reporting**: Aggregate the final state into `/home/redafrix/tests/internship/gemini_handoff_current/STAGE9_LIBERO_PRO_ALL_PERTURBATIONS_SETUP_REPORT.md`.

## Workspaces
- Bob: `/media/rootalkhatib/My Passport/reda_ws`
- Sam: `/home/rootalkhatib/test/reda_ws`
- SSH Aliases: `pcrobot` (Bob), `sam` (Sam)