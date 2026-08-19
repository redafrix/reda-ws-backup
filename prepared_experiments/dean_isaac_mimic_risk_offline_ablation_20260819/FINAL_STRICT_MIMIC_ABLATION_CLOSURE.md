# FINAL STRICT MIMIC ABLATION CLOSURE

Status: CLOSED / NO FURTHER TUNING

Primary baseline experiment:
`isaac_mimic_h10_strict_missingdyn_v2`

Primary scientific role:
Strict source-fidelity Mimic-style H10 baseline under the retained Isaac Round0 evidence. The original cross-candidate denoising internals are unavailable; therefore scalar channels 9..33 are permanently zero rather than replaced by invented proxy features. This is NOT claimed to be the exact original friend/W2A K1 implementation.

## Frozen provenance

Strict V2 dataset manifest SHA256:
`852ad05e6208caba23c630174eb6784793304281169e5e24a25da22d030b57a1`

Normalization SHA256:
`d055a71bc2e531264f35d8bdd91e545d3f3b39cbba1cc543699ec1b987107830`

Training freeze SHA256:
`ecf7fa8e2b8b755663f81dfd1e2b63c2bd578a1da03ee38ea1a94bc24128d6fd`

Held-out freeze SHA256:
`3389e7ebb320e928cd3306065d063656aff7d7ee2220955f648dfaf3c34aa6f8`

Stage 7 result commit:
`272b9ab742ee5e5cccd3e0bfc64e267c8138b13f`

Primary seed: `0`
Primary operating point: `conformal_alpha_0.10`
Primary checkpoint SHA256:
`78b801c9071561108dded63d4e4b43fcf3b423932864f6817f808d6268e17fe6`
Primary threshold:
`0.6284286379814148`

## Strict V2 held-out seen result

Test population:
- 600 episodes
- 586 successful episodes
- 14 failed episodes
- 11,368 query rows

Seed 0 / alpha=0.10:
- Row AUROC: 0.8738685501
- Row AUPRC: 0.7303644237
- Success false alarms: 51/586 = 8.70%
- Failure detection: 14/14 = 100.00%
- Det@10: 0/14 = 0.00%
- Det@25: 3/14 = 21.43%
- Det@50: 14/14 = 100.00%
- Never detected: 0/14
- Mean first-alarm fraction: 0.333333

Five-seed alpha=0.10 robustness:
- AUROC: 0.870846 +/- 0.010657
- AUPRC: 0.706573 +/- 0.025355
- Success false alarms: 7.68% +/- 1.33%
- Failure detection: 100.00% +/- 0.00%
- Det@25: 17.14% +/- 11.61%
- Det@50: 97.14% +/- 5.71%

## Exact matched TopK8 comparison

Membership is the exact same 600 held-out episodes.

Threshold-independent:
- TopK8 AUROC: 0.9310794797
- Strict V2 AUROC: 0.8738685501
- Delta (Strict V2 - TopK8): -0.0572109296

- TopK8 AUPRC: 0.8186299851
- Strict V2 AUPRC: 0.7303644237
- Delta (Strict V2 - TopK8): -0.0882655615

Matched validation-derived row-best-F1 operating point:

TopK8:
- threshold: 0.7990124226
- success FA: 12/586 = 2.05%
- failure detection: 14/14 = 100.00%
- Det@10: 2/14 = 14.29%
- Det@25: 5/14 = 35.71%
- Det@50: 14/14 = 100.00%

Strict V2:
- threshold: 0.9642555714
- success FA: 5/586 = 0.85%
- failure detection: 13/14 = 92.86%
- Det@10: 0/14 = 0.00%
- Det@25: 0/14 = 0.00%
- Det@50: 12/14 = 85.71%

Interpretation:
- TopK8 has materially stronger held-out discrimination: +0.0572 AUROC and +0.0883 AUPRC.
- At the matched validation-best-F1 rule, Strict V2 is more conservative (7 fewer success false alarms), but this comes with worse safety coverage and substantially later detection: one missed failure, zero Det@25 failures, and two fewer failures detected by halfway through the episode.
- The primary alpha=0.10 Strict V2 operating point eventually detects all 14 failures but is still late: only 3/14 by Det@25.
- Because only 14 held-out failure episodes exist, every failure corresponds to 7.14 percentage points; raw counts must always be reported.

## Scientific claim allowed

Allowed:
"On the exact same held-out Isaac split, the proposed TopK8 risk monitor substantially outperformed the strict Mimic-style missing-dynamics adaptation in row-level discrimination and early failure warning."

Do NOT claim:
"TopK8 beats the exact original Mimic/W2A K1 implementation."

The exact original implementation was not recoverable, and 25 cross-candidate denoising summary channels were unavailable in the retained Isaac data. The strict baseline preserves the source-backed architecture and available feature semantics while leaving those unavailable channels zero.

## Status of older variants

`isaac_mimic_h10_c0dyn_v1`:
Secondary diagnostic only. It uses custom candidate-0 denoising proxies and is therefore a proxy-enhanced adaptation, not the primary Mimic ablation.

Invalid Stage5 OOD150 result from commit:
`e098edbd1e2c93b3e61154c7b8aacba7a1081cb3`
MUST NEVER be cited. It used normalized final candidate chunks instead of ENV chunks.

Corrected V1 OOD150 results remain valid only as secondary proxy-enhanced diagnostic evidence, not as the primary strict baseline result.

## Lock

From this point forward:
- no retraining Strict V2;
- no changing zeroed channels;
- no changing architecture;
- no threshold recalibration;
- no seed selection from test;
- no new feature substitutions;
- no using V1 because it scores better or worse;
- no modifying the primary ablation because of observed results.

Any future OOD evaluation of Strict V2 is supplementary only and must use these already-frozen checkpoints, normalization and validation thresholds unchanged.
