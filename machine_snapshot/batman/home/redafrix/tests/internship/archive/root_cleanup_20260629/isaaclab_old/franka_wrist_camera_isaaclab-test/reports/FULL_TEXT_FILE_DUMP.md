# Full Small Text File Dump


================================================================================
FILE: ./AGENTS.md
================================================================================
     1	# AGENTS.md
     2	
     3	This repository is an Isaac Lab data-collection and evaluation environment for Franka tabletop manipulation.
     4	
     5	## Architecture rules
     6	
     7	Keep modules small and single-purpose.
     8	
     9	Do not put task logic, policy logic, dataset writing, and simulator launching in the same file.
    10	
    11	Use configuration files under `configs/` for experiment/task parameters. Do not add CLI arguments unless the value must change per invocation, such as config path, headless mode, device, or output directory.
    12	
    13	Do not add broad `try/except` blocks. If a failure should stop data collection, let it fail clearly. Only catch exceptions when the code can recover in a specific, tested way.
    14	
    15	Do not add fallback behavior that silently changes semantics. No hidden alternate camera paths, no silent object respawn, no automatic task substitution, no ignored failed resets.
    16	
    17	Use dataclasses for typed configs and episode/task records.
    18	
    19	Keep all randomization seeded and recorded in episode metadata.
    20	
    21	Every episode must record:
    22	- task name
    23	- language instruction
    24	- seed
    25	- success flag
    26	- timestamps
    27	- camera frame paths or arrays
    28	- robot state
    29	- action representation
    30	- object poses
    31	- randomization metadata
    32	
    33	## File ownership
    34	
    35	`scene/` owns Isaac Lab scene construction and assets.
    36	
    37	`tasks/` owns task definitions, reset sampling, language templates, and success checks.
    38	
    39	`policies/` owns scripted demonstrators.
    40	
    41	`control/` owns IK, gripper control, motion primitives, and trajectory utilities.
    42	
    43	`episode/` owns episode schemas, reset orchestration, and recording.
    44	
    45	`export/` owns conversion to model-specific formats.
    46	
    47	`scripts/` should only load configs and call package code.
    48	
    49	## Code quality
    50	
    51	Prefer explicit simple code over clever abstractions.
    52	
    53	Do not introduce framework-like registries unless there are at least two concrete implementations using them.
    54	
    55	No global mutable state except Isaac Sim application objects that must be global.
    56	
    57	No hardcoded absolute paths. Use config values or paths relative to repo root.
    58	
    59	No print spam in library code. Use concise logging from scripts.
    60	
    61	Do not mix debug visualization with data collection logic.
    62	
    63	Keep Isaac Sim compatibility patches isolated in `app/launcher.py`.
    64	
    65	## Testing expectations
    66	
    67	Pure Python modules must be testable without launching Isaac Sim.
    68	
    69	Task sampling, language generation, success predicates, episode schema validation, and exporters should have unit tests.
    70	
    71	Simulation-dependent tests should be smoke tests only:
    72	- scene launches
    73	- reset runs
    74	- one scripted episode finishes
    75	- one episode writes a valid dataset directory

================================================================================
FILE: ./configs/collection.yaml
================================================================================
     1	output_dir: data/raw/debug_pick_place
     2	start_episode_id: 0
     3	num_episodes: 20
     4	max_steps: 2400
     5	settle_time_s: 1.0
     6	
     7	record_cameras: true
     8	camera_fps: 30
     9	record_depth: true
    10	
    11	seed: 123
    12	
    13	target_object:
    14	  catalog_config: object_catalog.generated.yaml
    15	  category_id: apple
    16	  variant_id: apple00
    17	
    18	pose_randomization:
    19	  object_xy_range:
    20	    x: [-0.05, 0.05]
    21	    y: [-0.05, 0.05]
    22	  place_xy_range:
    23	    x: [-0.06, 0.06]
    24	    y: [-0.06, 0.06]
    25	
    26	
    27	lighting_randomization:
    28	  dome_light_intensity_range: [650.0, 1200.0]
    29	  dome_light_color_options:
    30	    - [0.90, 0.90, 0.90]
    31	    - [1.00, 0.92, 0.84]
    32	    - [0.82, 0.88, 1.00]

================================================================================
FILE: ./configs/object_catalog.generated.yaml
================================================================================
     1	asset_root: objects
     2	categories:
     3	- id: apple
     4	  label: apple
     5	  split: train
     6	  role: target
     7	  affordances:
     8	  - pickable
     9	  - reachable
    10	  variants:
    11	  - id: apple00
    12	    usd_path: apple/apple00.usd
    13	  - id: apple01
    14	    usd_path: apple/apple01.usd
    15	  - id: apple02
    16	    usd_path: apple/apple02.usd
    17	  - id: apple03
    18	    usd_path: apple/apple03.usd
    19	  - id: apple04
    20	    usd_path: apple/apple04.usd
    21	  - id: apple05
    22	    usd_path: apple/apple05.usd
    23	  - id: apple06
    24	    usd_path: apple/apple06.usd
    25	  - id: apple07
    26	    usd_path: apple/apple07.usd
    27	  - id: apple08
    28	    usd_path: apple/apple08.usd
    29	  - id: apple09
    30	    usd_path: apple/apple09.usd
    31	  - id: apple10
    32	    usd_path: apple/apple10.usd
    33	  - id: apple11
    34	    usd_path: apple/apple11.usd
    35	  - id: apple12
    36	    usd_path: apple/apple12.usd
    37	  - id: apple13
    38	    usd_path: apple/apple13.usd
    39	  - id: apple14
    40	    usd_path: apple/apple14.usd
    41	  - id: apple15
    42	    usd_path: apple/apple15.usd
    43	  - id: apple18
    44	    usd_path: apple/apple18.usd
    45	  - id: apple19
    46	    usd_path: apple/apple19.usd
    47	  - id: apple20
    48	    usd_path: apple/apple20.usd
    49	  - id: apple22
    50	    usd_path: apple/apple22.usd
    51	- id: avocado
    52	  label: avocado
    53	  split: train
    54	  role: target
    55	  affordances:
    56	  - pickable
    57	  - reachable
    58	  variants:
    59	  - id: avocado00
    60	    usd_path: avocado/avocado00.usd
    61	  - id: avocado01
    62	    usd_path: avocado/avocado01.usd
    63	  - id: avocado02
    64	    usd_path: avocado/avocado02.usd
    65	  - id: avocado04
    66	    usd_path: avocado/avocado04.usd
    67	  - id: avocado05
    68	    usd_path: avocado/avocado05.usd
    69	  - id: avocado06
    70	    usd_path: avocado/avocado06.usd
    71	  - id: avocado08
    72	    usd_path: avocado/avocado08.usd
    73	- id: beer
    74	  label: beer
    75	  split: train
    76	  role: target
    77	  affordances:
    78	  - pickable
    79	  - reachable
    80	  variants:
    81	  - id: beer00
    82	    usd_path: beer/beer00.usd
    83	  - id: beer01
    84	    usd_path: beer/beer01.usd
    85	  - id: beer03
    86	    usd_path: beer/beer03.usd
    87	  - id: beer05
    88	    usd_path: beer/beer05.usd
    89	  - id: beer07
    90	    usd_path: beer/beer07.usd
    91	  - id: beer09
    92	    usd_path: beer/beer09.usd
    93	  - id: beer13
    94	    usd_path: beer/beer13.usd
    95	  - id: beer19
    96	    usd_path: beer/beer19.usd
    97	- id: bottle
    98	  label: bottle
    99	  split: train
   100	  role: target
   101	  affordances:
   102	  - pickable
   103	  - reachable
   104	  variants:
   105	  - id: dbottle02
   106	    usd_path: bottle/dbottle02.usd
   107	  - id: dbottle04
   108	    usd_path: bottle/dbottle04.usd
   109	  - id: wbottle01
   110	    usd_path: bottle/wbottle01.usd
   111	  - id: wbottle02
   112	    usd_path: bottle/wbottle02.usd
   113	  - id: wbottle07
   114	    usd_path: bottle/wbottle07.usd
   115	  - id: wbottle08
   116	    usd_path: bottle/wbottle08.usd
   117	  - id: wbottle11
   118	    usd_path: bottle/wbottle11.usd
   119	  - id: wbottle12
   120	    usd_path: bottle/wbottle12.usd
   121	  - id: wbottle17
   122	    usd_path: bottle/wbottle17.usd
   123	  - id: wbottle23
   124	    usd_path: bottle/wbottle23.usd
   125	- id: bowl
   126	  label: bowl
   127	  split: train
   128	  role: target
   129	  affordances:
   130	  - pickable
   131	  - reachable
   132	  variants:
   133	  - id: bowl00
   134	    usd_path: bowl/bowl00.usd
   135	  - id: bowl01
   136	    usd_path: bowl/bowl01.usd
   137	  - id: bowl02
   138	    usd_path: bowl/bowl02.usd
   139	  - id: bowl04
   140	    usd_path: bowl/bowl04.usd
   141	  - id: bowl05
   142	    usd_path: bowl/bowl05.usd
   143	  - id: bowl06
   144	    usd_path: bowl/bowl06.usd
   145	  - id: bowl07
   146	    usd_path: bowl/bowl07.usd
   147	  - id: bowl08
   148	    usd_path: bowl/bowl08.usd
   149	  - id: bowl09
   150	    usd_path: bowl/bowl09.usd
   151	  - id: bowl10
   152	    usd_path: bowl/bowl10.usd
   153	  - id: bowl11
   154	    usd_path: bowl/bowl11.usd
   155	  - id: bowl12
   156	    usd_path: bowl/bowl12.usd
   157	  - id: bowl13
   158	    usd_path: bowl/bowl13.usd
   159	  - id: bowl14
   160	    usd_path: bowl/bowl14.usd
   161	  - id: bowl15
   162	    usd_path: bowl/bowl15.usd
   163	  - id: bowl16
   164	    usd_path: bowl/bowl16.usd
   165	  - id: bowl17
   166	    usd_path: bowl/bowl17.usd
   167	  - id: bowl18
   168	    usd_path: bowl/bowl18.usd
   169	  - id: bowl19
   170	    usd_path: bowl/bowl19.usd
   171	- id: box
   172	  label: box
   173	  split: train
   174	  role: target
   175	  affordances:
   176	  - pickable
   177	  - reachable
   178	  variants:
   179	  - id: box00
   180	    usd_path: box/box00.usd
   181	  - id: box01
   182	    usd_path: box/box01.usd
   183	  - id: box02
   184	    usd_path: box/box02.usd
   185	  - id: box03
   186	    usd_path: box/box03.usd
   187	  - id: box04
   188	    usd_path: box/box04.usd
   189	  - id: box05
   190	    usd_path: box/box05.usd
   191	  - id: box06
   192	    usd_path: box/box06.usd
   193	  - id: box08
   194	    usd_path: box/box08.usd
   195	  - id: box09
   196	    usd_path: box/box09.usd
   197	  - id: box10
   198	    usd_path: box/box10.usd
   199	  - id: box11
   200	    usd_path: box/box11.usd
   201	  - id: box12
   202	    usd_path: box/box12.usd
   203	  - id: box13
   204	    usd_path: box/box13.usd
   205	  - id: box14
   206	    usd_path: box/box14.usd
   207	  - id: box15
   208	    usd_path: box/box15.usd
   209	- id: can
   210	  label: can
   211	  split: train
   212	  role: target
   213	  affordances:
   214	  - pickable
   215	  - reachable
   216	  variants:
   217	  - id: can00
   218	    usd_path: can/can00.usd
   219	  - id: can02
   220	    usd_path: can/can02.usd
   221	  - id: can03
   222	    usd_path: can/can03.usd
   223	  - id: can04
   224	    usd_path: can/can04.usd
   225	  - id: can11
   226	    usd_path: can/can11.usd
   227	  - id: can12
   228	    usd_path: can/can12.usd
   229	  - id: can13
   230	    usd_path: can/can13.usd
   231	  - id: can15
   232	    usd_path: can/can15.usd
   233	  - id: fcan01
   234	    usd_path: can/fcan01.usd
   235	  - id: fcan03
   236	    usd_path: can/fcan03.usd
   237	  - id: fcan04
   238	    usd_path: can/fcan04.usd
   239	  - id: fcan05
   240	    usd_path: can/fcan05.usd
   241	  - id: fcan08
   242	    usd_path: can/fcan08.usd
   243	  - id: fcan11
   244	    usd_path: can/fcan11.usd
   245	  - id: fcan15
   246	    usd_path: can/fcan15.usd
   247	  - id: fcan17
   248	    usd_path: can/fcan17.usd
   249	  - id: fcan18
   250	    usd_path: can/fcan18.usd
   251	- id: cup
   252	  label: cup
   253	  split: train
   254	  role: target
   255	  affordances:
   256	  - pickable
   257	  - reachable
   258	  variants:
   259	  - id: cup00
   260	    usd_path: cup/cup00.usd
   261	  - id: cup01
   262	    usd_path: cup/cup01.usd
   263	  - id: cup02
   264	    usd_path: cup/cup02.usd
   265	  - id: cup03
   266	    usd_path: cup/cup03.usd
   267	  - id: cup04
   268	    usd_path: cup/cup04.usd
   269	  - id: cup05
   270	    usd_path: cup/cup05.usd
   271	  - id: cup06
   272	    usd_path: cup/cup06.usd
   273	  - id: cup07
   274	    usd_path: cup/cup07.usd
   275	  - id: cup08
   276	    usd_path: cup/cup08.usd
   277	  - id: cup09
   278	    usd_path: cup/cup09.usd
   279	- id: egg
   280	  label: egg
   281	  split: train
   282	  role: target
   283	  affordances:
   284	  - pickable
   285	  - reachable
   286	  variants:
   287	  - id: egg00
   288	    usd_path: egg/egg00.usd
   289	  - id: egg03
   290	    usd_path: egg/egg03.usd
   291	  - id: egg04
   292	    usd_path: egg/egg04.usd
   293	  - id: egg05
   294	    usd_path: egg/egg05.usd
   295	  - id: egg06
   296	    usd_path: egg/egg06.usd
   297	  - id: egg07
   298	    usd_path: egg/egg07.usd
   299	  - id: egg09
   300	    usd_path: egg/egg09.usd
   301	  - id: egg10
   302	    usd_path: egg/egg10.usd
   303	  - id: egg11
   304	    usd_path: egg/egg11.usd
   305	  - id: egg12
   306	    usd_path: egg/egg12.usd
   307	  - id: egg13
   308	    usd_path: egg/egg13.usd
   309	- id: kiwi
   310	  label: kiwi
   311	  split: train
   312	  role: target
   313	  affordances:
   314	  - pickable
   315	  - reachable
   316	  variants:
   317	  - id: kiwi00
   318	    usd_path: kiwi/kiwi00.usd
   319	  - id: kiwi05
   320	    usd_path: kiwi/kiwi05.usd
   321	  - id: kiwi07
   322	    usd_path: kiwi/kiwi07.usd
   323	- id: lemon
   324	  label: lemon
   325	  split: train
   326	  role: target
   327	  affordances:
   328	  - pickable
   329	  - reachable
   330	  variants:
   331	  - id: lemon01
   332	    usd_path: lemon/lemon01.usd
   333	  - id: lemon02
   334	    usd_path: lemon/lemon02.usd
   335	  - id: lemon03
   336	    usd_path: lemon/lemon03.usd
   337	  - id: lemon04
   338	    usd_path: lemon/lemon04.usd
   339	  - id: lemon05
   340	    usd_path: lemon/lemon05.usd
   341	  - id: lemon06
   342	    usd_path: lemon/lemon06.usd
   343	  - id: lemon08
   344	    usd_path: lemon/lemon08.usd
   345	  - id: lemon09
   346	    usd_path: lemon/lemon09.usd
   347	  - id: lemon10
   348	    usd_path: lemon/lemon10.usd
   349	  - id: lemon12
   350	    usd_path: lemon/lemon12.usd
   351	  - id: lemon13
   352	    usd_path: lemon/lemon13.usd
   353	  - id: lemon14
   354	    usd_path: lemon/lemon14.usd
   355	  - id: lemon15
   356	    usd_path: lemon/lemon15.usd
   357	- id: lime
   358	  label: lime
   359	  split: train
   360	  role: target
   361	  affordances:
   362	  - pickable
   363	  - reachable
   364	  variants:
   365	  - id: lime00
   366	    usd_path: lime/lime00.usd
   367	  - id: lime01
   368	    usd_path: lime/lime01.usd
   369	  - id: lime02
   370	    usd_path: lime/lime02.usd
   371	  - id: lime03
   372	    usd_path: lime/lime03.usd
   373	- id: onion
   374	  label: onion
   375	  split: train
   376	  role: target
   377	  affordances:
   378	  - pickable
   379	  - reachable
   380	  variants:
   381	  - id: onion00
   382	    usd_path: onion/onion00.usd
   383	  - id: onion02
   384	    usd_path: onion/onion02.usd
   385	  - id: onion04
   386	    usd_path: onion/onion04.usd
   387	  - id: onion07
   388	    usd_path: onion/onion07.usd
   389	  - id: onion08
   390	    usd_path: onion/onion08.usd
   391	  - id: onion09
   392	    usd_path: onion/onion09.usd
   393	  - id: onion10
   394	    usd_path: onion/onion10.usd
   395	- id: orange
   396	  label: orange
   397	  split: train
   398	  role: target
   399	  affordances:
   400	  - pickable
   401	  - reachable
   402	  variants:
   403	  - id: orange02
   404	    usd_path: orange/orange02.usd
   405	  - id: orange03
   406	    usd_path: orange/orange03.usd
   407	  - id: orange05
   408	    usd_path: orange/orange05.usd
   409	  - id: orange09
   410	    usd_path: orange/orange09.usd
   411	  - id: orange12
   412	    usd_path: orange/orange12.usd
   413	  - id: orange13
   414	    usd_path: orange/orange13.usd
   415	- id: peach
   416	  label: peach
   417	  split: train
   418	  role: target
   419	  affordances:
   420	  - pickable
   421	  - reachable
   422	  variants:
   423	  - id: peach01
   424	    usd_path: peach/peach01.usd
   425	  - id: peach02
   426	    usd_path: peach/peach02.usd
   427	  - id: peach03
   428	    usd_path: peach/peach03.usd
   429	  - id: peach05
   430	    usd_path: peach/peach05.usd
   431	  - id: peach06
   432	    usd_path: peach/peach06.usd
   433	- id: placemat
   434	  label: placemat
   435	  split: train
   436	  role: clutter
   437	  affordances:
   438	  - reachable
   439	  - support
   440	  variants:
   441	  - id: placemat00
   442	    usd_path: placemat/placemat00.usd
   443	  - id: placemat01
   444	    usd_path: placemat/placemat01.usd
   445	  - id: placemat02
   446	    usd_path: placemat/placemat02.usd
   447	  - id: placemat03
   448	    usd_path: placemat/placemat03.usd
   449	  - id: placemat04
   450	    usd_path: placemat/placemat04.usd
   451	  - id: placemat05
   452	    usd_path: placemat/placemat05.usd
   453	- id: plate
   454	  label: plate
   455	  split: train
   456	  role: clutter
   457	  affordances:
   458	  - reachable
   459	  - support
   460	  variants:
   461	  - id: plate00
   462	    usd_path: plate/plate00.usd
   463	  - id: plate01
   464	    usd_path: plate/plate01.usd
   465	  - id: plate02
   466	    usd_path: plate/plate02.usd
   467	  - id: plate03
   468	    usd_path: plate/plate03.usd
   469	  - id: plate04
   470	    usd_path: plate/plate04.usd
   471	  - id: plate05
   472	    usd_path: plate/plate05.usd
   473	  - id: plate06
   474	    usd_path: plate/plate06.usd
   475	  - id: plate07
   476	    usd_path: plate/plate07.usd
   477	  - id: plate08
   478	    usd_path: plate/plate08.usd
   479	  - id: plate09
   480	    usd_path: plate/plate09.usd
   481	  - id: plate10
   482	    usd_path: plate/plate10.usd
   483	  - id: plate12
   484	    usd_path: plate/plate12.usd
   485	  - id: plate13
   486	    usd_path: plate/plate13.usd
   487	  - id: plate14
   488	    usd_path: plate/plate14.usd
   489	  - id: plate15
   490	    usd_path: plate/plate15.usd
   491	  - id: plate16
   492	    usd_path: plate/plate16.usd
   493	- id: potato
   494	  label: potato
   495	  split: train
   496	  role: target
   497	  affordances:
   498	  - pickable
   499	  - reachable
   500	  variants:
   501	  - id: potato00
   502	    usd_path: potato/potato00.usd
   503	  - id: potato02
   504	    usd_path: potato/potato02.usd
   505	  - id: potato03
   506	    usd_path: potato/potato03.usd
   507	  - id: potato06
   508	    usd_path: potato/potato06.usd
   509	  - id: potato07
   510	    usd_path: potato/potato07.usd
   511	  - id: potato10
   512	    usd_path: potato/potato10.usd
   513	  - id: potato13
   514	    usd_path: potato/potato13.usd
   515	  - id: potato14
   516	    usd_path: potato/potato14.usd
   517	  - id: potato16
   518	    usd_path: potato/potato16.usd
   519	  - id: potato17
   520	    usd_path: potato/potato17.usd
   521	  - id: potato18
   522	    usd_path: potato/potato18.usd
   523	- id: tangerine
   524	  label: tangerine
   525	  split: train
   526	  role: target
   527	  affordances:
   528	  - pickable
   529	  - reachable
   530	  variants:
   531	  - id: tangerine00
   532	    usd_path: tangerine/tangerine00.usd
   533	  - id: tangerine03
   534	    usd_path: tangerine/tangerine03.usd
   535	  - id: tangerine04
   536	    usd_path: tangerine/tangerine04.usd
   537	  - id: tangerine05
   538	    usd_path: tangerine/tangerine05.usd
   539	  - id: tangerine06
   540	    usd_path: tangerine/tangerine06.usd
   541	- id: tomato
   542	  label: tomato
   543	  split: train
   544	  role: target
   545	  affordances:
   546	  - pickable
   547	  - reachable
   548	  variants:
   549	  - id: tomato01
   550	    usd_path: tomato/tomato01.usd
   551	  - id: tomato02
   552	    usd_path: tomato/tomato02.usd
   553	  - id: tomato03
   554	    usd_path: tomato/tomato03.usd
   555	  - id: tomato07
   556	    usd_path: tomato/tomato07.usd
   557	- id: tray
   558	  label: tray
   559	  split: train
   560	  role: clutter
   561	  affordances:
   562	  - reachable
   563	  - support
   564	  variants:
   565	  - id: tray04
   566	    usd_path: tray/tray04.usd
   567	  - id: tray05
   568	    usd_path: tray/tray05.usd
   569	  - id: tray06
   570	    usd_path: tray/tray06.usd
   571	  - id: tray07
   572	    usd_path: tray/tray07.usd
   573	  - id: tray08
   574	    usd_path: tray/tray08.usd
   575	  - id: tray09
   576	    usd_path: tray/tray09.usd
   577	  - id: tray10
   578	    usd_path: tray/tray10.usd
   579	  - id: tray11
   580	    usd_path: tray/tray11.usd
   581	  - id: tray12
   582	    usd_path: tray/tray12.usd
   583	- id: unseen_apple
   584	  label: apple
   585	  split: unseen
   586	  role: target
   587	  affordances:
   588	  - pickable
   589	  - reachable
   590	  variants:
   591	  - id: apple99
   592	    usd_path: unseen/apple99.usd
   593	- id: unseen_bottle
   594	  label: bottle
   595	  split: unseen
   596	  role: target
   597	  affordances:
   598	  - pickable
   599	  - reachable
   600	  variants:
   601	  - id: dbottle99
   602	    usd_path: unseen/dbottle99.usd
   603	- id: unseen_can
   604	  label: can
   605	  split: unseen
   606	  role: target
   607	  affordances:
   608	  - pickable
   609	  - reachable
   610	  variants:
   611	  - id: can99
   612	    usd_path: unseen/can99.usd
   613	- id: unseen_cup
   614	  label: cup
   615	  split: unseen
   616	  role: target
   617	  affordances:
   618	  - pickable
   619	  - reachable
   620	  variants:
   621	  - id: cup99
   622	    usd_path: unseen/cup99.usd
   623	- id: unseen_peach
   624	  label: peach
   625	  split: unseen
   626	  role: target
   627	  affordances:
   628	  - pickable
   629	  - reachable
   630	  variants:
   631	  - id: peach99
   632	    usd_path: unseen/peach99.usd

================================================================================
FILE: ./configs/object_catalog.yaml
================================================================================
     1	asset_root: objects
     2	
     3	categories:
     4	  - id: apple
     5	    label: apple
     6	    split: train
     7	    role: target
     8	    affordances: [pickable, reachable]
     9	    variants:
    10	      - id: apple00
    11	        usd_path: apple/apple00.usd
    12	      - id: apple01
    13	        usd_path: apple/apple01.usd
    14	      - id: apple02
    15	        usd_path: apple/apple02.usd
    16	
    17	  - id: can
    18	    label: can
    19	    split: train
    20	    role: target
    21	    affordances: [pickable, reachable]
    22	    variants:
    23	      - id: can00
    24	        usd_path: can/can00.usd
    25	      - id: can02
    26	        usd_path: can/can02.usd
    27	      - id: fcan01
    28	        usd_path: can/fcan01.usd
    29	
    30	  - id: cup
    31	    label: cup
    32	    split: train
    33	    role: target
    34	    affordances: [pickable, reachable]
    35	    variants:
    36	      - id: cup00
    37	        usd_path: cup/cup00.usd
    38	      - id: cup01
    39	        usd_path: cup/cup01.usd
    40	
    41	  - id: plate
    42	    label: plate
    43	    split: train
    44	    role: clutter
    45	    affordances: [reachable, support]
    46	    variants:
    47	      - id: plate00
    48	        usd_path: plate/plate00.usd
    49	      - id: plate02
    50	        usd_path: plate/plate02.usd
    51	
    52	  - id: unseen_apple
    53	    label: apple
    54	    split: unseen
    55	    role: target
    56	    affordances: [pickable, reachable]
    57	    variants:
    58	      - id: apple99
    59	        usd_path: unseen/apple99.usd

================================================================================
FILE: ./configs/objects.yaml
================================================================================
     1	objects:
     2	  - id: cube_primitive_006
     3	    label: cube
     4	    category: primitive
     5	    kind: cuboid
     6	    size: [0.06, 0.06, 0.06]
     7	    default_color:
     8	      name: red
     9	      rgb: [0.8, 0.15, 0.10]
    10	    grasp:
    11	      tcp_offset_local: [0.0, 0.0, 0.10]
    12	      pregrasp_height_m: 0.16
    13	      lift_height_m: 0.20
    14	    language:
    15	      aliases:
    16	        - cube
    17	        - block

================================================================================
FILE: ./configs/scene.yaml
================================================================================
     1	# Isaac Lab Franka Tabletop Scene Configurations (Active parameters only)
     2	
     3	sim:
     4	  dt: 0.008333333333333333 # 1/120
     5	
     6	robot:
     7	  base_pos: [0.1, 0.0, 1.05]
     8	
     9	table:
    10	  height_m: 1.05
    11	  size: [2.0, 2.0, 0.05]
    12	
    13	debug_circle:
    14	  center_local: [0.45, 0.0, 1.31] # 1.05 + 0.26
    15	  diameter_m: 0.40
    16	  frequency_hz: 0.045
    17	  orientation_wxyz: [0.0, 1.0, 0.0, 0.0]

================================================================================
FILE: ./.gitignore
================================================================================
     1	__pycache__/
     2	*.py[cod]
     3	*.egg-info/
     4	.ruff_cache/
     5	.mypy_cache/
     6	.pytest_cache/
     7	logs/
     8	runs/
     9	.cache/
    10	
    11	.thumbs/
    12	data/
    13	exports/
    14	

================================================================================
FILE: ./guidelines.md
================================================================================
     1	# Repository Coding Guidelines & Conventions
     2	
     3	This document records the architectural standards and implementation guidelines established for the Franka Tabletop Isaac Lab project. Refer to this to prevent design drift, circular dependencies, or simulation setup corruption.
     4	
     5	---
     6	
     7	## 1. Decoupled Architecture
     8	
     9	Keep the policy, trajectory generation, and controller loops strictly decoupled:
    10	
    11	*   **Policies**: Policies (e.g., `CircleMotionPolicy`, `PickPlaceScriptedPolicy`) are finite-state machines or neural network steps. They must output a unified command structure using the `PolicyCommand` dataclass.
    12	*   **Dataclasses / Commands**: `PolicyCommand` resides in `policies/scripted_base.py` and encapsulates:
    13	    *   `target_pos_w`: Tensor representing target TCP position in world coordinates.
    14	    *   `target_quat_w`: Tensor representing target TCP orientation in world coordinates.
    15	    *   `finger_opening_m`: Total opening width of one finger (parallel gripper fingers target the same distance).
    16	    *   `done`: Boolean flag indicating execution completion.
    17	*   **IK Controller**: `CartesianIKController` in `control/ik.py` should remain general. It must **never** contain code relating to circles, specific task trajectories, or gripper commands. It simply consumes `target_pos_w` and `target_quat_w`, computes differential IK, and sets joint targets.
    18	*   **Gripper Controller**: `GripperController` in `control/gripper.py` is dedicated to parallel finger controls.
    19	
    20	---
    21	
    22	## 2. Config Files & Settings
    23	
    24	To prevent drift risk between scene layouts and task planners, establish a single source of truth:
    25	
    26	*   **YAML Configuration**: Always mirror layout parameters (table heights, sizes, camera specifications, initial joint states) into `configs/scene.yaml`.
    27	*   **No Redundant Settings**: [settings.py](src/franka_wrist_camera_scene/settings.py) dynamically reads constants using `load_yaml_config("scene.yaml")` from `utils/paths.py` to maintain compatibility without risking settings drift.
    28	*   **Casing Conventions**: Use lowercase strings for conventions (e.g., `ros`, `world`) in configuration files to prevent parser mismatches inside Isaac Lab's camera and frame utilities.
    29	
    30	---
    31	
    32	## 3. Explicit Imports
    33	
    34	*   **Keep Package Roots Empty**: To prevent submodules from becoming dependency magnets, keep the package `__init__.py` clean. 
    35	*   **Explicit Submodule Imports**: Scripts and modules should import directly from the explicit submodule path (e.g., `from franka_wrist_camera_scene.control.ik import CartesianIKController`) rather than from the package root `__all__`.
    36	
    37	---
    38	
    39	## 4. Script Modularity
    40	
    41	Main entry scripts (e.g., [debug_scene.py](scripts/debug_scene.py)) must remain lightweight and restricted to CLI parsing, pipeline setup, and the simulation step loop:
    42	
    43	*   **Reset Logic**: episodic reset operations must be housed under `episode/reset.py` (e.g., `reset_robot_to_default(scene)`).
    44	*   **Camera Warmup**: RTX-specific render prim offsets or warmup workarounds must be housed under `app/camera_warmup.py` (e.g., `nudge_camera_prims(sim, scene)`).
    45	
    46	---
    47	
    48	## 5. Isaac Lab Simulation Conventions
    49	
    50	*   **Dynamic Rigid Bodies**: When creating movable objects (such as target manipulation cubes), spawn them using `RigidObjectCfg` instead of `AssetBaseCfg`.
    51	*   **Geometry Configuration**: Specify physics properties directly in the shape configuration using `rigid_props=sim_utils.RigidBodyPropertiesCfg()` and `collision_props=sim_utils.CollisionPropertiesCfg()` (Note: the keyword argument is `rigid_props`, **not** `rigid_body_props`).
    52	*   **TCP Alignment**: When target coordinates (like object pick poses) are defined in world coordinates, adjust wrist/hand commands by subtracting the TCP offset vector (`tcp_offset_w = quat_apply(quat_w, tcp_offset_local)`) to ensure the gripper matches the target's center instead of floating or penetrating the mesh.
    53	*   **Wrist Camera Updates**: Keep the hand-mounted camera's `update_period` at `0.0` to force updates on every physics simulation step, eliminating camera coordinate lag relative to rapid link movements.

