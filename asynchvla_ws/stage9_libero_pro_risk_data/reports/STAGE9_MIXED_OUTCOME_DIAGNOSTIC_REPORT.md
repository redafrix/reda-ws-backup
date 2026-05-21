# Stage 9 Mixed Outcome Diagnostic Report

Date: 2026-05-20

## Executive Summary

The current evidence says the old apparent `action_specific` mixed groups were not real. They were caused by a scorer bug: candidates with no positive progress and no strong negative evidence could be pushed into `SAFE_STRONG` or `SAFE_WEAK`. I fixed that behavior so no-evidence candidates become uncertain instead of safe.

After the fix, I rechecked the active Bob/Sam mining data, reran offline rescoring, tried 64 random seeds, and tested longer action chunks. The result is consistent:

- Failed-window states produce `state_context` risky groups: all 64 candidate seeds are risky together.
- Success-branchpoint states are mostly uncertain, not clearly good or action-specific bad.
- No corrected run has produced a validated mixed `action_specific` group yet.
- The seed set is not the issue: random 64-seed probes gave the same pattern as seeds `0..63`.
- Chunk length alone is not the issue: chunk-20 and chunk-40 probes gave the same state-context / uncertain split.

The current problem is therefore not just "collect more generic data". We need a stronger mixed-branchpoint mining strategy, or we must accept that SimVLA’s failures in these tasks are mostly state-context failures rather than seed-specific action failures.

## Current Job Status

I stopped the old live test collectors because they had the old scorer loaded in memory. Current status after the checks:

- Bob: no active `collect_failed_episode_mining_v2` or `collect_continuous_risk_dataset_v2`; GPU utilization 0%.
- Sam: no active `collect_failed_episode_mining_v2` or `collect_continuous_risk_dataset_v2`; GPU utilization 0%.

The only matching processes during the last status check were diagnostic commands, not collectors.

## Files Changed

Local tool copy:

- `/home/redafrix/tests/internship/stage9_v2_tools/data_collection_stage9/local_chunk_quality.py`
- `/home/redafrix/tests/internship/stage9_v2_tools/data_collection_stage9/diagnose_v2_collection.py`

Synced copies:

- Bob: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/local_chunk_quality.py`
- Bob: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/diagnose_v2_collection.py`
- Sam: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/data_collection_stage9/local_chunk_quality.py`
- Sam: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/data_collection_stage9/diagnose_v2_collection.py`

SHA checks match across local, Bob, and Sam:

- `local_chunk_quality.py`: `433f6701e516cfa4dcc1a8d91388448fbe95a0d40df91cb41520c7166a174e0c`
- `diagnose_v2_collection.py`: `ad89d20047c5187e4e86d1a01e2ca9d24711ea60814d435353ce99669108c766`

Compile check:

- `python3 -m py_compile stage9_v2_tools/data_collection_stage9/*.py`: passed.
- Bob/Sam Stage 9 source compile was run after sync earlier and passed.

Direct code audit:

- `collect_failed_episode_mining_v2.py` writes `terminal_continuation_used_for_label: false`.
- `collect_failed_episode_mining_v2.py` writes `episode_failure_used_for_label: false`.
- `collect_failed_episode_mining_v2.py` writes `episode_failure_used_for_mining_only: true`.
- `collect_continuous_risk_dataset_v2.py` writes `terminal_continuation_used_for_label: false`.
- `local_chunk_quality.py` records terminal success/failure/timeout fields as `*_audit_only`.
- `local_chunk_quality.py` explicitly marks `terminal_timeout_audit_only_not_label_proof` instead of using terminal timeout as strong bad proof.
- Candidate actions in the tested miners are generated from SimVLA seeds through `generate_chunk`; no synthetic/no-op/manual training actions were used in these probes.

## Scorer Bug Found And Fixed

Bug:

- The local scorer and group-level scorer could treat "no clear bad evidence" as safe, even when there was also no real positive evidence.
- That created fake mixed groups where most seeds were `RISKY_STRONG` and a few seeds were `SAFE_STRONG`, but the "safe" seeds had no reward, no success, no meaningful object progress, and sometimes worse goal distance.

Fix:

- If there is no positive evidence and only weak negative evidence, assign ambiguous/uncertain evidence and floor continuous risk to at least `0.45`.
- If there is neither positive nor negative evidence, assign ambiguous/uncertain evidence and floor continuous risk to at least `0.50`.
- This was added both in the local per-candidate scorer and in the same-state group rescoring path.

