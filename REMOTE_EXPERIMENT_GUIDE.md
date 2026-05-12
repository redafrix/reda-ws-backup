# 🦾 REMOTE CONTROL & EXPERIMENT EXECUTION GUIDE
# Workspace: /media/rootalkhatib/My Passport/reda_ws (on pcrobot)

This document is the definitive handbook for any Gemini CLI session managing this workspace. It ensures resilience, precision, and 100% remote reliability, specifically hardened against SSH disconnects and file system corruption.

###############################################################################
# 1. AUTHENTICATION & NETWORK (VERIFIED)
###############################################################################

## Target Machine: pcrobot
- **User:** `rootalkhatib` (UID: 1001)
- **Sudo Password:** `Mohammad_Alkhatib_CTT_2025`
- **Tailscale IP:** `100.105.217.20`
- **SSH Alias:** `pcrobot` (Configured in `~/.ssh/config` for passwordless access)

## Critical Reliability Check (MANDATORY)
Before starting any marathon, verify that **Lingering** is enabled for the user. Without this, Ubuntu's `systemd-logind` will kill all background processes (including tmux) as soon as the last SSH session disconnects.

- **Check Status:** `loginctl show-user rootalkhatib --property=Linger`
- **Enable if 'no':** `sudo loginctl enable-linger rootalkhatib`

###############################################################################
# 2. FILE SYSTEM CAUTION: EXFAT DRIVE
###############################################################################
The workspace resides on an **exFAT external drive**. This format does NOT have a journal.
- **Risk:** If a process is killed abruptly (SIGKILL) or the OS crashes, files being written to (especially logs) will suffer from **NULL-BYTE CORRUPTION** (appearing as `^@^@^@` in text editors).
- **Mitigation:**
  1. Always use **TMUX** to ensure processes have a persistent TTY.
  2. Use `python3 -u` (unbuffered) to ensure logs are flushed to disk frequently.
  3. Ensure **Linger** is active so the OS doesn't kill the session on disconnect.

###############################################################################
# 3. EXPERIMENT PROTOCOL: THE "MARATHON" STANDARDS
###############################################################################

Every experiment in a 100-run marathon follows this structure:

1.  **Isolation:** Dedicated folder: `experiments/a_100_tests/idea_XXX/`.
2.  **Unbuffered Logging:** Launch training with `PYTHONUNBUFFERED=1` or `python3 -u`.
3.  **Log Redirection:**
    - Standard Out: `../logs_marathon/idea_XXX.log`
    - Standard Err: Redirect to the same log or a dedicated `.err` file.

###############################################################################
# 4. RESILIENCE: HOW TO LAUNCH LONG-RUNNING TASKS
###############################################################################

### The TMUX Protocol (Required)
1. **Create/Enter Session:** `tmux attach -t marathon || tmux new -s marathon`
2. **Launch:** `python3 -u train.py --epochs 1000 ...`
3. **Detach:** Press `Ctrl+b`, then `d`.
4. **Disconnect Safety:** With `Linger` enabled, you can safely shut down your local PC. The training will persist.

###############################################################################
# 5. GIT BACKUP STRATEGY (THE CHUNKED METHOD)
###############################################################################

To backup the 233GB workspace code without timing out GitHub's servers:

1.  **Strict .gitignore:** Must ignore `*.pt`, `*.zip`, `runs/`, `logs/`, and `data/`.
2.  **Buffer Increase:** `git config http.postBuffer 524288000`
3.  **Chunked Uploads:**
    - **Chunk 1:** Root files (`.py`, `.sh`, `.md`).
    - **Chunk 2:** Research directories (`00_subjects/` to `06_papers/`).
    - **Chunk 3:** Code folders (`intern_ship_ws/tdqc/`, `intern_ship_ws/simvla/`).
4.  **Nested Git Cleanup:** Before a full workspace push, find and remove nested `.git` folders (`find . -name '.git' -type d -exec rm -rf {} +`) to avoid submodule conflicts.

###############################################################################
# 6. SYSTEM HEALTH & MONITORING
###############################################################################
- **GPU Status:** `nvidia-smi` (Target: 80% usage, Temp < 85°C).
- **Process Check:** `ps aux | grep train.py`
- **Progress Audit:** `tail -f experiments/a_100_tests/logs_marathon/idea_XXX.log`

**MANAGEMENT IS 100% REMOTE. NO PHYSICAL ACCESS REQUIRED.**
