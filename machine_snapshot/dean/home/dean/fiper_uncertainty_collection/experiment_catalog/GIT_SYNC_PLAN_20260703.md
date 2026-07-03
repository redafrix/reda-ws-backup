# Git Sync Plan

Updated: 2026-07-03 after Git repair and deep coverage audit.

## Current State

The local Git repo was repaired on 2026-07-03. The previous broken local `.git` directory was moved aside:

```text
/home/redafrix/tests/internship/.git.broken_20260703_112818
```

A clean lightweight repository now exists at:

```text
/home/redafrix/tests/internship
```

Remote:

```text
https://github.com/redafrix/reda-ws-backup.git
```

Branches pushed after the deep-audit update:

| Branch | Purpose |
|---|---|
| `catalog/batman-20260703` | local laptop catalog, Obsidian references, cleanup notes |
| `catalog/bob-20260703` | Bob workspace/report/dataset manifests |
| `catalog/sam-20260703` | Sam source dataset and disk-status manifests |
| `catalog/dean-20260703` | Dean FIPER/offline ablation manifests |
| `catalog/cross-machine-20260703` | merged cross-machine catalog |

Deep-audit content commit:

```text
dcbf0251b59cb58fe3576f17e3f26c2ebd2ef3df
```

Follow-up metadata-only commits may be newer; use `git rev-parse HEAD` for the exact current branch tip.

Existing remote branches `main`, `bob`, `sam`, and `dean` were not overwritten.

## Files Added/Updated By The Deep Audit

- `fiper_ws/experiment_catalog/DEEP_EXPERIMENT_COVERAGE_AUDIT_20260703.md`
- `fiper_ws/experiment_catalog/manifests/deep_audit_summary_20260703.json`
- `fiper_ws/experiment_catalog/CROSS_MACHINE_EXPERIMENT_MAP_20260703.md`
- `fiper_ws/experiment_catalog/HOST_WORKSPACE_MAP.md`
- `fiper_ws/experiment_catalog/MASTER_EXPERIMENT_INDEX.md`
- `fiper_ws/experiment_catalog/BIG_ARTIFACTS_NOT_IN_GIT_20260703.md`
- `fiper_ws/experiment_catalog/README.md`
- `fiper_ws/experiment_catalog/SYNC_STATUS.md`
- `.gitignore`

## Safe Commit Rules

1. Run stale-lock/process checks before Git operations if a prior session was interrupted.
2. Keep `.gitignore` active before staging.
3. Run a large-file audit before every commit:

```bash
find . -type f -size +20M -not -path './.git/*' -print
git ls-files --others --exclude-standard
```

4. Never stage raw datasets, tensors, videos, checkpoints, external repos, or environment folders.
5. Commit manifests, reports, scripts, and small JSON summaries instead.
6. For every large artifact that matters, add or update a substitute entry in `BIG_ARTIFACTS_NOT_IN_GIT_20260703.md`.

## Installed `.gitignore`

`/home/redafrix/tests/internship/.gitignore` excludes checkpoints, tensors, raw JSONL, videos, conda/env folders, copied external repos, generated archives, and `fiper_ws/tmp_checkpoint/`.

## Branch Update Procedure

When the catalog changes:

```bash
git status --short
find . -type f -size +20M -not -path './.git/*' -print
git add .gitignore fiper_ws/experiment_catalog
git commit -m "Update experiment catalog coverage"
for b in catalog/batman-20260703 catalog/bob-20260703 catalog/sam-20260703 catalog/dean-20260703 catalog/cross-machine-20260703; do
  git push origin HEAD:$b
done
```
