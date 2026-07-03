# Dean Goal-Object Dual Collection Worklog

## Objective

Build and launch two comparable modified-SimVLA data collectors on Dean for the exact LIBERO-PRO `libero_goal_object` object-substitution environment bundle:

- receding execution: query every environment step and execute one action;
- chunk execution: query every 10 environment steps and execute the full 10-action chunk;
- preserve the exact 200 bundled episodes separately;
- after exact validation, continue both modes on one shared reproducible 100,000-episode random plan;
- record main actions, eight ACE candidates, all 49 uncertainty features, their 49 deltas, and every environment transition.

## 2026-06-05 Audit

- Dean is reachable through `dean-via-bob` and the RTX A5000 is idle.
- Checkpoint SHA-256 verified:
  `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`.
- The reproduction bundle verifier passed previously on Dean.
- Exact identity table contains 200 unique episodes: task IDs 0-9, init-state indices 0-9 and 40-49, evaluation seed 0.
- Exact BDDL language differs from Dean's normal benchmark metadata for some tasks. The collector must parse `(:language ...)` from the bundled BDDL file.
- Reference evaluator behavior verified: each of the two windows is a separate seed-0 invocation; within a window it iterates task ID then initial-state index, calls `env.reset()`, then `env.set_init_state(...)`, and performs 10 zero-action warmup steps.
- Dean root disk has 56 GB free. The unmounted NVMe cannot be used without valid administrator authorization. Exact data can retain images/states; continuous data must use compact compressed numeric episode files and a low-disk pause guard.
- No active experiment processes or tmux sessions were found on Dean.

## Current Step

Implement the isolated collector, deterministic continuous-plan generator, output validator, and staged launcher.

## Next

1. Run syntax and local static checks.
2. Sync code to Dean.
3. Run one short receding smoke and one short chunk smoke.
4. Verify exact prompt, init hash, transition counts, uncertainty dimensions, seed uniqueness, resume behavior, and GPU memory.
5. Launch one worker per mode concurrently if memory remains healthy.