================================================================================
FILE: ./objects/citation.tex
================================================================================
     1	@article{xie2026dynamicvla,
     2	  title     = {DynamicVLA: A Vision-Language-Action Model for 
     3	               Dynamic Object Manipulation},
     4	  author    = {Xie, Haozhe and 
     5	               Wen, Beichen and 
     6	               Zheng, Jiarui and 
     7	               Chen, Zhaoxi and 
     8	               Hong, Fangzhou and 
     9	               Diao, Haiwen and 
    10	               Liu, Ziwei},
    11	  journal   = {arXiv preprint arXiv:2601.22153},
    12	  year      = {2026}
    13	}

================================================================================
FILE: ./objects/metadata.json
================================================================================
     1	{
     2	    "apple00.usd": {
     3	        "tags": [
     4	            "apple",
     5	            "red apple",
     6	            "round apple",
     7	            "red round apple"
     8	        ]
     9	    },
    10	    "apple01.usd": {
    11	        "tags": [
    12	            "apple",
    13	            "round apple"
    14	        ]
    15	    },
    16	    "apple02.usd": {
    17	        "tags": [
    18	            "apple",
    19	            "red apple",
    20	            "round apple",
    21	            "red round apple"
    22	        ]
    23	    },
    24	    "apple03.usd": {
    25	        "tags": [
    26	            "apple",
    27	            "red apple",
    28	            "round apple",
    29	            "red round apple"
    30	        ]
    31	    },
    32	    "apple04.usd": {
    33	        "tags": [
    34	            "apple",
    35	            "red apple",
    36	            "round apple",
    37	            "red round apple"
    38	        ]
    39	    },
    40	    "apple05.usd": {
    41	        "tags": [
    42	            "apple",
    43	            "green apple",
    44	            "round apple",
    45	            "green round apple"
    46	        ]
    47	    },
    48	    "apple06.usd": {
    49	        "tags": [
    50	            "apple",
    51	            "red apple",
    52	            "round apple",
    53	            "red round apple"
    54	        ]
    55	    },
    56	    "apple07.usd": {
    57	        "tags": [
    58	            "apple",
    59	            "red apple",
    60	            "round apple",
    61	            "red round apple"
    62	        ]
    63	    },
    64	    "apple08.usd": {
    65	        "tags": [
    66	            "apple",
    67	            "brown apple",
    68	            "cone-shaped apple",
    69	            "brown cone-shaped apple"
    70	        ]
    71	    },
    72	    "apple09.usd": {
    73	        "tags": [
    74	            "apple",
    75	            "red apple",
    76	            "round apple",
    77	            "red round apple"
    78	        ]
    79	    },
    80	    "apple10.usd": {
    81	        "tags": [
    82	            "apple",
    83	            "red apple",
    84	            "round apple",
    85	            "red round apple"
    86	        ]
    87	    },
    88	    "apple12.usd": {
    89	        "tags": [
    90	            "apple",
    91	            "red apple",
    92	            "round apple",
    93	            "red round apple"
    94	        ]
    95	    },
    96	    "apple13.usd": {
    97	        "tags": [
    98	            "apple",
    99	            "yellow-green apple",
   100	            "round apple",
   101	            "yellow-green round apple"
   102	        ]
   103	    },
   104	    "apple14.usd": {
   105	        "tags": [
   106	            "apple",
   107	            "red apple",
   108	            "round apple",
   109	            "red round apple"
   110	        ]
   111	    },
   112	    "apple15.usd": {
   113	        "tags": [
   114	            "apple",
   115	            "half-ripe red apple",
   116	            "round apple",
   117	            "half-ripe red round apple"
   118	        ]
   119	    },
   120	    "apple18.usd": {
   121	        "tags": [
   122	            "apple",
   123	            "half-ripe red apple",
   124	            "round apple",
   125	            "half-ripe red round apple"
   126	        ]
   127	    },
   128	    "apple19.usd": {
   129	        "tags": [
   130	            "apple",
   131	            "red apple",
   132	            "round apple",
   133	            "red round apple"
   134	        ]
   135	    },
   136	    "apple20.usd": {
   137	        "tags": [
   138	            "apple",
   139	            "red apple",
   140	            "cone-shaped apple",
   141	            "red cone-shaped apple"
   142	        ]
   143	    },
   144	    "apple22.usd": {
   145	        "tags": [
   146	            "apple",
   147	            "red apple",
   148	            "round apple",
   149	            "red round apple"
   150	        ]
   151	    },
   152	    "avocado00.usd": {
   153	        "tags": [
   154	            "avocado",
   155	            "green avocado",
   156	            "fusiform avocado",
   157	            "green fusiform avocado"
   158	        ]
   159	    },
   160	    "avocado01.usd": {
   161	        "tags": [
   162	            "avocado",
   163	            "green avocado",
   164	            "long fusiform avocado",
   165	            "green long fusiform avocado"
   166	        ]
   167	    },
   168	    "avocado02.usd": {
   169	        "tags": [
   170	            "avocado",
   171	            "green avocado",
   172	            "pear-shaped long avocado",
   173	            "green pear-shaped long avocado"
   174	        ]
   175	    },
   176	    "avocado04.usd": {
   177	        "tags": [
   178	            "avocado",
   179	            "green avocado",
   180	            "pear-shaped long avocado",
   181	            "green pear-shaped long avocado"
   182	        ]
   183	    },
   184	    "avocado05.usd": {
   185	        "tags": [
   186	            "avocado",
   187	            "green avocado",
   188	            "pear-shaped avocado",
   189	            "green pear-shaped avocado"
   190	        ]
   191	    },
   192	    "avocado06.usd": {
   193	        "tags": [
   194	            "avocado",
   195	            "green avocado",
   196	            "pear-shaped long avocado",
   197	            "green pear-shaped long avocado"
   198	        ]
   199	    },
   200	    "avocado08.usd": {
   201	        "tags": [
   202	            "avocado",
   203	            "dark-green avocado",
   204	            "pear-shaped long avocado",
   205	            "dark-green pear-shaped long avocado"
   206	        ]
   207	    },
   208	    "beer00.usd": {
   209	        "tags": [
   210	            "beer bottle",
   211	            "dark color beer bottle",
   212	            "beer bottle with blue Genevra IPA sticker",
   213	            "dark color beer bottle with blue Genevra IPA sticker"
   214	        ]
   215	    },
   216	    "beer01.usd": {
   217	        "tags": [
   218	            "beer bottle",
   219	            "light color beer bottle",
   220	            "beer bottle with green Heineken sticker",
   221	            "light color beer bottle with green Heineken sticker"
   222	        ]
   223	    },
   224	    "beer03.usd": {
   225	        "tags": [
   226	            "beer bottle",
   227	            "light color beer bottle",
   228	            "beer bottle with Heineken carvings",
   229	            "light color beer bottle with Heineken carvings"
   230	        ]
   231	    },
   232	    "beer05.usd": {
   233	        "tags": [
   234	            "beer bottle",
   235	            "dark color beer bottle",
   236	            "beer bottle with white Asahi sticker",
   237	            "dark color beer bottle with white Asahi sticker"
   238	        ]
   239	    },
   240	    "beer07.usd": {
   241	        "tags": [
   242	            "beer bottle",
   243	            "light color beer bottle",
   244	            "beer bottle with golden Warsteiner sticker",
   245	            "light color beer bottle with golden Warsteiner sticker"
   246	        ]
   247	    },
   248	    "beer09.usd": {
   249	        "tags": [
   250	            "beer bottle",
   251	            "dark color beer bottle",
   252	            "beer bottle with red Estrella sticker",
   253	            "dark color beer bottle with red Estrella sticker"
   254	        ]
   255	    },
   256	    "beer13.usd": {
   257	        "tags": [
   258	            "beer bottle",
   259	            "dark color beer bottle",
   260	            "beer bottle with yellow Sunset sticker",
   261	            "dark color beer bottle with yellow Sunset sticker"
   262	        ]
   263	    },
   264	    "beer19.usd": {
   265	        "tags": [
   266	            "beer bottle",
   267	            "green beer bottle",
   268	            "beer bottle with no sticker",
   269	            "green beer bottle with no sticker"
   270	        ]
   271	    },
   272	    "dbottle02.usd": {
   273	        "tags": [
   274	            "drink bottle",
   275	            "pink and yellow drink bottle",
   276	            "cylinder drink bottle",
   277	            "drink bottle saying enjoi raspberry lemonade",
   278	            "pink and yellow cylinder drink bottle",
   279	            "pink and yellow drink bottle saying enjoi raspberry lemonade",
   280	            "cylinder drink bottle saying enjoi raspberry lemonade",
   281	            "pink and yellow cylinder drink bottle saying enjoi raspberry lemonade"
   282	        ]
   283	    },
   284	    "dbottle04.usd": {
   285	        "tags": [
   286	            "drink bottle",
   287	            "transparent plastic drink bottle",
   288	            "drink bottle saying wilkinson lemon",
   289	            "transparent plastic drink bottle saying wilkinson lemon"
   290	        ]
   291	    },
   292	    "wbottle01.usd": {
   293	        "tags": [
   294	            "drink bottle",
   295	            "green plastic drink bottle",
   296	            "long drink bottle",
   297	            "green plastic long drink bottle"
   298	        ]
   299	    },
   300	    "wbottle02.usd": {
   301	        "tags": [
   302	            "drink bottle",
   303	            "grey plastic drink bottle",
   304	            "drink bottle with blue lid",
   305	            "drink bottle with blue sticker saying most water",
   306	            "grey plastic drink bottle with blue lid",
   307	            "grey plastic drink bottle with blue sticker saying most water",
   308	            "drink bottle with blue lid and blue sticker saying most water",
   309	            "grey plastic drink bottle with blue lid and blue sticker saying most water"
   310	        ]
   311	    },
   312	    "wbottle07.usd": {
   313	        "tags": [
   314	            "water bottle",
   315	            "white water bottle",
   316	            "cylinder water bottle",
   317	            "water bottle with black lid",
   318	            "white cylinder water bottle",
   319	            "white water bottle with black lid",
   320	            "cylinder water bottle with black lid",
   321	            "white cylinder water bottle with black lid"
   322	        ]
   323	    },
   324	    "wbottle08.usd": {
   325	        "tags": [
   326	            "water bottle",
   327	            "blue water bottle",
   328	            "cylinder water bottle",
   329	            "water bottle with grey lid",
   330	            "blue cylinder water bottle",
   331	            "blue water bottle with grey lid",
   332	            "cylinder water bottle with grey lid",
   333	            "blue cylinder water bottle with grey lid"
   334	        ]
   335	    },
   336	    "wbottle11.usd": {
   337	        "tags": [
   338	            "drink bottle",
   339	            "grey plastic drink bottle",
   340	            "tall drink bottle",
   341	            "drink bottle with blue lid",
   342	            "drink bottle with white sticker",
   343	            "grey plastic tall drink bottle",
   344	            "grey plastic drink bottle with blue lid",
   345	            "grey plastic drink bottle with white sticker",
   346	            "tall drink bottle with blue lid",
   347	            "tall drink bottle with white sticker",
   348	            "drink bottle with blue lid and white sticker",
   349	            "grey plastic tall drink bottle with blue lid",
   350	            "grey plastic tall drink bottle with white sticker",
   351	            "grey plastic drink bottle with blue lid and white sticker",
   352	            "tall drink bottle with blue lid and white sticker",
   353	            "grey plastic tall drink bottle with blue lid and white sticker"
   354	        ]
   355	    },
   356	    "wbottle12.usd": {
   357	        "tags": [
   358	            "drink bottle",
   359	            "white plastic drink bottle",
   360	            "fat drink bottle",
   361	            "white plastic fat drink bottle"
   362	        ]
   363	    },
   364	    "wbottle17.usd": {
   365	        "tags": [
   366	            "drink bottle",
   367	            "blue plastic drink bottle",
   368	            "tall drink bottle",
   369	            "drink bottle with black lid",
   370	            "blue plastic tall drink bottle",
   371	            "blue plastic drink bottle with black lid",
   372	            "tall drink bottle with black lid",
   373	            "blue plastic tall drink bottle with black lid"
   374	        ]
   375	    },
   376	    "wbottle23.usd": {
   377	        "tags": [
   378	            "water bottle",
   379	            "black water bottle",
   380	            "cylinder water bottle",
   381	            "water bottle with grey and orange lid",
   382	            "black cylinder water bottle",
   383	            "black water bottle with grey and orange lid",
   384	            "cylinder water bottle with grey and orange lid",
   385	            "black cylinder water bottle with grey and orange lid"
   386	        ]
   387	    },
   388	    "bowl00.usd": {
   389	        "tags": [
   390	            "bowl",
   391	            "pure red bowl"
   392	        ]
   393	    },
   394	    "bowl01.usd": {
   395	        "tags": [
   396	            "bowl",
   397	            "ceramic bowl",
   398	            "bowl with enameled gold rim",
   399	            "ceramic bowl with enameled gold rim"
   400	        ]
   401	    },
   402	    "bowl02.usd": {
   403	        "tags": [
   404	            "bowl",
   405	            "orange bowl",
   406	            "bowl with black saw-shaped stripes",
   407	            "orange bowl with black saw-shaped stripes"
   408	        ]
   409	    },
   410	    "bowl04.usd": {
   411	        "tags": [
   412	            "bowl",
   413	            "white bowl",
   414	            "deep bowl",
   415	            "white deep bowl"
   416	        ]
   417	    },
   418	    "bowl05.usd": {
   419	        "tags": [
   420	            "bowl",
   421	            "grey bowl",
   422	            "shallow bowl",
   423	            "bowl with large bottom surface",
   424	            "grey shallow bowl",
   425	            "grey bowl with large bottom surface",
   426	            "shallow bowl with large bottom surface",
   427	            "grey shallow bowl with large bottom surface"
   428	        ]
   429	    },
   430	    "bowl06.usd": {
   431	        "tags": [
   432	            "bowl",
   433	            "ceramic bowl",
   434	            "deep bowl",
   435	            "bowl with black stripes",
   436	            "ceramic deep bowl",
   437	            "ceramic bowl with black stripes",
   438	            "deep bowl with black stripes",
   439	            "ceramic deep bowl with black stripes"
   440	        ]
   441	    },
   442	    "bowl07.usd": {
   443	        "tags": [
   444	            "bowl",
   445	            "dark brown bowl",
   446	            "wooden bowl",
   447	            "dark brown wooden bowl",
   448	            "shallow bowl",
   449	            "wooden shallow bowl"
   450	        ]
   451	    },
   452	    "bowl08.usd": {
   453	        "tags": [
   454	            "bowl",
   455	            "dark brown bowl",
   456	            "wooden bowl",
   457	            "dark brown wooden bowl",
   458	            "deep bowl",
   459	            "wooden deep bowl"
   460	        ]
   461	    },
   462	    "bowl09.usd": {
   463	        "tags": [
   464	            "bowl",
   465	            "dark brown bowl",
   466	            "wooden bowl",
   467	            "light brown wooden bowl",
   468	            "shallow bowl",
   469	            "wooden shallow bowl"
   470	        ]
   471	    },
   472	    "bowl10.usd": {
   473	        "tags": [
   474	            "bowl",
   475	            "wooden bowl",
   476	            "deep bowl",
   477	            "wooden deep bowl"
   478	        ]
   479	    },
   480	    "bowl11.usd": {
   481	        "tags": [
   482	            "bowl",
   483	            "ceramic bowl",
   484	            "deep bowl",
   485	            "bowl with cyan patterns",
   486	            "ceramic deep bowl",
   487	            "ceramic bowl with cyan patterns",
   488	            "deep bowl with cyan patterns",
   489	            "ceramic deep bowl with cyan patterns"
   490	        ]
   491	    },
   492	    "bowl12.usd": {
   493	        "tags": [
   494	            "bowl",
   495	            "ceramic bowl",
   496	            "deep bowl",
   497	            "bowl with floral patterns",
   498	            "ceramic deep bowl",
   499	            "ceramic bowl with floral patterns",
   500	            "deep bowl with floral patterns",
   501	            "ceramic deep bowl with floral patterns"
   502	        ]
   503	    },
   504	    "bowl13.usd": {
   505	        "tags": [
   506	            "bowl",
   507	            "ceramic bowl",
   508	            "shallow bowl",
   509	            "bowl with floral patterns",
   510	            "ceramic shallow bowl",
   511	            "ceramic bowl with floral patterns",
   512	            "shallow bowl with floral patterns",
   513	            "ceramic shallow bowl with floral patterns"
   514	        ]
   515	    },
   516	    "bowl14.usd": {
   517	        "tags": [
   518	            "bowl",
   519	            "marble bowl",
   520	            "deep bowl",
   521	            "marble deep bowl"
   522	        ]
   523	    },
   524	    "bowl15.usd": {
   525	        "tags": [
   526	            "bowl",
   527	            "wooden bowl",
   528	            "shallow bowl",
   529	            "wooden shallow bowl"
   530	        ]
   531	    },
   532	    "bowl16.usd": {
   533	        "tags": [
   534	            "bowl",
   535	            "ceramic bowl",
   536	            "deep bowl",
   537	            "bowl with bird patterns",
   538	            "ceramic deep bowl",
   539	            "ceramic bowl with bird patterns",
   540	            "deep bowl with bird patterns",
   541	            "ceramic deep bowl with bird patterns"
   542	        ]
   543	    },
   544	    "bowl17.usd": {
   545	        "tags": [
   546	            "bowl",
   547	            "ceramic bowl",
   548	            "deep bowl",
   549	            "bowl with pink floral patterns",
   550	            "ceramic deep bowl",
   551	            "ceramic bowl with pink floral patterns",
   552	            "deep bowl with pink floral patterns",
   553	            "ceramic deep bowl with pink floral patterns"
   554	        ]
   555	    },
   556	    "bowl18.usd": {
   557	        "tags": [
   558	            "bowl",
   559	            "grey bowl",
   560	            "shallow bowl",
   561	            "grey shallow bowl"
   562	        ]
   563	    },
   564	    "bowl19.usd": {
   565	        "tags": [
   566	            "bowl",
   567	            "yellow bowl",
   568	            "bowl saying puffo pops",
   569	            "yellow bowl saying puffo pops"
   570	        ]
   571	    },
   572	    "box00.usd": {
   573	        "tags": [
   574	            "box",
   575	            "black box",
   576	            "plastic box",
   577	            "black plastic box"
   578	        ]
   579	    },
   580	    "box01.usd": {
   581	        "tags": [
   582	            "box",
   583	            "white box",
   584	            "plastic box",
   585	            "white plastic box"
   586	        ]
   587	    },
   588	    "box02.usd": {
   589	        "tags": [
   590	            "box",
   591	            "pink box",
   592	            "plastic box",
   593	            "pink plastic box"
   594	        ]
   595	    },
   596	    "box03.usd": {
   597	        "tags": [
   598	            "box",
   599	            "green box",
   600	            "plastic box",
   601	            "green plastic box"
   602	        ]
   603	    },
   604	    "box04.usd": {
   605	        "tags": [
   606	            "box",
   607	            "yellow box",
   608	            "plastic box",
   609	            "yellow plastic box"
   610	        ]
   611	    },
   612	    "box05.usd": {
   613	        "tags": [
   614	            "box",
   615	            "blue box",
   616	            "plastic box",
   617	            "blue plastic box"
   618	        ]
   619	    },
   620	    "box06.usd": {
   621	        "tags": [
   622	            "box",
   623	            "paper box"
   624	        ]
   625	    },
   626	    "box08.usd": {
   627	        "tags": [
   628	            "box",
   629	            "red box",
   630	            "plastic box",
   631	            "box with MMLab At NTU words",
   632	            "red box with MMLab At NTU words"
   633	        ]
   634	    },
   635	    "box09.usd": {
   636	        "tags": [
   637	            "box",
   638	            "white box",
   639	            "plastic box",
   640	            "box with Microsoft Logo",
   641	            "white box with Microsoft Logo"
   642	        ]
   643	    },
   644	    "box10.usd": {
   645	        "tags": [
   646	            "box",
   647	            "white box",
   648	            "plastic box",
   649	            "box with Google Logo",
   650	            "white box with Google Logo"
   651	        ]
   652	    },
   653	    "box11.usd": {
   654	        "tags": [
   655	            "box",
   656	            "black box",
   657	            "plastic box",
   658	            "box with Apple Logo",
   659	            "black box with Apple Logo"
   660	        ]
   661	    },
   662	    "box12.usd": {
   663	        "tags": [
   664	            "box",
   665	            "white box",
   666	            "plastic box",
   667	            "box with Tencent Logo",
   668	            "white box with Tencent Logo"
   669	        ]
   670	    },
   671	    "box13.usd": {
   672	        "tags": [
   673	            "box",
   674	            "white box",
   675	            "plastic box",
   676	            "box with OpenAI Logo",
   677	            "white box with OpenAI Logo"
   678	        ]
   679	    },
   680	    "box14.usd": {
   681	        "tags": [
   682	            "box",
   683	            "white box",
   684	            "plastic box",
   685	            "box with Nvidia Logo",
   686	            "white box with Nvidia Logo"
   687	        ]
   688	    },
   689	    "box15.usd": {
   690	        "tags": [
   691	            "box",
   692	            "white box",
   693	            "plastic box",
   694	            "box with Tesla Logo",
   695	            "white box with Tesla Logo"
   696	        ]
   697	    },
   698	    "can00.usd": {
   699	        "tags": [
   700	            "drink can",
   701	            "red drink can",
   702	            "drink can with blue ColaCa words",
   703	            "red drink can with blue ColaCa words"
   704	        ]
   705	    },
   706	    "can02.usd": {
   707	        "tags": [
   708	            "drink can",
   709	            "red drink can",
   710	            "drink can with white COLA words",
   711	            "red drink can with white COLA words"
   712	        ]
   713	    },
   714	    "can03.usd": {
   715	        "tags": [
   716	            "drink can",
   717	            "blue drink can",
   718	            "drink can with Pepsi logo",
   719	            "blue drink can with Pepsi logo"
   720	        ]
   721	    },
   722	    "can04.usd": {
   723	        "tags": [
   724	            "drink can",
   725	            "red drink can",
   726	            "drink can with Coke logo",
   727	            "red drink can with Coke logo"
   728	        ]
   729	    },
   730	    "can11.usd": {
   731	        "tags": [
   732	            "drink can",
   733	            "red drink can",
   734	            "drink can with CocaCola Logo",
   735	            "red drink can with CocaCola Logo"
   736	        ]
   737	    },
   738	    "can12.usd": {
   739	        "tags": [
   740	            "drink can",
   741	            "red drink can"
   742	        ]
   743	    },
   744	    "can13.usd": {
   745	        "tags": [
   746	            "drink can",
   747	            "purple and yellow drink can",
   748	            "drink can with flower",
   749	            "purple and yellow drink can with flower"
   750	        ]
   751	    },
   752	    "can15.usd": {
   753	        "tags": [
   754	            "drink can",
   755	            "red drink can",
   756	            "drink can with CocaCola Logo",
   757	            "red drink can with CocaCola Logo"
   758	        ]
   759	    },
   760	    "fcan01.usd": {
   761	        "tags": [
   762	            "food can"
   763	        ]
   764	    },
   765	    "fcan03.usd": {
   766	        "tags": [
   767	            "food can",
   768	            "red food can",
   769	            "food can with Campbells Cream of Chicken words",
   770	            "red food can with Campbells Cream of Chicken words"
   771	        ]
   772	    },
   773	    "fcan04.usd": {
   774	        "tags": [
   775	            "food can",
   776	            "red food can",
   777	            "food can with Chef Royardee Beef Goodaroni words",
   778	            "red food can with Chef Royardee Beef Goodaroni words"
   779	        ]
   780	    },
   781	    "fcan05.usd": {
   782	        "tags": [
   783	            "food can",
   784	            "orange food can",
   785	            "food can with Falls Salmon words",
   786	            "orange food can with Falls Salmon words"
   787	        ]
   788	    },
   789	    "fcan08.usd": {
   790	        "tags": [
   791	            "food can",
   792	            "red food can",
   793	            "food can with Granny Beryls Tomato Soup words",
   794	            "red food can with Granny Beryls Tomato Soup words"
   795	        ]
   796	    },
   797	    "fcan11.usd": {
   798	        "tags": [
   799	            "food can",
   800	            "blue food can",
   801	            "food can with Heinz Beanz words",
   802	            "blue food can with Heinz Beanz words"
   803	        ]
   804	    },
   805	    "fcan15.usd": {
   806	        "tags": [
   807	            "food can",
   808	            "red food can",
   809	            "food can with Campbells Tomato Soup words",
   810	            "red food can with Campbells Tomato Soup words"
   811	        ]
   812	    },
   813	    "fcan17.usd": {
   814	        "tags": [
   815	            "food can",
   816	            "yellow and red food can",
   817	            "food can with golden bull logo",
   818	            "yellow and red food can with golden bull logo"
   819	        ]
   820	    },
   821	    "fcan18.usd": {
   822	        "tags": [
   823	            "food can",
   824	            "blue food can"
   825	        ]
   826	    },
   827	    "cup00.usd": {
   828	        "tags": [
   829	            "cup",
   830	            "tall cup",
   831	            "cone-shaped cup",
   832	            "tall cone-shaped cup"
   833	        ]
   834	    },
   835	    "cup01.usd": {
   836	        "tags": [
   837	            "cup",
   838	            "yellow cup",
   839	            "tall cup",
   840	            "cup with red flower",
   841	            "yellow tall cup",
   842	            "yellow cup with red flower",
   843	            "tall cup with red flower",
   844	            "yellow tall cup with red flower"
   845	        ]
   846	    },
   847	    "cup02.usd": {
   848	        "tags": [
   849	            "cup",
   850	            "yellow cup",
   851	            "tall cup",
   852	            "cup with red watermelon",
   853	            "yellow tall cup",
   854	            "yellow cup with red watermelon",
   855	            "tall cup with red watermelon",
   856	            "yellow tall cup with red watermelon"
   857	        ]
   858	    },
   859	    "cup03.usd": {
   860	        "tags": [
   861	            "cup",
   862	            "blue cup",
   863	            "tall cup",
   864	            "cup with NTU Singapore logo",
   865	            "blue tall cup",
   866	            "blue cup with NTU Singapore logo",
   867	            "tall cup with NTU Singapore logo",
   868	            "blue tall cup with NTU Singapore logo"
   869	        ]
   870	    },
   871	    "cup04.usd": {
   872	        "tags": [
   873	            "cup",
   874	            "red cup",
   875	            "tall cup",
   876	            "cup with MMLab at NTU logo",
   877	            "red tall cup",
   878	            "red cup with MMLab at NTU logo",
   879	            "tall cup with MMLab at NTU logo",
   880	            "red tall cup with MMLab at NTU logo"
   881	        ]
   882	    },
   883	    "cup05.usd": {
   884	        "tags": [
   885	            "cup",
   886	            "white cup",
   887	            "short cup",
   888	            "white short cup"
   889	        ]
   890	    },
   891	    "cup06.usd": {
   892	        "tags": [
   893	            "cup",
   894	            "white cup",
   895	            "tall cup",
   896	            "white tall cup"
   897	        ]
   898	    },
   899	    "cup07.usd": {
   900	        "tags": [
   901	            "cup",
   902	            "yellow cup",
   903	            "tall cup",
   904	            "yellow tall cup"
   905	        ]
   906	    },
   907	    "cup08.usd": {
   908	        "tags": [
   909	            "cup",
   910	            "red cup",
   911	            "tall cup",
   912	            "red tall cup"
   913	        ]
   914	    },
   915	    "cup09.usd": {
   916	        "tags": [
   917	            "cup",
   918	            "black cup",
   919	            "tall cup",
   920	            "black tall cup"
   921	        ]
   922	    },
   923	    "egg00.usd": {
   924	        "tags": [
   925	            "egg",
   926	            "white egg"
   927	        ]
   928	    },
   929	    "egg03.usd": {
   930	        "tags": [
   931	            "egg",
   932	            "light-brown egg"
   933	        ]
   934	    },
   935	    "egg04.usd": {
   936	        "tags": [
   937	            "egg",
   938	            "white egg",
   939	            "white egg woth subtle speckling"
   940	        ]
   941	    },
   942	    "egg05.usd": {
   943	        "tags": [
   944	            "egg",
   945	            "orange egg"
   946	        ]
   947	    },
   948	    "egg06.usd": {
   949	        "tags": [
   950	            "egg",
   951	            "brown egg"
   952	        ]
   953	    },
   954	    "egg07.usd": {
   955	        "tags": [
   956	            "egg",
   957	            "light-yellow egg"
   958	        ]
   959	    },
   960	    "egg09.usd": {
   961	        "tags": [
   962	            "egg",
   963	            "white egg"
   964	        ]
   965	    },
   966	    "egg10.usd": {
   967	        "tags": [
   968	            "egg",
   969	            "white egg",
   970	            "egg with scattered dark spots",
   971	            "white egg with scattered dark spots"
   972	        ]
   973	    },
   974	    "egg11.usd": {
   975	        "tags": [
   976	            "egg",
   977	            "brown egg"
   978	        ]
   979	    },
   980	    "egg12.usd": {
   981	        "tags": [
   982	            "egg",
   983	            "white egg"
   984	        ]
   985	    },
   986	    "egg13.usd": {
   987	        "tags": [
   988	            "egg",
   989	            "brown egg"
   990	        ]
   991	    },
   992	    "kiwi07.usd": {
   993	        "tags": [
   994	            "kiwi",
   995	            "light-green kiwi"
   996	        ]
   997	    },
   998	    "lime00.usd": {
   999	        "tags": [
  1000	            "lime",
  1001	            "dark green lime"
  1002	        ]
  1003	    },
  1004	    "lime01.usd": {
  1005	        "tags": [
  1006	            "lime",
  1007	            "light green lime"
  1008	        ]
  1009	    },
  1010	    "lime02.usd": {
  1011	        "tags": [
  1012	            "lime",
  1013	            "light green lime"
  1014	        ]
  1015	    },
  1016	    "lime03.usd": {
  1017	        "tags": [
  1018	            "lime",
  1019	            "dark green lime"
  1020	        ]
  1021	    },
  1022	    "onion00.usd": {
  1023	        "tags": [
  1024	            "onion",
  1025	            "red onion"
  1026	        ]
  1027	    },
  1028	    "onion02.usd": {
  1029	        "tags": [
  1030	            "onion",
  1031	            "white onion",
  1032	            "smooth onion",
  1033	            "white smooth onion"
  1034	        ]
  1035	    },
  1036	    "onion04.usd": {
  1037	        "tags": [
  1038	            "onion",
  1039	            "white onion",
  1040	            "rough onion",
  1041	            "white rough onion"
  1042	        ]
  1043	    },
  1044	    "onion07.usd": {
  1045	        "tags": [
  1046	            "onion",
  1047	            "red onion",
  1048	            "round onion",
  1049	            "red round onion"
  1050	        ]
  1051	    },
  1052	    "onion08.usd": {
  1053	        "tags": [
  1054	            "onion",
  1055	            "purple onion"
  1056	        ]
  1057	    },
  1058	    "onion09.usd": {
  1059	        "tags": [
  1060	            "onion",
  1061	            "white onion",
  1062	            "round onion",
  1063	            "onion with long stem",
  1064	            "white round onion",
  1065	            "white onion with long stem",
  1066	            "round onion with long stem",
  1067	            "white round onion with long stem"
  1068	        ]
  1069	    },
  1070	    "onion10.usd": {
  1071	        "tags": [
  1072	            "onion",
  1073	            "purple onion",
  1074	            "round onion",
  1075	            "onion with long stem",
  1076	            "purple round onion",
  1077	            "purple onion with long stem",
  1078	            "round onion with long stem",
  1079	            "purple round onion with long stem"
  1080	        ]
  1081	    },
  1082	    "orange02.usd": {
  1083	        "tags": [
  1084	            "orange",
  1085	            "red orange",
  1086	            "smooth orange",
  1087	            "red smooth orange"
  1088	        ]
  1089	    },
  1090	    "orange03.usd": {
  1091	        "tags": [
  1092	            "orange",
  1093	            "round orange"
  1094	        ]
  1095	    },
  1096	    "orange05.usd": {
  1097	        "tags": [
  1098	            "orange",
  1099	            "yellow orange"
  1100	        ]
  1101	    },
  1102	    "orange09.usd": {
  1103	        "tags": [
  1104	            "orange",
  1105	            "yellow orange",
  1106	            "wrinkled orange",
  1107	            "yellow wrinkled orange"
  1108	        ]
  1109	    },
  1110	    "orange12.usd": {
  1111	        "tags": [
  1112	            "orange",
  1113	            "yellow orange",
  1114	            "smooth orange",
  1115	            "yellow smooth orange"
  1116	        ]
  1117	    },
  1118	    "orange13.usd": {
  1119	        "tags": [
  1120	            "orange",
  1121	            "wrinkled orange"
  1122	        ]
  1123	    },
  1124	    "peach01.usd": {
  1125	        "tags": [
  1126	            "peach",
  1127	            "pink-white peach"
  1128	        ]
  1129	    },
  1130	    "peach02.usd": {
  1131	        "tags": [
  1132	            "peach",
  1133	            "pink-white peach"
  1134	        ]
  1135	    },
  1136	    "peach03.usd": {
  1137	        "tags": [
  1138	            "peach",
  1139	            "red peach"
  1140	        ]
  1141	    },
  1142	    "peach05.usd": {
  1143	        "tags": [
  1144	            "peach",
  1145	            "pink-white peach"
  1146	        ]
  1147	    },
  1148	    "peach06.usd": {
  1149	        "tags": [
  1150	            "peach",
  1151	            "white peach"
  1152	        ]
  1153	    },
  1154	    "placemat00.usd": {
  1155	        "tags": [
  1156	            "square placemat",
  1157	            "floral-patterned square placemat",
  1158	            "white big-flower patterned square placemat",
  1159	            "square mat with minimal large-floral design"
  1160	        ]
  1161	    },
  1162	    "placemat01.usd": {
  1163	        "tags": [
  1164	            "square placemat",
  1165	            "square placemat with Google logo"
  1166	        ]
  1167	    },
  1168	    "placemat02.usd": {
  1169	        "tags": [
  1170	            "woven mat",
  1171	            "square woven mat",
  1172	            "woven rattan mat",
  1173	            "woven mat with natural rattan texture",
  1174	            "square mat with straw texture texture"
  1175	        ]
  1176	    },
  1177	    "placemat03.usd": {
  1178	        "tags": [
  1179	            "square placemat",
  1180	            "floral-patterned square placemat",
  1181	            "square mat with green dense-floral pattern"
  1182	        ]
  1183	    },
  1184	    "placemat04.usd": {
  1185	        "tags": [
  1186	            "square placemat",
  1187	            "green square placemat"
  1188	        ]
  1189	    },
  1190	    "placemat05.usd": {
  1191	        "tags": [
  1192	            "square placemat",
  1193	            "square placemat with yellow background",
  1194	            "square placemat features a bold, stylized illustration of a tui",
  1195	            "Square placemat with a bold, stylized tui"
  1196	        ]
  1197	    },
  1198	    "plate00.usd": {
  1199	        "tags": [
  1200	            "plate",
  1201	            "yellow plate",
  1202	            "plate with red square patterns",
  1203	            "yellow plate with red square patterns"
  1204	        ]
  1205	    },
  1206	    "plate01.usd": {
  1207	        "tags": [
  1208	            "plate",
  1209	            "white plate"
  1210	        ]
  1211	    },
  1212	    "plate02.usd": {
  1213	        "tags": [
  1214	            "plate",
  1215	            "ceramic plate",
  1216	            "plate with blue floral patterns",
  1217	            "ceramic plate with blue floral patterns"
  1218	        ]
  1219	    },
  1220	    "plate03.usd": {
  1221	        "tags": [
  1222	            "plate",
  1223	            "white plate"
  1224	        ]
  1225	    },
  1226	    "plate04.usd": {
  1227	        "tags": [
  1228	            "plate",
  1229	            "white plate"
  1230	        ]
  1231	    },
  1232	    "plate05.usd": {
  1233	        "tags": [
  1234	            "plate",
  1235	            "yellow and red plate",
  1236	            "plate with floral patterns",
  1237	            "yellow and red plate with floral patterns"
  1238	        ]
  1239	    },
  1240	    "plate06.usd": {
  1241	        "tags": [
  1242	            "plate",
  1243	            "white plate",
  1244	            "plate with grey edge",
  1245	            "plate with black line patterns",
  1246	            "white plate with grey edge",
  1247	            "white plate with black line patterns",
  1248	            "plate with grey edge and black line patterns",
  1249	            "white plate with grey edge and black line patterns"
  1250	        ]
  1251	    },
  1252	    "plate07.usd": {
  1253	        "tags": [
  1254	            "plate",
  1255	            "yellow plate",
  1256	            "plate with white edge",
  1257	            "yellow plate with white edge"
  1258	        ]
  1259	    },
  1260	    "plate08.usd": {
  1261	        "tags": [
  1262	            "plate",
  1263	            "wooden plate"
  1264	        ]
  1265	    },
  1266	    "plate09.usd": {
  1267	        "tags": [
  1268	            "plate",
  1269	            "white plate"
  1270	        ]
  1271	    },
  1272	    "plate10.usd": {
  1273	        "tags": [
  1274	            "plate",
  1275	            "yellow and red plate",
  1276	            "plate with floral patterns",
  1277	            "yellow and red plate with floral patterns"
  1278	        ]
  1279	    },
  1280	    "plate12.usd": {
  1281	        "tags": [
  1282	            "plate",
  1283	            "blue plate"
  1284	        ]
  1285	    },
  1286	    "plate13.usd": {
  1287	        "tags": [
  1288	            "plate",
  1289	            "white plate"
  1290	        ]
  1291	    },
  1292	    "plate14.usd": {
  1293	        "tags": [
  1294	            "plate",
  1295	            "white plate",
  1296	            "plate with black edge",
  1297	            "plate with dragon patterns",
  1298	            "white plate with black edge",
  1299	            "white plate with dragon patterns",
  1300	            "plate with black edge and dragon patterns",
  1301	            "white plate with black edge and dragon patterns"
  1302	        ]
  1303	    },
  1304	    "plate15.usd": {
  1305	        "tags": [
  1306	            "plate",
  1307	            "white plate"
  1308	        ]
  1309	    },
  1310	    "plate16.usd": {
  1311	        "tags": [
  1312	            "plate",
  1313	            "plate with dart patterns"
  1314	        ]
  1315	    },
  1316	    "potato00.usd": {
  1317	        "tags": [
  1318	            "potato",
  1319	            "light color potato",
  1320	            "pitted potato",
  1321	            "light color pitted potato"
  1322	        ]
  1323	    },
  1324	    "potato02.usd": {
  1325	        "tags": [
  1326	            "potato",
  1327	            "dark color potato"
  1328	        ]
  1329	    },
  1330	    "potato03.usd": {
  1331	        "tags": [
  1332	            "potato",
  1333	            "light color potato",
  1334	            "long potato",
  1335	            "light color long potato"
  1336	        ]
  1337	    },
  1338	    "potato06.usd": {
  1339	        "tags": [
  1340	            "potato",
  1341	            "light color potato",
  1342	            "pitted potato",
  1343	            "long potato",
  1344	            "light color pitted potato",
  1345	            "light color long potato",
  1346	            "pitted long potato",
  1347	            "light color pitted long potato"
  1348	        ]
  1349	    },
  1350	    "potato07.usd": {
  1351	        "tags": [
  1352	            "potato",
  1353	            "light color potato",
  1354	            "fat potato",
  1355	            "light color fat potato"
  1356	        ]
  1357	    },
  1358	    "potato10.usd": {
  1359	        "tags": [
  1360	            "potato",
  1361	            "grey color potato",
  1362	            "pitted potato",
  1363	            "grey color pitted potato"
  1364	        ]
  1365	    },
  1366	    "potato13.usd": {
  1367	        "tags": [
  1368	            "potato",
  1369	            "yellow-black color potato"
  1370	        ]
  1371	    },
  1372	    "potato14.usd": {
  1373	        "tags": [
  1374	            "potato",
  1375	            "light color potato",
  1376	            "long potato",
  1377	            "pitted potato",
  1378	            "light color long potato",
  1379	            "light color pitted potato",
  1380	            "long pitted potato",
  1381	            "light color long pitted potato"
  1382	        ]
  1383	    },
  1384	    "potato16.usd": {
  1385	        "tags": [
  1386	            "potato",
  1387	            "light color potato"
  1388	        ]
  1389	    },
  1390	    "potato17.usd": {
  1391	        "tags": [
  1392	            "potato",
  1393	            "light color potato",
  1394	            "round potato",
  1395	            "light color round potato"
  1396	        ]
  1397	    },
  1398	    "potato18.usd": {
  1399	        "tags": [
  1400	            "potato",
  1401	            "light color potato",
  1402	            "pitted potato",
  1403	            "light color pitted potato"
  1404	        ]
  1405	    },
  1406	    "tomato01.usd": {
  1407	        "tags": [
  1408	            "tomato",
  1409	            "red tomato"
  1410	        ]
  1411	    },
  1412	    "tomato02.usd": {
  1413	        "tags": [
  1414	            "tomato",
  1415	            "red tomato",
  1416	            "round tomato",
  1417	            "red round tomato"
  1418	        ]
  1419	    },
  1420	    "tomato03.usd": {
  1421	        "tags": [
  1422	            "tomato",
  1423	            "red tomato"
  1424	        ]
  1425	    },
  1426	    "tomato07.usd": {
  1427	        "tags": [
  1428	            "tomato",
  1429	            "red tomato",
  1430	            "small tomato",
  1431	            "red small tomato"
  1432	        ]
  1433	    },
  1434	    "tray00.usd": {
  1435	        "tags": [
  1436	            "tray",
  1437	            "dark color tray",
  1438	            "wooden tray",
  1439	            "dark color wooden tray"
  1440	        ]
  1441	    },
  1442	    "tray01.usd": {
  1443	        "tags": [
  1444	            "tray",
  1445	            "white tray"
  1446	        ]
  1447	    },
  1448	    "tray02.usd": {
  1449	        "tags": [
  1450	            "tray",
  1451	            "red patterned tray"
  1452	        ]
  1453	    },
  1454	    "tray03.usd": {
  1455	        "tags": [
  1456	            "tray",
  1457	            "yellow tray",
  1458	            "tray with painting",
  1459	            "yellow tray with painting"
  1460	        ]
  1461	    },
  1462	    "tray04.usd": {
  1463	        "tags": [
  1464	            "tray",
  1465	            "light color tray",
  1466	            "wooden tray",
  1467	            "light color wooden tray"
  1468	        ]
  1469	    },
  1470	    "tray05.usd": {
  1471	        "tags": [
  1472	            "tray",
  1473	            "white tray",
  1474	            "tray with Bytedance logo",
  1475	            "white tray with Bytedance logo"
  1476	        ]
  1477	    },
  1478	    "tray06.usd": {
  1479	        "tags": [
  1480	            "tray",
  1481	            "white tray",
  1482	            "tray with NTU logo",
  1483	            "white tray with NTU logo"
  1484	        ]
  1485	    },
  1486	    "tray07.usd": {
  1487	        "tags": [
  1488	            "tray",
  1489	            "white tray",
  1490	            "tray with Meta logo",
  1491	            "white tray with Meta logo"
  1492	        ]
  1493	    },
  1494	    "tray08.usd": {
  1495	        "tags": [
  1496	            "tray",
  1497	            "white tray",
  1498	            "tray with CapitaLand logo",
  1499	            "white tray with CapitaLand logo"
  1500	        ]
  1501	    },
  1502	    "tray09.usd": {
  1503	        "tags": [
  1504	            "tray",
  1505	            "white tray",
  1506	            "tray with HSBC logo",
  1507	            "white tray with HSBC logo"
  1508	        ]
  1509	    },
  1510	    "tray10.usd": {
  1511	        "tags": [
  1512	            "tray",
  1513	            "white tray",
  1514	            "tray with Don Don Donki logo",
  1515	            "white tray with Don Don Donki logo"
  1516	        ]
  1517	    },
  1518	    "tray11.usd": {
  1519	        "tags": [
  1520	            "tray",
  1521	            "white tray",
  1522	            "tray with Shell logo",
  1523	            "white tray with Shell logo"
  1524	        ]
  1525	    },
  1526	    "tray12.usd": {
  1527	        "tags": [
  1528	            "tray",
  1529	            "white tray",
  1530	            "tray with Mastercard logo",
  1531	            "white tray with Mastercard logo"
  1532	        ]
  1533	    }
  1534	}

