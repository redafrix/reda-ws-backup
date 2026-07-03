# CLI Session Provenance - 2026-06-10

This file maps the recent Gemini CLI and Antigravity CLI work to trusted artifacts. Treat raw JSONL episode summaries and Codex audit reports as the authority when a chat summary disagrees.

## Gemini CLI Sessions

| Session | Local conversation path | Main work | Trust notes |
|---|---|---|---|
| `0da70141-64e2-43bb-b763-dc0734cd5105` | `/home/redafrix/.gemini/tmp/internship/chats/session-2026-06-08T08-34-0da70141.jsonl` | Bob H10 risk-proof setup and early campaign checks | Useful operational history; Task 8 modified runs were interrupted and are not trusted. |
| `53ae7465-ab35-4fd1-ade0-498700340e82` | `/home/redafrix/.gemini/tmp/internship/chats/session-2026-06-09T07-11-53ae7465.jsonl` | OOD goal-object asset generation, invalid first sweep, corrected 10ep/100ep OOD sweeps | Trust only after Codex/forensic checks. The first root `h10_goal_object_ood_all_tasks_10ep_20260609` is invalid because it used q95 fallback instead of aggressive 0.3 controls. |
| `f8fd5877-e1da-49b6-82c4-9662ff112ce7` | `/home/redafrix/.gemini/tmp/internship/chats/session-2026-06-05T14-06-f8fd5877.jsonl` | Bob chunk10 `libero_goal_object` 100-episode modified-vs-official SimVLA diagnostic | Historical diagnostic: modified ckpt-60000 80/100 vs official SimVLA 78/100 on same 100 bundle episodes. Not a risk-aware result. |
| `b8d34f11-a931-49da-8614-54c3725d5829` | `/home/redafrix/.gemini/tmp/internship/chats/session-2026-06-05T13-21-b8d34f11.jsonl` | Dean/Bob/Sam synchronization and older remote setup | Historical context only; verify against current catalog before using paths. |

## Antigravity CLI Sessions

| Session / identifier | Main work | Trust notes |
|---|---|---|
| `dbebaa92-28e0-4ba8-a2d8-8a9dcdfb5cae` | Threshold 0.5 OOD sweep audit and report | Mechanically trusted after raw JSONL recomputation: threshold 0.5 tied modified SimVLA globally, 21 rescues / 21 regressions. |
| `7bcd0aa8-f0a6-4c00-908f-cde9d01e99fc` | Sam adaptive-horizon V2/V2B/V2C/V2D setup and reports | Original V2 is invalid. V2B, V2C, and V2D are mechanically trusted negative diagnostics. |

## Corrected Results To Prefer

| Experiment | Corrected value |
|---|---|
| Bob OOD 100ep threshold 0.3 | original 1668/1800, modified 1718/1800, risk 1713/1800; paired risk vs modified 24 rescues / 29 regressions, net -5. |
| Bob OOD 100ep threshold 0.5 | risk 1718/1800; paired vs modified 21 rescues / 21 regressions, net 0. |
| Bob OOD 100ep q95 | risk 1710/1800; paired vs modified 10 rescues / 18 regressions, net -8. |
| Bob goal-object chunk10 diagnostic | modified ckpt-60000 80/100, official SimVLA 78/100; paired modified vs official 8 rescues / 6 regressions, net +2. |
| Sam adaptive horizon | V2B 167/180, V2C 169/180, V2D 168/180 vs fixed-H10 modified baseline 171/180. |
| Dean selected-cap 10ep | modified 170/180, selected-cap risk 176/180; 7 rescues / 1 regression, net +6. |
| Dean selected-cap 100ep Tasks 0-3 interim | modified 358/400, selected-cap risk 371/400; 22 rescues / 9 regressions, net +13. |

## Active Runs

| Host | Run | Notes |
|---|---|---|
| Dean | `/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_100ep_20260610` | Selected-cap 100ep confirmation running. |
