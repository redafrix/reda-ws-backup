# Stage 7 Multi-Expert Target Experiments: holdout_libero_object

```json
{
  "split": "holdout_libero_object",
  "by_target": {
    "target_chunk_l2_single_expert": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 38,
        "best_calib_loss": 0.09452453255653381,
        "train_time_sec": 14.523582458496094,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8953520464763949,
              "spearman": 0.7989069683159783,
              "auroc_top30_bad": 0.8683053333333333,
              "mae": 0.22110375574305655,
              "mse": 0.24185099279905925,
              "expert_lt_perturb_large": 0.98,
              "expert_lt_other_task": 0.502,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.7938298443084911,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6300999336391687
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5661311921894551
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.724836527428031
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0186871194978555
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4164188162431122
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9979879220557801,
              "spearman": 0.994208897832078,
              "auroc_top30_worst": 0.9979255238095237,
              "pairwise_seed_ranking": 0.8386,
              "predicted_best_mean_error": 1.7126112487912177,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.0818131488263607,
              "gap_to_oracle": 0.011017201066017002,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7324555311799049
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8845618812799454
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.08573381742239
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.305745312333107
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.0724894523620607,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.490213297466437,
                  "rejected_mean_error": 4.439061107635498,
                  "gap_rejected_minus_accepted": 2.9488478101690614
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9936261773109436,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.305745312333107,
                  "rejected_mean_error": 3.2231563769340514,
                  "gap_rejected_minus_accepted": 1.9174110646009443
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.48183274269104,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.08573381742239,
                  "rejected_mean_error": 2.4844623395442964,
                  "gap_rejected_minus_accepted": 1.3987285221219063
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0747427940368652,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8845618812799454,
                  "rejected_mean_error": 2.085276810884476,
                  "gap_rejected_minus_accepted": 1.2007149296045305
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.134026885032654,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4917665520310401,
                  "rejected_mean_error": 4.518345007896423,
                  "gap_rejected_minus_accepted": 3.026578455865383
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.019087553024292,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3024907932678857,
                  "rejected_mean_error": 3.2702252106666565,
                  "gap_rejected_minus_accepted": 1.9677344173987708
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4888056516647339,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0785757425427436,
                  "rejected_mean_error": 2.5102730526924133,
                  "gap_rejected_minus_accepted": 1.4316973101496697
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.066884994506836,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8734018224477768,
                  "rejected_mean_error": 2.101431922674179,
                  "gap_rejected_minus_accepted": 1.2280301002264022
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8103155444186965,
              "spearman": 0.6870901121842173,
              "auroc_top30_bad": 0.7627832380952381,
              "mae": 0.47752818445265294,
              "mse": 0.5220427130892579,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.532,
              "expert_lt_simvla_seed0": 0.948,
              "same_context_pred_std": 0.9180560206288048,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9885052654147148
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7191099058866501
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.817355822277069
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1051618416229885
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8292236758514169,
              "spearman": 0.7622567049322914,
              "auroc_top30_worst": 0.858023619047619,
              "pairwise_seed_ranking": 0.7356,
              "predicted_best_mean_error": 2.0090035947561264,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.09547740995883958,
              "gap_to_oracle": 0.020108365058898903,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2301311440467835
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2471402938931415
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4280631502628327
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.611257656392004
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.353633546829225,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.843676648537318,
                  "rejected_mean_error": 4.20589340019226,
                  "gap_rejected_minus_accepted": 2.3622167516549424
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.824943482875824,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.610818598383646,
                  "rejected_mean_error": 3.48414018512153,
                  "gap_rejected_minus_accepted": 1.873321586737884
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.729353666305542,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4280631502628327,
                  "rejected_mean_error": 2.7317334971427916,
                  "gap_rejected_minus_accepted": 1.3036703468799589
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.243837147951126,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2510679249946302,
                  "rejected_mean_error": 2.3567648282872957,
                  "gap_rejected_minus_accepted": 1.1056969032926656
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.3648402214050295,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8662958346472847,
                  "rejected_mean_error": 4.2481475353240965,
                  "gap_rejected_minus_accepted": 2.381851700676812
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8592864274978638,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6288269892095881,
                  "rejected_mean_error": 3.5163429237547374,
                  "gap_rejected_minus_accepted": 1.8875159345451493
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7414114475250244,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4277362699508667,
                  "rejected_mean_error": 2.781225739479065,
                  "gap_rejected_minus_accepted": 1.3534894695281985
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2295380234718323,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1746263674327306,
                  "rejected_mean_error": 2.4177475402699433,
                  "gap_rejected_minus_accepted": 1.2431211728372127
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.618400552591463,
              "spearman": 0.5131322577267223,
              "auroc_top30_bad": 0.6221112380952382,
              "mae": 0.5341248122215271,
              "mse": 0.7092771333942977,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.6571698202141915,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7250998467803002
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8998869170427323
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9378751229882241
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.136800506679217
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8172807327616134,
              "spearman": 0.7664136458327334,
              "auroc_top30_worst": 0.816024380952381,
              "pairwise_seed_ranking": 0.7764,
              "predicted_best_mean_error": 1.600007110476494,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.05713603198528272,
              "gap_to_oracle": 0.02010958898067483,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.414990003824234
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.833301597680801
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1282869549751282
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3799499880149166
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.048325085639954,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4855820746421815,
                  "rejected_mean_error": 3.099526036262512,
                  "gap_rejected_minus_accepted": 1.6139439616203306
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.752964586019516,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3784328412220852,
                  "rejected_mean_error": 2.450891425815253,
                  "gap_rejected_minus_accepted": 1.072458584593168
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5217496752738953,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1282869549751282,
                  "rejected_mean_error": 2.1656659866333006,
                  "gap_rejected_minus_accepted": 1.0373790316581724
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0576604306697845,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8359833807229234,
                  "rejected_mean_error": 1.9178845147694696,
                  "gap_rejected_minus_accepted": 1.081901134046546
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0975741863250734,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4924642867512172,
                  "rejected_mean_error": 3.1392528438568115,
                  "gap_rejected_minus_accepted": 1.6467885571055942
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7772031426429749,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3779469279044452,
                  "rejected_mean_error": 2.4858684142430625,
                  "gap_rejected_minus_accepted": 1.1079214863386173
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5327438712120056,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1085406374931335,
                  "rejected_mean_error": 2.20574564743042,
                  "gap_rejected_minus_accepted": 1.0972050099372863
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0594216883182526,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8008119028712076,
                  "rejected_mean_error": 1.945639763286407,
                  "gap_rejected_minus_accepted": 1.1448278604151993
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.49691674702919997,
              "spearman": 0.3792901768045135,
              "auroc_top30_bad": 0.5693558095238096,
              "mae": 0.4923135523289442,
              "mse": 0.6612697455707004,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.6275886810673944,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4113510762453079
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9650255909442902
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.046608480989933
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2653668594360352
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6752137190453187,
              "spearman": 0.5411999224319505,
              "auroc_top30_worst": 0.674992761904762,
              "pairwise_seed_ranking": 0.7244,
              "predicted_best_mean_error": 1.6157862251996995,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.045964902758598214,
              "gap_to_oracle": 0.023762293219566466,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9494388997554779
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3128474936462367
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.475961906671524
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.580976877035871
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.912026607990265,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6252860431936051,
                  "rejected_mean_error": 1.9705585794448852,
                  "gap_rejected_minus_accepted": 0.34527253625128007
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7378842532634735,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5808240279889285,
                  "rejected_mean_error": 1.8962763795456565,
                  "gap_rejected_minus_accepted": 0.315452351556728
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4951539635658264,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.475961906671524,
                  "rejected_mean_error": 1.8436646869659423,
                  "gap_rejected_minus_accepted": 0.3677027802944184
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3265364170074463,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3129961582989738,
                  "rejected_mean_error": 1.775665766783178,
                  "gap_rejected_minus_accepted": 0.46266960848420413
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9241523742675781,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6284631530443827,
                  "rejected_mean_error": 1.9613429021835327,
                  "gap_rejected_minus_accepted": 0.33287974913914997
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7425897419452667,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.580739859272452,
                  "rejected_mean_error": 1.902213147708348,
                  "gap_rejected_minus_accepted": 0.32147328843589595
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5131888389587402,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4722396607398986,
                  "rejected_mean_error": 1.8512625951766968,
                  "gap_rejected_minus_accepted": 0.37902293443679813
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3352166712284088,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3409310550916762,
                  "rejected_mean_error": 1.7698348958224537,
                  "gap_rejected_minus_accepted": 0.4289038407307775
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_l2_single_expert"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 78,
        "best_calib_loss": 0.00889547634869814,
        "train_time_sec": 41.69154620170593,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997460987172919,
              "spearman": 0.9986594756876853,
              "auroc_top30_bad": 0.9998468095238096,
              "mae": 0.01959888800922781,
              "mse": 0.0007314499878941157,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8050298721239381,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.00103524149954319
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.199750347417593
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6186728413075209
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9863613034546376
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4164188162431122
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997251231739164,
              "spearman": 0.998951752942045,
              "auroc_top30_worst": 0.9998299047619047,
              "pairwise_seed_ranking": 0.9594,
              "predicted_best_mean_error": 1.703277207672596,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.0911471899449825,
              "gap_to_oracle": 0.0016831599473952075,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7242121315598488
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8797172069311142
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.084006791961193
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3051526755571365
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1365172863006596,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4899324606193436,
                  "rejected_mean_error": 4.441588639259338,
                  "gap_rejected_minus_accepted": 2.9516561786399946
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.013294994831085,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3051526755571365,
                  "rejected_mean_error": 3.224934287261963,
                  "gap_rejected_minus_accepted": 1.9197816117048263
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4971967339515686,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.084006791961193,
                  "rejected_mean_error": 2.4861893650054934,
                  "gap_rejected_minus_accepted": 1.4021825730443003
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0708536505699158,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8797172069311142,
                  "rejected_mean_error": 2.086891702334086,
                  "gap_rejected_minus_accepted": 1.2071744954029717
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2010728120803833,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.491615736650096,
                  "rejected_mean_error": 4.51970234632492,
                  "gap_rejected_minus_accepted": 3.0280866096748245
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.021999716758728,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.302068968017896,
                  "rejected_mean_error": 3.2714906864166258,
                  "gap_rejected_minus_accepted": 1.9694217183987297
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4891793727874756,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.076658120214939,
                  "rejected_mean_error": 2.512190675020218,
                  "gap_rejected_minus_accepted": 1.4355325548052789
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0699223279953003,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8668974953889846,
                  "rejected_mean_error": 2.1036000316937766,
                  "gap_rejected_minus_accepted": 1.2367025363047919
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.993399621548472,
              "spearman": 0.9879760298590736,
              "auroc_top30_bad": 0.9930994285714286,
              "mae": 0.09739113006880507,
              "mse": 0.01875276603896577,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.976,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9156164166015845,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06855963206291199
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1854322709798813
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5845779894471168
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0191527173757553
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5154402160465716
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.993491493893794,
              "spearman": 0.9942089752377443,
              "auroc_top30_worst": 0.9980586666666666,
              "pairwise_seed_ranking": 0.9184,
              "predicted_best_mean_error": 1.9948832414150237,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10959776329994231,
              "gap_to_oracle": 0.005988011717796171,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6189584782123566
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8653942143114713
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.224104313993454
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5531972998431496
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.1563235282897955,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8419778807693057,
                  "rejected_mean_error": 4.22118231010437,
                  "gap_rejected_minus_accepted": 2.379204429335065
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8416121006011963,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5518085825214263,
                  "rejected_mean_error": 3.6607931719039577,
                  "gap_rejected_minus_accepted": 2.1089845893825316
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8690115213394165,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.224104313993454,
                  "rejected_mean_error": 2.9356923334121703,
                  "gap_rejected_minus_accepted": 1.7115880194187163
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2633423209190369,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8669269567670913,
                  "rejected_mean_error": 2.4850851303739763,
                  "gap_rejected_minus_accepted": 1.618158173606885
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.192476081848144,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8657502100202772,
                  "rejected_mean_error": 4.253058156967163,
                  "gap_rejected_minus_accepted": 2.387307946946886
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.8906949758529663,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5583100063915558,
                  "rejected_mean_error": 3.7256552378336587,
                  "gap_rejected_minus_accepted": 2.167345231442103
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8874521255493164,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2231953601837158,
                  "rejected_mean_error": 2.985766649246216,
                  "gap_rejected_minus_accepted": 1.7625712890625
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2811228930950165,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8638620717184884,
                  "rejected_mean_error": 2.5224435329437256,
                  "gap_rejected_minus_accepted": 1.6585814612252372
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9920589376538671,
              "spearman": 0.9887344465882244,
              "auroc_top30_bad": 0.9895954285714286,
              "mae": 0.08359861172679811,
              "mse": 0.014093034542681985,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.976,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7862037781182125,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.03792508715391159
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18127226095199586
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6264072492957116
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0406593424717585
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.404149471873045
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9898833265661682,
              "spearman": 0.9894396246013599,
              "auroc_top30_worst": 0.9829211428571428,
              "pairwise_seed_ranking": 0.8932,
              "predicted_best_mean_error": 1.5876081252098084,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.0695350172519682,
              "gap_to_oracle": 0.00771060371398935,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4005154540538788
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.653857766626737
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0247182734489442
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3062752470660057
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8562727212905887,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4596455127398174,
                  "rejected_mean_error": 3.3329550933837893,
                  "gap_rejected_minus_accepted": 1.873309580643972
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.073930501937866,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3054922828679405,
                  "rejected_mean_error": 2.669247027022389,
                  "gap_rejected_minus_accepted": 1.3637547441544486
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7210428714752197,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0247182734489442,
                  "rejected_mean_error": 2.269234668159485,
                  "gap_rejected_minus_accepted": 1.2445163947105409
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0985914170742035,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6551485737672629,
                  "rejected_mean_error": 1.9782914460150638,
                  "gap_rejected_minus_accepted": 1.323142872247801
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9579549789428703,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4644762629932828,
                  "rejected_mean_error": 3.3911450576782225,
                  "gap_rejected_minus_accepted": 1.9266687946849397
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0913177132606506,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.303285054663286,
                  "rejected_mean_error": 2.7074838157684082,
                  "gap_rejected_minus_accepted": 1.4041987611051223
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7491983771324158,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0151230416297912,
                  "rejected_mean_error": 2.299163243293762,
                  "gap_rejected_minus_accepted": 1.284040201663971
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1082502901554108,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6435922592405289,
                  "rejected_mean_error": 1.9986068090015554,
                  "gap_rejected_minus_accepted": 1.3550145497610266
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9902968906052256,
              "spearman": 0.9807813404661164,
              "auroc_top30_bad": 0.9796944761904762,
              "mae": 0.07833639755193145,
              "mse": 0.01273334281895557,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7257634343940825,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06517896282672882
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2148857876777649
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.782782702922821
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1371951855977376
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.419131818675995
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9756054275015129,
              "spearman": 0.9559139209689095,
              "auroc_top30_worst": 0.9511619047619049,
              "pairwise_seed_ranking": 0.9204,
              "predicted_best_mean_error": 1.5974787237644195,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06427240419387825,
              "gap_to_oracle": 0.005454791784286428,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8448193819522858
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1014491805854516
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3609438917636871
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.522073262821891
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0490665912628176,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5930292468865712,
                  "rejected_mean_error": 2.260869746208191,
                  "gap_rejected_minus_accepted": 0.6678404993216196
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8794572949409485,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5217351443039824,
                  "rejected_mean_error": 2.0731654658485144,
                  "gap_rejected_minus_accepted": 0.551430321544532
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7323716282844543,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3609438917636871,
                  "rejected_mean_error": 1.9586827018737794,
                  "gap_rejected_minus_accepted": 0.5977388101100922
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4441336393356323,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1024495745047975,
                  "rejected_mean_error": 1.845997763290731,
                  "gap_rejected_minus_accepted": 0.7435481887859334
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0533592224121096,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5975362843937344,
                  "rejected_mean_error": 2.2396847200393677,
                  "gap_rejected_minus_accepted": 0.6421484356456333
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8788681328296661,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.530388152854328,
                  "rejected_mean_error": 2.0516698000923035,
                  "gap_rejected_minus_accepted": 0.5212816472379755
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7415492534637451,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.374139304637909,
                  "rejected_mean_error": 1.9493629512786865,
                  "gap_rejected_minus_accepted": 0.5752236466407776
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.467287689447403,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1135321202732267,
                  "rejected_mean_error": 1.8464452321516638,
                  "gap_rejected_minus_accepted": 0.7329131118784371
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_l2_single_expert"
      }
    ],
    "target_chunk_min_l2_K10": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 20,
        "best_calib_loss": 0.08379558473825455,
        "train_time_sec": 12.376439809799194,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9102408020765386,
              "spearman": 0.8187400022109159,
              "auroc_top30_bad": 0.8912435238095239,
              "mae": 0.20671004591217498,
              "mse": 0.19775008567357405,
              "expert_lt_perturb_large": 0.986,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.978,
              "same_context_pred_std": 0.7460610877809432,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5250259809456765
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5464822714810725
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6970497848852305
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9883581268036583
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3885712516240194
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9977229017177149,
              "spearman": 0.9938823881148552,
              "auroc_top30_worst": 0.9981697142857142,
              "pairwise_seed_ranking": 0.7971,
              "predicted_best_mean_error": 1.6945197366774083,
              "seed0_mean_error": 1.7723370801210403,
              "random_seed_mean_error": 1.7639946495592593,
              "oracle_best_mean_error": 1.6821038286685943,
              "improvement_over_seed0": 0.077817343443632,
              "gap_to_oracle": 0.01241590800881398,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6893386963009834
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8447829836606979
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0559256119847298
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2807139010190964
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.762259884315729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.071090626716614,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4654647891322772,
                  "rejected_mean_error": 4.4334157409667965,
                  "gap_rejected_minus_accepted": 2.9679509518345193
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0008265376091003,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2807139010190964,
                  "rejected_mean_error": 3.2068978342056274,
                  "gap_rejected_minus_accepted": 1.926183933186531
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.454651415348053,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0559256119847298,
                  "rejected_mean_error": 2.4685941566467284,
                  "gap_rejected_minus_accepted": 1.4126685446619986
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0560074746608734,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8447829836606979,
                  "rejected_mean_error": 2.0680855178674062,
                  "gap_rejected_minus_accepted": 1.2233025342067083
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.163601541519165,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4681127239598168,
                  "rejected_mean_error": 4.510356285572052,
                  "gap_rejected_minus_accepted": 3.042243561612235
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0303250551223755,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2787631384531657,
                  "rejected_mean_error": 3.2530589051246643,
                  "gap_rejected_minus_accepted": 1.9742957666714986
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4505711793899536,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0513585686683655,
                  "rejected_mean_error": 2.4933155915737153,
                  "gap_rejected_minus_accepted": 1.4419570229053498
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0588311851024628,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8353021438121796,
                  "rejected_mean_error": 2.0846820588906607,
                  "gap_rejected_minus_accepted": 1.2493799150784812
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8356013134313609,
              "spearman": 0.7373622547447785,
              "auroc_top30_bad": 0.8069268571428571,
              "mae": 0.4367890286497772,
              "mse": 0.4411960405077622,
              "expert_lt_perturb_large": 0.984,
              "expert_lt_other_task": 0.516,
              "expert_lt_simvla_seed0": 0.936,
              "same_context_pred_std": 0.8951968379027522,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4914632236137986
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6603238117963076
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7418200328692793
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0873511099030575
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.491789175183326
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8450611041295575,
              "spearman": 0.7847620868877356,
              "auroc_top30_worst": 0.8703542857142856,
              "pairwise_seed_ranking": 0.702,
              "predicted_best_mean_error": 1.997901482462883,
              "seed0_mean_error": 2.085954474210739,
              "random_seed_mean_error": 2.0572379875183104,
              "oracle_best_mean_error": 1.9730187737941742,
              "improvement_over_seed0": 0.0880529917478563,
              "gap_to_oracle": 0.024882708668708675,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2461973302364349
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1132036217321188
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3963880355834961
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5834813827136431
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.060303539466858
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.31798849105835,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.823558401107788,
                  "rejected_mean_error": 4.191009784698486,
                  "gap_rejected_minus_accepted": 2.367451383590698
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7533665895462036,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5828474720615968,
                  "rejected_mean_error": 3.4896209041912334,
                  "gap_rejected_minus_accepted": 1.9067734321296366
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.778598666191101,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3963880355834961,
                  "rejected_mean_error": 2.7242190433502196,
                  "gap_rejected_minus_accepted": 1.3278310077667235
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2245832681655884,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1139546003394996,
                  "rejected_mean_error": 2.376426504191365,
                  "gap_rejected_minus_accepted": 1.2624719038518655
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.345195007324219,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8472323817676968,
                  "rejected_mean_error": 4.23445330619812,
                  "gap_rejected_minus_accepted": 2.387220924430424
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7826457619667053,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5962070650595395,
                  "rejected_mean_error": 3.5396491648658874,
                  "gap_rejected_minus_accepted": 1.943442099806348
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8056105971336365,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4213848943710328,
                  "rejected_mean_error": 2.7505240540504454,
                  "gap_rejected_minus_accepted": 1.3291391596794127
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2307315170764923,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0913817939304171,
                  "rejected_mean_error": 2.421024414626035,
                  "gap_rejected_minus_accepted": 1.3296426206956178
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6678820051264798,
              "spearman": 0.5711487225139967,
              "auroc_top30_bad": 0.6718872380952381,
              "mae": 0.47912499461378905,
              "mse": 0.5733900130911433,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.488,
              "expert_lt_simvla_seed0": 0.944,
              "same_context_pred_std": 0.6369205397356322,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8474640322253107
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7611756004072726
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8648934891123324
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1024204904449484
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3750692298272624
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8305984748696944,
              "spearman": 0.7677901607617029,
              "auroc_top30_worst": 0.8196327619047618,
              "pairwise_seed_ranking": 0.78,
              "predicted_best_mean_error": 1.5810955513715743,
              "seed0_mean_error": 1.6361434885263444,
              "random_seed_mean_error": 1.6260707788467408,
              "oracle_best_mean_error": 1.561017747759819,
              "improvement_over_seed0": 0.05504793715477008,
              "gap_to_oracle": 0.020077803611755263,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4230065567493439
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8333900019717522
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0920729344844817
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3311790918935336
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6248770711660385
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1132959365844735,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4454257785744138,
                  "rejected_mean_error": 3.239938704490662,
                  "gap_rejected_minus_accepted": 1.794512925916248
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7929375171661377,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3300100227493867,
                  "rejected_mean_error": 2.5075940819213183,
                  "gap_rejected_minus_accepted": 1.1775840591719315
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4910297989845276,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0920729344844817,
                  "rejected_mean_error": 2.1576812078475953,
                  "gap_rejected_minus_accepted": 1.0656082733631136
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9181938618421555,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8387913436364061,
                  "rejected_mean_error": 1.88746493959376,
                  "gap_rejected_minus_accepted": 1.0486735959573539
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1536535263061523,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4526022175947826,
                  "rejected_mean_error": 3.2880149269104004,
                  "gap_rejected_minus_accepted": 1.8354127093156178
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8877802789211273,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3221656398020964,
                  "rejected_mean_error": 2.5681094839459373,
                  "gap_rejected_minus_accepted": 1.2459438441438409
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5023987889289856,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0798692200183868,
                  "rejected_mean_error": 2.1924177570343018,
                  "gap_rejected_minus_accepted": 1.112548537015915
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9080334901809692,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7936337850396595,
                  "rejected_mean_error": 1.9199836560111632,
                  "gap_rejected_minus_accepted": 1.1263498709715036
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5292661069200675,
              "spearman": 0.4122562638185201,
              "auroc_top30_bad": 0.5881851428571429,
              "mae": 0.4456158731892705,
              "mse": 0.5388951201732519,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.528,
              "expert_lt_simvla_seed0": 0.984,
              "same_context_pred_std": 0.6009528712975243,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.944321970127523
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9258373366564512
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.00646147903502
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2207368615011374
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3756778576776385
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6744590354678517,
              "spearman": 0.5133378537842265,
              "auroc_top30_worst": 0.6662887619047619,
              "pairwise_seed_ranking": 0.7036,
              "predicted_best_mean_error": 1.5754119256734849,
              "seed0_mean_error": 1.6154204576015472,
              "random_seed_mean_error": 1.6203936924934388,
              "oracle_best_mean_error": 1.5515936243534088,
              "improvement_over_seed0": 0.04000853192806231,
              "gap_to_oracle": 0.02381830132007612,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7911110060214996
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.244833232787175
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4228567822933198
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5348338975009126
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6173568556547164
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9028980135917664,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.582047885020574,
                  "rejected_mean_error": 1.9351375913619995,
                  "gap_rejected_minus_accepted": 0.35308970634142556
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7725213468074799,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5340202959968035,
                  "rejected_mean_error": 1.8668340326498112,
                  "gap_rejected_minus_accepted": 0.33281373665300773
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5673372149467468,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4228567822933198,
                  "rejected_mean_error": 1.8118569290161133,
                  "gap_rejected_minus_accepted": 0.3890001467227935
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3147999048233032,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2446412772606736,
                  "rejected_mean_error": 1.7418605654064085,
                  "gap_rejected_minus_accepted": 0.4972192881457349
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8968974828720093,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.580754725403256,
                  "rejected_mean_error": 1.9274120473861693,
                  "gap_rejected_minus_accepted": 0.34665732198291344
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7817532122135162,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5272172284636267,
                  "rejected_mean_error": 1.8772300425029935,
                  "gap_rejected_minus_accepted": 0.3500128140393668
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5821004509925842,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4042665143013,
                  "rejected_mean_error": 1.8265744009017943,
                  "gap_rejected_minus_accepted": 0.42230788660049434
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.340517520904541,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2249278937067305,
                  "rejected_mean_error": 1.7469767759190524,
                  "gap_rejected_minus_accepted": 0.5220488822123219
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K10"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 73,
        "best_calib_loss": 0.013963717967271805,
        "train_time_sec": 37.792290687561035,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9996426540494111,
              "spearman": 0.99891404581506,
              "auroc_top30_bad": 0.999675238095238,
              "mae": 0.028207344087550882,
              "mse": 0.0013344956250019042,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.99,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7743962304374741,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07654740119667258
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22629120509303174
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5982471390350489
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9590640060493567
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3885712516240194
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997347447038026,
              "spearman": 0.9993351624373744,
              "auroc_top30_worst": 0.9998624761904762,
              "pairwise_seed_ranking": 0.944,
              "predicted_best_mean_error": 1.6840144752562045,
              "seed0_mean_error": 1.7723370801210403,
              "random_seed_mean_error": 1.7639946495592593,
              "oracle_best_mean_error": 1.6821038286685943,
              "improvement_over_seed0": 0.08832260486483579,
              "gap_to_oracle": 0.0019106465876101986,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6821076237559318
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8412122560739517
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0537457179188727
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2794241635084151
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.762259884315729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.092050957679749,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.465236219200823,
                  "rejected_mean_error": 4.4354728703498845,
                  "gap_rejected_minus_accepted": 2.9702366511490617
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.987828552722931,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2794241635084151,
                  "rejected_mean_error": 3.2107670467376708,
                  "gap_rejected_minus_accepted": 1.9313428832292556
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4664391875267029,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0537457179188727,
                  "rejected_mean_error": 2.4707740507125853,
                  "gap_rejected_minus_accepted": 1.4170283327937125
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0360807180404663,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8412122560739517,
                  "rejected_mean_error": 2.0692757603963217,
                  "gap_rejected_minus_accepted": 1.22806350432237
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1637997388839723,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.467803936402003,
                  "rejected_mean_error": 4.513135373592377,
                  "gap_rejected_minus_accepted": 3.0453314371903737
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9882771670818329,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2777449466387432,
                  "rejected_mean_error": 3.256113480567932,
                  "gap_rejected_minus_accepted": 1.978368533929189
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4610885381698608,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.049101357936859,
                  "rejected_mean_error": 2.4955728023052215,
                  "gap_rejected_minus_accepted": 1.4464714443683624
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0346125066280365,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8333487930297852,
                  "rejected_mean_error": 2.0853331758181253,
                  "gap_rejected_minus_accepted": 1.2519843827883401
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9893428709681885,
              "spearman": 0.9808875996779389,
              "auroc_top30_bad": 0.9903710476190476,
              "mae": 0.12449220552407204,
              "mse": 0.03442679232860097,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9296534103808034,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.12053562846779824
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2260993090569973
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5736335828915239
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9976129806607962
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.491789175183326
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.990475134549884,
              "spearman": 0.9929170939629403,
              "auroc_top30_worst": 0.9963337142857143,
              "pairwise_seed_ranking": 0.9172,
              "predicted_best_mean_error": 1.976790597319603,
              "seed0_mean_error": 2.085954474210739,
              "random_seed_mean_error": 2.0572379875183104,
              "oracle_best_mean_error": 1.9730187737941742,
              "improvement_over_seed0": 0.10916387689113627,
              "gap_to_oracle": 0.003771823525428708,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6046578855514526
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8499302634826074
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2042016298294067
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5301538502483734
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.060303539466858
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.302123546600342,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.821832228342692,
                  "rejected_mean_error": 4.20654533958435,
                  "gap_rejected_minus_accepted": 2.384713111241658
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.872239410877228,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5291534172432655,
                  "rejected_mean_error": 3.650359975644194,
                  "gap_rejected_minus_accepted": 2.121206558400928
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8317038416862488,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2042016298294067,
                  "rejected_mean_error": 2.916405449104309,
                  "gap_rejected_minus_accepted": 1.7122038192749023
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2034767866134644,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8508153319739686,
                  "rejected_mean_error": 2.4643268147553044,
                  "gap_rejected_minus_accepted": 1.6135114827813357
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.354382562637329,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8463601650132073,
                  "rejected_mean_error": 4.242303256988525,
                  "gap_rejected_minus_accepted": 2.395943091975318
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.97188800573349,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5369188285128956,
                  "rejected_mean_error": 3.715631708266243,
                  "gap_rejected_minus_accepted": 2.1787128797533475
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8489846587181091,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2069825587272645,
                  "rejected_mean_error": 2.964926389694214,
                  "gap_rejected_minus_accepted": 1.7579438309669495
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2040996253490448,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8590049204372224,
                  "rejected_mean_error": 2.4993118105087686,
                  "gap_rejected_minus_accepted": 1.640306890071546
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9885855125809536,
              "spearman": 0.979932068643653,
              "auroc_top30_bad": 0.9787386666666666,
              "mae": 0.10761179445181042,
              "mse": 0.0192556170104134,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7470088847084357,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1265390543974936
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22407803215160965
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6044248202044517
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0162022562476496
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3750692298272624
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9879503418309935,
              "spearman": 0.9836325086928057,
              "auroc_top30_worst": 0.9769081904761905,
              "pairwise_seed_ranking": 0.8736,
              "predicted_best_mean_error": 1.570088817000389,
              "seed0_mean_error": 1.6361434885263444,
              "random_seed_mean_error": 1.6260707788467408,
              "oracle_best_mean_error": 1.561017747759819,
              "improvement_over_seed0": 0.06605467152595534,
              "gap_to_oracle": 0.009071069240569996,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3933199100494385
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6068640711406866
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9949723351955414
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.282071261994366
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6248770711660385
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7270757675170905,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4359764035277895,
                  "rejected_mean_error": 3.3249830799102784,
                  "gap_rejected_minus_accepted": 1.8890066763824889
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0711042284965515,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2813515773514164,
                  "rejected_mean_error": 2.653258501531217,
                  "gap_rejected_minus_accepted": 1.3719069241798008
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.670648992061615,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.9949723351955414,
                  "rejected_mean_error": 2.2547818071365358,
                  "gap_rejected_minus_accepted": 1.2598094719409945
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0392627716064453,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6077812745357855,
                  "rejected_mean_error": 1.9646326574470088,
                  "gap_rejected_minus_accepted": 1.3568513829112234
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.938938522338867,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4425084343221453,
                  "rejected_mean_error": 3.378858976364136,
                  "gap_rejected_minus_accepted": 1.9363505420419906
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.098282516002655,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.279560895686481,
                  "rejected_mean_error": 2.694571184733557,
                  "gap_rejected_minus_accepted": 1.4150102890470762
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6822434067726135,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.9862388460636139,
                  "rejected_mean_error": 2.286048130989075,
                  "gap_rejected_minus_accepted": 1.2998092849254608
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0394324362277985,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.5912648661742135,
                  "rejected_mean_error": 1.9881614201209123,
                  "gap_rejected_minus_accepted": 1.3968965539466989
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9852727803653405,
              "spearman": 0.9715708332648673,
              "auroc_top30_bad": 0.9706201904761904,
              "mae": 0.09860239048264921,
              "mse": 0.0177340538305735,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7046242711493352,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10577065666019916
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23675851380228996
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7417780532687902
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1018063143948713
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3756778576776385
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9557571371666448,
              "spearman": 0.9301358001509122,
              "auroc_top30_worst": 0.9390872380952382,
              "pairwise_seed_ranking": 0.9052,
              "predicted_best_mean_error": 1.556567700266838,
              "seed0_mean_error": 1.6154204576015472,
              "random_seed_mean_error": 1.6203936924934388,
              "oracle_best_mean_error": 1.5515936243534088,
              "improvement_over_seed0": 0.05885275733470907,
              "gap_to_oracle": 0.004974075913429354,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7169289381504059
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0186075311249647
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.299802605199814
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4769693935540185
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6173568556547164
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.03799741268158,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5560365356604258,
                  "rejected_mean_error": 2.1692397356033326,
                  "gap_rejected_minus_accepted": 0.6132031999429068
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.881699025630951,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4766724019002253,
                  "rejected_mean_error": 2.038511274721676,
                  "gap_rejected_minus_accepted": 0.5618388728214505
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6911949515342712,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.299802605199814,
                  "rejected_mean_error": 1.9349111061096191,
                  "gap_rejected_minus_accepted": 0.6351085009098052
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4180583953857422,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0200289745871631,
                  "rejected_mean_error": 1.816891142500121,
                  "gap_rejected_minus_accepted": 0.7968621679129579
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0306397914886474,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5551536128256056,
                  "rejected_mean_error": 2.157822060585022,
                  "gap_rejected_minus_accepted": 0.6026684477594162
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8634229898452759,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4800165136230183,
                  "rejected_mean_error": 2.017333751633054,
                  "gap_rejected_minus_accepted": 0.5373172380100355
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7120500802993774,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3027654013633727,
                  "rejected_mean_error": 1.9280755138397216,
                  "gap_rejected_minus_accepted": 0.6253101124763489
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4520423710346222,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.018577656102559,
                  "rejected_mean_error": 1.8164958399247357,
                  "gap_rejected_minus_accepted": 0.7979181838221767
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K10"
      }
    ],
    "target_chunk_softmin_l2_K10": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 67,
        "best_calib_loss": 0.08588895946741104,
        "train_time_sec": 14.691543817520142,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8917623459769578,
              "spearman": 0.7547393580167582,
              "auroc_top30_bad": 0.8240838095238094,
              "mae": 0.23415957726414505,
              "mse": 0.22211965848348264,
              "expert_lt_perturb_large": 0.994,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.993,
              "same_context_pred_std": 0.6813239522497727,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1996755505055189
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21446546174287795
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.25284320455789566
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.5068674916625023
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8960445861935615
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9986417371056575,
              "spearman": 0.996469216314684,
              "auroc_top30_worst": 0.9988066666666667,
              "pairwise_seed_ranking": 0.8734,
              "predicted_best_mean_error": 1.1905370975136758,
              "seed0_mean_error": 1.273960811495781,
              "random_seed_mean_error": 1.2650585584044456,
              "oracle_best_mean_error": 1.185694094002247,
              "improvement_over_seed0": 0.08342371398210524,
              "gap_to_oracle": 0.004843003511428856,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.22000795862078668
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3618604325652123
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5711775893986225
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7894275937438011
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2635830781012773
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.569933843612673,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9717589207788309,
                  "rejected_mean_error": 3.8900004940032957,
                  "gap_rejected_minus_accepted": 2.918241573224465
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4730606973171234,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7894275937438011,
                  "rejected_mean_error": 2.686049531173706,
                  "gap_rejected_minus_accepted": 1.896621937429905
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9861084520816803,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5711775893986225,
                  "rejected_mean_error": 1.9559885668039323,
                  "gap_rejected_minus_accepted": 1.38481097740531
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5528012812137604,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.3618604325652123,
                  "rejected_mean_error": 1.5641572932799657,
                  "gap_rejected_minus_accepted": 1.2022968607147533
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6125142097473155,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.9745248870054881,
                  "rejected_mean_error": 3.9688841319084167,
                  "gap_rejected_minus_accepted": 2.9943592449029284
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4824278950691223,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7877849666277568,
                  "rejected_mean_error": 2.7324883460998537,
                  "gap_rejected_minus_accepted": 1.944703379472097
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9786365330219269,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5665049036741256,
                  "rejected_mean_error": 1.9814167193174361,
                  "gap_rejected_minus_accepted": 1.4149118156433105
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5504392683506012,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.3565543122291565,
                  "rejected_mean_error": 1.5797629779179891,
                  "gap_rejected_minus_accepted": 1.2232086656888326
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.840690730997508,
              "spearman": 0.7254232313324794,
              "auroc_top30_bad": 0.783336,
              "mae": 0.4521047692517028,
              "mse": 0.40907603553701966,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.8555923902650002,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0392601347565651
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22073613402843476
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.2553000477850437
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.5760860574920972
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.9921554976791144
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8682862871791259,
              "spearman": 0.8116550802272515,
              "auroc_top30_worst": 0.8911116190476189,
              "pairwise_seed_ranking": 0.79,
              "predicted_best_mean_error": 1.488690579175949,
              "seed0_mean_error": 1.583361796617508,
              "random_seed_mean_error": 1.5554273549318314,
              "oracle_best_mean_error": 1.472350873351097,
              "improvement_over_seed0": 0.09467121744155893,
              "gap_to_oracle": 0.016339705824852002,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5586845977306366
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6335077805396838
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8588987847805023
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0888879405282963
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5582412529468537
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.858608627319336,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3265669632487826,
                  "rejected_mean_error": 3.643309860229492,
                  "gap_rejected_minus_accepted": 2.3167428969807093
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2784851789474487,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.088619659842651,
                  "rejected_mean_error": 2.9641052553067193,
                  "gap_rejected_minus_accepted": 1.8754855954640683
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4317266941070557,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.8588987847805023,
                  "rejected_mean_error": 2.257583721113205,
                  "gap_rejected_minus_accepted": 1.3986849363327027
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7319297194480896,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6348797856047511,
                  "rejected_mean_error": 1.8666853717068088,
                  "gap_rejected_minus_accepted": 1.2318055861020576
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.886617660522461,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.3508099675178529,
                  "rejected_mean_error": 3.6763282585144044,
                  "gap_rejected_minus_accepted": 2.3255182909965515
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3548662662506104,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.0994277998087878,
                  "rejected_mean_error": 3.019800803017995,
                  "gap_rejected_minus_accepted": 1.920373003209207
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4428397417068481,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.862064868927002,
                  "rejected_mean_error": 2.304658724308014,
                  "gap_rejected_minus_accepted": 1.4425938553810118
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7874003201723099,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6323000419707525,
                  "rejected_mean_error": 1.903772975990479,
                  "gap_rejected_minus_accepted": 1.2714729340197264
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6434513095264729,
              "spearman": 0.5018144005766203,
              "auroc_top30_bad": 0.6135508571428572,
              "mae": 0.4834502189745901,
              "mse": 0.5285372884576703,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.472,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5784234003095896,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4822282210588455
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5513094354391098
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.41602526378631594
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6176962884744008
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8829198032021522
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8373127003121963,
              "spearman": 0.7946841187098361,
              "auroc_top30_worst": 0.8356723809523809,
              "pairwise_seed_ranking": 0.806,
              "predicted_best_mean_error": 1.0760646650791168,
              "seed0_mean_error": 1.1370457689762115,
              "random_seed_mean_error": 1.128170433998108,
              "oracle_best_mean_error": 1.0650475682020188,
              "improvement_over_seed0": 0.06098110389709466,
              "gap_to_oracle": 0.011017096877097954,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.009223638772964478
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3022949845553973
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6033291526794433
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8514927238670748
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1261739067554475
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6421936988830577,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.9512305436134338,
                  "rejected_mean_error": 2.700664175033569,
                  "gap_rejected_minus_accepted": 1.7494336314201353
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3498581051826477,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 0.8511176511979281,
                  "rejected_mean_error": 1.9495851254691712,
                  "gap_rejected_minus_accepted": 1.098467474271243
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0958740711212158,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.6033291526794433,
                  "rejected_mean_error": 1.6490186608314514,
                  "gap_rejected_minus_accepted": 1.0456895081520081
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.58692766726017,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.3027701927259707,
                  "rejected_mean_error": 1.4012276554120389,
                  "gap_rejected_minus_accepted": 1.0984574626860681
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.719149100780487,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 0.9504224191771613,
                  "rejected_mean_error": 2.8166559171676635,
                  "gap_rejected_minus_accepted": 1.8662334979905022
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3979186415672302,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 0.8447929913984901,
                  "rejected_mean_error": 2.0045262357545277,
                  "gap_rejected_minus_accepted": 1.1597332443560378
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.105220913887024,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.5916339073181153,
                  "rejected_mean_error": 1.6824576306343078,
                  "gap_rejected_minus_accepted": 1.0908237233161926
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5663893073797226,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.3041038319231972,
                  "rejected_mean_error": 1.4176625712988848,
                  "gap_rejected_minus_accepted": 1.1135587393756876
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5235225381299743,
              "spearman": 0.39179304665224146,
              "auroc_top30_bad": 0.5587184761904761,
              "mae": 0.45480208553775375,
              "mse": 0.5096341142146835,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5583320411034506,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5132013903260231
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5714871632814408
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5211243295073509
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7403707830031713
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8961791918218136
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6632588947134094,
              "spearman": 0.5457283973941743,
              "auroc_top30_worst": 0.6823984761904762,
              "pairwise_seed_ranking": 0.7624,
              "predicted_best_mean_error": 1.0805478010177612,
              "seed0_mean_error": 1.1303126678466797,
              "random_seed_mean_error": 1.1341348474025725,
              "oracle_best_mean_error": 1.0674733737707138,
              "improvement_over_seed0": 0.049764866828918564,
              "gap_to_oracle": 0.013074427247047327,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3755817028284073
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7622553017945626
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.935854153418541
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.055966867678074
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1312655336737634
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.4589473366737367,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1088998976680968,
                  "rejected_mean_error": 1.332556257724762,
                  "gap_rejected_minus_accepted": 0.22365636005666523
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3267719447612762,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.0555870600259418,
                  "rejected_mean_error": 1.3578173860955163,
                  "gap_rejected_minus_accepted": 0.30223032606957445
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0752683281898499,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.935854153418541,
                  "rejected_mean_error": 1.3266769139289856,
                  "gap_rejected_minus_accepted": 0.3908227605104446
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8433835655450821,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.76164531798218,
                  "rejected_mean_error": 1.2547352535365868,
                  "gap_rejected_minus_accepted": 0.4930899355544067
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.4771259546279907,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.1114856884214612,
                  "rejected_mean_error": 1.299755482673645,
                  "gap_rejected_minus_accepted": 0.18826979425218382
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3337010145187378,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.0543178418740868,
                  "rejected_mean_error": 1.355884611606598,
                  "gap_rejected_minus_accepted": 0.30156676973251106
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.094509482383728,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.9271493573188782,
                  "rejected_mean_error": 1.3334759783744812,
                  "gap_rejected_minus_accepted": 0.406326621055603
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8540908247232437,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7726562051546007,
                  "rejected_mean_error": 1.2508065563472197,
                  "gap_rejected_minus_accepted": 0.47815035119261906
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_softmin_l2_K10"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 55,
        "best_calib_loss": 0.025025125592947006,
        "train_time_sec": 47.21606135368347,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9927565999597447,
              "spearman": 0.9906925459147579,
              "auroc_top30_bad": 0.9998213809523809,
              "mae": 0.0874757827410911,
              "mse": 0.023074285410946322,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.935,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6619057999280781,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.2995387224853039
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.24681846296191215
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.1268437145113945
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.47744503531455995
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8960445861935615
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9996676754032654,
              "spearman": 0.9992912219636318,
              "auroc_top30_worst": 0.9998575238095239,
              "pairwise_seed_ranking": 0.9429,
              "predicted_best_mean_error": 1.1869409334659577,
              "seed0_mean_error": 1.273960811495781,
              "random_seed_mean_error": 1.2650585584044456,
              "oracle_best_mean_error": 1.185694094002247,
              "improvement_over_seed0": 0.08701987802982325,
              "gap_to_oracle": 0.001246839463710847,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.21460979023575782
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3596050325989723
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5699583791553974
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7889269640962283
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2635830781012773
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5611264705657963,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9715039797392157,
                  "rejected_mean_error": 3.892294963359833,
                  "gap_rejected_minus_accepted": 2.920790983620617
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4708872437477112,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7889269640962283,
                  "rejected_mean_error": 2.6875514201164243,
                  "gap_rejected_minus_accepted": 1.8986244560201961
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9567722082138062,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5699583791553974,
                  "rejected_mean_error": 1.9572077770471572,
                  "gap_rejected_minus_accepted": 1.3872493978917597
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5425587445497513,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.3596050325989723,
                  "rejected_mean_error": 1.5649090932687124,
                  "gap_rejected_minus_accepted": 1.20530406066974
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.63854730129242,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.9742602002620697,
                  "rejected_mean_error": 3.971266312599182,
                  "gap_rejected_minus_accepted": 2.9970061123371123
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4857926964759827,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7868924571673075,
                  "rejected_mean_error": 2.735165874481201,
                  "gap_rejected_minus_accepted": 1.9482734173138936
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9497193098068237,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.565590503334999,
                  "rejected_mean_error": 1.9823311196565627,
                  "gap_rejected_minus_accepted": 1.4167406163215637
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5380612909793854,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.3543314156532288,
                  "rejected_mean_error": 1.5805039434432984,
                  "gap_rejected_minus_accepted": 1.2261725277900695
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.980068972845711,
              "spearman": 0.9714962667994028,
              "auroc_top30_bad": 0.9910666666666667,
              "mae": 0.18454853217839262,
              "mse": 0.06100371861002855,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.916,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.818625347551666,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.2667497269809246
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.26203858124017715
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.09851371776461601
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.509526921347777
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.9921554976791144
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.986095805682304,
              "spearman": 0.9894664923305553,
              "auroc_top30_worst": 0.9948099047619048,
              "pairwise_seed_ranking": 0.92,
              "predicted_best_mean_error": 1.4754318132400512,
              "seed0_mean_error": 1.583361796617508,
              "random_seed_mean_error": 1.5554273549318314,
              "oracle_best_mean_error": 1.472350873351097,
              "improvement_over_seed0": 0.10792998337745674,
              "gap_to_oracle": 0.003080939888954193,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1020898175239563
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.37787875284751254
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7306306412696838
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0449671017716942
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5582412529468537
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8225186824798585,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3277260782983569,
                  "rejected_mean_error": 3.6328778247833253,
                  "gap_rejected_minus_accepted": 2.3051517464849685
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4325416684150696,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.0438683846589722,
                  "rejected_mean_error": 3.098073130217604,
                  "gap_rejected_minus_accepted": 2.054204745558632
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.336520791053772,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.7306306412696838,
                  "rejected_mean_error": 2.3858518646240237,
                  "gap_rejected_minus_accepted": 1.65522122335434
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.763772651553154,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.3794878521285499,
                  "rejected_mean_error": 1.9519977251519007,
                  "gap_rejected_minus_accepted": 1.5725098730233509
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.900518536567688,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.3526963374349805,
                  "rejected_mean_error": 3.659350929260254,
                  "gap_rejected_minus_accepted": 2.306654591825273
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4791805148124695,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.0504507371448577,
                  "rejected_mean_error": 3.1651771636236283,
                  "gap_rejected_minus_accepted": 2.1147264264787706
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3621066212654114,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.7304048190116882,
                  "rejected_mean_error": 2.4363187742233277,
                  "gap_rejected_minus_accepted": 1.7059139552116394
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7607047408819199,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.38387015130784774,
                  "rejected_mean_error": 1.987468607604185,
                  "gap_rejected_minus_accepted": 1.6035984562963372
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9790446151568679,
              "spearman": 0.9750599409695907,
              "auroc_top30_bad": 0.9787017142857143,
              "mae": 0.15698340243607525,
              "mse": 0.04298882570857856,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.928,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6500662043665916,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.3149090394973755
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.26424227912425996
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.14223802645206451
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.5357452588558197
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8829198032021522
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9825900058425051,
              "spearman": 0.9802321342925661,
              "auroc_top30_worst": 0.9684571428571428,
              "pairwise_seed_ranking": 0.89,
              "predicted_best_mean_error": 1.070513736128807,
              "seed0_mean_error": 1.1370457689762115,
              "random_seed_mean_error": 1.128170433998108,
              "oracle_best_mean_error": 1.0650475682020188,
              "improvement_over_seed0": 0.06653203284740439,
              "gap_to_oracle": 0.0054661679267882235,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.12725173163414003
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1592428440657946
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5293038670539856
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7971674334138695
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1261739067554475
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3457853794097905,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.9430408562024435,
                  "rejected_mean_error": 2.774371361732483,
                  "gap_rejected_minus_accepted": 1.8313305055300395
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5073687136173248,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 0.796587016373841,
                  "rejected_mean_error": 2.1128285913802562,
                  "gap_rejected_minus_accepted": 1.3162415750064151
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1728981733322144,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.5293038670539856,
                  "rejected_mean_error": 1.7230439464569092,
                  "gap_rejected_minus_accepted": 1.1937400794029236
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5490650236606598,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.16030063558691227,
                  "rejected_mean_error": 1.4488188735385332,
                  "gap_rejected_minus_accepted": 1.288518237951621
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5742329120635987,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 0.9492193553182814,
                  "rejected_mean_error": 2.827483491897583,
                  "gap_rejected_minus_accepted": 1.8782641365793018
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.519310623407364,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 0.7955564818280266,
                  "rejected_mean_error": 2.1506727006700306,
                  "gap_rejected_minus_accepted": 1.3551162188420038
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1762886047363281,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.5238347382545471,
                  "rejected_mean_error": 1.750256799697876,
                  "gap_rejected_minus_accepted": 1.226422061443329
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5202598571777344,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.1505885138398125,
                  "rejected_mean_error": 1.469381635679918,
                  "gap_rejected_minus_accepted": 1.3187931218401057
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9802214921993696,
              "spearman": 0.9661360268247605,
              "auroc_top30_bad": 0.9662857142857143,
              "mae": 0.14483231797218324,
              "mse": 0.03606288381283328,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.952,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5920915590783943,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.3154003502726555
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.22186696126461028
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.28317197793722154
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6299418120622635
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8961791918218136
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.940126874855398,
              "spearman": 0.9170904147778657,
              "auroc_top30_worst": 0.9240350476190478,
              "pairwise_seed_ranking": 0.9132,
              "predicted_best_mean_error": 1.0699430822134017,
              "seed0_mean_error": 1.1303126678466797,
              "random_seed_mean_error": 1.1341348474025725,
              "oracle_best_mean_error": 1.0674733737707138,
              "improvement_over_seed0": 0.06036958563327799,
              "gap_to_oracle": 0.0024697084426879012,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.33385878598690033
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.560597675685317
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8190778366804123
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9925838427217022
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1312655336737634
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5101089239120484,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0731318468915092,
                  "rejected_mean_error": 1.6544687147140502,
                  "gap_rejected_minus_accepted": 0.581336867822541
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.364526778459549,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 0.9918749999561076,
                  "rejected_mean_error": 1.5485464604898764,
                  "gap_rejected_minus_accepted": 0.5566714605337688
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.19619882106781,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.8190778366804123,
                  "rejected_mean_error": 1.4434532306671142,
                  "gap_rejected_minus_accepted": 0.6243753939867018
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9114572554826736,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.5615928505841916,
                  "rejected_mean_error": 1.3215617447805252,
                  "gap_rejected_minus_accepted": 0.7599688941963336
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5017228960990905,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.0727459817462497,
                  "rejected_mean_error": 1.6484128427505493,
                  "gap_rejected_minus_accepted": 0.5756668610042996
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3545946180820465,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.0000978580770645,
                  "rejected_mean_error": 1.5168232936707755,
                  "gap_rejected_minus_accepted": 0.516725435593711
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.228203296661377,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.824337266921997,
                  "rejected_mean_error": 1.4362880687713624,
                  "gap_rejected_minus_accepted": 0.6119508018493653
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9307609498500824,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.5604777061750018,
                  "rejected_mean_error": 1.3222891522601325,
                  "gap_rejected_minus_accepted": 0.7618114460851307
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_softmin_l2_K10"
      }
    ]
  }
}
```