================================================================================
FILE: ./objects/tree.md
================================================================================
     1	# Objects Dataset Directory Tree
     2	
     3	This file lists the full directory and file structure of the `objects/` dataset at the repository root.
     4	
     5	```text
     6	objects/
     7	├── apple
     8	│   ├── texture
     9	│   │   ├── apple00.jpg
    10	│   │   ├── apple01.jpg
    11	│   │   ├── apple02.jpg
    12	│   │   ├── apple03.jpg
    13	│   │   ├── apple04.jpg
    14	│   │   ├── apple05.jpg
    15	│   │   ├── apple06.jpg
    16	│   │   ├── apple07.jpg
    17	│   │   ├── apple08.jpg
    18	│   │   ├── apple09.jpg
    19	│   │   ├── apple10.jpg
    20	│   │   ├── apple11.jpg
    21	│   │   ├── apple12.jpg
    22	│   │   ├── apple13.jpg
    23	│   │   ├── apple14.jpg
    24	│   │   ├── apple15.jpg
    25	│   │   ├── apple18.jpg
    26	│   │   ├── apple19.jpg
    27	│   │   ├── apple20.jpg
    28	│   │   └── apple22.jpg
    29	│   ├── apple00.usd
    30	│   ├── apple01.usd
    31	│   ├── apple02.usd
    32	│   ├── apple03.usd
    33	│   ├── apple04.usd
    34	│   ├── apple05.usd
    35	│   ├── apple06.usd
    36	│   ├── apple07.usd
    37	│   ├── apple08.usd
    38	│   ├── apple09.usd
    39	│   ├── apple10.usd
    40	│   ├── apple11.usd
    41	│   ├── apple12.usd
    42	│   ├── apple13.usd
    43	│   ├── apple14.usd
    44	│   ├── apple15.usd
    45	│   ├── apple18.usd
    46	│   ├── apple19.usd
    47	│   ├── apple20.usd
    48	│   └── apple22.usd
    49	├── avocado
    50	│   ├── texture
    51	│   │   ├── avocado00.jpg
    52	│   │   ├── avocado01.jpg
    53	│   │   ├── avocado02.jpg
    54	│   │   ├── avocado04.jpg
    55	│   │   ├── avocado05.jpg
    56	│   │   ├── avocado06.jpg
    57	│   │   └── avocado08.jpg
    58	│   ├── avocado00.usd
    59	│   ├── avocado01.usd
    60	│   ├── avocado02.usd
    61	│   ├── avocado04.usd
    62	│   ├── avocado05.usd
    63	│   ├── avocado06.usd
    64	│   └── avocado08.usd
    65	├── beer
    66	│   ├── texture
    67	│   │   ├── beer00.jpg
    68	│   │   ├── beer01.jpg
    69	│   │   ├── beer03.jpg
    70	│   │   ├── beer05.jpg
    71	│   │   ├── beer07.jpg
    72	│   │   ├── beer09.jpg
    73	│   │   ├── beer13.jpg
    74	│   │   └── beer19.jpg
    75	│   ├── beer00.usd
    76	│   ├── beer01.usd
    77	│   ├── beer03.usd
    78	│   ├── beer05.usd
    79	│   ├── beer07.usd
    80	│   ├── beer09.usd
    81	│   ├── beer13.usd
    82	│   └── beer19.usd
    83	├── bottle
    84	│   ├── texture
    85	│   │   ├── bottled_drink02.jpg
    86	│   │   ├── bottled_drink04.jpg
    87	│   │   ├── bottled_water01.jpg
    88	│   │   ├── bottled_water02.jpg
    89	│   │   ├── bottled_water11.jpg
    90	│   │   ├── water_bottle07.jpg
    91	│   │   ├── water_bottle08.jpg
    92	│   │   └── water_bottle23.jpg
    93	│   ├── dbottle02.usd
    94	│   ├── dbottle04.usd
    95	│   ├── wbottle01.usd
    96	│   ├── wbottle02.usd
    97	│   ├── wbottle07.usd
    98	│   ├── wbottle08.usd
    99	│   ├── wbottle11.usd
   100	│   ├── wbottle12.usd
   101	│   ├── wbottle17.usd
   102	│   └── wbottle23.usd
   103	├── bowl
   104	│   ├── texture
   105	│   │   ├── bowl00.jpg
   106	│   │   ├── bowl01.jpg
   107	│   │   ├── bowl02.jpg
   108	│   │   ├── bowl04.jpg
   109	│   │   ├── bowl06.jpg
   110	│   │   ├── bowl07.jpg
   111	│   │   ├── bowl08.jpg
   112	│   │   ├── bowl09.jpg
   113	│   │   ├── bowl10.jpg
   114	│   │   ├── bowl11.jpg
   115	│   │   ├── bowl12.jpg
   116	│   │   ├── bowl13.jpg
   117	│   │   ├── bowl14.jpg
   118	│   │   ├── bowl15.jpg
   119	│   │   ├── bowl16.jpg
   120	│   │   ├── bowl17.jpg
   121	│   │   ├── bowl18.jpg
   122	│   │   └── bowl19.jpg
   123	│   ├── bowl00.usd
   124	│   ├── bowl01.usd
   125	│   ├── bowl02.usd
   126	│   ├── bowl04.usd
   127	│   ├── bowl05.usd
   128	│   ├── bowl06.usd
   129	│   ├── bowl07.usd
   130	│   ├── bowl08.usd
   131	│   ├── bowl09.usd
   132	│   ├── bowl10.usd
   133	│   ├── bowl11.usd
   134	│   ├── bowl12.usd
   135	│   ├── bowl13.usd
   136	│   ├── bowl14.usd
   137	│   ├── bowl15.usd
   138	│   ├── bowl16.usd
   139	│   ├── bowl17.usd
   140	│   ├── bowl18.usd
   141	│   └── bowl19.usd
   142	├── box
   143	│   ├── texture
   144	│   │   ├── box06.jpg
   145	│   │   ├── box08.jpg
   146	│   │   ├── box09.jpg
   147	│   │   ├── box10.jpg
   148	│   │   ├── box11.jpg
   149	│   │   ├── box12.jpg
   150	│   │   ├── box13.jpg
   151	│   │   ├── box14.jpg
   152	│   │   └── box15.jpg
   153	│   ├── box00.usd
   154	│   ├── box01.usd
   155	│   ├── box02.usd
   156	│   ├── box03.usd
   157	│   ├── box04.usd
   158	│   ├── box05.usd
   159	│   ├── box06.usd
   160	│   ├── box08.usd
   161	│   ├── box09.usd
   162	│   ├── box10.usd
   163	│   ├── box11.usd
   164	│   ├── box12.usd
   165	│   ├── box13.usd
   166	│   ├── box14.usd
   167	│   └── box15.usd
   168	├── can
   169	│   ├── texture
   170	│   │   ├── can00.jpg
   171	│   │   ├── can02.jpg
   172	│   │   ├── can03.jpg
   173	│   │   ├── can04.jpg
   174	│   │   ├── can11.jpg
   175	│   │   ├── can12.jpg
   176	│   │   ├── can13.jpg
   177	│   │   ├── can15.jpg
   178	│   │   ├── canned_food01.jpg
   179	│   │   ├── canned_food03.jpg
   180	│   │   ├── canned_food04.jpg
   181	│   │   ├── canned_food05.jpg
   182	│   │   ├── canned_food08.jpg
   183	│   │   ├── canned_food11.jpg
   184	│   │   ├── canned_food15.jpg
   185	│   │   ├── canned_food17.jpg
   186	│   │   └── canned_food18.jpg
   187	│   ├── can00.usd
   188	│   ├── can02.usd
   189	│   ├── can03.usd
   190	│   ├── can04.usd
   191	│   ├── can11.usd
   192	│   ├── can12.usd
   193	│   ├── can13.usd
   194	│   ├── can15.usd
   195	│   ├── fcan01.usd
   196	│   ├── fcan03.usd
   197	│   ├── fcan04.usd
   198	│   ├── fcan05.usd
   199	│   ├── fcan08.usd
   200	│   ├── fcan11.usd
   201	│   ├── fcan15.usd
   202	│   ├── fcan17.usd
   203	│   └── fcan18.usd
   204	├── cup
   205	│   ├── texture
   206	│   │   ├── cup01.jpg
   207	│   │   ├── cup02.jpg
   208	│   │   ├── cup03.jpg
   209	│   │   └── cup04.jpg
   210	│   ├── cup00.usd
   211	│   ├── cup01.usd
   212	│   ├── cup02.usd
   213	│   ├── cup03.usd
   214	│   ├── cup04.usd
   215	│   ├── cup05.usd
   216	│   ├── cup06.usd
   217	│   ├── cup07.usd
   218	│   ├── cup08.usd
   219	│   └── cup09.usd
   220	├── egg
   221	│   ├── texture
   222	│   │   ├── egg03.jpg
   223	│   │   ├── egg04.jpg
   224	│   │   ├── egg05.jpg
   225	│   │   ├── egg06.jpg
   226	│   │   ├── egg07.jpg
   227	│   │   ├── egg09.jpg
   228	│   │   ├── egg10.jpg
   229	│   │   ├── egg11.jpg
   230	│   │   └── egg13.jpg
   231	│   ├── egg00.usd
   232	│   ├── egg03.usd
   233	│   ├── egg04.usd
   234	│   ├── egg05.usd
   235	│   ├── egg06.usd
   236	│   ├── egg07.usd
   237	│   ├── egg09.usd
   238	│   ├── egg10.usd
   239	│   ├── egg11.usd
   240	│   ├── egg12.usd
   241	│   └── egg13.usd
   242	├── kiwi
   243	│   ├── texture
   244	│   │   ├── kiwi00.jpg
   245	│   │   ├── kiwi05.jpg
   246	│   │   └── kiwi07.jpg
   247	│   ├── kiwi00.usd
   248	│   ├── kiwi05.usd
   249	│   └── kiwi07.usd
   250	├── lemon
   251	│   ├── texture
   252	│   │   ├── lemon01.jpg
   253	│   │   ├── lemon02.jpg
   254	│   │   ├── lemon03.jpg
   255	│   │   ├── lemon04.jpg
   256	│   │   ├── lemon05.jpg
   257	│   │   ├── lemon06.jpg
   258	│   │   ├── lemon08.jpg
   259	│   │   ├── lemon09.jpg
   260	│   │   ├── lemon10.jpg
   261	│   │   ├── lemon12.jpg
   262	│   │   ├── lemon13.jpg
   263	│   │   ├── lemon14.jpg
   264	│   │   └── lemon15.jpg
   265	│   ├── lemon01.usd
   266	│   ├── lemon02.usd
   267	│   ├── lemon03.usd
   268	│   ├── lemon04.usd
   269	│   ├── lemon05.usd
   270	│   ├── lemon06.usd
   271	│   ├── lemon08.usd
   272	│   ├── lemon09.usd
   273	│   ├── lemon10.usd
   274	│   ├── lemon12.usd
   275	│   ├── lemon13.usd
   276	│   ├── lemon14.usd
   277	│   └── lemon15.usd
   278	├── lime
   279	│   ├── texture
   280	│   │   ├── lime00.jpg
   281	│   │   ├── lime01.jpg
   282	│   │   ├── lime02.jpg
   283	│   │   └── lime03.jpg
   284	│   ├── lime00.usd
   285	│   ├── lime01.usd
   286	│   ├── lime02.usd
   287	│   └── lime03.usd
   288	├── onion
   289	│   ├── texture
   290	│   │   ├── onion00.jpg
   291	│   │   ├── onion02.jpg
   292	│   │   ├── onion04.jpg
   293	│   │   ├── onion07.jpg
   294	│   │   ├── onion08.jpg
   295	│   │   ├── onion09.jpg
   296	│   │   └── onion10.jpg
   297	│   ├── onion00.usd
   298	│   ├── onion02.usd
   299	│   ├── onion04.usd
   300	│   ├── onion07.usd
   301	│   ├── onion08.usd
   302	│   ├── onion09.usd
   303	│   └── onion10.usd
   304	├── orange
   305	│   ├── texture
   306	│   │   ├── orange02.jpg
   307	│   │   ├── orange03.jpg
   308	│   │   ├── orange04.jpg
   309	│   │   ├── orange05.jpg
   310	│   │   ├── orange09.jpg
   311	│   │   ├── orange12.jpg
   312	│   │   └── orange13.jpg
   313	│   ├── orange02.usd
   314	│   ├── orange03.usd
   315	│   ├── orange05.usd
   316	│   ├── orange09.usd
   317	│   ├── orange12.usd
   318	│   └── orange13.usd
   319	├── peach
   320	│   ├── texture
   321	│   │   ├── peach01.jpg
   322	│   │   ├── peach02.jpg
   323	│   │   ├── peach03.jpg
   324	│   │   ├── peach05.jpg
   325	│   │   └── peach06.jpg
   326	│   ├── peach01.usd
   327	│   ├── peach02.usd
   328	│   ├── peach03.usd
   329	│   ├── peach05.usd
   330	│   └── peach06.usd
   331	├── placemat
   332	│   ├── texture
   333	│   │   ├── placemat00.png
   334	│   │   ├── placemat01.png
   335	│   │   ├── placemat02.png
   336	│   │   ├── placemat03.png
   337	│   │   ├── placemat04.png
   338	│   │   └── placemat05.png
   339	│   ├── placemat00.usd
   340	│   ├── placemat01.usd
   341	│   ├── placemat02.usd
   342	│   ├── placemat03.usd
   343	│   ├── placemat04.usd
   344	│   └── placemat05.usd
   345	├── plate
   346	│   ├── texture
   347	│   │   ├── plate00.jpg
   348	│   │   ├── plate02.jpg
   349	│   │   ├── plate04.jpg
   350	│   │   ├── plate05.jpg
   351	│   │   ├── plate06.jpg
   352	│   │   ├── plate07.jpg
   353	│   │   ├── plate08.jpg
   354	│   │   ├── plate10.jpg
   355	│   │   ├── plate12.jpg
   356	│   │   ├── plate14.jpg
   357	│   │   └── plate16.jpg
   358	│   ├── plate00.usd
   359	│   ├── plate01.usd
   360	│   ├── plate02.usd
   361	│   ├── plate03.usd
   362	│   ├── plate04.usd
   363	│   ├── plate05.usd
   364	│   ├── plate06.usd
   365	│   ├── plate07.usd
   366	│   ├── plate08.usd
   367	│   ├── plate09.usd
   368	│   ├── plate10.usd
   369	│   ├── plate12.usd
   370	│   ├── plate13.usd
   371	│   ├── plate14.usd
   372	│   ├── plate15.usd
   373	│   └── plate16.usd
   374	├── potato
   375	│   ├── texture
   376	│   │   ├── potato00.jpg
   377	│   │   ├── potato02.jpg
   378	│   │   ├── potato03.jpg
   379	│   │   ├── potato06.jpg
   380	│   │   ├── potato07.jpg
   381	│   │   ├── potato10.jpg
   382	│   │   ├── potato13.jpg
   383	│   │   ├── potato14.jpg
   384	│   │   ├── potato16.jpg
   385	│   │   ├── potato17.jpg
   386	│   │   └── potato18.jpg
   387	│   ├── potato00.usd
   388	│   ├── potato02.usd
   389	│   ├── potato03.usd
   390	│   ├── potato06.usd
   391	│   ├── potato07.usd
   392	│   ├── potato10.usd
   393	│   ├── potato13.usd
   394	│   ├── potato14.usd
   395	│   ├── potato16.usd
   396	│   ├── potato17.usd
   397	│   └── potato18.usd
   398	├── tangerine
   399	│   ├── texture
   400	│   │   ├── tangerine00.jpg
   401	│   │   ├── tangerine03.jpg
   402	│   │   ├── tangerine04.jpg
   403	│   │   ├── tangerine05.jpg
   404	│   │   └── tangerine06.jpg
   405	│   ├── tangerine00.usd
   406	│   ├── tangerine03.usd
   407	│   ├── tangerine04.usd
   408	│   ├── tangerine05.usd
   409	│   └── tangerine06.usd
   410	├── tomato
   411	│   ├── texture
   412	│   │   ├── tomato01.jpg
   413	│   │   ├── tomato03.jpg
   414	│   │   └── tomato07.jpg
   415	│   ├── tomato01.usd
   416	│   ├── tomato02.usd
   417	│   ├── tomato03.usd
   418	│   └── tomato07.usd
   419	├── tray
   420	│   ├── texture
   421	│   │   ├── tray00.jpg
   422	│   │   ├── tray02.jpg
   423	│   │   ├── tray03.jpg
   424	│   │   ├── tray04.jpg
   425	│   │   ├── tray05.jpg
   426	│   │   ├── tray06.jpg
   427	│   │   ├── tray07.jpg
   428	│   │   ├── tray08.jpg
   429	│   │   ├── tray09.jpg
   430	│   │   ├── tray10.jpg
   431	│   │   ├── tray11.jpg
   432	│   │   └── tray12.jpg
   433	│   ├── tray04.usd
   434	│   ├── tray05.usd
   435	│   ├── tray06.usd
   436	│   ├── tray07.usd
   437	│   ├── tray08.usd
   438	│   ├── tray09.usd
   439	│   ├── tray10.usd
   440	│   ├── tray11.usd
   441	│   └── tray12.usd
   442	├── unseen
   443	│   ├── texture
   444	│   │   ├── apple99.jpg
   445	│   │   ├── bottled_drink99.jpg
   446	│   │   ├── can99.jpg
   447	│   │   ├── cup99.jpg
   448	│   │   └── peach99.jpg
   449	│   ├── apple99.usd
   450	│   ├── can99.usd
   451	│   ├── cup99.usd
   452	│   ├── dbottle99.usd
   453	│   └── peach99.usd
   454	├── citation.tex
   455	└── metadata.json
   456	```
   457	

