# Stage 7 Flow-trace Experiments: holdout_libero_object

```json
{
  "split": "holdout_libero_object",
  "variants": [
    {
      "variant": "context_gated_action_no_flow",
      "feature_mode": "M3_gated_base",
      "with_flow": false,
      "model_kind": "gated",
      "input_dim": 1456,
      "best_epoch": 97,
      "best_calib_loss": 0.06281183660030365,
      "train_time_sec": 19.373077154159546,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9995976606961673,
            "spearman": 0.998808026659912,
            "auroc_top30_bad": 0.9999192380952381,
            "mae": 0.021299687534570694,
            "mse": 0.0008593447816625661,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6993038614063213,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18261158776283265
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.49078830626010894
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.77831890985171
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1584886793255806
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9997493478408409,
            "spearman": 0.9994817409803144,
            "auroc_top30_worst": 0.9996586666666667,
            "pairwise_seed_ranking": 0.9528,
            "predicted_best_mean_error": 1.5315435655117036,
            "seed0_mean_error": 1.6047911508083343,
            "random_seed_mean_error": 1.586874898672104,
            "oracle_best_mean_error": 1.5305145078897475,
            "improvement_over_seed0": 0.07324758529663078,
            "gap_to_oracle": 0.0010290576219560421,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6728620612621308
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8436320831951423
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0262884887218475
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2163902379747138
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5889631366491317
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5869308710098267,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3693884298271604,
                "rejected_mean_error": 3.565135498046875,
                "gap_rejected_minus_accepted": 2.1957470682197147
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8118745684623718,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2157627772559734,
                "rejected_mean_error": 2.7061795479954243,
                "gap_rejected_minus_accepted": 1.490416770739451
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.382550597190857,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0262884887218475,
                "rejected_mean_error": 2.151637784576416,
                "gap_rejected_minus_accepted": 1.1253492958545683
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0440728068351746,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.844329157100318,
                "rejected_mean_error": 1.8377042632220013,
                "gap_rejected_minus_accepted": 0.9933751061216833
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5721894264221192,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3820225034819709,
                "rejected_mean_error": 3.6097089767456056,
                "gap_rejected_minus_accepted": 2.227686473263635
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8088040947914124,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2258267788326038,
                "rejected_mean_error": 2.729653651752169,
                "gap_rejected_minus_accepted": 1.5038268729195652
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3914300203323364,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0325154337882996,
                "rejected_mean_error": 2.177066867828369,
                "gap_rejected_minus_accepted": 1.1445514340400695
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0658938586711884,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8385919133822123,
                "rejected_mean_error": 1.8629224447005572,
                "gap_rejected_minus_accepted": 1.0243305313183448
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8574153460892112,
            "spearman": 0.9133586980685906,
            "auroc_top30_bad": 0.9168303571428571,
            "mae": 0.34397808864945545,
            "mse": 0.23607808263035587,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.95,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6903584062897862,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10580803574994206
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.25530224945396185
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.546635127197951
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9853070063268144
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3506465024407952
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.6402225022298698,
            "spearman": 0.7454454090338065,
            "auroc_top30_worst": 0.8790178571428571,
            "pairwise_seed_ranking": 0.89625,
            "predicted_best_mean_error": 1.918394736200571,
            "seed0_mean_error": 2.0284233927726745,
            "random_seed_mean_error": 2.0020590677857397,
            "oracle_best_mean_error": 1.9162342317402363,
            "improvement_over_seed0": 0.11002865657210337,
            "gap_to_oracle": 0.002160504460334778,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7913692906498909
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2574082666635513
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.580740679204464
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7885459862152735
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9964606110751628
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0502357244491582,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9654656143652067,
                "rejected_mean_error": 2.2754155814647676,
                "gap_rejected_minus_accepted": 0.3099499670995609
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.313743531703949,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.7885459862152735,
                "rejected_mean_error": 2.6202044856548308,
                "gap_rejected_minus_accepted": 0.8316584994395573
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6927193403244019,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.580740679204464,
                "rejected_mean_error": 2.412180542945862,
                "gap_rejected_minus_accepted": 0.8314398637413978
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4407994747161865,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.2574082666635513,
                "rejected_mean_error": 2.2428113925457,
                "gap_rejected_minus_accepted": 0.9854031258821487
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.06590349674225,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.998804857333501,
                "rejected_mean_error": 2.294990211725235,
                "gap_rejected_minus_accepted": 0.2961853543917339
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.37732994556427,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.827220630645752,
                "rejected_mean_error": 2.6320316791534424,
                "gap_rejected_minus_accepted": 0.8048110485076905
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7157316207885742,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.5854694217443466,
                "rejected_mean_error": 2.4713773638010026,
                "gap_rejected_minus_accepted": 0.885907942056656
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4397379159927368,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.2839465200901032,
                "rejected_mean_error": 2.276582350333532,
                "gap_rejected_minus_accepted": 0.9926358302434286
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9596309100050787,
            "spearman": 0.9262922445540972,
            "auroc_top30_bad": 0.9503645833333333,
            "mae": 0.17288667213288136,
            "mse": 0.059973326071483146,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9125,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8122689556931444,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11540294047445059
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21967766799032687
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6071049173921347
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.049564282844464
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3408511171862483
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.7495017753883364,
            "spearman": 0.7504899405621285,
            "auroc_top30_worst": 0.8277976190476191,
            "pairwise_seed_ranking": 0.87,
            "predicted_best_mean_error": 1.9464065417647363,
            "seed0_mean_error": 2.045435842871666,
            "random_seed_mean_error": 2.004871594905853,
            "oracle_best_mean_error": 1.9431253403425217,
            "improvement_over_seed0": 0.09902930110692987,
            "gap_to_oracle": 0.0032812014222145525,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3669703364372254
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.6343432223796845
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.7986521643400193
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.893328488667806
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.0061718955636025
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5083287715911866,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9522128101852205,
                "rejected_mean_error": 2.4918036639690397,
                "gap_rejected_minus_accepted": 0.5395908537838192
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.128504455089569,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.893328488667806,
                "rejected_mean_error": 2.344702116250992,
                "gap_rejected_minus_accepted": 0.4513736275831859
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.948164165019989,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.7986521643400193,
                "rejected_mean_error": 2.2136916267871856,
                "gap_rejected_minus_accepted": 0.4150394624471663
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.752145141363144,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.6343432223796845,
                "rejected_mean_error": 2.1301147866249086,
                "gap_rejected_minus_accepted": 0.49577156424522406
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.606605172157288,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9836555189556546,
                "rejected_mean_error": 2.6014587581157684,
                "gap_rejected_minus_accepted": 0.6178032391601138
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1752259731292725,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.9157825549443563,
                "rejected_mean_error": 2.434395706653595,
                "gap_rejected_minus_accepted": 0.5186131517092387
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9545063972473145,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.7967981308698655,
                "rejected_mean_error": 2.2940735548734663,
                "gap_rejected_minus_accepted": 0.4972754240036008
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7949314713478088,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.6463078081607818,
                "rejected_mean_error": 2.1784785211086275,
                "gap_rejected_minus_accepted": 0.5321707129478457
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9786145475188447,
            "spearman": 0.9483831971953328,
            "auroc_top30_bad": 0.9683556547619048,
            "mae": 0.12140756631153636,
            "mse": 0.023974202341757858,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9375,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6358386585173926,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09908346813172102
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18466480396687984
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5231905477494001
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9105866294602553
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.150641152523458
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.8648475553441854,
            "spearman": 0.8227450171563573,
            "auroc_top30_worst": 0.8727976190476191,
            "pairwise_seed_ranking": 0.865,
            "predicted_best_mean_error": 1.6015464678406715,
            "seed0_mean_error": 1.6772294983267784,
            "random_seed_mean_error": 1.6555854290723802,
            "oracle_best_mean_error": 1.6010722801089288,
            "improvement_over_seed0": 0.07568303048610692,
            "gap_to_oracle": 0.00047418773174268125,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2219172418117523
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.345068383216858
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4779125052690505
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5970801202456157
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6553256559371947
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.853049349784851,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.629756063885159,
                "rejected_mean_error": 1.8854519844055175,
                "gap_rejected_minus_accepted": 0.2556959205203586
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.746326208114624,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.5970801202456157,
                "rejected_mean_error": 1.8300622630119323,
                "gap_rejected_minus_accepted": 0.23298214276631657
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6154111623764038,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.4779125052690505,
                "rejected_mean_error": 1.832738806605339,
                "gap_rejected_minus_accepted": 0.35482630133628845
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4419297873973846,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.345068383216858,
                "rejected_mean_error": 1.7587447468439739,
                "gap_rejected_minus_accepted": 0.4136763636271159
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.866785025596619,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.6453171239958868,
                "rejected_mean_error": 1.964440867304802,
                "gap_rejected_minus_accepted": 0.31912374330891513
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7736268937587738,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.6207242925961813,
                "rejected_mean_error": 1.84674511551857,
                "gap_rejected_minus_accepted": 0.22602082292238856
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6341400146484375,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.496884736418724,
                "rejected_mean_error": 1.8575742602348329,
                "gap_rejected_minus_accepted": 0.36068952381610875
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4627444744110107,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.363513958454132,
                "rejected_mean_error": 1.781801344950994,
                "gap_rejected_minus_accepted": 0.4182873864968619
              }
            ]
          }
        }
      }
    },
    {
      "variant": "context_gated_action_plus_flow",
      "feature_mode": "M3_gated_base",
      "with_flow": true,
      "model_kind": "gated",
      "input_dim": 1468,
      "best_epoch": 7,
      "best_calib_loss": 0.05752244591712952,
      "train_time_sec": 19.773905992507935,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9805365257584664,
            "spearman": 0.968512605392017,
            "auroc_top30_bad": 0.9947253333333335,
            "mae": 0.13037078430056573,
            "mse": 0.030123872869924486,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.968,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6797519202747082,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.16132818567752838
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.24264710297584532
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.49541992862224576
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7833694666067759
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1584886793255806
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9935631713609049,
            "spearman": 0.9872233779349621,
            "auroc_top30_worst": 0.9931672380952381,
            "pairwise_seed_ranking": 0.7804,
            "predicted_best_mean_error": 1.5403525013923645,
            "seed0_mean_error": 1.6047911508083343,
            "random_seed_mean_error": 1.586874898672104,
            "oracle_best_mean_error": 1.5305145078897475,
            "improvement_over_seed0": 0.06443864941596988,
            "gap_to_oracle": 0.009837993502616937,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6811344969272614
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8523860987371359
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0320930072307586
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.219874512507463
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5889631366491317
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6159712314605716,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3722288805378808,
                "rejected_mean_error": 3.5395714416503905,
                "gap_rejected_minus_accepted": 2.16734256111251
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9239814281463623,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2192576349799382,
                "rejected_mean_error": 2.695717306182788,
                "gap_rejected_minus_accepted": 1.47645967120285
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4229600429534912,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0320930072307586,
                "rejected_mean_error": 2.145833266067505,
                "gap_rejected_minus_accepted": 1.1137402588367464
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.123003751039505,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8532849783524157,
                "rejected_mean_error": 1.83471261748891,
                "gap_rejected_minus_accepted": 0.9814276391364942
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6104859590530394,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3872000363137986,
                "rejected_mean_error": 3.5631111812591554,
                "gap_rejected_minus_accepted": 2.1759111449453568
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9212075471878052,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.230022196782464,
                "rejected_mean_error": 2.717200585774013,
                "gap_rejected_minus_accepted": 1.4871783889915489
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4187821745872498,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0391923651695252,
                "rejected_mean_error": 2.1703899364471435,
                "gap_rejected_minus_accepted": 1.1311975712776183
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1271522641181946,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8467255395556254,
                "rejected_mean_error": 1.8601822390913325,
                "gap_rejected_minus_accepted": 1.0134566995357073
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.894274485802616,
            "spearman": 0.8884443134761445,
            "auroc_top30_bad": 0.9030877976190476,
            "mae": 0.33272345415316523,
            "mse": 0.17647510101203573,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9125,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7207054877602569,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.2573826964013278
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.28843614522367717
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5581253324262798
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9899094880496462
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3506465024407952
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.7256546769191389,
            "spearman": 0.7091577447359045,
            "auroc_top30_worst": 0.8702083333333333,
            "pairwise_seed_ranking": 0.82375,
            "predicted_best_mean_error": 1.942335530370474,
            "seed0_mean_error": 2.0284233927726745,
            "random_seed_mean_error": 2.0020590677857397,
            "oracle_best_mean_error": 1.9162342317402363,
            "improvement_over_seed0": 0.08608786240220057,
            "gap_to_oracle": 0.02610129863023758,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7968405470252037
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3328805989027024
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.5886414250731469
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.791891970038414
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9964606110751628
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.840534353256226,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9655917669336,
                "rejected_mean_error": 2.2742802083492277,
                "gap_rejected_minus_accepted": 0.3086884414156277
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.4641201496124268,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.791891970038414,
                "rejected_mean_error": 2.6101665341854097,
                "gap_rejected_minus_accepted": 0.8182745641469957
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.743626356124878,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.5886414250731469,
                "rejected_mean_error": 2.4042797970771788,
                "gap_rejected_minus_accepted": 0.8156383720040319
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4601789116859436,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.3328805989027024,
                "rejected_mean_error": 2.217653948465983,
                "gap_rejected_minus_accepted": 0.8847733495632806
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.835835146903992,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.998804857333501,
                "rejected_mean_error": 2.294990211725235,
                "gap_rejected_minus_accepted": 0.2961853543917339
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.4651644825935364,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.8130516727765402,
                "rejected_mean_error": 2.674538552761078,
                "gap_rejected_minus_accepted": 0.8614868799845377
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7493940591812134,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.599543035030365,
                "rejected_mean_error": 2.457303750514984,
                "gap_rejected_minus_accepted": 0.857760715484619
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4516230821609497,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.3762172400951385,
                "rejected_mean_error": 2.2458254436651868,
                "gap_rejected_minus_accepted": 0.8696082035700483
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9344598386479367,
            "spearman": 0.8772812801381904,
            "auroc_top30_bad": 0.9215029761904762,
            "mae": 0.22604119238443673,
            "mse": 0.09570007701598145,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9375,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7433521312257582,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.2025452034547925
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2665035320073366
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6196417584270238
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0848809702694415
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3408511171862483
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.6132306663854524,
            "spearman": 0.5886603041269007,
            "auroc_top30_worst": 0.6932738095238095,
            "pairwise_seed_ranking": 0.74,
            "predicted_best_mean_error": 1.9724808409810066,
            "seed0_mean_error": 2.045435842871666,
            "random_seed_mean_error": 2.004871594905853,
            "oracle_best_mean_error": 1.9431253403425217,
            "improvement_over_seed0": 0.07295500189065951,
            "gap_to_oracle": 0.02935550063848491,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3667576253414153
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.7265645837783814
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.8751282340288162
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.9355540239810944
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.0061718955636025
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5112736463546756,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.957781414522065,
                "rejected_mean_error": 2.441686224937439,
                "gap_rejected_minus_accepted": 0.48390481041537403
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1566081047058105,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.9355540239810944,
                "rejected_mean_error": 2.2180255103111266,
                "gap_rejected_minus_accepted": 0.28247148633003216
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9655597805976868,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.8751282340288162,
                "rejected_mean_error": 2.1372155570983886,
                "gap_rejected_minus_accepted": 0.2620873230695724
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.763097733259201,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.7265645837783814,
                "rejected_mean_error": 2.099374332825343,
                "gap_rejected_minus_accepted": 0.3728097490469615
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5313073396682744,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9926521513197157,
                "rejected_mean_error": 2.520489066839218,
                "gap_rejected_minus_accepted": 0.5278369155195024
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1355504989624023,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.9697999954223633,
                "rejected_mean_error": 2.272343385219574,
                "gap_rejected_minus_accepted": 0.3025433897972105
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9852806329727173,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.8849866360425949,
                "rejected_mean_error": 2.205885049700737,
                "gap_rejected_minus_accepted": 0.3208984136581423
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.776231974363327,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.7881868422031402,
                "rejected_mean_error": 2.1311855097611745,
                "gap_rejected_minus_accepted": 0.3429986675580343
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9547286567882639,
            "spearman": 0.9176020415127971,
            "auroc_top30_bad": 0.9594196428571429,
            "mae": 0.1842069777753204,
            "mse": 0.05493806742634834,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.825,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6507399815506248,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.17333593722432852
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.24856791108846665
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.522645237967372
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9119583753248056
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.150641152523458
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.8081109502907784,
            "spearman": 0.8137978362364765,
            "auroc_top30_worst": 0.8625,
            "pairwise_seed_ranking": 0.7925,
            "predicted_best_mean_error": 1.608061182498932,
            "seed0_mean_error": 1.6772294983267784,
            "random_seed_mean_error": 1.6555854290723802,
            "oracle_best_mean_error": 1.6010722801089288,
            "improvement_over_seed0": 0.06916831582784644,
            "gap_to_oracle": 0.00698890239000316,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.222354918718338
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3461140179634095
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4803149783611298
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5978160305817921
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6553256559371947
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.237644624710083,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.627052272690667,
                "rejected_mean_error": 1.9097861051559448,
                "gap_rejected_minus_accepted": 0.2827338324652777
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8426637649536133,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.5978160305817921,
                "rejected_mean_error": 1.8278545320034028,
                "gap_rejected_minus_accepted": 0.23003850142161064
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7322453260421753,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.4803149783611298,
                "rejected_mean_error": 1.8303363335132599,
                "gap_rejected_minus_accepted": 0.35002135515213006
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5294422507286072,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.3461140179634095,
                "rejected_mean_error": 1.7583962019284567,
                "gap_rejected_minus_accepted": 0.41228218396504723
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.229280996322632,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.648337033059862,
                "rejected_mean_error": 1.9372616857290268,
                "gap_rejected_minus_accepted": 0.2889246526691649
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8371522724628448,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.6197392245133717,
                "rejected_mean_error": 1.8497003197669983,
                "gap_rejected_minus_accepted": 0.22996109525362662
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7359021306037903,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.5032604724168777,
                "rejected_mean_error": 1.851198524236679,
                "gap_rejected_minus_accepted": 0.3479380518198014
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.532012939453125,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.3597745776176453,
                "rejected_mean_error": 1.7830478052298229,
                "gap_rejected_minus_accepted": 0.42327322761217756
              }
            ]
          }
        }
      }
    },
    {
      "variant": "action_only_plus_flow",
      "feature_mode": "A0_action_flat",
      "with_flow": true,
      "model_kind": "mlp",
      "input_dim": 82,
      "best_epoch": 92,
      "best_calib_loss": 0.07583372294902802,
      "train_time_sec": 7.154823303222656,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9713285442015858,
            "spearman": 0.9429636322167738,
            "auroc_top30_bad": 0.9988975238095238,
            "mae": 0.10904425837397576,
            "mse": 0.043268905643786104,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.52,
            "expert_lt_simvla_seed0": 0.988,
            "same_context_pred_std": 0.6850022422550903,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.28294906157255173
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.32362055480480195
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.49887733442783355
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7784568023204803
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1584886793255806
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9990192971961073,
            "spearman": 0.9982162051943715,
            "auroc_top30_worst": 0.9995580952380952,
            "pairwise_seed_ranking": 0.89,
            "predicted_best_mean_error": 1.5342421214580535,
            "seed0_mean_error": 1.6047911508083343,
            "random_seed_mean_error": 1.586874898672104,
            "oracle_best_mean_error": 1.5305145078897475,
            "improvement_over_seed0": 0.07054902935028085,
            "gap_to_oracle": 0.0037276135683059763,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6735488197803498
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8446301981233634
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0267050912380218
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2167480377945057
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5889631366491317
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.538847947120667,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3693250246842703,
                "rejected_mean_error": 3.5657061443328857,
                "gap_rejected_minus_accepted": 2.196381119648615
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8268275260925293,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2160682273330912,
                "rejected_mean_error": 2.7052651495217517,
                "gap_rejected_minus_accepted": 1.4891969221886605
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4061258435249329,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0267050912380218,
                "rejected_mean_error": 2.1512211820602416,
                "gap_rejected_minus_accepted": 1.1245160908222198
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0517785549163818,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8453459453087645,
                "rejected_mean_error": 1.837364610383961,
                "gap_rejected_minus_accepted": 0.9920186650751964
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5420090198516845,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.381742963525984,
                "rejected_mean_error": 3.6122248363494873,
                "gap_rejected_minus_accepted": 2.2304818728235034
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.837307870388031,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2259435777995675,
                "rejected_mean_error": 2.7293069627549915,
                "gap_rejected_minus_accepted": 1.503363384955424
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4060510396957397,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0326425156593322,
                "rejected_mean_error": 2.1769397859573365,
                "gap_rejected_minus_accepted": 1.1442972702980043
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0710600912570953,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8390348250903781,
                "rejected_mean_error": 1.8627732284566298,
                "gap_rejected_minus_accepted": 1.0237384033662518
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8364001397748221,
            "spearman": 0.8525867271821495,
            "auroc_top30_bad": 0.9098735119047618,
            "mae": 0.40020018157549203,
            "mse": 0.2801121027560464,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.4875,
            "expert_lt_simvla_seed0": 0.9625,
            "same_context_pred_std": 0.7621277374797135,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3533921690657735
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.37656796392053365
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.574953974019736
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9949737917259336
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3506465024407952
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.5689277857669308,
            "spearman": 0.6410963193519958,
            "auroc_top30_worst": 0.8404761904761904,
            "pairwise_seed_ranking": 0.84125,
            "predicted_best_mean_error": 1.9236535929143428,
            "seed0_mean_error": 2.0284233927726745,
            "random_seed_mean_error": 2.0020590677857397,
            "oracle_best_mean_error": 1.9162342317402363,
            "improvement_over_seed0": 0.10476979985833168,
            "gap_to_oracle": 0.007419361174106465,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8182799279689789
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3601218551397323
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6010903325676917
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8633286891380947
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9964606110751628
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1531047344207765,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9661681577563286,
                "rejected_mean_error": 2.269092690944672,
                "gap_rejected_minus_accepted": 0.3029245331883432
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3081694841384888,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.8633286891380947,
                "rejected_mean_error": 2.3958563768863677,
                "gap_rejected_minus_accepted": 0.532527687748273
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5846792459487915,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.6010903325676917,
                "rejected_mean_error": 2.391830889582634,
                "gap_rejected_minus_accepted": 0.7907405570149422
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4171311259269714,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.3601218551397323,
                "rejected_mean_error": 2.208573529720306,
                "gap_rejected_minus_accepted": 0.8484516745805739
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.220347309112549,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.998804857333501,
                "rejected_mean_error": 2.294990211725235,
                "gap_rejected_minus_accepted": 0.2961853543917339
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3317437767982483,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.9042639454205832,
                "rejected_mean_error": 2.400901734828949,
                "gap_rejected_minus_accepted": 0.4966377894083658
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.590098261833191,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.6162776231765748,
                "rejected_mean_error": 2.4405691623687744,
                "gap_rejected_minus_accepted": 0.8242915391921997
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4372513890266418,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.376680415868759,
                "rejected_mean_error": 2.245671051740646,
                "gap_rejected_minus_accepted": 0.8689906358718871
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.95255487080685,
            "spearman": 0.8887958531213024,
            "auroc_top30_bad": 0.9384151785714285,
            "mae": 0.22376521285623313,
            "mse": 0.07622245219479508,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.4875,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7821008398763588,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.33713805470615626
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3276436607539654
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6052307676523924
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0379006478687127
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3408511171862483
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.7728362853522884,
            "spearman": 0.7504991281195507,
            "auroc_top30_worst": 0.9157142857142857,
            "pairwise_seed_ranking": 0.82,
            "predicted_best_mean_error": 1.9519401058554648,
            "seed0_mean_error": 2.045435842871666,
            "random_seed_mean_error": 2.004871594905853,
            "oracle_best_mean_error": 1.9431253403425217,
            "improvement_over_seed0": 0.09349573701620129,
            "gap_to_oracle": 0.008814765512943135,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3575882107019424
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.6379388535022736
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.7818999683856964
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8811191085974375
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.0061718955636025
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4886864185333253,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.957898806532224,
                "rejected_mean_error": 2.4406296968460084,
                "gap_rejected_minus_accepted": 0.48273089031378436
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2089840173721313,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.8811191085974375,
                "rejected_mean_error": 2.381330256462097,
                "gap_rejected_minus_accepted": 0.5002111478646596
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.749933660030365,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.7818999683856964,
                "rejected_mean_error": 2.2304438227415084,
                "gap_rejected_minus_accepted": 0.448543854355812
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6366795003414154,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.6379388535022736,
                "rejected_mean_error": 2.128916242917379,
                "gap_rejected_minus_accepted": 0.49097738941510527
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.53421688079834,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9926521513197157,
                "rejected_mean_error": 2.520489066839218,
                "gap_rejected_minus_accepted": 0.5278369155195024
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2831950783729553,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.9183725774288178,
                "rejected_mean_error": 2.4266256392002106,
                "gap_rejected_minus_accepted": 0.5082530617713927
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7990379929542542,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.7859901815652848,
                "rejected_mean_error": 2.3048815041780473,
                "gap_rejected_minus_accepted": 0.5188913226127625
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.644761472940445,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.665416568517685,
                "rejected_mean_error": 2.172108934322993,
                "gap_rejected_minus_accepted": 0.506692365805308
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9494614568763711,
            "spearman": 0.8887028279904482,
            "auroc_top30_bad": 0.9377232142857141,
            "mae": 0.2043055315501988,
            "mse": 0.06490906028160538,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.5125,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6010580472182203,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3410205846652389
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.32617077089846136
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5326150169223547
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9070428688824177
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.150641152523458
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.7648883873109652,
            "spearman": 0.7537550859692872,
            "auroc_top30_worst": 0.8370238095238095,
            "pairwise_seed_ranking": 0.8475,
            "predicted_best_mean_error": 1.6045831084251403,
            "seed0_mean_error": 1.6772294983267784,
            "random_seed_mean_error": 1.6555854290723802,
            "oracle_best_mean_error": 1.6010722801089288,
            "improvement_over_seed0": 0.07264638990163808,
            "gap_to_oracle": 0.003510828316211523,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.297781029343605
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3948965442180634
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.5064304399490356
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5804260190327961
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6553256559371947
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.6244203567504882,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.6294509728749593,
                "rejected_mean_error": 1.8881978034973144,
                "gap_rejected_minus_accepted": 0.25874683062235504
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.582087904214859,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.5804260190327961,
                "rejected_mean_error": 1.8800245666503905,
                "gap_rejected_minus_accepted": 0.2995985476175944
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5060026049613953,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.5064304399490356,
                "rejected_mean_error": 1.804220871925354,
                "gap_rejected_minus_accepted": 0.2977904319763185
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3676846623420715,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.3948965442180634,
                "rejected_mean_error": 1.742135359843572,
                "gap_rejected_minus_accepted": 0.3472388156255086
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.6593441963195803,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.6506856663359537,
                "rejected_mean_error": 1.9161239862442017,
                "gap_rejected_minus_accepted": 0.26543831990824795
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.5954696536064148,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.6018013894557952,
                "rejected_mean_error": 1.9035138249397279,
                "gap_rejected_minus_accepted": 0.3017124354839327
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5295300483703613,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.5242290884256362,
                "rejected_mean_error": 1.8302299082279205,
                "gap_rejected_minus_accepted": 0.30600081980228433
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3878122568130493,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.4156296730041504,
                "rejected_mean_error": 1.7644294401009877,
                "gap_rejected_minus_accepted": 0.34879976709683724
              }
            ]
          }
        }
      }
    },
    {
      "variant": "seed_relative_plus_flow",
      "feature_mode": "M4_seed_relative",
      "with_flow": true,
      "model_kind": "mlp_big",
      "input_dim": 1538,
      "best_epoch": 95,
      "best_calib_loss": 0.06897579878568649,
      "train_time_sec": 14.970632076263428,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.999248399380364,
            "spearman": 0.9983315026967152,
            "auroc_top30_bad": 0.9994841904761904,
            "mae": 0.028424557317141445,
            "mse": 0.001390800320837751,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7058372610220769,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0008113843202590943
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18266337232589722
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.49093520319461825
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7783052461783091
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1584886793255806
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9993280040823497,
            "spearman": 0.9986888265528492,
            "auroc_top30_worst": 0.9992838095238095,
            "pairwise_seed_ranking": 0.9356,
            "predicted_best_mean_error": 1.5319080612659455,
            "seed0_mean_error": 1.6047911508083343,
            "random_seed_mean_error": 1.586874898672104,
            "oracle_best_mean_error": 1.5305145078897475,
            "improvement_over_seed0": 0.07288308954238887,
            "gap_to_oracle": 0.0013935533761979535,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6733251483440399
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8438792670957553
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0266404931545257
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2164256127594886
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5889631366491317
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6493488311767583,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3695080814096663,
                "rejected_mean_error": 3.564058633804321,
                "gap_rejected_minus_accepted": 2.194550552394655
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.84233820438385,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2157792225400565,
                "rejected_mean_error": 2.7061303172248623,
                "gap_rejected_minus_accepted": 1.4903510946848058
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4134478569030762,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0266404931545257,
                "rejected_mean_error": 2.1512857801437377,
                "gap_rejected_minus_accepted": 1.124645286989212
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.063204139471054,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8446816361178986,
                "rejected_mean_error": 1.8375865194306429,
                "gap_rejected_minus_accepted": 0.9929048833127443
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.649348831176758,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.3821096777915955,
                "rejected_mean_error": 3.6089244079589844,
                "gap_rejected_minus_accepted": 2.226814730167389
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8455328047275543,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2259091811384109,
                "rejected_mean_error": 2.7294090607809642,
                "gap_rejected_minus_accepted": 1.5034998796425534
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4272862672805786,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0331726622581483,
                "rejected_mean_error": 2.1764096393585204,
                "gap_rejected_minus_accepted": 1.143236977100372
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0769524276256561,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8385793907301766,
                "rejected_mean_error": 1.8629266635619384,
                "gap_rejected_minus_accepted": 1.0243472728317617
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9039674085648481,
            "spearman": 0.9151365860093316,
            "auroc_top30_bad": 0.9246279761904761,
            "mae": 0.3778452315024333,
            "mse": 0.2364502014950043,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.95,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.4872697479171844,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.13474963689222932
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2644908195361495
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5467791490070522
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9841924258942405
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3506465024407952
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.8831851748223868,
            "spearman": 0.8410155063469146,
            "auroc_top30_worst": 0.9610714285714286,
            "pairwise_seed_ranking": 0.89125,
            "predicted_best_mean_error": 1.9195098221302032,
            "seed0_mean_error": 2.0284233927726745,
            "random_seed_mean_error": 2.0020590677857397,
            "oracle_best_mean_error": 1.9162342317402363,
            "improvement_over_seed0": 0.10891357064247131,
            "gap_to_oracle": 0.0032755903899668315,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.790771035850048
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2190990656614304
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.578451284468174
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.718895146648089
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9964606110751628
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.211686682701111,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.8939373650484614,
                "rejected_mean_error": 2.9191698253154756,
                "gap_rejected_minus_accepted": 1.0252324602670142
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9693226218223572,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.718895146648089,
                "rejected_mean_error": 2.829157004356384,
                "gap_rejected_minus_accepted": 1.110261857708295
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5154147148132324,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.578451284468174,
                "rejected_mean_error": 2.414469937682152,
                "gap_rejected_minus_accepted": 0.836018653213978
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3402429819107056,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.2190990656614304,
                "rejected_mean_error": 2.2555811262130736,
                "gap_rejected_minus_accepted": 1.0364820605516432
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2520094871521,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.913783609867096,
                "rejected_mean_error": 3.060181438922882,
                "gap_rejected_minus_accepted": 1.1463978290557861
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0039753913879395,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.7307342092196147,
                "rejected_mean_error": 2.9214909434318543,
                "gap_rejected_minus_accepted": 1.1907567342122396
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5362964868545532,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.5852897673845292,
                "rejected_mean_error": 2.47155701816082,
                "gap_rejected_minus_accepted": 0.886267250776291
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3420324921607971,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.2649443447589874,
                "rejected_mean_error": 2.282916408777237,
                "gap_rejected_minus_accepted": 1.0179720640182497
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9295620281328132,
            "spearman": 0.9157707947742805,
            "auroc_top30_bad": 0.9369196428571428,
            "mae": 0.30624547543952757,
            "mse": 0.1463085259804179,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.975,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.5548408711731978,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1091826545074582
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22963812954723836
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5928006803244352
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0602863649030527
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3408511171862483
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.763338460165835,
            "spearman": 0.8495794348714679,
            "auroc_top30_worst": 0.8952380952380953,
            "pairwise_seed_ranking": 0.86625,
            "predicted_best_mean_error": 1.946242581307888,
            "seed0_mean_error": 2.045435842871666,
            "random_seed_mean_error": 2.004871594905853,
            "oracle_best_mean_error": 1.9431253403425217,
            "improvement_over_seed0": 0.09919326156377806,
            "gap_to_oracle": 0.0031172409653663635,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3219425410032273
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.5711091828346253
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.749847060441971
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.897812262773514
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.0061718955636025
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0801363706588747,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.953459753923946,
                "rejected_mean_error": 2.480581170320511,
                "gap_rejected_minus_accepted": 0.527121416396565
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7721725404262543,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.897812262773514,
                "rejected_mean_error": 2.3312507939338682,
                "gap_rejected_minus_accepted": 0.43343853116035436
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6712775230407715,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.749847060441971,
                "rejected_mean_error": 2.262496730685234,
                "gap_rejected_minus_accepted": 0.5126496702432632
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5913589000701904,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.5711091828346253,
                "rejected_mean_error": 2.1511927998065947,
                "gap_rejected_minus_accepted": 0.5800836169719694
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1140738487243658,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9836555189556546,
                "rejected_mean_error": 2.6014587581157684,
                "gap_rejected_minus_accepted": 0.6178032391601138
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8066763877868652,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.9183725774288178,
                "rejected_mean_error": 2.4266256392002106,
                "gap_rejected_minus_accepted": 0.5082530617713927
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6827057003974915,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.761897447705269,
                "rejected_mean_error": 2.328974238038063,
                "gap_rejected_minus_accepted": 0.5670767903327942
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6156984865665436,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.5817175030708313,
                "rejected_mean_error": 2.2000086228052775,
                "gap_rejected_minus_accepted": 0.6182911197344463
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.9380025732855563,
            "spearman": 0.9305483443973324,
            "auroc_top30_bad": 0.9528571428571428,
            "mae": 0.19416802466268565,
            "mse": 0.0659316551766185,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.5830866387835074,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1244487764313817
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21342792987823486
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5280834128707648
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9193388692041238
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.150641152523458
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.7169812311433095,
            "spearman": 0.748943430896443,
            "auroc_top30_worst": 0.8303571428571429,
            "pairwise_seed_ranking": 0.845,
            "predicted_best_mean_error": 1.6037189215421677,
            "seed0_mean_error": 1.6772294983267784,
            "random_seed_mean_error": 1.6555854290723802,
            "oracle_best_mean_error": 1.6010722801089288,
            "improvement_over_seed0": 0.0735105767846107,
            "gap_to_oracle": 0.0026466414332388943,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.235681766271591
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.354754822254181
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4985412847995758
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6101929116249085
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6553256559371947
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8922414660453797,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.6252443697717456,
                "rejected_mean_error": 1.926057231426239,
                "gap_rejected_minus_accepted": 0.3008128616544934
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.568422943353653,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.6101929116249085,
                "rejected_mean_error": 1.790723888874054,
                "gap_rejected_minus_accepted": 0.18053097724914546
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4639069437980652,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.4985412847995758,
                "rejected_mean_error": 1.8121100270748138,
                "gap_rejected_minus_accepted": 0.313568742275238
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.303608238697052,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.354754822254181,
                "rejected_mean_error": 1.7555159338315327,
                "gap_rejected_minus_accepted": 0.4007611115773517
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9586217522621157,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.6453171239958868,
                "rejected_mean_error": 1.964440867304802,
                "gap_rejected_minus_accepted": 0.31912374330891513
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.5801029801368713,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.6341851989428202,
                "rejected_mean_error": 1.806362396478653,
                "gap_rejected_minus_accepted": 0.17217719753583283
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4967194199562073,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.5136649072170258,
                "rejected_mean_error": 1.8407940894365311,
                "gap_rejected_minus_accepted": 0.32712918221950527
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3120529055595398,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.3720414638519287,
                "rejected_mean_error": 1.7789588431517283,
                "gap_rejected_minus_accepted": 0.40691737929979954
              }
            ]
          }
        }
      }
    },
    {
      "variant": "flow_only",
      "feature_mode": "flow_only",
      "with_flow": true,
      "model_kind": "mlp",
      "input_dim": 12,
      "best_epoch": 99,
      "best_calib_loss": 0.0624358169734478,
      "train_time_sec": 6.617947340011597,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8202611735720708,
            "spearman": 0.6743003589408618,
            "auroc_top30_bad": 0.7579398095238095,
            "mae": 0.30320223338603974,
            "mse": 0.2653623684415384,
            "expert_lt_perturb_large": 0.5,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.98,
            "same_context_pred_std": 0.5337580442513092,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6770181224942208
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7187881823062897
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7220369923353195
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8281806978384654
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1584886793255806
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9960470654435761,
            "spearman": 0.9901685922358991,
            "auroc_top30_worst": 0.9985980952380952,
            "pairwise_seed_ranking": 0.8184,
            "predicted_best_mean_error": 1.5421255614757539,
            "seed0_mean_error": 1.6047911508083343,
            "random_seed_mean_error": 1.586874898672104,
            "oracle_best_mean_error": 1.5305145078897475,
            "improvement_over_seed0": 0.06266558933258048,
            "gap_to_oracle": 0.011611053586006337,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6799474685192108
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8549319172325807
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0285136495113374
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2173131552777057
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5889631366491317
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5275954246521,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3699219832685259,
                "rejected_mean_error": 3.560333517074585,
                "gap_rejected_minus_accepted": 2.190411533806059
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.804078757762909,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2167051558242663,
                "rejected_mean_error": 2.7033584338788406,
                "gap_rejected_minus_accepted": 1.4866532780545743
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3903838992118835,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0285136495113374,
                "rejected_mean_error": 2.1494126237869264,
                "gap_rejected_minus_accepted": 1.120898974275589
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0418566167354584,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.855660273529851,
                "rejected_mean_error": 1.8339191624296385,
                "gap_rejected_minus_accepted": 0.9782588888997875
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5275954246520995,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.381742963525984,
                "rejected_mean_error": 3.6122248363494873,
                "gap_rejected_minus_accepted": 2.2304818728235034
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8135702013969421,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2267350815834208,
                "rejected_mean_error": 2.726957578507681,
                "gap_rejected_minus_accepted": 1.5002224969242601
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4275459051132202,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.033765410900116,
                "rejected_mean_error": 2.1758168907165527,
                "gap_rejected_minus_accepted": 1.1420514798164367
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.075714260339737,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8435899596365671,
                "rejected_mean_error": 1.861238610935721,
                "gap_rejected_minus_accepted": 1.017648651299154
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8427803587322151,
            "spearman": 0.7983652493551191,
            "auroc_top30_bad": 0.8907068452380952,
            "mae": 0.3427861793804914,
            "mse": 0.27832075102350984,
            "expert_lt_perturb_large": 0.5,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7132469255574835,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7165656212717295
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7088486669957638
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7036580690555274
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9800286729012927
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3506465024407952
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.961434564465362,
            "spearman": 0.9131950199688748,
            "auroc_top30_worst": 0.9299107142857143,
            "pairwise_seed_ranking": 0.77,
            "predicted_best_mean_error": 1.932616601139307,
            "seed0_mean_error": 2.0284233927726745,
            "random_seed_mean_error": 2.0020590677857397,
            "oracle_best_mean_error": 1.9162342317402363,
            "improvement_over_seed0": 0.09580679163336736,
            "gap_to_oracle": 0.016382369399070784,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.790771035850048
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.195933284163475
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.5304212310910226
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7146693156162898
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9964606110751628
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0430590867996217,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.8581197650896177,
                "rejected_mean_error": 3.2415282249450685,
                "gap_rejected_minus_accepted": 1.3834084598554508
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.290165960788727,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.7146693156162898,
                "rejected_mean_error": 2.8418344974517824,
                "gap_rejected_minus_accepted": 1.1271651818354926
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8108264207839966,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.5304212310910226,
                "rejected_mean_error": 2.4624999910593033,
                "gap_rejected_minus_accepted": 0.9320787599682807
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.573008418083191,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.195933284163475,
                "rejected_mean_error": 2.263303053379059,
                "gap_rejected_minus_accepted": 1.067369769215584
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.052415704727174,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.8828485508759816,
                "rejected_mean_error": 3.3385969698429108,
                "gap_rejected_minus_accepted": 1.4557484189669292
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3623589277267456,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.7312264402707418,
                "rejected_mean_error": 2.9200142502784727,
                "gap_rejected_minus_accepted": 1.188787810007731
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.742259681224823,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.5577804654836656,
                "rejected_mean_error": 2.499066320061684,
                "gap_rejected_minus_accepted": 0.9412858545780183
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5725723505020142,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.2171136617660523,
                "rejected_mean_error": 2.298859969774882,
                "gap_rejected_minus_accepted": 1.0817463080088296
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.8134552722624122,
            "spearman": 0.7965342851978401,
            "auroc_top30_bad": 0.8548214285714286,
            "mae": 0.3591307208314538,
            "mse": 0.2739353376792203,
            "expert_lt_perturb_large": 0.5,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.690183176630694,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6383152697235346
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6445454493910074
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6755303388088941
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.045316678037246
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3408511171862483
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.8401223851820386,
            "spearman": 0.7807035043969024,
            "auroc_top30_worst": 0.8438392857142858,
            "pairwise_seed_ranking": 0.7525,
            "predicted_best_mean_error": 1.9521664530038834,
            "seed0_mean_error": 2.045435842871666,
            "random_seed_mean_error": 2.004871594905853,
            "oracle_best_mean_error": 1.9431253403425217,
            "improvement_over_seed0": 0.09326938986778277,
            "gap_to_oracle": 0.00904111266136165,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3373013645410539
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.5678332102298738
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.7848893564939499
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8868809644381206
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.0061718955636025
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.356426453590393,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.9356164279911252,
                "rejected_mean_error": 2.6411711037158967,
                "gap_rejected_minus_accepted": 0.7055546757247715
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1287899017333984,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.8868809644381206,
                "rejected_mean_error": 2.3640446889400484,
                "gap_rejected_minus_accepted": 0.4771637245019278
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8891047835350037,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.7848893564939499,
                "rejected_mean_error": 2.227454434633255,
                "gap_rejected_minus_accepted": 0.4425650781393051
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6311073005199432,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.5678332102298738,
                "rejected_mean_error": 2.1522847906748455,
                "gap_rejected_minus_accepted": 0.5844515804449717
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3967492103576666,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.9655449589093525,
                "rejected_mean_error": 2.764453798532486,
                "gap_rejected_minus_accepted": 0.7989088396231334
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2109612226486206,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.9186120609442392,
                "rejected_mean_error": 2.425907188653946,
                "gap_rejected_minus_accepted": 0.5072951277097066
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.943875014781952,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.8095613420009613,
                "rejected_mean_error": 2.2813103437423705,
                "gap_rejected_minus_accepted": 0.4717490017414092
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6806270778179169,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.5839979588985442,
                "rejected_mean_error": 2.1992484708627065,
                "gap_rejected_minus_accepted": 0.6152505119641622
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 800,
            "pearson": 0.7353340159899826,
            "spearman": 0.6885826800476783,
            "auroc_top30_bad": 0.7801450892857142,
            "mae": 0.2852555549517274,
            "mse": 0.2470521682753047,
            "expert_lt_perturb_large": 0.5,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.5772729287349796,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6380694348365068
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6284851162880659
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6459566491097212
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.921212221334378
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.150641152523458
              }
            ]
          },
          "simvla_only": {
            "n": 400,
            "contexts": 80,
            "pearson": 0.9324775296640311,
            "spearman": 0.9455907224420153,
            "auroc_top30_worst": 0.9656547619047618,
            "pairwise_seed_ranking": 0.6925,
            "predicted_best_mean_error": 1.618327558040619,
            "seed0_mean_error": 1.6772294983267784,
            "random_seed_mean_error": 1.6555854290723802,
            "oracle_best_mean_error": 1.6010722801089288,
            "improvement_over_seed0": 0.05890194028615947,
            "gap_to_oracle": 0.017255277931690127,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2062037408351898
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.334216103553772
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4717233657836915
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.568001627922058
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6553256559371947
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9955886960029605,
                "accepted_n": 360,
                "rejected_n": 40,
                "accepted_mean_error": 1.6224933634201686,
                "rejected_mean_error": 1.9508162885904312,
                "gap_rejected_minus_accepted": 0.3283229251702626
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.793035238981247,
                "accepted_n": 300,
                "rejected_n": 100,
                "accepted_mean_error": 1.568001627922058,
                "rejected_mean_error": 1.917297739982605,
                "gap_rejected_minus_accepted": 0.3492961120605469
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6672845482826233,
                "accepted_n": 200,
                "rejected_n": 200,
                "accepted_mean_error": 1.4717233657836915,
                "rejected_mean_error": 1.8389279460906982,
                "gap_rejected_minus_accepted": 0.36720458030700676
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5191514492034912,
                "accepted_n": 100,
                "rejected_n": 300,
                "accepted_mean_error": 1.334216103553772,
                "rejected_mean_error": 1.7623621733983357,
                "gap_rejected_minus_accepted": 0.4281460698445636
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9703911900520328,
                "accepted_n": 72,
                "rejected_n": 8,
                "accepted_mean_error": 1.6432004471619923,
                "rejected_mean_error": 1.9834909588098526,
                "gap_rejected_minus_accepted": 0.3402905116478603
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.799645334482193,
                "accepted_n": 60,
                "rejected_n": 20,
                "accepted_mean_error": 1.5843712051709493,
                "rejected_mean_error": 1.9558043777942657,
                "gap_rejected_minus_accepted": 0.37143317262331643
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6754443645477295,
                "accepted_n": 40,
                "rejected_n": 40,
                "accepted_mean_error": 1.480402648448944,
                "rejected_mean_error": 1.8740563482046126,
                "gap_rejected_minus_accepted": 0.39365369975566855
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5495991110801697,
                "accepted_n": 20,
                "rejected_n": 60,
                "accepted_mean_error": 1.353918582201004,
                "rejected_mean_error": 1.7849998037020365,
                "gap_rejected_minus_accepted": 0.43108122150103245
              }
            ]
          }
        }
      }
    }
  ]
}
```