Consequence:

- No-evidence candidates no longer become safe labels.
- Apparent mixed groups from the old scorer disappear under corrected rescoring.

## Existing Collection Diagnosis

### Generic Mass V2 Runs

Bob generic run:

- Path: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass/bob_20260520_134527`
- Samples: `10,176`
- Same-state groups: `159`
- Risk bins: `SAFE_STRONG 4,288`, `SAFE_WEAK 5,888`
- Mixed action-specific groups: `0`
- Interpretation: safe-anchor data, not risk data.

Sam generic run:

- Path: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass/sam_20260520_140528`
- Samples: `5,120`
- Same-state groups: `80`
- Risk bins: `SAFE_STRONG 1,800`, `SAFE_WEAK 3,320`
- Mixed action-specific groups: `0`
- Interpretation: safe-anchor data, not risk data.

### Failure Mining Runs Before Fix

Bob failure miner old live data:

- Path: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass_failure/bob_20260520_144340`
- Samples checked: `7,680`
- Old risk bins: `RISKY_STRONG 959`, `SAFE_STRONG 776`, `SAFE_WEAK 5,177`
- Old subtype counts: `action_specific 63`, `state_context 896`, `unknown 5,953`
- Old mixed groups: `1`

Sam failure miner old live data:

- Path: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass_failure/sam_20260520_144408`
- Samples checked: `8,064`
- Old risk bins: `RISKY_STRONG 1,246`, `SAFE_STRONG 34`, `SAFE_WEAK 6,016`
- Old subtype counts: `action_specific 30`, `state_context 1,216`, `unknown 6,848`
- Old mixed groups: `1`

Interpretation:

- These old `action_specific` counts were artifacts of the no-evidence-safe bug.

### Failure Mining Runs After Offline Corrected Rescore

Bob corrected rescore:

- Output: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass_failure/bob_20260520_144340/offline_rescore_after_group_no_evidence_safe_fix.jsonl`
- Rows: `7,680`
- Same-state groups: `120`
- Risk bins: `UNCERTAIN 6,721`, `RISKY_STRONG 959`
- Legacy labels: `AMBIGUOUS 6,721`, `VALIDATED_BAD 959`
- Subtypes: `state_context 959`, `unknown 6,721`
- Group types: `uncertain_or_low_confidence 106`, `all_risky_state_context_candidate 14`
- Corrected mixed action-specific groups: `0`

Sam corrected rescore:

- Output: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass_failure/sam_20260520_144408/offline_rescore_after_group_no_evidence_safe_fix.jsonl`
- Rows: `8,064`
- Same-state groups: `126`
- Risk bins: `UNCERTAIN 6,818`, `RISKY_STRONG 1,246`
- Legacy labels: `AMBIGUOUS 6,848`, `VALIDATED_BAD 1,216`
- Subtypes: `state_context 1,216`, `unknown 6,848`
- Group types: `uncertain_or_low_confidence 107`, `all_risky_state_context_candidate 19`
- Corrected mixed action-specific groups: `0`

Interpretation:

- Corrected scorer removes fake action-specific labels.
- The remaining bad labels are state-context groups backed by `no_progress_strong`.

## Random Seed Probe

Purpose:

- Test whether seeds `0..63` were somehow too correlated or broken.
- I used 64 large random SimVLA seeds on Bob and a different 64 random seeds on Sam.

Bob random-seed probe:

- Path: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/random_seed_boundary_bob_20260520`
- Episodes: `6`
- Success / failed: `5 / 1`
- Replay samples: `1,536`
- Same-state groups: `24`
- Risk bins: `UNCERTAIN 1,280`, `RISKY_STRONG 256`
- Subtypes: `state_context 256`, `unknown 1,280`
- Duplicate seed groups: `0`
- Mean action diversity: `0.2242`
- Mixed action-specific groups: `0`

Sam random-seed probe:

- Path: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/random_seed_boundary_sam_20260520`
- Episodes: `6`
- Success / failed: `5 / 1`
- Replay samples: `1,536`
- Same-state groups: `24`
- Risk bins: `UNCERTAIN 1,280`, `RISKY_STRONG 256`
- Subtypes: `state_context 256`, `unknown 1,280`
- Duplicate seed groups: `0`
- Mean action diversity: `0.2191`
- Mixed action-specific groups: `0`

