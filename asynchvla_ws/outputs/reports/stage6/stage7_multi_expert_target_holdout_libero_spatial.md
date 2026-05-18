# Stage 7 Multi-Expert Target Experiments: holdout_libero_spatial

```json
{
  "split": "holdout_libero_spatial",
  "by_target": {
    "target_chunk_l2_single_expert": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 68,
        "best_calib_loss": 0.043456222862005234,
        "train_time_sec": 10.937650203704834,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9791185591943172,
              "spearman": 0.942132583501174,
              "auroc_top30_bad": 0.9992567857142857,
              "mae": 0.11011463814005255,
              "mse": 0.044752817189313523,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.519,
              "expert_lt_simvla_seed0": 0.961,
              "same_context_pred_std": 0.7780554778298082,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2853554948568344
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.31968766971230506
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4825240647301078
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8227864096154769
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2758187427155674
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9991928865111877,
              "spearman": 0.9987223083728617,
              "auroc_top30_worst": 0.9991653333333333,
              "pairwise_seed_ranking": 0.87495,
              "predicted_best_mean_error": 1.777451872587204,
              "seed0_mean_error": 1.850025711297989,
              "random_seed_mean_error": 1.841148916900158,
              "oracle_best_mean_error": 1.7736391132473945,
              "improvement_over_seed0": 0.07257383871078504,
              "gap_to_oracle": 0.0038127593398094017,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6064276650547982
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8413910736322403
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.115140852844715
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3618107335805893
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8402536353409291
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.448615860939031,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5682130835122532,
                  "rejected_mean_error": 4.288618601799011,
                  "gap_rejected_minus_accepted": 2.720405518286758
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1303428411483765,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3618107335805893,
                  "rejected_mean_error": 3.2755823406219484,
                  "gap_rejected_minus_accepted": 1.913771607041359
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6192516088485718,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.115140852844715,
                  "rejected_mean_error": 2.565366417837143,
                  "gap_rejected_minus_accepted": 1.450225564992428
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1409856975078583,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8413910736322403,
                  "rejected_mean_error": 2.1732078225771585,
                  "gap_rejected_minus_accepted": 1.3318167489449182
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5012609243392947,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5771931121084426,
                  "rejected_mean_error": 4.305519104003906,
                  "gap_rejected_minus_accepted": 2.7283259918954634
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.142454147338867,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3727029441197713,
                  "rejected_mean_error": 3.2819940128326417,
                  "gap_rejected_minus_accepted": 1.9092910687128704
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6367242932319641,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.121596642255783,
                  "rejected_mean_error": 2.5784547803401945,
                  "gap_rejected_minus_accepted": 1.4568581380844114
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.156900405883789,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8448012180328369,
                  "rejected_mean_error": 2.185100542386373,
                  "gap_rejected_minus_accepted": 1.340299324353536
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8993236216163636,
              "spearman": 0.8946283544629692,
              "auroc_top30_bad": 0.9733973333333333,
              "mae": 0.26146977293491364,
              "mse": 0.1385109784529297,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.968,
              "same_context_pred_std": 0.6877410371071798,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.26954429841041566
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2912962038040161
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.43866625324487685
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7993239675283432
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1438312957584857
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7635905688667252,
              "spearman": 0.8169722855502628,
              "auroc_top30_worst": 0.9194057142857144,
              "pairwise_seed_ranking": 0.8276,
              "predicted_best_mean_error": 1.5681810374259948,
              "seed0_mean_error": 1.6587522393465042,
              "random_seed_mean_error": 1.6395123422145843,
              "oracle_best_mean_error": 1.5591331604719163,
              "improvement_over_seed0": 0.09057120192050938,
              "gap_to_oracle": 0.009047876954078493,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5828577063083649
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9265268143170919
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1625571732521056
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4084426190044834
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6363912368774414
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5036108970642093,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.566422431204054,
                  "rejected_mean_error": 2.2661104879379272,
                  "gap_rejected_minus_accepted": 0.6996880567338732
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0387012362480164,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.407134511045865,
                  "rejected_mean_error": 2.3226965151655787,
                  "gap_rejected_minus_accepted": 0.9155620041197137
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6343191862106323,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1625571732521056,
                  "rejected_mean_error": 2.110225300502777,
                  "gap_rejected_minus_accepted": 0.9476681272506715
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.240117073059082,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9251529159256444,
                  "rejected_mean_error": 1.8739767165550427,
                  "gap_rejected_minus_accepted": 0.9488238006293983
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5661507844924922,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.597039402458403,
                  "rejected_mean_error": 2.2141677713394166,
                  "gap_rejected_minus_accepted": 0.6171283688810136
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.052487373352051,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.419026982497404,
                  "rejected_mean_error": 2.3703176842795477,
                  "gap_rejected_minus_accepted": 0.9512907017821437
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.677315592765808,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1810853807926178,
                  "rejected_mean_error": 2.1364190979003905,
                  "gap_rejected_minus_accepted": 0.9553337171077727
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2826131284236908,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9520788500233303,
                  "rejected_mean_error": 1.896829370508857,
                  "gap_rejected_minus_accepted": 0.9447505204855268
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8345530780130233,
              "spearman": 0.8232467305185641,
              "auroc_top30_bad": 0.9147375238095238,
              "mae": 0.3262068328410387,
              "mse": 0.21225574344434672,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 0.952,
              "same_context_pred_std": 0.6253098873012928,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4122532194256783
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4342419227480888
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6429685149371624
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.005990526131789
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.273068219539523
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6395097564490737,
              "spearman": 0.6706945507226993,
              "auroc_top30_worst": 0.7967238095238094,
              "pairwise_seed_ranking": 0.7772,
              "predicted_best_mean_error": 1.76697731924057,
              "seed0_mean_error": 1.8436008858680726,
              "random_seed_mean_error": 1.808576955795288,
              "oracle_best_mean_error": 1.7398507182598113,
              "improvement_over_seed0": 0.07662356662750258,
              "gap_to_oracle": 0.027126600980758697,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2172553539276123
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3781124040102348
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.53629188079834
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.677280463643674
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114040771961213
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0292717218399052,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7523215143945483,
                  "rejected_mean_error": 2.3431471424102783,
                  "gap_rejected_minus_accepted": 0.59082562801573
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8422740697860718,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6766716594248214,
                  "rejected_mean_error": 2.2147404204923125,
                  "gap_rejected_minus_accepted": 0.538068761067491
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5549896359443665,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.53629188079834,
                  "rejected_mean_error": 2.0865162735939027,
                  "gap_rejected_minus_accepted": 0.5502243927955628
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.318148523569107,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.379680208123911,
                  "rejected_mean_error": 1.9556192010164006,
                  "gap_rejected_minus_accepted": 0.5759389928924896
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.074178194999695,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7701758209864298,
                  "rejected_mean_error": 2.5044264698028567,
                  "gap_rejected_minus_accepted": 0.7342506488164269
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8635857701301575,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.689000099738014,
                  "rejected_mean_error": 2.302495282793802,
                  "gap_rejected_minus_accepted": 0.6134951830557882
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5807673931121826,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.530753487586975,
                  "rejected_mean_error": 2.15644828414917,
                  "gap_rejected_minus_accepted": 0.6256947965621951
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3549310266971588,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3826176041648501,
                  "rejected_mean_error": 1.9989054139285165,
                  "gap_rejected_minus_accepted": 0.6162878097636664
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.8002154420383593,
              "spearman": 0.7997923885374071,
              "auroc_top30_bad": 0.887997619047619,
              "mae": 0.40896400408260525,
              "mse": 0.2823856954357632,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.47,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5976170702304657,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4584854208678007
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4384028019681573
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7408410107381642
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.091087144556145
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.48327798043566855,
              "spearman": 0.5364866604866606,
              "auroc_top30_worst": 0.8128047619047619,
              "pairwise_seed_ranking": 0.7405,
              "predicted_best_mean_error": 1.8823465493321418,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.04388351410627367,
              "gap_to_oracle": 0.01904516220092778,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.8341172921657563
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.6981498308181762
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.7356203091144562
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8222734553019206
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0800382137298583,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8752742252084944,
                  "rejected_mean_error": 2.2701489436626434,
                  "gap_rejected_minus_accepted": 0.394874718454149
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.876784771680832,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8222734553019206,
                  "rejected_mean_error": 2.1922264223098753,
                  "gap_rejected_minus_accepted": 0.36995296700795466
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5119617581367493,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.7356203091144562,
                  "rejected_mean_error": 2.0939030849933626,
                  "gap_rejected_minus_accepted": 0.35828277587890645
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.131206065416336,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.6981498308181762,
                  "rejected_mean_error": 1.9869656524658204,
                  "gap_rejected_minus_accepted": 0.2888158216476442
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.057184362411499,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.892869198322296,
                  "rejected_mean_error": 2.22647784948349,
                  "gap_rejected_minus_accepted": 0.33360865116119376
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8893934786319733,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8329909046490986,
                  "rejected_mean_error": 2.205947539806366,
                  "gap_rejected_minus_accepted": 0.3729566351572673
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5382745862007141,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.766676275730133,
                  "rejected_mean_error": 2.085783851146698,
                  "gap_rejected_minus_accepted": 0.3191075754165651
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1203598380088806,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.7080713415145874,
                  "rejected_mean_error": 1.998949637413025,
                  "gap_rejected_minus_accepted": 0.2908782958984375
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
        "best_calib_loss": 0.009220060892403126,
        "train_time_sec": 35.3127875328064,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997703881140664,
              "spearman": 0.9989410177685852,
              "auroc_top30_bad": 0.9996963809523809,
              "mae": 0.02633318721386604,
              "mse": 0.0010934277123081908,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7947328515415986,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0007461490333080292
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1725826847165823
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4750860001310706
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8225795405854781
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2758187427155674
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9998443223703568,
              "spearman": 0.9997289887251593,
              "auroc_top30_worst": 0.9998224761904762,
              "pairwise_seed_ranking": 0.9535,
              "predicted_best_mean_error": 1.7742420142889024,
              "seed0_mean_error": 1.850025711297989,
              "random_seed_mean_error": 1.841148916900158,
              "oracle_best_mean_error": 1.7736391132473945,
              "improvement_over_seed0": 0.0757836970090866,
              "gap_to_oracle": 0.0006029010415078417,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6037957341074943
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8403301589250565
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1144419116139412
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.361718096200625
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8402536353409291
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.415618062019348,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5681043335398037,
                  "rejected_mean_error": 4.2895973515510555,
                  "gap_rejected_minus_accepted": 2.7214930180112518
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.105038344860077,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.361718096200625,
                  "rejected_mean_error": 3.275860252761841,
                  "gap_rejected_minus_accepted": 1.914142156561216
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6022873520851135,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1144419116139412,
                  "rejected_mean_error": 2.5660653590679168,
                  "gap_rejected_minus_accepted": 1.4516234474539755
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1271145939826965,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8403301589250565,
                  "rejected_mean_error": 2.1735614608128864,
                  "gap_rejected_minus_accepted": 1.33323130188783
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.381537151336671,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5771077304416232,
                  "rejected_mean_error": 4.30628753900528,
                  "gap_rejected_minus_accepted": 2.7291798085636563
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1387770771980286,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.372678061167399,
                  "rejected_mean_error": 3.2820686616897583,
                  "gap_rejected_minus_accepted": 1.9093906005223593
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6239858269691467,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1211341967582702,
                  "rejected_mean_error": 2.5789172258377073,
                  "gap_rejected_minus_accepted": 1.4577830290794371
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1424451172351837,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8440675048828125,
                  "rejected_mean_error": 2.185345113436381,
                  "gap_rejected_minus_accepted": 1.3412776085535687
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9848880260929258,
              "spearman": 0.9869706278537022,
              "auroc_top30_bad": 0.9968495238095239,
              "mae": 0.09153138572340831,
              "mse": 0.021766981335626365,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.972,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7271379257685048,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.059123868525028225
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1691837746143341
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.401049451982975
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.775042092680931
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1438312957584857
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9667736219817997,
              "spearman": 0.9886181528436179,
              "auroc_top30_worst": 0.9953645714285715,
              "pairwise_seed_ranking": 0.9496,
              "predicted_best_mean_error": 1.5600144982337951,
              "seed0_mean_error": 1.6587522393465042,
              "random_seed_mean_error": 1.6395123422145843,
              "oracle_best_mean_error": 1.5591331604719163,
              "improvement_over_seed0": 0.09873774111270905,
              "gap_to_oracle": 0.0008813377618788198,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.467196804523468
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.748097056379685
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0912841262817383
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3462023761735034
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6363912368774414
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.517906403541566,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5124455841912163,
                  "rejected_mean_error": 2.7519021110534667,
                  "gap_rejected_minus_accepted": 1.2394565268622504
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.088523209095001,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3453796005299914,
                  "rejected_mean_error": 2.5075666466460063,
                  "gap_rejected_minus_accepted": 1.1621870461160149
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.645640254020691,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0912841262817383,
                  "rejected_mean_error": 2.1814983474731444,
                  "gap_rejected_minus_accepted": 1.090214221191406
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0817206799983978,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7495808292882511,
                  "rejected_mean_error": 1.9326256633186545,
                  "gap_rejected_minus_accepted": 1.1830448340304034
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5719359874725343,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5295531719260747,
                  "rejected_mean_error": 2.8215438461303712,
                  "gap_rejected_minus_accepted": 1.2919906742042966
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1190354228019714,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3649437218745124,
                  "rejected_mean_error": 2.530850537239559,
                  "gap_rejected_minus_accepted": 1.1659068153650467
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6671922206878662,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1106175692081452,
                  "rejected_mean_error": 2.2068869094848633,
                  "gap_rejected_minus_accepted": 1.096269340276718
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1171604096889496,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7606442887631674,
                  "rejected_mean_error": 1.9613233670831365,
                  "gap_rejected_minus_accepted": 1.2006790783199692
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9830983108836803,
              "spearman": 0.9843933128703986,
              "auroc_top30_bad": 0.9902895238095238,
              "mae": 0.0986508480515331,
              "mse": 0.02407186004525409,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7077665358144518,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04212873774766922
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17435353454351424
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5726431674420833
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9602308992664019
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.273068219539523
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9403286398260324,
              "spearman": 0.9701281185641127,
              "auroc_top30_worst": 0.9715657142857143,
              "pairwise_seed_ranking": 0.9332,
              "predicted_best_mean_error": 1.7411555933952332,
              "seed0_mean_error": 1.8436008858680726,
              "random_seed_mean_error": 1.808576955795288,
              "oracle_best_mean_error": 1.7398507182598113,
              "improvement_over_seed0": 0.1024452924728394,
              "gap_to_oracle": 0.001304875135421879,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.881929009437561
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1817248645119178
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4383579060554503
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6157212772730316
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114040771961213
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2777521371841436,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7260441949102614,
                  "rejected_mean_error": 2.57964301776886,
                  "gap_rejected_minus_accepted": 0.8535988228585987
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9863390624523163,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6154020821781017,
                  "rejected_mean_error": 2.398157653336327,
                  "gap_rejected_minus_accepted": 0.7827555711582255
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7688689231872559,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4383579060554503,
                  "rejected_mean_error": 2.184450248336792,
                  "gap_rejected_minus_accepted": 0.7460923422813417
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4847294688224792,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.182793449479551,
                  "rejected_mean_error": 2.0213882036371955,
                  "gap_rejected_minus_accepted": 0.8385947541576446
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3779789447784423,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7504408831066556,
                  "rejected_mean_error": 2.682040910720825,
                  "gap_rejected_minus_accepted": 0.9316000276141696
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.004992425441742,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6310164233579993,
                  "rejected_mean_error": 2.4746055603027344,
                  "gap_rejected_minus_accepted": 0.843589136944735
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7860934138298035,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.448211989402771,
                  "rejected_mean_error": 2.238989782333374,
                  "gap_rejected_minus_accepted": 0.7907777929306032
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5178552865982056,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.186412425268264,
                  "rejected_mean_error": 2.06500662393111,
                  "gap_rejected_minus_accepted": 0.8785941986628458
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.988577748077222,
              "spearman": 0.9697368201326078,
              "auroc_top30_bad": 0.9637797619047619,
              "mae": 0.12059017521119676,
              "mse": 0.025096474013245888,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.99,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7099623293955727,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.040374291185289624
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17179380495101212
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6652404665984213
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.058513855141898
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9391770024567112,
              "spearman": 0.906927270927271,
              "auroc_top30_worst": 0.9635476190476191,
              "pairwise_seed_ranking": 0.9245,
              "predicted_best_mean_error": 1.8645599648356437,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.06167009860277184,
              "gap_to_oracle": 0.0012585777044296087,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2963084661960602
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4602511205673219
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6618391683101654
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7669232513109843
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.157227659225464,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8459502577781677,
                  "rejected_mean_error": 2.5340646505355835,
                  "gap_rejected_minus_accepted": 0.6881143927574158
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.983032763004303,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7669232513109843,
                  "rejected_mean_error": 2.3582770342826844,
                  "gap_rejected_minus_accepted": 0.5913537829717002
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7852979898452759,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6618391683101654,
                  "rejected_mean_error": 2.1676842257976534,
                  "gap_rejected_minus_accepted": 0.505845057487488
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.591419368982315,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4602511205673219,
                  "rejected_mean_error": 2.0662652225494385,
                  "gap_rejected_minus_accepted": 0.6060141019821166
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1646297216415404,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8583704710006714,
                  "rejected_mean_error": 2.536966395378113,
                  "gap_rejected_minus_accepted": 0.6785959243774415
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0016645193099976,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7717185123761494,
                  "rejected_mean_error": 2.389764716625214,
                  "gap_rejected_minus_accepted": 0.6180462042490644
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7935392260551453,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.67364905834198,
                  "rejected_mean_error": 2.178811068534851,
                  "gap_rejected_minus_accepted": 0.5051620101928711
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6266188621520996,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4681547474861145,
                  "rejected_mean_error": 2.078921835422516,
                  "gap_rejected_minus_accepted": 0.6107670879364013
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_l2_single_expert"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 80,
        "best_calib_loss": 0.008431831374764442,
        "train_time_sec": 41.569247245788574,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9994096332280908,
              "spearman": 0.99816006984042,
              "auroc_top30_bad": 0.9994496190476191,
              "mae": 0.041649735131536726,
              "mse": 0.0036178613268991583,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8269009137859986,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.00211920190602541
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1732202856987715
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.47533323480933903
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8228126456091801
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2758187427155674
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9994769746454583,
              "spearman": 0.9990222905528915,
              "auroc_top30_worst": 0.9994611428571429,
              "pairwise_seed_ranking": 0.96,
              "predicted_best_mean_error": 1.7748349421322345,
              "seed0_mean_error": 1.850025711297989,
              "random_seed_mean_error": 1.841148916900158,
              "oracle_best_mean_error": 1.7736391132473945,
              "improvement_over_seed0": 0.07519076916575451,
              "gap_to_oracle": 0.0011958288848399334,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6048800427317619
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8410790249109268
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1147043461441994
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.361697089234988
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8402536353409291
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5896917343139667,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5681172481973966,
                  "rejected_mean_error": 4.289481119632721,
                  "gap_rejected_minus_accepted": 2.721363871435324
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1804890632629395,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.361697089234988,
                  "rejected_mean_error": 3.2759232736587522,
                  "gap_rejected_minus_accepted": 1.9142261844237642
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6547308564186096,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1147043461441994,
                  "rejected_mean_error": 2.5658029245376586,
                  "gap_rejected_minus_accepted": 1.4510985783934591
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1747077107429504,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8410790249109268,
                  "rejected_mean_error": 2.1733118388175963,
                  "gap_rejected_minus_accepted": 1.3322328139066695
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5685972213745134,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5771077304416232,
                  "rejected_mean_error": 4.30628753900528,
                  "gap_rejected_minus_accepted": 2.7291798085636563
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2099874019622803,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3726445945103962,
                  "rejected_mean_error": 3.2821690616607664,
                  "gap_rejected_minus_accepted": 1.9095244671503702
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6743106842041016,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1213788547515868,
                  "rejected_mean_error": 2.5786725678443907,
                  "gap_rejected_minus_accepted": 1.4572937130928039
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1836427450180054,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8444980721473694,
                  "rejected_mean_error": 2.185201591014862,
                  "gap_rejected_minus_accepted": 1.3407035188674927
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9874914223482948,
              "spearman": 0.9833688589870653,
              "auroc_top30_bad": 0.9975740952380953,
              "mae": 0.09294447983884366,
              "mse": 0.01857557746403126,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7122873305397964,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08684034407138824
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1786613879919052
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4019855172753334
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7739714344422023
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1438312957584857
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.983123489079474,
              "spearman": 0.9929841311898441,
              "auroc_top30_worst": 0.996376380952381,
              "pairwise_seed_ranking": 0.9256,
              "predicted_best_mean_error": 1.560928036093712,
              "seed0_mean_error": 1.6587522393465042,
              "random_seed_mean_error": 1.6395123422145843,
              "oracle_best_mean_error": 1.5591331604719163,
              "improvement_over_seed0": 0.09782420325279229,
              "gap_to_oracle": 0.0017948756217955886,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46594742155075075
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.747542407650214
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0926908237457276
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3440739919127687
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6363912368774414
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.50484938621521,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5015942821502686,
                  "rejected_mean_error": 2.849563829421997,
                  "gap_rejected_minus_accepted": 1.3479695472717286
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.02683424949646,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.343326184258517,
                  "rejected_mean_error": 2.513713774589685,
                  "gap_rejected_minus_accepted": 1.170387590331168
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6073789596557617,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0926908237457276,
                  "rejected_mean_error": 2.1800916500091554,
                  "gap_rejected_minus_accepted": 1.0874008262634278
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.05608269572258,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7491879417492558,
                  "rejected_mean_error": 1.932756905367433,
                  "gap_rejected_minus_accepted": 1.183568963618177
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.550055336952209,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.521705856455697,
                  "rejected_mean_error": 2.8921696853637697,
                  "gap_rejected_minus_accepted": 1.3704638289080728
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0478644967079163,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3610560411119206,
                  "rejected_mean_error": 2.542390161090427,
                  "gap_rejected_minus_accepted": 1.1813341199785063
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6120164394378662,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1113553001880645,
                  "rejected_mean_error": 2.2061491785049436,
                  "gap_rejected_minus_accepted": 1.0947938783168791
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1115075945854187,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7610495965632181,
                  "rejected_mean_error": 1.9611868195355258,
                  "gap_rejected_minus_accepted": 1.2001372229723075
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9784677835946103,
              "spearman": 0.9776768926169873,
              "auroc_top30_bad": 0.991031619047619,
              "mae": 0.10437859331139553,
              "mse": 0.028433052319876487,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6951251928216762,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13499867206811905
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21409075835943223
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5728016328275204
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.958155577814579
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.273068219539523
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9611428257675674,
              "spearman": 0.980359653033843,
              "auroc_top30_worst": 0.9873219047619047,
              "pairwise_seed_ranking": 0.9312,
              "predicted_best_mean_error": 1.741128894329071,
              "seed0_mean_error": 1.8436008858680726,
              "random_seed_mean_error": 1.808576955795288,
              "oracle_best_mean_error": 1.7398507182598113,
              "improvement_over_seed0": 0.10247199153900155,
              "gap_to_oracle": 0.0012781760692597288,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8797276849746705
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1802988065741
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4382016814231873
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6102945864963125
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114040771961213
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3758570909500123,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7212426262431675,
                  "rejected_mean_error": 2.6228571357727053,
                  "gap_rejected_minus_accepted": 0.9016145095295378
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.038808286190033,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6097102174764,
                  "rejected_mean_error": 2.415196877698929,
                  "gap_rejected_minus_accepted": 0.805486660222529
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7750686407089233,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4382016814231873,
                  "rejected_mean_error": 2.184606472969055,
                  "gap_rejected_minus_accepted": 0.7464047915458678
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4715380668640137,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1812494378120373,
                  "rejected_mean_error": 2.0219039727427788,
                  "gap_rejected_minus_accepted": 0.8406545349307415
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4986114025115964,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7456875605053372,
                  "rejected_mean_error": 2.7248208141326904,
                  "gap_rejected_minus_accepted": 0.9791332536273532
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.08051598072052,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6206300373383384,
                  "rejected_mean_error": 2.50543499182141,
                  "gap_rejected_minus_accepted": 0.8848049544830716
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7852930426597595,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4458104515075683,
                  "rejected_mean_error": 2.2413913202285767,
                  "gap_rejected_minus_accepted": 0.7955808687210084
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.490676999092102,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1892399314850095,
                  "rejected_mean_error": 2.064054041622794,
                  "gap_rejected_minus_accepted": 0.8748141101377847
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9873071139248955,
              "spearman": 0.9777577965589702,
              "auroc_top30_bad": 0.9811190476190476,
              "mae": 0.11110936688376091,
              "mse": 0.02215554804421543,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7020724391583212,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07678855117410421
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17715998516231776
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6660664513148368
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0520117333754897
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9659841397299291,
              "spearman": 0.9580561300561301,
              "auroc_top30_worst": 0.9776190476190476,
              "pairwise_seed_ranking": 0.933,
              "predicted_best_mean_error": 1.8641843995451928,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.06204566389322275,
              "gap_to_oracle": 0.000883012413978701,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.278077644109726
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4578445324897766
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.643594445705414
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.759923928896586
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2643765926361086,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8442956598599751,
                  "rejected_mean_error": 2.5489560317993165,
                  "gap_rejected_minus_accepted": 0.7046603719393414
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9958806335926056,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.759923928896586,
                  "rejected_mean_error": 2.379275001525879,
                  "gap_rejected_minus_accepted": 0.6193510726292928
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7843734622001648,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.643594445705414,
                  "rejected_mean_error": 2.1859289484024047,
                  "gap_rejected_minus_accepted": 0.5423345026969908
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5890920758247375,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4578445324897766,
                  "rejected_mean_error": 2.067067418575287,
                  "gap_rejected_minus_accepted": 0.6092228860855105
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2938955068588256,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8545466820398966,
                  "rejected_mean_error": 2.5713804960250854,
                  "gap_rejected_minus_accepted": 0.7168338139851889
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.009945034980774,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7680246750513713,
                  "rejected_mean_error": 2.400846228599548,
                  "gap_rejected_minus_accepted": 0.6328215535481769
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7899265885353088,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6506109833717346,
                  "rejected_mean_error": 2.2018491435050964,
                  "gap_rejected_minus_accepted": 0.5512381601333618
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5894053876399994,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4592434930801392,
                  "rejected_mean_error": 2.081892253557841,
                  "gap_rejected_minus_accepted": 0.6226487604777016
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_l2_single_expert"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 78,
        "best_calib_loss": 0.0089102853089571,
        "train_time_sec": 29.19154405593872,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9998198476553173,
              "spearman": 0.9990605776746364,
              "auroc_top30_bad": 0.9998261428571429,
              "mae": 0.0244435579204679,
              "mse": 0.0011524061151916946,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8198435376242428,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0011885562911629678
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1724192979902029
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.47507850506156685
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8225496656407912
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2758187427155674
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997758761322458,
              "spearman": 0.9996667355066533,
              "auroc_top30_worst": 0.9997121904761904,
              "pairwise_seed_ranking": 0.9601,
              "predicted_best_mean_error": 1.7740204818844796,
              "seed0_mean_error": 1.850025711297989,
              "random_seed_mean_error": 1.841148916900158,
              "oracle_best_mean_error": 1.7736391132473945,
              "improvement_over_seed0": 0.0760052294135094,
              "gap_to_oracle": 0.0003813686370850444,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6039228975176811
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.840402273774147
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1145205007195473
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.361681278649966
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8402536353409291
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5224678039550823,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5681219244334432,
                  "rejected_mean_error": 4.289439033508301,
                  "gap_rejected_minus_accepted": 2.7213171090748576
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1725670099258423,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.361681278649966,
                  "rejected_mean_error": 3.2759707054138185,
                  "gap_rejected_minus_accepted": 1.9142894267638526
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6625601053237915,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1145205007195473,
                  "rejected_mean_error": 2.565986769962311,
                  "gap_rejected_minus_accepted": 1.4514662692427636
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1637305617332458,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.840402273774147,
                  "rejected_mean_error": 2.1735374225298565,
                  "gap_rejected_minus_accepted": 1.3331351487557095
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.493501234054566,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5771077304416232,
                  "rejected_mean_error": 4.30628753900528,
                  "gap_rejected_minus_accepted": 2.7291798085636563
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.194422721862793,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3725954325993857,
                  "rejected_mean_error": 3.282316547393799,
                  "gap_rejected_minus_accepted": 1.9097211147944133
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6770048141479492,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1211388027668,
                  "rejected_mean_error": 2.578912619829178,
                  "gap_rejected_minus_accepted": 1.4577738170623782
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.177521526813507,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8439300174713135,
                  "rejected_mean_error": 2.185390942573547,
                  "gap_rejected_minus_accepted": 1.3414609251022336
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9873374433531922,
              "spearman": 0.9853362550106962,
              "auroc_top30_bad": 0.9972342857142857,
              "mae": 0.09629036382874592,
              "mse": 0.02080713537380447,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6987690213006383,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08293363201618195
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1685842244386673
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4037636478066444
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7748411494970322
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1438312957584857
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9792440520598559,
              "spearman": 0.9896487603512067,
              "auroc_top30_worst": 0.9975923809523809,
              "pairwise_seed_ranking": 0.9312,
              "predicted_best_mean_error": 1.5603090915679931,
              "seed0_mean_error": 1.6587522393465042,
              "random_seed_mean_error": 1.6395123422145843,
              "oracle_best_mean_error": 1.5591331604719163,
              "improvement_over_seed0": 0.09844314777851104,
              "gap_to_oracle": 0.001175931096076832,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.48610686588287355
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7567098484589503
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.094648468208313
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.343256520437025
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6363912368774414
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4492326736450196,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5001703539954292,
                  "rejected_mean_error": 2.862379182815552,
                  "gap_rejected_minus_accepted": 1.3622088288201226
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.995179295539856,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3424168731003459,
                  "rejected_mean_error": 2.5164358977692576,
                  "gap_rejected_minus_accepted": 1.1740190246689117
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5795102715492249,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.094648468208313,
                  "rejected_mean_error": 2.17813400554657,
                  "gap_rejected_minus_accepted": 1.0834855373382568
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0881227254867554,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.757967732204035,
                  "rejected_mean_error": 1.9298240618110338,
                  "gap_rejected_minus_accepted": 1.1718563296069988
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4769752264022826,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5188808039824169,
                  "rejected_mean_error": 2.917595157623291,
                  "gap_rejected_minus_accepted": 1.398714353640874
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0250775814056396,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.35950615587719,
                  "rejected_mean_error": 2.5469906140887546,
                  "gap_rejected_minus_accepted": 1.1874844582115647
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.588906168937683,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1141909601688385,
                  "rejected_mean_error": 2.20331351852417,
                  "gap_rejected_minus_accepted": 1.0891225583553314
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1204762756824493,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7714120967993661,
                  "rejected_mean_error": 1.9576957098302994,
                  "gap_rejected_minus_accepted": 1.1862836130309333
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9845313293407487,
              "spearman": 0.9836468224178744,
              "auroc_top30_bad": 0.993752380952381,
              "mae": 0.09827056306654376,
              "mse": 0.0209904123359165,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7025923804743035,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05730677765607834
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19032147566080093
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5751838212430477
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.958322054318587
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.273068219539523
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9665520006348849,
              "spearman": 0.9755716015332591,
              "auroc_top30_worst": 0.9842986666666667,
              "pairwise_seed_ranking": 0.9128,
              "predicted_best_mean_error": 1.7434360044002533,
              "seed0_mean_error": 1.8436008858680726,
              "random_seed_mean_error": 1.808576955795288,
              "oracle_best_mean_error": 1.7398507182598113,
              "improvement_over_seed0": 0.10016488146781932,
              "gap_to_oracle": 0.0035852861404419567,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8892704482078553
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1884642948324864
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4363347899436951
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6093109830229013
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114040771961213
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3219802379608154,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.725732164647844,
                  "rejected_mean_error": 2.5824512901306154,
                  "gap_rejected_minus_accepted": 0.8567191254827713
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.050547957420349,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6087484387094464,
                  "rejected_mean_error": 2.4180760684485634,
                  "gap_rejected_minus_accepted": 0.809327629739117
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7921876311302185,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4363347899436951,
                  "rejected_mean_error": 2.1864733644485472,
                  "gap_rejected_minus_accepted": 0.7501385745048521
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4700121581554413,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1894395101946382,
                  "rejected_mean_error": 2.0191681214559547,
                  "gap_rejected_minus_accepted": 0.8297286112613165
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4124129533767698,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7502025609546237,
                  "rejected_mean_error": 2.684185810089111,
                  "gap_rejected_minus_accepted": 0.9339832491344875
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0873544812202454,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6207499555087983,
                  "rejected_mean_error": 2.5050790442360773,
                  "gap_rejected_minus_accepted": 0.884329088727279
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8162252306938171,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.444787262916565,
                  "rejected_mean_error": 2.24241450881958,
                  "gap_rejected_minus_accepted": 0.7976272459030149
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5050705075263977,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1957006000337147,
                  "rejected_mean_error": 2.0618774527534445,
                  "gap_rejected_minus_accepted": 0.8661768527197298
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9886444604599364,
              "spearman": 0.977249965707522,
              "auroc_top30_bad": 0.9754690476190476,
              "mae": 0.09908456634620552,
              "mse": 0.01864993206292063,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7308565123889449,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0625894807651639
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17187834022194148
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.662135640386492
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0543955338026088
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9516683823293529,
              "spearman": 0.9395822795822796,
              "auroc_top30_worst": 0.9639857142857142,
              "pairwise_seed_ranking": 0.918,
              "predicted_best_mean_error": 1.8649181178212166,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.06131194561719888,
              "gap_to_oracle": 0.0016167306900025658,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2831151032447814
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4522973532676697
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6478249478340148
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7647622911135357
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.326526641845703,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.848495803144243,
                  "rejected_mean_error": 2.511154742240906,
                  "gap_rejected_minus_accepted": 0.6626589390966628
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0227527022361755,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7647622911135357,
                  "rejected_mean_error": 2.3647599148750307,
                  "gap_rejected_minus_accepted": 0.599997623761495
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8056241273880005,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6478249478340148,
                  "rejected_mean_error": 2.1816984462738036,
                  "gap_rejected_minus_accepted": 0.5338734984397888
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5717274844646454,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4522973532676697,
                  "rejected_mean_error": 2.0689164783159892,
                  "gap_rejected_minus_accepted": 0.6166191250483195
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3430439472198485,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8594205578168232,
                  "rejected_mean_error": 2.5275156140327453,
                  "gap_rejected_minus_accepted": 0.668095056215922
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0182507634162903,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7733531562487284,
                  "rejected_mean_error": 2.384860785007477,
                  "gap_rejected_minus_accepted": 0.6115076287587486
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8170302510261536,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6561272430419922,
                  "rejected_mean_error": 2.196332883834839,
                  "gap_rejected_minus_accepted": 0.5402056407928468
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5825927257537842,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.46461412191391,
                  "rejected_mean_error": 2.0801020439465843,
                  "gap_rejected_minus_accepted": 0.6154879220326743
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_l2_single_expert"
      }
    ],
    "target_chunk_min_l2_K5": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 75,
        "best_calib_loss": 0.052288755774497986,
        "train_time_sec": 10.818695068359375,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9835498103291238,
              "spearman": 0.941630934274613,
              "auroc_top30_bad": 0.9988002619047619,
              "mae": 0.10534468016574391,
              "mse": 0.036092185436402704,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.506,
              "expert_lt_simvla_seed0": 0.962,
              "same_context_pred_std": 0.8042827878629788,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.30206426031701267
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3150834286469966
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4583904661039589
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.797954082757902
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2539649001111626
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9987769648861134,
              "spearman": 0.9984887998834433,
              "auroc_top30_worst": 0.9993986666666667,
              "pairwise_seed_ranking": 0.8596,
              "predicted_best_mean_error": 1.7527569598257542,
              "seed0_mean_error": 1.8214172512590885,
              "random_seed_mean_error": 1.8132706600129604,
              "oracle_best_mean_error": 1.7476961852610111,
              "improvement_over_seed0": 0.0686602914333343,
              "gap_to_oracle": 0.005060774564743076,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5563193296194077
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7918928263664246
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.074719937992096
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3283054099082947
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8120445298671723
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5059512853622445,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5379680581092834,
                  "rejected_mean_error": 4.278732775688171,
                  "gap_rejected_minus_accepted": 2.740764717578888
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.149258852005005,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3283054099082947,
                  "rejected_mean_error": 3.263261889743805,
                  "gap_rejected_minus_accepted": 1.9349564798355101
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6358174085617065,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.074719937992096,
                  "rejected_mean_error": 2.5493691217422487,
                  "gap_rejected_minus_accepted": 1.4746491837501527
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1184731125831604,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7918928263664246,
                  "rejected_mean_error": 2.1520950977007547,
                  "gap_rejected_minus_accepted": 1.3602022713343302
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.4855591535568244,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5467365361915695,
                  "rejected_mean_error": 4.2935436868667605,
                  "gap_rejected_minus_accepted": 2.746807150675191
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1644737124443054,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3386576129992802,
                  "rejected_mean_error": 3.2696961660385133,
                  "gap_rejected_minus_accepted": 1.931038553039233
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.64734548330307,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.080437696993351,
                  "rejected_mean_error": 2.562396805524826,
                  "gap_rejected_minus_accepted": 1.4819591085314752
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1424184143543243,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7943659349679947,
                  "rejected_mean_error": 2.1637676900227865,
                  "gap_rejected_minus_accepted": 1.369401755054792
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8566303844014052,
              "spearman": 0.8793350004341427,
              "auroc_top30_bad": 0.9650735238095238,
              "mae": 0.30002661086320875,
              "mse": 0.2127802302227497,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 0.972,
              "same_context_pred_std": 0.7086813930683751,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3045537518262863
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3374627114772797
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.48667638549804687
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8515642811934153
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1942378834486007
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6718834389128902,
              "spearman": 0.7814913878344883,
              "auroc_top30_worst": 0.8865158095238095,
              "pairwise_seed_ranking": 0.8048,
              "predicted_best_mean_error": 1.6339693884849549,
              "seed0_mean_error": 1.7177031744718552,
              "random_seed_mean_error": 1.6985768196582793,
              "oracle_best_mean_error": 1.6184608579874038,
              "improvement_over_seed0": 0.08373378598690029,
              "gap_to_oracle": 0.015508530497551076,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.662320856809616
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9261264625268105
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1952939703941345
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4784342455965624
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6955634710311889
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5145942926406866,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6405838351779514,
                  "rejected_mean_error": 2.190380193710327,
                  "gap_rejected_minus_accepted": 0.5497963585323757
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9886675477027893,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4776982740760485,
                  "rejected_mean_error": 2.347766952011913,
                  "gap_rejected_minus_accepted": 0.8700686779358644
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6253769993782043,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1952939703941345,
                  "rejected_mean_error": 2.1958329716682434,
                  "gap_rejected_minus_accepted": 1.0005390012741089
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1908859610557556,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9282946281920607,
                  "rejected_mean_error": 1.9518656565260097,
                  "gap_rejected_minus_accepted": 1.023571028333949
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.649566340446472,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6675146737363604,
                  "rejected_mean_error": 2.1693996810913085,
                  "gap_rejected_minus_accepted": 0.5018850073549481
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0189613699913025,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4953208331437033,
                  "rejected_mean_error": 2.37779044158875,
                  "gap_rejected_minus_accepted": 0.8824696084450467
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6516624689102173,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.20069185423851,
                  "rejected_mean_error": 2.2347144947052002,
                  "gap_rejected_minus_accepted": 1.0340226404666901
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2252240180969238,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.923700170384513,
                  "rejected_mean_error": 1.98520151274727,
                  "gap_rejected_minus_accepted": 1.061501342362757
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8203359310974654,
              "spearman": 0.8067937369841027,
              "auroc_top30_bad": 0.9073059047619048,
              "mae": 0.36158793699741365,
              "mse": 0.2585918330965366,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.952,
              "same_context_pred_std": 0.6663528335684477,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4603761444091797
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4671674238204956
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6875799000859261
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0567205073436101
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3158914593279363
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.5680325761232259,
              "spearman": 0.5920158555114841,
              "auroc_top30_worst": 0.7398460952380952,
              "pairwise_seed_ranking": 0.7528,
              "predicted_best_mean_error": 1.8353224282264708,
              "seed0_mean_error": 1.9027296719551086,
              "random_seed_mean_error": 1.8683821330070496,
              "oracle_best_mean_error": 1.8003094832897186,
              "improvement_over_seed0": 0.06740724372863771,
              "gap_to_oracle": 0.03501294493675222,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2429856977462768
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4617577617367108
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6212783960342407
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.753057248556792
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8711545301914214
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0541427850723277,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8095568968984816,
                  "rejected_mean_error": 2.425533229827881,
                  "gap_rejected_minus_accepted": 0.6159763329293992
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8835082352161407,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7518401033977562,
                  "rejected_mean_error": 2.228335418068944,
                  "gap_rejected_minus_accepted": 0.47649531467118766
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5899876952171326,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.6212783960342407,
                  "rejected_mean_error": 2.121030664348602,
                  "gap_rejected_minus_accepted": 0.49975226831436137
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3158741891384125,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.461545842714584,
                  "rejected_mean_error": 2.0079821920700236,
                  "gap_rejected_minus_accepted": 0.5464363493554396
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0911314010620115,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8349717860751682,
                  "rejected_mean_error": 2.512550644874573,
                  "gap_rejected_minus_accepted": 0.6775788587994047
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9313907027244568,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7677263257337763,
                  "rejected_mean_error": 2.3034538901041426,
                  "gap_rejected_minus_accepted": 0.5357275643703663
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6254951357841492,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.610129626274109,
                  "rejected_mean_error": 2.1953297176361084,
                  "gap_rejected_minus_accepted": 0.5852000913619995
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3464484810829163,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.4675048722161188,
                  "rejected_mean_error": 2.0493562087655706,
                  "gap_rejected_minus_accepted": 0.5818513365494518
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.770219012725012,
              "spearman": 0.7745834400805789,
              "auroc_top30_bad": 0.8642297619047619,
              "mae": 0.4383295094203204,
              "mse": 0.34021880234247803,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.49,
              "expert_lt_simvla_seed0": 0.99,
              "same_context_pred_std": 0.6181538713032789,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46339354462921617
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.44810646966844797
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7728592990972102
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.092346895955503
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.39157835248332085,
              "spearman": 0.4348004068004068,
              "auroc_top30_worst": 0.7484952380952381,
              "pairwise_seed_ranking": 0.7145,
              "predicted_best_mean_error": 1.885932324528694,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.04029773890972144,
              "gap_to_oracle": 0.02263093739748001,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.8795927035808564
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.7570648922920227
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.781408369064331
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8273251393636067
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.084187650680542,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8767429007424248,
                  "rejected_mean_error": 2.2569308638572694,
                  "gap_rejected_minus_accepted": 0.3801879631148446
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8942012786865234,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8273251393636067,
                  "rejected_mean_error": 2.1770713701248168,
                  "gap_rejected_minus_accepted": 0.34974623076121003
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.449589729309082,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.781408369064331,
                  "rejected_mean_error": 2.0481150250434874,
                  "gap_rejected_minus_accepted": 0.26670665597915644
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0549773275852203,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.7570648922920227,
                  "rejected_mean_error": 1.967327298641205,
                  "gap_rejected_minus_accepted": 0.21026240634918225
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0812978506088258,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8912252068519593,
                  "rejected_mean_error": 2.2412737727165224,
                  "gap_rejected_minus_accepted": 0.3500485658645631
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8987319469451904,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8366390506426493,
                  "rejected_mean_error": 2.195003101825714,
                  "gap_rejected_minus_accepted": 0.3583640511830646
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4935649633407593,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.7929500234127045,
                  "rejected_mean_error": 2.0595101034641266,
                  "gap_rejected_minus_accepted": 0.26656008005142207
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0684778690338135,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.7647829699516295,
                  "rejected_mean_error": 1.980045761267344,
                  "gap_rejected_minus_accepted": 0.21526279131571457
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K5"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 66,
        "best_calib_loss": 0.016439683735370636,
        "train_time_sec": 34.93841290473938,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997545606419016,
              "spearman": 0.9989603642666219,
              "auroc_top30_bad": 0.9997378095238095,
              "mae": 0.023506126169639173,
              "mse": 0.0008811933263594929,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8055836378276374,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.060956509472220206
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1885287460168358
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4520824916819809
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7975835511830169
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2539649001111626
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9998890216582561,
              "spearman": 0.9998028757761008,
              "auroc_top30_worst": 0.9999091428571428,
              "pairwise_seed_ranking": 0.9425,
              "predicted_best_mean_error": 1.748502210855484,
              "seed0_mean_error": 1.8214172512590885,
              "random_seed_mean_error": 1.8132706600129604,
              "oracle_best_mean_error": 1.7476961852610111,
              "improvement_over_seed0": 0.07291504040360453,
              "gap_to_oracle": 0.0008060255944728478,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5539844644069671
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7907083966255188
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.073986442232132
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.327986033185323
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8120445298671723
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.4691784143447886,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5377047340075174,
                  "rejected_mean_error": 4.2811026926040645,
                  "gap_rejected_minus_accepted": 2.743397958596547
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.122666656970978,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.327986033185323,
                  "rejected_mean_error": 3.26422001991272,
                  "gap_rejected_minus_accepted": 1.9362339867273968
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6262561082839966,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.073986442232132,
                  "rejected_mean_error": 2.5501026175022123,
                  "gap_rejected_minus_accepted": 1.4761161752700804
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1352596282958984,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7907083966255188,
                  "rejected_mean_error": 2.15248990761439,
                  "gap_rejected_minus_accepted": 1.3617815109888711
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.421168303489685,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5463899611433347,
                  "rejected_mean_error": 4.296662862300873,
                  "gap_rejected_minus_accepted": 2.750272901157538
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1418634057044983,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3385205315351487,
                  "rejected_mean_error": 3.2701074104309082,
                  "gap_rejected_minus_accepted": 1.9315868788957595
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6342365145683289,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0800529831051826,
                  "rejected_mean_error": 2.5627815194129946,
                  "gap_rejected_minus_accepted": 1.482728536307812
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1519332230091095,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7927702723741531,
                  "rejected_mean_error": 2.164299577554067,
                  "gap_rejected_minus_accepted": 1.371529305179914
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9704814964904689,
              "spearman": 0.9729263673876335,
              "auroc_top30_bad": 0.9947969523809523,
              "mae": 0.13401438615582884,
              "mse": 0.04831492431711731,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7431947036942144,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13619935220479965
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2371970204114914
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4443118129253387
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8102598437945048
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1942378834486007
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9514929837107746,
              "spearman": 0.9812239178393074,
              "auroc_top30_worst": 0.9921859047619047,
              "pairwise_seed_ranking": 0.9404,
              "predicted_best_mean_error": 1.6198202619552613,
              "seed0_mean_error": 1.7177031744718552,
              "random_seed_mean_error": 1.6985768196582793,
              "oracle_best_mean_error": 1.6184608579874038,
              "improvement_over_seed0": 0.09788291251659387,
              "gap_to_oracle": 0.0013594039678574976,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47412509632110594
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7627948449972348
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1088483905792237
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3730326073764483
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6955634710311889
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5999713182449344,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5400960127512613,
                  "rejected_mean_error": 3.094770595550537,
                  "gap_rejected_minus_accepted": 1.5546745827992756
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0778160095214844,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3721277847361284,
                  "rejected_mean_error": 2.6638038482148048,
                  "gap_rejected_minus_accepted": 1.2916760634786764
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.684229850769043,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1088483905792237,
                  "rejected_mean_error": 2.2822785514831545,
                  "gap_rejected_minus_accepted": 1.1734301609039308
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1199069023132324,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7635930864193949,
                  "rejected_mean_error": 2.0068833540445206,
                  "gap_rejected_minus_accepted": 1.2432902676251256
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.610587239265442,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5587486604849496,
                  "rejected_mean_error": 3.1482938003540037,
                  "gap_rejected_minus_accepted": 1.589545139869054
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.098983585834503,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3881005875885806,
                  "rejected_mean_error": 2.6960473609349083,
                  "gap_rejected_minus_accepted": 1.3079467733463277
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6999083161354065,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1284390933513642,
                  "rejected_mean_error": 2.306967255592346,
                  "gap_rejected_minus_accepted": 1.178528162240982
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1337567865848541,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7723909062998635,
                  "rejected_mean_error": 2.0361773610752536,
                  "gap_rejected_minus_accepted": 1.26378645477539
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9714087987776571,
              "spearman": 0.966809497751071,
              "auroc_top30_bad": 0.9772495238095239,
              "mae": 0.14126393939591944,
              "mse": 0.041206397547424646,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7270863770389769,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.16547212505340575
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2527323987722397
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6016492860913276
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9980875405708949
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3158914593279363
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9278452876100602,
              "spearman": 0.9400873922199053,
              "auroc_top30_worst": 0.9478521904761905,
              "pairwise_seed_ranking": 0.9232,
              "predicted_best_mean_error": 1.8019488706588744,
              "seed0_mean_error": 1.9027296719551086,
              "random_seed_mean_error": 1.8683821330070496,
              "oracle_best_mean_error": 1.8003094832897186,
              "improvement_over_seed0": 0.10078080129623412,
              "gap_to_oracle": 0.0016393873691558092,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.893724377155304
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2165797538100145
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4883241980552673
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6635434009245973
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8711545301914214
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4018408536911013,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7856816421614752,
                  "rejected_mean_error": 2.6404105224609373,
                  "gap_rejected_minus_accepted": 0.8547288802994621
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.063978135585785,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6631216490790328,
                  "rejected_mean_error": 2.493923889943205,
                  "gap_rejected_minus_accepted": 0.8308022408641722
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8151493072509766,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4883241980552673,
                  "rejected_mean_error": 2.2539848623275756,
                  "gap_rejected_minus_accepted": 0.7656606642723083
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4932079017162323,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2183560252951358,
                  "rejected_mean_error": 2.0892184918056556,
                  "gap_rejected_minus_accepted": 0.8708624665105198
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.502016282081604,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8114587630165948,
                  "rejected_mean_error": 2.724167852401733,
                  "gap_rejected_minus_accepted": 0.9127090893851384
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0805352330207825,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6770978745292215,
                  "rejected_mean_error": 2.5724621500287737,
                  "gap_rejected_minus_accepted": 0.8953642754995521
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.841181755065918,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4964107904434205,
                  "rejected_mean_error": 2.309048553466797,
                  "gap_rejected_minus_accepted": 0.8126377630233765
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5263825356960297,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2233074354746984,
                  "rejected_mean_error": 2.131625933443161,
                  "gap_rejected_minus_accepted": 0.9083184979684626
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9859625079008414,
              "spearman": 0.9649824817218493,
              "auroc_top30_bad": 0.9581821428571429,
              "mae": 0.10715486345021054,
              "mse": 0.019393888567454887,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7507184841629799,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07106475638225675
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17143534380942582
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.664313043359667
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0616300629004836
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9360303716709872,
              "spearman": 0.895977295977296,
              "auroc_top30_worst": 0.9588333333333334,
              "pairwise_seed_ranking": 0.8965,
              "predicted_best_mean_error": 1.8656305727362632,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.060599490702152314,
              "gap_to_oracle": 0.0023291856050491333,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.297503844499588
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.453640600681305
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6724577350616454
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7661205089886984
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2754021883010864,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8438070289293924,
                  "rejected_mean_error": 2.5533537101745605,
                  "gap_rejected_minus_accepted": 0.7095466812451681
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0912400484085083,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7661205089886984,
                  "rejected_mean_error": 2.360685261249542,
                  "gap_rejected_minus_accepted": 0.5945647522608437
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8887152075767517,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6724577350616454,
                  "rejected_mean_error": 2.157065659046173,
                  "gap_rejected_minus_accepted": 0.48460792398452757
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6582661867141724,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.453640600681305,
                  "rejected_mean_error": 2.068468729178111,
                  "gap_rejected_minus_accepted": 0.614828128496806
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2867432594299317,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.851836245589786,
                  "rejected_mean_error": 2.5957744240760805,
                  "gap_rejected_minus_accepted": 0.7439381784862944
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.107348084449768,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7711600534121195,
                  "rejected_mean_error": 2.3914400935173035,
                  "gap_rejected_minus_accepted": 0.620280040105184
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9012593030929565,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.682830379009247,
                  "rejected_mean_error": 2.1696297478675843,
                  "gap_rejected_minus_accepted": 0.4867993688583374
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.675787627696991,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.462044427394867,
                  "rejected_mean_error": 2.0809586087862653,
                  "gap_rejected_minus_accepted": 0.6189141813913983
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K5"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 61,
        "best_calib_loss": 0.018714411184191704,
        "train_time_sec": 41.478394508361816,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9994570627130929,
              "spearman": 0.9981090765666732,
              "auroc_top30_bad": 0.9995768571428572,
              "mae": 0.05291230946049327,
              "mse": 0.0046664323143926914,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8231712915141531,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.061593384971260094
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18907592472634277
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45226545188229067
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7979233736025014
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2539649001111626
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9996349022393083,
              "spearman": 0.9992134670965199,
              "auroc_top30_worst": 0.9993918095238095,
              "pairwise_seed_ranking": 0.9526,
              "predicted_best_mean_error": 1.7486473932266235,
              "seed0_mean_error": 1.8214172512590885,
              "random_seed_mean_error": 1.8132706600129604,
              "oracle_best_mean_error": 1.7476961852610111,
              "improvement_over_seed0": 0.07276985803246494,
              "gap_to_oracle": 0.0009512079656124328,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5546569669246674
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7914284522056579
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.074316970539093
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3281835821151733
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8120445298671723
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5504324913024905,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5377415206697251,
                  "rejected_mean_error": 4.2807716126441955,
                  "gap_rejected_minus_accepted": 2.7430300919744703
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.188590407371521,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3281835821151733,
                  "rejected_mean_error": 3.263627373123169,
                  "gap_rejected_minus_accepted": 1.9354437910079956
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6563007235527039,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.074316970539093,
                  "rejected_mean_error": 2.5497720891952516,
                  "gap_rejected_minus_accepted": 1.4754551186561586
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1486502587795258,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7914284522056579,
                  "rejected_mean_error": 2.152249889087677,
                  "gap_rejected_minus_accepted": 1.360821436882019
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.516526508331299,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5463576686713432,
                  "rejected_mean_error": 4.296953494548798,
                  "gap_rejected_minus_accepted": 2.7505958258774545
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2295747995376587,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3386744488477706,
                  "rejected_mean_error": 3.269645658493042,
                  "gap_rejected_minus_accepted": 1.9309712096452714
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6802226901054382,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0800583694577217,
                  "rejected_mean_error": 2.5627761330604555,
                  "gap_rejected_minus_accepted": 1.4827177636027338
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.175133228302002,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.793963854432106,
                  "rejected_mean_error": 2.1639017168680827,
                  "gap_rejected_minus_accepted": 1.3699378624359766
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9696788542088135,
              "spearman": 0.9701812750146626,
              "auroc_top30_bad": 0.9961432380952381,
              "mae": 0.1481994584224187,
              "mse": 0.052414890189869105,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7172809353218685,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.14802106717228888
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2331946008205414
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4443773118972778
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8092532254219055
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1942378834486007
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.953573660876916,
              "spearman": 0.9835000439680284,
              "auroc_top30_worst": 0.993152,
              "pairwise_seed_ranking": 0.9324,
              "predicted_best_mean_error": 1.619925833940506,
              "seed0_mean_error": 1.7177031744718552,
              "random_seed_mean_error": 1.6985768196582793,
              "oracle_best_mean_error": 1.6184608579874038,
              "improvement_over_seed0": 0.09777734053134912,
              "gap_to_oracle": 0.0014649759531022433,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46821538591384887
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7605012473769677
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1080570442199706
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.371439927930771
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6955634710311889
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5366597890853884,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5389623285929361,
                  "rejected_mean_error": 3.104973752975464,
                  "gap_rejected_minus_accepted": 1.5660114243825278
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.067841351032257,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3704639783918284,
                  "rejected_mean_error": 2.6687846358972616,
                  "gap_rejected_minus_accepted": 1.2983206575054331
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5479113459587097,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1080570442199706,
                  "rejected_mean_error": 2.2830698978424073,
                  "gap_rejected_minus_accepted": 1.1750128536224367
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9989490211009979,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7614309123148933,
                  "rejected_mean_error": 2.007605617112513,
                  "gap_rejected_minus_accepted": 1.2461747047976197
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.548677110671997,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5528720790810056,
                  "rejected_mean_error": 3.201183032989502,
                  "gap_rejected_minus_accepted": 1.6483109539084966
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1286391615867615,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3846020352712927,
                  "rejected_mean_error": 2.7064319527338423,
                  "gap_rejected_minus_accepted": 1.3218299174625496
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5698559880256653,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1290240485668182,
                  "rejected_mean_error": 2.306382300376892,
                  "gap_rejected_minus_accepted": 1.1773582518100738
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0459102988243103,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.771765123757105,
                  "rejected_mean_error": 2.0363881862099795,
                  "gap_rejected_minus_accepted": 1.2646230624528745
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9673013974212175,
              "spearman": 0.9602965375455605,
              "auroc_top30_bad": 0.9739009523809524,
              "mae": 0.1558530695439782,
              "mse": 0.04525422330590287,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6924195625240136,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.16957387036085128
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.28856371388435365
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6041055160641671
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9973244002103806
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3158914593279363
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9384279856923012,
              "spearman": 0.9324756041686693,
              "auroc_top30_worst": 0.9512411428571428,
              "pairwise_seed_ranking": 0.92,
              "predicted_best_mean_error": 1.8030371878147124,
              "seed0_mean_error": 1.9027296719551086,
              "random_seed_mean_error": 1.8683821330070496,
              "oracle_best_mean_error": 1.8003094832897186,
              "improvement_over_seed0": 0.09969248414039611,
              "gap_to_oracle": 0.0027277045249938237,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8930771450996399
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2133147779565592
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4981298577308655
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6597627483324202
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8711545301914214
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4203999757766725,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7834035988383823,
                  "rejected_mean_error": 2.6609129123687745,
                  "gap_rejected_minus_accepted": 0.8775093135303922
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1125332713127136,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6586407704821517,
                  "rejected_mean_error": 2.507337893921727,
                  "gap_rejected_minus_accepted": 0.8486971234395753
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7910966873168945,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4981298577308655,
                  "rejected_mean_error": 2.2441792026519773,
                  "gap_rejected_minus_accepted": 0.7460493449211119
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4506483674049377,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2148568651165825,
                  "rejected_mean_error": 2.09038736815132,
                  "gap_rejected_minus_accepted": 0.8755305030347373
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.534442687034607,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8045809390809802,
                  "rejected_mean_error": 2.7860682678222655,
                  "gap_rejected_minus_accepted": 0.9814873287412853
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1603190898895264,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6693532377640832,
                  "rejected_mean_error": 2.5954501988395813,
                  "gap_rejected_minus_accepted": 0.9260969610754981
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8030896186828613,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5048177785873413,
                  "rejected_mean_error": 2.300641565322876,
                  "gap_rejected_minus_accepted": 0.7958237867355344
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4821305572986603,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2244588817868913,
                  "rejected_mean_error": 2.1312380130278235,
                  "gap_rejected_minus_accepted": 0.9067791312409321
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9857426162125397,
              "spearman": 0.9730930762400858,
              "auroc_top30_bad": 0.9786928571428571,
              "mae": 0.10399353670352139,
              "mse": 0.02066415847462303,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.99,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7340367159619956,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11757393741980195
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17794226179271935
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6680276383198798
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.053181085191667
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9528675922829488,
              "spearman": 0.9414488094488095,
              "auroc_top30_worst": 0.9688285714285715,
              "pairwise_seed_ranking": 0.895,
              "predicted_best_mean_error": 1.8658231994509697,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.06040686398744577,
              "gap_to_oracle": 0.0025218123197556785,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3163643836975099
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.469188223838806
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6449183447360993
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.761094516913096
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3519030809402466,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8418075646294487,
                  "rejected_mean_error": 2.571348888874054,
                  "gap_rejected_minus_accepted": 0.7295413242446052
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.044410824775696,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.761094516913096,
                  "rejected_mean_error": 2.375763237476349,
                  "gap_rejected_minus_accepted": 0.6146687205632528
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8321608304977417,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6449183447360993,
                  "rejected_mean_error": 2.1846050493717195,
                  "gap_rejected_minus_accepted": 0.5396867046356202
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6140550374984741,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.469188223838806,
                  "rejected_mean_error": 2.0632861881256104,
                  "gap_rejected_minus_accepted": 0.5940979642868043
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3807098627090455,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8515371256404454,
                  "rejected_mean_error": 2.5984665036201475,
                  "gap_rejected_minus_accepted": 0.7469293779797022
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0536128282546997,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.770752724011739,
                  "rejected_mean_error": 2.392662081718445,
                  "gap_rejected_minus_accepted": 0.6219093577067059
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8505387902259827,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6509274911880494,
                  "rejected_mean_error": 2.201532635688782,
                  "gap_rejected_minus_accepted": 0.5506051445007325
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6211173236370087,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4757307934761048,
                  "rejected_mean_error": 2.0763964867591858,
                  "gap_rejected_minus_accepted": 0.600665693283081
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K5"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 53,
        "best_calib_loss": 0.01931264065206051,
        "train_time_sec": 29.201967239379883,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997108016879208,
              "spearman": 0.9984902698975683,
              "auroc_top30_bad": 0.999849380952381,
              "mae": 0.022623417213431096,
              "mse": 0.0008837199034691837,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.808298817328582,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06047499255219009
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18845659821233712
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4522179563025711
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7975545873946666
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2539649001111626
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9998067368024964,
              "spearman": 0.9996948191317854,
              "auroc_top30_worst": 0.9997093333333333,
              "pairwise_seed_ranking": 0.951,
              "predicted_best_mean_error": 1.7485231047570706,
              "seed0_mean_error": 1.8214172512590885,
              "random_seed_mean_error": 1.8132706600129604,
              "oracle_best_mean_error": 1.7476961852610111,
              "improvement_over_seed0": 0.07289414650201786,
              "gap_to_oracle": 0.0008269194960595083,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5538540643453598
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7907889559745789
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0740126815319062
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.328000098355611
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8120445298671723
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.4607493162155154,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.537724332438575,
                  "rejected_mean_error": 4.280926306724548,
                  "gap_rejected_minus_accepted": 2.743201974285973
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1295018196105957,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.328000098355611,
                  "rejected_mean_error": 3.2641778244018553,
                  "gap_rejected_minus_accepted": 1.9361777260462443
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6228547096252441,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0740126815319062,
                  "rejected_mean_error": 2.5500763782024385,
                  "gap_rejected_minus_accepted": 1.4760636966705323
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1286670863628387,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7907889559745789,
                  "rejected_mean_error": 2.1524630544980368,
                  "gap_rejected_minus_accepted": 1.3616740985234579
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.429883146286011,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5463958813415632,
                  "rejected_mean_error": 4.296609580516815,
                  "gap_rejected_minus_accepted": 2.750213699175252
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1564878821372986,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.338464148402214,
                  "rejected_mean_error": 3.270276559829712,
                  "gap_rejected_minus_accepted": 1.931812411427498
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.632598876953125,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0800247591137886,
                  "rejected_mean_error": 2.5628097434043884,
                  "gap_rejected_minus_accepted": 1.4827849842905998
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1442101299762726,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7928706918954849,
                  "rejected_mean_error": 2.1642661043802898,
                  "gap_rejected_minus_accepted": 1.371395412484805
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9701583028778453,
              "spearman": 0.9739501212096293,
              "auroc_top30_bad": 0.9918438095238095,
              "mae": 0.14819774079429918,
              "mse": 0.0600057004196154,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6918134128329684,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1168054881989956
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2217246120452881
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.44812195019721984
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8127264962832133
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1942378834486007
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9478003952171754,
              "spearman": 0.97242053095714,
              "auroc_top30_worst": 0.9854872380952381,
              "pairwise_seed_ranking": 0.9332,
              "predicted_best_mean_error": 1.6199739611148833,
              "seed0_mean_error": 1.7177031744718552,
              "random_seed_mean_error": 1.6985768196582793,
              "oracle_best_mean_error": 1.6184608579874038,
              "improvement_over_seed0": 0.09772921335697182,
              "gap_to_oracle": 0.0015131031274795426,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47742673873901365
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7792447841702363
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1117116720199585
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3725911625412737
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6955634710311889
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.440722799301148,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.538551758872138,
                  "rejected_mean_error": 3.1086688804626466,
                  "gap_rejected_minus_accepted": 1.5701171215905085
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9464598596096039,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3719311044208522,
                  "rejected_mean_error": 2.6643926324174045,
                  "gap_rejected_minus_accepted": 1.2924615279965523
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5699456334114075,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1117116720199585,
                  "rejected_mean_error": 2.2794152700424193,
                  "gap_rejected_minus_accepted": 1.1677035980224608
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0967203378677368,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7802202193120036,
                  "rejected_mean_error": 2.0013291463653458,
                  "gap_rejected_minus_accepted": 1.2211089270533422
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.456113839149475,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.554233069817225,
                  "rejected_mean_error": 3.188934116363525,
                  "gap_rejected_minus_accepted": 1.6347010465463
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.981075942516327,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3862880052410982,
                  "rejected_mean_error": 2.7014275656806097,
                  "gap_rejected_minus_accepted": 1.3151395604395115
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5853718519210815,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1319167973995208,
                  "rejected_mean_error": 2.3034895515441893,
                  "gap_rejected_minus_accepted": 1.1715727541446685
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1059418618679047,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.791988773478402,
                  "rejected_mean_error": 2.0295748710632324,
                  "gap_rejected_minus_accepted": 1.2375860975848303
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9672356644900564,
              "spearman": 0.9638606139346378,
              "auroc_top30_bad": 0.9779630476190476,
              "mae": 0.16927032056543975,
              "mse": 0.055594122943073566,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.6696245566505901,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.16744522207975387
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.27323590171337125
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6050700115323067
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9954646942218145
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3158914593279363
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9312899742183652,
              "spearman": 0.936770739084153,
              "auroc_top30_worst": 0.9590582857142856,
              "pairwise_seed_ranking": 0.9104,
              "predicted_best_mean_error": 1.8025926830768586,
              "seed0_mean_error": 1.9027296719551086,
              "random_seed_mean_error": 1.8683821330070496,
              "oracle_best_mean_error": 1.8003094832897186,
              "improvement_over_seed0": 0.10013698887824996,
              "gap_to_oracle": 0.002283199787139978,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9141340670585633
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2182227634848692
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4857894619941712
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.665210746562303
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8711545301914214
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2561737298965454,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7863724168671502,
                  "rejected_mean_error": 2.6341935501098632,
                  "gap_rejected_minus_accepted": 0.847821133242713
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.983381986618042,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.664428716598987,
                  "rejected_mean_error": 2.490011039252479,
                  "gap_rejected_minus_accepted": 0.825582322653492
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7335945963859558,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4857894619941712,
                  "rejected_mean_error": 2.256519598388672,
                  "gap_rejected_minus_accepted": 0.7707301363945007
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4054035246372223,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.220299531286136,
                  "rejected_mean_error": 2.0885692736891315,
                  "gap_rejected_minus_accepted": 0.8682697424029955
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3450872898101807,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8107480594846936,
                  "rejected_mean_error": 2.7305641841888426,
                  "gap_rejected_minus_accepted": 0.919816124704149
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0071998238563538,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6749853157104655,
                  "rejected_mean_error": 2.578732761125716,
                  "gap_rejected_minus_accepted": 0.9037474454152503
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7678180932998657,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4920761289596558,
                  "rejected_mean_error": 2.3133832149505613,
                  "gap_rejected_minus_accepted": 0.8213070859909055
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4395157098770142,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2267417983403281,
                  "rejected_mean_error": 2.1304689021034036,
                  "gap_rejected_minus_accepted": 0.9037271037630754
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9855678050297567,
              "spearman": 0.9714262034430979,
              "auroc_top30_bad": 0.9682821428571428,
              "mae": 0.12864887773612282,
              "mse": 0.027662175704768272,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7036475018400717,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09357847096398472
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17506984487920998
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6628421021737159
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0565170576597254
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9395197774285011,
              "spearman": 0.9257140097140097,
              "auroc_top30_worst": 0.9687190476190477,
              "pairwise_seed_ranking": 0.916,
              "predicted_best_mean_error": 1.866938963830471,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.05929109960794454,
              "gap_to_oracle": 0.003637576699256906,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.292753779888153
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.450245822429657
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6527394335269927
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7630768772761027
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2883432865142823,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8505381724569532,
                  "rejected_mean_error": 2.4927734184265136,
                  "gap_rejected_minus_accepted": 0.6422352459695604
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.001784324645996,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7630768772761027,
                  "rejected_mean_error": 2.369816156387329,
                  "gap_rejected_minus_accepted": 0.6067392791112263
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7496894598007202,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6527394335269927,
                  "rejected_mean_error": 2.176783960580826,
                  "gap_rejected_minus_accepted": 0.5240445270538332
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5547919273376465,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.450245822429657,
                  "rejected_mean_error": 2.06960032192866,
                  "gap_rejected_minus_accepted": 0.619354499499003
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3054852962493895,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8645066963301764,
                  "rejected_mean_error": 2.4817403674125673,
                  "gap_rejected_minus_accepted": 0.6172336710823909
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9995974004268646,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.769446841875712,
                  "rejected_mean_error": 2.3965797281265258,
                  "gap_rejected_minus_accepted": 0.6271328862508136
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7521529793739319,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.655570446252823,
                  "rejected_mean_error": 2.1968896806240084,
                  "gap_rejected_minus_accepted": 0.5413192343711855
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5733659267425537,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4644346809387208,
                  "rejected_mean_error": 2.0801618576049803,
                  "gap_rejected_minus_accepted": 0.6157271766662595
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K5"
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
        "best_epoch": 72,
        "best_calib_loss": 0.05021972209215164,
        "train_time_sec": 11.039316177368164,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9866007526894951,
              "spearman": 0.9426857100104975,
              "auroc_top30_bad": 0.9989812380952379,
              "mae": 0.09534712349089096,
              "mse": 0.030200535425017723,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.512,
              "expert_lt_simvla_seed0": 0.982,
              "same_context_pred_std": 0.8123743905482965,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2721117549063638
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2908670677659567
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4209660795884905
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7716484494022249
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2337197005012421
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9990770229074861,
              "spearman": 0.9986830655872911,
              "auroc_top30_worst": 0.9993967619047619,
              "pairwise_seed_ranking": 0.8574,
              "predicted_best_mean_error": 1.7494538143873215,
              "seed0_mean_error": 1.8170942743122578,
              "random_seed_mean_error": 1.809038346260786,
              "oracle_best_mean_error": 1.7438368230164052,
              "improvement_over_seed0": 0.06764045992493628,
              "gap_to_oracle": 0.005616991370916313,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.547314692735672
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7833792380332947
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0677808078289033
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.323081129137675
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8077851967811585
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.492646336555482,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5333300062285529,
                  "rejected_mean_error": 4.2778819117546085,
                  "gap_rejected_minus_accepted": 2.7445519055260554
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.124574899673462,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.323081129137675,
                  "rejected_mean_error": 3.261897399711609,
                  "gap_rejected_minus_accepted": 1.938816270573934
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6168547868728638,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0677808078289033,
                  "rejected_mean_error": 2.5477895857334136,
                  "gap_rejected_minus_accepted": 1.4800087779045104
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.109177678823471,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7833792380332947,
                  "rejected_mean_error": 2.149253849697113,
                  "gap_rejected_minus_accepted": 1.3658746116638183
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.530346441268922,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.541816949877474,
                  "rejected_mean_error": 4.294590194225311,
                  "gap_rejected_minus_accepted": 2.7527732443478365
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.132875084877014,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3334581912755967,
                  "rejected_mean_error": 3.268002523422241,
                  "gap_rejected_minus_accepted": 1.9345443321466445
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6324366331100464,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0737448244690895,
                  "rejected_mean_error": 2.560443724155426,
                  "gap_rejected_minus_accepted": 1.4866988996863366
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1256432831287384,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7851142030954361,
                  "rejected_mean_error": 2.1610876313845315,
                  "gap_rejected_minus_accepted": 1.3759734282890954
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8772597420343301,
              "spearman": 0.8848548154360336,
              "auroc_top30_bad": 0.9670605714285714,
              "mae": 0.2961829466819763,
              "mse": 0.18932313050223815,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.46,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.7015719841489428,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2883338452279568
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.34607027101516724
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.48323150893449784
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8306274194955826
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1911071869909764
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7321499557968029,
              "spearman": 0.8143002213761417,
              "auroc_top30_worst": 0.9060297142857143,
              "pairwise_seed_ranking": 0.8224,
              "predicted_best_mean_error": 1.6262203234434127,
              "seed0_mean_error": 1.716470638871193,
              "random_seed_mean_error": 1.6973294532299041,
              "oracle_best_mean_error": 1.617486641049385,
              "improvement_over_seed0": 0.09025031542778028,
              "gap_to_oracle": 0.008733682394027609,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6329332792758942
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9308810255084282
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.172006719684601
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4346593971699795
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.694315631389618
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4157703399658215,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6387473368114895,
                  "rejected_mean_error": 2.1944302825927733,
                  "gap_rejected_minus_accepted": 0.5556829457812837
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0070942640304565,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4338529015808756,
                  "rejected_mean_error": 2.4740395222228173,
                  "gap_rejected_minus_accepted": 1.0401866206419417
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.58676415681839,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.172006719684601,
                  "rejected_mean_error": 2.216624543094635,
                  "gap_rejected_minus_accepted": 1.044617823410034
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.123807668685913,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9330003735737298,
                  "rejected_mean_error": 1.9486290526237406,
                  "gap_rejected_minus_accepted": 1.0156286790500109
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.471336340904236,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6627256166934967,
                  "rejected_mean_error": 2.200175838470459,
                  "gap_rejected_minus_accepted": 0.5374502217769623
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0363240838050842,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4487847645971226,
                  "rejected_mean_error": 2.5110302974307346,
                  "gap_rejected_minus_accepted": 1.062245532833612
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6267715692520142,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.186547711610794,
                  "rejected_mean_error": 2.2463935661315917,
                  "gap_rejected_minus_accepted": 1.0598458545207976
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1650528609752655,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9620279636647966,
                  "rejected_mean_error": 1.9706411658123852,
                  "gap_rejected_minus_accepted": 1.0086132021475886
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8241151819757104,
              "spearman": 0.8145173962795649,
              "auroc_top30_bad": 0.9085912380952381,
              "mae": 0.3782925938367844,
              "mse": 0.26547996082355535,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.651123284115301,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4149901616573334
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4359623934984207
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6563105406045914
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0555950500011444
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3136809441208839
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.592847372399366,
              "spearman": 0.6174950429292999,
              "auroc_top30_worst": 0.7508236190476191,
              "pairwise_seed_ranking": 0.7644,
              "predicted_best_mean_error": 1.8212368640899659,
              "seed0_mean_error": 1.9024355149269103,
              "random_seed_mean_error": 1.868010503768921,
              "oracle_best_mean_error": 1.8000093309879304,
              "improvement_over_seed0": 0.08119865083694444,
              "gap_to_oracle": 0.021227533102035512,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.184197991371155
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.397431866862835
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6040614110946656
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.755212483121388
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8708093903064729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.06362566947937,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.818135807249281,
                  "rejected_mean_error": 2.3448716378211976,
                  "gap_rejected_minus_accepted": 0.5267358305719165
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8134788870811462,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7548231640900211,
                  "rejected_mean_error": 2.218026942909716,
                  "gap_rejected_minus_accepted": 0.463203778819695
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5554540157318115,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.6040614110946656,
                  "rejected_mean_error": 2.13755736951828,
                  "gap_rejected_minus_accepted": 0.5334959584236145
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2597684562206268,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3980846203173312,
                  "rejected_mean_error": 2.028720652853539,
                  "gap_rejected_minus_accepted": 0.6306360325362079
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0789211511611936,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8333870580461291,
                  "rejected_mean_error": 2.5238716268539427,
                  "gap_rejected_minus_accepted": 0.6904845688078136
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8278359472751617,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7695421343818705,
                  "rejected_mean_error": 2.29689681908441,
                  "gap_rejected_minus_accepted": 0.5273546847025394
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6014613509178162,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6053291883468628,
                  "rejected_mean_error": 2.199541841506958,
                  "gap_rejected_minus_accepted": 0.5942126531600951
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2852822244167328,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.398932865687779,
                  "rejected_mean_error": 2.072064749697313,
                  "gap_rejected_minus_accepted": 0.6731318840095337
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.7546268245232044,
              "spearman": 0.7693653153538285,
              "auroc_top30_bad": 0.8591499999999999,
              "mae": 0.46020167436264453,
              "mse": 0.36708245709740506,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.505,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.60405578317709,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4552286387979984
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4896078139618039
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7781878435947001
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0882889431342482
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.37281256990966416,
              "spearman": 0.4156400956400957,
              "auroc_top30_worst": 0.7645857142857142,
              "pairwise_seed_ranking": 0.7085,
              "predicted_best_mean_error": 1.8871793949604034,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.039050668478012085,
              "gap_to_oracle": 0.023878007829189363,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.8438217294216157
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.7981654019355775
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.7691198401451111
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.833114194393158
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1173799514770506,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8837147743172116,
                  "rejected_mean_error": 2.1941840016841887,
                  "gap_rejected_minus_accepted": 0.31046922736697713
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.895820677280426,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.833114194393158,
                  "rejected_mean_error": 2.1597042050361632,
                  "gap_rejected_minus_accepted": 0.3265900106430053
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4536179304122925,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.7691198401451111,
                  "rejected_mean_error": 2.0604035539627077,
                  "gap_rejected_minus_accepted": 0.29128371381759655
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9621346592903137,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.7981654019355775,
                  "rejected_mean_error": 1.95362712876002,
                  "gap_rejected_minus_accepted": 0.15546172682444248
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1058924913406374,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.9037441770235697,
                  "rejected_mean_error": 2.1286030411720276,
                  "gap_rejected_minus_accepted": 0.2248588641484579
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9203486144542694,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.848765709400177,
                  "rejected_mean_error": 2.158623125553131,
                  "gap_rejected_minus_accepted": 0.3098574161529539
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4864433407783508,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.7906960380077361,
                  "rejected_mean_error": 2.061764088869095,
                  "gap_rejected_minus_accepted": 0.27106805086135877
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0054174661636353,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.799905161857605,
                  "rejected_mean_error": 1.9683383639653524,
                  "gap_rejected_minus_accepted": 0.16843320210774748
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
        "best_calib_loss": 0.020984526723623276,
        "train_time_sec": 35.20964980125427,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997294050247725,
              "spearman": 0.9986792892741821,
              "auroc_top30_bad": 0.9997483809523809,
              "mae": 0.02012295100732008,
              "mse": 0.0006637066892811637,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8061930700299115,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0598679383037379
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17476031105271542
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.41688782417352777
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7711902781935254
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2337197005012421
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997748055072508,
              "spearman": 0.9995379566615072,
              "auroc_top30_worst": 0.999688380952381,
              "pairwise_seed_ranking": 0.937,
              "predicted_best_mean_error": 1.7448336240947246,
              "seed0_mean_error": 1.8170942743122578,
              "random_seed_mean_error": 1.809038346260786,
              "oracle_best_mean_error": 1.7438368230164052,
              "improvement_over_seed0": 0.07226065021753314,
              "gap_to_oracle": 0.0009968010783194536,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5463290895223618
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7828682173728942
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0672730689048766
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.322788136100769
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8077851967811585
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.4221706867218034,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5332090827094185,
                  "rejected_mean_error": 4.2789702234268185,
                  "gap_rejected_minus_accepted": 2.7457611407174003
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1140844225883484,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.322788136100769,
                  "rejected_mean_error": 3.2627763788223265,
                  "gap_rejected_minus_accepted": 1.9399882427215576
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6034901142120361,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0672730689048766,
                  "rejected_mean_error": 2.5482973246574403,
                  "gap_rejected_minus_accepted": 1.4810242557525637
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1136219203472137,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7828682173728942,
                  "rejected_mean_error": 2.1494241899172466,
                  "gap_rejected_minus_accepted": 1.3665559725443523
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.385867333412171,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5417988356285626,
                  "rejected_mean_error": 4.294753222465515,
                  "gap_rejected_minus_accepted": 2.7529543868369526
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1419352889060974,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3331817827622097,
                  "rejected_mean_error": 3.2688317489624024,
                  "gap_rejected_minus_accepted": 1.9356499662001927
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6101070642471313,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.073308453142643,
                  "rejected_mean_error": 2.5608800954818727,
                  "gap_rejected_minus_accepted": 1.4875716423392298
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1327031254768372,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7843817878961563,
                  "rejected_mean_error": 2.1613317697842915,
                  "gap_rejected_minus_accepted": 1.3769499818881352
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9583407198142084,
              "spearman": 0.9700863872488605,
              "auroc_top30_bad": 0.994071619047619,
              "mae": 0.15825618701949715,
              "mse": 0.06699639053962728,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7344099138347217,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13020548164844514
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2292728184223175
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.43900680023431776
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8075542050758998
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1911071869909764
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9138587867178011,
              "spearman": 0.9704850038304026,
              "auroc_top30_worst": 0.9854171428571428,
              "pairwise_seed_ranking": 0.9472,
              "predicted_best_mean_error": 1.618729144692421,
              "seed0_mean_error": 1.716470638871193,
              "random_seed_mean_error": 1.6973294532299041,
              "oracle_best_mean_error": 1.617486641049385,
              "improvement_over_seed0": 0.09774149417877198,
              "gap_to_oracle": 0.0012425036430359082,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4686605997085571
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7629512466299229
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1087332592010497
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3775968580866165
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.694315631389618
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.550305843353272,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.560955428123474,
                  "rejected_mean_error": 2.8945574607849123,
                  "gap_rejected_minus_accepted": 1.3336020326614382
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.072847604751587,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3768768141338386,
                  "rejected_mean_error": 2.6446037201073986,
                  "gap_rejected_minus_accepted": 1.26772690597356
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6648032069206238,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1087332592010497,
                  "rejected_mean_error": 2.279898003578186,
                  "gap_rejected_minus_accepted": 1.1711647443771362
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0727854073047638,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7636785467211812,
                  "rejected_mean_error": 2.0051901324581567,
                  "gap_rejected_minus_accepted": 1.2415115857369754
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5958339929580685,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.581766441795561,
                  "rejected_mean_error": 2.92880841255188,
                  "gap_rejected_minus_accepted": 1.3470419707563188
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0968106389045715,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3902541394220953,
                  "rejected_mean_error": 2.684764057870895,
                  "gap_rejected_minus_accepted": 1.2945099184487998
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6968839764595032,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1280360729694368,
                  "rejected_mean_error": 2.304905204772949,
                  "gap_rejected_minus_accepted": 1.1768691318035123
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1039879620075226,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7738139179963914,
                  "rejected_mean_error": 2.034050175850404,
                  "gap_rejected_minus_accepted": 1.2602362578540127
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9644258335667232,
              "spearman": 0.9606067478204264,
              "auroc_top30_bad": 0.9763702857142856,
              "mae": 0.1636142601378262,
              "mse": 0.05283823121391926,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7160066411892517,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.16184761661291122
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.26176250150203706
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5982371716737748
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9964336645285289
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3136809441208839
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9071041878430934,
              "spearman": 0.9299138740132271,
              "auroc_top30_worst": 0.9378834285714287,
              "pairwise_seed_ranking": 0.9104,
              "predicted_best_mean_error": 1.8028666579723358,
              "seed0_mean_error": 1.9024355149269103,
              "random_seed_mean_error": 1.868010503768921,
              "oracle_best_mean_error": 1.8000093309879304,
              "improvement_over_seed0": 0.09956885695457451,
              "gap_to_oracle": 0.0028573269844054394,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8968119292259217
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2167594354504194
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4861552430152893
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6698221041322516
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8708093903064729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3269227981567386,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7904125534163582,
                  "rejected_mean_error": 2.5943809223175047,
                  "gap_rejected_minus_accepted": 0.8039683689011465
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.042454719543457,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6694804888652,
                  "rejected_mean_error": 2.4735096479757144,
                  "gap_rejected_minus_accepted": 0.8040291591105144
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8037354350090027,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4861552430152893,
                  "rejected_mean_error": 2.2554635375976564,
                  "gap_rejected_minus_accepted": 0.769308294582367
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4761188626289368,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.217647481459779,
                  "rejected_mean_error": 2.0889947451293276,
                  "gap_rejected_minus_accepted": 0.8713472636695485
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.412621212005615,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.812881858083937,
                  "rejected_mean_error": 2.708418426513672,
                  "gap_rejected_minus_accepted": 0.895536568429735
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0542386770248413,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.678811852944726,
                  "rejected_mean_error": 2.5662073370010132,
                  "gap_rejected_minus_accepted": 0.8873954840562872
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8117467164993286,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4943508071899414,
                  "rejected_mean_error": 2.3105202226638792,
                  "gap_rejected_minus_accepted": 0.8161694154739378
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4936673641204834,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2186957654498873,
                  "rejected_mean_error": 2.1327863396170303,
                  "gap_rejected_minus_accepted": 0.914090574167143
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9790434687873395,
              "spearman": 0.9646508795492944,
              "auroc_top30_bad": 0.9649380952380953,
              "mae": 0.1354769594781101,
              "mse": 0.03102555840696883,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7311706237755362,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0825620754994452
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18345173317939042
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6669365960396826
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0580163257146875
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9273803072709488,
              "spearman": 0.9058564138564138,
              "auroc_top30_worst": 0.9643714285714287,
              "pairwise_seed_ranking": 0.904,
              "predicted_best_mean_error": 1.8656823441386223,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.06054771929979319,
              "gap_to_oracle": 0.0023809570074082576,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3262064862251282
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4628621592521667
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6609485137462616
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.765138571103414
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.262498664855957,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8458532624774509,
                  "rejected_mean_error": 2.5349376082420347,
                  "gap_rejected_minus_accepted": 0.6890843457645839
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.057062327861786,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.765138571103414,
                  "rejected_mean_error": 2.3636310749053955,
                  "gap_rejected_minus_accepted": 0.5984925038019815
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8598612546920776,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6609485137462616,
                  "rejected_mean_error": 2.168574880361557,
                  "gap_rejected_minus_accepted": 0.5076263666152954
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5701931416988373,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4628621592521667,
                  "rejected_mean_error": 2.065394876321157,
                  "gap_rejected_minus_accepted": 0.6025327170689903
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.266794729232788,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.857996526029375,
                  "rejected_mean_error": 2.5403319001197815,
                  "gap_rejected_minus_accepted": 0.6823353740904066
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.061495542526245,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.769446841875712,
                  "rejected_mean_error": 2.3965797281265258,
                  "gap_rejected_minus_accepted": 0.6271328862508136
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8651911616325378,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6690668308734893,
                  "rejected_mean_error": 2.1833932960033415,
                  "gap_rejected_minus_accepted": 0.5143264651298523
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6029505729675293,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.471254470348358,
                  "rejected_mean_error": 2.0778885944684347,
                  "gap_rejected_minus_accepted": 0.6066341241200766
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K10"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 66,
        "best_calib_loss": 0.01710183173418045,
        "train_time_sec": 41.47847366333008,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9993071270898435,
              "spearman": 0.9973525129922319,
              "auroc_top30_bad": 0.9993546666666666,
              "mae": 0.038686780982988424,
              "mse": 0.002453094659567729,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8241245702359177,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.061715518099605106
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17584223933569157
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.41699441793735603
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7714927689683158
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2337197005012421
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.999442396345584,
              "spearman": 0.9987259841889784,
              "auroc_top30_worst": 0.999224761904762,
              "pairwise_seed_ranking": 0.9582,
              "predicted_best_mean_error": 1.745110033750534,
              "seed0_mean_error": 1.8170942743122578,
              "random_seed_mean_error": 1.809038346260786,
              "oracle_best_mean_error": 1.7438368230164052,
              "improvement_over_seed0": 0.0719842405617237,
              "gap_to_oracle": 0.0012732107341288934,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5473093214035034
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7837806636810303
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0676000548362732
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3229257123947145
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8077851967811585
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.53377606868744,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5331964822875128,
                  "rejected_mean_error": 4.279083627223969,
                  "gap_rejected_minus_accepted": 2.745887144936456
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1619972586631775,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3229257123947145,
                  "rejected_mean_error": 3.262363649940491,
                  "gap_rejected_minus_accepted": 1.9394379375457764
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6372648477554321,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0676000548362732,
                  "rejected_mean_error": 2.5479703387260435,
                  "gap_rejected_minus_accepted": 1.4803702838897703
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1330944001674652,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7837806636810303,
                  "rejected_mean_error": 2.1491200411478677,
                  "gap_rejected_minus_accepted": 1.3653393774668374
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.4723910570144656,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5418473222851754,
                  "rejected_mean_error": 4.294316842555999,
                  "gap_rejected_minus_accepted": 2.7524695202708243
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1956111192703247,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.333421856602033,
                  "rejected_mean_error": 3.268111527442932,
                  "gap_rejected_minus_accepted": 1.9346896708408992
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6572495698928833,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.07357243424654,
                  "rejected_mean_error": 2.5606161143779755,
                  "gap_rejected_minus_accepted": 1.4870436801314355
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1515023410320282,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7857514063119888,
                  "rejected_mean_error": 2.1608752303123473,
                  "gap_rejected_minus_accepted": 1.3751238240003585
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9758363707336002,
              "spearman": 0.9708720023742267,
              "auroc_top30_bad": 0.9952319999999999,
              "mae": 0.14077577206492425,
              "mse": 0.0457786053800206,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7214605273053478,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1279321777820587
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2398515127658844
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.43892629491090773
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8048282000303268
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1911071869909764
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9652812474454038,
              "spearman": 0.9827282710580936,
              "auroc_top30_worst": 0.9938895238095238,
              "pairwise_seed_ranking": 0.936,
              "predicted_best_mean_error": 1.6186256638765335,
              "seed0_mean_error": 1.716470638871193,
              "random_seed_mean_error": 1.6973294532299041,
              "oracle_best_mean_error": 1.617486641049385,
              "improvement_over_seed0": 0.0978449749946595,
              "gap_to_oracle": 0.0011390228271483949,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4682855496406555
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7580053878900332
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1086330591201783
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.369024791824284
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.694315631389618
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.49425392150879,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5323713293075563,
                  "rejected_mean_error": 3.151814350128174,
                  "gap_rejected_minus_accepted": 1.6194430208206176
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0697988271713257,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.368047945400185,
                  "rejected_mean_error": 2.671033911811658,
                  "gap_rejected_minus_accepted": 1.3029859664114731
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5538684129714966,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1086330591201783,
                  "rejected_mean_error": 2.2799982036590576,
                  "gap_rejected_minus_accepted": 1.1713651445388793
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0345114469528198,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7588189310920886,
                  "rejected_mean_error": 2.006813461905228,
                  "gap_rejected_minus_accepted": 1.2479945308131395
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5298758029937742,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5468010993798573,
                  "rejected_mean_error": 3.243496494293213,
                  "gap_rejected_minus_accepted": 1.6966953949133556
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0998000502586365,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3807750546677227,
                  "rejected_mean_error": 2.7129003888084773,
                  "gap_rejected_minus_accepted": 1.3321253341407546
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5576149821281433,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1274984476566314,
                  "rejected_mean_error": 2.3054428300857546,
                  "gap_rejected_minus_accepted": 1.1779443824291231
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0840643048286438,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7674214882510049,
                  "rejected_mean_error": 2.03620377517639,
                  "gap_rejected_minus_accepted": 1.2687822869253853
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9693213474389049,
              "spearman": 0.9649029212839147,
              "auroc_top30_bad": 0.9814339047619047,
              "mae": 0.15300220282748342,
              "mse": 0.045601412357638954,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7130873797153914,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.17895186066627503
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2681164137840271
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6005748286485671
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.992224230146408
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3136809441208839
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9378798285186732,
              "spearman": 0.9438959435272282,
              "auroc_top30_worst": 0.9642331428571428,
              "pairwise_seed_ranking": 0.9092,
              "predicted_best_mean_error": 1.80326207613945,
              "seed0_mean_error": 1.9024355149269103,
              "random_seed_mean_error": 1.868010503768921,
              "oracle_best_mean_error": 1.8000093309879304,
              "improvement_over_seed0": 0.09917343878746032,
              "gap_to_oracle": 0.0032527451515196315,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9186191506385804
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2213429596561651
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4850287545204162
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6590899346606818
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8708093903064729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.436782550811768,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7851982278294034,
                  "rejected_mean_error": 2.6413098526000978,
                  "gap_rejected_minus_accepted": 0.8561116247706944
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0893722772598267,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6580732907531355,
                  "rejected_mean_error": 2.507658352867102,
                  "gap_rejected_minus_accepted": 0.8495850621139664
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7930328249931335,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4850287545204162,
                  "rejected_mean_error": 2.256590026092529,
                  "gap_rejected_minus_accepted": 0.771561271572113
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.445755809545517,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2223706727210706,
                  "rejected_mean_error": 2.0874169875361748,
                  "gap_rejected_minus_accepted": 0.8650463148151042
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.564808392524719,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8085122887293499,
                  "rejected_mean_error": 2.7477445507049563,
                  "gap_rejected_minus_accepted": 0.9392322619756064
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1618326902389526,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6673092593483747,
                  "rejected_mean_error": 2.600349956088596,
                  "gap_rejected_minus_accepted": 0.9330406967402212
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8192195296287537,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.491366858482361,
                  "rejected_mean_error": 2.31350417137146,
                  "gap_rejected_minus_accepted": 0.8221373128890992
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.456284761428833,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2308713481539773,
                  "rejected_mean_error": 2.128684405337043,
                  "gap_rejected_minus_accepted": 0.8978130571830656
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9826842432055454,
              "spearman": 0.9731573987896739,
              "auroc_top30_bad": 0.9805797619047618,
              "mae": 0.12707363243412692,
              "mse": 0.02859110093937115,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7484109239510498,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11879093462601303
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19175516087561845
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6638513383902609
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0528874228820204
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9619546526582318,
              "spearman": 0.9457564777564779,
              "auroc_top30_worst": 0.9905142857142857,
              "pairwise_seed_ranking": 0.9175,
              "predicted_best_mean_error": 1.8647672888636588,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.061462774574756684,
              "gap_to_oracle": 0.0014659017324447632,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2883612883090974
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4512395796775819
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.64892778301239
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.759393754641215
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.319090723991394,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8451184381379022,
                  "rejected_mean_error": 2.5415510272979738,
                  "gap_rejected_minus_accepted": 0.6964325891600716
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0643593072891235,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.759393754641215,
                  "rejected_mean_error": 2.380865524291992,
                  "gap_rejected_minus_accepted": 0.621471769650777
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8457419872283936,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.64892778301239,
                  "rejected_mean_error": 2.1805956110954283,
                  "gap_rejected_minus_accepted": 0.5316678280830383
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6176092028617859,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4512395796775819,
                  "rejected_mean_error": 2.069269069512685,
                  "gap_rejected_minus_accepted": 0.6180294898351033
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.347907829284668,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8579015003310309,
                  "rejected_mean_error": 2.5411871314048766,
                  "gap_rejected_minus_accepted": 0.6832856310738458
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.053837776184082,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7676159159342448,
                  "rejected_mean_error": 2.402072505950928,
                  "gap_rejected_minus_accepted": 0.634456590016683
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8597050309181213,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6485533511638641,
                  "rejected_mean_error": 2.203906775712967,
                  "gap_rejected_minus_accepted": 0.555353424549103
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6334631443023682,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4618150615692138,
                  "rejected_mean_error": 2.0810350640614828,
                  "gap_rejected_minus_accepted": 0.6192200024922689
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K10"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 60,
        "best_calib_loss": 0.02120642177760601,
        "train_time_sec": 29.130589723587036,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997406195784582,
              "spearman": 0.9986489718045288,
              "auroc_top30_bad": 0.9998587619047619,
              "mae": 0.026307770564837848,
              "mse": 0.00129511164652556,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8235270888886573,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06039850067102816
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17464978268495762
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4167577383237658
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7711725721966941
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2337197005012421
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9998092676839707,
              "spearman": 0.9997339656293522,
              "auroc_top30_worst": 0.9997422857142857,
              "pairwise_seed_ranking": 0.9487,
              "predicted_best_mean_error": 1.7444739224612713,
              "seed0_mean_error": 1.8170942743122578,
              "random_seed_mean_error": 1.809038346260786,
              "oracle_best_mean_error": 1.7438368230164052,
              "improvement_over_seed0": 0.07262035185098648,
              "gap_to_oracle": 0.0006370994448661182,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.545933144569397
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7823115854263306
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0672469070911408
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3227741087595621
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8077851967811585
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.51469328403473,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5332090349197387,
                  "rejected_mean_error": 4.278970653533936,
                  "gap_rejected_minus_accepted": 2.745761618614197
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.139323353767395,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3227741087595621,
                  "rejected_mean_error": 3.2628184608459474,
                  "gap_rejected_minus_accepted": 1.9400443520863853
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.623028576374054,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0672469070911408,
                  "rejected_mean_error": 2.548323486471176,
                  "gap_rejected_minus_accepted": 1.4810765793800353
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1085664927959442,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7823115854263306,
                  "rejected_mean_error": 2.1496097338994344,
                  "gap_rejected_minus_accepted": 1.367298148473104
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.486217498779297,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5418473222851754,
                  "rejected_mean_error": 4.294316842555999,
                  "gap_rejected_minus_accepted": 2.7524695202708243
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.166303873062134,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3332537673711777,
                  "rejected_mean_error": 3.268615795135498,
                  "gap_rejected_minus_accepted": 1.9353620277643202
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.635055661201477,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0732298899292947,
                  "rejected_mean_error": 2.560958658695221,
                  "gap_rejected_minus_accepted": 1.4877287687659262
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1235383749008179,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7840584560632705,
                  "rejected_mean_error": 2.1614395470619203,
                  "gap_rejected_minus_accepted": 1.3773810909986497
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9701674125920063,
              "spearman": 0.9662589853880839,
              "auroc_top30_bad": 0.9936220952380953,
              "mae": 0.15886321226963773,
              "mse": 0.06409770535883934,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7014580160432626,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1559288356602192
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24560162172317504
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.44312418862581254
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8076603773832322
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1911071869909764
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9543083911443248,
              "spearman": 0.9773221558541799,
              "auroc_top30_worst": 0.9896045714285715,
              "pairwise_seed_ranking": 0.9228,
              "predicted_best_mean_error": 1.619281154036522,
              "seed0_mean_error": 1.716470638871193,
              "random_seed_mean_error": 1.6973294532299041,
              "oracle_best_mean_error": 1.617486641049385,
              "improvement_over_seed0": 0.09718948483467105,
              "gap_to_oracle": 0.0017945129871368426,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.474492663860321
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7737387464596674
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.108818316268921
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3692225966372216
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.694315631389618
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4007421731948853,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5349254713058471,
                  "rejected_mean_error": 3.1288270721435545,
                  "gap_rejected_minus_accepted": 1.5939016008377074
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9505161046981812,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3683051624064002,
                  "rejected_mean_error": 2.6702639043521574,
                  "gap_rejected_minus_accepted": 1.3019587419457572
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5488547086715698,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.108818316268921,
                  "rejected_mean_error": 2.2798129465103147,
                  "gap_rejected_minus_accepted": 1.1709946302413938
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0546631813049316,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.774373480496696,
                  "rejected_mean_error": 2.0016175451884273,
                  "gap_rejected_minus_accepted": 1.2272440646917313
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.407127022743225,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5502226899729834,
                  "rejected_mean_error": 3.212702178955078,
                  "gap_rejected_minus_accepted": 1.6624794889820946
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.973157823085785,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3826066231663852,
                  "rejected_mean_error": 2.707463828344194,
                  "gap_rejected_minus_accepted": 1.3248572051778087
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5613824725151062,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1289517090320587,
                  "rejected_mean_error": 2.3039895687103273,
                  "gap_rejected_minus_accepted": 1.1750378596782687
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0925418436527252,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7853044351888081,
                  "rejected_mean_error": 2.0301790390422636,
                  "gap_rejected_minus_accepted": 1.2448746038534555
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9676003064526852,
              "spearman": 0.9625746837932164,
              "auroc_top30_bad": 0.9772182857142857,
              "mae": 0.17396329262368382,
              "mse": 0.05591775715534061,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.7033504419234466,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1624094398021698
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2726661578655243
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6013876126527786
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9924895485083262
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3136809441208839
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9270173643465132,
              "spearman": 0.9321448724364931,
              "auroc_top30_worst": 0.9544655238095237,
              "pairwise_seed_ranking": 0.9132,
              "predicted_best_mean_error": 1.8035307686328887,
              "seed0_mean_error": 1.9024355149269103,
              "random_seed_mean_error": 1.868010503768921,
              "oracle_best_mean_error": 1.8000093309879304,
              "improvement_over_seed0": 0.09890474629402157,
              "gap_to_oracle": 0.0035214376449583806,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9214324231147766
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2234604715918884
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.485513027858734
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.662536387949356
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8708093903064729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2475117683410657,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.785345003604889,
                  "rejected_mean_error": 2.6399888706207277,
                  "gap_rejected_minus_accepted": 0.8546438670158387
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0308103561401367,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.66228084840286,
                  "rejected_mean_error": 2.4950625652703233,
                  "gap_rejected_minus_accepted": 0.8327817168674634
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7673312425613403,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.485513027858734,
                  "rejected_mean_error": 2.256105752754211,
                  "gap_rejected_minus_accepted": 0.7705927248954771
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.415216088294983,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2245197835059973,
                  "rejected_mean_error": 2.086699088202469,
                  "gap_rejected_minus_accepted": 0.8621793046964719
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3281556367874146,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.810451619360182,
                  "rejected_mean_error": 2.7302905750274657,
                  "gap_rejected_minus_accepted": 0.9198389556672837
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.069142460823059,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6733459897219816,
                  "rejected_mean_error": 2.5824314072018577,
                  "gap_rejected_minus_accepted": 0.9090854174798761
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8056076169013977,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4919300060272216,
                  "rejected_mean_error": 2.3129410238265993,
                  "gap_rejected_minus_accepted": 0.8210110177993777
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4384803771972656,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2257901392285786,
                  "rejected_mean_error": 2.1303962564723378,
                  "gap_rejected_minus_accepted": 0.9046061172437592
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9801977970314852,
              "spearman": 0.9675482236453125,
              "auroc_top30_bad": 0.9651488095238094,
              "mae": 0.14218706982745788,
              "mse": 0.03455678415638056,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7264692142088933,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0989231613650918
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.184962908513844
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.665328264836222
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0572499966646234
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9324235841943721,
              "spearman": 0.9153362553362554,
              "auroc_top30_worst": 0.9641523809523809,
              "pairwise_seed_ranking": 0.8985,
              "predicted_best_mean_error": 1.866948483288288,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.05928158015012741,
              "gap_to_oracle": 0.0036470961570740368,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3065749573707581
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.45584144449234
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6555730490684508
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.763634140809377
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.346500110626221,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8472071793344287,
                  "rejected_mean_error": 2.522752356529236,
                  "gap_rejected_minus_accepted": 0.6755451771948073
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.058079719543457,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.763634140809377,
                  "rejected_mean_error": 2.368144365787506,
                  "gap_rejected_minus_accepted": 0.6045102249781291
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7544469833374023,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6555730490684508,
                  "rejected_mean_error": 2.173950345039368,
                  "gap_rejected_minus_accepted": 0.518377295970917
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5368621051311493,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.45584144449234,
                  "rejected_mean_error": 2.0677351145744325,
                  "gap_rejected_minus_accepted": 0.6118936700820925
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.375807499885559,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.860801104704539,
                  "rejected_mean_error": 2.5150906920433043,
                  "gap_rejected_minus_accepted": 0.6542895873387653
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.061947822570801,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.771656359831492,
                  "rejected_mean_error": 2.3899511742591857,
                  "gap_rejected_minus_accepted": 0.6182948144276936
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.757649004459381,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6581199169158936,
                  "rejected_mean_error": 2.1943402099609375,
                  "gap_rejected_minus_accepted": 0.5362202930450439
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5692777931690216,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4646503663063049,
                  "rejected_mean_error": 2.0800899624824525,
                  "gap_rejected_minus_accepted": 0.6154395961761476
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K10"
      }
    ],
    "target_chunk_min_l2_K20": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 49,
        "best_calib_loss": 0.05540791153907776,
        "train_time_sec": 11.050647497177124,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9890411645009933,
              "spearman": 0.9604496866009147,
              "auroc_top30_bad": 0.9993305238095238,
              "mae": 0.09414623101303586,
              "mse": 0.027245326431617683,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.518,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8476258019928834,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10092807737307158
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17200474317348563
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3206514181899605
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7041349095137635
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1828610509836464
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9985966663958329,
              "spearman": 0.9982867365073871,
              "auroc_top30_worst": 0.9990217142857143,
              "pairwise_seed_ranking": 0.8544,
              "predicted_best_mean_error": 1.7483019546866416,
              "seed0_mean_error": 1.8164365499317645,
              "random_seed_mean_error": 1.8085007551014423,
              "oracle_best_mean_error": 1.7432524019777775,
              "improvement_over_seed0": 0.06813459524512289,
              "gap_to_oracle": 0.005049552708864091,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5458176820278168
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7819290307044983
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0668918535709382
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3223809721946715
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8071557508707046
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.3411688327789313,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.532692597468694,
                  "rejected_mean_error": 4.2773241314888,
                  "gap_rejected_minus_accepted": 2.7446315340201064
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0734665393829346,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3223809721946715,
                  "rejected_mean_error": 3.261480086898804,
                  "gap_rejected_minus_accepted": 1.9390991147041323
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5946595668792725,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0668918535709382,
                  "rejected_mean_error": 2.547419648170471,
                  "gap_rejected_minus_accepted": 1.480527794599533
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.105311542749405,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7819290307044983,
                  "rejected_mean_error": 2.148897990926107,
                  "gap_rejected_minus_accepted": 1.3669689602216084
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.332941460609436,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5413131208221118,
                  "rejected_mean_error": 4.29254741191864,
                  "gap_rejected_minus_accepted": 2.7512342910965284
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.086335241794586,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3327993199427923,
                  "rejected_mean_error": 3.2673482398986815,
                  "gap_rejected_minus_accepted": 1.9345489199558892
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6041000485420227,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0729970963597297,
                  "rejected_mean_error": 2.5598760035037995,
                  "gap_rejected_minus_accepted": 1.4868789071440698
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1190820038318634,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7840744510889054,
                  "rejected_mean_error": 2.160557249546051,
                  "gap_rejected_minus_accepted": 1.376482798457146
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8721929722865146,
              "spearman": 0.8611456290829735,
              "auroc_top30_bad": 0.9724342857142857,
              "mae": 0.3185624201774597,
              "mse": 0.2119084420168787,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.492,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7307338474515161,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.41935642686486246
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3679038918018341
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.47212627269029617
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8241165158669154
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.187991971451044
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7271244489361659,
              "spearman": 0.8240252887201848,
              "auroc_top30_worst": 0.9094552380952381,
              "pairwise_seed_ranking": 0.806,
              "predicted_best_mean_error": 1.628958249092102,
              "seed0_mean_error": 1.7162024990320206,
              "random_seed_mean_error": 1.6969918372631072,
              "oracle_best_mean_error": 1.6172266017198562,
              "improvement_over_seed0": 0.08724424993991864,
              "gap_to_oracle": 0.011731647372245746,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6696623554229736
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9156327419556104
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1650592599868774
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4541112351010856
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6940473551750184
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.339390182495118,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6337796626620822,
                  "rejected_mean_error": 2.236456587791443,
                  "gap_rejected_minus_accepted": 0.6026769251293609
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.963361918926239,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.453470421575304,
                  "rejected_mean_error": 2.414240923171607,
                  "gap_rejected_minus_accepted": 0.9607705015963031
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5858469605445862,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1650592599868774,
                  "rejected_mean_error": 2.223035450363159,
                  "gap_rejected_minus_accepted": 1.0579761903762817
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0705441236495972,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9171703414033396,
                  "rejected_mean_error": 1.9535591004370625,
                  "gap_rejected_minus_accepted": 1.0363887590337229
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3491836786270137,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6605428739388783,
                  "rejected_mean_error": 2.2171391248703003,
                  "gap_rejected_minus_accepted": 0.556596250931422
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.992964655160904,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4513257418405563,
                  "rejected_mean_error": 2.502423984663827,
                  "gap_rejected_minus_accepted": 1.051098242823271
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6168009638786316,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1717993948459626,
                  "rejected_mean_error": 2.2606056032180786,
                  "gap_rejected_minus_accepted": 1.088806208372116
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1258407533168793,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9217209281429412,
                  "rejected_mean_error": 1.9838620656951864,
                  "gap_rejected_minus_accepted": 1.0621411375522452
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8249978527427071,
              "spearman": 0.8048651265695864,
              "auroc_top30_bad": 0.9054712380952381,
              "mae": 0.3974158736869693,
              "mse": 0.3060668487796922,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.484,
              "expert_lt_simvla_seed0": 0.988,
              "same_context_pred_std": 0.67844570628296,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47715127050876616
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.44025391578674317
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6813845529437065
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.055622497733434
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.31065023406744
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6012289561103624,
              "spearman": 0.6088060819630187,
              "auroc_top30_worst": 0.7004373333333332,
              "pairwise_seed_ranking": 0.7504,
              "predicted_best_mean_error": 1.8231343886852265,
              "seed0_mean_error": 1.9024355149269103,
              "random_seed_mean_error": 1.868010503768921,
              "oracle_best_mean_error": 1.8000093309879304,
              "improvement_over_seed0": 0.07930112624168384,
              "gap_to_oracle": 0.023125057697296114,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.1150334796905517
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4687561748119502
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6005267740249634
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7557334751208453
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8708093903064729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.004291033744812,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8107446468671162,
                  "rejected_mean_error": 2.411392081260681,
                  "gap_rejected_minus_accepted": 0.6006474343935648
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7679096460342407,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7550298469170944,
                  "rejected_mean_error": 2.2174082150855385,
                  "gap_rejected_minus_accepted": 0.46237836816844413
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.498267948627472,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.6005267740249634,
                  "rejected_mean_error": 2.141092006587982,
                  "gap_rejected_minus_accepted": 0.5405652325630188
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.179547667503357,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.468182526457424,
                  "rejected_mean_error": 2.0053048101407867,
                  "gap_rejected_minus_accepted": 0.5371222836833627
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0596057653427122,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8318111901813083,
                  "rejected_mean_error": 2.5380544376373293,
                  "gap_rejected_minus_accepted": 0.706243247456021
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7716959714889526,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.774215726928915,
                  "rejected_mean_error": 2.283024409460643,
                  "gap_rejected_minus_accepted": 0.508808682531728
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5445539355278015,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.610850296974182,
                  "rejected_mean_error": 2.194020732879639,
                  "gap_rejected_minus_accepted": 0.5831704359054568
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2399789690971375,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.4481140223760454,
                  "rejected_mean_error": 2.0554956969092872,
                  "gap_rejected_minus_accepted": 0.6073816745332419
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.7413064700729853,
              "spearman": 0.754570243014025,
              "auroc_top30_bad": 0.8590809523809524,
              "mae": 0.49318226959370076,
              "mse": 0.4471283726325033,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.515,
              "expert_lt_simvla_seed0": 0.99,
              "same_context_pred_std": 0.6228966570940626,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5840138626098633
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5476479731872678
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8100670862682163
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.085345036568741
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.41049968329039355,
              "spearman": 0.44126736926736926,
              "auroc_top30_worst": 0.7676809523809525,
              "pairwise_seed_ranking": 0.72,
              "predicted_best_mean_error": 1.886914648413658,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.03931541502475744,
              "gap_to_oracle": 0.02361326128244401,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.8626235508918763
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.828421152114868
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.7845531232357026
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.809863426844279
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.026233196258545,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8681163317627376,
                  "rejected_mean_error": 2.3345699846744536,
                  "gap_rejected_minus_accepted": 0.46645365291171603
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8930970430374146,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.809863426844279,
                  "rejected_mean_error": 2.2294565076828,
                  "gap_rejected_minus_accepted": 0.4195930808385211
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.349173367023468,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.7845531232357026,
                  "rejected_mean_error": 2.044970270872116,
                  "gap_rejected_minus_accepted": 0.26041714763641344
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8174815326929092,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.828421152114868,
                  "rejected_mean_error": 1.9435418787002563,
                  "gap_rejected_minus_accepted": 0.11512072658538819
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.023935651779175,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8800031218263837,
                  "rejected_mean_error": 2.342272537946701,
                  "gap_rejected_minus_accepted": 0.46226941612031713
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9147387444972992,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8176012492179872,
                  "rejected_mean_error": 2.252116506099701,
                  "gap_rejected_minus_accepted": 0.43451525688171366
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.399954080581665,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.7916375696659088,
                  "rejected_mean_error": 2.0608225572109222,
                  "gap_rejected_minus_accepted": 0.2691849875450134
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8559818118810654,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.855296289920807,
                  "rejected_mean_error": 1.9498746546109518,
                  "gap_rejected_minus_accepted": 0.0945783646901448
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K20"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 36,
        "best_calib_loss": 0.022084267809987068,
        "train_time_sec": 35.12159752845764,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9992182425172548,
              "spearman": 0.9936023160305095,
              "auroc_top30_bad": 0.9997397619047619,
              "mae": 0.030112335459759925,
              "mse": 0.0019354372932453739,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.959,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8616569208953917,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.019071292621083556
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.07519220280996523
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3185679224538384
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7037616093587596
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1828610509836464
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.999758179231808,
              "spearman": 0.9996465668898372,
              "auroc_top30_worst": 0.9998491428571429,
              "pairwise_seed_ranking": 0.9171,
              "predicted_best_mean_error": 1.7451292815506458,
              "seed0_mean_error": 1.8164365499317645,
              "random_seed_mean_error": 1.8085007551014423,
              "oracle_best_mean_error": 1.7432524019777775,
              "improvement_over_seed0": 0.07130726838111867,
              "gap_to_oracle": 0.0018768795728683063,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5447177466154098
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7805662443161011
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0661466825962067
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3220263588269552
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8071557508707046
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.442463684082032,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5325471229288312,
                  "rejected_mean_error": 4.278633402347564,
                  "gap_rejected_minus_accepted": 2.746086279418733
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.123573958873749,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3220263588269552,
                  "rejected_mean_error": 3.262543927001953,
                  "gap_rejected_minus_accepted": 1.9405175681749978
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6178458333015442,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0661466825962067,
                  "rejected_mean_error": 2.5481648191452027,
                  "gap_rejected_minus_accepted": 1.482018136548996
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1360054016113281,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7805662443161011,
                  "rejected_mean_error": 2.1493522530555724,
                  "gap_rejected_minus_accepted": 1.3687860087394714
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.398530554771424,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5411503988173272,
                  "rejected_mean_error": 4.2940119099617,
                  "gap_rejected_minus_accepted": 2.752861511144373
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1426392793655396,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3324986896912256,
                  "rejected_mean_error": 3.2682501306533815,
                  "gap_rejected_minus_accepted": 1.935751440962156
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6265972256660461,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0721283519864082,
                  "rejected_mean_error": 2.560744747877121,
                  "gap_rejected_minus_accepted": 1.4886163958907126
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.148750752210617,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7821576100587845,
                  "rejected_mean_error": 2.1611961965560913,
                  "gap_rejected_minus_accepted": 1.3790385864973067
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9552078169984562,
              "spearman": 0.9573756014292895,
              "auroc_top30_bad": 0.9930613333333334,
              "mae": 0.16287821580693126,
              "mse": 0.0777163489365337,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.94,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7403965080309581,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.20738426545262337
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.25019808628559115
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4340290534615517
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8056361213127772
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.187991971451044
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9174484881438238,
              "spearman": 0.9737600897024575,
              "auroc_top30_worst": 0.9908175238095238,
              "pairwise_seed_ranking": 0.9452,
              "predicted_best_mean_error": 1.6182724851369858,
              "seed0_mean_error": 1.7162024990320206,
              "random_seed_mean_error": 1.6969918372631072,
              "oracle_best_mean_error": 1.6172266017198562,
              "improvement_over_seed0": 0.09793001389503475,
              "gap_to_oracle": 0.0010458834171296338,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4689886951446533
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7591923106557283
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1097629402160645
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3753417834544233
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6940473551750184
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.436978054046631,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5590033112631905,
                  "rejected_mean_error": 2.90944375038147,
                  "gap_rejected_minus_accepted": 1.3504404391182794
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0570271611213684,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3737259285172632,
                  "rejected_mean_error": 2.6529648528693204,
                  "gap_rejected_minus_accepted": 1.2792389243520572
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.678793728351593,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1097629402160645,
                  "rejected_mean_error": 2.2783317701339723,
                  "gap_rejected_minus_accepted": 1.1685688299179078
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0740914940834045,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7599191903687132,
                  "rejected_mean_error": 2.006088033493453,
                  "gap_rejected_minus_accepted": 1.2461688431247397
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4559088230133055,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5720396843221454,
                  "rejected_mean_error": 3.0136678314208982,
                  "gap_rejected_minus_accepted": 1.4416281470987529
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0755192637443542,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3881428326196212,
                  "rejected_mean_error": 2.689966905684698,
                  "gap_rejected_minus_accepted": 1.3018240730650767
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6944915652275085,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1287821581363677,
                  "rejected_mean_error": 2.3036228399276735,
                  "gap_rejected_minus_accepted": 1.1748406817913057
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1136786043643951,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7689160416050563,
                  "rejected_mean_error": 2.0353417868282704,
                  "gap_rejected_minus_accepted": 1.2664257452232142
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9514891778653225,
              "spearman": 0.944116105398979,
              "auroc_top30_bad": 0.9736822857142858,
              "mae": 0.20058555387407542,
              "mse": 0.08380807826144226,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.928,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7342291337044652,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2734660267829895
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.29977831296920776
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5930961432218551
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.992587320693334
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.31065023406744
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9015642471961118,
              "spearman": 0.9222604019672493,
              "auroc_top30_worst": 0.9374384761904762,
              "pairwise_seed_ranking": 0.9168,
              "predicted_best_mean_error": 1.8030966240167619,
              "seed0_mean_error": 1.9024355149269103,
              "random_seed_mean_error": 1.868010503768921,
              "oracle_best_mean_error": 1.8000093309879304,
              "improvement_over_seed0": 0.09933889091014847,
              "gap_to_oracle": 0.0030872930288314837,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8918150334358216
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2218411039465513
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.491135774898529
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6704147077445537
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8708093903064729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1512898683547976,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7903321889771355,
                  "rejected_mean_error": 2.595104202270508,
                  "gap_rejected_minus_accepted": 0.8047720132933724
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0063130259513855,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6700076552439906,
                  "rejected_mean_error": 2.4719315173146064,
                  "gap_rejected_minus_accepted": 0.8019238620706157
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7804261445999146,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.491135774898529,
                  "rejected_mean_error": 2.2504830057144165,
                  "gap_rejected_minus_accepted": 0.7593472308158875
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4795657992362976,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2225288101278555,
                  "rejected_mean_error": 2.0873641625539725,
                  "gap_rejected_minus_accepted": 0.864835352426117
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.215023326873779,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8140471442540487,
                  "rejected_mean_error": 2.697930850982666,
                  "gap_rejected_minus_accepted": 0.8838837067286174
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0376830101013184,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6825615065620545,
                  "rejected_mean_error": 2.5550774127718,
                  "gap_rejected_minus_accepted": 0.8725159062097456
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.813286542892456,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5007187967300415,
                  "rejected_mean_error": 2.304152233123779,
                  "gap_rejected_minus_accepted": 0.8034334363937377
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5079652070999146,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.220667216512892,
                  "rejected_mean_error": 2.13212216091666,
                  "gap_rejected_minus_accepted": 0.9114549444037678
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9564805472049999,
              "spearman": 0.9416426907768203,
              "auroc_top30_bad": 0.9588119047619048,
              "mae": 0.17554541563801468,
              "mse": 0.06825135711286821,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.935,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7654428260241182,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2661711927317083
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2694436973109841
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6678201817311347
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.05992047842592
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.914749941334694,
              "spearman": 0.885896865896866,
              "auroc_top30_worst": 0.9449714285714286,
              "pairwise_seed_ranking": 0.8915,
              "predicted_best_mean_error": 1.8669946441054344,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.059235419332981154,
              "gap_to_oracle": 0.0036932569742202936,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.317602163553238
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.454762878894806
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6653943984508515
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7724759972890218
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.197382664680481,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8495148902469212,
                  "rejected_mean_error": 2.501982958316803,
                  "gap_rejected_minus_accepted": 0.652468068069882
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.011367619037628,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7724759972890218,
                  "rejected_mean_error": 2.341618796348572,
                  "gap_rejected_minus_accepted": 0.5691427990595501
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.848305881023407,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6653943984508515,
                  "rejected_mean_error": 2.1641289956569674,
                  "gap_rejected_minus_accepted": 0.4987345972061159
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6080841720104218,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.454762878894806,
                  "rejected_mean_error": 2.0680946364402772,
                  "gap_rejected_minus_accepted": 0.6133317575454713
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.207771158218384,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.861438586976793,
                  "rejected_mean_error": 2.5093533515930178,
                  "gap_rejected_minus_accepted": 0.6479147646162247
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.024277687072754,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7762390104929606,
                  "rejected_mean_error": 2.37620322227478,
                  "gap_rejected_minus_accepted": 0.5999642117818196
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8741238117218018,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6722636485099793,
                  "rejected_mean_error": 2.180196478366852,
                  "gap_rejected_minus_accepted": 0.5079328298568726
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6264621317386627,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4668251132965089,
                  "rejected_mean_error": 2.079365046819051,
                  "gap_rejected_minus_accepted": 0.6125399335225421
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K20"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 13,
        "best_calib_loss": 0.022315602749586105,
        "train_time_sec": 41.385218381881714,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.995564034361891,
              "spearman": 0.9727877296303713,
              "auroc_top30_bad": 0.9984379523809525,
              "mae": 0.07882178955354029,
              "mse": 0.012082822810737456,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.944,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.871459293853271,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07069499349535908
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.10442301294258796
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3196107177304802
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7048353242826182
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1828610509836464
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9985633892184342,
              "spearman": 0.9969745900228382,
              "auroc_top30_worst": 0.9975638095238096,
              "pairwise_seed_ranking": 0.9201,
              "predicted_best_mean_error": 1.7455604042708874,
              "seed0_mean_error": 1.8164365499317645,
              "random_seed_mean_error": 1.8085007551014423,
              "oracle_best_mean_error": 1.7432524019777775,
              "improvement_over_seed0": 0.07087614566087708,
              "gap_to_oracle": 0.002308002293109901,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5457672611474991
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7825473269462585
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0677406103610994
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3232242418924967
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8071557508707046
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5505281448364285,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5325772081216176,
                  "rejected_mean_error": 4.2783626356124875,
                  "gap_rejected_minus_accepted": 2.74578542749087
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1613094806671143,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3232242418924967,
                  "rejected_mean_error": 3.2589502778053285,
                  "gap_rejected_minus_accepted": 1.9357260359128319
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6661852598190308,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0677406103610994,
                  "rejected_mean_error": 2.54657089138031,
                  "gap_rejected_minus_accepted": 1.4788302810192107
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.146545648574829,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7825473269462585,
                  "rejected_mean_error": 2.1486918921788534,
                  "gap_rejected_minus_accepted": 1.3661445652325948
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.515212988853455,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5411503988173272,
                  "rejected_mean_error": 4.2940119099617,
                  "gap_rejected_minus_accepted": 2.752861511144373
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.195095181465149,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.332819571852684,
                  "rejected_mean_error": 3.2672874841690063,
                  "gap_rejected_minus_accepted": 1.9344679123163222
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6966353058815002,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0731657465100288,
                  "rejected_mean_error": 2.5597073533535,
                  "gap_rejected_minus_accepted": 1.4865416068434714
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1747546792030334,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7835959960222244,
                  "rejected_mean_error": 2.160716734568278,
                  "gap_rejected_minus_accepted": 1.3771207385460538
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9605830931465634,
              "spearman": 0.9556702015266512,
              "auroc_top30_bad": 0.9933142857142857,
              "mae": 0.1694905416415073,
              "mse": 0.06579046045692151,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.928,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.738205743268814,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.19934324356913566
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.25620522084236147
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4387278271317482
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8025096338987351
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.187991971451044
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9353465554351125,
              "spearman": 0.9727571916526028,
              "auroc_top30_worst": 0.992896,
              "pairwise_seed_ranking": 0.9096,
              "predicted_best_mean_error": 1.6206074874401093,
              "seed0_mean_error": 1.7162024990320206,
              "random_seed_mean_error": 1.6969918372631072,
              "oracle_best_mean_error": 1.6172266017198562,
              "improvement_over_seed0": 0.0955950115919113,
              "gap_to_oracle": 0.0033808857202530795,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4669587497711182
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7818774017385948
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1093864866256713
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3697640766212935
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6940473551750184
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.464481282234192,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5404554986953736,
                  "rejected_mean_error": 3.076374063491821,
                  "gap_rejected_minus_accepted": 1.5359185647964475
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.112798810005188,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3690356732432591,
                  "rejected_mean_error": 2.667005649009071,
                  "gap_rejected_minus_accepted": 1.2979699757658119
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6618797779083252,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1093864866256713,
                  "rejected_mean_error": 2.278708223724365,
                  "gap_rejected_minus_accepted": 1.169321737098694
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0893474221229553,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7825729170927225,
                  "rejected_mean_error": 1.998520673339115,
                  "gap_rejected_minus_accepted": 1.2159477562463925
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.513868904113769,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5532360062334272,
                  "rejected_mean_error": 3.18290093421936,
                  "gap_rejected_minus_accepted": 1.629664927985933
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1678292751312256,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3812388565769806,
                  "rejected_mean_error": 2.7104596599699957,
                  "gap_rejected_minus_accepted": 1.329220803393015
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7074381709098816,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1316711056232451,
                  "rejected_mean_error": 2.300733892440796,
                  "gap_rejected_minus_accepted": 1.169062786817551
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.11836439371109,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7973386905496083,
                  "rejected_mean_error": 2.0257662419966835,
                  "gap_rejected_minus_accepted": 1.2284275514470753
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9420270514561204,
              "spearman": 0.9279720818911825,
              "auroc_top30_bad": 0.969799619047619,
              "mae": 0.21162655738005415,
              "mse": 0.08257561192604619,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.956,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7200660043949788,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.26938818728923797
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.36173767654895783
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5961221394777299
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9937036470254262
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.31065023406744
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9195384465141282,
              "spearman": 0.9079893277238416,
              "auroc_top30_worst": 0.9246262857142857,
              "pairwise_seed_ranking": 0.8932,
              "predicted_best_mean_error": 1.8033764402866364,
              "seed0_mean_error": 1.9024355149269103,
              "random_seed_mean_error": 1.868010503768921,
              "oracle_best_mean_error": 1.8000093309879304,
              "improvement_over_seed0": 0.09905907464027397,
              "gap_to_oracle": 0.0033671092987059836,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8993677916526794
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2245628507091448
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.498744732952118
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6773632196093928
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8708093903064729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3360321998596194,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7832901620335049,
                  "rejected_mean_error": 2.6584824447631834,
                  "gap_rejected_minus_accepted": 0.8751922827296785
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.119698643684387,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6766275935264636,
                  "rejected_mean_error": 2.4521140023923147,
                  "gap_rejected_minus_accepted": 0.7754864088658511
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8123410940170288,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.498744732952118,
                  "rejected_mean_error": 2.2428740476608278,
                  "gap_rejected_minus_accepted": 0.7441293147087098
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.453680157661438,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.225714228975887,
                  "rejected_mean_error": 2.086300089875815,
                  "gap_rejected_minus_accepted": 0.8605858608999277
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3965782880783078,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8051217381159466,
                  "rejected_mean_error": 2.778259506225586,
                  "gap_rejected_minus_accepted": 0.9731377681096396
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.153941035270691,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.684602991144925,
                  "rejected_mean_error": 2.5490177680575656,
                  "gap_rejected_minus_accepted": 0.8644147769126407
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8615607023239136,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5046374416351318,
                  "rejected_mean_error": 2.300233588218689,
                  "gap_rejected_minus_accepted": 0.795596146583557
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5070021450519562,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.23239433008527,
                  "rejected_mean_error": 2.128171315167677,
                  "gap_rejected_minus_accepted": 0.8957769850824069
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9553059579876749,
              "spearman": 0.9432381008162516,
              "auroc_top30_bad": 0.9645119047619047,
              "mae": 0.1744703301843256,
              "mse": 0.06232937989742186,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.92,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7546119334786354,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2236230337806046
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2957267561629415
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6689945304431021
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0577643216475845
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9193386882181069,
              "spearman": 0.9010630690630692,
              "auroc_top30_worst": 0.9476190476190477,
              "pairwise_seed_ranking": 0.862,
              "predicted_best_mean_error": 1.8689325508475303,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.057297512590885225,
              "gap_to_oracle": 0.005631163716316223,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3564115297794341
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4618642578125
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6574850099086762
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.767449117342631
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.399569368362427,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8518566595183479,
                  "rejected_mean_error": 2.4809070348739626,
                  "gap_rejected_minus_accepted": 0.6290503753556147
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0337987542152405,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.767449117342631,
                  "rejected_mean_error": 2.356699436187744,
                  "gap_rejected_minus_accepted": 0.589250318845113
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.838696002960205,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6574850099086762,
                  "rejected_mean_error": 2.1720383841991424,
                  "gap_rejected_minus_accepted": 0.5145533742904662
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6114181578159332,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4618642578125,
                  "rejected_mean_error": 2.065727510134379,
                  "gap_rejected_minus_accepted": 0.603863252321879
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.417345952987671,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8637093252605863,
                  "rejected_mean_error": 2.4889167070388796,
                  "gap_rejected_minus_accepted": 0.6252073817782933
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0433002710342407,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7753456362088522,
                  "rejected_mean_error": 2.3788833451271056,
                  "gap_rejected_minus_accepted": 0.6035377089182534
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8467667698860168,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6628879606723785,
                  "rejected_mean_error": 2.1895721662044525,
                  "gap_rejected_minus_accepted": 0.526684205532074
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6441056430339813,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4726616048812866,
                  "rejected_mean_error": 2.0774195496241252,
                  "gap_rejected_minus_accepted": 0.6047579447428386
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K20"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 40,
        "best_calib_loss": 0.02351175807416439,
        "train_time_sec": 29.365100622177124,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9992844734802946,
              "spearman": 0.9929399141521099,
              "auroc_top30_bad": 0.999652,
              "mae": 0.03793764900346577,
              "mse": 0.0027097495102207155,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.975,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8689817064318142,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.022529688737704417
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.07367203438929282
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.31856468004460914
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7038132552257894
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1828610509836464
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.999611273444144,
              "spearman": 0.9993979217198878,
              "auroc_top30_worst": 0.9995811428571428,
              "pairwise_seed_ranking": 0.9352,
              "predicted_best_mean_error": 1.7446692254543303,
              "seed0_mean_error": 1.8164365499317645,
              "random_seed_mean_error": 1.8085007551014423,
              "oracle_best_mean_error": 1.7432524019777775,
              "improvement_over_seed0": 0.07176732447743417,
              "gap_to_oracle": 0.0014168234765528087,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.544691373348236
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.780926030921936
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0663814554691315
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3222557810147604
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8071557508707046
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5435001373291017,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.53257762477133,
                  "rejected_mean_error": 4.278358885765075,
                  "gap_rejected_minus_accepted": 2.7457812609937453
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.145283877849579,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3222557810147604,
                  "rejected_mean_error": 3.261855660438538,
                  "gap_rejected_minus_accepted": 1.9395998794237774
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6248164772987366,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0663814554691315,
                  "rejected_mean_error": 2.547930046272278,
                  "gap_rejected_minus_accepted": 1.4815485908031465
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1134097874164581,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.780926030921936,
                  "rejected_mean_error": 2.149232324186961,
                  "gap_rejected_minus_accepted": 1.3683062932650247
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5203156948089602,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5412011901868714,
                  "rejected_mean_error": 4.293554787635803,
                  "gap_rejected_minus_accepted": 2.7523535974489315
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.169835090637207,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.332622423529625,
                  "rejected_mean_error": 3.267878929138184,
                  "gap_rejected_minus_accepted": 1.9352565056085589
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6399022936820984,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0723555017113686,
                  "rejected_mean_error": 2.5605175981521606,
                  "gap_rejected_minus_accepted": 1.488162096440792
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1284092366695404,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.782739471077919,
                  "rejected_mean_error": 2.1610022428830464,
                  "gap_rejected_minus_accepted": 1.3782627718051275
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9642972816230466,
              "spearman": 0.9457417334699287,
              "auroc_top30_bad": 0.9935794285714286,
              "mae": 0.169572425084305,
              "mse": 0.07023308175965254,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.96,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7196556476732372,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.28201527741551397
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2743168209314346
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4335935962319374
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8029060731331508
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.187991971451044
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9527516122822187,
              "spearman": 0.9768297508030406,
              "auroc_top30_worst": 0.9900129523809524,
              "pairwise_seed_ranking": 0.932,
              "predicted_best_mean_error": 1.6183304362297057,
              "seed0_mean_error": 1.7162024990320206,
              "random_seed_mean_error": 1.6969918372631072,
              "oracle_best_mean_error": 1.6172266017198562,
              "improvement_over_seed0": 0.09787206280231486,
              "gap_to_oracle": 0.0011038345098495217,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4693182640075684
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7633672203773108
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.110618937110901
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3689797469801994
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6940473551750184
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.453594899177552,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5366299765904745,
                  "rejected_mean_error": 3.1108037624359133,
                  "gap_rejected_minus_accepted": 1.5741737858454388
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9704838991165161,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3682263443284253,
                  "rejected_mean_error": 2.6694284643228063,
                  "gap_rejected_minus_accepted": 1.301202119994381
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5909446477890015,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.110618937110901,
                  "rejected_mean_error": 2.2774757732391357,
                  "gap_rejected_minus_accepted": 1.1668568361282348
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0171669125556946,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7640111017912722,
                  "rejected_mean_error": 2.0047211516628654,
                  "gap_rejected_minus_accepted": 1.240710049871593
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4816001892089843,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.552627634074953,
                  "rejected_mean_error": 3.18837628364563,
                  "gap_rejected_minus_accepted": 1.635748649570677
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.011523485183716,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3820504971685257,
                  "rejected_mean_error": 2.7080505045633467,
                  "gap_rejected_minus_accepted": 1.326000007394821
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6047115325927734,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.130996821641922,
                  "rejected_mean_error": 2.301408176422119,
                  "gap_rejected_minus_accepted": 1.170411354780197
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.02419713139534,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.779089516590512,
                  "rejected_mean_error": 2.0319143594267532,
                  "gap_rejected_minus_accepted": 1.2528248428362412
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9561247720838078,
              "spearman": 0.9454710059949125,
              "auroc_top30_bad": 0.9779984761904762,
              "mae": 0.20641939527464565,
              "mse": 0.08036024659187294,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.96,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7310491555992757,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2600054228901863
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3302510843753815
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5943170843839646
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9885241459369659
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.31065023406744
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9366922841852852,
              "spearman": 0.938491788252268,
              "auroc_top30_worst": 0.9540937142857142,
              "pairwise_seed_ranking": 0.9084,
              "predicted_best_mean_error": 1.8015567128658294,
              "seed0_mean_error": 1.9024355149269103,
              "random_seed_mean_error": 1.868010503768921,
              "oracle_best_mean_error": 1.8000093309879304,
              "improvement_over_seed0": 0.10087880206108091,
              "gap_to_oracle": 0.0015473818778990456,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9110621013641358
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2226097635351694
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4845371850013733
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6648217927037017
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8708093903064729
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.288760185241699,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7806555983755323,
                  "rejected_mean_error": 2.6821935176849365,
                  "gap_rejected_minus_accepted": 0.9015379193094042
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.001078188419342,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6639190261493753,
                  "rejected_mean_error": 2.490158499620212,
                  "gap_rejected_minus_accepted": 0.8262394734708367
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7369311451911926,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4845371850013733,
                  "rejected_mean_error": 2.2570815956115724,
                  "gap_rejected_minus_accepted": 0.7725444106101991
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4267445802688599,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2236243815848622,
                  "rejected_mean_error": 2.0869981925795402,
                  "gap_rejected_minus_accepted": 0.863373810994678
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3377537727355957,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.807150665389167,
                  "rejected_mean_error": 2.7599991607666015,
                  "gap_rejected_minus_accepted": 0.9528484953774345
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0301137566566467,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6761342306188083,
                  "rejected_mean_error": 2.5741552000954036,
                  "gap_rejected_minus_accepted": 0.8980209694765953
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7620814442634583,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4927895288467408,
                  "rejected_mean_error": 2.31208150100708,
                  "gap_rejected_minus_accepted": 0.8192919721603391
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4510530531406403,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.22564330933586,
                  "rejected_mean_error": 2.1304457232276386,
                  "gap_rejected_minus_accepted": 0.9048024138917785
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9678005911329561,
              "spearman": 0.9558083620514588,
              "auroc_top30_bad": 0.9605047619047619,
              "mae": 0.16946325610873464,
              "mse": 0.05776073540078171,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.965,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7403898817316226,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.17003610307350756
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2298650379255414
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6627839287556708
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0578477547988296
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9276279550038679,
              "spearman": 0.9055981015981017,
              "auroc_top30_worst": 0.9702571428571429,
              "pairwise_seed_ranking": 0.8975,
              "predicted_best_mean_error": 1.8653613111376763,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.06086875230073918,
              "gap_to_oracle": 0.002059924006462266,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2727196729183197
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.451435257434845
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.66117556142807
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7630891234079997
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.259643483161926,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8530106157726711,
                  "rejected_mean_error": 2.4705214285850525,
                  "gap_rejected_minus_accepted": 0.6175108128123814
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0117082595825195,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7630891234079997,
                  "rejected_mean_error": 2.369779417991638,
                  "gap_rejected_minus_accepted": 0.6066902945836383
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7725387215614319,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.66117556142807,
                  "rejected_mean_error": 2.1683478326797485,
                  "gap_rejected_minus_accepted": 0.5071722712516784
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5617385804653168,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.451435257434845,
                  "rejected_mean_error": 2.0692038435935975,
                  "gap_rejected_minus_accepted": 0.6177685861587525
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2693810939788817,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.866905442873637,
                  "rejected_mean_error": 2.4601516485214234,
                  "gap_rejected_minus_accepted": 0.5932462056477865
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9999743402004242,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7699391134579976,
                  "rejected_mean_error": 2.3951029133796693,
                  "gap_rejected_minus_accepted": 0.6251637999216717
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7717793583869934,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.667242511510849,
                  "rejected_mean_error": 2.185217615365982,
                  "gap_rejected_minus_accepted": 0.517975103855133
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5824817717075348,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4618808341026306,
                  "rejected_mean_error": 2.081013139883677,
                  "gap_rejected_minus_accepted": 0.6191323057810465
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K20"
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
        "best_epoch": 59,
        "best_calib_loss": 0.08832160383462906,
        "train_time_sec": 10.715311527252197,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9835520262057384,
              "spearman": 0.9250795105261336,
              "auroc_top30_bad": 0.999365880952381,
              "mae": 0.131483867381914,
              "mse": 0.04007411204093873,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.494,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7217334694569172,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.1447045276015997
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.1542846764266491
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.05485024091601372
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.28723300037781396
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7373432215481996
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9987660203479662,
              "spearman": 0.9989381278534996,
              "auroc_top30_worst": 0.9995487619047618,
              "pairwise_seed_ranking": 0.84835,
              "predicted_best_mean_error": 1.2431324819326401,
              "seed0_mean_error": 1.3106810560822486,
              "random_seed_mean_error": 1.3029831425845624,
              "oracle_best_mean_error": 1.2376449169814587,
              "improvement_over_seed0": 0.06754857414960846,
              "gap_to_oracle": 0.005487564951181412,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04622432535886765
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2887890269041061
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5739010553479195
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8262915236552556
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.301517175513506
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.967055940628054,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.031938964717918,
                  "rejected_mean_error": 3.7277210726737975,
                  "gap_rejected_minus_accepted": 2.6957821079558792
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6434204578399658,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.8262915236552556,
                  "rejected_mean_error": 2.727194131088257,
                  "gap_rejected_minus_accepted": 1.9009026074330015
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1188520193099976,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5739010553479195,
                  "rejected_mean_error": 2.0291332956790926,
                  "gap_rejected_minus_accepted": 1.4552322403311733
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6251989603042603,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.2887890269041061,
                  "rejected_mean_error": 1.6390932250499726,
                  "gap_rejected_minus_accepted": 1.3503041981458663
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.941520881652834,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.0402271639638476,
                  "rejected_mean_error": 3.7447660851478575,
                  "gap_rejected_minus_accepted": 2.70453892118401
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.672635942697525,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.8365177468458811,
                  "rejected_mean_error": 2.7331709837913514,
                  "gap_rejected_minus_accepted": 1.8966532369454703
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1383136510849,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.579466542840004,
                  "rejected_mean_error": 2.0418955693244936,
                  "gap_rejected_minus_accepted": 1.4624290264844895
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6449155062437057,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.29168112349510195,
                  "rejected_mean_error": 1.6503477002779643,
                  "gap_rejected_minus_accepted": 1.3586665767828623
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8572543838260405,
              "spearman": 0.8617899265015526,
              "auroc_top30_bad": 0.9608319999999999,
              "mae": 0.45842545554313513,
              "mse": 0.34393496740829327,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.516,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6238164640563305,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2416715937256813
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2570260136127472
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3978167565941811
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7426717361370723
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0858352556169033
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.715649743463372,
              "spearman": 0.7906877083441334,
              "auroc_top30_worst": 0.9182323809523809,
              "pairwise_seed_ranking": 0.7938,
              "predicted_best_mean_error": 1.5270388702154158,
              "seed0_mean_error": 1.6078072472810745,
              "random_seed_mean_error": 1.5886361465454102,
              "oracle_best_mean_error": 1.5090124953985213,
              "improvement_over_seed0": 0.08076837706565865,
              "gap_to_oracle": 0.018026374816894508,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7310509557723999
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8898444592188566
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.111670884513855
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3507871584597426
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5857927939414977
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.123879218101502,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.512392875459459,
                  "rejected_mean_error": 2.246392060279846,
                  "gap_rejected_minus_accepted": 0.7339991848203871
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5077983736991882,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.350165357075735,
                  "rejected_mean_error": 2.291169497913446,
                  "gap_rejected_minus_accepted": 0.941004140837711
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0945632457733154,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.111670884513855,
                  "rejected_mean_error": 2.0599147033691407,
                  "gap_rejected_minus_accepted": 0.9482438188552857
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6782810539007187,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8908927650116503,
                  "rejected_mean_error": 1.8179205517377008,
                  "gap_rejected_minus_accepted": 0.9270277867260506
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1560484170913696,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.541817153427336,
                  "rejected_mean_error": 2.2017180919647217,
                  "gap_rejected_minus_accepted": 0.6599009385373857
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5408744513988495,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3775716352271523,
                  "rejected_mean_error": 2.2912050163935103,
                  "gap_rejected_minus_accepted": 0.913633381166358
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.135887086391449,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.114158011674881,
                  "rejected_mean_error": 2.101456482887268,
                  "gap_rejected_minus_accepted": 0.9872984712123871
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7109617441892624,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.881224523934107,
                  "rejected_mean_error": 1.8525918011359352,
                  "gap_rejected_minus_accepted": 0.9713672772018282
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.7407778091631096,
              "spearman": 0.7692829986215672,
              "auroc_top30_bad": 0.8730361904761905,
              "mae": 0.6080970254133649,
              "mse": 0.6138078859705739,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.5539702342201918,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.31185630518198015
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.29795259640216826
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.616764727818966
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9376075235128403
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.186990550583601
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.4885996368786376,
              "spearman": 0.49611889338213044,
              "auroc_top30_worst": 0.7432259047619048,
              "pairwise_seed_ranking": 0.7504,
              "predicted_best_mean_error": 1.7130994410514833,
              "seed0_mean_error": 1.7728077206611634,
              "random_seed_mean_error": 1.7385039970874787,
              "oracle_best_mean_error": 1.6705015254020692,
              "improvement_over_seed0": 0.05970827960968017,
              "gap_to_oracle": 0.042597915649414064,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3877087635993957
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4666557642511833
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5084876921653747
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6049928742049853
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7413277290344238
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5319385170936588,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6696862466600206,
                  "rejected_mean_error": 2.386101070404053,
                  "gap_rejected_minus_accepted": 0.7164148237440322
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3111575543880463,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6052668655058617,
                  "rejected_mean_error": 2.1486409211311095,
                  "gap_rejected_minus_accepted": 0.5433740556252478
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9956457018852234,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5084876921653747,
                  "rejected_mean_error": 1.9741677659034729,
                  "gap_rejected_minus_accepted": 0.46568007373809817
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6156161427497864,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.4657366822321956,
                  "rejected_mean_error": 1.8333874917335673,
                  "gap_rejected_minus_accepted": 0.36765080950137174
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5874436140060424,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6824313513437907,
                  "rejected_mean_error": 2.5861950445175172,
                  "gap_rejected_minus_accepted": 0.9037636931737265
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3393064439296722,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6003112914090487,
                  "rejected_mean_error": 2.284820931298392,
                  "gap_rejected_minus_accepted": 0.6845096398893433
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0393913984298706,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.486357295036316,
                  "rejected_mean_error": 2.0592581462860107,
                  "gap_rejected_minus_accepted": 0.5729008512496947
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7177179455757141,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.4375930655570257,
                  "rejected_mean_error": 1.8857410001882258,
                  "gap_rejected_minus_accepted": 0.44814793463120006
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.6822714969962533,
              "spearman": 0.7121978616480737,
              "auroc_top30_bad": 0.8316595238095239,
              "mae": 0.7633965396098443,
              "mse": 0.8846972392058321,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.535,
              "expert_lt_simvla_seed0": 0.945,
              "same_context_pred_std": 0.543326068778756,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4616558311879635
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.635173307903111
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8201456393487752
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0831673186048865
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.3431966545162052,
              "spearman": 0.41894761094761096,
              "auroc_top30_worst": 0.7677714285714285,
              "pairwise_seed_ranking": 0.634,
              "predicted_best_mean_error": 1.9061314260959625,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.020098637342452985,
              "gap_to_oracle": 0.04283003896474846,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.8809833228588104
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.874089862346649
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.7518838155269623
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8120978657404583
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.533551287651062,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8717886130015056,
                  "rejected_mean_error": 2.301519453525543,
                  "gap_rejected_minus_accepted": 0.42973084052403765
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4143235683441162,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8120978657404583,
                  "rejected_mean_error": 2.2227531909942626,
                  "gap_rejected_minus_accepted": 0.4106553252538043
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9850996732711792,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.7518838155269623,
                  "rejected_mean_error": 2.077639578580856,
                  "gap_rejected_minus_accepted": 0.32575576305389387
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.4854241982102394,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.874089862346649,
                  "rejected_mean_error": 1.9283189752896628,
                  "gap_rejected_minus_accepted": 0.05422911294301369
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5130178928375244,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8880901826752556,
                  "rejected_mean_error": 2.2694889903068542,
                  "gap_rejected_minus_accepted": 0.3813988076315986
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.430172622203827,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.823873720963796,
                  "rejected_mean_error": 2.2332990908622743,
                  "gap_rejected_minus_accepted": 0.4094253698984782
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0187946557998657,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.7632068657875062,
                  "rejected_mean_error": 2.089253261089325,
                  "gap_rejected_minus_accepted": 0.3260463953018189
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5450751036405563,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.8842278385162354,
                  "rejected_mean_error": 1.9402308050791424,
                  "gap_rejected_minus_accepted": 0.05600296656290693
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
        "best_epoch": 34,
        "best_calib_loss": 0.05908970907330513,
        "train_time_sec": 35.0761981010437,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9936176661225686,
              "spearman": 0.9766873239248243,
              "auroc_top30_bad": 0.9994893809523809,
              "mae": 0.13448845026134512,
              "mse": 0.03135891375233778,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.86,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.7217626121535134,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.26893608206510544
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.2869313793897629
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.05964248667359352
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.28708042428096137
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7373432215481996
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9985950598500002,
              "spearman": 0.99946507153859,
              "auroc_top30_worst": 0.9995201904761905,
              "pairwise_seed_ranking": 0.9061,
              "predicted_best_mean_error": 1.2397060804963111,
              "seed0_mean_error": 1.3106810560822486,
              "random_seed_mean_error": 1.3029831425845624,
              "oracle_best_mean_error": 1.2376449169814587,
              "improvement_over_seed0": 0.07097497558593746,
              "gap_to_oracle": 0.0020611635148524154,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.045480651438236236
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.28816043651103973
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5736224869847297
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8261734308004379
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.301517175513506
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.958939838409424,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0319556944966317,
                  "rejected_mean_error": 3.727570504665375,
                  "gap_rejected_minus_accepted": 2.695614810168743
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.66774383187294,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.8261734308004379,
                  "rejected_mean_error": 2.72754840965271,
                  "gap_rejected_minus_accepted": 1.9013749788522722
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1865911483764648,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5736224869847297,
                  "rejected_mean_error": 2.0294118640422822,
                  "gap_rejected_minus_accepted": 1.4557893770575525
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7002691626548767,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.28816043651103973,
                  "rejected_mean_error": 1.6393027551809947,
                  "gap_rejected_minus_accepted": 1.351142318669955
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9358839273452757,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.0404879864719179,
                  "rejected_mean_error": 3.742418682575226,
                  "gap_rejected_minus_accepted": 2.7019306961033083
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6824352741241455,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.8365926385720571,
                  "rejected_mean_error": 2.7329463086128234,
                  "gap_rejected_minus_accepted": 1.8963536700407664
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1996625065803528,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5790680381059646,
                  "rejected_mean_error": 2.0422940740585327,
                  "gap_rejected_minus_accepted": 1.4632260359525682
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7160975635051727,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.2910225021839142,
                  "rejected_mean_error": 1.650567240715027,
                  "gap_rejected_minus_accepted": 1.3595447385311128
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9589583433061988,
              "spearman": 0.9343157354577332,
              "auroc_top30_bad": 0.9820891428571429,
              "mae": 0.3401119256015169,
              "mse": 0.16397718468565187,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.728,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6532595465542615,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.22013699400424958
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1696697680950165
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.35016319831609727
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7197427277803421
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0858352556169033
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9410449892274222,
              "spearman": 0.9602041130266324,
              "auroc_top30_worst": 0.9778468571428571,
              "pairwise_seed_ranking": 0.9292,
              "predicted_best_mean_error": 1.5111880033016205,
              "seed0_mean_error": 1.6078072472810745,
              "random_seed_mean_error": 1.5886361465454102,
              "oracle_best_mean_error": 1.5090124953985213,
              "improvement_over_seed0": 0.09661924397945398,
              "gap_to_oracle": 0.002175507903099172,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.421366446018219
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7211890362012081
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0360771844863892
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2963291768834535
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5857927939414977
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1121954202651985,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4552782746420967,
                  "rejected_mean_error": 2.7604234676361084,
                  "gap_rejected_minus_accepted": 1.3051451929940117
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.636842042207718,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2959441999997248,
                  "rejected_mean_error": 2.4534865080738983,
                  "gap_rejected_minus_accepted": 1.1575423080741736
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2265941500663757,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0360771844863892,
                  "rejected_mean_error": 2.1355084033966065,
                  "gap_rejected_minus_accepted": 1.0994312189102173
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6974454671144485,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7223782135655705,
                  "rejected_mean_error": 1.8742119654011191,
                  "gap_rejected_minus_accepted": 1.1518337518355486
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1328720808029176,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4766744901074305,
                  "rejected_mean_error": 2.788002061843872,
                  "gap_rejected_minus_accepted": 1.3113275717364414
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6491715610027313,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3148660113148511,
                  "rejected_mean_error": 2.4773312334030395,
                  "gap_rejected_minus_accepted": 1.1624652220881884
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2563270330429077,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0572179729938507,
                  "rejected_mean_error": 2.1583965215682985,
                  "gap_rejected_minus_accepted": 1.1011785485744479
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7203117907047272,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7328941580795106,
                  "rejected_mean_error": 1.902564063429195,
                  "gap_rejected_minus_accepted": 1.1696699053496844
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9447468761368807,
              "spearman": 0.9343789056146107,
              "auroc_top30_bad": 0.9672152380952381,
              "mae": 0.3742902144753607,
              "mse": 0.19596990423398472,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.876,
              "expert_lt_simvla_seed0": 0.984,
              "same_context_pred_std": 0.6427235123225783,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10314460176229477
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.14831484994888305
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.47918052009344103
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.870647079428037
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.186990550583601
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9068555683780744,
              "spearman": 0.9084378246515683,
              "auroc_top30_worst": 0.9422598095238095,
              "pairwise_seed_ranking": 0.9024,
              "predicted_best_mean_error": 1.674257956147194,
              "seed0_mean_error": 1.7728077206611634,
              "random_seed_mean_error": 1.7385039970874787,
              "oracle_best_mean_error": 1.6705015254020692,
              "improvement_over_seed0": 0.09854976451396946,
              "gap_to_oracle": 0.0037564307451247725,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8203832688331604
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0990343720485003
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3470607118606568
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.53171884835656
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7413277290344238
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8612971901893618,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6498954652150473,
                  "rejected_mean_error": 2.5642181034088134,
                  "gap_rejected_minus_accepted": 0.9143226381937661
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5982348322868347,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5308979257321027,
                  "rejected_mean_error": 2.3712725395592638,
                  "gap_rejected_minus_accepted": 0.840374613827161
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3669419884681702,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3470607118606568,
                  "rejected_mean_error": 2.135594746208191,
                  "gap_rejected_minus_accepted": 0.7885340343475342
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0597364008426666,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0999573137813483,
                  "rejected_mean_error": 1.955574196456209,
                  "gap_rejected_minus_accepted": 0.8556168826748607
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9655144333839416,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6735471391677856,
                  "rejected_mean_error": 2.6661529541015625,
                  "gap_rejected_minus_accepted": 0.9926058149337769
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5988018810749054,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.541953046691609,
                  "rejected_mean_error": 2.4580430227612693,
                  "gap_rejected_minus_accepted": 0.9160899760696604
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3831040859222412,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3548070497512816,
                  "rejected_mean_error": 2.190808391571045,
                  "gap_rejected_minus_accepted": 0.8360013418197634
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.07737135887146,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0998956343484303,
                  "rejected_mean_error": 1.9995107230018168,
                  "gap_rejected_minus_accepted": 0.8996150886533865
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9624705000250782,
              "spearman": 0.9431950952977393,
              "auroc_top30_bad": 0.9447583333333334,
              "mae": 0.4212775509320054,
              "mse": 0.2305506181766745,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.91,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.674475670656779,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.18335081500932573
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18172680944949388
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6737818121947348
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0653307350501418
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.8725588017402623,
              "spearman": 0.8404542004542005,
              "auroc_top30_worst": 0.9333666666666667,
              "pairwise_seed_ranking": 0.884,
              "predicted_best_mean_error": 1.8663130250573159,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.05991703838109963,
              "gap_to_oracle": 0.003011637926101818,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3632656276226043
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.472481978416443
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6850650882720948
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7711928410530091
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.849808967113495,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.847521341641744,
                  "rejected_mean_error": 2.5199248957633973,
                  "gap_rejected_minus_accepted": 0.6724035541216533
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6818543374538422,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7711928410530091,
                  "rejected_mean_error": 2.3454682650566103,
                  "gap_rejected_minus_accepted": 0.5742754240036012
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4553455114364624,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6850650882720948,
                  "rejected_mean_error": 2.144458305835724,
                  "gap_rejected_minus_accepted": 0.4593932175636293
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2554085552692413,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.472481978416443,
                  "rejected_mean_error": 2.0621882699330647,
                  "gap_rejected_minus_accepted": 0.5897062915166218
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8467372179031372,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8603042006492614,
                  "rejected_mean_error": 2.519562828540802,
                  "gap_rejected_minus_accepted": 0.6592586278915404
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6993733644485474,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7738009635607401,
                  "rejected_mean_error": 2.3835173630714417,
                  "gap_rejected_minus_accepted": 0.6097163995107016
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4738145470619202,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6981339049339295,
                  "rejected_mean_error": 2.1543262219429016,
                  "gap_rejected_minus_accepted": 0.4561923170089721
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2718652784824371,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4787502765655518,
                  "rejected_mean_error": 2.075389992396037,
                  "gap_rejected_minus_accepted": 0.596639715830485
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_softmin_l2_K10"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 1,
        "best_calib_loss": 0.24403774738311768,
        "train_time_sec": 239.5696771144867,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.04450004767419051,
              "spearman": 0.23825102553022828,
              "auroc_top30_bad": 0.5698529999999999,
              "mae": 0.889101322445167,
              "mse": 1.5791098336792806,
              "expert_lt_perturb_large": 0.956,
              "expert_lt_other_task": 0.45,
              "expert_lt_simvla_seed0": 0.921,
              "same_context_pred_std": 0.009607561019904584,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2514607721418142
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3444186892449856
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.613349490404129
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.728244374281168
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7373432215481996
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": -0.04036041771118307,
              "spearman": -0.07287011667655356,
              "auroc_top30_worst": 0.421252,
              "pairwise_seed_ranking": 0.5753,
              "predicted_best_mean_error": 1.2823942424058914,
              "seed0_mean_error": 1.3106810560822486,
              "random_seed_mean_error": 1.3029831425845624,
              "oracle_best_mean_error": 1.2376449169814587,
              "improvement_over_seed0": 0.028286813676357214,
              "gap_to_oracle": 0.04474932542443266,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.1297801221609116
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.224499393081665
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4201162133455276
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3974177228212357
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.301517175513506
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 0.004141368390992296,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3246130153735478,
                  "rejected_mean_error": 1.0936546167731285,
                  "gap_rejected_minus_accepted": -0.23095839860041933
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.347189704072662e-05,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3974177228212357,
                  "rejected_mean_error": 1.0138155335903167,
                  "gap_rejected_minus_accepted": -0.38360218923091893
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0410752910038354e-07,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.4201162133455276,
                  "rejected_mean_error": 1.1829181376814841,
                  "gap_rejected_minus_accepted": -0.2371980756640435
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0301524744349422e-08,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 1.224499393081665,
                  "rejected_mean_error": 1.3271897696574528,
                  "gap_rejected_minus_accepted": 0.10269037657578783
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 0.004564527887851002,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3306947545541656,
                  "rejected_mean_error": 1.1305577698349953,
                  "gap_rejected_minus_accepted": -0.2001369847191703
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.594218742364319e-05,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.403558227300644,
                  "rejected_mean_error": 1.032049542427063,
                  "gap_rejected_minus_accepted": -0.3715086848735809
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.1783048254064852e-07,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4149240189194678,
                  "rejected_mean_error": 1.2064380932450294,
                  "gap_rejected_minus_accepted": -0.20848592567443847
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1396756427473065e-08,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.2067576348781586,
                  "rejected_mean_error": 1.345322196483612,
                  "gap_rejected_minus_accepted": 0.13856456160545338
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.01610974845476341,
              "spearman": 0.08083441106009497,
              "auroc_top30_bad": 0.4348944761904762,
              "mae": 1.0878902699727186,
              "mse": 1.8996537127879347,
              "expert_lt_perturb_large": 0.908,
              "expert_lt_other_task": 0.468,
              "expert_lt_simvla_seed0": 0.868,
              "same_context_pred_std": 0.007345430051376886,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.222785044580698
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.07355106934309
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0273767555475235
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0387694392442703
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0858352556169033
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": -0.11040531075167906,
              "spearman": -0.416267451563169,
              "auroc_top30_worst": 0.2431664761904762,
              "pairwise_seed_ranking": 0.6134,
              "predicted_best_mean_error": 1.5472057803869248,
              "seed0_mean_error": 1.6078072472810745,
              "random_seed_mean_error": 1.5886361465454102,
              "oracle_best_mean_error": 1.5090124953985213,
              "improvement_over_seed0": 0.06060146689414969,
              "gap_to_oracle": 0.038193284988403464,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 2.3294136419296265
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.9941980581826124
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.7660721654891969
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6968297119587978
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5857927939414977
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 0.0021925948094576645,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6241611835691665,
                  "rejected_mean_error": 1.2404772872924805,
                  "gap_rejected_minus_accepted": -0.383683896276686
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6437063297635177e-05,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.697757779279666,
                  "rejected_mean_error": 1.2506132691432112,
                  "gap_rejected_minus_accepted": -0.44714451013645484
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4433790340717678e-07,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.7660721654891969,
                  "rejected_mean_error": 1.4055134223937988,
                  "gap_rejected_minus_accepted": -0.36055874309539804
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.9327407169432718e-09,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.9931418746233749,
                  "rejected_mean_error": 1.4497199420168152,
                  "gap_rejected_minus_accepted": -0.5434219326065597
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 0.0022584684658795576,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6445461547374725,
                  "rejected_mean_error": 1.2771570801734924,
                  "gap_rejected_minus_accepted": -0.36738907456398007
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.266283101766021e-05,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7191675877507357,
                  "rejected_mean_error": 1.2772614747758895,
                  "gap_rejected_minus_accepted": -0.4419061129748463
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.641998821355628e-07,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.77911727309227,
                  "rejected_mean_error": 1.4364972214698792,
                  "gap_rejected_minus_accepted": -0.34262005162239073
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 3.00871277891801e-09,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 2.024165598646043,
                  "rejected_mean_error": 1.4675367866607911,
                  "gap_rejected_minus_accepted": -0.5566288119852518
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.10305990841201,
              "spearman": 0.15360884741169029,
              "auroc_top30_bad": 0.5129249523809525,
              "mae": 1.2035523935622365,
              "mse": 2.099514750826923,
              "expert_lt_perturb_large": 0.788,
              "expert_lt_other_task": 0.448,
              "expert_lt_simvla_seed0": 0.76,
              "same_context_pred_std": 0.002200085505597644,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9523694511651993
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9501297118425369
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.058460496532917
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1368463685115178
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.186990550583601
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.038645206062566384,
              "spearman": -0.16418550155490996,
              "auroc_top30_worst": 0.4116632380952381,
              "pairwise_seed_ranking": 0.5588,
              "predicted_best_mean_error": 1.74114344727993,
              "seed0_mean_error": 1.7728077206611634,
              "random_seed_mean_error": 1.7385039970874787,
              "oracle_best_mean_error": 1.6705015254020692,
              "improvement_over_seed0": 0.03166427338123334,
              "gap_to_oracle": 0.07064192187786089,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.7441735401153564
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.7987011900314918
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8060487849235534
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7519566442158176
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7413277290344238
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 0.0008801861142274002,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7429380078315735,
                  "rejected_mean_error": 1.726835219860077,
                  "gap_rejected_minus_accepted": -0.016102787971496557
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 7.1537247094966006e-06,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7517336080270236,
                  "rejected_mean_error": 1.710176583296194,
                  "gap_rejected_minus_accepted": -0.04155702473082967
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1529768784157568e-07,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.8060487849235534,
                  "rejected_mean_error": 1.6766066731452942,
                  "gap_rejected_minus_accepted": -0.12944211177825915
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 5.521927359808387e-09,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.8015387149664541,
                  "rejected_mean_error": 1.7212145608415472,
                  "gap_rejected_minus_accepted": -0.0803241541249069
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 0.0009420955728273836,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7720415899488662,
                  "rejected_mean_error": 1.7797028970718385,
                  "gap_rejected_minus_accepted": 0.007661307122972305
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 7.741080025880365e-06,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7803594275591845,
                  "rejected_mean_error": 1.750392336694021,
                  "gap_rejected_minus_accepted": -0.02996709086516347
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.23839164700712e-07,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.830530303478241,
                  "rejected_mean_error": 1.7150851378440857,
                  "gap_rejected_minus_accepted": -0.1154451656341553
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 5.704593464272989e-09,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.8251525504248483,
                  "rejected_mean_error": 1.7551728314894406,
                  "gap_rejected_minus_accepted": -0.06997971893540766
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.08118280610678572,
              "spearman": 0.17186171206038325,
              "auroc_top30_bad": 0.521997619047619,
              "mae": 1.3402951748192395,
              "mse": 2.4490841089190543,
              "expert_lt_perturb_large": 0.87,
              "expert_lt_other_task": 0.405,
              "expert_lt_simvla_seed0": 0.85,
              "same_context_pred_std": 0.0002823338844733103,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4703149412572384
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0165266260132193
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2085831229276955
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3272767651801307
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": -0.1660050963998343,
              "spearman": -0.3248937248937249,
              "auroc_top30_worst": 0.3545380952380952,
              "pairwise_seed_ranking": 0.524,
              "predicted_best_mean_error": 1.9202432212233544,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.005986842215061072,
              "gap_to_oracle": 0.056941834092140375,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 2.174169456958771
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 2.060534269332886
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 2.010817066669464
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.9527459020614624
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 0.0011007881374098364,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.9378044909901089,
                  "rejected_mean_error": 1.7073765516281127,
                  "gap_rejected_minus_accepted": -0.23042793936199613
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5729893050320243e-06,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.9527459020614624,
                  "rejected_mean_error": 1.80080908203125,
                  "gap_rejected_minus_accepted": -0.15193682003021247
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7805623997446673e-07,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 2.010817066669464,
                  "rejected_mean_error": 1.8187063274383546,
                  "gap_rejected_minus_accepted": -0.19211073923110944
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.398517739976569e-08,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 2.060534269332886,
                  "rejected_mean_error": 1.8661708396275838,
                  "gap_rejected_minus_accepted": -0.19436342970530207
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 0.0011862583458423614,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.9482609576649137,
                  "rejected_mean_error": 1.7279520153999328,
                  "gap_rejected_minus_accepted": -0.22030894226498088
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9269306221758598e-06,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.9675311549504597,
                  "rejected_mean_error": 1.8023267889022827,
                  "gap_rejected_minus_accepted": -0.165204366048177
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.1518077630844346e-07,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0254307770729065,
                  "rejected_mean_error": 1.8270293498039245,
                  "gap_rejected_minus_accepted": -0.19840142726898202
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.613863747669143e-08,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 2.0793778920173644,
                  "rejected_mean_error": 1.8751807872454325,
                  "gap_rejected_minus_accepted": -0.20419710477193198
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_softmin_l2_K10"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 15,
        "best_calib_loss": 0.07494980841875076,
        "train_time_sec": 29.171327352523804,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9830493457427405,
              "spearman": 0.9041857768835582,
              "auroc_top30_bad": 0.999177380952381,
              "mae": 0.12888193836845577,
              "mse": 0.040218946370077446,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.342,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7224591777782855,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.03853371061384678
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.10044779359102249
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.05518295357823372
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.2870683329463005
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7373432215481996
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9992636981194241,
              "spearman": 0.9994546474261728,
              "auroc_top30_worst": 0.9996287619047619,
              "pairwise_seed_ranking": 0.9041,
              "predicted_best_mean_error": 1.240356993585825,
              "seed0_mean_error": 1.3106810560822486,
              "random_seed_mean_error": 1.3029831425845624,
              "oracle_best_mean_error": 1.2376449169814587,
              "improvement_over_seed0": 0.07032406249642364,
              "gap_to_oracle": 0.0027120766043662314,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04546691370010376
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.28842176940441133
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5737405847668647
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8261879337390264
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.301517175513506
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.953296709060671,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0319689042634435,
                  "rejected_mean_error": 3.7274516167640686,
                  "gap_rejected_minus_accepted": 2.695482712500625
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6210114061832428,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.8261879337390264,
                  "rejected_mean_error": 2.7275049008369447,
                  "gap_rejected_minus_accepted": 1.9013169670979182
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1242781281471252,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5737405847668647,
                  "rejected_mean_error": 2.029293766260147,
                  "gap_rejected_minus_accepted": 1.4555531814932823
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6437108218669891,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.28842176940441133,
                  "rejected_mean_error": 1.6392156442165375,
                  "gap_rejected_minus_accepted": 1.3507938748121262
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9591745376586913,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.0403630461295446,
                  "rejected_mean_error": 3.7435431456565857,
                  "gap_rejected_minus_accepted": 2.7031800995270414
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6424600481987,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.836393471956253,
                  "rejected_mean_error": 2.7335438084602357,
                  "gap_rejected_minus_accepted": 1.8971503365039828
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1364392638206482,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5790403589010239,
                  "rejected_mean_error": 2.0423217532634736,
                  "gap_rejected_minus_accepted": 1.4632813943624496
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.652582511305809,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.29081429171562195,
                  "rejected_mean_error": 1.6506366442044575,
                  "gap_rejected_minus_accepted": 1.3598223524888355
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9530349364542022,
              "spearman": 0.8943357107356802,
              "auroc_top30_bad": 0.9837935238095238,
              "mae": 0.40710008140305115,
              "mse": 0.23752096982107088,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.444,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6125492439158604,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3750007032155991
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.26346965470314027
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.35292340048551557
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7193040369590123
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0858352556169033
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9423275899351375,
              "spearman": 0.9599599257343525,
              "auroc_top30_worst": 0.9847740952380952,
              "pairwise_seed_ranking": 0.904,
              "predicted_best_mean_error": 1.5109420275688172,
              "seed0_mean_error": 1.6078072472810745,
              "random_seed_mean_error": 1.5886361465454102,
              "oracle_best_mean_error": 1.5090124953985213,
              "improvement_over_seed0": 0.09686521971225726,
              "gap_to_oracle": 0.0019295321702959,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.451891175031662
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7477844323103244
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.036534593963623
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2855626687820532
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5857927939414977
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.917460072040558,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4491834014256795,
                  "rejected_mean_error": 2.815277326583862,
                  "gap_rejected_minus_accepted": 1.3660939251581827
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4706977903842926,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2848092115294336,
                  "rejected_mean_error": 2.4868203233986996,
                  "gap_rejected_minus_accepted": 1.202011111869266
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1107631921768188,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.036534593963623,
                  "rejected_mean_error": 2.1350509939193727,
                  "gap_rejected_minus_accepted": 1.0985163999557497
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7419949918985367,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7488603797583534,
                  "rejected_mean_error": 1.8653657348585995,
                  "gap_rejected_minus_accepted": 1.1165053551002462
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9202836155891416,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4697412015332116,
                  "rejected_mean_error": 2.850401659011841,
                  "gap_rejected_minus_accepted": 1.3806604574786292
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5074357092380524,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3026312438243213,
                  "rejected_mean_error": 2.513647130557469,
                  "gap_rejected_minus_accepted": 1.2110158867331478
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1261339783668518,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.055584187746048,
                  "rejected_mean_error": 2.160030306816101,
                  "gap_rejected_minus_accepted": 1.104446119070053
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7603563964366913,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7564234104421403,
                  "rejected_mean_error": 1.8946370960556886,
                  "gap_rejected_minus_accepted": 1.1382136856135483
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9280047537837839,
              "spearman": 0.9041051276293655,
              "auroc_top30_bad": 0.977856761904762,
              "mae": 0.4474039147505242,
              "mse": 0.2834063900301401,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.396,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6413270453691208,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.28118227100372317
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.33459406238794326
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.48291258569955825
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8616074849685034
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.186990550583601
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.93386058010733,
              "spearman": 0.9271955608453314,
              "auroc_top30_worst": 0.9570194285714286,
              "pairwise_seed_ranking": 0.8748,
              "predicted_best_mean_error": 1.6777542476654053,
              "seed0_mean_error": 1.7728077206611634,
              "random_seed_mean_error": 1.7385039970874787,
              "oracle_best_mean_error": 1.6705015254020692,
              "improvement_over_seed0": 0.09505347299575817,
              "gap_to_oracle": 0.007252722263336064,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8245338039398193
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1046866967509954
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3379939241409302
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.533232883730931
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7413277290344238
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.833474552631379,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6491019003126357,
                  "rejected_mean_error": 2.5713601875305176,
                  "gap_rejected_minus_accepted": 0.922258287217882
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5336560308933258,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.532964439376823,
                  "rejected_mean_error": 2.3650862031851334,
                  "gap_rejected_minus_accepted": 0.8321217638083105
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2591906189918518,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3379939241409302,
                  "rejected_mean_error": 2.1446615339279176,
                  "gap_rejected_minus_accepted": 0.8066676097869874
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9643966555595398,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1043313831186141,
                  "rejected_mean_error": 1.9541130612346889,
                  "gap_rejected_minus_accepted": 0.8497816781160747
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8884150743484496,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6714815611309475,
                  "rejected_mean_error": 2.6847431564331057,
                  "gap_rejected_minus_accepted": 1.0132615953021582
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5524860322475433,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5448488035304024,
                  "rejected_mean_error": 2.4494476810334223,
                  "gap_rejected_minus_accepted": 0.9045988775030198
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2782154083251953,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3403860521316528,
                  "rejected_mean_error": 2.205229389190674,
                  "gap_rejected_minus_accepted": 0.8648433370590212
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9744476824998856,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0996701301090301,
                  "rejected_mean_error": 1.9995866950182992,
                  "gap_rejected_minus_accepted": 0.8999165649092691
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.911779196923114,
              "spearman": 0.8792046643010955,
              "auroc_top30_bad": 0.9345779761904762,
              "mae": 0.5397089770199598,
              "mse": 0.4037278170993392,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.44,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6612844933616686,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.45103676214814187
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5032220139838756
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6777785967625678
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.067142352980872
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.8352390536508004,
              "spearman": 0.8028095952180241,
              "auroc_top30_worst": 0.917404761904762,
              "pairwise_seed_ranking": 0.879,
              "predicted_best_mean_error": 1.866841041147709,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.05938902229070653,
              "gap_to_oracle": 0.0035396540164949197,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4109869813919067
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.502645703792572
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6930413408279419
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7700815536181131
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7889625191688538,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8551840580834282,
                  "rejected_mean_error": 2.4509604477882387,
                  "gap_rejected_minus_accepted": 0.5957763897048105
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5028940439224243,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7700815536181131,
                  "rejected_mean_error": 2.3488021273612976,
                  "gap_rejected_minus_accepted": 0.5787205737431844
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3082678318023682,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6930413408279419,
                  "rejected_mean_error": 2.1364820532798765,
                  "gap_rejected_minus_accepted": 0.4434407124519346
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1451610326766968,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.502645703792572,
                  "rejected_mean_error": 2.0521336948076883,
                  "gap_rejected_minus_accepted": 0.5494879910151163
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8010542511940002,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8698464632034302,
                  "rejected_mean_error": 2.4336824655532836,
                  "gap_rejected_minus_accepted": 0.5638360023498534
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.494939923286438,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7786472932497661,
                  "rejected_mean_error": 2.368978374004364,
                  "gap_rejected_minus_accepted": 0.5903310807545981
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3152695894241333,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.7061069190502167,
                  "rejected_mean_error": 2.1463532078266145,
                  "gap_rejected_minus_accepted": 0.4402462887763978
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1653249561786652,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.516546607017517,
                  "rejected_mean_error": 2.062791215578715,
                  "gap_rejected_minus_accepted": 0.546244608561198
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_softmin_l2_K10"
      }
    ],
    "target_chunk_mean_top3_l2_K10": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 50,
        "best_calib_loss": 0.0579419806599617,
        "train_time_sec": 10.765190601348877,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9897100099227802,
              "spearman": 0.957633456887431,
              "auroc_top30_bad": 0.9991125238095239,
              "mae": 0.08564068014048971,
              "mse": 0.024029813851120362,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.509,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8443250554781502,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13616273522237315
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2068584394266829
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3444649384747259
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7228785657174265
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1980022756641264
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9990691221203747,
              "spearman": 0.9981551955021635,
              "auroc_top30_worst": 0.9991137142857143,
              "pairwise_seed_ranking": 0.8469,
              "predicted_best_mean_error": 1.7556183564066887,
              "seed0_mean_error": 1.8231409954726696,
              "random_seed_mean_error": 1.8152789250612258,
              "oracle_best_mean_error": 1.7502542590796948,
              "improvement_over_seed0": 0.06752263906598088,
              "gap_to_oracle": 0.005364097326993944,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.552931272149086
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7898446905136108
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0750420337200164
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3300569987932842
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8139421585321427
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.4552529335021975,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5399161692990198,
                  "rejected_mean_error": 4.280176061630249,
                  "gap_rejected_minus_accepted": 2.7402598923312294
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.105520188808441,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3300569987932842,
                  "rejected_mean_error": 3.2655976377487184,
                  "gap_rejected_minus_accepted": 1.9355406389554342
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.61097252368927,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0750420337200164,
                  "rejected_mean_error": 2.552842283344269,
                  "gap_rejected_minus_accepted": 1.4778002496242526
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1091972291469574,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7898446905136108,
                  "rejected_mean_error": 2.1553079812049867,
                  "gap_rejected_minus_accepted": 1.365463290691376
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.428695034980776,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5483552693989542,
                  "rejected_mean_error": 4.296212530136108,
                  "gap_rejected_minus_accepted": 2.747857260737154
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.118640422821045,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3402294826110204,
                  "rejected_mean_error": 3.2718755340576173,
                  "gap_rejected_minus_accepted": 1.931646051446597
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6258392930030823,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.080450554549694,
                  "rejected_mean_error": 2.565831436395645,
                  "gap_rejected_minus_accepted": 1.485380881845951
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.137879639863968,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7914418219327927,
                  "rejected_mean_error": 2.167040719985962,
                  "gap_rejected_minus_accepted": 1.3755988980531693
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.851433187609827,
              "spearman": 0.8519593809343217,
              "auroc_top30_bad": 0.9601188571428572,
              "mae": 0.32863741971552374,
              "mse": 0.2321133883699199,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7238260649270274,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.32697248059511186
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.37446477949619295
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4996072030186653
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.836777864686648
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1891180973947049
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6813702936804149,
              "spearman": 0.7636635036566425,
              "auroc_top30_worst": 0.8802468571428571,
              "pairwise_seed_ranking": 0.8032,
              "predicted_best_mean_error": 1.631424493074417,
              "seed0_mean_error": 1.7167358001470565,
              "random_seed_mean_error": 1.6975189623832703,
              "oracle_best_mean_error": 1.6177381602525711,
              "improvement_over_seed0": 0.08531130707263945,
              "gap_to_oracle": 0.013686332821845948,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6633860342502594
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9963793892126817
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2084817330360413
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4512312212097112
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6945780180931092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4252359867095956,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6373534203635323,
                  "rejected_mean_error": 2.209599397659302,
                  "gap_rejected_minus_accepted": 0.5722459772957695
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9795880317687988,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.450323615346418,
                  "rejected_mean_error": 2.4257804953252164,
                  "gap_rejected_minus_accepted": 0.9754568799787984
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6091105341911316,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2084817330360413,
                  "rejected_mean_error": 2.180674303150177,
                  "gap_rejected_minus_accepted": 0.9721925701141358
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.10869300365448,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9972634780140349,
                  "rejected_mean_error": 1.927512330840975,
                  "gap_rejected_minus_accepted": 0.93024885282694
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4314901351928713,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6649807250499726,
                  "rejected_mean_error": 2.182531476020813,
                  "gap_rejected_minus_accepted": 0.5175507509708404
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.029447317123413,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.480879500428623,
                  "rejected_mean_error": 2.416817197723994,
                  "gap_rejected_minus_accepted": 0.935937697295371
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6434149742126465,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2114643113613128,
                  "rejected_mean_error": 2.2220072889328004,
                  "gap_rejected_minus_accepted": 1.0105429775714876
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1108926236629486,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9712328622265468,
                  "rejected_mean_error": 1.9678945439384583,
                  "gap_rejected_minus_accepted": 0.9966616817119115
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8412191311382261,
              "spearman": 0.8249540678359938,
              "auroc_top30_bad": 0.9199245714285714,
              "mae": 0.36738233004808424,
              "mse": 0.2626871763730547,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.6805979839476836,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4758095152974129
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4439944832801819
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6549717778801918
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0459879475037257
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.311900108009577
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6289451899350391,
              "spearman": 0.6714336621088659,
              "auroc_top30_worst": 0.7782064761904762,
              "pairwise_seed_ranking": 0.7616,
              "predicted_best_mean_error": 1.8206160767078399,
              "seed0_mean_error": 1.9030981945991516,
              "random_seed_mean_error": 1.868715567588806,
              "oracle_best_mean_error": 1.8006762993335723,
              "improvement_over_seed0": 0.08248211789131177,
              "gap_to_oracle": 0.019939777374267553,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.196561505317688
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.409282691585712
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5749799974441527
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7459730404272262
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8714999006748199
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.033092212677002,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8120812684694927,
                  "rejected_mean_error": 2.406267590522766,
                  "gap_rejected_minus_accepted": 0.5941863220532733
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8180902302265167,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7455334723186595,
                  "rejected_mean_error": 2.2485942884375114,
                  "gap_rejected_minus_accepted": 0.5030608161188519
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5082107186317444,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5749799974441527,
                  "rejected_mean_error": 2.168019803905487,
                  "gap_rejected_minus_accepted": 0.5930398064613345
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2743504345417023,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.4089935888497593,
                  "rejected_mean_error": 2.0259977401638745,
                  "gap_rejected_minus_accepted": 0.6170041513141151
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0711016178131105,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8341820700963338,
                  "rejected_mean_error": 2.523343315124512,
                  "gap_rejected_minus_accepted": 0.6891612450281781
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8424718976020813,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7632939044167013,
                  "rejected_mean_error": 2.318072833712139,
                  "gap_rejected_minus_accepted": 0.5547789292954375
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5254732966423035,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5719643983840943,
                  "rejected_mean_error": 2.234231990814209,
                  "gap_rejected_minus_accepted": 0.6622675924301149
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3176665604114532,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.419899756946261,
                  "rejected_mean_error": 2.0658869730597513,
                  "gap_rejected_minus_accepted": 0.6459872161134903
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.7660594666980964,
              "spearman": 0.7649476800702971,
              "auroc_top30_bad": 0.8707547619047618,
              "mae": 0.43799273793213067,
              "mse": 0.3585458602490006,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.505,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6420264180398254,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6055797451734543
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5487653203085064
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7697863647527993
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0877307150786122
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.3935479503139962,
              "spearman": 0.489912933912934,
              "auroc_top30_worst": 0.7715190476190477,
              "pairwise_seed_ranking": 0.7445,
              "predicted_best_mean_error": 1.8800178146362305,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.046212248802184996,
              "gap_to_oracle": 0.01671642750501645,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.90001691699028
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.734655958175659
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.7575048429965974
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8255619209607443
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0122650384902956,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8754118981626298,
                  "rejected_mean_error": 2.268909887075424,
                  "gap_rejected_minus_accepted": 0.3934979889127943
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8533826768398285,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8255619209607443,
                  "rejected_mean_error": 2.1823610253334045,
                  "gap_rejected_minus_accepted": 0.35679910437266016
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.464387834072113,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.7575048429965974,
                  "rejected_mean_error": 2.0720185511112215,
                  "gap_rejected_minus_accepted": 0.3145137081146241
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.159207820892334,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.734655958175659,
                  "rejected_mean_error": 1.9747969433466595,
                  "gap_rejected_minus_accepted": 0.24014098517100035
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.005208897590637,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8952151834964752,
                  "rejected_mean_error": 2.205363982915878,
                  "gap_rejected_minus_accepted": 0.310148799419403
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8703992664813995,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.840271938641866,
                  "rejected_mean_error": 2.184104437828064,
                  "gap_rejected_minus_accepted": 0.34383249918619807
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5043995380401611,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.776438409090042,
                  "rejected_mean_error": 2.076021717786789,
                  "gap_rejected_minus_accepted": 0.299583308696747
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1694843173027039,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.7537233996391297,
                  "rejected_mean_error": 1.9837322847048442,
                  "gap_rejected_minus_accepted": 0.23000888506571449
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_mean_top3_l2_K10"
      },
      {
        "variant": "context_gated_action",
        "feature_mode": "M3_gated_base",
        "model_kind": "gated",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1456,
        "best_epoch": 75,
        "best_calib_loss": 0.02255837619304657,
        "train_time_sec": 35.09662103652954,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997471244006173,
              "spearman": 0.9981081219024062,
              "auroc_top30_bad": 0.999665380952381,
              "mae": 0.018066399734886364,
              "mse": 0.0006406149400545843,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8493768654776767,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.046183244646992534
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.10577925198283046
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3423839887271635
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7225368784672891
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1980022756641264
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9998281379262319,
              "spearman": 0.9996204115687983,
              "auroc_top30_worst": 0.9998097142857143,
              "pairwise_seed_ranking": 0.9416,
              "predicted_best_mean_error": 1.7512780942618846,
              "seed0_mean_error": 1.8231409954726696,
              "random_seed_mean_error": 1.8152789250612258,
              "oracle_best_mean_error": 1.7502542590796948,
              "improvement_over_seed0": 0.07186290121078498,
              "gap_to_oracle": 0.0010238351821898473,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5519996641874313
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7882934739112853
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0740605325698853
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3298984117190042
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8139421585321427
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.452693819999696,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5398419899675582,
                  "rejected_mean_error": 4.280843675613403,
                  "gap_rejected_minus_accepted": 2.7410016856458452
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.118899881839752,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3298984117190042,
                  "rejected_mean_error": 3.2660733989715576,
                  "gap_rejected_minus_accepted": 1.9361749872525533
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.614173710346222,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0740605325698853,
                  "rejected_mean_error": 2.5538237844944,
                  "gap_rejected_minus_accepted": 1.4797632519245147
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1174941062927246,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7882934739112853,
                  "rejected_mean_error": 2.1558250534057617,
                  "gap_rejected_minus_accepted": 1.3675315794944765
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.410331869125367,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5483351807792982,
                  "rejected_mean_error": 4.296393327713012,
                  "gap_rejected_minus_accepted": 2.7480581469337144
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1455048322677612,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3401531594196956,
                  "rejected_mean_error": 3.2721045036315917,
                  "gap_rejected_minus_accepted": 1.931951344211896
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6243999600410461,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.079902915894985,
                  "rejected_mean_error": 2.566379075050354,
                  "gap_rejected_minus_accepted": 1.4864761591553688
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1336072087287903,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7898614972829818,
                  "rejected_mean_error": 2.1675674948692323,
                  "gap_rejected_minus_accepted": 1.3777059975862505
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9571993776893521,
              "spearman": 0.9601450053830408,
              "auroc_top30_bad": 0.9942742857142858,
              "mae": 0.16726125558167695,
              "mse": 0.07375816377593315,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.932,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.742865122044206,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.17898805004358292
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24910070168972015
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.43571226071119307
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8053122910102208
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1891180973947049
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9183231414973887,
              "spearman": 0.9717837602456066,
              "auroc_top30_worst": 0.9890224761904761,
              "pairwise_seed_ranking": 0.9444,
              "predicted_best_mean_error": 1.6194092044830322,
              "seed0_mean_error": 1.7167358001470565,
              "random_seed_mean_error": 1.6975189623832703,
              "oracle_best_mean_error": 1.6177381602525711,
              "improvement_over_seed0": 0.09732659566402435,
              "gap_to_oracle": 0.0016710442304610496,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4704577956199646
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7630798835784961
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1101423267364503
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3757563571431743
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6945780180931092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.509553527832032,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5613600308100382,
                  "rejected_mean_error": 2.893539903640747,
                  "gap_rejected_minus_accepted": 1.332179872830709
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.081024944782257,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3748756262892212,
                  "rejected_mean_error": 2.651642366720084,
                  "gap_rejected_minus_accepted": 1.2767667404308627
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6340338587760925,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1101423267364503,
                  "rejected_mean_error": 2.279013709449768,
                  "gap_rejected_minus_accepted": 1.168871382713318
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.047447919845581,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7639269089927307,
                  "rejected_mean_error": 2.005457203950546,
                  "gap_rejected_minus_accepted": 1.2415302949578153
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.546170163154602,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5770772365729013,
                  "rejected_mean_error": 2.973662872314453,
                  "gap_rejected_minus_accepted": 1.3965856357415518
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1025596857070923,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3896417915821075,
                  "rejected_mean_error": 2.687633889062064,
                  "gap_rejected_minus_accepted": 1.2979920974799564
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6591569781303406,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.129580375432968,
                  "rejected_mean_error": 2.303891224861145,
                  "gap_rejected_minus_accepted": 1.1743108494281769
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.069671779870987,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.774026365034164,
                  "rejected_mean_error": 2.0343330964685125,
                  "gap_rejected_minus_accepted": 1.2603067314343486
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9553017940054527,
              "spearman": 0.9463140518149146,
              "auroc_top30_bad": 0.9726514285714285,
              "mae": 0.1870724188439548,
              "mse": 0.0696034351576902,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.944,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7377325291576537,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.26543057787418367
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.29629082651138305
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5965562295079231
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9929910621086756
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.311900108009577
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9103164807969386,
              "spearman": 0.9246721784904908,
              "auroc_top30_worst": 0.9480167619047619,
              "pairwise_seed_ranking": 0.9204,
              "predicted_best_mean_error": 1.8030919796228408,
              "seed0_mean_error": 1.9030981945991516,
              "random_seed_mean_error": 1.868715567588806,
              "oracle_best_mean_error": 1.8006762993335723,
              "improvement_over_seed0": 0.10000621497631079,
              "gap_to_oracle": 0.002415680289268529,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8988399682044983
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2266172562272122
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.491015986919403
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6679307658916342
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8714999006748199
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.346276116371155,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7897639048364427,
                  "rejected_mean_error": 2.607123863220215,
                  "gap_rejected_minus_accepted": 0.8173599583837723
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.024799644947052,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6668113190819893,
                  "rejected_mean_error": 2.4842577311939325,
                  "gap_rejected_minus_accepted": 0.8174464121119431
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7915682792663574,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.491015986919403,
                  "rejected_mean_error": 2.2519838144302367,
                  "gap_rejected_minus_accepted": 0.7609678275108336
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4904941320419312,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2276281185043505,
                  "rejected_mean_error": 2.0865819367680505,
                  "gap_rejected_minus_accepted": 0.8589538182637
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.432154154777527,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.813948466512892,
                  "rejected_mean_error": 2.7054457473754883,
                  "gap_rejected_minus_accepted": 0.8914972808625963
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0508739948272705,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6793144233724013,
                  "rejected_mean_error": 2.5673452615737915,
                  "gap_rejected_minus_accepted": 0.8880308382013902
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8248486518859863,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.500775053024292,
                  "rejected_mean_error": 2.3054213361740112,
                  "gap_rejected_minus_accepted": 0.8046462831497192
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.509929120540619,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.232147419263446,
                  "rejected_mean_error": 2.1291404344181326,
                  "gap_rejected_minus_accepted": 0.8969930151546865
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9615743273672863,
              "spearman": 0.9435761329561455,
              "auroc_top30_bad": 0.9511547619047619,
              "mae": 0.16980617086961866,
              "mse": 0.05536852860430639,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.945,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7531207205841131,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1697745460830629
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23670166159421205
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6671439360417426
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.064687906426688
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9144261528643096,
              "spearman": 0.8648812088812089,
              "auroc_top30_worst": 0.938904761904762,
              "pairwise_seed_ranking": 0.9075,
              "predicted_best_mean_error": 1.8656809529662133,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.06054911047220224,
              "gap_to_oracle": 0.002379565834999209,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.333054587841034
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4591715230941773
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6728229522705078
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.776929354508718
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2591995477676394,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8461027346716987,
                  "rejected_mean_error": 2.532692358493805,
                  "gap_rejected_minus_accepted": 0.6865896238221061
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0488675832748413,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.776929354508718,
                  "rejected_mean_error": 2.3282587246894835,
                  "gap_rejected_minus_accepted": 0.5513293701807656
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8584411144256592,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6728229522705078,
                  "rejected_mean_error": 2.1567004418373106,
                  "gap_rejected_minus_accepted": 0.48387748956680277
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.635591834783554,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4591715230941773,
                  "rejected_mean_error": 2.06662508837382,
                  "gap_rejected_minus_accepted": 0.6074535652796427
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2571042299270627,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8578950749503242,
                  "rejected_mean_error": 2.541244959831238,
                  "gap_rejected_minus_accepted": 0.6833498848809136
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0446327924728394,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7774632374445598,
                  "rejected_mean_error": 2.372530541419983,
                  "gap_rejected_minus_accepted": 0.5950673039754231
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.871242344379425,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6907758402824402,
                  "rejected_mean_error": 2.161684286594391,
                  "gap_rejected_minus_accepted": 0.47090844631195083
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6585695445537567,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4698044228553773,
                  "rejected_mean_error": 2.0783719436327615,
                  "gap_rejected_minus_accepted": 0.6085675207773842
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_mean_top3_l2_K10"
      },
      {
        "variant": "seed_relative_pairwise",
        "feature_mode": "M4_seed_relative",
        "model_kind": "mlp_big_pairwise",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 64,
        "best_calib_loss": 0.021353989839553833,
        "train_time_sec": 41.45205020904541,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9990164921771159,
              "spearman": 0.9957433349636657,
              "auroc_top30_bad": 0.9987769999999999,
              "mae": 0.04960986762274988,
              "mse": 0.00500397926637607,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.979,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8701018842540107,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0495445730923675
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.10762905394341797
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3424626505027525
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7233342855539794
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1980022756641264
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9989822005801049,
              "spearman": 0.9986679081946204,
              "auroc_top30_worst": 0.9989301904761905,
              "pairwise_seed_ranking": 0.9507,
              "predicted_best_mean_error": 1.7510015695989132,
              "seed0_mean_error": 1.8231409954726696,
              "random_seed_mean_error": 1.8152789250612258,
              "oracle_best_mean_error": 1.7502542590796948,
              "improvement_over_seed0": 0.07213942587375644,
              "gap_to_oracle": 0.0007473105192183915,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5522921721935272
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7886223422050476
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0746013000011445
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3303391311327617
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8139421585321427
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5989458560943604,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.539998696671592,
                  "rejected_mean_error": 4.2794333152771,
                  "gap_rejected_minus_accepted": 2.7394346186055074
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2073243856430054,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3303391311327617,
                  "rejected_mean_error": 3.2647512407302854,
                  "gap_rejected_minus_accepted": 1.9344121095975237
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6757137179374695,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0746013000011445,
                  "rejected_mean_error": 2.5532830170631406,
                  "gap_rejected_minus_accepted": 1.4786817170619961
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1516311168670654,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7886223422050476,
                  "rejected_mean_error": 2.155715430641174,
                  "gap_rejected_minus_accepted": 1.3670930884361265
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5872552394866943,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5486666143933931,
                  "rejected_mean_error": 4.293410425186157,
                  "gap_rejected_minus_accepted": 2.744743810792764
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.247419595718384,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3406151033639908,
                  "rejected_mean_error": 3.270718671798706,
                  "gap_rejected_minus_accepted": 1.9301035684347152
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.681372880935669,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0804271134734154,
                  "rejected_mean_error": 2.565854877471924,
                  "gap_rejected_minus_accepted": 1.4854277639985085
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1676308512687683,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7905906590223313,
                  "rejected_mean_error": 2.167324440956116,
                  "gap_rejected_minus_accepted": 1.3767337819337846
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9722838887104392,
              "spearman": 0.950315521424833,
              "auroc_top30_bad": 0.9942453333333334,
              "mae": 0.16317803368456663,
              "mse": 0.05607677899055598,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.952,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7458423393193996,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.21919903659820555
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.28287127704620363
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4331333795428276
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8039246875683467
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1891180973947049
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9649934868198524,
              "spearman": 0.982007855877028,
              "auroc_top30_worst": 0.9937462857142857,
              "pairwise_seed_ranking": 0.9292,
              "predicted_best_mean_error": 1.6189439117908477,
              "seed0_mean_error": 1.7167358001470565,
              "random_seed_mean_error": 1.6975189623832703,
              "oracle_best_mean_error": 1.6177381602525711,
              "improvement_over_seed0": 0.09779188835620878,
              "gap_to_oracle": 0.0012057515382766226,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4673908195495605
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7568329144746829
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1108718704223632
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3673737655316334
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6945780180931092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5989845752716065,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5317162228690253,
                  "rejected_mean_error": 3.1603341751098633,
                  "gap_rejected_minus_accepted": 1.628617952240838
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0729432106018066,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.366619595214168,
                  "rejected_mean_error": 2.6763577057530705,
                  "gap_rejected_minus_accepted": 1.3097381105389025
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.563880741596222,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1108718704223632,
                  "rejected_mean_error": 2.278284165763855,
                  "gap_rejected_minus_accepted": 1.1674122953414916
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0080236196517944,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7576438763651985,
                  "rejected_mean_error": 2.007556018478206,
                  "gap_rejected_minus_accepted": 1.2499121421130077
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6395736217498778,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5462706336710188,
                  "rejected_mean_error": 3.2509222984313966,
                  "gap_rejected_minus_accepted": 1.7046516647603778
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.145858585834503,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3801512761230774,
                  "rejected_mean_error": 2.715804149234106,
                  "gap_rejected_minus_accepted": 1.3356528731110284
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.589183509349823,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1303930575847625,
                  "rejected_mean_error": 2.3030785427093505,
                  "gap_rejected_minus_accepted": 1.172685485124588
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0586655139923096,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7738735803536007,
                  "rejected_mean_error": 2.034384569382285,
                  "gap_rejected_minus_accepted": 1.2605109890286843
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9609033966134958,
              "spearman": 0.9486533482287708,
              "auroc_top30_bad": 0.9773226666666667,
              "mae": 0.18368566183373333,
              "mse": 0.06182104749482801,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.944,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7608686752461467,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.23795062279701232
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.31222639186382295
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.596478449165821
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9900180020729701
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.311900108009577
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9398951373182722,
              "spearman": 0.9369075814119423,
              "auroc_top30_worst": 0.961654857142857,
              "pairwise_seed_ranking": 0.9156,
              "predicted_best_mean_error": 1.8028697855472564,
              "seed0_mean_error": 1.9030981945991516,
              "random_seed_mean_error": 1.868715567588806,
              "oracle_best_mean_error": 1.8006762993335723,
              "improvement_over_seed0": 0.10022840905189523,
              "gap_to_oracle": 0.0021934862136840927,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9136560659408569
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2202116463046808
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4914952776908874
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6579782899890119
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8714999006748199
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.536914038658143,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.785788305123647,
                  "rejected_mean_error": 2.642904260635376,
                  "gap_rejected_minus_accepted": 0.8571159555117291
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1470685601234436,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6569201206448494,
                  "rejected_mean_error": 2.5138681239594285,
                  "gap_rejected_minus_accepted": 0.8569480033145791
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8346075415611267,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4914952776908874,
                  "rejected_mean_error": 2.2515045236587525,
                  "gap_rejected_minus_accepted": 0.7600092459678651
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4255081117153168,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2207983132368458,
                  "rejected_mean_error": 2.0888633978659468,
                  "gap_rejected_minus_accepted": 0.8680650846291009
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.672048497200012,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.810471076435513,
                  "rejected_mean_error": 2.7367422580718994,
                  "gap_rejected_minus_accepted": 0.9262711816363864
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1998879313468933,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.668894049318079,
                  "rejected_mean_error": 2.5982755782112243,
                  "gap_rejected_minus_accepted": 0.9293815288931453
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.865996241569519,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4977007331848144,
                  "rejected_mean_error": 2.3084956560134886,
                  "gap_rejected_minus_accepted": 0.8107949228286742
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4674140214920044,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2202026844024658,
                  "rejected_mean_error": 2.1331645964301207,
                  "gap_rejected_minus_accepted": 0.9129619120276549
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9714553926937287,
              "spearman": 0.9663368936739577,
              "auroc_top30_bad": 0.9825845238095238,
              "mae": 0.13872259613825008,
              "mse": 0.0462810925166841,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.92,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7761186166316588,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1541342772729695
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2394310800805688
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6667528626956045
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0513597027485568
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9647926003887349,
              "spearman": 0.9524689124689125,
              "auroc_top30_worst": 0.9789095238095238,
              "pairwise_seed_ranking": 0.88,
              "predicted_best_mean_error": 1.8679081586003303,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.05832190483808519,
              "gap_to_oracle": 0.004606771469116255,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2859508407115936
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4582034487724305
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6433638944625855
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7600216617584228
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.369743394851685,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8428966283798218,
                  "rejected_mean_error": 2.561547315120697,
                  "gap_rejected_minus_accepted": 0.7186506867408753
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.081455647945404,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7600216617584228,
                  "rejected_mean_error": 2.378981802940369,
                  "gap_rejected_minus_accepted": 0.6189601411819461
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8578657507896423,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6433638944625855,
                  "rejected_mean_error": 2.186159499645233,
                  "gap_rejected_minus_accepted": 0.5427956051826477
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.603698492050171,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4582034487724305,
                  "rejected_mean_error": 2.0669477798144023,
                  "gap_rejected_minus_accepted": 0.6087443310419718
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.43969783782959,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.853449747297499,
                  "rejected_mean_error": 2.581252908706665,
                  "gap_rejected_minus_accepted": 0.7278031614091662
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0894609093666077,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7693370898564658,
                  "rejected_mean_error": 2.396908984184265,
                  "gap_rejected_minus_accepted": 0.6275718943277993
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8871190547943115,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6489567470550537,
                  "rejected_mean_error": 2.203503379821777,
                  "gap_rejected_minus_accepted": 0.5545466327667234
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6448173224925995,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.468473446369171,
                  "rejected_mean_error": 2.0788156024614968,
                  "gap_rejected_minus_accepted": 0.6103421560923257
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_mean_top3_l2_K10"
      },
      {
        "variant": "per_step_error_head",
        "feature_mode": "M4_seed_relative",
        "model_kind": "perstep",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 1526,
        "best_epoch": 22,
        "best_calib_loss": 0.024937788024544716,
        "train_time_sec": 29.29584264755249,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9990119666403532,
              "spearman": 0.9917554395353015,
              "auroc_top30_bad": 0.9994770000000001,
              "mae": 0.036339719662396235,
              "mse": 0.0026567485140508097,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.982,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8644618506769678,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06338480190734845
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.11039817567374557
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.34247499485118316
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7226859642274057
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1980022756641264
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9996116358452865,
              "spearman": 0.9993986398239023,
              "auroc_top30_worst": 0.9995958095238096,
              "pairwise_seed_ranking": 0.91,
              "predicted_best_mean_error": 1.7523886225819587,
              "seed0_mean_error": 1.8231409954726696,
              "random_seed_mean_error": 1.8152789250612258,
              "oracle_best_mean_error": 1.7502542590796948,
              "improvement_over_seed0": 0.0707523728907109,
              "gap_to_oracle": 0.002134363502263925,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5524592646360398
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7881730484008789
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0741141026496888
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3300261946678162
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8139421585321427
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.470115470886231,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5398809515370262,
                  "rejected_mean_error": 4.28049302148819,
                  "gap_rejected_minus_accepted": 2.7406120699511636
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.15408456325531,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3300261946678162,
                  "rejected_mean_error": 3.265690050125122,
                  "gap_rejected_minus_accepted": 1.9356638554573058
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.635998547077179,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0741141026496888,
                  "rejected_mean_error": 2.5537702144145964,
                  "gap_rejected_minus_accepted": 1.4796561117649076
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.137142926454544,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7881730484008789,
                  "rejected_mean_error": 2.155865195242564,
                  "gap_rejected_minus_accepted": 1.367692146841685
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.459122323989868,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.548384921517637,
                  "rejected_mean_error": 4.295945661067963,
                  "gap_rejected_minus_accepted": 2.747560739550326
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.182598352432251,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3403596210082371,
                  "rejected_mean_error": 3.2714851188659666,
                  "gap_rejected_minus_accepted": 1.9311254978577295
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6420337557792664,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0797872852683068,
                  "rejected_mean_error": 2.5664947056770324,
                  "gap_rejected_minus_accepted": 1.4867074204087256
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1572412252426147,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7900033429861069,
                  "rejected_mean_error": 2.1675202129681903,
                  "gap_rejected_minus_accepted": 1.3775168699820834
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9604492917882562,
              "spearman": 0.9529221797661797,
              "auroc_top30_bad": 0.9950937142857142,
              "mae": 0.18108692513713612,
              "mse": 0.07974285658262069,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.948,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7069976847518862,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.20645596522092818
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2679795688390732
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4389329089999199
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8034595860719681
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1891180973947049
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9377883707803183,
              "spearman": 0.9757444140071684,
              "auroc_top30_worst": 0.9931733333333334,
              "pairwise_seed_ranking": 0.9256,
              "predicted_best_mean_error": 1.6192883775234221,
              "seed0_mean_error": 1.7167358001470565,
              "random_seed_mean_error": 1.6975189623832703,
              "oracle_best_mean_error": 1.6177381602525711,
              "improvement_over_seed0": 0.09744742262363437,
              "gap_to_oracle": 0.0015502172708510287,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46828145456314085
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7799166769553454
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1104317811965942
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3699289329016386
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6945780180931092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3821746110916138,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5428249536090426,
                  "rejected_mean_error": 3.060355598449707,
                  "gap_rejected_minus_accepted": 1.5175306448406645
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9588826298713684,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3691671624891022,
                  "rejected_mean_error": 2.668731282313411,
                  "gap_rejected_minus_accepted": 1.2995641198243089
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5412707328796387,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1104317811965942,
                  "rejected_mean_error": 2.278724254989624,
                  "gap_rejected_minus_accepted": 1.1682924737930298
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0632413923740387,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7809096110133699,
                  "rejected_mean_error": 1.9997842202446123,
                  "gap_rejected_minus_accepted": 1.2188746092312424
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3783207893371583,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5569933672746024,
                  "rejected_mean_error": 3.1544176959991455,
                  "gap_rejected_minus_accepted": 1.597424328724543
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9790560007095337,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3824203886131552,
                  "rejected_mean_error": 2.709068847081018,
                  "gap_rejected_minus_accepted": 1.3266484584678628
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5701480507850647,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1289533107280731,
                  "rejected_mean_error": 2.30451828956604,
                  "gap_rejected_minus_accepted": 1.1755649788379667
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0773442685604095,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.79804603306074,
                  "rejected_mean_error": 2.026240908844586,
                  "gap_rejected_minus_accepted": 1.228194875783846
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9486491856385919,
              "spearman": 0.937250588611408,
              "auroc_top30_bad": 0.9709173333333334,
              "mae": 0.2158674085667357,
              "mse": 0.0909296435888264,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.964,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7432255838641957,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.23691465497016906
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3394581495285034
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5968533821225166
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9933743556420008
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.311900108009577
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8950056427458011,
              "spearman": 0.8996294979767097,
              "auroc_top30_worst": 0.924327619047619,
              "pairwise_seed_ranking": 0.9016,
              "predicted_best_mean_error": 1.8046339499950408,
              "seed0_mean_error": 1.9030981945991516,
              "random_seed_mean_error": 1.868715567588806,
              "oracle_best_mean_error": 1.8006762993335723,
              "improvement_over_seed0": 0.09846424460411085,
              "gap_to_oracle": 0.00395765066146847,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9167051010131836
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2226476709430034
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.492318117427826
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6927461237160129
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8714999006748199
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2293866395950324,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7921984384854635,
                  "rejected_mean_error": 2.5852130603790284,
                  "gap_rejected_minus_accepted": 0.793014621893565
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0413621068000793,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6925468461999518,
                  "rejected_mean_error": 2.40721559410278,
                  "gap_rejected_minus_accepted": 0.7146687479028284
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.777609646320343,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.492318117427826,
                  "rejected_mean_error": 2.250681683921814,
                  "gap_rejected_minus_accepted": 0.7583635664939881
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4278985261917114,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2238792373349492,
                  "rejected_mean_error": 2.0878342311181277,
                  "gap_rejected_minus_accepted": 0.8639549937831785
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.266004157066345,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8146809095806546,
                  "rejected_mean_error": 2.698853759765625,
                  "gap_rejected_minus_accepted": 0.8841728501849702
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0696874856948853,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7093175031284598,
                  "rejected_mean_error": 2.4782885010280307,
                  "gap_rejected_minus_accepted": 0.7689709978995709
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8012465834617615,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.495810030937195,
                  "rejected_mean_error": 2.3103863582611086,
                  "gap_rejected_minus_accepted": 0.8145763273239137
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.454563468694687,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2257654193847898,
                  "rejected_mean_error": 2.1312905199387493,
                  "gap_rejected_minus_accepted": 0.9055251005539595
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9647869906823914,
              "spearman": 0.9500740783090725,
              "auroc_top30_bad": 0.9613154761904763,
              "mae": 0.1753214163046796,
              "mse": 0.06254357665546274,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.92,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.758270318541189,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.17807742955163122
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.25435892609506844
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.667723216895014
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0594975286349655
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3405276080984623
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9247016846156306,
              "spearman": 0.8947248187248187,
              "auroc_top30_worst": 0.9535714285714285,
              "pairwise_seed_ranking": 0.897,
              "predicted_best_mean_error": 1.8675276950001716,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.058702368438243946,
              "gap_to_oracle": 0.004226307868957502,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3191215133666991
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4620903463363648
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6651362192630768
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7666695631345113
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2901377201080324,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8481621885299682,
                  "rejected_mean_error": 2.5141572737693787,
                  "gap_rejected_minus_accepted": 0.6659950852394105
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9779891967773438,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7666695631345113,
                  "rejected_mean_error": 2.3590380988121034,
                  "gap_rejected_minus_accepted": 0.5923685356775921
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7815406322479248,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6651362192630768,
                  "rejected_mean_error": 2.164387174844742,
                  "gap_rejected_minus_accepted": 0.4992509555816651
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5470024645328522,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4620903463363648,
                  "rejected_mean_error": 2.0656521472930907,
                  "gap_rejected_minus_accepted": 0.6035618009567258
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.305787944793701,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8596532808409796,
                  "rejected_mean_error": 2.525421106815338,
                  "gap_rejected_minus_accepted": 0.6657678259743585
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9789424240589142,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.775175568262736,
                  "rejected_mean_error": 2.3793935489654543,
                  "gap_rejected_minus_accepted": 0.6042179807027184
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7843408584594727,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6742999970912933,
                  "rejected_mean_error": 2.1781601297855375,
                  "gap_rejected_minus_accepted": 0.5038601326942442
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5623253881931305,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4726616048812866,
                  "rejected_mean_error": 2.0774195496241252,
                  "gap_rejected_minus_accepted": 0.6047579447428386
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_mean_top3_l2_K10"
      }
    ]
  }
}
```
