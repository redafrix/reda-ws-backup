# Git Sync Plan

Updated: 2026-07-03.

## Current State

`/home/redafrix/tests/internship/.git` exists as an empty directory, but it is not a valid Git repository:

```text
fatal: not a git repository: '/home/redafrix/tests/internship/.git'
```

No project GitHub remote was discoverable from local Git config. Because of that, no safe `git push` was possible during the 2026-07-03 catalog audit.

## Files Prepared For Git

These lightweight files should be committed once Git is restored:

- `fiper_ws/experiment_catalog/CROSS_MACHINE_EXPERIMENT_MAP_20260703.md`
- `fiper_ws/experiment_catalog/BIG_ARTIFACTS_NOT_IN_GIT_20260703.md`
- `fiper_ws/experiment_catalog/GIT_SYNC_PLAN_20260703.md`
- updated `fiper_ws/experiment_catalog/README.md`
- updated `fiper_ws/experiment_catalog/SYNC_STATUS.md`
- updated `fiper_ws/experiment_catalog/HOST_WORKSPACE_MAP.md` if modified by the final sync
- `.gitignore`

## Branch Plan

When the remote is known, use branch-per-host plus one consolidated branch:

| Branch | Contents |
|---|---|
| `catalog/batman-20260703` | local laptop catalog, Obsidian references, cleanup notes |
| `catalog/bob-20260703` | Bob workspace/report/dataset manifests |
| `catalog/sam-20260703` | Sam source dataset and disk status manifests |
| `catalog/dean-20260703` | Dean FIPER/offline ablation manifests |
| `catalog/cross-machine-20260703` | merged final catalog files |

## Safe Commit Rules

1. Restore or initialize a valid Git repo only after confirming the intended GitHub URL.
2. Add a `.gitignore` before staging anything.
3. Run a large-file audit before every commit:

```bash
find . -type f -size +20M -not -path './.git/*' -print
git ls-files --others --exclude-standard
```

4. Never stage raw datasets, tensors, videos, checkpoints, or external repos.
5. Commit manifests and reports instead.

## Installed `.gitignore`

An actual `.gitignore` has been created at `/home/redafrix/tests/internship/.gitignore` with the heavy artifact patterns above plus `fiper_ws/tmp_checkpoint/`.