Conclusion:

- The seed set is not the main problem.
- Candidate actions are diverse and seed hashes are unique, but outcomes are homogeneous under corrected scoring.

## Longer Chunk Probes

Purpose:

- Test whether the 10-step local chunk was too short to reveal action-specific damage.
- Bob ran 20-step action chunks.
- Sam ran 40-step action chunks.

Bob chunk-20 probe:

- Path: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/random_seed_chunk20_bob_20260520`
- Episodes: `4`
- Success / failed: `1 / 3`
- Replay samples: `768`
- Same-state groups: `12`
- Risk bins: `UNCERTAIN 192`, `RISKY_STRONG 576`
- Subtypes: `state_context 576`, `unknown 192`
- Group types: `all_risky_state_context_candidate 9`, `uncertain_or_other 3`
- Duplicate seed groups: `0`
- Mean action diversity: `0.2499`
- Max action diversity: `1.0137`
- Mixed action-specific groups: `0`

Sam chunk-40 probe:

- Path: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/probe/random_seed_chunk40_sam_20260520`
- Episodes: `4`
- Success / failed: `1 / 3`
- Replay samples: `768`
- Same-state groups: `12`
- Risk bins: `UNCERTAIN 192`, `RISKY_STRONG 576`
- Subtypes: `state_context 576`, `unknown 192`
- Group types: `all_risky_state_context_candidate 9`, `uncertain_or_other 3`
- Duplicate seed groups: `0`
- Mean action diversity: `0.2105`
- Max action diversity: `0.3643`
- Mixed action-specific groups: `0`

Conclusion:

- Longer chunks alone did not reveal action-specific risk.
- Failed states remain homogeneous: all same-state seeds are bad.
- Success branchpoints remain uncertain rather than producing clear good-vs-bad alternatives.

## Current Interpretation

The evidence now points to this:

1. The scorer had a real bug and it is fixed.
2. The old apparent mixed action-specific labels should not be trusted.
3. Random seeds are working: no duplicate seed groups, unique action hashes, measurable action diversity.
4. More generic collection is not the answer. It mostly creates safe or uncertain anchors.
5. Current failure mining reliably finds state-context bad states, not action-specific bad chunks.
6. It is still possible that action-specific risk exists, but the current miner is not finding it after the scorer fix.

## What This Means For Training Data

Trustworthy right now:

- `state_context` high-risk samples from failed-window states, with strong no-progress evidence.
- Safe/uncertain anchors from generic and success-branchpoint states, but only if no-evidence samples are treated as uncertain, not safe.

Not trustworthy right now:

- Old `action_specific` labels from before the no-evidence-safe fix.
- Any safe label that is based only on absence of bad evidence.

Not solved yet:

- Finding same-state groups where some real SimVLA seeds make meaningful progress and other real SimVLA seeds cause local harm or clear no-progress.

## Recommended Next Experiment

Do not keep running generic mass collection.

The next useful collector should be an active mixed-branchpoint miner:

1. Run many parent episodes, both success and failure.
2. Save dense candidate states around:
   - grasp contact onset,
   - lift onset,
   - object barely held,
   - transport with object in gripper,
   - pre-place / near-goal,
   - stuck onset,
   - recovery attempts after hesitation.
3. For each candidate state, replay 64 or 128 real SimVLA seeds.
4. Keep a state only if the same-state group has genuine score spread:
   - at least one seed has positive progress evidence,
   - at least one seed has strong negative evidence,
   - labels are not produced only by lack of evidence.
5. Rank states by continuous score range, not just max risk.
6. Produce review clips only for the highest-spread states.

If that still produces no mixed groups, the honest conclusion is that for these LIBERO-PRO/SimVLA settings, the main learnable risk is state-context risk, not action-specific seed-level risk.

## Bottom Line

The code is stricter now and the current evidence is cleaner. We fixed a scorer bug that created fake mixed labels. After the fix, Bob and Sam both show the same behavior:

- state-context bad exists,
- action-specific bad has not been found,
- seeds are not duplicated,
- random seeds do not fix it,
- longer chunks do not fix it.

The next step is not more blind collection. The next step is a targeted active mixed-branchpoint miner that selects for within-state score spread and real positive-vs-negative evidence.