================================================================================
FILE: ./pyproject.toml
================================================================================
     1	[project]
     2	name = "franka-wrist-camera-isaaclab"
     3	version = "0.1.0"
     4	description = "Isaac Lab Franka Panda tabletop scene with wrist and third-person cameras."
     5	requires-python = ">=3.11,<3.12"
     6	readme = "README.md"
     7	
     8	[tool.ruff]
     9	line-length = 110
    10	target-version = "py311"
    11	
    12	[tool.ruff.lint]
    13	select = ["E", "F", "I", "UP", "B", "SIM", "C4"]
    14	ignore = ["E501"]
    15	
    16	[tool.black]
    17	line-length = 110
    18	target-version = ["py311"]

================================================================================
FILE: ./README.md
================================================================================
     1	# Franka wrist-camera tabletop scene for Isaac Lab
     2	
     3	Clean Isaac Lab scene for a Franka Panda arm on a tabletop inside a warehouse background, with:
     4	
     5	- a wrist-mounted RGB-D camera attached under `Robot/panda_hand/wrist_rgbd_camera`
     6	- a fixed third-person “agent view” RGB-D camera
     7	- a Seattle lab table, simple tabletop props, dome lighting, and a warehouse USD background
     8	- a differential-IK controller that moves the gripper through a 40 cm horizontal circle above the table
     9	- viewport markers showing the desired circular path and current IK target
    10	- an optional wrist-camera pixel/depth probe for checking `(u, v, z)` image coordinates
    11	
    12	The repo targets Isaac Sim 5.1 / Isaac Lab with Python 3.11 and your existing setup:
    13	
    14	```bash
    15	~/IsaacLab
    16	conda env: env_isaaclab
    17	```
    18	
    19	## Run
    20	
    21	```bash
    22	unzip franka_wrist_camera_isaaclab.zip
    23	cd franka_wrist_camera_isaaclab
    24	conda activate env_isaaclab
    25	./scripts/run.sh
    26	```
    27	
    28	Headless smoke run:
    29	
    30	```bash
    31	conda activate env_isaaclab
    32	./scripts/run.sh --headless --max_steps 600
    33	```
    34	
    35	Custom Isaac Lab path:
    36	
    37	```bash
    38	ISAACLAB_ROOT=~/IsaacLab ./scripts/run.sh
    39	```
    40	
    41	## Circle IK test
    42	
    43	The default gripper path is a 40 cm diameter circle in the air above the table:
    44	
    45	```bash
    46	./scripts/run.sh --circle_diameter 0.40 --circle_frequency 0.045
    47	```
    48	
    49	The path center, table height, robot base pose, and default camera geometry are centralized in:
    50	
    51	```text
    52	src/franka_wrist_camera_scene/settings.py
    53	```
    54	
    55	The IK control node is isolated in:
    56	
    57	```text
    58	src/franka_wrist_camera_scene/control.py
    59	```
    60	
    61	## Camera attachment note
    62	
    63	The wrist-camera line is in `src/franka_wrist_camera_scene/scene.py`:
    64	
    65	```python
    66	prim_path="{ENV_REGEX_NS}/Robot/panda_hand/wrist_rgbd_camera"
    67	```
    68	
    69	That means the camera prim is created as a child of the Franka hand link, so it follows the wrist through the USD/physics hierarchy. The local camera pose is then set with `CameraCfg.OffsetCfg`, relative to `panda_hand`.
    70	
    71	## Wrist camera coordinate probe
    72	
    73	To visually verify the image coordinate convention:
    74	
    75	```bash
    76	./scripts/run.sh --probe_u 320 --probe_v 240 --save_probe_every 60
    77	```
    78	
    79	Images are saved under:
    80	
    81	```text
    82	camera_probes/
    83	```
    84	
    85	The convention is:
    86	
    87	```python
    88	z = depth[v, u]
    89	```
    90	
    91	where `u` is the image column, `v` is the image row, and `z` is `distance_to_image_plane` in meters.
    92	
    93	## Files
    94	
    95	```text
    96	franka_wrist_camera_isaaclab/
    97	├── README.md
    98	├── pyproject.toml
    99	├── scripts/
   100	│   ├── run.sh
   101	│   └── run_scene.py
   102	└── src/
   103	    └── franka_wrist_camera_scene/
   104	        ├── __init__.py
   105	        ├── camera_probe.py
   106	        ├── control.py
   107	        ├── scene.py
   108	        ├── settings.py
   109	        └── visualization.py
   110	```
   111	
   112	## Notes
   113	
   114	- The scene uses Isaac Lab’s built-in Franka Panda high-PD config because it is intended for differential IK task-space control.
   115	- The IK target uses the `panda_hand` body and the `panda_joint.*` joints.
   116	- The robot starts from a stable tabletop-ready Franka pose and the controller immediately tracks a downward-facing gripper pose above the table.
   117	- First launch can take time if Isaac Sim has to download or cache warehouse/table assets.

================================================================================
FILE: ./run_collect
================================================================================
     1	#!/usr/bin/env bash
     2	# Helper script to run the Franka wrist camera data collection with pre-configured env variables.
     3	
     4	# Exit immediately if a command exits with a non-zero status
     5	set -euo pipefail
     6	
     7	# Get directory of this script
     8	SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
     9	
    10	# Clean up conda env variables to prevent conflicting python environment paths
    11	unset CONDA_PREFIX
    12	unset CONDA_DEFAULT_ENV
    13	
    14	# Set PYTHONPATH to include all relevant Isaac Lab modules and the project src folder
    15	export PYTHONPATH="/home/utilisateur/IsaacLab/source/isaaclab:/home/utilisateur/IsaacLab/source/isaaclab_assets:/home/utilisateur/IsaacLab/source/isaaclab_contrib:/home/utilisateur/IsaacLab/source/isaaclab_mimic:/home/utilisateur/IsaacLab/source/isaaclab_rl:/home/utilisateur/IsaacLab/source/isaaclab_tasks:${SCRIPT_DIR}/src:${PYTHONPATH:-}"
    16	
    17	# Force Vulkan to use the NVIDIA ICD (prevents interference from integrated graphics GPUs)
    18	export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json
    19	export TERM=xterm
    20	
    21	ISAACLAB_ROOT="${ISAACLAB_ROOT:-$HOME/IsaacLab}"
    22	
    23	exec "$ISAACLAB_ROOT/isaaclab.sh" -p "${SCRIPT_DIR}/scripts/collect.py" "$@"

================================================================================
FILE: ./run_collect.sh
================================================================================
     1	#!/usr/bin/env bash
     2	# Helper script to run the Franka wrist camera data collection with pre-configured env variables.
     3	
     4	# Exit immediately if a command exits with a non-zero status
     5	set -euo pipefail
     6	
     7	# Get directory of this script
     8	SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
     9	
    10	# Clean up conda env variables to prevent conflicting python environment paths
    11	unset CONDA_PREFIX
    12	unset CONDA_DEFAULT_ENV
    13	
    14	# Set PYTHONPATH to include all relevant Isaac Lab modules and the project src folder
    15	export PYTHONPATH="/home/utilisateur/IsaacLab/source/isaaclab:/home/utilisateur/IsaacLab/source/isaaclab_assets:/home/utilisateur/IsaacLab/source/isaaclab_contrib:/home/utilisateur/IsaacLab/source/isaaclab_mimic:/home/utilisateur/IsaacLab/source/isaaclab_rl:/home/utilisateur/IsaacLab/source/isaaclab_tasks:${SCRIPT_DIR}/src:${PYTHONPATH:-}"
    16	
    17	# Force Vulkan to use the NVIDIA ICD (prevents interference from integrated graphics GPUs)
    18	export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json
    19	export TERM=xterm
    20	
    21	ISAACLAB_ROOT="${ISAACLAB_ROOT:-$HOME/IsaacLab}"
    22	
    23	exec "$ISAACLAB_ROOT/isaaclab.sh" -p "${SCRIPT_DIR}/scripts/collect.py" "$@"

================================================================================
FILE: ./run_sim.sh
================================================================================
     1	#!/usr/bin/env bash
     2	# Helper script to run the Franka wrist camera simulation with pre-configured env variables.
     3	
     4	# Exit immediately if a command exits with a non-zero status
     5	set -euo pipefail
     6	
     7	# Get directory of this script
     8	SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
     9	
    10	# Clean up conda env variables to prevent conflicting python environment paths
    11	unset CONDA_PREFIX
    12	unset CONDA_DEFAULT_ENV
    13	
    14	# Set PYTHONPATH to include all relevant Isaac Lab modules and the project src folder
    15	export PYTHONPATH="/home/utilisateur/IsaacLab/source/isaaclab:/home/utilisateur/IsaacLab/source/isaaclab_assets:/home/utilisateur/IsaacLab/source/isaaclab_contrib:/home/utilisateur/IsaacLab/source/isaaclab_mimic:/home/utilisateur/IsaacLab/source/isaaclab_rl:/home/utilisateur/IsaacLab/source/isaaclab_tasks:${SCRIPT_DIR}/src:${PYTHONPATH:-}"
    16	
    17	# Force Vulkan to use the NVIDIA ICD (prevents interference from integrated graphics GPUs)
    18	export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json
    19	export TERM=xterm
    20	
    21	# Execute the simulation run script passing along all arguments
    22	exec "${SCRIPT_DIR}/scripts/run.sh" "$@"

================================================================================
FILE: ./scripts/collect.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Collect deterministic pick-place episodes in the tabletop scene."""
     3	
     4	from __future__ import annotations
     5	
     6	import argparse
     7	from pathlib import Path
     8	import sys
     9	
    10	REPO_SRC = Path(__file__).resolve().parents[1] / "src"
    11	sys.path.insert(0, str(REPO_SRC))
    12	
    13	# Import launcher to apply Isaac Sim 6.0 and pxr compatibility patches before importing isaaclab
    14	from franka_wrist_camera_scene.app import launcher  # noqa: F401
    15	from isaaclab.app import AppLauncher  # noqa: E402
    16	from franka_wrist_camera_scene.utils.paths import load_yaml_config  # noqa: E402
    17	
    18	
    19	def parse_args() -> argparse.Namespace:
    20	    parser = argparse.ArgumentParser(description="Collect deterministic pick-and-place tabletop episodes.")
    21	    parser.add_argument(
    22	        "--collection_config",
    23	        type=str,
    24	        default="collection.yaml",
    25	        help="Collection config file under configs/.",
    26	    )
    27	    # Add app launcher arguments
    28	    AppLauncher.add_app_launcher_args(parser)
    29	    args = parser.parse_args()
    30	    args.enable_cameras = True
    31	    args.kit_args = f"{args.kit_args} --/rtx/hydra/readTransformsFromFabricInRenderDelegate=false".strip()
    32	    return args
    33	
    34	
    35	def preflight_collection_output(collection_cfg: dict) -> None:
    36	    """Preflight check on output paths before launching simulator."""
    37	    output_dir = Path(collection_cfg["output_dir"])
    38	    start_episode_id = int(collection_cfg["start_episode_id"])
    39	    num_episodes = int(collection_cfg["num_episodes"])
    40	
    41	    for episode_id in range(start_episode_id, start_episode_id + num_episodes):
    42	        episode_dir = output_dir / f"{episode_id:06d}"
    43	        if episode_dir.exists():
    44	            raise FileExistsError(f"Episode directory already exists: {episode_dir}")
    45	
    46	    manifest_path = output_dir / "manifest.json"
    47	    if manifest_path.exists():
    48	        raise FileExistsError(f"Collection manifest already exists: {manifest_path}")
    49	
    50	
    51	def main() -> None:
    52	    args_cli = parse_args()
    53	    collection_cfg = load_yaml_config(args_cli.collection_config)
    54	    preflight_collection_output(collection_cfg)
    55	
    56	    app_launcher = AppLauncher(args_cli)
    57	    simulation_app = app_launcher.app
    58	    launcher.patch_physx_schema()
    59	
    60	    from franka_wrist_camera_scene.collection.pick_place import collect_pick_place_dataset
    61	
    62	    collect_pick_place_dataset(
    63	        collection_cfg=collection_cfg,
    64	        device=args_cli.device,
    65	        simulation_app=simulation_app,
    66	    )
    67	
    68	    simulation_app.close()
    69	
    70	
    71	if __name__ == "__main__":
    72	    main()

================================================================================
FILE: ./scripts/debug_scene.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Run the Franka tabletop wrist-camera scene in Isaac Lab."""
     3	
     4	from __future__ import annotations
     5	
     6	import argparse
     7	import sys
     8	from pathlib import Path
     9	
    10	
    11	REPO_SRC = Path(__file__).resolve().parents[1] / "src"
    12	sys.path.insert(0, str(REPO_SRC))
    13	
    14	from franka_wrist_camera_scene.app import launcher  # noqa: F401
    15	from isaaclab.app import AppLauncher  # noqa: E402
    16	
    17	
    18	def parse_args() -> argparse.Namespace:
    19	    parser = argparse.ArgumentParser(description="Franka Panda tabletop scene with wrist and agent cameras.")
    20	    parser.add_argument("--num_envs", type=int, default=1, help="Number of cloned tabletop scenes.")
    21	    parser.add_argument(
    22	        "--max_steps", type=int, default=0, help="Stop after this many simulation steps; 0 runs forever."
    23	    )
    24	    parser.add_argument(
    25	        "--task",
    26	        type=str,
    27	        default="circle",
    28	        choices=["circle", "pick_place"],
    29	        help="Task/policy to run.",
    30	    )
    31	    parser.add_argument(
    32	        "--circle_diameter", type=float, default=0.40, help="Gripper circle diameter in meters."
    33	    )
    34	    parser.add_argument("--circle_frequency", type=float, default=0.045, help="Circle frequency in Hz.")
    35	    parser.add_argument("--probe_u", type=int, default=320, help="Wrist-camera pixel u coordinate.")
    36	    parser.add_argument("--probe_v", type=int, default=240, help="Wrist-camera pixel v coordinate.")
    37	    parser.add_argument(
    38	        "--save_probe_every", type=int, default=0, help="Save wrist-camera overlay every N steps; 0 disables."
    39	    )
    40	    parser.add_argument("--video", action="store_true", help="Record a video from the wrist camera.")
    41	    parser.add_argument(
    42	        "--show_markers", action="store_true", help="Show physical circle debug markers in the scene."
    43	    )
    44	    AppLauncher.add_app_launcher_args(parser)
    45	    args = parser.parse_args()
    46	    args.enable_cameras = True
    47	    args.kit_args = f"{args.kit_args} --/rtx/hydra/readTransformsFromFabricInRenderDelegate=false".strip()
    48	    return args
    49	
    50	
    51	args_cli = parse_args()
    52	app_launcher = AppLauncher(args_cli)
    53	simulation_app = app_launcher.app
    54	
    55	launcher.patch_physx_schema()
    56	
    57	import isaaclab.sim as sim_utils  # noqa: E402
    58	from isaaclab.assets import Articulation  # noqa: E402
    59	from isaaclab.scene import InteractiveScene  # noqa: E402
    60	
    61	from franka_wrist_camera_scene.control.gripper import GripperController
    62	from franka_wrist_camera_scene.control.ik import CartesianIKController
    63	from franka_wrist_camera_scene.control.trajectory import CircleTrajectoryCfg, circle_points_w
    64	from franka_wrist_camera_scene.debug.camera_probe import WristCameraProbe
    65	from franka_wrist_camera_scene.debug.video_recorder import VideoRecorder
    66	from franka_wrist_camera_scene.debug.visualization import CircleMotionMarkers
    67	from franka_wrist_camera_scene.policies.circle_policy import CircleMotionPolicy
    68	from franka_wrist_camera_scene.policies.pick_place_scripted import PickPlaceScriptedPolicy
    69	from franka_wrist_camera_scene.scene.tabletop import TabletopFrankaSceneCfg
    70	from franka_wrist_camera_scene.settings import CIRCLE_CENTER_LOCAL, GRIPPER_DOWN_QUAT_WXYZ, SIM_DT
    71	from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
    72	from franka_wrist_camera_scene.app.camera_warmup import nudge_camera_prims
    73	from franka_wrist_camera_scene.episode.reset import reset_robot_to_default, reset_pick_place_episode
    74	from franka_wrist_camera_scene.episode.success import pick_place_success
    75	
    76	
    77	def run_simulator(
    78	    sim: sim_utils.SimulationContext,
    79	    scene: InteractiveScene,
    80	    policy: CircleMotionPolicy | PickPlaceScriptedPolicy,
    81	    ik: CartesianIKController,
    82	    gripper: GripperController,
    83	    probe: WristCameraProbe,
    84	    max_steps: int,
    85	    video: bool = False,
    86	    show_markers: bool = False,
    87	) -> None:
    88	    """Run the scene until the app closes or the optional step limit is reached."""
    89	    robot: Articulation = scene["robot"]
    90	    sim_dt = sim.get_physics_dt()
    91	    sim_time_s = 0.0
    92	    step = 0
    93	
    94	    video_recorder = VideoRecorder(video, sim_dt)
    95	
    96	    # Debug markers (only applicable for circle task)
    97	    markers = None
    98	    if show_markers and isinstance(policy, CircleMotionPolicy):
    99	        markers = CircleMotionMarkers()
   100	        points_w = circle_points_w(scene, policy.cfg, robot.device)
   101	        markers.draw_path(points_w)
   102	
   103	    settling = False
   104	    settle_steps = 0
   105	    max_settle_steps = int(1.0 / sim_dt)
   106	
   107	    while simulation_app.is_running() and (max_steps <= 0 or step < max_steps):
   108	        # 1. Step the policy to get reference actions
   109	        cmd = policy.step(None, sim_time_s)
   110	
   111	        # 2. Update and apply Cartesian IK command
   112	        ik.set_target_pose(cmd.target_pos_w, cmd.target_quat_w)
   113	        ik.apply(scene, robot)
   114	
   115	        # 3. Update and apply gripper command
   116	        gripper.set_width(cmd.finger_opening_m)
   117	        gripper.apply(robot)
   118	
   119	        scene.write_data_to_sim()
   120	
   121	        sim.step()
   122	        sim_time_s += sim_dt
   123	        step += 1
   124	        scene.update(sim_dt)
   125	        probe.maybe_save(scene, step)
   126	
   127	        if markers is not None:
   128	            markers.draw_target(cmd.target_pos_w)
   129	
   130	        video_recorder.record_step(scene, step)
   131	
   132	        if cmd.done:
   133	            if not settling:
   134	                print(f"[INFO] Scripted policy completed execution. Settling for 1.0s ({max_settle_steps} steps)...", flush=True)
   135	                settling = True
   136	            settle_steps += 1
   137	            if settle_steps >= max_settle_steps:
   138	                if isinstance(policy, PickPlaceScriptedPolicy):
   139	                    success = pick_place_success(scene, policy.spec)
   140	                    print(f"[INFO] Pick-place success: {success.detach().cpu().tolist()}", flush=True)
   141	                break
   142	
   143	    video_recorder.close()
   144	
   145	
   146	def main() -> None:
   147	    sim_cfg = sim_utils.SimulationCfg(
   148	        dt=SIM_DT,
   149	        device=args_cli.device,
   150	        physx=sim_utils.PhysxCfg(
   151	            enable_external_forces_every_iteration=True,
   152	            min_velocity_iteration_count=1,
   153	            min_position_iteration_count=4,
   154	        ),
   155	    )
   156	    sim = sim_utils.SimulationContext(sim_cfg)
   157	    sim.set_camera_view(eye=[2.2, -2.2, 1.9], target=[0.55, 0.0, 1.20])
   158	
   159	    scene = InteractiveScene(TabletopFrankaSceneCfg(num_envs=args_cli.num_envs, env_spacing=2.5))
   160	    robot: Articulation = scene["robot"]
   161	
   162	    # Choose policy based on selected task
   163	    if args_cli.task == "circle":
   164	        trajectory_cfg = CircleTrajectoryCfg(
   165	            center_local=CIRCLE_CENTER_LOCAL,
   166	            diameter_m=args_cli.circle_diameter,
   167	            frequency_hz=args_cli.circle_frequency,
   168	            orientation_wxyz=GRIPPER_DOWN_QUAT_WXYZ,
   169	        )
   170	        policy = CircleMotionPolicy(cfg=trajectory_cfg)
   171	    else:  # pick_place
   172	        spec = PickPlaceTaskSpec()
   173	        policy = PickPlaceScriptedPolicy(spec=spec)
   174	
   175	    ik = CartesianIKController()
   176	    gripper = GripperController()
   177	    probe = WristCameraProbe(args_cli.probe_u, args_cli.probe_v, args_cli.save_probe_every)
   178	
   179	    sim.reset()
   180	    policy.bind(scene, robot)
   181	    ik.bind(scene, robot)
   182	    gripper.bind(scene, robot)
   183	    if args_cli.task == "pick_place":
   184	        reset_pick_place_episode(scene, spec)
   185	    else:
   186	        reset_robot_to_default(scene)
   187	        scene.reset()
   188	    ik.reset()
   189	
   190	    nudge_camera_prims(sim, scene)
   191	    run_simulator(
   192	        sim,
   193	        scene,
   194	        policy,
   195	        ik,
   196	        gripper,
   197	        probe,
   198	        args_cli.max_steps,
   199	        video=args_cli.video,
   200	        show_markers=args_cli.show_markers,
   201	    )
   202	
   203	
   204	if __name__ == "__main__":
   205	    main()
   206	    simulation_app.close()

================================================================================
FILE: ./scripts/export_ila.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Export raw tabletop episodes to an image-language-action dataset."""
     3	
     4	from __future__ import annotations
     5	
     6	import argparse
     7	from pathlib import Path
     8	import sys
     9	
    10	REPO_SRC = Path(__file__).resolve().parents[1] / "src"
    11	sys.path.insert(0, str(REPO_SRC))
    12	
    13	from franka_wrist_camera_scene.export.ila import export_collection_to_ila
    14	
    15	
    16	def parse_args() -> argparse.Namespace:
    17	    parser = argparse.ArgumentParser(description="Export raw tabletop collection to ILA format.")
    18	    parser.add_argument("raw_collection_dir", type=Path)
    19	    parser.add_argument("export_dir", type=Path)
    20	    return parser.parse_args()
    21	
    22	
    23	def main() -> None:
    24	    args = parse_args()
    25	    manifest_path = export_collection_to_ila(
    26	        raw_collection_dir=args.raw_collection_dir,
    27	        export_dir=args.export_dir,
    28	    )
    29	    print(f"[INFO] Saved ILA manifest to: {manifest_path}", flush=True)
    30	
    31	
    32	if __name__ == "__main__":
    33	    main()

================================================================================
FILE: ./scripts/generate_object_catalog.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Generate a USD object catalog from the local objects asset tree."""
     3	
     4	from __future__ import annotations
     5	
     6	import argparse
     7	from pathlib import Path
     8	import sys
     9	
    10	REPO_SRC = Path(__file__).resolve().parents[1] / "src"
    11	sys.path.insert(0, str(REPO_SRC))
    12	
    13	from franka_wrist_camera_scene.objects.catalog_generator import write_generated_object_catalog
    14	from franka_wrist_camera_scene.utils.paths import REPO_ROOT
    15	
    16	
    17	def parse_args() -> argparse.Namespace:
    18	    parser = argparse.ArgumentParser(description="Generate a USD object catalog.")
    19	    parser.add_argument(
    20	        "--asset-root",
    21	        type=Path,
    22	        default=REPO_ROOT / "objects",
    23	        help="Root directory containing object USD asset folders.",
    24	    )
    25	    parser.add_argument(
    26	        "--output",
    27	        type=Path,
    28	        default=REPO_ROOT / "configs" / "object_catalog.generated.yaml",
    29	        help="Generated catalog YAML path.",
    30	    )
    31	    return parser.parse_args()
    32	
    33	
    34	def main() -> None:
    35	    args = parse_args()
    36	    output_path = write_generated_object_catalog(
    37	        asset_root=args.asset_root.resolve(),
    38	        output_path=args.output.resolve(),
    39	    )
    40	    print(f"[INFO] Saved generated object catalog to: {output_path}", flush=True)
    41	
    42	
    43	if __name__ == "__main__":
    44	    main()

