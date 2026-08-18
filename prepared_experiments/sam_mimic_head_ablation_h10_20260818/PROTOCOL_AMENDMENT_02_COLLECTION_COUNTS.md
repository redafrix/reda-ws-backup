# Protocol Amendment 02 — collection counts and calibration

This amendment supersedes the earlier fixed `500/200/200/100 calibration-pool` interpretation while preserving the same official Goal-Object-only scope.

## Goal

Keep the campaign approximately 1000 episodes while satisfying the supplied Mimic-style handoff requirement of **exactly 100 successful ID calibration episodes** and retaining an untouched seen test split.

## Fixed state groups per official Goal-Object task

Official LIBERO-PRO Goal-Object has 50 init states per task. Keep the same init-state group assignment for all 10 tasks:

- training states: `0..24`
- id_development states: `25..34`
- heldout_seen_test states: `35..44`
- successful_calibration states: `45..49`

No init-state group may cross assignments.

## Fixed non-calibration collection

Use two independent policy rollout seeds per `(task_id, init_state_idx)`:

- training: 25 states x 2 seeds x 10 tasks = **500 episodes**
- id_development: 10 states x 2 seeds x 10 tasks = **200 episodes**
- heldout_seen_test: 10 states x 2 seeds x 10 tasks = **200 episodes**

Fixed total = **900 episodes**.

## Adaptive successful calibration collection

For calibration states `45..49`, collect deterministic additional policy seeds in rounds while preserving the same reset/init-state group.

Continue until the dataset contains **exactly 100 successful calibration episodes**. Failed calibration attempts remain preserved in the raw collection/audit but are NOT members of the `successful_calibration` split consumed by threshold calibration.

Do not cherry-pick based on risk scores. Membership depends only on assignment to calibration init states plus the final episode success label, matching the supplied handoff's success-only calibration requirement.

Stop with an error rather than silently changing protocol if 100 successes have not been obtained after 500 calibration attempts.

Thus expected total collection is approximately 1000 episodes when baseline Goal-Object success is high, but the scientific invariant is 900 fixed train/dev/test episodes plus exactly 100 successful calibration members.

## Failure-class gate

Single-Head training requires both eventual classes in training and ID development.

After collection, if either training or id_development contains zero successes or zero failures, STOP before training and report the class counts. Do not move episodes between init-state groups and do not relabel outcomes.

No minimum failure count beyond the handoff's both-class requirement is invented here.
