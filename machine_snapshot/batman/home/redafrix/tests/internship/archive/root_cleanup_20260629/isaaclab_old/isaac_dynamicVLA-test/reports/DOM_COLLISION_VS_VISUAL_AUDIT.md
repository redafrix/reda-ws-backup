# DOM Collision vs Visual Mesh Audit

Goal:
Verify whether physics collision geometry matches the actual visible/render mesh shape for DOM object USD assets.

This audit is static only:
- no Isaac launch
- no SimulationApp
- no rendering
- no process cleanup
- no asset modification

## Start
Thu Jun 11 02:00:59 PM CEST 2026
ROOT=/home/redafrix/tests/internship/isaac_dynamicVLA-test
/home/redafrix/tests/internship/isaac_dynamicVLA-test

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  258G   29G  91% /

## Object USD count
211

## Collision vs visual static audit
usd_files: 211
csv: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/dom_collision_vs_visual_audit.csv
json: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/dom_collision_vs_visual_audit.json

verdict_counts:
Counter({'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 126, 'UNCLEAR_NEEDS_OVERLAY': 69, 'ROUGH_PRIMITIVE_COLLISION': 14, 'BAD_BBOX_MISMATCH': 2})

Worst / suspicious assets:
apple/apple03.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 555 collision_pts= 0 vis_bbox= 0.064731,0.066538,0.085000 col_bbox= 0.085000,0.085000,0.089250 ratios= 1.3131 1.2775 1.0500 notes= 
apple/apple15.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 55274 collision_pts= 0 vis_bbox= 0.060811,0.060354,0.070000 col_bbox= 0.070000,0.070000,0.073500 ratios= 1.1511 1.1598 1.0500 notes= 
avocado/avocado00.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 313495 collision_pts= 0 vis_bbox= 0.082875,0.071070,0.081406 col_bbox= 0.057400,0.057400,0.078400 ratios= 0.6926 0.8076 0.9631 notes= 
bowl/bowl00.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 826 vis_bbox=  col_bbox= 0.150000,0.150000,0.042472 ratios=    notes= 
bowl/bowl01.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 742 vis_bbox=  col_bbox= 0.150000,0.150000,0.065715 ratios=    notes= 
bowl/bowl02.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 448 vis_bbox=  col_bbox= 0.150000,0.150000,0.063174 ratios=    notes= 
bowl/bowl04.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 133201 vis_bbox=  col_bbox= 0.150000,0.150000,0.074634 ratios=    notes= 
bowl/bowl05.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1969 vis_bbox=  col_bbox= 0.150000,0.150000,0.043627 ratios=    notes= 
bowl/bowl06.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 51332 vis_bbox=  col_bbox= 0.149885,0.150000,0.061433 ratios=    notes= 
bowl/bowl07.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 469 vis_bbox=  col_bbox= 0.150000,0.150000,0.049643 ratios=    notes= 
bowl/bowl08.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1766 vis_bbox=  col_bbox= 0.150000,0.150000,0.061694 ratios=    notes= 
bowl/bowl09.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 72139 vis_bbox=  col_bbox= 0.150000,0.149557,0.042892 ratios=    notes= 
bowl/bowl10.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 3079 vis_bbox=  col_bbox= 0.150000,0.150000,0.069907 ratios=    notes= 
bowl/bowl11.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 30313 vis_bbox=  col_bbox= 0.150000,0.150000,0.077199 ratios=    notes= 
bowl/bowl12.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1304 vis_bbox=  col_bbox= 0.150000,0.150000,0.075979 ratios=    notes= 
bowl/bowl13.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1024 vis_bbox=  col_bbox= 0.150000,0.150000,0.032598 ratios=    notes= 
bowl/bowl14.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 897 vis_bbox=  col_bbox= 0.150000,0.149993,0.074033 ratios=    notes= 
bowl/bowl15.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 498 vis_bbox=  col_bbox= 0.150000,0.150000,0.039921 ratios=    notes= 
bowl/bowl16.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 3313 vis_bbox=  col_bbox= 0.150000,0.150000,0.060438 ratios=    notes= 
bowl/bowl17.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 90444 vis_bbox=  col_bbox= 0.150000,0.150000,0.055850 ratios=    notes= 
bowl/bowl18.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 826 vis_bbox=  col_bbox= 0.150000,0.150000,0.042472 ratios=    notes= 
bowl/bowl19.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 33602 vis_bbox=  col_bbox= 0.150000,0.150000,0.073503 ratios=    notes= 
box/box00.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 5960 vis_bbox=  col_bbox= 0.242279,0.122178,0.120000 ratios=    notes= 
box/box01.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 5960 vis_bbox=  col_bbox= 0.242279,0.122178,0.120000 ratios=    notes= 
box/box02.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 5960 vis_bbox=  col_bbox= 0.242279,0.122178,0.120000 ratios=    notes= 
box/box03.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 5960 vis_bbox=  col_bbox= 0.242279,0.122178,0.120000 ratios=    notes= 
box/box04.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 5960 vis_bbox=  col_bbox= 0.242279,0.122178,0.120000 ratios=    notes= 
box/box05.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 5960 vis_bbox=  col_bbox= 0.242279,0.122178,0.120000 ratios=    notes= 
box/box06.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 16 vis_bbox=  col_bbox= 0.192765,0.129027,0.090250 ratios=    notes= 
box/box08.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 804 vis_bbox=  col_bbox= 0.236220,0.167323,0.101270 ratios=    notes= 
box/box09.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 804 vis_bbox=  col_bbox= 0.236220,0.167323,0.101270 ratios=    notes= 
box/box10.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 804 vis_bbox=  col_bbox= 0.236220,0.167323,0.101270 ratios=    notes= 
box/box11.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 804 vis_bbox=  col_bbox= 0.236220,0.167323,0.101270 ratios=    notes= 
box/box12.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 804 vis_bbox=  col_bbox= 0.236220,0.167323,0.101270 ratios=    notes= 
box/box13.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 804 vis_bbox=  col_bbox= 0.236220,0.167323,0.101270 ratios=    notes= 
box/box14.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 804 vis_bbox=  col_bbox= 0.236220,0.167323,0.101270 ratios=    notes= 
box/box15.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 804 vis_bbox=  col_bbox= 0.236220,0.167323,0.101270 ratios=    notes= 
cup/cup00.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 322 collision_pts= 0 vis_bbox= 0.098243,0.098963,0.120000 col_bbox= 0.084000,0.084000,0.120000 ratios= 0.8550 0.8488 1.0000 notes= 
kiwi/kiwi05.usd verdict= BAD_BBOX_MISMATCH visual_pts= 74339 collision_pts= 0 vis_bbox= 0.091068,0.077496,0.090081 col_bbox= 0.045240,0.045240,0.068440 ratios= 0.4968 0.5838 0.7598 notes= 
kiwi/kiwi07.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 4945 collision_pts= 0 vis_bbox= 0.045790,0.055493,0.060000 col_bbox= 0.055493,0.055493,0.060000 ratios= 1.2119 1.0000 1.0000 notes= 
lime/lime03.usd verdict= BAD_BBOX_MISMATCH visual_pts= 14359 collision_pts= 0 vis_bbox= 0.099745,0.090720,0.082816 col_bbox= 0.054000,0.054000,0.060000 ratios= 0.5414 0.5952 0.7245 notes= 
peach/peach01.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 40255 collision_pts= 0 vis_bbox= 0.067394,0.070000,0.061474 col_bbox= 0.070000,0.070000,0.073500 ratios= 1.0387 1.0000 1.1956 notes= 
peach/peach03.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 6380 collision_pts= 0 vis_bbox= 0.065000,0.056332,0.054182 col_bbox= 0.065000,0.065000,0.068250 ratios= 1.0000 1.1539 1.2596 notes= 
peach/peach06.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 9126 collision_pts= 0 vis_bbox= 0.058944,0.060000,0.053447 col_bbox= 0.060000,0.060000,0.063000 ratios= 1.0179 1.0000 1.1787 notes= 
placemat/placemat00.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 8 vis_bbox=  col_bbox= 0.150000,0.150000,0.000200 ratios=    notes= 
placemat/placemat01.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 8 vis_bbox=  col_bbox= 0.150000,0.150000,0.000200 ratios=    notes= 
placemat/placemat02.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 8 vis_bbox=  col_bbox= 0.150000,0.150000,0.000200 ratios=    notes= 
placemat/placemat03.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 8 vis_bbox=  col_bbox= 0.150000,0.150000,0.000200 ratios=    notes= 
placemat/placemat04.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 8 vis_bbox=  col_bbox= 0.150000,0.150000,0.000200 ratios=    notes= 
placemat/placemat05.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 8 vis_bbox=  col_bbox= 0.150000,0.150000,0.000200 ratios=    notes= 
plate/plate00.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 2202 vis_bbox=  col_bbox= 0.150000,0.149998,0.013592 ratios=    notes= 
plate/plate01.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 5506 vis_bbox=  col_bbox= 0.150000,0.150000,0.008993 ratios=    notes= 
plate/plate02.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 4140 vis_bbox=  col_bbox= 0.150000,0.150000,0.011890 ratios=    notes= 
plate/plate03.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 30359 vis_bbox=  col_bbox= 0.150000,0.150000,0.014913 ratios=    notes= 
plate/plate04.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 638 vis_bbox=  col_bbox= 0.150000,0.149197,0.023125 ratios=    notes= 
plate/plate05.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 872 vis_bbox=  col_bbox= 0.150000,0.150000,0.013963 ratios=    notes= 
plate/plate06.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 2498 vis_bbox=  col_bbox= 0.150000,0.150000,0.012920 ratios=    notes= 
plate/plate07.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 579 vis_bbox=  col_bbox= 0.150000,0.150000,0.007769 ratios=    notes= 
plate/plate08.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 706 vis_bbox=  col_bbox= 0.150000,0.150000,0.010012 ratios=    notes= 
plate/plate09.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1102 vis_bbox=  col_bbox= 0.149703,0.150000,0.009371 ratios=    notes= 
plate/plate10.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 872 vis_bbox=  col_bbox= 0.150000,0.150000,0.013963 ratios=    notes= 
plate/plate12.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 3012 vis_bbox=  col_bbox= 0.150000,0.150000,0.016133 ratios=    notes= 
plate/plate13.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 2838 vis_bbox=  col_bbox= 0.150000,0.150000,0.010129 ratios=    notes= 
plate/plate14.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 14464 vis_bbox=  col_bbox= 0.150000,0.148998,0.013097 ratios=    notes= 
plate/plate15.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1187 vis_bbox=  col_bbox= 0.150000,0.150000,0.012566 ratios=    notes= 
plate/plate16.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 63230 vis_bbox=  col_bbox= 0.143427,0.074588,0.150000 ratios=    notes= 
potato/potato10.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 2327 collision_pts= 0 vis_bbox= 0.059144,0.048759,0.080000 col_bbox= 0.059144,0.059144,0.080000 ratios= 1.0000 1.2130 1.0000 notes= 
potato/potato14.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 722 collision_pts= 0 vis_bbox= 0.056465,0.044784,0.100000 col_bbox= 0.056465,0.056465,0.100000 ratios= 1.0000 1.2608 1.0000 notes= 
potato/potato18.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 12362 collision_pts= 0 vis_bbox= 0.077272,0.066055,0.100000 col_bbox= 0.077272,0.077272,0.100000 ratios= 1.0000 1.1698 1.0000 notes= 
tangerine/tangerine00.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 4596 collision_pts= 0 vis_bbox= 0.080000,0.078897,0.064489 col_bbox= 0.080000,0.080000,0.084000 ratios= 1.0000 1.0140 1.3025 notes= 
tangerine/tangerine03.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 25942 collision_pts= 0 vis_bbox= 0.082724,0.085000,0.075159 col_bbox= 0.085000,0.085000,0.089250 ratios= 1.0275 1.0000 1.1875 notes= 
tangerine/tangerine04.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 6274 collision_pts= 0 vis_bbox= 0.070000,0.069719,0.060313 col_bbox= 0.070000,0.070000,0.073500 ratios= 1.0000 1.0040 1.2186 notes= 
tangerine/tangerine06.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 1768 collision_pts= 0 vis_bbox= 0.069840,0.070000,0.051056 col_bbox= 0.070000,0.070000,0.073500 ratios= 1.0023 1.0000 1.4396 notes= 
tomato/tomato01.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 327 collision_pts= 0 vis_bbox= 0.085000,0.084994,0.076639 col_bbox= 0.085000,0.085000,0.089250 ratios= 1.0000 1.0001 1.1645 notes= 
tomato/tomato02.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 2421 collision_pts= 0 vis_bbox= 0.080000,0.080000,0.071558 col_bbox= 0.080000,0.080000,0.084000 ratios= 1.0000 1.0000 1.1739 notes= 
tray/tray04.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 744 vis_bbox=  col_bbox= 0.250000,0.150000,0.042500 ratios=    notes= 
tray/tray05.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1158 vis_bbox=  col_bbox= 0.200000,0.118869,0.031726 ratios=    notes= 
tray/tray06.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1158 vis_bbox=  col_bbox= 0.200000,0.118869,0.031726 ratios=    notes= 
tray/tray07.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1158 vis_bbox=  col_bbox= 0.200000,0.118869,0.031726 ratios=    notes= 
tray/tray08.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1158 vis_bbox=  col_bbox= 0.200000,0.118869,0.031726 ratios=    notes= 
tray/tray09.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1158 vis_bbox=  col_bbox= 0.200000,0.118869,0.031726 ratios=    notes= 
tray/tray10.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1158 vis_bbox=  col_bbox= 0.200000,0.118869,0.031726 ratios=    notes= 
tray/tray11.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1158 vis_bbox=  col_bbox= 0.200000,0.118869,0.031726 ratios=    notes= 
tray/tray12.usd verdict= UNCLEAR_NEEDS_OVERLAY visual_pts= 0 collision_pts= 1158 vis_bbox=  col_bbox= 0.200000,0.118869,0.031726 ratios=    notes= 
unseen/peach99.usd verdict= ROUGH_PRIMITIVE_COLLISION visual_pts= 9126 collision_pts= 0 vis_bbox= 0.058944,0.060000,0.053447 col_bbox= 0.060000,0.060000,0.063000 ratios= 1.0179 1.0000 1.1787 notes= 

Likely good assets sample:
## Collision vs visual static audit
usd_files: 211
csv: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/dom_collision_vs_visual_audit.csv
json: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/dom_collision_vs_visual_audit.json

verdict_counts:
Counter({'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 126, 'EXACT_OR_SHARED_MESH_LIKELY': 65, 'ROUGH_PRIMITIVE_COLLISION': 18, 'BAD_BBOX_MISMATCH': 2})

## Category-level collision quality summary
apple        count  20 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 18, 'ROUGH_PRIMITIVE_COLLISION': 2}
avocado      count   7 {'ROUGH_PRIMITIVE_COLLISION': 1, 'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 6}
beer         count   8 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 8}
bottle       count  10 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 10}
bowl         count  19 {'EXACT_OR_SHARED_MESH_LIKELY': 19}
box          count  15 {'EXACT_OR_SHARED_MESH_LIKELY': 15}
can          count  17 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 17}
cup          count  10 {'ROUGH_PRIMITIVE_COLLISION': 1, 'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 9}
egg          count  11 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 11}
kiwi         count   3 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 1, 'BAD_BBOX_MISMATCH': 1, 'ROUGH_PRIMITIVE_COLLISION': 1}
lemon        count  13 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 13}
lime         count   4 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 3, 'BAD_BBOX_MISMATCH': 1}
onion        count   7 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 7}
orange       count   6 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 6}
peach        count   5 {'ROUGH_PRIMITIVE_COLLISION': 3, 'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 2}
placemat     count   6 {'EXACT_OR_SHARED_MESH_LIKELY': 6}
plate        count  16 {'EXACT_OR_SHARED_MESH_LIKELY': 16}
potato       count  11 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 8, 'ROUGH_PRIMITIVE_COLLISION': 3}
tangerine    count   5 {'ROUGH_PRIMITIVE_COLLISION': 4, 'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 1}
tomato       count   4 {'ROUGH_PRIMITIVE_COLLISION': 2, 'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 2}
tray         count   9 {'EXACT_OR_SHARED_MESH_LIKELY': 9}
unseen       count   5 {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 4, 'ROUGH_PRIMITIVE_COLLISION': 1}

## High-risk objects for manipulation

### BAD_BBOX_MISMATCH (count=2)
kiwi/kiwi05.usd                          vis_pts=  74339 col_pts=      0 ratios= 0.4968,  0.5838,  0.7598
lime/lime03.usd                          vis_pts=  14359 col_pts=      0 ratios= 0.5414,  0.5952,  0.7245

### ROUGH_PRIMITIVE_COLLISION (count=18)
apple/apple03.usd                        vis_pts=    555 col_pts=      0 ratios= 1.3131,  1.2775,  1.0500
apple/apple15.usd                        vis_pts=  55274 col_pts=      0 ratios= 1.1511,  1.1598,  1.0500
avocado/avocado00.usd                    vis_pts= 313495 col_pts=      0 ratios= 0.6926,  0.8076,  0.9631
cup/cup00.usd                            vis_pts=    322 col_pts=      0 ratios= 0.8550,  0.8488,  1.0000
kiwi/kiwi07.usd                          vis_pts=   4945 col_pts=      0 ratios= 1.2119,  1.0000,  1.0000
peach/peach01.usd                        vis_pts=  40255 col_pts=      0 ratios= 1.0387,  1.0000,  1.1956
peach/peach03.usd                        vis_pts=   6380 col_pts=      0 ratios= 1.0000,  1.1539,  1.2596
peach/peach06.usd                        vis_pts=   9126 col_pts=      0 ratios= 1.0179,  1.0000,  1.1787
potato/potato10.usd                      vis_pts=   2327 col_pts=      0 ratios= 1.0000,  1.2130,  1.0000
potato/potato14.usd                      vis_pts=    722 col_pts=      0 ratios= 1.0000,  1.2608,  1.0000
potato/potato18.usd                      vis_pts=  12362 col_pts=      0 ratios= 1.0000,  1.1698,  1.0000
tangerine/tangerine00.usd                vis_pts=   4596 col_pts=      0 ratios= 1.0000,  1.0140,  1.3025
tangerine/tangerine03.usd                vis_pts=  25942 col_pts=      0 ratios= 1.0275,  1.0000,  1.1875
tangerine/tangerine04.usd                vis_pts=   6274 col_pts=      0 ratios= 1.0000,  1.0040,  1.2186
tangerine/tangerine06.usd                vis_pts=   1768 col_pts=      0 ratios= 1.0023,  1.0000,  1.4396
tomato/tomato01.usd                      vis_pts=    327 col_pts=      0 ratios= 1.0000,  1.0001,  1.1645
tomato/tomato02.usd                      vis_pts=   2421 col_pts=      0 ratios= 1.0000,  1.0000,  1.1739
unseen/peach99.usd                       vis_pts=   9126 col_pts=      0 ratios= 1.0179,  1.0000,  1.1787

### BBOX_MATCH_BUT_SIMPLIFIED_COLLISION (count=126)
apple/apple00.usd                        vis_pts=   5178 col_pts=      0 ratios= 1.0000,  1.0048,  1.0518
apple/apple01.usd                        vis_pts=   1274 col_pts=      0 ratios= 1.0000,  1.0485,  1.0766
apple/apple02.usd                        vis_pts=    898 col_pts=      0 ratios= 1.0414,  0.9680,  1.0517
apple/apple04.usd                        vis_pts=    898 col_pts=      0 ratios= 1.0414,  0.9680,  1.0517
apple/apple05.usd                        vis_pts=    719 col_pts=      0 ratios= 1.0000,  0.9904,  1.1414
apple/apple06.usd                        vis_pts=    898 col_pts=      0 ratios= 1.0414,  0.9680,  1.0517
apple/apple07.usd                        vis_pts=    825 col_pts=      0 ratios= 1.0000,  1.0044,  1.1063
apple/apple08.usd                        vis_pts=   1207 col_pts=      0 ratios= 1.0999,  1.0513,  1.0573
apple/apple09.usd                        vis_pts= 120214 col_pts=      0 ratios= 1.0152,  0.9678,  1.0517
apple/apple10.usd                        vis_pts=    305 col_pts=      0 ratios= 1.0861,  1.1070,  1.0500
apple/apple11.usd                        vis_pts=  54672 col_pts=      0 ratios= 1.0096,  1.0054,  1.0500
apple/apple12.usd                        vis_pts=    880 col_pts=      0 ratios= 1.0414,  0.9680,  1.0517
apple/apple13.usd                        vis_pts=   2721 col_pts=      0 ratios= 1.0000,  1.0062,  1.0589
apple/apple14.usd                        vis_pts=  14611 col_pts=      0 ratios= 1.0190,  1.0169,  1.0500
apple/apple18.usd                        vis_pts=   1538 col_pts=      0 ratios= 1.0000,  1.0945,  1.0886
apple/apple19.usd                        vis_pts=    898 col_pts=      0 ratios= 1.0414,  0.9680,  1.0517
apple/apple20.usd                        vis_pts=   1358 col_pts=      0 ratios= 0.9844,  0.9936,  0.9100
apple/apple22.usd                        vis_pts=   1483 col_pts=      0 ratios= 1.0187,  1.0622,  1.0500
avocado/avocado01.usd                    vis_pts=   2203 col_pts=      0 ratios= 1.0000,  1.0109,  1.0000
avocado/avocado02.usd                    vis_pts=    493 col_pts=      0 ratios= 1.0000,  1.0106,  1.0000
avocado/avocado04.usd                    vis_pts=  69005 col_pts=      0 ratios= 1.0000,  1.0221,  1.0000
avocado/avocado05.usd                    vis_pts= 201891 col_pts=      0 ratios= 1.0000,  1.0124,  1.0000
avocado/avocado06.usd                    vis_pts=    242 col_pts=      0 ratios= 1.0000,  1.0025,  1.0000
avocado/avocado08.usd                    vis_pts=    289 col_pts=      0 ratios= 1.0000,  1.0891,  1.0000
beer/beer00.usd                          vis_pts=   1024 col_pts=      0 ratios= 1.0266,  1.0110,  0.9900
beer/beer01.usd                          vis_pts=   1901 col_pts=      0 ratios= 0.9857,  0.9918,  0.9800
beer/beer03.usd                          vis_pts=    694 col_pts=      0 ratios= 0.9610,  0.9610,  0.9800
beer/beer05.usd                          vis_pts=   3475 col_pts=      0 ratios= 0.9512,  0.9512,  0.9800
beer/beer07.usd                          vis_pts=  16272 col_pts=      0 ratios= 1.0212,  1.0212,  0.9800
beer/beer09.usd                          vis_pts=    256 col_pts=      0 ratios= 0.9526,  0.9526,  0.9800
beer/beer13.usd                          vis_pts=    458 col_pts=      0 ratios= 0.9993,  0.9938,  0.9800
beer/beer19.usd                          vis_pts=   4762 col_pts=      0 ratios= 1.0372,  1.0372,  0.9800
bottle/dbottle02.usd                     vis_pts=   3785 col_pts=      0 ratios= 1.0335,  1.0354,  0.9875
bottle/dbottle04.usd                     vis_pts=  84243 col_pts=      0 ratios= 0.9712,  0.9863,  0.9200
bottle/wbottle01.usd                     vis_pts=    525 col_pts=      0 ratios= 0.9894,  0.9894,  0.9200
bottle/wbottle02.usd                     vis_pts=  35145 col_pts=      0 ratios= 0.9583,  0.9583,  0.9000
bottle/wbottle07.usd                     vis_pts=  19782 col_pts=      0 ratios= 0.9991,  0.9991,  0.9800
bottle/wbottle08.usd                     vis_pts=   1681 col_pts=      0 ratios= 1.0342,  1.0342,  0.9400
bottle/wbottle11.usd                     vis_pts=   5428 col_pts=      0 ratios= 1.0161,  1.0162,  0.9200
bottle/wbottle12.usd                     vis_pts=   5505 col_pts=      0 ratios= 1.0226,  1.0226,  0.9512

### EXACT_OR_SHARED_MESH_LIKELY (count=65)
bowl/bowl00.usd                          vis_pts=    826 col_pts=    826 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl01.usd                          vis_pts=    742 col_pts=    742 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl02.usd                          vis_pts=    448 col_pts=    448 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl04.usd                          vis_pts= 133201 col_pts= 133201 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl05.usd                          vis_pts=   1969 col_pts=   1969 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl06.usd                          vis_pts=  51332 col_pts=  51332 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl07.usd                          vis_pts=    469 col_pts=    469 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl08.usd                          vis_pts=   1766 col_pts=   1766 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl09.usd                          vis_pts=  72139 col_pts=  72139 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl10.usd                          vis_pts=   3079 col_pts=   3079 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl11.usd                          vis_pts=  30313 col_pts=  30313 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl12.usd                          vis_pts=   1304 col_pts=   1304 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl13.usd                          vis_pts=   1024 col_pts=   1024 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl14.usd                          vis_pts=    897 col_pts=    897 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl15.usd                          vis_pts=    498 col_pts=    498 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl16.usd                          vis_pts=   3313 col_pts=   3313 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl17.usd                          vis_pts=  90444 col_pts=  90444 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl18.usd                          vis_pts=    826 col_pts=    826 ratios= 1.0000,  1.0000,  1.0000
bowl/bowl19.usd                          vis_pts=  33602 col_pts=  33602 ratios= 1.0000,  1.0000,  1.0000
box/box00.usd                            vis_pts=   5960 col_pts=   5960 ratios= 1.0000,  1.0000,  1.0000
box/box01.usd                            vis_pts=   5960 col_pts=   5960 ratios= 1.0000,  1.0000,  1.0000
box/box02.usd                            vis_pts=   5960 col_pts=   5960 ratios= 1.0000,  1.0000,  1.0000
box/box03.usd                            vis_pts=   5960 col_pts=   5960 ratios= 1.0000,  1.0000,  1.0000
box/box04.usd                            vis_pts=   5960 col_pts=   5960 ratios= 1.0000,  1.0000,  1.0000
box/box05.usd                            vis_pts=   5960 col_pts=   5960 ratios= 1.0000,  1.0000,  1.0000
box/box06.usd                            vis_pts=     16 col_pts=     16 ratios= 1.0000,  1.0000,  1.0000
box/box08.usd                            vis_pts=    804 col_pts=    804 ratios= 1.0000,  1.0000,  1.0000
box/box09.usd                            vis_pts=    804 col_pts=    804 ratios= 1.0000,  1.0000,  1.0000
box/box10.usd                            vis_pts=    804 col_pts=    804 ratios= 1.0000,  1.0000,  1.0000
box/box11.usd                            vis_pts=    804 col_pts=    804 ratios= 1.0000,  1.0000,  1.0000
box/box12.usd                            vis_pts=    804 col_pts=    804 ratios= 1.0000,  1.0000,  1.0000
box/box13.usd                            vis_pts=    804 col_pts=    804 ratios= 1.0000,  1.0000,  1.0000
box/box14.usd                            vis_pts=    804 col_pts=    804 ratios= 1.0000,  1.0000,  1.0000
box/box15.usd                            vis_pts=    804 col_pts=    804 ratios= 1.0000,  1.0000,  1.0000
placemat/placemat00.usd                  vis_pts=      8 col_pts=      8 ratios= 1.0000,  1.0000,  1.0000
placemat/placemat01.usd                  vis_pts=      8 col_pts=      8 ratios= 1.0000,  1.0000,  1.0000
placemat/placemat02.usd                  vis_pts=      8 col_pts=      8 ratios= 1.0000,  1.0000,  1.0000
placemat/placemat03.usd                  vis_pts=      8 col_pts=      8 ratios= 1.0000,  1.0000,  1.0000
placemat/placemat04.usd                  vis_pts=      8 col_pts=      8 ratios= 1.0000,  1.0000,  1.0000
placemat/placemat05.usd                  vis_pts=      8 col_pts=      8 ratios= 1.0000,  1.0000,  1.0000

## Key Task Objects Quality

CUP: 11
  cup/cup00.usd                            ROUGH_PRIMITIVE_COLLISION           vis_pts=    322 col_pts=      0
  cup/cup01.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    475 col_pts=      0
  cup/cup02.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    475 col_pts=      0
  cup/cup03.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    475 col_pts=      0
  cup/cup04.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    475 col_pts=      0
  cup/cup05.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1631 col_pts=      0
  cup/cup06.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1631 col_pts=      0
  cup/cup07.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1631 col_pts=      0
  cup/cup08.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1631 col_pts=      0
  cup/cup09.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1631 col_pts=      0
  unseen/cup99.usd                         BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    475 col_pts=      0

BOWL: 19
  bowl/bowl00.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    826 col_pts=    826
  bowl/bowl01.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    742 col_pts=    742
  bowl/bowl02.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    448 col_pts=    448
  bowl/bowl04.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts= 133201 col_pts= 133201
  bowl/bowl05.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1969 col_pts=   1969
  bowl/bowl06.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=  51332 col_pts=  51332
  bowl/bowl07.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    469 col_pts=    469
  bowl/bowl08.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1766 col_pts=   1766
  bowl/bowl09.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=  72139 col_pts=  72139
  bowl/bowl10.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   3079 col_pts=   3079
  bowl/bowl11.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=  30313 col_pts=  30313
  bowl/bowl12.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1304 col_pts=   1304
  bowl/bowl13.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1024 col_pts=   1024
  bowl/bowl14.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    897 col_pts=    897
  bowl/bowl15.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    498 col_pts=    498
  bowl/bowl16.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   3313 col_pts=   3313
  bowl/bowl17.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=  90444 col_pts=  90444
  bowl/bowl18.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    826 col_pts=    826
  bowl/bowl19.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=  33602 col_pts=  33602

BOTTLE: 11
  bottle/dbottle02.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   3785 col_pts=      0
  bottle/dbottle04.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=  84243 col_pts=      0
  bottle/wbottle01.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    525 col_pts=      0
  bottle/wbottle02.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=  35145 col_pts=      0
  bottle/wbottle07.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=  19782 col_pts=      0
  bottle/wbottle08.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1681 col_pts=      0
  bottle/wbottle11.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   5428 col_pts=      0
  bottle/wbottle12.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   5505 col_pts=      0
  bottle/wbottle17.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts= 163454 col_pts=      0
  bottle/wbottle23.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   2666 col_pts=      0
  unseen/dbottle99.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   3785 col_pts=      0

CAN: 18
  can/can00.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   2111 col_pts=      0
  can/can02.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    264 col_pts=      0
  can/can03.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   3770 col_pts=      0
  can/can04.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1003 col_pts=      0
  can/can11.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   6287 col_pts=      0
  can/can12.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   2748 col_pts=      0
  can/can13.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    771 col_pts=      0
  can/can15.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    227 col_pts=      0
  can/fcan01.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   4922 col_pts=      0
  can/fcan03.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    130 col_pts=      0
  can/fcan04.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    785 col_pts=      0
  can/fcan05.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=  33100 col_pts=      0
  can/fcan08.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    595 col_pts=      0
  can/fcan11.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    204 col_pts=      0
  can/fcan15.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=     98 col_pts=      0
  can/fcan17.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   3554 col_pts=      0
  can/fcan18.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   3554 col_pts=      0
  unseen/can99.usd                         BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   6287 col_pts=      0

TOMATO: 4
  tomato/tomato01.usd                      ROUGH_PRIMITIVE_COLLISION           vis_pts=    327 col_pts=      0
  tomato/tomato02.usd                      ROUGH_PRIMITIVE_COLLISION           vis_pts=   2421 col_pts=      0
  tomato/tomato03.usd                      BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=  43447 col_pts=      0
  tomato/tomato07.usd                      BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts= 141188 col_pts=      0

APPLE: 21
  apple/apple00.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   5178 col_pts=      0
  apple/apple01.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1274 col_pts=      0
  apple/apple02.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    898 col_pts=      0
  apple/apple03.usd                        ROUGH_PRIMITIVE_COLLISION           vis_pts=    555 col_pts=      0
  apple/apple04.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    898 col_pts=      0
  apple/apple05.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    719 col_pts=      0
  apple/apple06.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    898 col_pts=      0
  apple/apple07.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    825 col_pts=      0
  apple/apple08.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1207 col_pts=      0
  apple/apple09.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts= 120214 col_pts=      0
  apple/apple10.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    305 col_pts=      0
  apple/apple11.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=  54672 col_pts=      0
  apple/apple12.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    880 col_pts=      0
  apple/apple13.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   2721 col_pts=      0
  apple/apple14.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=  14611 col_pts=      0
  apple/apple15.usd                        ROUGH_PRIMITIVE_COLLISION           vis_pts=  55274 col_pts=      0
  apple/apple18.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1538 col_pts=      0
  apple/apple19.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    898 col_pts=      0
  apple/apple20.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1358 col_pts=      0
  apple/apple22.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=   1483 col_pts=      0
  unseen/apple99.usd                       BBOX_MATCH_BUT_SIMPLIFIED_COLLISION vis_pts=    898 col_pts=      0

BOX: 15
  box/box00.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   5960 col_pts=   5960
  box/box01.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   5960 col_pts=   5960
  box/box02.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   5960 col_pts=   5960
  box/box03.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   5960 col_pts=   5960
  box/box04.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   5960 col_pts=   5960
  box/box05.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   5960 col_pts=   5960
  box/box06.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=     16 col_pts=     16
  box/box08.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    804 col_pts=    804
  box/box09.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    804 col_pts=    804
  box/box10.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    804 col_pts=    804
  box/box11.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    804 col_pts=    804
  box/box12.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    804 col_pts=    804
  box/box13.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    804 col_pts=    804
  box/box14.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    804 col_pts=    804
  box/box15.usd                            EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    804 col_pts=    804

TRAY: 9
  tray/tray04.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=    744 col_pts=    744
  tray/tray05.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1158 col_pts=   1158
  tray/tray06.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1158 col_pts=   1158
  tray/tray07.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1158 col_pts=   1158
  tray/tray08.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1158 col_pts=   1158
  tray/tray09.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1158 col_pts=   1158
  tray/tray10.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1158 col_pts=   1158
  tray/tray11.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1158 col_pts=   1158
  tray/tray12.usd                          EXACT_OR_SHARED_MESH_LIKELY         vis_pts=   1158 col_pts=   1158

# FINAL SUMMARY
- report: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/DOM_COLLISION_VS_VISUAL_AUDIT.md
- csv: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/dom_collision_vs_visual_audit.csv
- json: /home/redafrix/tests/internship/isaac_dynamicVLA-test/reports/dom_collision_vs_visual_audit.json

verdict_counts: {'BBOX_MATCH_BUT_SIMPLIFIED_COLLISION': 126, 'ROUGH_PRIMITIVE_COLLISION': 18, 'EXACT_OR_SHARED_MESH_LIKELY': 65, 'BAD_BBOX_MISMATCH': 2}
good_count: 65
unclear_or_simplified_count: 126
bad_count: 20

Recommended interpretation:
Some assets have likely collision problems. Do not trust all objects blindly.

Top bad assets:
  apple/apple03.usd                        ROUGH_PRIMITIVE_COLLISION
  apple/apple15.usd                        ROUGH_PRIMITIVE_COLLISION
  avocado/avocado00.usd                    ROUGH_PRIMITIVE_COLLISION
  cup/cup00.usd                            ROUGH_PRIMITIVE_COLLISION
  kiwi/kiwi05.usd                          BAD_BBOX_MISMATCH
  kiwi/kiwi07.usd                          ROUGH_PRIMITIVE_COLLISION
  lime/lime03.usd                          BAD_BBOX_MISMATCH
  peach/peach01.usd                        ROUGH_PRIMITIVE_COLLISION
  peach/peach03.usd                        ROUGH_PRIMITIVE_COLLISION
  peach/peach06.usd                        ROUGH_PRIMITIVE_COLLISION
  potato/potato10.usd                      ROUGH_PRIMITIVE_COLLISION
  potato/potato14.usd                      ROUGH_PRIMITIVE_COLLISION
  potato/potato18.usd                      ROUGH_PRIMITIVE_COLLISION
  tangerine/tangerine00.usd                ROUGH_PRIMITIVE_COLLISION
  tangerine/tangerine03.usd                ROUGH_PRIMITIVE_COLLISION
  tangerine/tangerine04.usd                ROUGH_PRIMITIVE_COLLISION
  tangerine/tangerine06.usd                ROUGH_PRIMITIVE_COLLISION
  tomato/tomato01.usd                      ROUGH_PRIMITIVE_COLLISION
  tomato/tomato02.usd                      ROUGH_PRIMITIVE_COLLISION
  unseen/peach99.usd                       ROUGH_PRIMITIVE_COLLISION

Top unclear/simplified assets:
  apple/apple00.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple01.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple02.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple04.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple05.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple06.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple07.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple08.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple09.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple10.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple11.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple12.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple13.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple14.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple18.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple19.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple20.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  apple/apple22.usd                        BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  avocado/avocado01.usd                    BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  avocado/avocado02.usd                    BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  avocado/avocado04.usd                    BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  avocado/avocado05.usd                    BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  avocado/avocado06.usd                    BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  avocado/avocado08.usd                    BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  beer/beer00.usd                          BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  beer/beer01.usd                          BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  beer/beer03.usd                          BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  beer/beer05.usd                          BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  beer/beer07.usd                          BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  beer/beer09.usd                          BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  beer/beer13.usd                          BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  beer/beer19.usd                          BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  bottle/dbottle02.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  bottle/dbottle04.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  bottle/wbottle01.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  bottle/wbottle02.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  bottle/wbottle07.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  bottle/wbottle08.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  bottle/wbottle11.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  bottle/wbottle12.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  bottle/wbottle17.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  bottle/wbottle23.usd                     BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/can00.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/can02.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/can03.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/can04.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/can11.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/can12.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/can13.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/can15.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/fcan01.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/fcan03.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/fcan04.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/fcan05.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/fcan08.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/fcan11.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/fcan15.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/fcan17.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  can/fcan18.usd                           BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
  cup/cup01.usd                            BBOX_MATCH_BUT_SIMPLIFIED_COLLISION