================================================================================
FILE: ./scripts/inspect_collection.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Inspect a raw collection directory."""
     3	
     4	from __future__ import annotations
     5	
     6	import argparse
     7	import json
     8	from pathlib import Path
     9	
    10	import numpy as np
    11	
    12	
    13	def parse_args() -> argparse.Namespace:
    14	    parser = argparse.ArgumentParser(description="Inspect a raw tabletop collection.")
    15	    parser.add_argument("collection_dir", type=Path)
    16	    return parser.parse_args()
    17	
    18	
    19	def load_episode_summary(episode_dir: Path) -> dict:
    20	    meta_path = episode_dir / "meta.json"
    21	    traj_path = episode_dir / "trajectory.npz"
    22	
    23	    if not meta_path.exists():
    24	        raise FileNotFoundError(meta_path)
    25	    if not traj_path.exists():
    26	        raise FileNotFoundError(traj_path)
    27	
    28	    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    29	
    30	    with np.load(traj_path) as traj:
    31	        steps = int(traj["timestamps_s"].shape[0])
    32	        camera_frames = int(traj["camera_timestamps_s"].shape[0]) if "camera_timestamps_s" in traj.files else 0
    33	
    34	    return {
    35	        "episode_id": int(meta["episode_id"]),
    36	        "success": bool(meta["success"]),
    37	        "num_steps": int(meta["num_steps"]),
    38	        "trajectory_steps": steps,
    39	        "num_camera_frames": int(meta.get("num_camera_frames", camera_frames)),
    40	        "trajectory_camera_frames": camera_frames,
    41	        "record_depth": bool(meta.get("record_depth", False)),
    42	        "object_pos_local": tuple(meta["object_pos_local"]),
    43	        "place_pos_local": tuple(meta["place_pos_local"]),
    44	        "object_category_id": meta.get("object_category_id"),
    45	        "object_variant_id": meta.get("object_variant_id"),
    46	        "object_label": meta.get("object_label"),
    47	        "object_usd_path": meta.get("object_usd_path"),
    48	        "light_intensity": meta.get("light_intensity"),
    49	        "light_color": tuple(meta["light_color"]) if meta.get("light_color") is not None else None,
    50	    }
    51	
    52	
    53	def main() -> None:
    54	    args = parse_args()
    55	    collection_dir: Path = args.collection_dir
    56	
    57	    manifest_path = collection_dir / "manifest.json"
    58	    if not manifest_path.exists():
    59	        raise FileNotFoundError(manifest_path)
    60	
    61	    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    62	    episode_dirs = [collection_dir / item["episode_dir"] for item in manifest["episodes"]]
    63	
    64	    summaries = [load_episode_summary(path) for path in episode_dirs]
    65	    successes = sum(item["success"] for item in summaries)
    66	
    67	    print(f"collection: {collection_dir}")
    68	    print(f"episodes: {len(summaries)}")
    69	    print(f"success: {successes}/{len(summaries)}")
    70	    print()
    71	    print(
    72	        f"{'episode_id':<10} {'success':<8} {'meta_steps':<10} "
    73	        f"{'traj_steps':<10} {'meta_cam':<9} {'traj_cam':<9} {'depth':<6} {'object_variant':<20} {'light':<24}"
    74	    )
    75	
    76	    for item in summaries:
    77	        episode_id = f"{item['episode_id']:06d}"
    78	        success = str(item["success"]).lower()
    79	        record_depth = str(item["record_depth"]).lower()
    80	        variant_id = item.get("object_variant_id", "none") or "none"
    81	        light_str = "none"
    82	        if item["light_intensity"] is not None and item["light_color"] is not None:
    83	            light_color_str = f"({', '.join(f'{x:.2f}' for x in item['light_color'])})"
    84	            light_str = f"{item['light_intensity']:.1f} {light_color_str}"
    85	        print(
    86	            f"{episode_id:<10} {success:<8} "
    87	            f"{item['num_steps']:<10} {item['trajectory_steps']:<10} "
    88	            f"{item['num_camera_frames']:<9} {item['trajectory_camera_frames']:<9} "
    89	            f"{record_depth:<6} {variant_id:<20} {light_str:<24}"
    90	        )
    91	
    92	    print_pose_variant_summary(summaries)
    93	
    94	
    95	def pose_key(summary: dict) -> tuple:
    96	    return (
    97	        tuple(round(float(x), 4) for x in summary["object_pos_local"]),
    98	        tuple(round(float(x), 4) for x in summary["place_pos_local"]),
    99	    )
   100	
   101	
   102	def print_pose_variant_summary(summaries: list[dict]) -> None:
   103	    grouped: dict[tuple, list[dict]] = {}
   104	
   105	    for item in summaries:
   106	        grouped.setdefault(pose_key(item), []).append(item)
   107	
   108	    print()
   109	    print("success by pose variant:")
   110	    print(f"{'object_pos_local':<26} {'place_pos_local':<26} {'success':<8}")
   111	
   112	    for (object_pos, place_pos), items in sorted(grouped.items()):
   113	        successes = sum(item["success"] for item in items)
   114	        total = len(items)
   115	        print(f"{str(object_pos):<26} {str(place_pos):<26} {successes}/{total:<8}")
   116	
   117	
   118	if __name__ == "__main__":
   119	    main()

================================================================================
FILE: ./scripts/inspect_episode.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Inspect one raw recorded episode."""
     3	
     4	from __future__ import annotations
     5	
     6	import argparse
     7	import json
     8	from pathlib import Path
     9	
    10	import numpy as np
    11	
    12	
    13	def parse_args() -> argparse.Namespace:
    14	    parser = argparse.ArgumentParser(description="Inspect one raw tabletop episode.")
    15	    parser.add_argument("episode_dir", type=Path)
    16	    return parser.parse_args()
    17	
    18	
    19	def main() -> None:
    20	    args = parse_args()
    21	    episode_dir: Path = args.episode_dir
    22	
    23	    meta_path = episode_dir / "meta.json"
    24	    traj_path = episode_dir / "trajectory.npz"
    25	
    26	    if not meta_path.exists():
    27	        raise FileNotFoundError(meta_path)
    28	    if not traj_path.exists():
    29	        raise FileNotFoundError(traj_path)
    30	
    31	    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    32	    traj = np.load(traj_path)
    33	
    34	    print("metadata:")
    35	    for key, value in meta.items():
    36	        print(f"  {key}: {value}")
    37	
    38	    print("\ntrajectory.npz:")
    39	    for key in traj.files:
    40	        array = traj[key]
    41	        print(f"  {key:<28} {str(array.shape):<24} {array.dtype}")
    42	
    43	
    44	if __name__ == "__main__":
    45	    main()

================================================================================
FILE: ./scripts/inspect_ila_dataset.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Inspect an exported image-language-action dataset."""
     3	
     4	from __future__ import annotations
     5	
     6	import argparse
     7	from pathlib import Path
     8	import sys
     9	
    10	REPO_SRC = Path(__file__).resolve().parents[1] / "src"
    11	sys.path.insert(0, str(REPO_SRC))
    12	
    13	from franka_wrist_camera_scene.datasets.ila import ILADataset
    14	
    15	
    16	def parse_args() -> argparse.Namespace:
    17	    parser = argparse.ArgumentParser(description="Inspect an exported ILA dataset.")
    18	    parser.add_argument("dataset_dir", type=Path)
    19	    parser.add_argument("--split", type=str, default=None)
    20	    return parser.parse_args()
    21	
    22	
    23	def main() -> None:
    24	    args = parse_args()
    25	    dataset = ILADataset(args.dataset_dir, split=args.split)
    26	
    27	    print(f"dataset: {args.dataset_dir}")
    28	    print(f"split: {args.split or 'all'}")
    29	    print(f"episodes: {len(dataset.episodes)}")
    30	    print(f"frames: {len(dataset)}")
    31	    print(f"observation_keys: {dataset.observation_keys}")
    32	    print(f"state_keys: {dataset.state_keys}")
    33	    print(f"action_keys: {dataset.action_keys}")
    34	
    35	    sample = dataset[0]
    36	    print()
    37	    print("sample[0]:")
    38	    for key, value in sample.items():
    39	        if hasattr(value, "shape"):
    40	            print(f"  {key:<18} shape={tuple(value.shape)} dtype={value.dtype}")
    41	        else:
    42	            print(f"  {key:<18} {value}")
    43	
    44	
    45	if __name__ == "__main__":
    46	    main()

================================================================================
FILE: ./scripts/inspect_object_catalog.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Inspect the USD object catalog."""
     3	
     4	from __future__ import annotations
     5	
     6	import argparse
     7	from pathlib import Path
     8	import sys
     9	
    10	REPO_SRC = Path(__file__).resolve().parents[1] / "src"
    11	sys.path.insert(0, str(REPO_SRC))
    12	
    13	from franka_wrist_camera_scene.objects.catalog import load_object_catalog
    14	
    15	
    16	def parse_args() -> argparse.Namespace:
    17	    parser = argparse.ArgumentParser(description="Inspect a USD object catalog.")
    18	    parser.add_argument(
    19	        "--config",
    20	        type=str,
    21	        default="object_catalog.yaml",
    22	        help="Catalog config name under configs/.",
    23	    )
    24	    return parser.parse_args()
    25	
    26	
    27	def main() -> None:
    28	    args = parse_args()
    29	    catalog = load_object_catalog(args.config)
    30	
    31	    missing_paths = [
    32	        variant.usd_path
    33	        for category in catalog.categories
    34	        for variant in category.variants
    35	        if not variant.usd_path.exists()
    36	    ]
    37	
    38	    print(f"config: {args.config}")
    39	    print(f"asset_root: {catalog.asset_root}")
    40	    print(f"categories: {len(catalog.categories)}")
    41	    print(f"variants: {len(catalog.variants)}")
    42	    print(f"missing files: {len(missing_paths)}")
    43	    print()
    44	    print(f"{'category':<18} {'label':<12} {'split':<8} {'role':<10} {'affordances':<28} {'variants':<8}")
    45	
    46	    for category in catalog.categories:
    47	        affordances = ",".join(category.affordances)
    48	        print(
    49	            f"{category.id:<18} "
    50	            f"{category.label:<12} "
    51	            f"{category.split:<8} "
    52	            f"{category.role:<10} "
    53	            f"{affordances:<28} "
    54	            f"{len(category.variants):<8}"
    55	        )
    56	
    57	    if missing_paths:
    58	        print()
    59	        print("missing USD files:")
    60	        for path in missing_paths:
    61	            print(f"  {path}")
    62	        raise FileNotFoundError(f"{len(missing_paths)} catalog USD files are missing.")
    63	
    64	
    65	if __name__ == "__main__":
    66	    main()

================================================================================
FILE: ./scripts/inspect_objects.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Inspect registered manipulation objects."""
     3	
     4	from __future__ import annotations
     5	
     6	from pathlib import Path
     7	import sys
     8	
     9	REPO_SRC = Path(__file__).resolve().parents[1] / "src"
    10	sys.path.insert(0, str(REPO_SRC))
    11	
    12	from franka_wrist_camera_scene.objects.registry import load_object_registry
    13	
    14	
    15	def main() -> None:
    16	    objects = load_object_registry()
    17	
    18	    print(f"objects: {len(objects)}")
    19	    print(f"{'id':<22} {'label':<14} {'category':<14} {'kind':<10} {'size'}")
    20	
    21	    for spec in objects.values():
    22	        print(f"{spec.id:<22} {spec.label:<14} {spec.category:<14} {spec.kind:<10} {spec.size}")
    23	
    24	
    25	if __name__ == "__main__":
    26	    main()

================================================================================
FILE: ./scripts/run.sh
================================================================================
     1	#!/usr/bin/env bash
     2	# Main entry point bash script to run simulation, collection, or evaluation commands.
     3	set -euo pipefail
     4	
     5	REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
     6	ISAACLAB_ROOT="${ISAACLAB_ROOT:-$HOME/IsaacLab}"
     7	
     8	export PYTHONPATH="$REPO_ROOT/src:${PYTHONPATH:-}"
     9	exec "$ISAACLAB_ROOT/isaaclab.sh" -p "$REPO_ROOT/scripts/debug_scene.py" "$@"

================================================================================
FILE: ./scripts/visualize_ila_episode.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Visualize one exported image-language-action episode."""
     3	
     4	from __future__ import annotations
     5	
     6	import argparse
     7	import json
     8	from pathlib import Path
     9	
    10	import matplotlib.pyplot as plt
    11	import numpy as np
    12	
    13	
    14	def parse_args() -> argparse.Namespace:
    15	    parser = argparse.ArgumentParser(description="Visualize one exported ILA episode.")
    16	    parser.add_argument("dataset_dir", type=Path)
    17	    parser.add_argument("episode_id", type=str)
    18	    parser.add_argument("--output", type=Path, default=Path("ila_episode_preview.png"))
    19	    parser.add_argument("--num_frames", type=int, default=8)
    20	    return parser.parse_args()
    21	
    22	
    23	def load_episode_entry(dataset_dir: Path, episode_id: str) -> dict:
    24	    manifest = json.loads((dataset_dir / "manifest.json").read_text(encoding="utf-8"))
    25	    normalized_id = int(episode_id)
    26	
    27	    for episode in manifest["episodes"]:
    28	        if int(episode["episode_id"]) == normalized_id:
    29	            return episode
    30	
    31	    raise KeyError(f"Episode {episode_id} not found in {dataset_dir / 'manifest.json'}")
    32	
    33	
    34	def main() -> None:
    35	    args = parse_args()
    36	
    37	    episode_entry = load_episode_entry(args.dataset_dir, args.episode_id)
    38	    episode_path = args.dataset_dir / episode_entry["episode_file"]
    39	
    40	    with np.load(episode_path) as episode:
    41	        agent_rgb = episode["agent_rgb"]
    42	        wrist_rgb = episode["wrist_rgb"]
    43	        delta_pos = episode["action_delta_target_pos_w"]
    44	        gripper = episode["action_finger_opening_m"]
    45	        timestamps = episode["timestamps_s"]
    46	
    47	        frame_count = int(agent_rgb.shape[0])
    48	        frame_indices = np.linspace(0, frame_count - 1, min(args.num_frames, frame_count), dtype=int)
    49	
    50	        action_norm = np.linalg.norm(delta_pos.reshape(frame_count, -1)[:, :3], axis=1)
    51	
    52	        fig = plt.figure(figsize=(2.4 * len(frame_indices), 7.0))
    53	        grid = fig.add_gridspec(4, len(frame_indices))
    54	
    55	        for col, frame_idx in enumerate(frame_indices):
    56	            ax = fig.add_subplot(grid[0, col])
    57	            ax.imshow(agent_rgb[frame_idx])
    58	            ax.set_title(f"t={timestamps[frame_idx]:.2f}s")
    59	            ax.axis("off")
    60	
    61	            ax = fig.add_subplot(grid[1, col])
    62	            ax.imshow(wrist_rgb[frame_idx])
    63	            ax.axis("off")
    64	
    65	        action_ax = fig.add_subplot(grid[2, :])
    66	        action_ax.plot(timestamps, action_norm)
    67	        action_ax.set_ylabel("||delta target pos||")
    68	        action_ax.set_xlabel("time [s]")
    69	
    70	        gripper_ax = fig.add_subplot(grid[3, :])
    71	        gripper_ax.plot(timestamps, gripper)
    72	        gripper_ax.set_ylabel("gripper opening [m]")
    73	        gripper_ax.set_xlabel("time [s]")
    74	
    75	        fig.suptitle(
    76	            f"episode {episode_entry['episode_id']} | "
    77	            f"success={episode_entry['success']} | "
    78	            f"{episode_entry['instruction']}"
    79	        )
    80	        fig.tight_layout()
    81	        fig.savefig(args.output, dpi=140)
    82	        plt.close(fig)
    83	
    84	    print(f"[INFO] Saved episode visualization to: {args.output}", flush=True)
    85	
    86	
    87	if __name__ == "__main__":
    88	    main()

================================================================================
FILE: ./scripts/write_ila_splits.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Write deterministic train/val splits for an exported ILA dataset."""
     3	
     4	from __future__ import annotations
     5	
     6	import argparse
     7	from pathlib import Path
     8	import sys
     9	
    10	REPO_SRC = Path(__file__).resolve().parents[1] / "src"
    11	sys.path.insert(0, str(REPO_SRC))
    12	
    13	from franka_wrist_camera_scene.export.ila_splits import write_deterministic_ila_splits
    14	
    15	
    16	def parse_args() -> argparse.Namespace:
    17	    parser = argparse.ArgumentParser(description="Write deterministic ILA train/val splits.")
    18	    parser.add_argument("dataset_dir", type=Path)
    19	    parser.add_argument("--val_fraction", type=float, default=0.2)
    20	    return parser.parse_args()
    21	
    22	
    23	def main() -> None:
    24	    args = parse_args()
    25	    train_path, val_path = write_deterministic_ila_splits(
    26	        dataset_dir=args.dataset_dir,
    27	        val_fraction=args.val_fraction,
    28	    )
    29	    print(f"[INFO] Saved train split to: {train_path}", flush=True)
    30	    print(f"[INFO] Saved val split to: {val_path}", flush=True)
    31	
    32	
    33	if __name__ == "__main__":
    34	    main()

================================================================================
FILE: ./scripts/write_ila_stats.py
================================================================================
     1	#!/usr/bin/env python3
     2	"""Write normalization statistics for an exported ILA dataset."""
     3	
     4	from __future__ import annotations
     5	
     6	import argparse
     7	from pathlib import Path
     8	import sys
     9	
    10	REPO_SRC = Path(__file__).resolve().parents[1] / "src"
    11	sys.path.insert(0, str(REPO_SRC))
    12	
    13	from franka_wrist_camera_scene.export.ila_stats import write_ila_dataset_stats
    14	
    15	
    16	def parse_args() -> argparse.Namespace:
    17	    parser = argparse.ArgumentParser(description="Write ILA dataset statistics.")
    18	    parser.add_argument("dataset_dir", type=Path)
    19	    return parser.parse_args()
    20	
    21	
    22	def main() -> None:
    23	    args = parse_args()
    24	    stats_path = write_ila_dataset_stats(args.dataset_dir)
    25	    print(f"[INFO] Saved ILA stats to: {stats_path}", flush=True)
    26	
    27	
    28	if __name__ == "__main__":
    29	    main()

================================================================================
FILE: ./sim_output.log
================================================================================

================================================================================
FILE: ./src/franka_wrist_camera_scene/app/camera_warmup.py
================================================================================
     1	"""Camera render-product warmup and RTX transform refresh helpers."""
     2	
     3	from __future__ import annotations
     4	
     5	import isaaclab.sim as sim_utils
     6	from isaaclab.scene import InteractiveScene
     7	
     8	
     9	def nudge_camera_prims(sim: sim_utils.SimulationContext, scene: InteractiveScene) -> None:
    10	    """Dirty camera transforms once to prevent white camera views."""
    11	    from pxr import Gf, UsdGeom
    12	    import omni.usd
    13	
    14	    stage = omni.usd.get_context().get_stage()
    15	    for camera_name in ("wrist_camera", "agent_camera"):
    16	        camera = scene[camera_name]
    17	        for path in camera._view.prim_paths:
    18	            prim = stage.GetPrimAtPath(path)
    19	            xform = UsdGeom.Xformable(prim)
    20	            translate_op = next(
    21	                (op for op in xform.GetOrderedXformOps() if op.GetOpName() == "xformOp:translate"),
    22	                None,
    23	            )
    24	            if translate_op is None:
    25	                translate_op = xform.AddTranslateOp(precision=UsdGeom.XformOp.PrecisionDouble)
    26	
    27	            original = translate_op.Get() or Gf.Vec3d(0.0, 0.0, 0.0)
    28	            translate_op.Set(Gf.Vec3d(original[0] + 1.0e-3, original[1], original[2]))
    29	            sim.render()
    30	            translate_op.Set(original)
    31	
    32	    sim.render()

================================================================================
FILE: ./src/franka_wrist_camera_scene/app/__init__.py
================================================================================
     1	"""Simulation launcher and loop helpers."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/app/launcher.py
================================================================================
     1	"""Isaac Sim and pxr compatibility patches and launcher setup."""
     2	
     3	from __future__ import annotations
     4	
     5	import sys
     6	import types
     7	
     8	# Compatibility layer for Isaac Sim 6.0 (redirects omni.physics.tensors.impl.api -> omni.physics.tensors.api)
     9	class LazyApiModule(types.ModuleType):
    10	    def __getattr__(self, name):
    11	        import omni.physics.tensors.api as api
    12	        return getattr(api, "DeformableBodyView" if name == "SoftBodyView" else name)
    13	
    14	    def __dir__(self):
    15	        import omni.physics.tensors.api as api
    16	        return dir(api)
    17	
    18	# Apply sys.modules patches immediately when this module is imported
    19	if "omni.physics.tensors.impl.api" not in sys.modules:
    20	    sys.modules["omni.physics.tensors.impl.api"] = LazyApiModule("omni.physics.tensors.impl.api")
    21	if "omni.physics.tensors.impl" not in sys.modules:
    22	    sys.modules["omni.physics.tensors.impl"] = types.ModuleType("omni.physics.tensors.impl")
    23	
    24	
    25	def patch_physx_schema() -> None:
    26	    """Apply pxr.PhysxSchema patch for compatibility after SimulationApp is started."""
    27	    from pxr import PhysxSchema
    28	    if not hasattr(PhysxSchema, "PhysxDeformableBodyAPI"):
    29	        PhysxSchema.PhysxDeformableBodyAPI = PhysxSchema.PhysxRigidBodyAPI

================================================================================
FILE: ./src/franka_wrist_camera_scene/collection/__init__.py
================================================================================
     1	"""Data collection pipelines and orchestrations."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/collection/pick_place.py
================================================================================
     1	"""Pick-and-place data collection orchestration pipeline."""
     2	
     3	from __future__ import annotations
     4	
     5	from pathlib import Path
     6	
     7	import isaaclab.sim as sim_utils
     8	from isaaclab.assets import Articulation
     9	from isaaclab.scene import InteractiveScene
    10	
    11	from franka_wrist_camera_scene.control.gripper import GripperController
    12	from franka_wrist_camera_scene.control.ik import CartesianIKController
    13	from franka_wrist_camera_scene.episode.reset import reset_pick_place_episode
    14	from franka_wrist_camera_scene.episode.success import pick_place_success
    15	from franka_wrist_camera_scene.episode.recorder import EpisodeRecorder
    16	from franka_wrist_camera_scene.policies.pick_place_scripted import PickPlaceScriptedPolicy
    17	from franka_wrist_camera_scene.scene.tabletop import TabletopFrankaSceneCfg, make_tabletop_scene_cfg
    18	from franka_wrist_camera_scene.scene.object_context import load_catalog_object_context
    19	from franka_wrist_camera_scene.settings import SIM_DT
    20	from franka_wrist_camera_scene.utils.paths import REPO_ROOT
    21	from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec, make_pick_place_episode_spec
    22	from franka_wrist_camera_scene.app.camera_warmup import nudge_camera_prims
    23	from franka_wrist_camera_scene.episode.manifest import write_collection_manifest
    24	from franka_wrist_camera_scene.tasks.sampling import (
    25	    parse_xy_range,
    26	    sample_pick_place_offsets,
    27	    parse_lighting_options,
    28	)
    29	from franka_wrist_camera_scene.scene.lighting import set_dome_light
    30	
    31	
    32	def run_episode(
    33	    sim: sim_utils.SimulationContext,
    34	    scene: InteractiveScene,
    35	    policy: PickPlaceScriptedPolicy,
    36	    ik: CartesianIKController,
    37	    gripper: GripperController,
    38	    output_dir: Path,
    39	    episode_id: int,
    40	    max_steps: int,
    41	    settle_time_s: float,
    42	    record_cameras: bool,
    43	    record_depth: bool,
    44	    camera_fps: int,
    45	    simulation_app,
    46	    seed: int | None = None,
    47	    object_xy_offset: tuple[float, float] | None = None,
    48	    place_xy_offset: tuple[float, float] | None = None,
    49	    object_category_id: str | None = None,
    50	    object_variant_id: str | None = None,
    51	    object_label: str | None = None,
    52	    object_usd_path: str | None = None,
    53	    light_intensity: float | None = None,
    54	    light_color: tuple[float, float, float] | None = None,
    55	) -> Path:
    56	    """Run one episode, record data, check success, and save."""
    57	    robot: Articulation = scene["robot"]
    58	    sim_dt = sim.get_physics_dt()
    59	    sim_time_s = 0.0
    60	    step = 0
    61	    camera_interval_steps = max(1, round(1.0 / (camera_fps * sim_dt)))
    62	
    63	    # Initialize EpisodeRecorder
    64	    recorder = EpisodeRecorder(
    65	        output_dir=output_dir,
    66	        episode_id=episode_id,
    67	        task_name="pick_place",
    68	        instruction=policy.spec.instruction,
    69	        sim_dt=sim_dt,
    70	        ee_body_id=ik.end_effector_body_id,
    71	        object_name=policy.spec.object_name,
    72	        record_cameras=record_cameras,
    73	        record_depth=record_depth,
    74	        object_pos_local=policy.spec.object_pos_local,
    75	        place_pos_local=policy.spec.place_pos_local,
    76	        seed=seed,
    77	        object_xy_offset=object_xy_offset,
    78	        place_xy_offset=place_xy_offset,
    79	        object_category_id=object_category_id,
    80	        object_variant_id=object_variant_id,
    81	        object_label=object_label,
    82	        object_usd_path=object_usd_path,
    83	        light_intensity=light_intensity,
    84	        light_color=light_color,
    85	    )
    86	    recorder.validate_output_path()
    87	
    88	    settling = False
    89	    settle_steps = 0
    90	    max_settle_steps = int(settle_time_s / sim_dt)
    91	    completed = False
    92	
    93	    while simulation_app.is_running() and step < max_steps:
    94	        # 1. Step the policy to get reference actions
    95	        cmd = policy.step(None, sim_time_s)
    96	
    97	        # 2. Update and apply Cartesian IK command
    98	        ik.set_target_pose(cmd.target_pos_w, cmd.target_quat_w)
    99	        ik.apply(scene, robot)
   100	
   101	        # 3. Update and apply gripper command
   102	        gripper.set_width(cmd.finger_opening_m)
   103	        gripper.apply(robot)
   104	
   105	        scene.write_data_to_sim()
   106	
   107	        # Dataset convention: record state_t and command_t before advancing to state_{t+1}.
   108	        recorder.record_step(scene, cmd, step, sim_time_s)
   109	
   110	        if record_cameras and step % camera_interval_steps == 0:
   111	            recorder.record_cameras_step(scene, step, sim_time_s)
   112	
   113	        sim.step()
   114	        sim_time_s += sim_dt
   115	        step += 1
   116	        scene.update(sim_dt)
   117	
   118	        if cmd.done:
   119	            if not settling:
   120	                print(
   121	                    f"[INFO] Scripted policy completed execution. Settling for {settle_time_s}s ({max_settle_steps} steps)...",
   122	                    flush=True,
   123	                )
   124	                settling = True
   125	            settle_steps += 1
   126	            if settle_steps >= max_settle_steps:
   127	                completed = True
   128	                break
   129	
   130	    if not completed:
   131	        if step >= max_steps:
   132	            raise RuntimeError(f"Episode exceeded max_steps={max_steps} before policy completion.")
   133	        raise RuntimeError("Simulation stopped before episode completion.")
   134	
   135	    # Check success
   136	    success = bool(pick_place_success(scene, policy.spec)[0].item())
   137	    print(f"[INFO] Episode {episode_id} success: {success}", flush=True)
   138	
   139	    # Save episode data
   140	    saved_dir = recorder.save(success)
   141	    print(f"[INFO] Saved episode data to: {saved_dir}", flush=True)
   142	    return saved_dir
   143	
   144	
   145	def collect_pick_place_dataset(
   146	    collection_cfg: dict,
   147	    device: str,
   148	    simulation_app,
   149	) -> None:
   150	    """Run the pick-and-place data collection pipeline."""
   151	    sim_cfg = sim_utils.SimulationCfg(
   152	        dt=SIM_DT,
   153	        device=device,
   154	        physx=sim_utils.PhysxCfg(
   155	            enable_external_forces_every_iteration=True,
   156	            min_velocity_iteration_count=1,
   157	            min_position_iteration_count=4,
   158	        ),
   159	    )
   160	    sim = sim_utils.SimulationContext(sim_cfg)
   161	    sim.set_camera_view(eye=[2.2, -2.2, 1.9], target=[0.55, 0.0, 1.20])
   162	
   163	    target_object_cfg = collection_cfg["target_object"]
   164	    object_context = load_catalog_object_context(
   165	        catalog_config=target_object_cfg["catalog_config"],
   166	        category_id=target_object_cfg["category_id"],
   167	        variant_id=target_object_cfg["variant_id"],
   168	    )
   169	
   170	    durable_usd_path = object_context.usd_path.relative_to(REPO_ROOT).as_posix()
   171	
   172	    scene = InteractiveScene(
   173	        make_tabletop_scene_cfg(
   174	            object_context=object_context,
   175	            num_envs=1,
   176	            env_spacing=2.5,
   177	        )
   178	    )
   179	    robot: Articulation = scene["robot"]
   180	
   181	    spec = PickPlaceTaskSpec()
   182	
   183	    ik = CartesianIKController()
   184	    gripper = GripperController()
   185	
   186	    sim.reset()
   187	    ik.bind(scene, robot)
   188	    gripper.bind(scene, robot)
   189	
   190	    seed = int(collection_cfg["seed"])
   191	    pose_randomization = collection_cfg["pose_randomization"]
   192	    object_xy_range = parse_xy_range(pose_randomization["object_xy_range"])
   193	    place_xy_range = parse_xy_range(pose_randomization["place_xy_range"])
   194	
   195	    lighting_randomization = collection_cfg["lighting_randomization"]
   196	    lighting_options = parse_lighting_options(lighting_randomization)
   197	
   198	    output_dir = Path(collection_cfg["output_dir"])
   199	    start_episode_id = int(collection_cfg["start_episode_id"])
   200	    num_episodes = int(collection_cfg["num_episodes"])
   201	    max_steps = int(collection_cfg["max_steps"])
   202	    settle_time_s = float(collection_cfg["settle_time_s"])
   203	    record_cameras = bool(collection_cfg["record_cameras"])
   204	    record_depth = bool(collection_cfg.get("record_depth", False))
   205	    camera_fps = int(collection_cfg.get("camera_fps", 30))
   206	
   207	    saved_episode_dirs: list[Path] = []
   208	
   209	    for episode_id in range(start_episode_id, start_episode_id + num_episodes):
   210	        print(f"[INFO] Starting episode {episode_id}", flush=True)
   211	        sample = sample_pick_place_offsets(
   212	            seed=seed,
   213	            episode_id=episode_id,
   214	            object_range=object_xy_range,
   215	            place_range=place_xy_range,
   216	            lighting=lighting_options,
   217	        )
   218	        episode_spec = make_pick_place_episode_spec(
   219	            base_spec=spec,
   220	            object_xy_offset=sample.object_xy_offset,
   221	            place_xy_offset=sample.place_xy_offset,
   222	            object_label=object_context.label,
   223	        )
   224	
   225	        policy = PickPlaceScriptedPolicy(spec=episode_spec)
   226	        policy.bind(scene, robot)
   227	
   228	        reset_pick_place_episode(scene, episode_spec)
   229	        # USD catalog objects keep their authored materials.
   230	        set_dome_light(scene, sample.light_intensity, sample.light_color)
   231	        policy.reset()
   232	        ik.reset()
   233	        nudge_camera_prims(sim, scene)
   234	
   235	        saved_dir = run_episode(
   236	            sim=sim,
   237	            scene=scene,
   238	            policy=policy,
   239	            ik=ik,
   240	            gripper=gripper,
   241	            output_dir=output_dir,
   242	            episode_id=episode_id,
   243	            max_steps=max_steps,
   244	            settle_time_s=settle_time_s,
   245	            record_cameras=record_cameras,
   246	            record_depth=record_depth,
   247	            camera_fps=camera_fps,
   248	            simulation_app=simulation_app,
   249	            seed=seed,
   250	            object_xy_offset=sample.object_xy_offset,
   251	            place_xy_offset=sample.place_xy_offset,
   252	            object_category_id=object_context.category_id,
   253	            object_variant_id=object_context.variant_id,
   254	            object_label=object_context.label,
   255	            object_usd_path=durable_usd_path,
   256	            light_intensity=sample.light_intensity,
   257	            light_color=sample.light_color,
   258	        )
   259	        saved_episode_dirs.append(saved_dir)
   260	
   261	    manifest_path = write_collection_manifest(
   262	        output_dir=output_dir,
   263	        task_name="pick_place",
   264	        episode_dirs=saved_episode_dirs,
   265	    )
   266	    print(f"[INFO] Saved collection manifest to: {manifest_path}", flush=True)

================================================================================
FILE: ./src/franka_wrist_camera_scene/control/gripper.py
================================================================================
     1	"""Gripper controller interface for joint position control of fingers."""
     2	
     3	from __future__ import annotations
     4	
     5	import torch
     6	from isaaclab.assets import Articulation
     7	from isaaclab.scene import InteractiveScene
     8	
     9	
    10	class GripperController:
    11	    """Robot gripper controller for setting parallel finger widths."""
    12	
    13	    def __init__(self, finger_joint_expr: str = "panda_finger_joint.*"):
    14	        self.finger_joint_expr = finger_joint_expr
    15	        self._finger_joint_ids = None
    16	        self._target_width = None
    17	
    18	    def bind(self, scene: InteractiveScene, robot: Articulation) -> None:
    19	        """Resolve finger joint indices and initialize target buffer."""
    20	        self._finger_joint_ids, _ = robot.find_joints(self.finger_joint_expr)
    21	        self._target_width = torch.zeros(
    22	            (scene.num_envs, len(self._finger_joint_ids)),
    23	            device=robot.device,
    24	        )
    25	
    26	    def set_width(self, width: float | torch.Tensor) -> None:
    27	        """Set target gripper width."""
    28	        if self._target_width is None:
    29	            raise RuntimeError("GripperController was not bound before set_width().")
    30	        if isinstance(width, (float, int)):
    31	            self._target_width.fill_(width)
    32	        else:
    33	            self._target_width[:] = width
    34	
    35	    def apply(self, robot: Articulation) -> None:
    36	        """Apply finger width targets to the robot simulator."""
    37	        if self._finger_joint_ids is None or self._target_width is None:
    38	            raise RuntimeError("GripperController was not bound before apply().")
    39	        robot.set_joint_position_target(self._target_width, joint_ids=self._finger_joint_ids)

================================================================================
FILE: ./src/franka_wrist_camera_scene/control/ik.py
================================================================================
     1	"""Inverse Kinematics solver using Isaac Lab differential IK."""
     2	
     3	from __future__ import annotations
     4	
     5	import torch
     6	
     7	from isaaclab.assets import Articulation
     8	from isaaclab.controllers import DifferentialIKController, DifferentialIKControllerCfg
     9	from isaaclab.managers import SceneEntityCfg
    10	from isaaclab.scene import InteractiveScene
    11	from isaaclab.utils.math import subtract_frame_transforms
    12	
    13	
    14	class CartesianIKController:
    15	    """Robot arm end-effector IK controller using differential IK."""
    16	
    17	    def __init__(
    18	        self,
    19	        arm_joint_expr: str = "panda_joint.*",
    20	        end_effector_body: str = "panda_hand",
    21	    ):
    22	        self.arm_joint_expr = arm_joint_expr
    23	        self.end_effector_body = end_effector_body
    24	
    25	        self._entity = None
    26	        self._ik = None
    27	        self._ee_jacobian_index = None
    28	        self._target_pos_w = None
    29	        self._target_quat_w = None
    30	
    31	    def bind(self, scene: InteractiveScene, robot: Articulation) -> None:
    32	        """Resolve scene references and initialize differential IK."""
    33	        self._entity = SceneEntityCfg(
    34	            "robot",
    35	            joint_names=[self.arm_joint_expr],
    36	            body_names=[self.end_effector_body],
    37	        )
    38	        self._entity.resolve(scene)
    39	
    40	        self._ee_jacobian_index = self._entity.body_ids[0] - int(robot.is_fixed_base)
    41	
    42	        self._ik = DifferentialIKController(
    43	            DifferentialIKControllerCfg(
    44	                command_type="pose",
    45	                use_relative_mode=False,
    46	                ik_method="dls",
    47	                ik_params={"lambda_val": 0.01},
    48	            ),
    49	            num_envs=scene.num_envs,
    50	            device=robot.device,
    51	        )
    52	
    53	    def reset(self) -> None:
    54	        """Reset the differential IK solver state."""
    55	        self._ik.reset()
    56	        self._target_pos_w = None
    57	        self._target_quat_w = None
    58	
    59	    @property
    60	    def end_effector_body_id(self) -> int:
    61	        if self._entity is None:
    62	            raise RuntimeError("CartesianIKController was not bound.")
    63	        return self._entity.body_ids[0]
    64	
    65	    def set_target_pose(self, target_pos_w: torch.Tensor, target_quat_w: torch.Tensor) -> None:
    66	        """Set the target end-effector pose in world coordinates."""
    67	        self._target_pos_w = target_pos_w
    68	        self._target_quat_w = target_quat_w
    69	
    70	    def apply(self, scene: InteractiveScene, robot: Articulation) -> None:
    71	        """Compute and apply joint command targets for the arm."""
    72	        if self._target_pos_w is None or self._target_quat_w is None:
    73	            raise RuntimeError("CartesianIKController target pose was not set before apply().")
    74	
    75	        # Transform target pose from world to robot base frame
    76	        root_pose_w = robot.data.root_pose_w
    77	        target_pos_b, target_quat_b = subtract_frame_transforms(
    78	            root_pose_w[:, :3],
    79	            root_pose_w[:, 3:7],
    80	            self._target_pos_w,
    81	            self._target_quat_w,
    82	        )
    83	
    84	        self._ik.set_command(torch.cat((target_pos_b, target_quat_b), dim=-1))
    85	
    86	        # Compute joint velocities/positions from Jacobian and current joint states
    87	        jacobian = robot.root_physx_view.get_jacobians()[:, self._ee_jacobian_index, :, self._entity.joint_ids]
    88	        ee_pose_w = robot.data.body_pose_w[:, self._entity.body_ids[0]]
    89	        
    90	        ee_pos_b, ee_quat_b = subtract_frame_transforms(
    91	            root_pose_w[:, :3],
    92	            root_pose_w[:, 3:7],
    93	            ee_pose_w[:, :3],
    94	            ee_pose_w[:, 3:7],
    95	        )
    96	        joint_pos = robot.data.joint_pos[:, self._entity.joint_ids]
    97	        joint_pos_des = self._ik.compute(ee_pos_b, ee_quat_b, jacobian, joint_pos)
    98	
    99	        robot.set_joint_position_target(joint_pos_des, joint_ids=self._entity.joint_ids)

================================================================================
FILE: ./src/franka_wrist_camera_scene/control/__init__.py
================================================================================
     1	"""Robot control interfaces, IK solver, gripper commands, and motion primitives."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/control/motion_primitives.py
