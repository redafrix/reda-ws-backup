# Stage 9 V2 Collection Diagnosis

## /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass_failure/sam_20260520_144408

- Analyzed samples: `7296`
- Replay samples: `7296`
- Episode chunks: `339`
- Same-state groups: `114`
- Risk bins: `{'SAFE_WEAK': 6016, 'RISKY_STRONG': 1246, 'SAFE_STRONG': 34}`
- Bad subtypes: `{'unknown': 6050, 'state_context': 1216, 'action_specific': 30}`
- Group types: `{'all_safe_or_weak_safe': 94, 'all_risky_state_context_candidate': 19, 'action_specific_mixed': 1}`
- Duplicate-seed groups: `0`
- Possible scorer saturation groups: `106`
- Mean risk-score range/group: `0.008861222261145545`
- Max risk-score range/group: `0.7140793377705866`
- Mean action diversity/group: `0.3737220711562941`
- Max action diversity/group: `2.276107885922592`

### Mixed Groups

- `libero_spatial_with_mug_t0_r6_pseed6_window009_state` `action_specific_mixed` bins={'SAFE_STRONG': 34, 'RISKY_STRONG': 30} subtypes={'unknown': 34, 'action_specific': 30} range=0.7140793377705866 div={'mean_l2_to_group_mean': 1.6257537478946922, 'max_l2_to_group_mean': 3.9920552745976785}

### Possible Scorer Saturation

- `libero_spatial_with_mug_t0_r0_pseed0_window000_state` bins={'SAFE_WEAK': 64} range=0.0 div={'mean_l2_to_group_mean': 0.1573820792482169, 'max_l2_to_group_mean': 0.4257302009528353}
- `libero_spatial_with_mug_t0_r0_pseed0_window002_state` bins={'SAFE_WEAK': 64} range=0.0 div={'mean_l2_to_group_mean': 0.22541504429301185, 'max_l2_to_group_mean': 0.4306235842542567}
- `libero_spatial_with_mug_t0_r0_pseed0_window004_state` bins={'SAFE_WEAK': 64} range=0.0 div={'mean_l2_to_group_mean': 0.16586732637810536, 'max_l2_to_group_mean': 0.33483421864491003}
- `libero_spatial_with_mug_t0_r0_pseed0_window006_state` bins={'SAFE_WEAK': 64} range=0.0 div={'mean_l2_to_group_mean': 0.30789665216923023, 'max_l2_to_group_mean': 0.755458204162152}
- `libero_spatial_with_mug_t0_r1_pseed1_window009_state` bins={'RISKY_STRONG': 64} range=0.0 div={'mean_l2_to_group_mean': 0.35463417601736125, 'max_l2_to_group_mean': 0.7606912168729011}
- `libero_spatial_with_mug_t0_r1_pseed1_window011_state` bins={'RISKY_STRONG': 64} range=0.0 div={'mean_l2_to_group_mean': 0.300444491621643, 'max_l2_to_group_mean': 0.7915069862413464}
- `libero_spatial_with_mug_t0_r1_pseed1_window013_state` bins={'RISKY_STRONG': 64} range=0.0 div={'mean_l2_to_group_mean': 0.22075432181705626, 'max_l2_to_group_mean': 0.39780496302935553}
- `libero_spatial_with_mug_t0_r1_pseed1_window014_state` bins={'RISKY_STRONG': 64} range=0.0 div={'mean_l2_to_group_mean': 0.35263096349916184, 'max_l2_to_group_mean': 0.6343324154643499}
- `libero_spatial_with_mug_t0_r2_pseed2_window000_state` bins={'SAFE_WEAK': 64} range=5.745404152435185e-15 div={'mean_l2_to_group_mean': 0.18312392530501392, 'max_l2_to_group_mean': 0.4353640436208047}
- `libero_spatial_with_mug_t0_r2_pseed2_window002_state` bins={'SAFE_WEAK': 64} range=0.0 div={'mean_l2_to_group_mean': 0.20085812199854847, 'max_l2_to_group_mean': 0.39964973129071896}

## /home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/v2_mass/sam_20260520_140528

- Analyzed samples: `5120`
- Replay samples: `0`
- Episode chunks: `0`
- Same-state groups: `80`
- Risk bins: `{'SAFE_WEAK': 3320, 'SAFE_STRONG': 1800}`
- Bad subtypes: `{'unknown': 5120}`
- Group types: `{'all_safe_or_weak_safe': 80}`
- Duplicate-seed groups: `0`
- Possible scorer saturation groups: `28`
- Mean risk-score range/group: `0.05770757270806524`
- Max risk-score range/group: `0.3318444444444445`
- Mean action diversity/group: `0.7239165371258796`
- Max action diversity/group: `2.7971779769803544`

### Possible Scorer Saturation

- `libero_spatial_with_mug_t0_r0_pTRANSPORT_s26_state` bins={'SAFE_WEAK': 64} range=0.0 div={'mean_l2_to_group_mean': 0.3042513404577763, 'max_l2_to_group_mean': 0.5768420891725251}
- `libero_spatial_with_mug_t0_r1_pTRANSPORT_s80_state` bins={'SAFE_WEAK': 64} range=2.4980018054066022e-15 div={'mean_l2_to_group_mean': 1.1669780997517627, 'max_l2_to_group_mean': 2.651647165592382}
- `libero_spatial_with_mug_t0_r1_pSTUCK_OR_NO_PROGRESS_s108_state` bins={'SAFE_WEAK': 64} range=5.551115123125783e-16 div={'mean_l2_to_group_mean': 1.2515111141564945, 'max_l2_to_group_mean': 2.4823219699992354}
- `libero_spatial_with_mug_t0_r1_pSTUCK_OR_NO_PROGRESS_s119_state` bins={'SAFE_WEAK': 64} range=1.3877787807814457e-16 div={'mean_l2_to_group_mean': 0.35744284027291245, 'max_l2_to_group_mean': 1.9321121908120373}
- `libero_spatial_with_mug_t0_r2_pPLACE_OR_GOAL_s75_state` bins={'SAFE_STRONG': 64} range=0.0 div={'mean_l2_to_group_mean': 1.233197153587709, 'max_l2_to_group_mean': 2.394548925048006}
- `libero_spatial_with_mug_t0_r3_pTRANSPORT_s25_state` bins={'SAFE_WEAK': 64} range=0.0 div={'mean_l2_to_group_mean': 0.2150699699645532, 'max_l2_to_group_mean': 0.366168636238887}
- `libero_spatial_with_mug_t0_r4_pTRANSPORT_s80_state` bins={'SAFE_WEAK': 64} range=6.38378239159465e-16 div={'mean_l2_to_group_mean': 0.8377767573164622, 'max_l2_to_group_mean': 2.056307756877857}
- `libero_spatial_with_mug_t0_r4_pTRANSPORT_s119_state` bins={'SAFE_WEAK': 64} range=0.0 div={'mean_l2_to_group_mean': 1.4053179349338474, 'max_l2_to_group_mean': 3.24848095760862}
- `libero_spatial_with_mug_t0_r5_pTRANSPORT_s80_state` bins={'SAFE_STRONG': 64} range=0.0 div={'mean_l2_to_group_mean': 0.27515849725863295, 'max_l2_to_group_mean': 0.49916704380562027}
- `libero_spatial_with_mug_t0_r7_pPLACE_OR_GOAL_s80_state` bins={'SAFE_STRONG': 64} range=0.0 div={'mean_l2_to_group_mean': 0.31423384147263844, 'max_l2_to_group_mean': 0.6377811806792824}

