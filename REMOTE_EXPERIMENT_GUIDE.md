# 🦾 REMOTE CONTROL & EXPERIMENT EXECUTION GUIDE
# Workspace (Current): /media/rootalkhatib/My Passport/reda_ws (on pcrobot)
# Workspace (Fallback): /media/redafrix/My Passport/reda_ws (on Batman)

This document is the definitive handbook for any Gemini CLI session managing this workspace. It ensures resilience, precision, and 100% remote reliability.

###############################################################################
# 1. AUTHENTICATION & NETWORK (VERIFIED)
###############################################################################

## Target Machines
- **Batman (Local Workspace Host):**
  - **User:** `redafrix`
  - **Sudo Password:** `cvbn,;:!`
  - **Tailscale IP:** `100.100.216.15`
- **pcrobotubuntu02 (Bob - Remote Assistant):**
  - **User:** `rootalkhatib`
  - **Sudo Password:** `Mohammad_Alkhatib_CTT_2025`
  - **Tailscale IP:** `100.105.217.20`
  - **Local IP:** `172.16.8.104`
  - **SSH Alias:** `pcrobot` (Configured in `~/.ssh/config` for passwordless access)
- **pcrobotubuntu05 (Sam - Remote Assistant):**
  - **User:** `rootalkhatib`
  - **Sudo Password:** `Mohammad_Alkhatib_CTT_2025`
  - **Tailscale IP:** `100.112.19.30`
  - **Local IP:** `172.16.8.107`
  - **SSH Alias:** `sam` (Configured in `~/.ssh/config` for passwordless access)

## Global Access & Automation
- Tailscale is **ACTIVE**.
- Passwordless SSH is **CONFIGURED**. 
- **Aliases:**
  - `bob "command"` -> Runs any command on Bob (e.g., `bob "ls -la"`).
  - `remsmi` -> Quick check of Bob's GPU status.
  - `sam "command"` -> Runs any command on Sam (e.g., `sam "ls -la"`).
  - `remsmi_sam` -> Quick check of Sam's GPU status.

###############################################################################
# 2. GIT WORKFLOW: MULTI-NODE SYNCHRONIZATION
###############################################################################

To prevent code drift and manage experiments across multiple machines, follow this branching strategy:

1.  **Node-Specific Branches:**
    - **Bob (pcrobot):** Always operates on the `bob` branch.
    - **Sam (pcrobotubuntu05):** Always operates on the `sam` branch.
2.  **The "Merge-and-Sync" Protocol:**
    - When you want to synchronize both machines:
      1.  Commit and push changes from `bob` and `sam` to their respective remote branches.
      2.  Merge both `bob` and `sam` into the `main` branch (Resolve any conflicts here).
      3.  Push the updated `main` branch to GitHub.
      4.  On both nodes, pull `main` back into the local `bob` and `sam` branches:
          - `git checkout bob && git pull origin main`
          - `git checkout sam && git pull origin main`
3.  **Rule:** Never commit directly to `main` unless it is a merge from a node-specific branch.

###############################################################################
# 3. EXPERIMENT PROTOCOL: THE "CAPSULE" STANDARDS
###############################################################################

To maintain causality and reproducibility, every experiment **MUST** follow these rules:

1.  **Isolation:** Create a dedicated folder: `experiments/v8_expXX/`.
2.  **Code Locality:** Copy all training and model code into `experiments/v8_expXX/code/`. Never run from the central source during a production experiment.
3.  **Unbuffered Logging:** Every `print()` statement in training scripts must use `flush=True`.
4.  **Causality:** STRICT ban on non-causal normalization. Always use global training statistics collected at the start of the run.
5.  **Output Redirection:** Always redirect `stdout` and `stderr` to `../outputs_v1/training.log`.

###############################################################################
# 3. RESILIENCE: HOW TO LAUNCH LONG-RUNNING TASKS
###############################################################################

**NEVER** run a training loop directly in the primary CLI shell. If the connection drops, the process dies.

### Standard Launch (Detached):
```bash
nohup python3 train_tdqc.py [ARGS] > ../outputs_v1/training.log 2>&1 &
```

### The TMUX Protocol (Preferred for Interactive Debugging):
1. **Create Session:** `tmux new -s expXX_run`
2. **Launch:** Run your training script.
3. **Detach:** Press `Ctrl+b`, then `d`.
4. **Reconnect:** `tmux attach -t expXX_run`.

**System Status:**
- Sleep/Suspend: **DISABLED**.
- Lid Close: **IGNORED**.
- The machine will remain awake and reachable 24/7.

###############################################################################
# 4. GRANULAR EVALUATION & REPORTING
###############################################################################

Every evaluation must produce detailed tables for the following intervals:
- **Steps:** 10, 12, 15, 50, 100, 150, 200, 300, and Overall.
- **Metrics:** Accuracy (Acc), Brier Score (Brier), AUC-ROC (AUC), and Sample Count (N).
- **Datasets:**
  1. `v8_test.pt` (Standard Test Set)
  2. `v8_unseen_obj_ood.pt` (OOD Unseen Objects)
- **Proactivity Logic:** Use **Horizon Max-Pooling** (`max()` probability from step 0 to target step) to credit the model for early warnings.

###############################################################################
# 5. TROUBLESHOOTING
###############################################################################

- **`spawn ENOENT`:** Restart the CLI session or verify the execution path.
- **Environment:** Always use the SSD-based environment: `/home/redafrix/envs/simvla`.
- **Activation:** `source intern_ship_ws/activate_simvla.sh`.
- **GPU Not Found:** Re-run the activation script; it handles the CUDA pathing for the hybrid external/internal setup.

**MANAGEMENT IS 100% REMOTE. NO MANUAL INTERVENTION REQUIRED ON THE PHYSICAL PC.**
###############################################################################