================================================================================
     1	"""Basic Cartesian motion primitives for scripted policies."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass
     6	import math
     7	
     8	import torch
     9	
    10	
    11	@dataclass(slots=True)
    12	class TrapezoidalScalarProfile:
    13	    """One-dimensional triangular/trapezoidal motion profile."""
    14	
    15	    distance_m: float
    16	    max_speed_m_s: float
    17	    max_accel_m_s2: float
    18	
    19	    accel_time_s: float = 0.0
    20	    cruise_time_s: float = 0.0
    21	    duration_s: float = 0.0
    22	    peak_speed_m_s: float = 0.0
    23	    accel_distance_m: float = 0.0
    24	    cruise_distance_m: float = 0.0
    25	
    26	    def __post_init__(self) -> None:
    27	        if self.distance_m < 0.0:
    28	            raise ValueError("distance_m must be non-negative.")
    29	        if self.max_speed_m_s <= 0.0:
    30	            raise ValueError("max_speed_m_s must be positive.")
    31	        if self.max_accel_m_s2 <= 0.0:
    32	            raise ValueError("max_accel_m_s2 must be positive.")
    33	
    34	        if self.distance_m == 0.0:
    35	            return
    36	
    37	        time_to_max = self.max_speed_m_s / self.max_accel_m_s2
    38	        accel_distance = 0.5 * self.max_accel_m_s2 * time_to_max * time_to_max
    39	
    40	        if 2.0 * accel_distance >= self.distance_m:
    41	            self.peak_speed_m_s = math.sqrt(self.distance_m * self.max_accel_m_s2)
    42	            self.accel_time_s = self.peak_speed_m_s / self.max_accel_m_s2
    43	            self.cruise_time_s = 0.0
    44	            self.accel_distance_m = 0.5 * self.distance_m
    45	            self.cruise_distance_m = 0.0
    46	            self.duration_s = 2.0 * self.accel_time_s
    47	        else:
    48	            self.peak_speed_m_s = self.max_speed_m_s
    49	            self.accel_time_s = time_to_max
    50	            self.accel_distance_m = accel_distance
    51	            self.cruise_distance_m = self.distance_m - 2.0 * accel_distance
    52	            self.cruise_time_s = self.cruise_distance_m / self.max_speed_m_s
    53	            self.duration_s = 2.0 * self.accel_time_s + self.cruise_time_s
    54	
    55	    def sample(self, elapsed_s: float) -> tuple[float, bool]:
    56	        """Return travelled distance and completion flag."""
    57	        if self.distance_m == 0.0:
    58	            return 0.0, True
    59	
    60	        t = max(0.0, min(elapsed_s, self.duration_s))
    61	
    62	        if t <= self.accel_time_s:
    63	            travelled = 0.5 * self.max_accel_m_s2 * t * t
    64	        elif t <= self.accel_time_s + self.cruise_time_s:
    65	            cruise_t = t - self.accel_time_s
    66	            travelled = self.accel_distance_m + self.peak_speed_m_s * cruise_t
    67	        else:
    68	            decel_t = t - self.accel_time_s - self.cruise_time_s
    69	            travelled = (
    70	                self.accel_distance_m
    71	                + self.cruise_distance_m
    72	                + self.peak_speed_m_s * decel_t
    73	                - 0.5 * self.max_accel_m_s2 * decel_t * decel_t
    74	            )
    75	
    76	        return min(travelled, self.distance_m), elapsed_s >= self.duration_s
    77	
    78	
    79	@dataclass(slots=True)
    80	class LinearPoseMotion:
    81	    """Move along a straight Cartesian segment using a trapezoidal scalar profile."""
    82	
    83	    start_pos_w: torch.Tensor
    84	    goal_pos_w: torch.Tensor
    85	    quat_w: torch.Tensor
    86	    start_time_s: float
    87	    profile: TrapezoidalScalarProfile
    88	
    89	    def __post_init__(self) -> None:
    90	        self.start_pos_w = self.start_pos_w.clone()
    91	        self.goal_pos_w = self.goal_pos_w.clone()
    92	        self.quat_w = self.quat_w.clone()
    93	
    94	    @classmethod
    95	    def from_limits(
    96	        cls,
    97	        start_pos_w: torch.Tensor,
    98	        goal_pos_w: torch.Tensor,
    99	        quat_w: torch.Tensor,
   100	        start_time_s: float,
   101	        max_speed_m_s: float,
   102	        max_accel_m_s2: float,
   103	    ) -> "LinearPoseMotion":
   104	        distance_m = float(torch.linalg.norm(goal_pos_w - start_pos_w, dim=-1).max().item())
   105	        profile = TrapezoidalScalarProfile(
   106	            distance_m=distance_m,
   107	            max_speed_m_s=max_speed_m_s,
   108	            max_accel_m_s2=max_accel_m_s2,
   109	        )
   110	        return cls(
   111	            start_pos_w=start_pos_w,
   112	            goal_pos_w=goal_pos_w,
   113	            quat_w=quat_w,
   114	            start_time_s=start_time_s,
   115	            profile=profile,
   116	        )
   117	
   118	    def sample(self, sim_time_s: float) -> tuple[torch.Tensor, torch.Tensor, bool]:
   119	        """Sample target pose at simulation time."""
   120	        travelled_m, done = self.profile.sample(sim_time_s - self.start_time_s)
   121	
   122	        if self.profile.distance_m == 0.0:
   123	            alpha = 1.0
   124	        else:
   125	            alpha = travelled_m / self.profile.distance_m
   126	
   127	        pos_w = self.start_pos_w + alpha * (self.goal_pos_w - self.start_pos_w)
   128	        return pos_w, self.quat_w, done

================================================================================
FILE: ./src/franka_wrist_camera_scene/control/trajectory.py
================================================================================
     1	"""Trajectory generation utilities for circular and custom target trajectories."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass
     6	import math
     7	import torch
     8	
     9	from isaaclab.scene import InteractiveScene
    10	from isaaclab.utils.math import quat_apply
    11	
    12	from ..settings import CIRCLE_CENTER_LOCAL, CIRCLE_DIAMETER_M, CIRCLE_FREQUENCY_HZ, GRIPPER_DOWN_QUAT_WXYZ
    13	
    14	
    15	@dataclass(frozen=True, slots=True)
    16	class CircleTrajectoryCfg:
    17	    """Circular end-effector path configurations relative to environment origins."""
    18	
    19	    center_local: tuple[float, float, float] = CIRCLE_CENTER_LOCAL
    20	    diameter_m: float = CIRCLE_DIAMETER_M
    21	    frequency_hz: float = CIRCLE_FREQUENCY_HZ
    22	    orientation_wxyz: tuple[float, float, float, float] = GRIPPER_DOWN_QUAT_WXYZ
    23	    tcp_offset_local: tuple[float, float, float] = (0.0, 0.0, 0.10)
    24	    preview_points: int = 96
    25	
    26	    @property
    27	    def radius_m(self) -> float:
    28	        return 0.5 * self.diameter_m
    29	
    30	
    31	def circle_pose_w(
    32	    scene: InteractiveScene,
    33	    sim_time_s: float,
    34	    cfg: CircleTrajectoryCfg,
    35	    device: str | torch.device,
    36	) -> tuple[torch.Tensor, torch.Tensor]:
    37	    """Calculate the target wrist pose in world frame to trace a circle in local frame."""
    38	    phase = 2.0 * math.pi * cfg.frequency_hz * sim_time_s
    39	    center_local = torch.tensor(cfg.center_local, device=device).view(1, 3)
    40	    target_quat_w = torch.tensor(cfg.orientation_wxyz, device=device).view(1, 4)
    41	    tcp_offset_local = torch.tensor(cfg.tcp_offset_local, device=device).view(1, 3)
    42	
    43	    tcp_pos_w = center_local.repeat(scene.num_envs, 1) + scene.env_origins
    44	    tcp_pos_w[:, 0] += cfg.radius_m * math.cos(phase)
    45	    tcp_pos_w[:, 1] += cfg.radius_m * math.sin(phase)
    46	
    47	    quat_w = target_quat_w.repeat(scene.num_envs, 1)
    48	    tcp_offset_w = quat_apply(quat_w, tcp_offset_local.repeat(scene.num_envs, 1))
    49	    hand_pos_w = tcp_pos_w - tcp_offset_w
    50	
    51	    return hand_pos_w, quat_w
    52	
    53	
    54	def circle_points_w(
    55	    scene: InteractiveScene,
    56	    cfg: CircleTrajectoryCfg,
    57	    device: str | torch.device,
    58	) -> torch.Tensor:
    59	    """Generate preview path points in world coordinates for visualization markers."""
    60	    center_local = torch.tensor(cfg.center_local, device=device).view(1, 3)
    61	    angles = torch.linspace(0.0, 2.0 * math.pi, cfg.preview_points + 1, device=device)[:-1]
    62	    
    63	    points = center_local.repeat(cfg.preview_points, 1)
    64	    points[:, 0] += cfg.radius_m * torch.cos(angles)
    65	    points[:, 1] += cfg.radius_m * torch.sin(angles)
    66	
    67	    points_w = points.unsqueeze(0) + scene.env_origins.unsqueeze(1)
    68	    return points_w.reshape(-1, 3)

================================================================================
FILE: ./src/franka_wrist_camera_scene/datasets/ila.py
================================================================================
     1	"""PyTorch dataset for exported image-language-action episodes."""
     2	
     3	from __future__ import annotations
     4	
     5	import json
     6	from pathlib import Path
     7	
     8	import numpy as np
     9	import torch
    10	from torch.utils.data import Dataset
    11	
    12	
    13	class ILADataset(Dataset):
    14	    """Frame-level dataset for exported image-language-action episodes."""
    15	
    16	    def __init__(self, dataset_dir: Path | str, split: str | None = None):
    17	        self.dataset_dir = Path(dataset_dir)
    18	        self.manifest = json.loads((self.dataset_dir / "manifest.json").read_text(encoding="utf-8"))
    19	
    20	        episodes = self.manifest["episodes"]
    21	        if split is not None:
    22	            split_data = json.loads((self.dataset_dir / "splits" / f"{split}.json").read_text(encoding="utf-8"))
    23	            episode_files = set(split_data["episode_files"])
    24	            episodes = [episode for episode in episodes if episode["episode_file"] in episode_files]
    25	
    26	        self.episodes = episodes
    27	        self.observation_keys = tuple(self.manifest["observation_keys"])
    28	        self.action_keys = tuple(self.manifest["action_keys"])
    29	        self.state_keys = tuple(self.manifest["state_keys"])
    30	
    31	        self.index: list[tuple[int, int]] = []
    32	        self._episode_cache: dict[int, dict[str, np.ndarray]] = {}
    33	
    34	        for episode_idx, episode in enumerate(self.episodes):
    35	            episode_path = self.dataset_dir / episode["episode_file"]
    36	            with np.load(episode_path) as data:
    37	                num_frames = int(data["timestamps_s"].shape[0])
    38	
    39	            for frame_idx in range(num_frames):
    40	                self.index.append((episode_idx, frame_idx))
    41	
    42	    def __len__(self) -> int:
    43	        return len(self.index)
    44	
    45	    def _load_episode(self, episode_idx: int) -> dict[str, np.ndarray]:
    46	        if episode_idx not in self._episode_cache:
    47	            episode_path = self.dataset_dir / self.episodes[episode_idx]["episode_file"]
    48	            with np.load(episode_path) as data:
    49	                self._episode_cache[episode_idx] = {key: data[key] for key in data.files}
    50	        return self._episode_cache[episode_idx]
    51	
    52	    @staticmethod
    53	    def _rgb_to_tensor(array: np.ndarray) -> torch.Tensor:
    54	        return torch.from_numpy(array).permute(2, 0, 1).float() / 255.0
    55	
    56	    @staticmethod
    57	    def _vector_to_tensor(array: np.ndarray) -> torch.Tensor:
    58	        return torch.from_numpy(np.asarray(array)).float().reshape(-1)
    59	
    60	    def __getitem__(self, item_idx: int) -> dict:
    61	        episode_idx, frame_idx = self.index[item_idx]
    62	        episode_meta = self.episodes[episode_idx]
    63	        episode = self._load_episode(episode_idx)
    64	
    65	        sample = {
    66	            "instruction": episode_meta["instruction"],
    67	            "episode_id": int(episode_meta["episode_id"]),
    68	            "frame_index": int(frame_idx),
    69	            "timestamp_s": float(episode["timestamps_s"][frame_idx]),
    70	        }
    71	
    72	        for key in self.observation_keys:
    73	            sample[key] = self._rgb_to_tensor(episode[key][frame_idx])
    74	
    75	        action_parts = [self._vector_to_tensor(episode[key][frame_idx]) for key in self.action_keys]
    76	        state_parts = [self._vector_to_tensor(episode[key][frame_idx]) for key in self.state_keys]
    77	
    78	        sample["action"] = torch.cat(action_parts, dim=0)
    79	        sample["state"] = torch.cat(state_parts, dim=0)
    80	
    81	        return sample

================================================================================
FILE: ./src/franka_wrist_camera_scene/datasets/__init__.py
================================================================================
     1	"""Dataset loaders."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/debug/camera_probe.py
================================================================================
     1	"""Optional wrist-camera image coordinate probe."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass, field
     6	from pathlib import Path
     7	
     8	import numpy as np
     9	from isaaclab.scene import InteractiveScene
    10	
    11	
    12	@dataclass(slots=True)
    13	class WristCameraProbe:
    14	    """Save a wrist-camera RGB image with one annotated pixel and its depth value."""
    15	
    16	    u: int = 320
    17	    v: int = 240
    18	    save_every: int = 0
    19	    output_dir: Path = field(default_factory=lambda: Path("camera_probes"))
    20	
    21	    def maybe_save(self, scene: InteractiveScene, step: int) -> None:
    22	        """Save an annotated probe image when the configured period is reached."""
    23	        if self.save_every <= 0 or step % self.save_every != 0:
    24	            return
    25	
    26	        from PIL import Image, ImageDraw
    27	
    28	        self.output_dir.mkdir(parents=True, exist_ok=True)
    29	        camera = scene["wrist_camera"]
    30	        rgb = camera.data.output["rgb"][0].detach().cpu().numpy()[..., :3]
    31	        depth = camera.data.output["distance_to_image_plane"][0, ..., 0].detach().cpu().numpy()
    32	
    33	        height, width = depth.shape
    34	        u = min(max(self.u, 0), width - 1)
    35	        v = min(max(self.v, 0), height - 1)
    36	        z_m = float(depth[v, u])
    37	
    38	        image = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))
    39	        draw = ImageDraw.Draw(image)
    40	        draw.line((u - 12, v, u + 12, v), fill=(255, 0, 0), width=2)
    41	        draw.line((u, v - 12, u, v + 12), fill=(255, 0, 0), width=2)
    42	        draw.text((u + 14, v + 14), f"u={u} v={v} z={z_m:.3f} m", fill=(255, 0, 0))
    43	        image.save(self.output_dir / f"wrist_probe_{step:06d}.png")

================================================================================
FILE: ./src/franka_wrist_camera_scene/debug/__init__.py
================================================================================
     1	"""Debugging tools, standalone visualizers, and camera rendering probes."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/debug/video_recorder.py
================================================================================
     1	"""Optional video recorder for scene cameras."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass, field
     6	import numpy as np
     7	from isaaclab.scene import InteractiveScene
     8	
     9	
    10	@dataclass(slots=True)
    11	class VideoRecorder:
    12	    """Record video outputs from scene cameras."""
    13	
    14	    enabled: bool = False
    15	    sim_dt: float = 1.0 / 120.0
    16	    fps: int = 30
    17	    video_writers: dict = field(default_factory=dict, init=False)
    18	    recorded_frames: int = field(default=0, init=False)
    19	    record_interval: int = field(default=1, init=False)
    20	    max_record_frames: int = field(default=0, init=False)
    21	
    22	    def __post_init__(self) -> None:
    23	        if not self.enabled:
    24	            return
    25	
    26	        self.record_interval = max(1, int((1.0 / self.sim_dt) / self.fps))
    27	        self.max_record_frames = 20 * self.fps
    28	
    29	    def record_step(self, scene: InteractiveScene, step: int) -> None:
    30	        """Record a frame if the step matches the interval and limit is not exceeded."""
    31	        if not self.enabled or self.recorded_frames >= self.max_record_frames:
    32	            return
    33	
    34	        if step % self.record_interval == 0:
    35	            import cv2
    36	
    37	            if not self.video_writers:
    38	                fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    39	                for camera_name in ("wrist_camera", "agent_camera"):
    40	                    rgb = scene[camera_name].data.output["rgb"][0].detach().cpu().numpy()[..., :3]
    41	                    height, width = rgb.shape[:2]
    42	                    self.video_writers[camera_name] = cv2.VideoWriter(
    43	                        f"{camera_name}.mp4", fourcc, self.fps, (width, height)
    44	                    )
    45	                print("[INFO] Recording wrist_camera.mp4 and agent_camera.mp4 until stop or 20 seconds.")
    46	
    47	            for camera_name, writer in self.video_writers.items():
    48	                rgb = scene[camera_name].data.output["rgb"][0].detach().cpu().numpy()[..., :3]
    49	                rgb = np.clip(rgb, 0, 255).astype(np.uint8)
    50	                frame = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    51	                writer.write(frame)
    52	
    53	            self.recorded_frames += 1
    54	            if self.recorded_frames == self.max_record_frames:
    55	                self.close()
    56	                print("[INFO] Saved wrist_camera.mp4 and agent_camera.mp4")
    57	
    58	    def close(self) -> None:
    59	        """Release all video writers."""
    60	        for writer in self.video_writers.values():
    61	            writer.release()
    62	        self.video_writers.clear()

================================================================================
FILE: ./src/franka_wrist_camera_scene/debug/visualization.py
================================================================================
     1	"""Lightweight viewport markers for the circle-drawing motion."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass, field
     6	
     7	import torch
     8	
     9	import isaaclab.sim as sim_utils
    10	from isaaclab.markers import VisualizationMarkers
    11	from isaaclab.markers.visualization_markers import VisualizationMarkersCfg
    12	
    13	
    14	@dataclass(slots=True)
    15	class CircleMotionMarkers:
    16	    """Visualize the commanded circle and the moving IK target."""
    17	
    18	    root_prim_path: str = "/Visuals/franka_circle_motion"
    19	    path_radius_m: float = 0.006
    20	    target_radius_m: float = 0.025
    21	    _path: VisualizationMarkers = field(init=False, repr=False)
    22	    _target: VisualizationMarkers = field(init=False, repr=False)
    23	
    24	    def __post_init__(self) -> None:
    25	        self._path = VisualizationMarkers(
    26	            VisualizationMarkersCfg(
    27	                prim_path=f"{self.root_prim_path}/path",
    28	                markers={
    29	                    "point": sim_utils.SphereCfg(
    30	                        radius=self.path_radius_m,
    31	                        visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(0.0, 0.65, 1.0)),
    32	                    )
    33	                },
    34	            )
    35	        )
    36	        self._target = VisualizationMarkers(
    37	            VisualizationMarkersCfg(
    38	                prim_path=f"{self.root_prim_path}/target",
    39	                markers={
    40	                    "target": sim_utils.SphereCfg(
    41	                        radius=self.target_radius_m,
    42	                        visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(1.0, 0.55, 0.0)),
    43	                    )
    44	                },
    45	            )
    46	        )
    47	
    48	    def draw_path(self, points_w: torch.Tensor) -> None:
    49	        """Draw the desired circle as small point instances in world coordinates."""
    50	        self._path.visualize(translations=points_w)
    51	
    52	    def draw_target(self, position_w: torch.Tensor) -> None:
    53	        """Draw the instantaneous IK target position in world coordinates."""
    54	        self._target.visualize(translations=position_w)

================================================================================
FILE: ./src/franka_wrist_camera_scene/episode/__init__.py
================================================================================
     1	"""Episode recording, schemas, resets, and metrics."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/episode/manifest.py
