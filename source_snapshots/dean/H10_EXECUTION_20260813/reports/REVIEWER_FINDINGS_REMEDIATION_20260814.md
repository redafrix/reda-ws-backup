# Reviewer Findings Remediation

Date: 2026-08-14.

The active H10 collector was not stopped or restarted. Its scientific row
implementation was unchanged.

## 1. Future Handoff Race

Accepted and fixed.

The primary supervisor source already performs an explicit finite handoff to
the hard-1000 orchestrator. Because the currently running Python supervisor
started before that source edit, an external fail-closed guard was added to
`automation/run_production_round_stage.sh`.

If the old in-memory supervisor races the systemd handoff and attempts any
broad round with `round_id != 0` after the first-cycle completion marker exists,
the external stage exits before launching a collector with status:

```text
blocked_by_hard1000_handoff
```

Generating Round 1 as an offline official-scene candidate pool remains allowed
because hard-1000 selection needs it. Collecting that broad round is blocked.
The systemd path handoff and five-minute hard-1000 watchdog remain active.

Result: an additional broad collector cannot start through the stale process.

## 2. Limited Failure Count

No change, per user instruction. The later H10 hard-1000 is intended to enrich
genuine failures. The first model remains scientifically valid but its
calibration uncertainty must be reported honestly if holdout failure counts are
small. Existing minimum holdout gates remain fail-closed.

## 3. OOD-150 Identity Audit

Accepted and fixed.

Added `risk_head_pipeline/ood_identity.py` and integrated it into
`risk_head_pipeline/audit_ood150.py`. Before a future OOD evaluation can pass,
the audit now independently proves:

- the run manifest references the exact locked manifest and SHA-256;
- both official and locked canonical manifest fingerprints are valid;
- the official fingerprint equals
  `49ac35a2f77d2ca12ad2d9ca00a396c3f745d2c6bc179ee6d641638fad1cde4e`;
- the locked 150 episode identities exactly equal the official 150 identities;
- collected source IDs, benchmark IDs and scene fingerprints exactly equal the
  locked manifest;
- no locked OOD scene fingerprint overlaps H10 Round 0.

The locked manifest was prepared ahead of collection and checked:

```text
official manifest SHA-256:
273fd0ef22d13ab6b9223a130e38169ae4ba890a9335dccc5de8edbfaf94f567

locked manifest SHA-256:
7ff10101f7d61966ef85246850aa4b08f158da3ef1c8867217d1e2a4a9fc8829

locked manifest fingerprint:
996082c1ecd21514af2698b5dcfff5269b4eb1ff28e62b21bcdb3e33f74eeccc

locked episodes: 150
locked identity equals official identity: yes
Round-0 scene overlap: 0
```

Four focused regression tests cover valid identity, substituted collection
membership, Round-0 overlap and run-manifest hash mismatch.

## 4. "Same Model" Wording

Accepted and corrected in pipeline reports.

The future Isaac risk head is a newly trained checkpoint. It uses the same
promoted LIBERO `SeqRiskModel` architecture and optimization recipe, but it does
not reuse LIBERO risk-head weights. Isaac training-only normalization, seen
validation model selection and seen validation threshold calibration remain
separate. No Isaac selected-candidate online deployment has been claimed.

## Verification

```text
CPU_TESTS=43_PASS_2_EXPECTED_FUTURE_MANIFEST_SKIPS
PYTHON_COMPILE=PASS
SHELL_SYNTAX=PASS
ACTIVE_COLLECTOR_RESTARTED=NO
ACTIVE_H10_COLLECTION_CONTINUES=YES
HANDOFF_RACE_ELIMINATED=YES
OOD150_EXACT_MEMBERSHIP_GATE=YES
OOD150_OFFICIAL_FINGERPRINT_GATE=YES
OOD150_ROUND0_OVERLAP_GATE=YES
LIBERO_WEIGHTS_REUSED_FOR_ISAAC_RISK_HEAD=NO
```
