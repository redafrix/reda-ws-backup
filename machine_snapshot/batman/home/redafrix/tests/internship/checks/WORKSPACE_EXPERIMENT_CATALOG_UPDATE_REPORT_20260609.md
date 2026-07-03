# Workspace Experiment Catalog Audit & Update Report

> [!IMPORTANT]
> This report documents the workspace-wide experiment catalog audit and update completed on 2026-06-09. No experiments were launched, no raw data was moved or deleted, and no running jobs were affected.

---

## 1. Executive Summary

The experiment catalogs across 4 machines (Batman, Bob, Dean, Sam) have been audited and updated. The update incorporates findings from the 8-step forensic audit (Steps 1–8) and adds 7 new catalog documents, updates 3 existing documents, and syncs the updated catalog to Bob and Dean.

**Key outcomes:**
- All 4 hosts verified reachable (Dean via ProxyJump only)
- Sam is back online (was previously listed as offline)
- 7 new catalog files created on Batman and synced to Bob + Dean
- 3 existing files updated with forensic corrections
- Backups created for all modified files
- Obsidian Vault report cross-checked and discrepancies documented

---

## 2. Host Reachability

| Host | Method | Status | GPU | Hostname |
| :--- | :--- | :--- | :--- | :--- |
| **Batman** (local) | N/A | ✅ Online | RTX 4060 (8 GB) | Batman |
| **Bob** | `ssh pcrobot` | ✅ Online | RTX 4070 (16 GB) | PCROBOTUBUNTU02 |
| **Dean** | `ssh dean` (direct) | ❌ Timeout | — | — |
| **Dean** | `ssh dean-via-bob` (ProxyJump) | ✅ Online (~2s) | RTX A5000 (24 GB) | Batman |
| **Sam** | `ssh sam` | ✅ Online | RTX 4070 (16 GB) | PCROBOTUBUNTU05 |

---

## 3. Files Created