================================================================================
     1	"""Collection manifest writer."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import asdict, dataclass
     6	import json
     7	from pathlib import Path
     8	
     9	
    10	@dataclass(frozen=True, slots=True)
    11	class EpisodeManifestEntry:
    12	    episode_id: int
    13	    episode_dir: str
    14	    success: bool
    15	    num_steps: int
    16	    num_camera_frames: int
    17	    object_pos_local: tuple[float, float, float] | None
    18	    place_pos_local: tuple[float, float, float] | None
    19	    seed: int | None
    20	    object_xy_offset: tuple[float, float] | None
    21	    place_xy_offset: tuple[float, float] | None
    22	    object_category_id: str | None
    23	    object_variant_id: str | None
    24	    object_label: str | None
    25	    object_usd_path: str | None
    26	    light_intensity: float | None
    27	    light_color: tuple[float, float, float] | None
    28	    trajectory_file: str
    29	    metadata_file: str
    30	
    31	
    32	@dataclass(frozen=True, slots=True)
    33	class CollectionManifest:
    34	    format_version: int
    35	    task_name: str
    36	    num_episodes: int
    37	    successes: int
    38	    failures: int
    39	    episodes: list[EpisodeManifestEntry]
    40	
    41	    def save(self, path: Path) -> None:
    42	        path.write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")
    43	
    44	
    45	def write_collection_manifest(
    46	    output_dir: Path,
    47	    task_name: str,
    48	    episode_dirs: list[Path],
    49	) -> Path:
    50	    entries: list[EpisodeManifestEntry] = []
    51	
    52	    for episode_dir in sorted(episode_dirs):
    53	        meta_path = episode_dir / "meta.json"
    54	        if not meta_path.exists():
    55	            raise FileNotFoundError(meta_path)
    56	
    57	        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    58	        rel_dir = episode_dir.relative_to(output_dir)
    59	
    60	        entries.append(
    61	            EpisodeManifestEntry(
    62	                episode_id=int(meta["episode_id"]),
    63	                episode_dir=rel_dir.as_posix(),
    64	                success=bool(meta["success"]),
    65	                num_steps=int(meta["num_steps"]),
    66	                num_camera_frames=int(meta.get("num_camera_frames", 0)),
    67	                object_pos_local=tuple(meta["object_pos_local"]) if meta.get("object_pos_local") is not None else None,
    68	                place_pos_local=tuple(meta["place_pos_local"]) if meta.get("place_pos_local") is not None else None,
    69	                seed=meta.get("seed"),
    70	                object_xy_offset=tuple(meta["object_xy_offset"]) if meta.get("object_xy_offset") is not None else None,
    71	                place_xy_offset=tuple(meta["place_xy_offset"]) if meta.get("place_xy_offset") is not None else None,
    72	                object_category_id=meta.get("object_category_id"),
    73	                object_variant_id=meta.get("object_variant_id"),
    74	                object_label=meta.get("object_label"),
    75	                object_usd_path=meta.get("object_usd_path"),
    76	                light_intensity=meta.get("light_intensity"),
    77	                light_color=tuple(meta["light_color"]) if meta.get("light_color") is not None else None,
    78	                trajectory_file=(rel_dir / "trajectory.npz").as_posix(),
    79	                metadata_file=(rel_dir / "meta.json").as_posix(),
    80	            )
    81	        )
    82	
    83	    successes = sum(entry.success for entry in entries)
    84	
    85	    manifest = CollectionManifest(
    86	        format_version=1,
    87	        task_name=task_name,
    88	        num_episodes=len(entries),
    89	        successes=successes,
    90	        failures=len(entries) - successes,
    91	        episodes=entries,
    92	    )
    93	
    94	    manifest_path = output_dir / "manifest.json"
    95	    manifest.save(manifest_path)
    96	    return manifest_path

================================================================================
FILE: ./src/franka_wrist_camera_scene/episode/recorder.py
================================================================================
     1	"""Episode recorder for internal raw dataset format."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass, field
     6	from pathlib import Path
     7	
     8	import numpy as np
     9	from isaaclab.scene import InteractiveScene
    10	
    11	from franka_wrist_camera_scene.policies.scripted_base import PolicyCommand
    12	from franka_wrist_camera_scene.episode.schema import EpisodeMetadata
    13	
    14	
    15	@dataclass(slots=True)
    16	class EpisodeRecorder:
    17	    """Record one episode into a simple internal directory format."""
    18	
    19	    output_dir: Path
    20	    episode_id: int
    21	    task_name: str
    22	    instruction: str
    23	    sim_dt: float
    24	    ee_body_id: int
    25	    object_name: str
    26	
    27	    record_cameras: bool = False
    28	    record_depth: bool = False
    29	    object_pos_local: tuple[float, float, float] | None = None
    30	    place_pos_local: tuple[float, float, float] | None = None
    31	    seed: int | None = None
    32	    object_xy_offset: tuple[float, float] | None = None
    33	    place_xy_offset: tuple[float, float] | None = None
    34	    object_category_id: str | None = None
    35	    object_variant_id: str | None = None
    36	    object_label: str | None = None
    37	    object_usd_path: str | None = None
    38	    light_intensity: float | None = None
    39	    light_color: tuple[float, float, float] | None = None
    40	
    41	    joint_pos: list[np.ndarray] = field(default_factory=list)
    42	    joint_vel: list[np.ndarray] = field(default_factory=list)
    43	    ee_pos_w: list[np.ndarray] = field(default_factory=list)
    44	    object_pos_w: list[np.ndarray] = field(default_factory=list)
    45	    action_target_pos_w: list[np.ndarray] = field(default_factory=list)
    46	    action_target_quat_w: list[np.ndarray] = field(default_factory=list)
    47	    action_finger_opening_m: list[float] = field(default_factory=list)
    48	
    49	    timestamps_s: list[float] = field(default_factory=list)
    50	    camera_step_indices: list[int] = field(default_factory=list)
    51	    camera_timestamps_s: list[float] = field(default_factory=list)
    52	    agent_rgb: list[np.ndarray] = field(default_factory=list)
    53	    wrist_rgb: list[np.ndarray] = field(default_factory=list)
    54	    agent_depth: list[np.ndarray] = field(default_factory=list)
    55	    wrist_depth: list[np.ndarray] = field(default_factory=list)
    56	
    57	    @property
    58	    def episode_dir(self) -> Path:
    59	        return self.output_dir / f"{self.episode_id:06d}"
    60	
    61	    def validate_output_path(self) -> None:
    62	        if self.episode_dir.exists():
    63	            raise FileExistsError(f"Episode directory already exists: {self.episode_dir}")
    64	
    65	    def record_step(self, scene: InteractiveScene, cmd: PolicyCommand, step: int, sim_time_s: float) -> None:
    66	        # Dataset convention: record state_t and command_t before advancing to state_{t+1}.
    67	        robot = scene["robot"]
    68	        obj = scene[self.object_name]
    69	
    70	        self.timestamps_s.append(float(sim_time_s))
    71	
    72	        self.joint_pos.append(robot.data.joint_pos.detach().cpu().numpy().copy())
    73	        self.joint_vel.append(robot.data.joint_vel.detach().cpu().numpy().copy())
    74	        self.ee_pos_w.append(robot.data.body_pose_w[:, self.ee_body_id, :3].detach().cpu().numpy().copy())
    75	        self.object_pos_w.append(obj.data.root_pos_w.detach().cpu().numpy().copy())
    76	
    77	        self.action_target_pos_w.append(cmd.target_pos_w.detach().cpu().numpy().copy())
    78	        self.action_target_quat_w.append(cmd.target_quat_w.detach().cpu().numpy().copy())
    79	        self.action_finger_opening_m.append(float(cmd.finger_opening_m))
    80	
    81	    def record_cameras_step(self, scene: InteractiveScene, step: int, sim_time_s: float) -> None:
    82	        """Record camera observations for this control step."""
    83	        if not self.record_cameras:
    84	            return
    85	
    86	        self.camera_step_indices.append(int(step))
    87	        self.camera_timestamps_s.append(float(sim_time_s))
    88	
    89	        for camera_name, buffer in (
    90	            ("agent_camera", self.agent_rgb),
    91	            ("wrist_camera", self.wrist_rgb),
    92	        ):
    93	            rgb = scene[camera_name].data.output["rgb"][0].detach().cpu().numpy()[..., :3]
    94	            buffer.append(np.clip(rgb, 0, 255).astype(np.uint8).copy())
    95	
    96	        if self.record_depth:
    97	            for camera_name, buffer in (
    98	                ("agent_camera", self.agent_depth),
    99	                ("wrist_camera", self.wrist_depth),
   100	            ):
   101	                depth = scene[camera_name].data.output["distance_to_image_plane"][0, ..., 0]
   102	                buffer.append(depth.detach().cpu().numpy().astype(np.float32).copy())
   103	
   104	    def save(self, success: bool) -> Path:
   105	        episode_dir = self.episode_dir
   106	        if episode_dir.exists():
   107	            raise FileExistsError(f"Episode directory already exists: {episode_dir}")
   108	        episode_dir.mkdir(parents=True)
   109	
   110	        arrays = {
   111	            "timestamps_s": np.asarray(self.timestamps_s, dtype=np.float32),
   112	            "joint_pos": np.asarray(self.joint_pos),
   113	            "joint_vel": np.asarray(self.joint_vel),
   114	            "ee_pos_w": np.asarray(self.ee_pos_w),
   115	            "object_pos_w": np.asarray(self.object_pos_w),
   116	            "action_target_pos_w": np.asarray(self.action_target_pos_w),
   117	            "action_target_quat_w": np.asarray(self.action_target_quat_w),
   118	            "action_finger_opening_m": np.asarray(self.action_finger_opening_m),
   119	        }
   120	
   121	        if self.record_cameras:
   122	            arrays.update(
   123	                camera_step_indices=np.asarray(self.camera_step_indices, dtype=np.int64),
   124	                camera_timestamps_s=np.asarray(self.camera_timestamps_s, dtype=np.float32),
   125	                agent_rgb=np.asarray(self.agent_rgb, dtype=np.uint8),
   126	                wrist_rgb=np.asarray(self.wrist_rgb, dtype=np.uint8),
   127	            )
   128	
   129	        if self.record_cameras and self.record_depth:
   130	            arrays.update(
   131	                agent_depth=np.asarray(self.agent_depth, dtype=np.float32),
   132	                wrist_depth=np.asarray(self.wrist_depth, dtype=np.float32),
   133	            )
   134	
   135	        np.savez_compressed(episode_dir / "trajectory.npz", **arrays)
   136	
   137	        meta = EpisodeMetadata(
   138	            episode_id=self.episode_id,
   139	            task_name=self.task_name,
   140	            instruction=self.instruction,
   141	            success=success,
   142	            num_steps=len(self.joint_pos),
   143	            sim_dt=self.sim_dt,
   144	            seed=self.seed,
   145	            record_cameras=self.record_cameras,
   146	            record_depth=self.record_depth,
   147	            num_camera_frames=len(self.camera_step_indices) if self.record_cameras else 0,
   148	            object_pos_local=self.object_pos_local,
   149	            place_pos_local=self.place_pos_local,
   150	            object_xy_offset=self.object_xy_offset,
   151	            place_xy_offset=self.place_xy_offset,
   152	            object_category_id=self.object_category_id,
   153	            object_variant_id=self.object_variant_id,
   154	            object_label=self.object_label,
   155	            object_usd_path=self.object_usd_path,
   156	            light_intensity=self.light_intensity,
   157	            light_color=self.light_color,
   158	        )
   159	        meta.save(episode_dir / "meta.json")
   160	        return episode_dir
   161	
   162	

================================================================================
FILE: ./src/franka_wrist_camera_scene/episode/reset.py
================================================================================
     1	"""Reset logic for Franka tabletop episodes."""
     2	
     3	from __future__ import annotations
     4	
     5	import torch
     6	from isaaclab.assets import Articulation
     7	from isaaclab.scene import InteractiveScene
     8	
     9	from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
    10	
    11	
    12	def reset_robot_to_default(scene: InteractiveScene) -> None:
    13	    """Reset the robot to its default root and joint state."""
    14	    robot: Articulation = scene["robot"]
    15	    root_state = robot.data.default_root_state.clone()
    16	    root_state[:, :3] += scene.env_origins
    17	
    18	    robot.write_root_pose_to_sim(root_state[:, :7])
    19	    robot.write_root_velocity_to_sim(root_state[:, 7:])
    20	    robot.write_joint_state_to_sim(
    21	        robot.data.default_joint_pos.clone(),
    22	        robot.data.default_joint_vel.clone(),
    23	    )
    24	    robot.set_joint_position_target(robot.data.default_joint_pos.clone())
    25	
    26	
    27	def reset_pick_place_objects(scene: InteractiveScene, spec: PickPlaceTaskSpec) -> None:
    28	    """Reset the pick-place object to the task initial pose and zero velocity."""
    29	    obj = scene[spec.object_name]
    30	
    31	    root_state = obj.data.default_root_state.clone()
    32	    pos_local = torch.tensor(spec.object_pos_local, device=root_state.device).view(1, 3)
    33	
    34	    root_state[:, :3] = scene.env_origins + pos_local
    35	    root_state[:, 3:7] = torch.tensor((1.0, 0.0, 0.0, 0.0), device=root_state.device).view(1, 4)
    36	    root_state[:, 7:] = 0.0
    37	
    38	    obj.write_root_pose_to_sim(root_state[:, :7])
    39	    obj.write_root_velocity_to_sim(root_state[:, 7:])
    40	
    41	
    42	def reset_pick_place_episode(scene: InteractiveScene, spec: PickPlaceTaskSpec) -> None:
    43	    """Reset robot and task objects for one deterministic pick-place episode."""
    44	    reset_robot_to_default(scene)
    45	    reset_pick_place_objects(scene, spec)
    46	    scene.reset()

================================================================================
FILE: ./src/franka_wrist_camera_scene/episode/schema.py
================================================================================
     1	"""Dataclass schemas for recorded tabletop episodes."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import asdict, dataclass
     6	import json
     7	from pathlib import Path
     8	
     9	
    10	@dataclass(frozen=True, slots=True)
    11	class EpisodeMetadata:
    12	    """Metadata saved once per recorded episode."""
    13	
    14	    episode_id: int
    15	    task_name: str
    16	    instruction: str
    17	    success: bool
    18	    num_steps: int
    19	    sim_dt: float
    20	    seed: int | None = None
    21	    record_cameras: bool = False
    22	    record_depth: bool = False
    23	    num_camera_frames: int = 0
    24	    object_pos_local: tuple[float, float, float] | None = None
    25	    place_pos_local: tuple[float, float, float] | None = None
    26	    object_xy_offset: tuple[float, float] | None = None
    27	    place_xy_offset: tuple[float, float] | None = None
    28	    object_category_id: str | None = None
    29	    object_variant_id: str | None = None
    30	    object_label: str | None = None
    31	    object_usd_path: str | None = None
    32	    light_intensity: float | None = None
    33	    light_color: tuple[float, float, float] | None = None
    34	
    35	    def save(self, path: Path) -> None:
    36	        path.write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")

================================================================================
FILE: ./src/franka_wrist_camera_scene/episode/success.py
================================================================================
     1	"""Success predicates for tabletop episodes."""
     2	
     3	from __future__ import annotations
     4	
     5	import torch
     6	from isaaclab.scene import InteractiveScene
     7	
     8	from franka_wrist_camera_scene.tasks.pick_place import PickPlaceTaskSpec
     9	
    10	
    11	def pick_place_success(
    12	    scene: InteractiveScene,
    13	    spec: PickPlaceTaskSpec,
    14	    xy_threshold_m: float = 0.08,
    15	    z_threshold_m: float = 0.08,
    16	) -> torch.Tensor:
    17	    """Return per-env success for placing the object near the target area."""
    18	    obj = scene[spec.object_name]
    19	    obj_pos_w = obj.data.root_pos_w
    20	
    21	    target_pos_local = torch.tensor(spec.place_pos_local, device=obj_pos_w.device).view(1, 3)
    22	    target_pos_w = scene.env_origins + target_pos_local
    23	
    24	    xy_error = torch.linalg.norm(obj_pos_w[:, :2] - target_pos_w[:, :2], dim=-1)
    25	    z_error = torch.abs(obj_pos_w[:, 2] - target_pos_w[:, 2])
    26	
    27	    return (xy_error <= xy_threshold_m) & (z_error <= z_threshold_m)

================================================================================
FILE: ./src/franka_wrist_camera_scene/export/ila.py
================================================================================
     1	"""Exporter for image-language-action datasets."""
     2	
     3	from __future__ import annotations
     4	
     5	import json
     6	from pathlib import Path
     7	
     8	import numpy as np
     9	
    10	
    11	def load_json(path: Path) -> dict:
    12	    return json.loads(path.read_text(encoding="utf-8"))
    13	
    14	
    15	def export_episode(
    16	    raw_collection_dir: Path,
    17	    export_dir: Path,
    18	    episode_entry: dict,
    19	) -> dict:
    20	    episode_id = int(episode_entry["episode_id"])
    21	    raw_meta_path = raw_collection_dir / episode_entry["metadata_file"]
    22	    raw_traj_path = raw_collection_dir / episode_entry["trajectory_file"]
    23	
    24	    meta = load_json(raw_meta_path)
    25	
    26	    with np.load(raw_traj_path) as traj:
    27	        idx = traj["camera_step_indices"].astype(np.int64)
    28	        ee_pos_w = traj["ee_pos_w"][idx]
    29	        action_target_pos_w = traj["action_target_pos_w"][idx]
    30	        delta_target_pos_w = action_target_pos_w - ee_pos_w
    31	
    32	        arrays = {
    33	            "agent_rgb": traj["agent_rgb"],
    34	            "wrist_rgb": traj["wrist_rgb"],
    35	            "ee_pos_w": ee_pos_w,
    36	            "object_pos_w": traj["object_pos_w"][idx],
    37	            "action_target_pos_w": action_target_pos_w,
    38	            "action_target_quat_w": traj["action_target_quat_w"][idx],
    39	            "action_delta_target_pos_w": delta_target_pos_w,
    40	            "action_finger_opening_m": traj["action_finger_opening_m"][idx],
    41	            "timestamps_s": traj["camera_timestamps_s"],
    42	            "source_control_step_indices": idx,
    43	        }
    44	
    45	        if "agent_depth" in traj.files and "wrist_depth" in traj.files:
    46	            arrays["agent_depth"] = traj["agent_depth"]
    47	            arrays["wrist_depth"] = traj["wrist_depth"]
    48	
    49	        episode_file = export_dir / "episodes" / f"{episode_id:06d}.npz"
    50	        np.savez_compressed(episode_file, **arrays)
    51	
    52	    return {
    53	        "episode_id": episode_id,
    54	        "episode_file": f"episodes/{episode_id:06d}.npz",
    55	        "source_episode_dir": episode_entry["episode_dir"],
    56	        "instruction": meta["instruction"],
    57	        "success": bool(meta["success"]),
    58	        "num_frames": int(arrays["timestamps_s"].shape[0]),
    59	        "object_pos_local": meta["object_pos_local"],
    60	        "place_pos_local": meta["place_pos_local"],
    61	        "object_category_id": meta.get("object_category_id"),
    62	        "object_variant_id": meta.get("object_variant_id"),
    63	        "object_label": meta.get("object_label"),
    64	        "object_usd_path": meta.get("object_usd_path"),
    65	        "light_intensity": meta.get("light_intensity"),
    66	        "light_color": meta.get("light_color"),
    67	    }
    68	
    69	
    70	def export_collection_to_ila(
    71	    raw_collection_dir: Path,
    72	    export_dir: Path,
    73	) -> Path:
    74	    raw_manifest_path = raw_collection_dir / "manifest.json"
    75	    raw_manifest = load_json(raw_manifest_path)
    76	
    77	    episodes_dir = export_dir / "episodes"
    78	    episodes_dir.mkdir(parents=True, exist_ok=False)
    79	
    80	    exported_episodes = [
    81	        export_episode(raw_collection_dir, export_dir, episode_entry)
    82	        for episode_entry in raw_manifest["episodes"]
    83	    ]
    84	
    85	    manifest = {
    86	        "format_version": 1,
    87	        "dataset_type": "image_language_action",
    88	        "source_collection": str(raw_collection_dir),
    89	        "task_name": raw_manifest["task_name"],
    90	        "num_episodes": len(exported_episodes),
    91	        "camera_names": ["agent_rgb", "wrist_rgb"],
    92	        "action_space": "relative_cartesian_target_plus_gripper",
    93	        "action_keys": [
    94	            "action_delta_target_pos_w",
    95	            "action_target_quat_w",
    96	            "action_finger_opening_m",
    97	        ],
    98	        "state_keys": [
    99	            "ee_pos_w",
   100	            "object_pos_w",
   101	        ],
   102	        "observation_keys": [
   103	            "agent_rgb",
   104	            "wrist_rgb",
   105	        ],
   106	        "episodes": exported_episodes,
   107	    }
   108	
   109	    manifest_path = export_dir / "manifest.json"
   110	    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
   111	    return manifest_path

================================================================================
FILE: ./src/franka_wrist_camera_scene/export/ila_splits.py
================================================================================
     1	"""Deterministic split writer for exported ILA datasets."""
     2	
     3	from __future__ import annotations
     4	
     5	import json
     6	from pathlib import Path
     7	
     8	
     9	def load_json(path: Path) -> dict:
    10	    return json.loads(path.read_text(encoding="utf-8"))
    11	
    12	
    13	def write_split_file(dataset_dir: Path, split_name: str, episodes: list[dict]) -> Path:
    14	    split = {
    15	        "split": split_name,
    16	        "dataset_type": "image_language_action",
    17	        "episode_ids": [int(episode["episode_id"]) for episode in episodes],
    18	        "episode_files": [episode["episode_file"] for episode in episodes],
    19	    }
    20	
    21	    split_dir = dataset_dir / "splits"
    22	    split_dir.mkdir(parents=True, exist_ok=True)
    23	
    24	    split_path = split_dir / f"{split_name}.json"
    25	    split_path.write_text(json.dumps(split, indent=2), encoding="utf-8")
    26	    return split_path
    27	
    28	
    29	def write_deterministic_ila_splits(
    30	    dataset_dir: Path,
    31	    val_fraction: float,
    32	) -> tuple[Path, Path]:
    33	    manifest = load_json(dataset_dir / "manifest.json")
    34	    episodes = sorted(manifest["episodes"], key=lambda item: int(item["episode_id"]))
    35	
    36	    num_episodes = len(episodes)
    37	    num_val = max(1, round(num_episodes * val_fraction))
    38	    num_val = min(num_val, num_episodes - 1)
    39	
    40	    train_episodes = episodes[:-num_val]
    41	    val_episodes = episodes[-num_val:]
    42	
    43	    train_path = write_split_file(dataset_dir, "train", train_episodes)
    44	    val_path = write_split_file(dataset_dir, "val", val_episodes)
    45	
    46	    return train_path, val_path

================================================================================
FILE: ./src/franka_wrist_camera_scene/export/ila_stats.py
================================================================================
     1	"""Statistics writer for exported image-language-action datasets."""
     2	
     3	from __future__ import annotations
     4	
     5	import json
     6	from pathlib import Path
     7	
     8	import numpy as np
     9	
    10	
    11	def load_json(path: Path) -> dict:
    12	    return json.loads(path.read_text(encoding="utf-8"))
    13	
    14	
    15	def flatten_parts(episode: np.lib.npyio.NpzFile, keys: list[str]) -> np.ndarray:
    16	    parts = [np.asarray(episode[key]).reshape(episode[key].shape[0], -1) for key in keys]
    17	    return np.concatenate(parts, axis=1)
    18	
    19	
    20	def vector_stats(values: np.ndarray) -> dict:
    21	    values = values.astype(np.float64, copy=False)
    22	    return {
    23	        "mean": values.mean(axis=0).tolist(),
    24	        "std": values.std(axis=0).tolist(),
    25	        "min": values.min(axis=0).tolist(),
    26	        "max": values.max(axis=0).tolist(),
    27	    }
    28	
    29	
    30	def write_ila_dataset_stats(dataset_dir: Path) -> Path:
    31	    manifest_path = dataset_dir / "manifest.json"
    32	    manifest = load_json(manifest_path)
    33	
    34	    action_keys = list(manifest["action_keys"])
    35	    state_keys = list(manifest["state_keys"])
    36	
    37	    action_batches: list[np.ndarray] = []
    38	    state_batches: list[np.ndarray] = []
    39	
    40	    for episode_entry in manifest["episodes"]:
    41	        episode_path = dataset_dir / episode_entry["episode_file"]
    42	        with np.load(episode_path) as episode:
    43	            action_batches.append(flatten_parts(episode, action_keys))
    44	            state_batches.append(flatten_parts(episode, state_keys))
    45	
    46	    actions = np.concatenate(action_batches, axis=0)
    47	    states = np.concatenate(state_batches, axis=0)
    48	
    49	    stats = {
    50	        "format_version": 1,
    51	        "dataset_type": manifest["dataset_type"],
    52	        "num_frames": int(actions.shape[0]),
    53	        "action_keys": action_keys,
    54	        "state_keys": state_keys,
    55	        "action": vector_stats(actions),
    56	        "state": vector_stats(states),
    57	    }
    58	
    59	    stats_path = dataset_dir / "stats.json"
    60	    stats_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")
    61	    return stats_path

================================================================================
FILE: ./src/franka_wrist_camera_scene/export/__init__.py
================================================================================
     1	"""Dataset exporters."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/__init__.py
================================================================================
     1	"""Franka tabletop Isaac Lab data-collection package."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/objects/catalog_generator.py
================================================================================
     1	"""Generate USD object catalog configs from an asset directory tree."""
     2	
     3	from __future__ import annotations
     4	
     5	from pathlib import Path
     6	
     7	import yaml
     8	
     9	from franka_wrist_camera_scene.utils.paths import REPO_ROOT
    10	
    11	
    12	SUPPORT_CATEGORIES = {"plate", "tray", "placemat"}
    13	IGNORED_DIRECTORY_NAMES = {"texture"}
    14	
    15	
    16	def label_from_variant_stem(stem: str) -> str:
    17	    """Infer a human object label from a USD filename stem."""
    18	    if stem.startswith("dbottle") or stem.startswith("wbottle"):
    19	        return "bottle"
    20	    if stem.startswith("fcan"):
    21	        return "can"
    22	
    23	    label = "".join(char for char in stem if not char.isdigit())
    24	    return label.lower()
    25	
    26	
    27	def category_entry(
    28	    category_id: str,
    29	    label: str,
    30	    split: str,
    31	    variants: list[dict],
    32	) -> dict:
    33	    """Create one catalog category entry."""
    34	    is_support = label in SUPPORT_CATEGORIES
    35	
    36	    return {
    37	        "id": category_id,
    38	        "label": label,
    39	        "split": split,
    40	        "role": "clutter" if is_support else "target",
    41	        "affordances": ["reachable", "support"] if is_support else ["pickable", "reachable"],
    42	        "variants": variants,
    43	    }
    44	
    45	
    46	def collect_category_variants(asset_root: Path, category_dir: Path) -> list[dict]:
    47	    """Collect direct USD variants from one category directory."""
    48	    variants: list[dict] = []
    49	
    50	    for usd_path in sorted(category_dir.glob("*.usd")):
    51	        variants.append(
    52	            {
    53	                "id": usd_path.stem,
    54	                "usd_path": str(usd_path.relative_to(asset_root)),
    55	            }
    56	        )
    57	
    58	    return variants
    59	
    60	
    61	def collect_unseen_categories(asset_root: Path, unseen_dir: Path) -> list[dict]:
    62	    """Collect unseen USD variants, grouped by inferred object label."""
    63	    grouped_variants: dict[str, list[dict]] = {}
    64	
    65	    for usd_path in sorted(unseen_dir.glob("*.usd")):
    66	        label = label_from_variant_stem(usd_path.stem)
    67	        grouped_variants.setdefault(label, []).append(
    68	            {
    69	                "id": usd_path.stem,
    70	                "usd_path": str(usd_path.relative_to(asset_root)),
    71	            }
    72	        )
    73	
    74	    return [
    75	        category_entry(
    76	            category_id=f"unseen_{label}",
    77	            label=label,
    78	            split="unseen",
    79	            variants=variants,
    80	        )
    81	        for label, variants in sorted(grouped_variants.items())
    82	    ]
    83	
    84	def catalog_asset_root_value(asset_root: Path) -> str:
    85	    try:
    86	        return str(asset_root.relative_to(REPO_ROOT))
    87	    except ValueError:
    88	        return str(asset_root)
    89	
    90	
    91	def generate_object_catalog(asset_root: Path) -> dict:
    92	    """Generate an object catalog dictionary from an asset tree."""
    93	    categories: list[dict] = []
    94	
    95	    for category_dir in sorted(path for path in asset_root.iterdir() if path.is_dir()):
    96	        if category_dir.name in IGNORED_DIRECTORY_NAMES:
    97	            continue
    98	
    99	        if category_dir.name == "unseen":
   100	            categories.extend(collect_unseen_categories(asset_root, category_dir))
   101	            continue
   102	
   103	        variants = collect_category_variants(asset_root, category_dir)
   104	        if not variants:
   105	            continue
   106	
   107	        label = category_dir.name
   108	        categories.append(
   109	            category_entry(
   110	                category_id=category_dir.name,
   111	                label=label,
   112	                split="train",
   113	                variants=variants,
   114	            )
   115	        )
   116	
   117	    return {
   118	        "asset_root": catalog_asset_root_value(asset_root),
   119	        "categories": categories,
   120	    }
   121	
   122	
   123	def write_generated_object_catalog(
   124	    asset_root: Path,
   125	    output_path: Path,
   126	) -> Path:
   127	    """Generate and write an object catalog YAML file."""
   128	    catalog = generate_object_catalog(asset_root)
   129	
   130	    output_path.parent.mkdir(parents=True, exist_ok=True)
   131	    output_path.write_text(
   132	        yaml.safe_dump(catalog, sort_keys=False, allow_unicode=True),
   133	        encoding="utf-8",
   134	    )
   135	
   136	    return output_path

================================================================================
FILE: ./src/franka_wrist_camera_scene/objects/catalog.py
================================================================================
     1	"""USD object catalog for tabletop manipulation assets."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass
     6	from pathlib import Path
     7	
     8	from franka_wrist_camera_scene.utils.paths import REPO_ROOT, load_yaml_config
     9	
    10	
    11	@dataclass(frozen=True, slots=True)
    12	class ObjectVariant:
    13	    """One concrete USD asset variant."""
    14	
    15	    id: str
    16	    usd_path: Path
    17	
    18	
    19	@dataclass(frozen=True, slots=True)
    20	class ObjectCategory:
    21	    """Object category containing one or more USD variants."""
    22	
    23	    id: str
    24	    label: str
    25	    split: str
    26	    role: str
    27	    affordances: tuple[str, ...]
    28	    variants: tuple[ObjectVariant, ...]
    29	
    30	
    31	@dataclass(frozen=True, slots=True)
    32	class ObjectCatalog:
    33	    """Loaded USD object catalog."""
    34	
    35	    asset_root: Path
    36	    categories: tuple[ObjectCategory, ...]
    37	
    38	    @property
    39	    def variants(self) -> tuple[ObjectVariant, ...]:
    40	        return tuple(variant for category in self.categories for variant in category.variants)
    41	
    42	
    43	def resolve_asset_root(asset_root_value: str) -> Path:
    44	    asset_root = Path(asset_root_value)
    45	    if asset_root.is_absolute():
    46	        return asset_root
    47	    return REPO_ROOT / asset_root
    48	
    49	
    50	def load_object_catalog(config_name: str = "object_catalog.yaml") -> ObjectCatalog:
    51	    """Load the USD object catalog from configs/."""
    52	    data = load_yaml_config(config_name)
    53	    asset_root = resolve_asset_root(str(data["asset_root"]))
    54	
    55	    categories: list[ObjectCategory] = []
    56	    for item in data["categories"]:
    57	        variants = tuple(
    58	            ObjectVariant(
    59	                id=str(variant["id"]),
    60	                usd_path=asset_root / str(variant["usd_path"]),
    61	            )
    62	            for variant in item["variants"]
    63	        )
    64	
    65	        categories.append(
    66	            ObjectCategory(
    67	                id=str(item["id"]),
    68	                label=str(item["label"]),
    69	                split=str(item["split"]),
    70	                role=str(item["role"]),
    71	                affordances=tuple(str(value) for value in item["affordances"]),
    72	                variants=variants,
    73	            )
    74	        )
    75	
    76	    return ObjectCatalog(
    77	        asset_root=asset_root,
    78	        categories=tuple(categories),
    79	    )

================================================================================
FILE: ./src/franka_wrist_camera_scene/objects/__init__.py
================================================================================
     1	"""Object asset registry and metadata."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/objects/registry.py
================================================================================
     1	"""Object registry for tabletop manipulation assets."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass
     6	
     7	from franka_wrist_camera_scene.utils.paths import load_yaml_config
     8	
     9	
    10	@dataclass(frozen=True, slots=True)
    11	class ObjectColor:
    12	    name: str
    13	    rgb: tuple[float, float, float]
    14	
    15	
    16	@dataclass(frozen=True, slots=True)
    17	class ObjectGraspSpec:
    18	    tcp_offset_local: tuple[float, float, float]
    19	    pregrasp_height_m: float
    20	    lift_height_m: float
    21	
    22	
    23	@dataclass(frozen=True, slots=True)
    24	class ObjectSpec:
    25	    id: str
    26	    label: str
    27	    category: str
    28	    kind: str
    29	    size: tuple[float, float, float]
    30	    default_color: ObjectColor
    31	    grasp: ObjectGraspSpec
    32	    aliases: tuple[str, ...]
    33	
    34	
    35	def load_object_registry(config_name: str = "objects.yaml") -> dict[str, ObjectSpec]:
    36	    data = load_yaml_config(config_name)
    37	    objects: dict[str, ObjectSpec] = {}
    38	
    39	    for item in data["objects"]:
    40	        object_id = str(item["id"])
    41	        color = item["default_color"]
    42	        grasp = item["grasp"]
    43	        language = item["language"]
    44	
    45	        objects[object_id] = ObjectSpec(
    46	            id=object_id,
    47	            label=str(item["label"]),
    48	            category=str(item["category"]),
    49	            kind=str(item["kind"]),
    50	            size=tuple(float(x) for x in item["size"]),
    51	            default_color=ObjectColor(
    52	                name=str(color["name"]),
    53	                rgb=tuple(float(x) for x in color["rgb"]),
    54	            ),
    55	            grasp=ObjectGraspSpec(
    56	                tcp_offset_local=tuple(float(x) for x in grasp["tcp_offset_local"]),
    57	                pregrasp_height_m=float(grasp["pregrasp_height_m"]),
    58	                lift_height_m=float(grasp["lift_height_m"]),
    59	            ),
    60	            aliases=tuple(str(x) for x in language["aliases"]),
    61	        )
    62	
    63	    return objects

================================================================================
FILE: ./src/franka_wrist_camera_scene/objects/selection.py
================================================================================
     1	"""Deterministic object selection helpers."""
     2	
     3	from __future__ import annotations
     4	
     5	from franka_wrist_camera_scene.objects.catalog import ObjectCatalog, ObjectCategory, ObjectVariant
     6	
     7	
     8	def find_variant(
     9	    catalog: ObjectCatalog,
    10	    category_id: str,
    11	    variant_id: str,
    12	) -> tuple[ObjectCategory, ObjectVariant]:
    13	    for category in catalog.categories:
    14	        if category.id != category_id:
    15	            continue
    16	
    17	        for variant in category.variants:
    18	            if variant.id == variant_id:
    19	                return category, variant
    20	
    21	        raise KeyError(f"Variant '{variant_id}' not found in category '{category_id}'.")
    22	
    23	    raise KeyError(f"Category '{category_id}' not found in object catalog.")

================================================================================
FILE: ./src/franka_wrist_camera_scene/policies/circle_policy.py
================================================================================
     1	"""Scripted reaching policies for tracking specified task trajectories."""
     2	
     3	from __future__ import annotations
     4	
     5	import torch
     6	from isaaclab.scene import InteractiveScene
     7	from isaaclab.assets import Articulation
     8	
     9	from ..control.trajectory import CircleTrajectoryCfg, circle_pose_w
    10	from .scripted_base import PolicyCommand
    11	
    12	
    13	class CircleMotionPolicy:
    14	    """Policy that generates target poses to trace a circular end-effector trajectory."""
    15	
    16	    def __init__(self, cfg: CircleTrajectoryCfg, gripper_width: float = 0.035):
    17	        self.cfg = cfg
    18	        self.gripper_width = gripper_width
    19	        self._scene = None
    20	        self._device = None
    21	
    22	    def bind(self, scene: InteractiveScene, robot: Articulation) -> None:
    23	        """Bind simulation scene and get device reference."""
    24	        self._scene = scene
    25	        self._device = robot.device
    26	
    27	    def step(self, obs: dict | None, sim_time_s: float) -> PolicyCommand:
    28	        """Compute the next target end-effector pose and gripper width."""
    29	        if self._scene is None or self._device is None:
    30	            raise RuntimeError("CircleMotionPolicy was not bound before step().")
    31	
    32	        target_pos_w, target_quat_w = circle_pose_w(self._scene, sim_time_s, self.cfg, self._device)
    33	        return PolicyCommand(
    34	            target_pos_w=target_pos_w,
    35	            target_quat_w=target_quat_w,
    36	            finger_opening_m=self.gripper_width,
    37	            done=False,
    38	        )

================================================================================
FILE: ./src/franka_wrist_camera_scene/policies/__init__.py
================================================================================
     1	"""Scripted policy demonstrators for different task scenarios."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/policies/pick_place_scripted.py
================================================================================
     1	"""Scripted pick-and-place policy using a simple finite-state machine."""
     2	
     3	from __future__ import annotations
     4	
     5	import torch
     6	from isaaclab.assets import Articulation
     7	from isaaclab.scene import InteractiveScene
     8	from isaaclab.utils.math import quat_apply
     9	
    10	from ..control.motion_primitives import LinearPoseMotion
    11	from ..tasks.pick_place import PickPlaceTaskSpec
    12	from .scripted_base import PolicyCommand
    13	
    14	
    15	class PickPlaceScriptedPolicy:
    16	    """Scripted finite-state machine policy for deterministic pick-and-place."""
    17	
    18	    def __init__(self, spec: PickPlaceTaskSpec):
    19	        self.spec = spec
    20	        self.state = "move_to_pregrasp"
    21	        self._scene = None
    22	        self._device = None
    23	        self._motion = None
    24	        self._state_start_time = None
    25	        self._ee_body_id = None
    26	
    27	        # Gripper orientation (always pointing down)
    28	        self.quat_wxyz = torch.tensor([0.0, 1.0, 0.0, 0.0])
    29	
    30	    def bind(self, scene: InteractiveScene, robot: Articulation) -> None:
    31	        """Bind simulation scene and get device reference."""
    32	        if scene.num_envs != 1:
    33	            raise RuntimeError("PickPlaceScriptedPolicy currently supports only num_envs=1.")
    34	        self._scene = scene
    35	        self._device = robot.device
    36	        self.quat_wxyz = self.quat_wxyz.to(self._device)
    37	        self._ee_body_id = robot.find_bodies(self.spec.ee_body_name)[0][0]
    38	
    39	    def reset(self) -> None:
    40	        """Reset the policy to the initial state."""
    41	        self.state = "move_to_pregrasp"
    42	        self._motion = None
    43	        self._state_start_time = None
    44	
    45	    def step(self, obs: dict | None, sim_time_s: float) -> PolicyCommand:
    46	        """Compute the next command target according to the FSM state."""
    47	        if self._scene is None or self._device is None or self._ee_body_id is None:
    48	            raise RuntimeError("PickPlaceScriptedPolicy was not bound before step().")
    49	
    50	        robot = self._scene["robot"]
    51	        ee_pos_w = robot.data.body_pose_w[:, self._ee_body_id, :3]  # shape: (num_envs, 3)
    52	        num_envs = self._scene.num_envs
    53	
    54	        # Target definitions (TCP targets)
    55	        # Dynamic object position from the simulated RigidObject (allows randomization)
    56	        obj_pos = self._scene[self.spec.object_name].data.root_pos_w  # shape: (num_envs, 3)
    57	
    58	        place_local = torch.tensor(self.spec.place_pos_local, device=self._device)
    59	        # Convert env-local coordinates to world coordinates using env origins
    60	        place_pos = self._scene.env_origins + place_local.view(1, 3)
    61	
    62	        # Subtract TCP offset (0.10m down in local coordinates) to get the hand position targets
    63	        tcp_offset_local = torch.tensor([0.0, 0.0, 0.10], device=self._device).view(1, 3)
    64	        tcp_offset_w = quat_apply(self.quat_wxyz.view(1, 4), tcp_offset_local).view(3)
    65	
    66	        obj_hand_pos = obj_pos - tcp_offset_w.view(1, 3)
    67	        place_hand_pos = place_pos - tcp_offset_w.view(1, 3)
    68	
    69	        pregrasp_pos = obj_hand_pos.clone()
    70	        pregrasp_pos[:, 2] += self.spec.pregrasp_height_m
    71	
    72	        lift_pos = obj_hand_pos.clone()
    73	        lift_pos[:, 2] += self.spec.lift_height_m
    74	
    75	        place_pre_pos = place_hand_pos.clone()
    76	        place_pre_pos[:, 2] += self.spec.lift_height_m
    77	
    78	        target_pos_w = ee_pos_w.clone()
    79	        target_quat_w = self.quat_wxyz.repeat(num_envs, 1)
    80	        finger_opening = self.spec.open_finger_m
    81	        done = False
    82	
    83	        if self.state == "move_to_pregrasp":
    84	            if self._motion is None:
    85	                self._motion = LinearPoseMotion.from_limits(
    86	                    start_pos_w=ee_pos_w,
    87	                    goal_pos_w=pregrasp_pos,
    88	                    quat_w=target_quat_w,
    89	                    start_time_s=sim_time_s,
    90	                    max_speed_m_s=self.spec.free_space_max_speed_m_s,
    91	                    max_accel_m_s2=self.spec.free_space_max_accel_m_s2,
    92	                )
    93	            pos, quat, finished = self._motion.sample(sim_time_s)
    94	            target_pos_w = pos
    95	            target_quat_w = quat
    96	            if finished:
    97	                self.state = "move_to_grasp"
    98	                self._motion = None
    99	
   100	        elif self.state == "move_to_grasp":
   101	            if self._motion is None:
   102	                self._motion = LinearPoseMotion.from_limits(
   103	                    start_pos_w=ee_pos_w,
   104	                    goal_pos_w=obj_hand_pos,
   105	                    quat_w=target_quat_w,
   106	                    start_time_s=sim_time_s,
   107	                    max_speed_m_s=self.spec.approach_max_speed_m_s,
   108	                    max_accel_m_s2=self.spec.approach_max_accel_m_s2,
   109	                )
   110	            pos, quat, finished = self._motion.sample(sim_time_s)
   111	            target_pos_w = pos
   112	            target_quat_w = quat
   113	            if finished:
   114	                self.state = "close"
   115	                self._state_start_time = sim_time_s
   116	                self._motion = None
   117	
   118	        elif self.state == "close":
   119	            target_pos_w = obj_hand_pos
   120	            finger_opening = self.spec.closed_finger_m
   121	            if sim_time_s - self._state_start_time >= self.spec.grasp_dwell_s:
   122	                self.state = "lift"
   123	                self._state_start_time = None
   124	
   125	        elif self.state == "lift":
   126	            finger_opening = self.spec.closed_finger_m
   127	            if self._motion is None:
   128	                self._motion = LinearPoseMotion.from_limits(
   129	                    start_pos_w=ee_pos_w,
   130	                    goal_pos_w=lift_pos,
   131	                    quat_w=target_quat_w,
   132	                    start_time_s=sim_time_s,
   133	                    max_speed_m_s=self.spec.lift_max_speed_m_s,
   134	                    max_accel_m_s2=self.spec.lift_max_accel_m_s2,
   135	                )
   136	            pos, quat, finished = self._motion.sample(sim_time_s)
   137	            target_pos_w = pos
   138	            target_quat_w = quat
   139	            if finished:
   140	                self.state = "move_to_place"
   141	                self._motion = None
   142	
   143	        elif self.state == "move_to_place":
   144	            finger_opening = self.spec.closed_finger_m
   145	            if self._motion is None:
   146	                self._motion = LinearPoseMotion.from_limits(
   147	                    start_pos_w=ee_pos_w,
   148	                    goal_pos_w=place_pre_pos,
   149	                    quat_w=target_quat_w,
   150	                    start_time_s=sim_time_s,
   151	                    max_speed_m_s=self.spec.free_space_max_speed_m_s,
   152	                    max_accel_m_s2=self.spec.free_space_max_accel_m_s2,
   153	                )
   154	            pos, quat, finished = self._motion.sample(sim_time_s)
   155	            target_pos_w = pos
   156	            target_quat_w = quat
   157	            if finished:
   158	                self.state = "lower"
   159	                self._motion = None
   160	
   161	        elif self.state == "lower":
   162	            finger_opening = self.spec.closed_finger_m
   163	            if self._motion is None:
   164	                self._motion = LinearPoseMotion.from_limits(
   165	                    start_pos_w=ee_pos_w,
   166	                    goal_pos_w=place_hand_pos,
   167	                    quat_w=target_quat_w,
   168	                    start_time_s=sim_time_s,
   169	                    max_speed_m_s=self.spec.approach_max_speed_m_s,
   170	                    max_accel_m_s2=self.spec.approach_max_accel_m_s2,
   171	                )
   172	            pos, quat, finished = self._motion.sample(sim_time_s)
   173	            target_pos_w = pos
   174	            target_quat_w = quat
   175	            if finished:
   176	                self.state = "open"
   177	                self._state_start_time = sim_time_s
   178	                self._motion = None
   179	
   180	        elif self.state == "open":
   181	            target_pos_w = place_hand_pos
   182	            finger_opening = self.spec.open_finger_m
   183	            if sim_time_s - self._state_start_time >= self.spec.release_dwell_s:
   184	                self.state = "retreat"
   185	                self._state_start_time = None
   186	
   187	        elif self.state == "retreat":
   188	            finger_opening = self.spec.open_finger_m
   189	            if self._motion is None:
   190	                self._motion = LinearPoseMotion.from_limits(
   191	                    start_pos_w=ee_pos_w,
   192	                    goal_pos_w=place_pre_pos,
   193	                    quat_w=target_quat_w,
   194	                    start_time_s=sim_time_s,
   195	                    max_speed_m_s=self.spec.retreat_max_speed_m_s,
   196	                    max_accel_m_s2=self.spec.retreat_max_accel_m_s2,
   197	                )
   198	            pos, quat, finished = self._motion.sample(sim_time_s)
   199	            target_pos_w = pos
   200	            target_quat_w = quat
   201	            if finished:
   202	                self.state = "done"
   203	                self._motion = None
   204	
   205	        elif self.state == "done":
   206	            target_pos_w = place_pre_pos
   207	            finger_opening = self.spec.open_finger_m
   208	            done = True
   209	
   210	        return PolicyCommand(
   211	            target_pos_w=target_pos_w,
   212	            target_quat_w=target_quat_w,
   213	            finger_opening_m=finger_opening,
   214	            done=done,
   215	        )

================================================================================
FILE: ./src/franka_wrist_camera_scene/policies/scripted_base.py
================================================================================
     1	"""Base types for scripted demonstrator policies."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass
     6	import torch
     7	
     8	
     9	@dataclass(frozen=True, slots=True)
    10	class PolicyCommand:
    11	    """Single Cartesian command produced by a scripted policy."""
    12	
    13	    target_pos_w: torch.Tensor
    14	    target_quat_w: torch.Tensor
    15	    finger_opening_m: float
    16	    done: bool = False

================================================================================
FILE: ./src/franka_wrist_camera_scene/scene/__init__.py
================================================================================
     1	"""Isaac Lab scene construction, assets, cameras, and tabletop layout."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/scene/lighting.py
================================================================================
     1	"""Scene lighting utilities."""
     2	
     3	from __future__ import annotations
     4	
     5	from pxr import Gf, UsdLux
     6	from isaaclab.scene import InteractiveScene
     7	
     8	
     9	def set_dome_light(scene: InteractiveScene, intensity: float, color_rgb: tuple[float, float, float]) -> None:
    10	    """Set the dome light intensity and color in the USD stage."""
    11	    light_path = "/World/Light"
    12	    light_prim = scene.stage.GetPrimAtPath(light_path)
    13	    if not light_prim.IsValid():
    14	        raise RuntimeError(f"Dome light prim not found: {light_path}")
    15	
    16	    light = UsdLux.DomeLight(light_prim)
    17	    light.GetIntensityAttr().Set(float(intensity))
    18	    light.GetColorAttr().Set(Gf.Vec3f(*color_rgb))

================================================================================
FILE: ./src/franka_wrist_camera_scene/scene/object_context.py
================================================================================
     1	"""Selected catalog object context for scene construction."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass
     6	from pathlib import Path
     7	
     8	from franka_wrist_camera_scene.objects.catalog import load_object_catalog
     9	from franka_wrist_camera_scene.objects.selection import find_variant
    10	
    11	
    12	@dataclass(frozen=True, slots=True)
    13	class CatalogObjectContext:
    14	    category_id: str
    15	    variant_id: str
    16	    label: str
    17	    usd_path: Path
    18	
    19	
    20	def load_catalog_object_context(
    21	    catalog_config: str,
    22	    category_id: str,
    23	    variant_id: str,
    24	) -> CatalogObjectContext:
    25	    catalog = load_object_catalog(catalog_config)
    26	    category, variant = find_variant(catalog, category_id=category_id, variant_id=variant_id)
    27	
    28	    return CatalogObjectContext(
    29	        category_id=category.id,
    30	        variant_id=variant.id,
    31	        label=category.label,
    32	        usd_path=variant.usd_path,
    33	    )

================================================================================
FILE: ./src/franka_wrist_camera_scene/scene/tabletop.py
================================================================================
     1	"""Isaac Lab scene configuration for a Franka tabletop setup with cameras."""
     2	
     3	from __future__ import annotations
     4	
     5	import isaaclab.sim as sim_utils
     6	from isaaclab.assets import ArticulationCfg, AssetBaseCfg, RigidObjectCfg
     7	from isaaclab.scene import InteractiveSceneCfg
     8	from isaaclab.sensors import CameraCfg
     9	from isaaclab.utils import configclass
    10	from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR
    11	from isaaclab_assets import FRANKA_PANDA_HIGH_PD_CFG
    12	
    13	from ..settings import ROBOT_BASE_POS, TABLE_HEIGHT_M, TABLE_SIZE
    14	from franka_wrist_camera_scene.scene.object_context import CatalogObjectContext
    15	
    16	WAREHOUSE_USD = f"{ISAAC_NUCLEUS_DIR}/Environments/Simple_Warehouse/warehouse_multiple_shelves.usd"
    17	
    18	
    19	def pinhole_camera_cfg(clipping_range: tuple[float, float]) -> sim_utils.PinholeCameraCfg:
    20	    """Return a compact RGB-D pinhole camera model."""
    21	    return sim_utils.PinholeCameraCfg(
    22	        focal_length=18.0,
    23	        focus_distance=0.55,
    24	        horizontal_aperture=20.955,
    25	        clipping_range=clipping_range,
    26	    )
    27	
    28	
    29	@configclass
    30	class TabletopFrankaSceneCfg(InteractiveSceneCfg):
    31	    """Warehouse tabletop scene with a Franka Panda and two camera sensors."""
    32	
    33	    warehouse = AssetBaseCfg(
    34	        prim_path="/World/Warehouse",
    35	        spawn=sim_utils.UsdFileCfg(usd_path=WAREHOUSE_USD),
    36	        init_state=AssetBaseCfg.InitialStateCfg(pos=(-4.0, -2.0, 0.0)),
    37	    )
    38	
    39	    table = AssetBaseCfg(
    40	        prim_path="{ENV_REGEX_NS}/Table",
    41	        spawn=sim_utils.CuboidCfg(
    42	            size=TABLE_SIZE,
    43	            collision_props=sim_utils.CollisionPropertiesCfg(),
    44	            visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(0.55, 0.42, 0.30)),
    45	        ),
    46	        # Cuboid origin is at its center; keep TABLE_HEIGHT_M as the tabletop z.
    47	        init_state=AssetBaseCfg.InitialStateCfg(pos=(0.45, 0.0, TABLE_HEIGHT_M - 0.5 * TABLE_SIZE[2])),
    48	    )
    49	
    50	    dome_light = AssetBaseCfg(
    51	        prim_path="/World/Light",
    52	        spawn=sim_utils.DomeLightCfg(intensity=900.0, color=(0.9, 0.9, 0.9)),
    53	    )
    54	
    55	    robot: ArticulationCfg = FRANKA_PANDA_HIGH_PD_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
    56	    robot.spawn.fix_base = True
    57	    robot.init_state.pos = ROBOT_BASE_POS
    58	
    59	    target_cube = RigidObjectCfg(
    60	        prim_path="{ENV_REGEX_NS}/TargetCube",
    61	        spawn=sim_utils.UsdFileCfg(
    62	            usd_path="",
    63	            rigid_props=sim_utils.RigidBodyPropertiesCfg(),
    64	            collision_props=sim_utils.CollisionPropertiesCfg(),
    65	        ),
    66	        init_state=RigidObjectCfg.InitialStateCfg(pos=(0.58, -0.16, TABLE_HEIGHT_M + 0.05)),
    67	    )
    68	
    69	    place_target = AssetBaseCfg(
    70	        prim_path="{ENV_REGEX_NS}/PlaceTarget",
    71	        spawn=sim_utils.CuboidCfg(
    72	            size=(0.14, 0.14, 0.004),
    73	            visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(0.10, 0.65, 0.20)),
    74	        ),
    75	        init_state=AssetBaseCfg.InitialStateCfg(pos=(0.55, 0.22, TABLE_HEIGHT_M + 0.002)),
    76	    )
    77	
    78	    wrist_camera = CameraCfg(
    79	        prim_path="{ENV_REGEX_NS}/Robot/panda_hand/wrist_rgbd_camera",
    80	        update_period=0.0,
    81	        height=128,
    82	        width=128,
    83	        data_types=["rgb", "distance_to_image_plane"],
    84	        update_latest_camera_pose=True,
    85	        spawn=pinhole_camera_cfg(clipping_range=(0.02, 4.0)),
    86	        offset=CameraCfg.OffsetCfg(
    87	            pos=(-0.042, 0.0, 0.020),
    88	            rot=(0.7054, -0.0493, 0.0493, -0.7054),
    89	            convention="ros",
    90	        ),
    91	    )
    92	
    93	    agent_camera = CameraCfg(
    94	        prim_path="{ENV_REGEX_NS}/AgentViewCamera",
    95	        update_period=1.0 / 30.0,
    96	        height=128,
    97	        width=128,
    98	        data_types=["rgb", "distance_to_image_plane"],
    99	        spawn=pinhole_camera_cfg(clipping_range=(0.05, 25.0)),
   100	        offset=CameraCfg.OffsetCfg(
   101	            pos=(1.4186131747, 0.0, 1.7603500240),
   102	            rot=(0.0, -0.33316794, 0.0, 0.94286750),
   103	            convention="world",
   104	        ),
   105	    )
   106	
   107	
   108	def make_tabletop_scene_cfg(
   109	    object_context: CatalogObjectContext,
   110	    num_envs: int = 1,
   111	    env_spacing: float = 2.5,
   112	) -> TabletopFrankaSceneCfg:
   113	    """Create a tabletop scene configuration with the specified target object."""
   114	    scene_cfg = TabletopFrankaSceneCfg(num_envs=num_envs, env_spacing=env_spacing)
   115	    scene_cfg.target_cube.spawn.usd_path = str(object_context.usd_path)
   116	    return scene_cfg

================================================================================
FILE: ./src/franka_wrist_camera_scene/settings.py
================================================================================
     1	"""Shared settings loading constants from configs/scene.yaml to prevent drift."""
     2	
     3	from __future__ import annotations
     4	
     5	from .utils.paths import load_yaml_config
     6	
     7	# Load config from the single source of truth configs/scene.yaml
     8	_cfg = load_yaml_config("scene.yaml")
     9	
    10	SIM_DT = float(_cfg["sim"]["dt"])
    11	TABLE_HEIGHT_M = _cfg["table"]["height_m"]
    12	TABLE_SIZE = tuple(_cfg["table"]["size"])
    13	ROBOT_BASE_POS = tuple(_cfg["robot"]["base_pos"])
    14	
    15	# Local to each Isaac Lab environment origin.
    16	CIRCLE_CENTER_LOCAL = tuple(_cfg["debug_circle"]["center_local"])
    17	CIRCLE_DIAMETER_M = _cfg["debug_circle"]["diameter_m"]
    18	CIRCLE_FREQUENCY_HZ = _cfg["debug_circle"]["frequency_hz"]
    19	
    20	# WXYZ quaternion used by Isaac Lab to orient the gripper toward the table.
    21	GRIPPER_DOWN_QUAT_WXYZ = tuple(_cfg["debug_circle"]["orientation_wxyz"])

================================================================================
FILE: ./src/franka_wrist_camera_scene/tasks/base.py
================================================================================
     1	"""Base definitions for Franka tabletop tasks."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass
     6	
     7	
     8	@dataclass(frozen=True, slots=True)
     9	class TaskSpec:
    10	    """Base task specification containing the language instruction."""
    11	
    12	    instruction: str

================================================================================
FILE: ./src/franka_wrist_camera_scene/tasks/__init__.py
================================================================================
     1	"""Task specifications, reset conditions, and success criteria."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/tasks/pick_place.py
================================================================================
     1	"""Pick-and-place task definitions."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass
     6	from .base import TaskSpec
     7	
     8	
     9	@dataclass(frozen=True, slots=True)
    10	class PickPlaceTaskSpec(TaskSpec):
    11	    """Static single-object pick-and-place task."""
    12	
    13	    object_name: str = "target_cube"
    14	    ee_body_name: str = "panda_hand"
    15	    instruction: str = "pick up the red cube and place it on the target area"
    16	
    17	    object_pos_local: tuple[float, float, float] = (0.58, -0.16, 1.08)
    18	    place_pos_local: tuple[float, float, float] = (0.55, 0.22, 1.08)
    19	
    20	    pregrasp_height_m: float = 0.16
    21	    lift_height_m: float = 0.20
    22	    open_finger_m: float = 0.04
    23	    closed_finger_m: float = 0.0
    24	
    25	    free_space_max_speed_m_s: float = 0.22
    26	    free_space_max_accel_m_s2: float = 0.45
    27	
    28	    approach_max_speed_m_s: float = 0.08
    29	    approach_max_accel_m_s2: float = 0.20
    30	
    31	    lift_max_speed_m_s: float = 0.12
    32	    lift_max_accel_m_s2: float = 0.25
    33	
    34	    retreat_max_speed_m_s: float = 0.15
    35	    retreat_max_accel_m_s2: float = 0.30
    36	
    37	    grasp_dwell_s: float = 1.0
    38	    release_dwell_s: float = 1.0
    39	
    40	
    41	def instruction_for_object(object_label: str) -> str:
    42	    return f"pick up the {object_label} and place it on the target area"
    43	
    44	
    45	def make_pick_place_episode_spec(
    46	    base_spec: PickPlaceTaskSpec,
    47	    object_xy_offset: tuple[float, float],
    48	    place_xy_offset: tuple[float, float],
    49	    object_label: str,
    50	) -> PickPlaceTaskSpec:
    51	    object_pos = (
    52	        base_spec.object_pos_local[0] + object_xy_offset[0],
    53	        base_spec.object_pos_local[1] + object_xy_offset[1],
    54	        base_spec.object_pos_local[2],
    55	    )
    56	    place_pos = (
    57	        base_spec.place_pos_local[0] + place_xy_offset[0],
    58	        base_spec.place_pos_local[1] + place_xy_offset[1],
    59	        base_spec.place_pos_local[2],
    60	    )
    61	
    62	    return PickPlaceTaskSpec(
    63	        instruction=instruction_for_object(object_label),
    64	        object_name=base_spec.object_name,
    65	        ee_body_name=base_spec.ee_body_name,
    66	        object_pos_local=object_pos,
    67	        place_pos_local=place_pos,
    68	        pregrasp_height_m=base_spec.pregrasp_height_m,
    69	        lift_height_m=base_spec.lift_height_m,
    70	        open_finger_m=base_spec.open_finger_m,
    71	        closed_finger_m=base_spec.closed_finger_m,
    72	        free_space_max_speed_m_s=base_spec.free_space_max_speed_m_s,
    73	        free_space_max_accel_m_s2=base_spec.free_space_max_accel_m_s2,
    74	        approach_max_speed_m_s=base_spec.approach_max_speed_m_s,
    75	        approach_max_accel_m_s2=base_spec.approach_max_accel_m_s2,
    76	        lift_max_speed_m_s=base_spec.lift_max_speed_m_s,
    77	        lift_max_accel_m_s2=base_spec.lift_max_accel_m_s2,
    78	        retreat_max_speed_m_s=base_spec.retreat_max_speed_m_s,
    79	        retreat_max_accel_m_s2=base_spec.retreat_max_accel_m_s2,
    80	        grasp_dwell_s=base_spec.grasp_dwell_s,
    81	        release_dwell_s=base_spec.release_dwell_s,
    82	    )
    83	

================================================================================
FILE: ./src/franka_wrist_camera_scene/tasks/sampling.py
================================================================================
     1	"""Deterministic task-parameter sampling."""
     2	
     3	from __future__ import annotations
     4	
     5	from dataclasses import dataclass
     6	import random
     7	
     8	
     9	@dataclass(frozen=True, slots=True)
    10	class XYRange:
    11	    x: tuple[float, float]
    12	    y: tuple[float, float]
    13	
    14	
    15	@dataclass(frozen=True, slots=True)
    16	class LightingOptions:
    17	    intensity_range: tuple[float, float]
    18	    color_options: tuple[tuple[float, float, float], ...]
    19	
    20	
    21	@dataclass(frozen=True, slots=True)
    22	class PickPlaceSample:
    23	    object_xy_offset: tuple[float, float]
    24	    place_xy_offset: tuple[float, float]
    25	    light_intensity: float
    26	    light_color: tuple[float, float, float]
    27	
    28	
    29	def parse_xy_range(config: dict) -> XYRange:
    30	    return XYRange(
    31	        x=(float(config["x"][0]), float(config["x"][1])),
    32	        y=(float(config["y"][0]), float(config["y"][1])),
    33	    )
    34	
    35	
    36	def parse_lighting_options(config: dict) -> LightingOptions:
    37	    return LightingOptions(
    38	        intensity_range=(float(config["dome_light_intensity_range"][0]), float(config["dome_light_intensity_range"][1])),
    39	        color_options=tuple(tuple(float(x) for x in color) for color in config["dome_light_color_options"]),
    40	    )
    41	
    42	
    43	def sample_pick_place_offsets(
    44	    seed: int,
    45	    episode_id: int,
    46	    object_range: XYRange,
    47	    place_range: XYRange,
    48	    lighting: LightingOptions,
    49	) -> PickPlaceSample:
    50	    rng = random.Random(seed + episode_id)
    51	
    52	    object_xy_offset = (
    53	        rng.uniform(object_range.x[0], object_range.x[1]),
    54	        rng.uniform(object_range.y[0], object_range.y[1]),
    55	    )
    56	    place_xy_offset = (
    57	        rng.uniform(place_range.x[0], place_range.x[1]),
    58	        rng.uniform(place_range.y[0], place_range.y[1]),
    59	    )
    60	    light_intensity = rng.uniform(lighting.intensity_range[0], lighting.intensity_range[1])
    61	    light_color = lighting.color_options[rng.randrange(len(lighting.color_options))]
    62	
    63	    return PickPlaceSample(
    64	        object_xy_offset=object_xy_offset,
    65	        place_xy_offset=place_xy_offset,
    66	        light_intensity=light_intensity,
    67	        light_color=light_color,
    68	    )

================================================================================
FILE: ./src/franka_wrist_camera_scene/utils/__init__.py
================================================================================
     1	"""General math, USD stage helpers, seed configurations, and path utilities."""

================================================================================
FILE: ./src/franka_wrist_camera_scene/utils/paths.py
================================================================================
     1	"""Relative paths resolution, config path helpers, and dataset output path builders."""
     2	
     3	from __future__ import annotations
     4	
     5	from pathlib import Path
     6	import yaml
     7	
     8	REPO_ROOT = Path(__file__).resolve().parents[3]
     9	
    10	
    11	def get_config_path(config_name: str) -> Path:
    12	    """Return the absolute path to a configuration file in the configs/ directory."""
    13	    return REPO_ROOT / "configs" / config_name
    14	
    15	
    16	def load_yaml_config(config_name: str) -> dict:
    17	    """Load and return a YAML configuration file as a dict."""
    18	    config_path = get_config_path(config_name)
    19	    with open(config_path, "r") as f:
    20	        return yaml.safe_load(f)