| File | Purpose |
| :--- | :--- |
| [TRUSTED_RESULTS_SUMMARY.md](file:///home/redafrix/tests/internship/fiper_ws/experiment_catalog/TRUSTED_RESULTS_SUMMARY.md) | Forensic-verified results with corrected intervention rates and trust verdicts |
| [MASTER_EXPERIMENT_INDEX.md](file:///home/redafrix/tests/internship/fiper_ws/experiment_catalog/MASTER_EXPERIMENT_INDEX.md) | Central table of all online, offline, and data collection campaigns |
| [DATASET_MAP.md](file:///home/redafrix/tests/internship/fiper_ws/experiment_catalog/DATASET_MAP.md) | All known datasets across hosts with provenance chain |
| [HOST_WORKSPACE_MAP.md](file:///home/redafrix/tests/internship/fiper_ws/experiment_catalog/HOST_WORKSPACE_MAP.md) | Host details: SSH configs, GPUs, paths, datasets, and roles |
| [MODEL_AND_SUITE_IDENTITY.md](file:///home/redafrix/tests/internship/fiper_ws/experiment_catalog/MODEL_AND_SUITE_IDENTITY.md) | Checkpoint/detector SHA256 hashes and LIBERO-PRO suite verification |
| [FORENSIC_AUDIT_MAP.md](file:///home/redafrix/tests/internship/fiper_ws/experiment_catalog/FORENSIC_AUDIT_MAP.md) | Map of the 8-step forensic audit with local/remote paths and verdicts |
| [OBSIDIAN_REPORT_ACCURACY_AUDIT_20260609.md](file:///home/redafrix/tests/internship/fiper_ws/experiment_catalog/OBSIDIAN_REPORT_ACCURACY_AUDIT_20260609.md) | Cross-check of Obsidian Vault report claims against forensic evidence |

## 4. Files Updated

| File | Changes |
| :--- | :--- |
| [KEY_RESULTS.md](file:///home/redafrix/tests/internship/fiper_ws/experiment_catalog/KEY_RESULTS.md) | Added OOD goal-swap results (net negative), forensic corrections (intervention rates), updated active work status, forensic audit verdict summary |
| [README.md](file:///home/redafrix/tests/internship/fiper_ws/experiment_catalog/README.md) | Added links to 7 new files, added semantic corrections for intervention rate and OOD failure, updated timestamp |
| [SYNC_STATUS.md](file:///home/redafrix/tests/internship/fiper_ws/experiment_catalog/SYNC_STATUS.md) | Updated Sam status to online, documented new file list, updated Dean routing, added file change log |

## 5. Backups Created

All pre-update versions saved in `experiment_catalog/`:
- `README.md.20260609_115800.bak`
- `KEY_RESULTS.md.20260609_115800.bak`
- `WORKSPACE_MAP.md.20260609_115800.bak`
- `inventory.json.20260609_115800.bak`

---

## 6. Synchronization Status

| Host | Catalog Location | Sync Status |
| :--- | :--- | :--- |
| **Batman** | `/home/redafrix/tests/internship/fiper_ws/experiment_catalog/` | ✅ Source (canonical) |
| **Bob** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiment_catalog/` | ✅ All 10 files synced and verified |
| **Dean** | `/home/dean/fiper_uncertainty_collection/experiment_catalog/` | ✅ All 10 files synced and verified |
| **Sam** | N/A | ⚠️ No catalog folder. Sam re-integration steps documented in SYNC_STATUS.md |

---

## 7. Key Corrections Applied

### 7.1 Intervention Rate
- **Before:** Synthesis report claimed "98.9% intervention rate" for Task 3 aggressive TopK8
- **After:** True query-level modification rate is **1.04%** (29/2,776). The 98.9% figure is the gating threshold exceedance rate, not the actual replacement rate.

### 7.2 OOD Goal-Swap
- **Before:** Not in catalog (absent from KEY_RESULTS.md)
- **After:** Documented as net negative (-2 successes, 2 rescues / 4 regressions over 300 episodes). Clear "DO NOT CLAIM OOD GENERALIZATION" warning added.

### 7.3 Active Work Status
- **Before:** "Bob and Dean were running conservative top-8 intervention pilots. Sam remains offline."
- **After:** "All Bob campaigns complete (except Task 8 incomplete). Sam is back online and idle. Dean is online and idle."

### 7.4 Obsidian Report
- **Before:** Obsidian report claimed 17 rescues / 12 regressions for Task 6 (incorrect count)
- **After:** Correct: 19 rescues / 14 regressions (verified in Step 3 forensic audit)

---

## 8. Remaining Work

1. **Sam catalog integration:** Sam is back online but has no `experiment_catalog/` folder. Run `scan_experiment_workspace.py` and create a catalog for Sam.
2. **Obsidian Vault update:** The Obsidian report has several stale/incorrect claims (documented in `OBSIDIAN_REPORT_ACCURACY_AUDIT_20260609.md`). Consider updating the Obsidian vault with corrected numbers.
3. **inventory.json update:** The `inventory.json` file was backed up but not yet updated to include the new H10 campaigns (Campaigns 1–4) or the OOD goal-swap results. A full rescan is needed to add these entries.

---

## 9. Audit Summary Fields

AUDIT_READ_ONLY = NO (catalog files were created/updated, no experiment data modified)
RAW_DATA_MODIFIED = NO
EXPERIMENTS_LAUNCHED = NO
EXPERIMENTS_STOPPED = NO
FILES_DELETED = NO
BACKUPS_CREATED = YES
HOSTS_CHECKED = 4 (Batman, Bob, Dean, Sam)
HOSTS_REACHABLE = 4 (Dean via ProxyJump only)
NEW_CATALOG_FILES = 7
UPDATED_CATALOG_FILES = 3
SYNCED_TO_BOB = YES (10 files verified)
SYNCED_TO_DEAN = YES (10 files verified)
SYNCED_TO_SAM = NO (no catalog folder; re-integration documented)
