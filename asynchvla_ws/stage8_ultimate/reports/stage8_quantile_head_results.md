# Stage 8 Quantile Head Results

```json
{
  "splits": {
    "holdout_libero_object": [
      {
        "variant": "quantile_action_q80",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.8,
        "best_epoch": 92,
        "best_calib_pinball": 0.172541543841362,
        "train_time_sec": 17.10212469100952,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8539906965041492,
              "spearman": 0.7459390635805455,
              "auroc_top30_bad": 0.9545399285714288,
              "mae": 0.2957271222189069,
              "mse": 0.3753194871322794,
              "expert_lt_perturb_large": 0.663,
              "expert_lt_other_task": 0.483,
              "expert_lt_simvla_seed0": 0.516,
              "same_context_pred_std": 0.6712811845720328,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2660722094476223
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5168565005302429
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8355775196880102
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0764843795637289
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
              "pearson": 0.9978688993216087,
              "spearman": 0.9952168144484431,
              "auroc_top30_worst": 0.9984729523809523,
              "pairwise_seed_ranking": 0.8256,
              "predicted_best_mean_error": 1.7162921440601349,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.07813225355744358,
              "gap_to_oracle": 0.01469809633493413,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7299950267672539
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8822427725076676
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0859658982157707
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.306208909058571
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2533996343612674,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4902630558477508,
                  "rejected_mean_error": 4.438613282203674,
                  "gap_rejected_minus_accepted": 2.948350226355923
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.102427840232849,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.306208909058571,
                  "rejected_mean_error": 3.22176558675766,
                  "gap_rejected_minus_accepted": 1.9155566776990889
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5612030029296875,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0859658982157707,
                  "rejected_mean_error": 2.4842302587509155,
                  "gap_rejected_minus_accepted": 1.3982643605351448
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1253604590892792,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8822427725076676,
                  "rejected_mean_error": 2.0860498471419016,
                  "gap_rejected_minus_accepted": 1.203807074634234
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.312072801589966,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4919825195272765,
                  "rejected_mean_error": 4.516401300430298,
                  "gap_rejected_minus_accepted": 3.024418780903021
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1171995401382446,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3028034193118414,
                  "rejected_mean_error": 3.26928733253479,
                  "gap_rejected_minus_accepted": 1.9664839132229488
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5578500032424927,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0785275734066964,
                  "rejected_mean_error": 2.5103212218284607,
                  "gap_rejected_minus_accepted": 1.4317936484217644
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1175057590007782,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8703489905595779,
                  "rejected_mean_error": 2.1024495333035786,
                  "gap_rejected_minus_accepted": 1.2321005427440008
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8331386909532363,
              "spearman": 0.7551653913660376,
              "auroc_top30_bad": 0.8775078095238096,
              "mae": 0.5111735984027386,
              "mse": 0.4903356319792911,
              "expert_lt_perturb_large": 0.908,
              "expert_lt_other_task": 0.488,
              "expert_lt_simvla_seed0": 0.784,
              "same_context_pred_std": 0.7590723290585992,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.29984466075897215
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5041606148481369
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7992807664275169
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1082548581202825
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
              "pearson": 0.885442189782339,
              "spearman": 0.8530525369936237,
              "auroc_top30_worst": 0.8980358095238096,
              "pairwise_seed_ranking": 0.7532,
              "predicted_best_mean_error": 2.0207609869241714,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.08372001779079463,
              "gap_to_oracle": 0.03186575722694385,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7311690642833709
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0407055098658953
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3770595746517182
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.604050207335049
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.497200965881348,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8436898020373451,
                  "rejected_mean_error": 4.205775018692017,
                  "gap_rejected_minus_accepted": 2.3620852166546715
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.9346521496772766,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.603538299541972,
                  "rejected_mean_error": 3.505934562165135,
                  "gap_rejected_minus_accepted": 1.9023962626231632
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7998740673065186,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3770595746517182,
                  "rejected_mean_error": 2.7827370727539065,
                  "gap_rejected_minus_accepted": 1.4056774981021882
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2947682738304138,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0420967212881143,
                  "rejected_mean_error": 2.4265705772308808,
                  "gap_rejected_minus_accepted": 1.3844738559427665
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.495728015899658,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.867043316099379,
                  "rejected_mean_error": 4.241420202255249,
                  "gap_rejected_minus_accepted": 2.37437688615587
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.001388430595398,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6157545444162134,
                  "rejected_mean_error": 3.555145259887453,
                  "gap_rejected_minus_accepted": 1.9393907154712395
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.825939118862152,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4187488145828246,
                  "rejected_mean_error": 2.790213194847107,
                  "gap_rejected_minus_accepted": 1.3714643802642823
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2732879221439362,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0193103939767867,
                  "rejected_mean_error": 2.4700732425572403,
                  "gap_rejected_minus_accepted": 1.4507628485804536
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6386410773693114,
              "spearman": 0.5497493325086388,
              "auroc_top30_bad": 0.8011146666666666,
              "mae": 0.5092337059795856,
              "mse": 0.5486140814778947,
              "expert_lt_perturb_large": 0.732,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.576,
              "same_context_pred_std": 0.5325056906746555,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.37871631187200544
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7188096330165863
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9928350253105164
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1781803389469783
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
              "pearson": 0.8079117565697006,
              "spearman": 0.7036774797295872,
              "auroc_top30_worst": 0.8349714285714285,
              "pairwise_seed_ranking": 0.714,
              "predicted_best_mean_error": 1.606008213877678,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.05113492858409874,
              "gap_to_oracle": 0.026110692381858813,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8701548290252685
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9692804124683906
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1976383364200591
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3639784696132644
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.320787930488587,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4692179711129931,
                  "rejected_mean_error": 3.2468029680252077,
                  "gap_rejected_minus_accepted": 1.7775849969122146
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.022853672504425,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3635822315099018,
                  "rejected_mean_error": 2.4953483628769653,
                  "gap_rejected_minus_accepted": 1.1317661313670635
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.54886794090271,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1976383364200591,
                  "rejected_mean_error": 2.0963146051883697,
                  "gap_rejected_minus_accepted": 0.8986762687683105
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3082495331764221,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9699144122509149,
                  "rejected_mean_error": 1.8731455469271416,
                  "gap_rejected_minus_accepted": 0.9032311346762267
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3732552766799926,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4770895753966438,
                  "rejected_mean_error": 3.2776252460479736,
                  "gap_rejected_minus_accepted": 1.8005356706513298
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0822499990463257,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3535000630878509,
                  "rejected_mean_error": 2.5584329177462863,
                  "gap_rejected_minus_accepted": 1.2049328546584355
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5414658188819885,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1483505041599273,
                  "rejected_mean_error": 2.165935780763626,
                  "gap_rejected_minus_accepted": 1.0175852766036986
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.292509287595749,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9524151138843052,
                  "rejected_mean_error": 1.894564884709802,
                  "gap_rejected_minus_accepted": 0.9421497708254968
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5070217745766872,
              "spearman": 0.4684151430478507,
              "auroc_top30_bad": 0.7421782857142858,
              "mae": 0.46922460634112356,
              "mse": 0.4930255819065447,
              "expert_lt_perturb_large": 0.76,
              "expert_lt_other_task": 0.524,
              "expert_lt_simvla_seed0": 0.472,
              "same_context_pred_std": 0.45206296505191057,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.35597337675094604
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.881136976313591
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1379669895648956
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2963034211794535
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
              "pearson": 0.5253620397489154,
              "spearman": 0.46036270359213033,
              "auroc_top30_worst": 0.646272,
              "pairwise_seed_ranking": 0.7248,
              "predicted_best_mean_error": 1.6231567153930664,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.03859441256523133,
              "gap_to_oracle": 0.03113278341293335,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.1936880795955658
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3961255359343994
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.504868594455719
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5815928116091278
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.934299981594086,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6227619558175406,
                  "rejected_mean_error": 1.9932753658294677,
                  "gap_rejected_minus_accepted": 0.37051341001192717
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7857277989387512,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5813511170152665,
                  "rejected_mean_error": 1.8946984804476412,
                  "gap_rejected_minus_accepted": 0.3133473634323747
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5211086869239807,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.504868594455719,
                  "rejected_mean_error": 1.8147579991817475,
                  "gap_rejected_minus_accepted": 0.30988940472602855
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3167097866535187,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3968910142636528,
                  "rejected_mean_error": 1.7476411243958305,
                  "gap_rejected_minus_accepted": 0.3507501101321777
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9608489513397216,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6293342502911885,
                  "rejected_mean_error": 1.9535030269622802,
                  "gap_rejected_minus_accepted": 0.3241687766710917
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.798246055841446,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5826667142424353,
                  "rejected_mean_error": 1.8964937527974446,
                  "gap_rejected_minus_accepted": 0.31382703855500926
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5192177891731262,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.492027096271515,
                  "rejected_mean_error": 1.8314751596450807,
                  "gap_rejected_minus_accepted": 0.3394480633735657
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3246813714504242,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3782151530659388,
                  "rejected_mean_error": 1.7572739430289854,
                  "gap_rejected_minus_accepted": 0.37905878996304665
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_object/quantile_action_q80/model.pt"
      },
      {
        "variant": "quantile_action_q90",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.9,
        "best_epoch": 77,
        "best_calib_pinball": 0.1265673190355301,
        "train_time_sec": 16.23387336730957,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.7464229927800538,
              "spearman": 0.5433549804724597,
              "auroc_top30_bad": 0.902763,
              "mae": 0.4838043940499425,
              "mse": 0.7452813559991741,
              "expert_lt_perturb_large": 0.295,
              "expert_lt_other_task": 0.507,
              "expert_lt_simvla_seed0": 0.309,
              "same_context_pred_std": 0.6106561895682849,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4138631346523762
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7050023200511932
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0132130632191896
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1719767719904581
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
              "pearson": 0.9965985275608289,
              "spearman": 0.9913298458849857,
              "auroc_top30_worst": 0.9952790476190476,
              "pairwise_seed_ranking": 0.7672,
              "predicted_best_mean_error": 1.726161033630371,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.06826336398720745,
              "gap_to_oracle": 0.024566985905170258,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7402903001308441
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8843131441354751
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0872891270518303
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3080348680098852
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.319502139091494,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4903263956109682,
                  "rejected_mean_error": 4.4380432243347165,
                  "gap_rejected_minus_accepted": 2.947716828723748
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1658506989479065,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3080348680098852,
                  "rejected_mean_error": 3.216287709903717,
                  "gap_rejected_minus_accepted": 1.9082528418938318
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6555526852607727,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0872891270518303,
                  "rejected_mean_error": 2.482907029914856,
                  "gap_rejected_minus_accepted": 1.3956179028630256
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1710891425609589,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8843131441354751,
                  "rejected_mean_error": 2.0853597232659657,
                  "gap_rejected_minus_accepted": 1.2010465791304905
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.3968739986419676,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4918582316570812,
                  "rejected_mean_error": 4.517519891262054,
                  "gap_rejected_minus_accepted": 3.0256616596049732
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.173260986804962,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3051203872760138,
                  "rejected_mean_error": 3.262336428642273,
                  "gap_rejected_minus_accepted": 1.9572160413662594
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6422849893569946,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0801675077080726,
                  "rejected_mean_error": 2.5086812875270845,
                  "gap_rejected_minus_accepted": 1.428513779819012
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.164178878068924,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8720464714765549,
                  "rejected_mean_error": 2.101883706331253,
                  "gap_rejected_minus_accepted": 1.2298372348546982
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.754989210066709,
              "spearman": 0.5938643822887478,
              "auroc_top30_bad": 0.8566430476190476,
              "mae": 0.6710415892779827,
              "mse": 0.8490583945791639,
              "expert_lt_perturb_large": 0.5,
              "expert_lt_other_task": 0.532,
              "expert_lt_simvla_seed0": 0.584,
              "same_context_pred_std": 0.6581318616847904,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3731839712262154
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7336933176517486
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0196455046892166
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1601804426431657
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
              "pearson": 0.8892084420618038,
              "spearman": 0.850311340487258,
              "auroc_top30_worst": 0.9003001904761905,
              "pairwise_seed_ranking": 0.7072,
              "predicted_best_mean_error": 2.026771211743355,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.07770979297161107,
              "gap_to_oracle": 0.03787598204612741,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.811907644033432
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.07275759237699
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3787136455059052
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.601149248002943
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.559826326370239,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8445066077709198,
                  "rejected_mean_error": 4.198423767089844,
                  "gap_rejected_minus_accepted": 2.3539171593189243
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.9360581636428833,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.600593220939504,
                  "rejected_mean_error": 3.514750979578914,
                  "gap_rejected_minus_accepted": 1.9141577586394098
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9553165435791016,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3787136455059052,
                  "rejected_mean_error": 2.7810830018997192,
                  "gap_rejected_minus_accepted": 1.402369356393814
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4080411791801453,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.072792406470631,
                  "rejected_mean_error": 2.416316842479411,
                  "gap_rejected_minus_accepted": 1.34352443600878
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.6114866733551025,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8660761578877767,
                  "rejected_mean_error": 4.250124626159668,
                  "gap_rejected_minus_accepted": 2.384048468271891
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.9824323654174805,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6120985485015706,
                  "rejected_mean_error": 3.565997184269012,
                  "gap_rejected_minus_accepted": 1.9538986357674413
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9722469449043274,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.393418168067932,
                  "rejected_mean_error": 2.8155438413619995,
                  "gap_rejected_minus_accepted": 1.4221256732940675
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4039846360683441,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.033606715618618,
                  "rejected_mean_error": 2.4652568347313824,
                  "gap_rejected_minus_accepted": 1.4316501191127644
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.4824986849176354,
              "spearman": 0.38105531975370893,
              "auroc_top30_bad": 0.779112380952381,
              "mae": 0.6375763026714325,
              "mse": 0.8733128141850324,
              "expert_lt_perturb_large": 0.356,
              "expert_lt_other_task": 0.488,
              "expert_lt_simvla_seed0": 0.292,
              "same_context_pred_std": 0.4412814107848549,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4849952304363251
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8087697651147843
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.141299578988552
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3004441455682119
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
              "pearson": 0.7947049311313661,
              "spearman": 0.714275745200477,
              "auroc_top30_worst": 0.8454643809523811,
              "pairwise_seed_ranking": 0.6728,
              "predicted_best_mean_error": 1.6141523852348327,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.0429907572269439,
              "gap_to_oracle": 0.03425486373901365,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7444085912704468
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9166445051057216
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1752420570373534
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.370200665234757
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4691521644592287,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4747066646681892,
                  "rejected_mean_error": 3.1974047260284424,
                  "gap_rejected_minus_accepted": 1.7226980613602532
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0706377029418945,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3693758245148042,
                  "rejected_mean_error": 2.4780046036258674,
                  "gap_rejected_minus_accepted": 1.1086287791110632
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7669732570648193,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1752420570373534,
                  "rejected_mean_error": 2.1187108845710756,
                  "gap_rejected_minus_accepted": 0.9434688275337222
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4158016443252563,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9172877552219854,
                  "rejected_mean_error": 1.8907252093071363,
                  "gap_rejected_minus_accepted": 0.9734374540851509
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5102103710174557,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.481688817607032,
                  "rejected_mean_error": 3.23623206615448,
                  "gap_rejected_minus_accepted": 1.754543248547448
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0916630625724792,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3742696952054845,
                  "rejected_mean_error": 2.496783374793946,
                  "gap_rejected_minus_accepted": 1.1225136795884614
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7852863669395447,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1680120918750763,
                  "rejected_mean_error": 2.146274193048477,
                  "gap_rejected_minus_accepted": 0.978262101173401
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4386827945709229,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8641270593045249,
                  "rejected_mean_error": 1.9243089886591396,
                  "gap_rejected_minus_accepted": 1.0601819293546146
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.20094291406670728,
              "spearman": 0.207845092651218,
              "auroc_top30_bad": 0.6844106666666666,
              "mae": 0.6111872272014618,
              "mse": 0.867944485899191,
              "expert_lt_perturb_large": 0.368,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.224,
              "same_context_pred_std": 0.37650533399159763,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7565001580715179
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1639508808374406
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.334129110264778
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4155867836236953
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
              "pearson": 0.334307953932362,
              "spearman": 0.3257616840714779,
              "auroc_top30_worst": 0.6152746666666666,
              "pairwise_seed_ranking": 0.6496,
              "predicted_best_mean_error": 1.6342915766239166,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.02745955133438116,
              "gap_to_oracle": 0.04226764464378352,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.369237578868866
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.5592559888385809
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.562891224718094
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.598282166476697
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0971669435501097,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.616849715789159,
                  "rejected_mean_error": 2.0464855260848998,
                  "gap_rejected_minus_accepted": 0.4296358102957407
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9347994029521942,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.598120850680859,
                  "rejected_mean_error": 1.844496434298567,
                  "gap_rejected_minus_accepted": 0.24637558361770795
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.71809720993042,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.562891224718094,
                  "rejected_mean_error": 1.7567353689193725,
                  "gap_rejected_minus_accepted": 0.1938441442012786
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4889542162418365,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.5580750996121964,
                  "rejected_mean_error": 1.6937984149891132,
                  "gap_rejected_minus_accepted": 0.13572331537691684
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0984309196472166,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6209555941157872,
                  "rejected_mean_error": 2.0289109325408936,
                  "gap_rejected_minus_accepted": 0.40795533842510645
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9369273781776428,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5988119968118515,
                  "rejected_mean_error": 1.8485704537421939,
                  "gap_rejected_minus_accepted": 0.24975845693034238
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7165676355361938,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.539820686817169,
                  "rejected_mean_error": 1.7836815690994263,
                  "gap_rejected_minus_accepted": 0.24386088228225722
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4957424700260162,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.5692560890364269,
                  "rejected_mean_error": 1.692912558183313,
                  "gap_rejected_minus_accepted": 0.12365646914688622
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_object/quantile_action_q90/model.pt"
      },
      {
        "variant": "quantile_action_q95",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.95,
        "best_epoch": 21,
        "best_calib_pinball": 0.09149154275655746,
        "train_time_sec": 16.171353816986084,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.6819584481985771,
              "spearman": 0.3791026105753697,
              "auroc_top30_bad": 0.8756028809523809,
              "mae": 0.7435542718604207,
              "mse": 1.1633733388333238,
              "expert_lt_perturb_large": 0.312,
              "expert_lt_other_task": 0.501,
              "expert_lt_simvla_seed0": 0.285,
              "same_context_pred_std": 0.4680859768822854,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8571041901111602
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.01695620251894
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1686537070646883
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1715962630093097
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
              "pearson": 0.9842988352263595,
              "spearman": 0.9498271628386784,
              "auroc_top30_worst": 0.9913634285714286,
              "pairwise_seed_ranking": 0.6793,
              "predicted_best_mean_error": 1.7403735221028327,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.054050875514745744,
              "gap_to_oracle": 0.03877947437763196,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8285537665486336
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9216363054037094
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.105700706923008
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3105626536289852
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.589391183853153,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.492370027270582,
                  "rejected_mean_error": 4.4196505393981935,
                  "gap_rejected_minus_accepted": 2.9272805121276115
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.342009425163269,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3105626536289852,
                  "rejected_mean_error": 3.2087043530464174,
                  "gap_rejected_minus_accepted": 1.8981416994174323
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.791238248348236,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.105700706923008,
                  "rejected_mean_error": 2.464495450043678,
                  "gap_rejected_minus_accepted": 1.3587947431206702
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3818387985229492,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.9216363054037094,
                  "rejected_mean_error": 2.0729186695098876,
                  "gap_rejected_minus_accepted": 1.1512823641061782
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.732447648048401,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.494714766509003,
                  "rejected_mean_error": 4.4918110775947575,
                  "gap_rejected_minus_accepted": 2.9970963110857545
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.359366536140442,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.305394050637881,
                  "rejected_mean_error": 3.261515438556671,
                  "gap_rejected_minus_accepted": 1.9561213879187902
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7960588932037354,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0998477963805198,
                  "rejected_mean_error": 2.489000998854637,
                  "gap_rejected_minus_accepted": 1.3891532024741173
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3694103956222534,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.9112150521278382,
                  "rejected_mean_error": 2.088827512780825,
                  "gap_rejected_minus_accepted": 1.177612460652987
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6830382600887162,
              "spearman": 0.42153443918308436,
              "auroc_top30_bad": 0.8198297142857145,
              "mae": 0.9849136745870113,
              "mse": 1.502251715319552,
              "expert_lt_perturb_large": 0.416,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.564,
              "same_context_pred_std": 0.4941182485559041,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.1170240497589112
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1923731959819794
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1742867187023163
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.163933071931203
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
              "pearson": 0.8381755974339948,
              "spearman": 0.7370399924735953,
              "auroc_top30_worst": 0.8852998095238095,
              "pairwise_seed_ranking": 0.662,
              "predicted_best_mean_error": 2.0349793404340746,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.06950166428089144,
              "gap_to_oracle": 0.04608411073684704,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0898815093040466
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2479061780449672
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5034865561962127
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5984763028715718
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.856914138793946,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8445459983348846,
                  "rejected_mean_error": 4.19806925201416,
                  "gap_rejected_minus_accepted": 2.3535232536792754
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.218915045261383,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5979762150803651,
                  "rejected_mean_error": 3.5225852750741637,
                  "gap_rejected_minus_accepted": 1.9246090599937986
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.1686463356018066,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5034865561962127,
                  "rejected_mean_error": 2.6563100912094115,
                  "gap_rejected_minus_accepted": 1.1528235350131988
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7051210403442383,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2520242032532494,
                  "rejected_mean_error": 2.35644538848479,
                  "gap_rejected_minus_accepted": 1.1044211852315406
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.92032904624939,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8659203264448379,
                  "rejected_mean_error": 4.251527109146118,
                  "gap_rejected_minus_accepted": 2.3856067827012803
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.239283323287964,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6069155236616492,
                  "rejected_mean_error": 3.5813817183176675,
                  "gap_rejected_minus_accepted": 1.9744661946560182
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.19648814201355,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5061707618236542,
                  "rejected_mean_error": 2.7027912476062776,
                  "gap_rejected_minus_accepted": 1.1966204857826235
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.721567541360855,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.23437756205362,
                  "rejected_mean_error": 2.397617458659697,
                  "gap_rejected_minus_accepted": 1.1632398966060773
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.29679265552237355,
              "spearman": 0.16968381058521773,
              "auroc_top30_bad": 0.7190331428571428,
              "mae": 0.8107082178890705,
              "mse": 1.27232965078246,
              "expert_lt_perturb_large": 0.328,
              "expert_lt_other_task": 0.484,
              "expert_lt_simvla_seed0": 0.22,
              "same_context_pred_std": 0.24371686984650365,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.868017419219017
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1556385157823563
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3425055535912513
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3539405514876048
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
              "pearson": 0.6793242340418394,
              "spearman": 0.5339066887082808,
              "auroc_top30_worst": 0.7917104761904762,
              "pairwise_seed_ranking": 0.632,
              "predicted_best_mean_error": 1.617482524871826,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.03966061758995054,
              "gap_to_oracle": 0.03758500337600701,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8281599662303925
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9857150952403362
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3116634477615357
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4908157817717553
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4457693815231325,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4850247129599254,
                  "rejected_mean_error": 3.104542291402817,
                  "gap_rejected_minus_accepted": 1.6195175784428915
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2241504788398743,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4905553947390715,
                  "rejected_mean_error": 2.115240203305936,
                  "gap_rejected_minus_accepted": 0.6246848085668646
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.971273422241211,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3116634477615357,
                  "rejected_mean_error": 1.9822894938468933,
                  "gap_rejected_minus_accepted": 0.6706260460853577
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.680331975221634,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9853202424491175,
                  "rejected_mean_error": 1.867999309091456,
                  "gap_rejected_minus_accepted": 0.8826790666423384
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4448887825012204,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4970103895664215,
                  "rejected_mean_error": 3.0983379185199738,
                  "gap_rejected_minus_accepted": 1.6013275289535522
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.23615825176239,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4974312657978446,
                  "rejected_mean_error": 2.131208554146782,
                  "gap_rejected_minus_accepted": 0.6337772883489372
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.981395184993744,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3029700095653534,
                  "rejected_mean_error": 2.0113162753582,
                  "gap_rejected_minus_accepted": 0.7083462657928468
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7092004716396332,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9457805695987883,
                  "rejected_mean_error": 1.8968000520359387,
                  "gap_rejected_minus_accepted": 0.9510194824371504
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.053693606797447196,
              "spearman": 0.1460015800052212,
              "auroc_top30_bad": 0.6810080000000001,
              "mae": 0.730125890994072,
              "mse": 1.1115968870404545,
              "expert_lt_perturb_large": 0.384,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 0.304,
              "same_context_pred_std": 0.2610063469389937,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2948503326773644
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3469327980518342
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.420794545006752
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4111342450141906
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
              "pearson": 0.3248582078807153,
              "spearman": 0.37305295478589107,
              "auroc_top30_worst": 0.6785371428571428,
              "pairwise_seed_ranking": 0.6228,
              "predicted_best_mean_error": 1.6346063460111617,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.027144781947135987,
              "gap_to_oracle": 0.04258241403102869,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.5361907773017884
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4734688258897035
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5378220472812654
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.626802465427659
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.450181818008423,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.616625724607044,
                  "rejected_mean_error": 2.048501446723938,
                  "gap_rejected_minus_accepted": 0.4318757221168943
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1664716601371765,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.626676875219274,
                  "rejected_mean_error": 1.759010827293792,
                  "gap_rejected_minus_accepted": 0.13233395207451815
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8811700940132141,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5378220472812654,
                  "rejected_mean_error": 1.7818045463562011,
                  "gap_rejected_minus_accepted": 0.24398249907493574
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6657423973083496,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.4734992583910116,
                  "rejected_mean_error": 1.7220505369765526,
                  "gap_rejected_minus_accepted": 0.24855127858554105
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4748087406158445,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6222936044798957,
                  "rejected_mean_error": 2.016868839263916,
                  "gap_rejected_minus_accepted": 0.3945752347840201
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.184919595718384,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6264256404682915,
                  "rejected_mean_error": 1.7666061463810148,
                  "gap_rejected_minus_accepted": 0.14018050591272324
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.877699613571167,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5375196347236633,
                  "rejected_mean_error": 1.7859826211929322,
                  "gap_rejected_minus_accepted": 0.2484629864692689
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6659583449363708,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.4576461655753,
                  "rejected_mean_error": 1.7305137623440137,
                  "gap_rejected_minus_accepted": 0.27286759676871375
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_object/quantile_action_q95/model.pt"
      },
      {
        "variant": "quantile_context_gated_q80",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.8,
        "best_epoch": 110,
        "best_calib_pinball": 0.03303265944123268,
        "train_time_sec": 50.966657876968384,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9993021153220701,
              "spearman": 0.998128545875301,
              "auroc_top30_bad": 0.9993770952380953,
              "mae": 0.0319411586313392,
              "mse": 0.0025189054984524352,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8127738106588591,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.00385679093003273
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19993852259516717
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6187410235613584
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9866352160274983
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
              "pearson": 0.9992746689211927,
              "spearman": 0.9987820661192535,
              "auroc_top30_worst": 0.9994611428571428,
              "pairwise_seed_ranking": 0.9515,
              "predicted_best_mean_error": 1.7040422359704972,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.09038216164708124,
              "gap_to_oracle": 0.0024481882452964676,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7248313600420951
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8796985754728317
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0840215578913688
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3054179914712907
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.240602016448976,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4900109463731448,
                  "rejected_mean_error": 4.4408822674751285,
                  "gap_rejected_minus_accepted": 2.9508713211019835
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0641724467277527,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3054179914712907,
                  "rejected_mean_error": 3.224138339519501,
                  "gap_rejected_minus_accepted": 1.9187203480482102
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5298425555229187,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0840215578913688,
                  "rejected_mean_error": 2.4861745990753175,
                  "gap_rejected_minus_accepted": 1.4021530411839487
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.104343742132187,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8796985754728317,
                  "rejected_mean_error": 2.0868979128201803,
                  "gap_rejected_minus_accepted": 1.2071993373473486
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.302732610702515,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.491753253042698,
                  "rejected_mean_error": 4.518464698791504,
                  "gap_rejected_minus_accepted": 3.0267114457488056
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.064439594745636,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3020561287005743,
                  "rejected_mean_error": 3.2715292043685915,
                  "gap_rejected_minus_accepted": 1.9694730756680172
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5196106433868408,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0765248587727547,
                  "rejected_mean_error": 2.512323936462402,
                  "gap_rejected_minus_accepted": 1.4357990776896474
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1080533266067505,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8669158264398574,
                  "rejected_mean_error": 2.1035939213434856,
                  "gap_rejected_minus_accepted": 1.236678094903628
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9916877798096744,
              "spearman": 0.9900403427794446,
              "auroc_top30_bad": 0.9941219047619048,
              "mae": 0.11710010719071143,
              "mse": 0.03411678634304605,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9377714293267596,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.044528997480869296
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1936865582227707
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5843709044098854
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.018808990708987
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
              "pearson": 0.9905068178032623,
              "spearman": 0.9951851100064706,
              "auroc_top30_worst": 0.9963672380952381,
              "pairwise_seed_ranking": 0.9116,
              "predicted_best_mean_error": 1.9935051807165145,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.11097582399845152,
              "gap_to_oracle": 0.004609951019286962,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6194967725276948
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8645871972235349
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2198950929164887
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5538230853230715
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.381587886810303,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.842737490415573,
                  "rejected_mean_error": 4.214345823287964,
                  "gap_rejected_minus_accepted": 2.3716083328723907
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.914107382297516,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5525640175144089,
                  "rejected_mean_error": 3.658531693985668,
                  "gap_rejected_minus_accepted": 2.105967676471259
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8998913168907166,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2198950929164887,
                  "rejected_mean_error": 2.939901554489136,
                  "gap_rejected_minus_accepted": 1.7200064615726471
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3225052058696747,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8658456207273867,
                  "rejected_mean_error": 2.4854463450809425,
                  "gap_rejected_minus_accepted": 1.619600724353556
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.451520109176636,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.865855475531684,
                  "rejected_mean_error": 4.252110767364502,
                  "gap_rejected_minus_accepted": 2.3862552918328177
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.013797402381897,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5593788152072519,
                  "rejected_mean_error": 3.7224827418251643,
                  "gap_rejected_minus_accepted": 2.1631039266179126
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9188902974128723,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2199705400466918,
                  "rejected_mean_error": 2.98899146938324,
                  "gap_rejected_minus_accepted": 1.769020929336548
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3580355644226074,
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
              "pearson": 0.9902580359788625,
              "spearman": 0.9894922828030577,
              "auroc_top30_bad": 0.9918666666666667,
              "mae": 0.09886371259721927,
              "mse": 0.020206469199365834,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7670458146937672,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.03277193158864975
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18515313098430633
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6270201221823692
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0396192170699436
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
              "pearson": 0.9884637020750779,
              "spearman": 0.990737023191695,
              "auroc_top30_worst": 0.988007619047619,
              "pairwise_seed_ranking": 0.8772,
              "predicted_best_mean_error": 1.5898192621469498,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06732388031482683,
              "gap_to_oracle": 0.009921740651130717,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.40801270699501035
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.654679879737206
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.024940533924103
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3034542467929662
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.773740673065186,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4593239409658645,
                  "rejected_mean_error": 3.3358492393493653,
                  "gap_rejected_minus_accepted": 1.8765252983835008
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0844644904136658,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3026707583964825,
                  "rejected_mean_error": 2.6776935715264023,
                  "gap_rejected_minus_accepted": 1.3750228131299198
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7481773495674133,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.024940533924103,
                  "rejected_mean_error": 2.2690124076843263,
                  "gap_rejected_minus_accepted": 1.2440718737602234
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.117266833782196,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6559466194040098,
                  "rejected_mean_error": 1.9780248630008677,
                  "gap_rejected_minus_accepted": 1.3220782435968579
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8796101808547974,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4650840894381205,
                  "rejected_mean_error": 3.3856746196746825,
                  "gap_rejected_minus_accepted": 1.920590530236562
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1097258925437927,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.300720803559145,
                  "rejected_mean_error": 2.7150951642838734,
                  "gap_rejected_minus_accepted": 1.4143743607247283
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.756823718547821,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0150735774040223,
                  "rejected_mean_error": 2.299212707519531,
                  "gap_rejected_minus_accepted": 1.284139130115509
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1327238380908966,
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
              "pearson": 0.9889785621116083,
              "spearman": 0.9818214578699909,
              "auroc_top30_bad": 0.982408380952381,
              "mae": 0.0770292185747996,
              "mse": 0.014852610672485408,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7238556876437542,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.047520946741104124
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2162415165424347
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7828074842453003
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1380474355697632
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
              "pearson": 0.967366207434229,
              "spearman": 0.9629901361856873,
              "auroc_top30_worst": 0.962767238095238,
              "pairwise_seed_ranking": 0.9084,
              "predicted_best_mean_error": 1.5990525288581847,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.062698599100113,
              "gap_to_oracle": 0.007028596878051685,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8479326975345611
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1005060295454967
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3581868673801423
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5204116316047558
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.077032041549683,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5964038513236576,
                  "rejected_mean_error": 2.230498306274414,
                  "gap_rejected_minus_accepted": 0.6340944549507566
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9208536744117737,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5200461778022436,
                  "rejected_mean_error": 2.078221573235509,
                  "gap_rejected_minus_accepted": 0.5581753954332653
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7664129734039307,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3581868673801423,
                  "rejected_mean_error": 1.9614397262573242,
                  "gap_rejected_minus_accepted": 0.6032528588771819
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.439613789319992,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1015451260077687,
                  "rejected_mean_error": 1.846299889629653,
                  "gap_rejected_minus_accepted": 0.7447547636218843
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.061228346824646,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6063539804352653,
                  "rejected_mean_error": 2.160325455665588,
                  "gap_rejected_minus_accepted": 0.5539714752303229
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9204656779766083,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5263939410607446,
                  "rejected_mean_error": 2.063525635098654,
                  "gap_rejected_minus_accepted": 0.5371316940379094
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7820578217506409,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3701235947608947,
                  "rejected_mean_error": 1.9533786611557007,
                  "gap_rejected_minus_accepted": 0.583255066394806
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4508919715881348,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1092465027930245,
                  "rejected_mean_error": 1.847889049805422,
                  "gap_rejected_minus_accepted": 0.7386425470123974
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_object/quantile_context_gated_q80/model.pt"
      },
      {
        "variant": "quantile_context_gated_q90",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.9,
        "best_epoch": 119,
        "best_calib_pinball": 0.023262524977326393,
        "train_time_sec": 51.039209842681885,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9986106827589506,
              "spearman": 0.9976453958282231,
              "auroc_top30_bad": 0.9991018095238094,
              "mae": 0.06517404072862118,
              "mse": 0.007866268361179277,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.824594707648243,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.00583135960996151
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2007826127111912
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6188428534477949
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9867378096719582
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
              "pearson": 0.9986266104886687,
              "spearman": 0.998645867361802,
              "auroc_top30_worst": 0.9996704761904762,
              "pairwise_seed_ranking": 0.9166,
              "predicted_best_mean_error": 1.7067806596159936,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.08764373800158487,
              "gap_to_oracle": 0.005186611890792836,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7255487788319588
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.880209939455986
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0838856662154197
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.305279589676857
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.3230092287063604,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4904324799577395,
                  "rejected_mean_error": 4.437088465213775,
                  "gap_rejected_minus_accepted": 2.9466559852560357
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.099963128566742,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.305279589676857,
                  "rejected_mean_error": 3.2245535449028013,
                  "gap_rejected_minus_accepted": 1.9192739552259444
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5645827651023865,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0838856662154197,
                  "rejected_mean_error": 2.4863104907512663,
                  "gap_rejected_minus_accepted": 1.4024248245358466
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1334900259971619,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.880209939455986,
                  "rejected_mean_error": 2.0867274581591286,
                  "gap_rejected_minus_accepted": 1.2065175187031425
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.387205696105957,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4924941385123465,
                  "rejected_mean_error": 4.511796729564667,
                  "gap_rejected_minus_accepted": 3.0193025910523206
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.110502600669861,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3021014746427535,
                  "rejected_mean_error": 3.2713931665420533,
                  "gap_rejected_minus_accepted": 1.9692916918992998
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5681825876235962,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0766248252987862,
                  "rejected_mean_error": 2.512223969936371,
                  "gap_rejected_minus_accepted": 1.4355991446375846
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1245495975017548,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8677337490320206,
                  "rejected_mean_error": 2.103321280479431,
                  "gap_rejected_minus_accepted": 1.2355875314474103
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9894938175408663,
              "spearman": 0.9884378630800825,
              "auroc_top30_bad": 0.9939367619047619,
              "mae": 0.1508531800317578,
              "mse": 0.05134187723368193,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9429756736716075,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0646958401799202
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19179230477809905
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5843984240174294
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0189680146932603
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
              "pearson": 0.9873356668777536,
              "spearman": 0.9938522052174114,
              "auroc_top30_worst": 0.9949013333333334,
              "pairwise_seed_ranking": 0.882,
              "predicted_best_mean_error": 1.9950066462755203,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10947435843944575,
              "gap_to_oracle": 0.006111416578292728,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6186195857524872
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8643795701746757
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.221277250432968
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5555871876000342
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.48792462348938,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8436828558974796,
                  "rejected_mean_error": 4.205837533950806,
                  "gap_rejected_minus_accepted": 2.3621546780533267
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.9782885313034058,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5546509663285162,
                  "rejected_mean_error": 3.652284182679539,
                  "gap_rejected_minus_accepted": 2.0976332163510225
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9065182209014893,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.221277250432968,
                  "rejected_mean_error": 2.9385193969726564,
                  "gap_rejected_minus_accepted": 1.7172421465396883
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3484539985656738,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8660709956012214,
                  "rejected_mean_error": 2.4853710597708996,
                  "gap_rejected_minus_accepted": 1.6193000641696782
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.552844381332397,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8666733943091498,
                  "rejected_mean_error": 4.24474949836731,
                  "gap_rejected_minus_accepted": 2.37807610405816
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.0564300417900085,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5624311123302277,
                  "rejected_mean_error": 3.7134227487776013,
                  "gap_rejected_minus_accepted": 2.1509916364473733
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9339517951011658,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2195120267868043,
                  "rejected_mean_error": 2.9894499826431273,
                  "gap_rejected_minus_accepted": 1.769937955856323
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3811518847942352,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.862742231005714,
                  "rejected_mean_error": 2.5228208054833234,
                  "gap_rejected_minus_accepted": 1.6600785744776094
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9861218986241518,
              "spearman": 0.9892652181056496,
              "auroc_top30_bad": 0.9926986666666667,
              "mae": 0.1224694734916091,
              "mse": 0.029968851082494745,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7871183628660109,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.039166889309883116
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18195581176280975
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6283348159193992
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.039279691274961
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
              "pearson": 0.9759999403048161,
              "spearman": 0.9877074455727654,
              "auroc_top30_worst": 0.9881965714285714,
              "pairwise_seed_ranking": 0.8596,
              "predicted_best_mean_error": 1.589910255432129,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06723288702964769,
              "gap_to_oracle": 0.010012733936309859,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4164019811153412
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6547558596118902
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0281758721351624
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.303636617053038
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9166110754013066,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.463811174445682,
                  "rejected_mean_error": 3.2954641380310057,
                  "gap_rejected_minus_accepted": 1.8316529635853236
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0991403460502625,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.302944439134323,
                  "rejected_mean_error": 2.6768742780715895,
                  "gap_rejected_minus_accepted": 1.3739298389372665
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7868228554725647,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0281758721351624,
                  "rejected_mean_error": 2.2657770694732666,
                  "gap_rejected_minus_accepted": 1.2376011973381043
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1610669493675232,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6561280944096014,
                  "rejected_mean_error": 1.9779642422145816,
                  "gap_rejected_minus_accepted": 1.32183614780498
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.0469380378723137,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4718088867929247,
                  "rejected_mean_error": 3.3251514434814453,
                  "gap_rejected_minus_accepted": 1.8533425566885207
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1306058764457703,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.300581877563089,
                  "rejected_mean_error": 2.715507531922961,
                  "gap_rejected_minus_accepted": 1.4149256543598718
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.79947429895401,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0186800398826599,
                  "rejected_mean_error": 2.2956062450408936,
                  "gap_rejected_minus_accepted": 1.2769262051582337
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1834623515605927,
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
              "pearson": 0.9853106797444748,
              "spearman": 0.9750312494859915,
              "auroc_top30_bad": 0.9775169523809524,
              "mae": 0.09811336706476285,
              "mse": 0.021826557879315672,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7300275765202328,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06596197193861007
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21760599236488343
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7833992302894592
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1410532842636107
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
              "pearson": 0.9588671975219378,
              "spearman": 0.9503625922320591,
              "auroc_top30_worst": 0.9508510476190477,
              "pairwise_seed_ranking": 0.9024,
              "predicted_best_mean_error": 1.5983057310581208,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06344539690017692,
              "gap_to_oracle": 0.00628179907798776,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8529107763767242
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1012989023748117
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3613543026447297
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5226923667355132
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0512630701065064,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6008308633433448,
                  "rejected_mean_error": 2.190655198097229,
                  "gap_rejected_minus_accepted": 0.5898243347538841
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9179835617542267,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5223127142024269,
                  "rejected_mean_error": 2.071436446695663,
                  "gap_rejected_minus_accepted": 0.5491237324932361
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7996589541435242,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3613543026447297,
                  "rejected_mean_error": 1.9582722909927368,
                  "gap_rejected_minus_accepted": 0.5969179883480071
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4880734086036682,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1023991748738213,
                  "rejected_mean_error": 1.8460145990265853,
                  "gap_rejected_minus_accepted": 0.7436154241527639
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0456292390823365,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6087428911526997,
                  "rejected_mean_error": 2.138825259208679,
                  "gap_rejected_minus_accepted": 0.5300823680559794
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.938759833574295,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5275145147573501,
                  "rejected_mean_error": 2.060199487776983,
                  "gap_rejected_minus_accepted": 0.532684973019633
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8061286211013794,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3771658616065978,
                  "rejected_mean_error": 1.9463363943099976,
                  "gap_rejected_minus_accepted": 0.5691705327033998
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.504343956708908,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1121270779579404,
                  "rejected_mean_error": 1.8469185886536053,
                  "gap_rejected_minus_accepted": 0.7347915106956648
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_object/quantile_context_gated_q90/model.pt"
      },
      {
        "variant": "quantile_context_gated_q95",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.95,
        "best_epoch": 88,
        "best_calib_pinball": 0.014972474426031113,
        "train_time_sec": 50.86443209648132,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9974521310184299,
              "spearman": 0.995394382170368,
              "auroc_top30_bad": 0.9977140714285714,
              "mae": 0.13789054047912358,
              "mse": 0.026791503286022925,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8386862800112226,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.01992499140650034
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20146812245249748
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6188649991244077
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9880029423216978
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
              "pearson": 0.9977170769479726,
              "spearman": 0.9971316005011951,
              "auroc_top30_worst": 0.9984177142857142,
              "pairwise_seed_ranking": 0.8914,
              "predicted_best_mean_error": 1.7089182124733926,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.08550618514418584,
              "gap_to_oracle": 0.007324164748191864,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7289701119065285
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.881656136393547
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0841098037600518
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3063135798374812
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.470723295211792,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4904169313046667,
                  "rejected_mean_error": 4.437228403091431,
                  "gap_rejected_minus_accepted": 2.9468114717867637
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2277368903160095,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3063135798374812,
                  "rejected_mean_error": 3.221451574420929,
                  "gap_rejected_minus_accepted": 1.915137994583448
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6428278088569641,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0841098037600518,
                  "rejected_mean_error": 2.4860863532066344,
                  "gap_rejected_minus_accepted": 1.4019765494465826
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.176795244216919,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.881656136393547,
                  "rejected_mean_error": 2.086245392513275,
                  "gap_rejected_minus_accepted": 1.204589256119728
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5315083026885987,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.492085879544417,
                  "rejected_mean_error": 4.515471060276031,
                  "gap_rejected_minus_accepted": 3.023385180731614
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2385602593421936,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.303233334740003,
                  "rejected_mean_error": 3.267997586250305,
                  "gap_rejected_minus_accepted": 1.964764251510302
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6413196325302124,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0766721411347389,
                  "rejected_mean_error": 2.512176654100418,
                  "gap_rejected_minus_accepted": 1.4355045129656792
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1697635650634766,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8695811244249344,
                  "rejected_mean_error": 2.102705488681793,
                  "gap_rejected_minus_accepted": 1.2331243642568586
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.987112226921525,
              "spearman": 0.9859358524671694,
              "auroc_top30_bad": 0.9915215238095239,
              "mae": 0.2236728766027838,
              "mse": 0.0978622745168118,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9626248197293403,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09616845834255218
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1942655947446823
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5845874989151955
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.020497311758995
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
              "pearson": 0.9865996106875266,
              "spearman": 0.9924632609684871,
              "auroc_top30_worst": 0.9959527619047619,
              "pairwise_seed_ranking": 0.854,
              "predicted_best_mean_error": 1.9985880423784257,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.10589296233654033,
              "gap_to_oracle": 0.009692812681198149,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6185220100879669
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8665398927644278
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2234178308010102
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5554547364205948
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.766366195678712,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8441728399859534,
                  "rejected_mean_error": 4.201427677154541,
                  "gap_rejected_minus_accepted": 2.357254837168588
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.1019354462623596,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5540128258974346,
                  "rejected_mean_error": 3.6541945263981437,
                  "gap_rejected_minus_accepted": 2.100181700500709
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9995981454849243,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2234178308010102,
                  "rejected_mean_error": 2.936378816604614,
                  "gap_rejected_minus_accepted": 1.712960985803604
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4058522880077362,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8682236262975028,
                  "rejected_mean_error": 2.4846519846290254,
                  "gap_rejected_minus_accepted": 1.6164283583315227
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.814725303649902,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8666733943091498,
                  "rejected_mean_error": 4.24474949836731,
                  "gap_rejected_minus_accepted": 2.37807610405816
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.1916850805282593,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5624311123302277,
                  "rejected_mean_error": 3.7134227487776013,
                  "gap_rejected_minus_accepted": 2.1509916364473733
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0173884630203247,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.223924563407898,
                  "rejected_mean_error": 2.9850374460220337,
                  "gap_rejected_minus_accepted": 1.7611128826141358
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.414663553237915,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8677799474625361,
                  "rejected_mean_error": 2.521123606890918,
                  "gap_rejected_minus_accepted": 1.6533436594283821
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9847565179640452,
              "spearman": 0.9823199741399337,
              "auroc_top30_bad": 0.9853824761904763,
              "mae": 0.1747513441424817,
              "mse": 0.051583238713714584,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7973484704059031,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06003817254304886
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18352945263385773
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6281466611266137
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0426273761351903
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
              "pearson": 0.9735694195393457,
              "spearman": 0.9783766696810687,
              "auroc_top30_worst": 0.9782247619047619,
              "pairwise_seed_ranking": 0.8444,
              "predicted_best_mean_error": 1.5923881299495697,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06475501251220694,
              "gap_to_oracle": 0.012490608453750607,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4239827482700348
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6562069333516635
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0311714150428772
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.308747199870376
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1024820566177373,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4613952808909947,
                  "rejected_mean_error": 3.3172071800231935,
                  "gap_rejected_minus_accepted": 1.8558118991321988
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.200350821018219,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.307883792714859,
                  "rejected_mean_error": 2.6620877786947132,
                  "gap_rejected_minus_accepted": 1.3542039859798543
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8706151843070984,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0311714150428772,
                  "rejected_mean_error": 2.2627815265655515,
                  "gap_rejected_minus_accepted": 1.2316101115226743
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2110242247581482,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6567426480043429,
                  "rejected_mean_error": 1.9777589537672453,
                  "gap_rejected_minus_accepted": 1.3210163057629023
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2491826534271238,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.466823774708642,
                  "rejected_mean_error": 3.37001745223999,
                  "gap_rejected_minus_accepted": 1.9031936775313483
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2112924456596375,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3047751701451877,
                  "rejected_mean_error": 2.7030607745760964,
                  "gap_rejected_minus_accepted": 1.3982856044309087
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8800358772277832,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0233852553367615,
                  "rejected_mean_error": 2.290901029586792,
                  "gap_rejected_minus_accepted": 1.2675157742500305
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1961394250392914,
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
              "pearson": 0.9857547428613517,
              "spearman": 0.9766901825817544,
              "auroc_top30_bad": 0.9782902857142859,
              "mae": 0.15660124142877757,
              "mse": 0.03892109889428847,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7507979989643732,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07095768421888352
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21946416501998903
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7824553239822387
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1384548370997112
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
              "pearson": 0.9568021625902342,
              "spearman": 0.9547694404924422,
              "auroc_top30_worst": 0.957824,
              "pairwise_seed_ranking": 0.8696,
              "predicted_best_mean_error": 1.5988854401111603,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06286568784713742,
              "gap_to_oracle": 0.006861508131027261,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8609613473415375
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1020430591052923
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3601844656467437
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5211340149900299
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2918785333633425,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5988473885059358,
                  "rejected_mean_error": 2.2085064716339113,
                  "gap_rejected_minus_accepted": 0.6096590831279756
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0796303749084473,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5208864026606528,
                  "rejected_mean_error": 2.075706267509217,
                  "gap_rejected_minus_accepted": 0.554819864848564
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8899827599525452,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3601844656467437,
                  "rejected_mean_error": 1.9594421279907226,
                  "gap_rejected_minus_accepted": 0.5992576623439789
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5728650987148285,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1034964030733505,
                  "rejected_mean_error": 1.8456480756258888,
                  "gap_rejected_minus_accepted": 0.7421516725525383
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2779655694961547,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6056308881441752,
                  "rejected_mean_error": 2.1668332862854003,
                  "gap_rejected_minus_accepted": 0.5612023981412251
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.099162518978119,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5265887271274219,
                  "rejected_mean_error": 2.062947460583278,
                  "gap_rejected_minus_accepted": 0.5363587334558562
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9050990343093872,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3737660250663757,
                  "rejected_mean_error": 1.9497362308502197,
                  "gap_rejected_minus_accepted": 0.5759702057838441
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.596364676952362,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.113580498430464,
                  "rejected_mean_error": 1.8464289336281026,
                  "gap_rejected_minus_accepted": 0.7328484351976385
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_object/quantile_context_gated_q95/model.pt"
      },
      {
        "variant": "quantile_seed_relative_q90",
        "feature_mode": "M4_seed_relative",
        "kind": "mlp_big",
        "q": 0.9,
        "best_epoch": 54,
        "best_calib_pinball": 0.03370804339647293,
        "train_time_sec": 53.51371884346008,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9972122877108064,
              "spearman": 0.9944979525268642,
              "auroc_top30_bad": 0.996080238095238,
              "mae": 0.18141027905010998,
              "mse": 0.05431178944657716,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8917956224532723,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.019612548425793647
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20063500384688376
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.61921825697124
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9882329430401325
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
              "pearson": 0.9978477123758678,
              "spearman": 0.9965990479678803,
              "auroc_top30_worst": 0.9990670476190477,
              "pairwise_seed_ranking": 0.9326,
              "predicted_best_mean_error": 1.7047314284145831,
              "seed0_mean_error": 1.7944243976175784,
              "random_seed_mean_error": 1.78608657553792,
              "oracle_best_mean_error": 1.7015940477252007,
              "improvement_over_seed0": 0.0896929692029953,
              "gap_to_oracle": 0.0031373806893824074,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7279236103892326
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8819067567586899
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0848906618475913
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3055186997969945
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850980784833432
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5748784065246584,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4903775952061018,
                  "rejected_mean_error": 4.437582427978516,
                  "gap_rejected_minus_accepted": 2.947204832772414
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3739492297172546,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3055186997969945,
                  "rejected_mean_error": 3.223836214542389,
                  "gap_rejected_minus_accepted": 1.9183175147453946
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7301524877548218,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0848906618475913,
                  "rejected_mean_error": 2.485305495119095,
                  "gap_rejected_minus_accepted": 1.4004148332715036
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1931172907352448,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8819067567586899,
                  "rejected_mean_error": 2.086161852391561,
                  "gap_rejected_minus_accepted": 1.2042550956328713
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.6724810838699344,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4921214576893382,
                  "rejected_mean_error": 4.515150856971741,
                  "gap_rejected_minus_accepted": 3.023029399282403
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3740004897117615,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3023243473768233,
                  "rejected_mean_error": 3.2707245483398437,
                  "gap_rejected_minus_accepted": 1.9684002009630204
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7241936922073364,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0774623940587045,
                  "rejected_mean_error": 2.511386401176453,
                  "gap_rejected_minus_accepted": 1.4339240071177484
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.187526136636734,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.870142462849617,
                  "rejected_mean_error": 2.1025183758735655,
                  "gap_rejected_minus_accepted": 1.2323759130239484
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9890433001226748,
              "spearman": 0.9812170132716445,
              "auroc_top30_bad": 0.9901241904761905,
              "mae": 0.20162167264863384,
              "mse": 0.07364612899313959,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9659475336976411,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.088976034283638
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2118503596305847
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5892782186150551
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0211718707164128
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
              "pearson": 0.9897693644521199,
              "spearman": 0.985313907528901,
              "auroc_top30_worst": 0.9989851428571428,
              "pairwise_seed_ranking": 0.9148,
              "predicted_best_mean_error": 1.993032815337181,
              "seed0_mean_error": 2.104481004714966,
              "random_seed_mean_error": 2.077451464056969,
              "oracle_best_mean_error": 1.9888952296972275,
              "improvement_over_seed0": 0.111448189377785,
              "gap_to_oracle": 0.004137585639953478,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6288585097789764
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8754178582666776
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2291908774852753
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5492073583132677
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.079898323702812
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.521091127395631,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8435539214611054,
                  "rejected_mean_error": 4.206997943878174,
                  "gap_rejected_minus_accepted": 2.3634440224170685
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.213434934616089,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5481260355597755,
                  "rejected_mean_error": 3.6718172821373987,
                  "gap_rejected_minus_accepted": 2.123691246577623
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9719663858413696,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2291908774852753,
                  "rejected_mean_error": 2.930605769920349,
                  "gap_rejected_minus_accepted": 1.7014148924350738
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3758086264133453,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8772943361689107,
                  "rejected_mean_error": 2.481621960947328,
                  "gap_rejected_minus_accepted": 1.6043276247784173
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.5592375755310055,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.86610019048055,
                  "rejected_mean_error": 4.249908332824707,
                  "gap_rejected_minus_accepted": 2.383808142344157
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.315537393093109,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5548569416617328,
                  "rejected_mean_error": 3.7359048109205943,
                  "gap_rejected_minus_accepted": 2.1810478692588617
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0041069984436035,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2293762350082398,
                  "rejected_mean_error": 2.979585774421692,
                  "gap_rejected_minus_accepted": 1.750209539413452
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.378494679927826,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.875371293416099,
                  "rejected_mean_error": 2.5185660946177926,
                  "gap_rejected_minus_accepted": 1.6431948012016937
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9852025337078844,
              "spearman": 0.9741716399813859,
              "auroc_top30_bad": 0.9666224761904761,
              "mae": 0.18256479593024125,
              "mse": 0.054368656699926715,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8180741882171562,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06543637609481812
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20040404992103578
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6312310319304466
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.045540721344948
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
              "pearson": 0.9826450027726007,
              "spearman": 0.9656521794893951,
              "auroc_top30_worst": 0.9490620952380953,
              "pairwise_seed_ranking": 0.8964,
              "predicted_best_mean_error": 1.5876846829652786,
              "seed0_mean_error": 1.6571431424617766,
              "random_seed_mean_error": 1.6510543216466904,
              "oracle_best_mean_error": 1.579897521495819,
              "improvement_over_seed0": 0.06945845949649798,
              "gap_to_oracle": 0.007787161469459569,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4226560094356537
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6591753827837797
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0340392603874207
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3135723800166075
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6469764708042145
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8441379070281982,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4587865120040047,
                  "rejected_mean_error": 3.3406861000061037,
                  "gap_rejected_minus_accepted": 1.881899588002099
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.260236620903015,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.312936362169341,
                  "rejected_mean_error": 2.6469623551201136,
                  "gap_rejected_minus_accepted": 1.3340259929507725
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8988201022148132,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0340392603874207,
                  "rejected_mean_error": 2.259913681221008,
                  "gap_rejected_minus_accepted": 1.2258744208335874
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1927227079868317,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.6605932520220454,
                  "rejected_mean_error": 1.9764726794262197,
                  "gap_rejected_minus_accepted": 1.3158794274041743
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9519893169403075,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4650620998276604,
                  "rejected_mean_error": 3.385872526168823,
                  "gap_rejected_minus_accepted": 1.9208104263411627
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2609394788742065,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3087963544748684,
                  "rejected_mean_error": 2.6911248782324413,
                  "gap_rejected_minus_accepted": 1.3823285237575729
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.902892827987671,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0243180994987489,
                  "rejected_mean_error": 2.289968185424805,
                  "gap_rejected_minus_accepted": 1.265650085926056
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2117943167686462,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6496417484586201,
                  "rejected_mean_error": 1.9965687457890433,
                  "gap_rejected_minus_accepted": 1.3469269973304232
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9791104931751007,
              "spearman": 0.9687367408656882,
              "auroc_top30_bad": 0.9709828571428571,
              "mae": 0.19183481593135512,
              "mse": 0.059848548119840486,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7448256260209528,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06712165683507919
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22580678870677948
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7862565514564515
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1418926907221476
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
              "pearson": 0.9400130496739224,
              "spearman": 0.9255367613035274,
              "auroc_top30_worst": 0.928911238095238,
              "pairwise_seed_ranking": 0.8732,
              "predicted_best_mean_error": 1.5986058104038239,
              "seed0_mean_error": 1.6617511279582977,
              "random_seed_mean_error": 1.6605152992010117,
              "oracle_best_mean_error": 1.592023931980133,
              "improvement_over_seed0": 0.06314531755447383,
              "gap_to_oracle": 0.006581878423690846,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8593590223789215
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.105211716145277
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.368737662744522
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5273217895963807
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6598132968187331
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3493721723556518,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.597914691845576,
                  "rejected_mean_error": 2.2169007415771484,
                  "gap_rejected_minus_accepted": 0.6189860497315725
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.171048939228058,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.526919208983856,
                  "rejected_mean_error": 2.0576463968228227,
                  "gap_rejected_minus_accepted": 0.5307271878389668
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.982646882534027,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.368737662744522,
                  "rejected_mean_error": 1.9508889308929442,
                  "gap_rejected_minus_accepted": 0.5821512681484222
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5131847262382507,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1059672037443034,
                  "rejected_mean_error": 1.8448227174508534,
                  "gap_rejected_minus_accepted": 0.73885551370655
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3530319690704347,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6070637366506788,
                  "rejected_mean_error": 2.153937649726868,
                  "gap_rejected_minus_accepted": 0.546873913076189
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1722663044929504,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.535290391368662,
                  "rejected_mean_error": 2.037118711168804,
                  "gap_rejected_minus_accepted": 0.5018283198001419
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9847761392593384,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3749493107795716,
                  "rejected_mean_error": 1.9485529451370238,
                  "gap_rejected_minus_accepted": 0.5736036343574522
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5227202475070953,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1146080427699618,
                  "rejected_mean_error": 1.8460827555885926,
                  "gap_rejected_minus_accepted": 0.7314747128186307
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_object/quantile_seed_relative_q90/model.pt"
      }
    ],
    "holdout_object_bowl": [
      {
        "variant": "quantile_action_q80",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.8,
        "best_epoch": 39,
        "best_calib_pinball": 0.17491483688354492,
        "train_time_sec": 15.987872838973999,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8196123495676908,
              "spearman": 0.764999129046066,
              "auroc_top30_bad": 0.9435748095238096,
              "mae": 0.3069791381120682,
              "mse": 0.32256451525919266,
              "expert_lt_perturb_large": 0.818,
              "expert_lt_other_task": 0.505,
              "expert_lt_simvla_seed0": 0.659,
              "same_context_pred_std": 0.5854448947518226,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.28360897025465964
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5060125291645526
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7468524983525276
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0028236230254173
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3045572458028794
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9913298974843536,
              "spearman": 0.9901087923641143,
              "auroc_top30_worst": 0.9967146666666666,
              "pairwise_seed_ranking": 0.7643,
              "predicted_best_mean_error": 1.5503050000965595,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.06530332791805282,
              "gap_to_oracle": 0.021445765912532666,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6783524190783501
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.813127270436287
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0145013105034828
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2434094157775244
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7728833436965954,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.406460135585732,
                  "rejected_mean_error": 3.4496466517448425,
                  "gap_rejected_minus_accepted": 2.0431865161591105
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0327794551849365,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2434094157775244,
                  "rejected_mean_error": 2.712886901473999,
                  "gap_rejected_minus_accepted": 1.4694774856964747
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4602425694465637,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0145013105034828,
                  "rejected_mean_error": 2.207056263899803,
                  "gap_rejected_minus_accepted": 1.1925549533963202
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0716802179813385,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.813127270436287,
                  "rejected_mean_error": 1.8766626261234283,
                  "gap_rejected_minus_accepted": 1.0635353556871414
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.773466944694519,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4119692756401168,
                  "rejected_mean_error": 3.448359799385071,
                  "gap_rejected_minus_accepted": 2.036390523744954
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0414270162582397,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2446854839722314,
                  "rejected_mean_error": 2.728376860141754,
                  "gap_rejected_minus_accepted": 1.4836913761695227
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4709978103637695,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0074938772320747,
                  "rejected_mean_error": 2.22372277879715,
                  "gap_rejected_minus_accepted": 1.2162289015650751
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0546438097953796,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8029517987966538,
                  "rejected_mean_error": 1.8864938377539318,
                  "gap_rejected_minus_accepted": 1.0835420389572779
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5681273418710595,
              "spearman": 0.5552530947102855,
              "auroc_top30_bad": 0.7690780952380951,
              "mae": 0.46940106297135353,
              "mse": 0.4588885332655369,
              "expert_lt_perturb_large": 0.808,
              "expert_lt_other_task": 0.468,
              "expert_lt_simvla_seed0": 0.616,
              "same_context_pred_std": 0.5045486013077691,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.35141491174697875
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6235062587738037
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9688053150653839
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1801969513177872
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.40430782941453025,
              "spearman": 0.4547124563919721,
              "auroc_top30_worst": 0.7065325714285714,
              "pairwise_seed_ranking": 0.6876,
              "predicted_best_mean_error": 1.4943523797988891,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.034441443920135484,
              "gap_to_oracle": 0.0315093576908112,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0600635232925415
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.200468788162256
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.38746669921875
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4693351504899292
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1637928009033205,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5169855396482679,
                  "rejected_mean_error": 1.7121137599945069,
                  "gap_rejected_minus_accepted": 0.195128220346239
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9120585322380066,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.469184015960042,
                  "rejected_mean_error": 1.738011275236599,
                  "gap_rejected_minus_accepted": 0.26882725927655704
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.613783061504364,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.38746669921875,
                  "rejected_mean_error": 1.6855300241470337,
                  "gap_rejected_minus_accepted": 0.2980633249282836
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3182614147663116,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2025987713481672,
                  "rejected_mean_error": 1.6480357915385684,
                  "gap_rejected_minus_accepted": 0.4454370201904012
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1657031774520874,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.508084275457594,
                  "rejected_mean_error": 1.7151797580718995,
                  "gap_rejected_minus_accepted": 0.20709548261430544
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9156757593154907,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4713239178938025,
                  "rejected_mean_error": 1.6993790997399225,
                  "gap_rejected_minus_accepted": 0.22805518184612006
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6112458109855652,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3692965784072877,
                  "rejected_mean_error": 1.6882910690307618,
                  "gap_rejected_minus_accepted": 0.31899449062347407
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2769878506660461,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1681185658015902,
                  "rejected_mean_error": 1.650304739488,
                  "gap_rejected_minus_accepted": 0.4821861736864097
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.4140024296876802,
              "spearman": 0.3346295266449178,
              "auroc_top30_bad": 0.5971287619047619,
              "mae": 0.6689792558908463,
              "mse": 0.826497579655711,
              "expert_lt_perturb_large": 0.796,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.624,
              "same_context_pred_std": 0.5641264056095238,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.378757661819458
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7589855287790298
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2373879399061203
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.341980816467603
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.09753373002369506,
              "spearman": -0.04266454391330811,
              "auroc_top30_worst": 0.36787504761904766,
              "pairwise_seed_ranking": 0.642,
              "predicted_best_mean_error": 1.7674482172727586,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.039700364112853936,
              "gap_to_oracle": 0.043561417102813804,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.719467511177063
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.8498353438499646
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8917312955856322
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.81508603507776
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8396906852722217,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7484224914974638,
                  "rejected_mean_error": 2.2887934513092043,
                  "gap_rejected_minus_accepted": 0.5403709598117405
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0739287734031677,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.8158510876312581,
                  "rejected_mean_error": 1.7623706557118475,
                  "gap_rejected_minus_accepted": -0.053480431919410654
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5922070741653442,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.8917312955856322,
                  "rejected_mean_error": 1.713187879371643,
                  "gap_rejected_minus_accepted": -0.17854341621398917
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3003041446208954,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.848362529620576,
                  "rejected_mean_error": 1.7871259472540628,
                  "gap_rejected_minus_accepted": -0.06123658236651308
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.749283528327942,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7481933677196502,
                  "rejected_mean_error": 2.3377455043792725,
                  "gap_rejected_minus_accepted": 0.5895521366596224
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0462602376937866,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.8182234832628525,
                  "rejected_mean_error": 1.7742754599404713,
                  "gap_rejected_minus_accepted": -0.043948023322381236
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.590923011302948,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.910309586286545,
                  "rejected_mean_error": 1.7039875764846801,
                  "gap_rejected_minus_accepted": -0.20632200980186477
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2945845127105713,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.8730893291178203,
                  "rejected_mean_error": 1.7849332492619274,
                  "gap_rejected_minus_accepted": -0.08815607985589291
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6589050862968379,
              "spearman": 0.6301313152141081,
              "auroc_top30_bad": 0.8486491428571428,
              "mae": 0.5021068047404289,
              "mse": 0.5166565367424768,
              "expert_lt_perturb_large": 0.86,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.688,
              "same_context_pred_std": 0.5293703222575161,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.31085821080207826
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5365309270858765
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8466516660690308
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0829663542985917
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7392928747271946,
              "spearman": 0.6568039582745334,
              "auroc_top30_worst": 0.8788845714285715,
              "pairwise_seed_ranking": 0.6884,
              "predicted_best_mean_error": 1.5794034556150436,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.039918822646141106,
              "gap_to_oracle": 0.02826019537448876,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7117578852176666
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1027893611253836
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2740143046855927
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3833066320686198
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4567329406738283,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5081977925035688,
                  "rejected_mean_error": 2.6563232135772705,
                  "gap_rejected_minus_accepted": 1.1481254210737017
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1358531713485718,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3824475240618341,
                  "rejected_mean_error": 2.3431616236988346,
                  "gap_rejected_minus_accepted": 0.9607140996370005
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.817696452140808,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2740143046855927,
                  "rejected_mean_error": 1.9720063645362853,
                  "gap_rejected_minus_accepted": 0.6979920598506926
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5335736274719238,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1015234890456398,
                  "rejected_mean_error": 1.7972103161071382,
                  "gap_rejected_minus_accepted": 0.6956868270614984
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5201553821563722,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.503412245379554,
                  "rejected_mean_error": 2.662512574195862,
                  "gap_rejected_minus_accepted": 1.159100328816308
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1820110082626343,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3721319953388071,
                  "rejected_mean_error": 2.353045816459353,
                  "gap_rejected_minus_accepted": 0.9809138211205457
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8130606412887573,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2422232704162597,
                  "rejected_mean_error": 1.9964212861061097,
                  "gap_rejected_minus_accepted": 0.75419801568985
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4877272248268127,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0540287636575245,
                  "rejected_mean_error": 1.8097687564431664,
                  "gap_rejected_minus_accepted": 0.7557399927856419
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_object_bowl/quantile_action_q80/model.pt"
      },
      {
        "variant": "quantile_action_q90",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.9,
        "best_epoch": 41,
        "best_calib_pinball": 0.11781009286642075,
        "train_time_sec": 15.78492546081543,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.7164099224380766,
              "spearman": 0.6288514475091935,
              "auroc_top30_bad": 0.9269227619047619,
              "mae": 0.49542619416564704,
              "mse": 0.6444311570234471,
              "expert_lt_perturb_large": 0.728,
              "expert_lt_other_task": 0.482,
              "expert_lt_simvla_seed0": 0.372,
              "same_context_pred_std": 0.5743570192982604,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4276666956096888
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6361197698891163
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8545755963027477
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0505646139721077
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3045572458028794
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9811311457127657,
              "spearman": 0.9822328497608876,
              "auroc_top30_worst": 0.9880855238095237,
              "pairwise_seed_ranking": 0.7192,
              "predicted_best_mean_error": 1.5542089365720748,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.061399391442537476,
              "gap_to_oracle": 0.025349702388048012,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6796917982697487
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8162575537919998
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0159134204745293
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2483720546007155
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.005524826049805,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4082162316309081,
                  "rejected_mean_error": 3.433841787338257,
                  "gap_rejected_minus_accepted": 2.025625555707349
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1303956508636475,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2483720546007155,
                  "rejected_mean_error": 2.6979989850044253,
                  "gap_rejected_minus_accepted": 1.4496269304037097
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5415259003639221,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0159134204745293,
                  "rejected_mean_error": 2.205644153928757,
                  "gap_rejected_minus_accepted": 1.1897307334542275
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.142345815896988,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8162575537919998,
                  "rejected_mean_error": 1.8756191983381907,
                  "gap_rejected_minus_accepted": 1.0593616445461909
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.977005481719971,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.413677982919746,
                  "rejected_mean_error": 3.432981433868408,
                  "gap_rejected_minus_accepted": 2.0193034509486623
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.117943525314331,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2489972974856693,
                  "rejected_mean_error": 2.7154414196014405,
                  "gap_rejected_minus_accepted": 1.4664441221157711
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5375597476959229,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0096031438708306,
                  "rejected_mean_error": 2.221613512158394,
                  "gap_rejected_minus_accepted": 1.2120103682875634
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1316407322883606,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8057158943414688,
                  "rejected_mean_error": 1.8855724725723266,
                  "gap_rejected_minus_accepted": 1.0798565782308578
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.3995607825694393,
              "spearman": 0.40206570215015225,
              "auroc_top30_bad": 0.7388007619047618,
              "mae": 0.6164332747220993,
              "mse": 0.7843282543614637,
              "expert_lt_perturb_large": 0.7,
              "expert_lt_other_task": 0.472,
              "expert_lt_simvla_seed0": 0.436,
              "same_context_pred_std": 0.4768132303289594,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4915762910246849
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7937540884494781
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1112567925453185
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2322771653254827
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.3500847406361082,
              "spearman": 0.42653303150914024,
              "auroc_top30_worst": 0.6961798095238094,
              "pairwise_seed_ranking": 0.6724,
              "predicted_best_mean_error": 1.4942777037620545,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.034516119956970126,
              "gap_to_oracle": 0.03143468165397656,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9772642707824707
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.218148957269314
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3804470156669617
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4958434007696506
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.29360408782959,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5283999819755554,
                  "rejected_mean_error": 1.6093837790489196,
                  "gap_rejected_minus_accepted": 0.08098379707336423
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0353044271469116,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4950990940870572,
                  "rejected_mean_error": 1.6604316324090804,
                  "gap_rejected_minus_accepted": 0.16533253832202321
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7377046942710876,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3804470156669617,
                  "rejected_mean_error": 1.692549707698822,
                  "gap_rejected_minus_accepted": 0.31210269203186036
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.423195332288742,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.22077150523853,
                  "rejected_mean_error": 1.64196528384627,
                  "gap_rejected_minus_accepted": 0.42119377860774
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2909087419509886,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5174249511294895,
                  "rejected_mean_error": 1.6311136770248413,
                  "gap_rejected_minus_accepted": 0.11368872589535184
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.052492916584015,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4851289095088123,
                  "rejected_mean_error": 1.6584023785969568,
                  "gap_rejected_minus_accepted": 0.17327346908814456
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7185497283935547,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3456220541000365,
                  "rejected_mean_error": 1.7119655933380127,
                  "gap_rejected_minus_accepted": 0.36634353923797613
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3736633360385895,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.259045710639348,
                  "rejected_mean_error": 1.619671530264584,
                  "gap_rejected_minus_accepted": 0.3606258196252361
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.23431006234958246,
              "spearman": 0.14110751189852377,
              "auroc_top30_bad": 0.527096380952381,
              "mae": 0.8462994882047177,
              "mse": 1.1990481309667562,
              "expert_lt_perturb_large": 0.736,
              "expert_lt_other_task": 0.52,
              "expert_lt_simvla_seed0": 0.356,
              "same_context_pred_std": 0.5260727376073794,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6012440562844277
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3451572897434234
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.348409734606743
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3284059346437453
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.019864998453774735,
              "spearman": -0.19302278926258515,
              "auroc_top30_worst": 0.28636952380952385,
              "pairwise_seed_ranking": 0.6316,
              "predicted_best_mean_error": 1.7655315514802932,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.04161702990531935,
              "gap_to_oracle": 0.041644751310348394,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 2.235084596157074
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 2.1452037713084464
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.9142906760215759
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8035096994468145
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9553790807724005,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7466162533230252,
                  "rejected_mean_error": 2.3050495948791503,
                  "gap_rejected_minus_accepted": 0.5584333415561251
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1965577006340027,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.8036395362881485,
                  "rejected_mean_error": 1.798927280659112,
                  "gap_rejected_minus_accepted": -0.004712255629036655
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7561622858047485,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.9142906760215759,
                  "rejected_mean_error": 1.6906284989356994,
                  "gap_rejected_minus_accepted": -0.22366217708587643
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2957205176353455,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 2.1413991719769974,
                  "rejected_mean_error": 1.6892385736600821,
                  "gap_rejected_minus_accepted": -0.45216059831691524
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8847030162811276,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7481933677196502,
                  "rejected_mean_error": 2.3377455043792725,
                  "gap_rejected_minus_accepted": 0.5895521366596224
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1739779114723206,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.8134647536086526,
                  "rejected_mean_error": 1.7884005781203982,
                  "gap_rejected_minus_accepted": -0.025064175488254348
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7642927765846252,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.9186016061306,
                  "rejected_mean_error": 1.695695556640625,
                  "gap_rejected_minus_accepted": -0.22290604948997483
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3011594116687775,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 2.198178985289165,
                  "rejected_mean_error": 1.6754110656320091,
                  "gap_rejected_minus_accepted": -0.5227679196571557
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5056126860299878,
              "spearman": 0.48584509077156984,
              "auroc_top30_bad": 0.825824,
              "mae": 0.6859856289148331,
              "mse": 0.862746327094884,
              "expert_lt_perturb_large": 0.76,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.44,
              "same_context_pred_std": 0.4686119321536185,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4146787526607513
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7516196300029755
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9842965986251832
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0870815097332
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6285580357081494,
              "spearman": 0.5675534476502065,
              "auroc_top30_worst": 0.8433462857142856,
              "pairwise_seed_ranking": 0.6984,
              "predicted_best_mean_error": 1.5772014104127885,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.04212086784839619,
              "gap_to_oracle": 0.026058150172233674,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9371971800327301
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1554739527786388
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2918053179264068
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4126271105714951
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.542245697975159,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.540853247669008,
                  "rejected_mean_error": 2.362424117088318,
                  "gap_rejected_minus_accepted": 0.82157086941931
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.308589220046997,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4116909208458033,
                  "rejected_mean_error": 2.25561829211232,
                  "gap_rejected_minus_accepted": 0.8439273712665165
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8795108795166016,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2918053179264068,
                  "rejected_mean_error": 1.9542153512954712,
                  "gap_rejected_minus_accepted": 0.6624100333690643
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6290886402130127,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.153784394169006,
                  "rejected_mean_error": 1.7797528312580309,
                  "gap_rejected_minus_accepted": 0.6259684370890248
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5337377309799196,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5334113126330906,
                  "rejected_mean_error": 2.392520968914032,
                  "gap_rejected_minus_accepted": 0.8591096562809413
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3646597862243652,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3987370723071584,
                  "rejected_mean_error": 2.2740751911723422,
                  "gap_rejected_minus_accepted": 0.8753381188651839
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8901974558830261,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2656932115554809,
                  "rejected_mean_error": 1.9729513449668885,
                  "gap_rejected_minus_accepted": 0.7072581334114076
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.576093703508377,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0901278011382571,
                  "rejected_mean_error": 1.797607048628802,
                  "gap_rejected_minus_accepted": 0.7074792474905449
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_object_bowl/quantile_action_q90/model.pt"
      },
      {
        "variant": "quantile_action_q95",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.95,
        "best_epoch": 1,
        "best_calib_pinball": 0.07004319876432419,
        "train_time_sec": 15.98409104347229,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.585713268084588,
              "spearman": 0.4845851061528583,
              "auroc_top30_bad": 0.8089215,
              "mae": 0.9288038082480431,
              "mse": 1.3442105374319349,
              "expert_lt_perturb_large": 0.774,
              "expert_lt_other_task": 0.515,
              "expert_lt_simvla_seed0": 0.608,
              "same_context_pred_std": 0.4705612078132208,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7162221917808056
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7879139416515827
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9506892912834882
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0944542651434739
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3045572458028794
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.7895577751584393,
              "spearman": 0.6182520031597561,
              "auroc_top30_worst": 0.8757494285714286,
              "pairwise_seed_ranking": 0.603,
              "predicted_best_mean_error": 1.5853270962834358,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.030281231731176472,
              "gap_to_oracle": 0.056467862099409016,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9696973255872726
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0890601194381715
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2246610861539842
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3122782675584157
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.487214326858521,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4151182977557182,
                  "rejected_mean_error": 3.371723192214966,
                  "gap_rejected_minus_accepted": 1.9566048944592478
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6159512996673584,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3122782675584157,
                  "rejected_mean_error": 2.5062803461313248,
                  "gap_rejected_minus_accepted": 1.194002078572909
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0682045221328735,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.2246610861539842,
                  "rejected_mean_error": 1.9968964882493019,
                  "gap_rejected_minus_accepted": 0.7722354020953177
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6876168251037598,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 1.0890601194381715,
                  "rejected_mean_error": 1.7846850097894669,
                  "gap_rejected_minus_accepted": 0.6956248903512954
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.507035875320435,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4179570663306449,
                  "rejected_mean_error": 3.3944696831703185,
                  "gap_rejected_minus_accepted": 1.9765126168396736
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6251445412635803,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3114303928613662,
                  "rejected_mean_error": 2.52814213347435,
                  "gap_rejected_minus_accepted": 1.216711740612984
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0617048740386963,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.2304566526412963,
                  "rejected_mean_error": 2.000760003387928,
                  "gap_rejected_minus_accepted": 0.7703033507466315
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6940631568431854,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.075555944442749,
                  "rejected_mean_error": 1.7956257892052332,
                  "gap_rejected_minus_accepted": 0.7200698447624843
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.3563332129799205,
              "spearman": 0.39948052729483874,
              "auroc_top30_bad": 0.7495748571428571,
              "mae": 0.94015163539052,
              "mse": 1.3790957733448894,
              "expert_lt_perturb_large": 0.74,
              "expert_lt_other_task": 0.512,
              "expert_lt_simvla_seed0": 0.608,
              "same_context_pred_std": 0.4252738473014283,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8422930905818939
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8984981489658356
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0572283804059028
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.233541052254041
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.34651840436366177,
              "spearman": 0.3971698966847339,
              "auroc_top30_worst": 0.7837500952380954,
              "pairwise_seed_ranking": 0.61,
              "predicted_best_mean_error": 1.512839721918106,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.015954101800918608,
              "gap_to_oracle": 0.04999669981002808,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.273604730129242
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3142422466323926
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.379450425720215
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4751048593887135
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9149626970291145,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5216025888125102,
                  "rejected_mean_error": 1.6705603175163268,
                  "gap_rejected_minus_accepted": 0.14895772870381663
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.537384331226349,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4739935614383335,
                  "rejected_mean_error": 1.7236133707217134,
                  "gap_rejected_minus_accepted": 0.2496198092833799
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.1512757539749146,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.379450425720215,
                  "rejected_mean_error": 1.6935462976455689,
                  "gap_rejected_minus_accepted": 0.31409587192535393
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.8274790942668915,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3147797194151833,
                  "rejected_mean_error": 1.6105623264959044,
                  "gap_rejected_minus_accepted": 0.295782607080721
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9273919343948362,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5138508462905884,
                  "rejected_mean_error": 1.663280620574951,
                  "gap_rejected_minus_accepted": 0.14942977428436266
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.52103990316391,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4659870311538166,
                  "rejected_mean_error": 1.7152203349840074,
                  "gap_rejected_minus_accepted": 0.24923330383019082
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.1193774938583374,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3567575206756592,
                  "rejected_mean_error": 1.7008301267623902,
                  "gap_rejected_minus_accepted": 0.34407260608673096
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.8376455307006836,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2974942563072083,
                  "rejected_mean_error": 1.606718276911241,
                  "gap_rejected_minus_accepted": 0.30922402060403265
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.3324351787513081,
              "spearman": 0.32821046438494955,
              "auroc_top30_bad": 0.6399779047619047,
              "mae": 1.1111040188848973,
              "mse": 1.9294452380299538,
              "expert_lt_perturb_large": 0.676,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 0.62,
              "same_context_pred_std": 0.4699747191255769,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.675901987850666
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9685188187837601
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1039948984265326
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3236693746089936
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.19134691741087687,
              "spearman": 0.12057803403394178,
              "auroc_top30_worst": 0.5710171428571429,
              "pairwise_seed_ranking": 0.6164,
              "predicted_best_mean_error": 1.7776615258455277,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.029487055540084794,
              "gap_to_oracle": 0.053774725675582946,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.5936086587905884
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.5687678020734053
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6377859402656556
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7943959547512567
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5976106882095342,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7614431461228264,
                  "rejected_mean_error": 2.1716075596809388,
                  "gap_rejected_minus_accepted": 0.4101644135581124
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.9699990153312683,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.793363772054365,
                  "rejected_mean_error": 1.829688913525103,
                  "gap_rejected_minus_accepted": 0.036325141470738176
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.588784098625183,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.6377859402656556,
                  "rejected_mean_error": 1.96713323469162,
                  "gap_rejected_minus_accepted": 0.32934729442596433
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.0824902057647705,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.5665550595655229,
                  "rejected_mean_error": 1.881262273964022,
                  "gap_rejected_minus_accepted": 0.314707214398499
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5848963022232057,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.764177964925766,
                  "rejected_mean_error": 2.193884129524231,
                  "gap_rejected_minus_accepted": 0.429706164598465
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.9898011088371277,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7915965151340567,
                  "rejected_mean_error": 1.853311063751342,
                  "gap_rejected_minus_accepted": 0.0617145486172852
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.587276577949524,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6406447818279266,
                  "rejected_mean_error": 1.9736523809432984,
                  "gap_rejected_minus_accepted": 0.3330075991153718
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.088138461112976,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.558860028546954,
                  "rejected_mean_error": 1.890796596513075,
                  "gap_rejected_minus_accepted": 0.33193656796612103
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.4464501240294588,
              "spearman": 0.4046535570535735,
              "auroc_top30_bad": 0.721542857142857,
              "mae": 1.088263259267807,
              "mse": 1.700327097918273,
              "expert_lt_perturb_large": 0.68,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.672,
              "same_context_pred_std": 0.4070522569388909,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7270978941321373
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8780685193061829
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0191573710799218
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1241763550122579
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.46544131916174375,
              "spearman": 0.3729289687865401,
              "auroc_top30_worst": 0.7484739047619049,
              "pairwise_seed_ranking": 0.6644,
              "predicted_best_mean_error": 1.5971665494441987,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.02215572881698602,
              "gap_to_oracle": 0.04602328920364385,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3659676189422607
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3570032270672994
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.431869202041626
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.454796613247664
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.4270123481750487,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5201401767995621,
                  "rejected_mean_error": 2.54884175491333,
                  "gap_rejected_minus_accepted": 1.0287015781137678
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.834043800830841,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4557541249719474,
                  "rejected_mean_error": 2.1237102337538625,
                  "gap_rejected_minus_accepted": 0.667956108781915
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.4070634841918945,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.431869202041626,
                  "rejected_mean_error": 1.814151467180252,
                  "gap_rejected_minus_accepted": 0.3822822651386262
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.0751055479049683,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3565642264323494,
                  "rejected_mean_error": 1.7120152778979172,
                  "gap_rejected_minus_accepted": 0.35545105146556777
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.479126715660095,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5037857333819071,
                  "rejected_mean_error": 2.6591511821746825,
                  "gap_rejected_minus_accepted": 1.1553654487927754
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.826883018016815,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.446038660518626,
                  "rejected_mean_error": 2.133672064258939,
                  "gap_rejected_minus_accepted": 0.6876334037403129
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.3933931589126587,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.37556156539917,
                  "rejected_mean_error": 1.8630829911231994,
                  "gap_rejected_minus_accepted": 0.48752142572402946
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.0878771543502808,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3822239377195873,
                  "rejected_mean_error": 1.6992003288179796,
                  "gap_rejected_minus_accepted": 0.31697639109839226
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_object_bowl/quantile_action_q95/model.pt"
      },
      {
        "variant": "quantile_context_gated_q80",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.8,
        "best_epoch": 114,
        "best_calib_pinball": 0.0284222774207592,
        "train_time_sec": 50.838393211364746,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9990662849967797,
              "spearman": 0.9983956587557022,
              "auroc_top30_bad": 0.9992593333333333,
              "mae": 0.04241270707184449,
              "mse": 0.0030065953040123994,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.750818530928183,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0007367839068174362
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1979503117322922
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5741754744291305
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9269387103239696
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3045572458028794
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9988604293172381,
              "spearman": 0.9985556834942272,
              "auroc_top30_worst": 0.9992190476190477,
              "pairwise_seed_ranking": 0.9346,
              "predicted_best_mean_error": 1.5326320721805096,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.08297625583410273,
              "gap_to_oracle": 0.0037728379964827585,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6668831216692924
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8077137791872024
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.010323227441311
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2416591424862544
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.754097056388856,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4058029205203055,
                  "rejected_mean_error": 3.4555615873336794,
                  "gap_rejected_minus_accepted": 2.049758666813374
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.008880615234375,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2416591424862544,
                  "rejected_mean_error": 2.7181377213478086,
                  "gap_rejected_minus_accepted": 1.4764785788615542
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.467739760875702,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.010323227441311,
                  "rejected_mean_error": 2.2112343469619753,
                  "gap_rejected_minus_accepted": 1.2009111195206643
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0775246322154999,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8077137791872024,
                  "rejected_mean_error": 1.8784671232064565,
                  "gap_rejected_minus_accepted": 1.070753344019254
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.795439338684082,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4106576990087827,
                  "rejected_mean_error": 3.4601639890670777,
                  "gap_rejected_minus_accepted": 2.0495062900582948
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0164055228233337,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2434318140745162,
                  "rejected_mean_error": 2.7321378698349,
                  "gap_rejected_minus_accepted": 1.4887060557603837
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4807636141777039,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0041112650036812,
                  "rejected_mean_error": 2.2271053910255434,
                  "gap_rejected_minus_accepted": 1.2229941260218622
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0729367434978485,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.799189583659172,
                  "rejected_mean_error": 1.8877479094664256,
                  "gap_rejected_minus_accepted": 1.0885583258072535
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9879545254265543,
              "spearman": 0.984670002355145,
              "auroc_top30_bad": 0.9867885714285715,
              "mae": 0.09480762975234538,
              "mse": 0.018181546621654446,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7115126115845023,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04500319147109985
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22856230947971343
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6798819406867027
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0351129267613093
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9768847760500606,
              "spearman": 0.9758635570326766,
              "auroc_top30_worst": 0.9833478095238095,
              "pairwise_seed_ranking": 0.8768,
              "predicted_best_mean_error": 1.4691476705074311,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.0596461532115935,
              "gap_to_oracle": 0.0063046483993531854,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8739586734771728
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9796591156568283
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1694189149856566
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3607556929212135
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1273902654647836,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4593796022203234,
                  "rejected_mean_error": 2.230567196846008,
                  "gap_rejected_minus_accepted": 0.7711875946256848
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.969803273677826,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3601700271079227,
                  "rejected_mean_error": 2.064356666784317,
                  "gap_rejected_minus_accepted": 0.7041866396763945
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5739163160324097,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1694189149856566,
                  "rejected_mean_error": 1.903577808380127,
                  "gap_rejected_minus_accepted": 0.7341588933944703
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2390349507331848,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9806548292263628,
                  "rejected_mean_error": 1.7221750166016683,
                  "gap_rejected_minus_accepted": 0.7415201873753055
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1272093057632446,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4529997401767307,
                  "rejected_mean_error": 2.2109405755996705,
                  "gap_rejected_minus_accepted": 0.7579408354229398
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9732712507247925,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3515765214348858,
                  "rejected_mean_error": 2.0548197844671825,
                  "gap_rejected_minus_accepted": 0.7032432630322967
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.572096586227417,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1565153045654297,
                  "rejected_mean_error": 1.9010723428726197,
                  "gap_rejected_minus_accepted": 0.74455703830719
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2706335484981537,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.964195416087196,
                  "rejected_mean_error": 1.7190061214773413,
                  "gap_rejected_minus_accepted": 0.7548107053901454
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9625198541615806,
              "spearman": 0.9701297368869783,
              "auroc_top30_bad": 0.9806940952380953,
              "mae": 0.16995892594195902,
              "mse": 0.06948597211968205,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7018816200682795,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09157452511787414
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20633184254169465
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6975954596400261
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0550565814892452
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9221187320616954,
              "spearman": 0.9511026252176802,
              "auroc_top30_worst": 0.9640838095238096,
              "pairwise_seed_ranking": 0.8944,
              "predicted_best_mean_error": 1.7271974741220475,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.07995110726356502,
              "gap_to_oracle": 0.003310673952102716,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9412685680389404
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.111651795796859
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3182207054138184
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4687070190779437
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.23726007938385,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6627822214762369,
                  "rejected_mean_error": 3.059555881500244,
                  "gap_rejected_minus_accepted": 1.396773660024007
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9641703069210052,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4681824154380545,
                  "rejected_mean_error": 2.803155147229521,
                  "gap_rejected_minus_accepted": 1.3349727317914664
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6641273498535156,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3182207054138184,
                  "rejected_mean_error": 2.286698469543457,
                  "gap_rejected_minus_accepted": 0.9684777641296385
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4292573928833008,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1128111651149422,
                  "rejected_mean_error": 2.0328330732842264,
                  "gap_rejected_minus_accepted": 0.9200219081692842
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2343440532684324,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6688829251130421,
                  "rejected_mean_error": 3.051539487838745,
                  "gap_rejected_minus_accepted": 1.3826565627257028
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0056551694869995,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4704654266171278,
                  "rejected_mean_error": 2.8065096915714323,
                  "gap_rejected_minus_accepted": 1.3360442649543045
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6693271398544312,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3171636130809783,
                  "rejected_mean_error": 2.2971335496902467,
                  "gap_rejected_minus_accepted": 0.9799699366092685
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4287736117839813,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1087549825509389,
                  "rejected_mean_error": 2.0424362644154757,
                  "gap_rejected_minus_accepted": 0.9336812818645368
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9905406393278275,
              "spearman": 0.9897855943444096,
              "auroc_top30_bad": 0.9966491428571428,
              "mae": 0.10005981634818018,
              "mse": 0.01885351313247469,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7338238806639212,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04194839304685593
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19784453921318054
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.590265345287323
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9330034182230631
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9832168708807975,
              "spearman": 0.9820872179758195,
              "auroc_top30_worst": 0.9969950476190476,
              "pairwise_seed_ranking": 0.9156,
              "predicted_best_mean_error": 1.5540343220233916,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06528795623779304,
              "gap_to_oracle": 0.0028910617828368235,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5703311417102813
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8735821217489548
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1170295708179474
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.311734070052216
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6716965436935447,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4774259408579933,
                  "rejected_mean_error": 2.9332698783874513,
                  "gap_rejected_minus_accepted": 1.455843937529458
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0811867117881775,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3110743005667578,
                  "rejected_mean_error": 2.556825235247993,
                  "gap_rejected_minus_accepted": 1.2457509346812352
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6011581420898438,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1170295708179474,
                  "rejected_mean_error": 2.128991098403931,
                  "gap_rejected_minus_accepted": 1.0119615275859835
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3078492879867554,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8747586995458451,
                  "rejected_mean_error": 1.8729599202836973,
                  "gap_rejected_minus_accepted": 0.9982012207378522
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6618089437484738,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4691338721911114,
                  "rejected_mean_error": 2.971017932891846,
                  "gap_rejected_minus_accepted": 1.5018840607007344
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.106657862663269,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2984497531212587,
                  "rejected_mean_error": 2.5717534243114413,
                  "gap_rejected_minus_accepted": 1.2733036711901826
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.610473096370697,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1043508524894714,
                  "rejected_mean_error": 2.1342937040328978,
                  "gap_rejected_minus_accepted": 1.0299428515434264
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3003322780132294,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8537329596186441,
                  "rejected_mean_error": 1.8772480914936984,
                  "gap_rejected_minus_accepted": 1.0235151318750542
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_object_bowl/quantile_context_gated_q80/model.pt"
      },
      {
        "variant": "quantile_context_gated_q90",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.9,
        "best_epoch": 110,
        "best_calib_pinball": 0.017772672697901726,
        "train_time_sec": 50.765456199645996,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9981144842199394,
              "spearman": 0.996954878321526,
              "auroc_top30_bad": 0.9989771428571428,
              "mae": 0.09886172311818227,
              "mse": 0.014670238857934573,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7739735484232496,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.007337213203310967
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20021917103528977
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5747505524158478
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9272685518423717
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3045572458028794
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9980979919910395,
              "spearman": 0.9977337019893481,
              "auroc_top30_worst": 0.9994274285714286,
              "pairwise_seed_ranking": 0.9162,
              "predicted_best_mean_error": 1.5346649703383446,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.0809433576762677,
              "gap_to_oracle": 0.0058057361543177866,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6684240545630455
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8084513288259506
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0105364303946496
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2420713245948156
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.94741473197937,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4059085108107992,
                  "rejected_mean_error": 3.4546112747192383,
                  "gap_rejected_minus_accepted": 2.048702763908439
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1067777276039124,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2420713245948156,
                  "rejected_mean_error": 2.7169011750221252,
                  "gap_rejected_minus_accepted": 1.4748298504273096
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5001847743988037,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0105364303946496,
                  "rejected_mean_error": 2.2110211440086367,
                  "gap_rejected_minus_accepted": 1.2004847136139871
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0969308912754059,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8084513288259506,
                  "rejected_mean_error": 1.8782212733268737,
                  "gap_rejected_minus_accepted": 1.0697699445009232
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.983850836753845,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.410788960357507,
                  "rejected_mean_error": 3.4589826369285586,
                  "gap_rejected_minus_accepted": 2.0481936765710516
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1159119606018066,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.244043818195661,
                  "rejected_mean_error": 2.730301857471466,
                  "gap_rejected_minus_accepted": 1.4862580392758051
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5228719115257263,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0040121484398843,
                  "rejected_mean_error": 2.2272045075893403,
                  "gap_rejected_minus_accepted": 1.223192359149456
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0931010842323303,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7997720173597336,
                  "rejected_mean_error": 1.8875537648995717,
                  "gap_rejected_minus_accepted": 1.0877817475398381
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9884484875450776,
              "spearman": 0.9851333375786108,
              "auroc_top30_bad": 0.9864853333333332,
              "mae": 0.12225183559004217,
              "mse": 0.027798767919970317,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7417170351049152,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.023325089752674104
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.232771830534935
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.680177483689785
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0353833185434342
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9745176887233511,
              "spearman": 0.9778720564941163,
              "auroc_top30_worst": 0.984984380952381,
              "pairwise_seed_ranking": 0.8584,
              "predicted_best_mean_error": 1.4708665041923523,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.057927319526672294,
              "gap_to_oracle": 0.008023482084274391,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.876427315235138
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.976901460916568
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.169909031867981
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3601914209597654
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.238924479484558,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.458127631717258,
                  "rejected_mean_error": 2.2418349313735964,
                  "gap_rejected_minus_accepted": 0.7837072996563383
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.038256585597992,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3595070943252254,
                  "rejected_mean_error": 2.0663412291401873,
                  "gap_rejected_minus_accepted": 0.7068341348149618
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.59872967004776,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.169909031867981,
                  "rejected_mean_error": 1.9030876914978028,
                  "gap_rejected_minus_accepted": 0.7331786596298218
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2507181465625763,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.978195886261547,
                  "rejected_mean_error": 1.7229964137713454,
                  "gap_rejected_minus_accepted": 0.7448005275097984
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2336557865142823,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4506876103083293,
                  "rejected_mean_error": 2.2317497444152834,
                  "gap_rejected_minus_accepted": 0.7810621341069541
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.033202290534973,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3516123524324142,
                  "rejected_mean_error": 2.0547134289665827,
                  "gap_rejected_minus_accepted": 0.7031010765341685
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5915912985801697,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1558725728988648,
                  "rejected_mean_error": 1.9017150745391846,
                  "gap_rejected_minus_accepted": 0.7458425016403198
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2732397019863129,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.964195416087196,
                  "rejected_mean_error": 1.7190061214773413,
                  "gap_rejected_minus_accepted": 0.7548107053901454
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9729263279323354,
              "spearman": 0.9729548746573056,
              "auroc_top30_bad": 0.9763786666666668,
              "mae": 0.16732300522308796,
              "mse": 0.05092955164431173,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7458440052587104,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09131161040067673
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20392747390270233
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7023291481852532
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0549441614707311
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9419186700286886,
              "spearman": 0.947342120026957,
              "auroc_top30_worst": 0.9578300952380953,
              "pairwise_seed_ranking": 0.8848,
              "predicted_best_mean_error": 1.728012286543846,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.07913629484176643,
              "gap_to_oracle": 0.00412548637390131,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9450717315673828
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.111553885615789
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3190676195144653
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4704011879495975
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.492235183715821,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.65860556962755,
                  "rejected_mean_error": 3.097145748138428,
                  "gap_rejected_minus_accepted": 1.438540178510878
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0640196800231934,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.469785580385711,
                  "rejected_mean_error": 2.798355896252032,
                  "gap_rejected_minus_accepted": 1.3285703158663211
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.707712709903717,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3190676195144653,
                  "rejected_mean_error": 2.28585155544281,
                  "gap_rejected_minus_accepted": 0.9667839359283448
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4551545679569244,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1122112472217305,
                  "rejected_mean_error": 2.0330334727512227,
                  "gap_rejected_minus_accepted": 0.9208222255294922
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.488503122329712,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6634694998794133,
                  "rejected_mean_error": 3.1002603149414063,
                  "gap_rejected_minus_accepted": 1.436790815061993
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.063270330429077,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4675465189518138,
                  "rejected_mean_error": 2.8151737508319674,
                  "gap_rejected_minus_accepted": 1.3476272318801537
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.708216369152069,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3160881402492524,
                  "rejected_mean_error": 2.2982090225219727,
                  "gap_rejected_minus_accepted": 0.9821208822727203
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.45697620511055,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1115328674278562,
                  "rejected_mean_error": 2.0415003994569423,
                  "gap_rejected_minus_accepted": 0.9299675320290861
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.990558512156503,
              "spearman": 0.9898692397083063,
              "auroc_top30_bad": 0.9958430476190476,
              "mae": 0.13190242210589348,
              "mse": 0.028868244972177264,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7468172781119206,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.034306587874889376
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19819983201026917
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5903445433616639
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9336954988479614
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9818070957465055,
              "spearman": 0.9799311088199099,
              "auroc_top30_worst": 0.9954224761904762,
              "pairwise_seed_ranking": 0.8992,
              "predicted_best_mean_error": 1.5555500044822692,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06377227377891548,
              "gap_to_oracle": 0.004406744241714389,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5715921075344086
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8739132312818979
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1185383970737457
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3129978143393612
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8472390174865723,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4769714614285363,
                  "rejected_mean_error": 2.9373601932525633,
                  "gap_rejected_minus_accepted": 1.460388731824027
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1754552125930786,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3120738433608379,
                  "rejected_mean_error": 2.553832993720667,
                  "gap_rejected_minus_accepted": 1.241759150359829
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6411168575286865,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1185383970737457,
                  "rejected_mean_error": 2.127482272148132,
                  "gap_rejected_minus_accepted": 1.0089438750743864
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3137153089046478,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8748994914297098,
                  "rejected_mean_error": 1.8729128894836442,
                  "gap_rejected_minus_accepted": 0.9980133980539344
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.847903609275818,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4691338721911114,
                  "rejected_mean_error": 2.971017932891846,
                  "gap_rejected_minus_accepted": 1.5018840607007344
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.198218584060669,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2984497531212587,
                  "rejected_mean_error": 2.5717534243114413,
                  "gap_rejected_minus_accepted": 1.2733036711901826
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6774048209190369,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1058556399345398,
                  "rejected_mean_error": 2.1327889165878298,
                  "gap_rejected_minus_accepted": 1.02693327665329
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2982219457626343,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8530538072661747,
                  "rejected_mean_error": 1.877476896831696,
                  "gap_rejected_minus_accepted": 1.0244230895655213
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_object_bowl/quantile_context_gated_q90/model.pt"
      },
      {
        "variant": "quantile_context_gated_q95",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.95,
        "best_epoch": 70,
        "best_calib_pinball": 0.0138399014249444,
        "train_time_sec": 50.74078297615051,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9966298524017823,
              "spearman": 0.9954585931644793,
              "auroc_top30_bad": 0.9964627142857142,
              "mae": 0.14701388127747922,
              "mse": 0.029087095831278168,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7806205113188552,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.00936650700867176
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19917860077619554
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5755575271368026
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9287325032393138
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3045572458028794
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9955353879148992,
              "spearman": 0.9939323047568555,
              "auroc_top30_worst": 0.9969085714285714,
              "pairwise_seed_ranking": 0.8855,
              "predicted_best_mean_error": 1.537629079401493,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.07797924861311922,
              "gap_to_oracle": 0.008769845217466266,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6697685462832451
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.810173500752449
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0121117475867272
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2434689668893815
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.974824118614197,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4063664822247293,
                  "rejected_mean_error": 3.450489531993866,
                  "gap_rejected_minus_accepted": 2.0441230497691367
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1297702193260193,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2434689668893815,
                  "rejected_mean_error": 2.7127082481384277,
                  "gap_rejected_minus_accepted": 1.4692392812490462
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5818922519683838,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0121117475867272,
                  "rejected_mean_error": 2.209445826816559,
                  "gap_rejected_minus_accepted": 1.1973340792298317
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1632323265075684,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.810173500752449,
                  "rejected_mean_error": 1.877647216018041,
                  "gap_rejected_minus_accepted": 1.0674737152655922
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.0038867473602298,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4110848152968618,
                  "rejected_mean_error": 3.4563199424743654,
                  "gap_rejected_minus_accepted": 2.0452351271775036
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1446723341941833,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2456607453425725,
                  "rejected_mean_error": 2.725451076030731,
                  "gap_rejected_minus_accepted": 1.4797903306881586
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5988974571228027,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.005356157720089,
                  "rejected_mean_error": 2.2258604983091352,
                  "gap_rejected_minus_accepted": 1.2205043405890463
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1639914512634277,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8005485461950302,
                  "rejected_mean_error": 1.8872949219544728,
                  "gap_rejected_minus_accepted": 1.0867463757594424
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9852815855297197,
              "spearman": 0.9799314177964868,
              "auroc_top30_bad": 0.983479619047619,
              "mae": 0.16840081005617977,
              "mse": 0.04273996806399505,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7329597162464365,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06757763767242432
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2334606486082077
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6810717711806298
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0361300143162409
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.96990210110094,
              "spearman": 0.9696102389825532,
              "auroc_top30_worst": 0.9798857142857142,
              "pairwise_seed_ranking": 0.8536,
              "predicted_best_mean_error": 1.4689935252666473,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.05980029845237733,
              "gap_to_oracle": 0.006150503158569354,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8809016265869141
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9793336108708993
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1729058643341064
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.361129772815623
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2366470813751222,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4597816364500258,
                  "rejected_mean_error": 2.2269488887786864,
                  "gap_rejected_minus_accepted": 0.7671672523286606
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.028345823287964,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3605590063836048,
                  "rejected_mean_error": 2.06319221444785,
                  "gap_rejected_minus_accepted": 0.7026332080642452
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6829447746276855,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1729058643341064,
                  "rejected_mean_error": 1.9000908590316772,
                  "gap_rejected_minus_accepted": 0.7271849946975708
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3541161715984344,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9805863966195347,
                  "rejected_mean_error": 1.7221978761597656,
                  "gap_rejected_minus_accepted": 0.7416114795402309
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.259258008003235,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4552287917666966,
                  "rejected_mean_error": 2.190879111289978,
                  "gap_rejected_minus_accepted": 0.7356503195232813
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0501925945281982,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3516858070291937,
                  "rejected_mean_error": 2.054495397068205,
                  "gap_rejected_minus_accepted": 0.7028095900390114
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.692899465560913,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1588027830123901,
                  "rejected_mean_error": 1.898784864425659,
                  "gap_rejected_minus_accepted": 0.7399820814132689
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.335138350725174,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9559735854466757,
                  "rejected_mean_error": 1.72177604303003,
                  "gap_rejected_minus_accepted": 0.7658024575833543
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9466406340379956,
              "spearman": 0.9445418423217739,
              "auroc_top30_bad": 0.9550453333333333,
              "mae": 0.22550052556023,
              "mse": 0.09133257906509436,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7425241420658051,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06793309360742569
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2018715707540512
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.713429052722454
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.095213935716947
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8555254233447139,
              "spearman": 0.8951060197798528,
              "auroc_top30_worst": 0.9109790476190477,
              "pairwise_seed_ranking": 0.874,
              "predicted_best_mean_error": 1.7308546265363693,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.07629395484924317,
              "gap_to_oracle": 0.006967826366424568,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9426107444763183
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1328400350533998
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3395260427474975
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5328082235128895
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.23208270072937,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6683252979914347,
                  "rejected_mean_error": 3.0096681928634643,
                  "gap_rejected_minus_accepted": 1.3413428948720296
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9820261597633362,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5323971820361078,
                  "rejected_mean_error": 2.610921165432793,
                  "gap_rejected_minus_accepted": 1.0785239833966853
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.75471693277359,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3395260427474975,
                  "rejected_mean_error": 2.265393132209778,
                  "gap_rejected_minus_accepted": 0.9258670894622802
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.517440527677536,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1336116931689815,
                  "rejected_mean_error": 2.0258847645532616,
                  "gap_rejected_minus_accepted": 0.8922730713842801
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2354604721069333,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6701761032475366,
                  "rejected_mean_error": 3.0399008846282958,
                  "gap_rejected_minus_accepted": 1.3697247813807591
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9927457869052887,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5325811832027638,
                  "rejected_mean_error": 2.62213435059502,
                  "gap_rejected_minus_accepted": 1.0895531673922563
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7732431888580322,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3451480996608733,
                  "rejected_mean_error": 2.2691490631103517,
                  "gap_rejected_minus_accepted": 0.9240009634494784
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5318441689014435,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1218024619988032,
                  "rejected_mean_error": 2.0380405895212754,
                  "gap_rejected_minus_accepted": 0.9162381275224722
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9862794792002294,
              "spearman": 0.9864539410314901,
              "auroc_top30_bad": 0.9926521904761905,
              "mae": 0.19100366719067097,
              "mse": 0.05609259762397689,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.772549324184585,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.03863777166604996
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19956949677467345
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5918625195503235
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9354545928319296
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9713102711227247,
              "spearman": 0.9718705504451524,
              "auroc_top30_worst": 0.9911375238095238,
              "pairwise_seed_ranking": 0.8756,
              "predicted_best_mean_error": 1.5575633578300476,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.061758920431137065,
              "gap_to_oracle": 0.006420097589492801,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5718779261112213
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8790728450776675
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1207754593372345
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.314974549133132
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.992542600631717,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4771300409369998,
                  "rejected_mean_error": 2.9359329776763916,
                  "gap_rejected_minus_accepted": 1.4588029367393918
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1962578892707825,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3140263103560934,
                  "rejected_mean_error": 2.547988068562346,
                  "gap_rejected_minus_accepted": 1.2339617582062528
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7226195931434631,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1207754593372345,
                  "rejected_mean_error": 2.1252452098846435,
                  "gap_rejected_minus_accepted": 1.004469750547409
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.39706951379776,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8802880270602985,
                  "rejected_mean_error": 1.8711128770478125,
                  "gap_rejected_minus_accepted": 0.990824849987514
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.989007520675659,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4691338721911114,
                  "rejected_mean_error": 2.971017932891846,
                  "gap_rejected_minus_accepted": 1.5018840607007344
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.216787815093994,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3010100664939472,
                  "rejected_mean_error": 2.5641537639829846,
                  "gap_rejected_minus_accepted": 1.2631436974890373
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7577377557754517,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1087180037498474,
                  "rejected_mean_error": 2.129926552772522,
                  "gap_rejected_minus_accepted": 1.0212085490226748
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4001711308956146,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8605828332522559,
                  "rejected_mean_error": 1.8749403800556366,
                  "gap_rejected_minus_accepted": 1.0143575468033807
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_object_bowl/quantile_context_gated_q95/model.pt"
      },
      {
        "variant": "quantile_seed_relative_q90",
        "feature_mode": "M4_seed_relative",
        "kind": "mlp_big",
        "q": 0.9,
        "best_epoch": 68,
        "best_calib_pinball": 0.026347290724515915,
        "train_time_sec": 54.42364001274109,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9974573626064385,
              "spearman": 0.9957942897100037,
              "auroc_top30_bad": 0.9980135714285714,
              "mae": 0.14012430052036143,
              "mse": 0.028326662764492635,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8044670478686762,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.015081188946962356
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19893987830877305
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5758581949114799
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9279690161069234
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3045572458028794
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9971476058636046,
              "spearman": 0.9949481029019239,
              "auroc_top30_worst": 0.9979251428571428,
              "pairwise_seed_ranking": 0.927,
              "predicted_best_mean_error": 1.534032225370407,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.08157610264420523,
              "gap_to_oracle": 0.00517299118638026,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6710321279168129
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8092564616441726
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0121164599061012
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2425406416495641
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.0111147880554205,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4060479892823432,
                  "rejected_mean_error": 3.453355968475342,
                  "gap_rejected_minus_accepted": 2.0473079791929987
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1421674489974976,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2425406416495641,
                  "rejected_mean_error": 2.7154932238578797,
                  "gap_rejected_minus_accepted": 1.4729525822083156
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5345937609672546,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0121164599061012,
                  "rejected_mean_error": 2.2094411144971846,
                  "gap_rejected_minus_accepted": 1.1973246545910834
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1433655619621277,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8092564616441726,
                  "rejected_mean_error": 1.8779528957207998,
                  "gap_rejected_minus_accepted": 1.0686964340766272
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.030288052558899,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4110554723276032,
                  "rejected_mean_error": 3.456584029197693,
                  "gap_rejected_minus_accepted": 2.0455285568700896
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1514878273010254,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2446383257309597,
                  "rejected_mean_error": 2.72851833486557,
                  "gap_rejected_minus_accepted": 1.4838800091346105
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5403099656105042,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.004949795305729,
                  "rejected_mean_error": 2.2262668607234954,
                  "gap_rejected_minus_accepted": 1.2213170654177665
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.139428287744522,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.800776583313942,
                  "rejected_mean_error": 1.8872189095815022,
                  "gap_rejected_minus_accepted": 1.0864423262675602
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9768284840613782,
              "spearman": 0.9760461362195161,
              "auroc_top30_bad": 0.9812876190476191,
              "mae": 0.15779616175215924,
              "mse": 0.04546484486456806,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7240779906559467,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07738740980625153
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24284476723670959
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6853168756842614
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.036853212316831
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3217480289638042
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9615351164827888,
              "spearman": 0.9623900820416527,
              "auroc_top30_worst": 0.9743847619047619,
              "pairwise_seed_ranking": 0.8744,
              "predicted_best_mean_error": 1.4701740815639497,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.05861974215507493,
              "gap_to_oracle": 0.007331059455871758,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8852212657928467
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.980673108345423
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1779323755264282
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3645311266120308
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.213060164451599,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4594884796142578,
                  "rejected_mean_error": 2.229587300300598,
                  "gap_rejected_minus_accepted": 0.7700988206863404
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.016620397567749,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.364019280691157,
                  "rejected_mean_error": 2.0528335019041557,
                  "gap_rejected_minus_accepted": 0.6888142212129986
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6592766046524048,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1779323755264282,
                  "rejected_mean_error": 1.8950643478393554,
                  "gap_rejected_minus_accepted": 0.7171319723129272
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2420211732387543,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9819575098756784,
                  "rejected_mean_error": 1.7217398628735618,
                  "gap_rejected_minus_accepted": 0.7397823529978834
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2465452909469605,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4514245404137505,
                  "rejected_mean_error": 2.2251173734664915,
                  "gap_rejected_minus_accepted": 0.7736928330527411
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0182043313980103,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3551779316070882,
                  "rejected_mean_error": 2.0441298844322326,
                  "gap_rejected_minus_accepted": 0.6889519528251444
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6515694856643677,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1669247074127198,
                  "rejected_mean_error": 1.8906629400253296,
                  "gap_rejected_minus_accepted": 0.7237382326126098
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2527536153793335,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9590352943965367,
                  "rejected_mean_error": 1.7207445581966543,
                  "gap_rejected_minus_accepted": 0.7617092638001176
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9468070178084644,
              "spearman": 0.9528724480115457,
              "auroc_top30_bad": 0.9748914285714285,
              "mae": 0.20793748222392314,
              "mse": 0.09085405590381188,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7190126213261728,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10354851818084716
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.203242426943779
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6976612312197685
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0923429346640905
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4179270033299922
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8752248039126773,
              "spearman": 0.9331154530271554,
              "auroc_top30_worst": 0.9567542857142857,
              "pairwise_seed_ranking": 0.92,
              "predicted_best_mean_error": 1.7263538159132004,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08079476547241216,
              "gap_to_oracle": 0.002467015743255585,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9409515128135681
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.119944230868266
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2929242195129393
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5227044508147087
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.150284004211426,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6705663702223037,
                  "rejected_mean_error": 2.9894985427856446,
                  "gap_rejected_minus_accepted": 1.318932172563341
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9750017523765564,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5222907472191143,
                  "rejected_mean_error": 2.641175892025518,
                  "gap_rejected_minus_accepted": 1.1188851448064037
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7031015753746033,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2929242195129393,
                  "rejected_mean_error": 2.311994955444336,
                  "gap_rejected_minus_accepted": 1.0190707359313966
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4383811950683594,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1208401457570232,
                  "rejected_mean_error": 2.030151033859497,
                  "gap_rejected_minus_accepted": 0.9093108881024738
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.139451026916504,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6874693911605412,
                  "rejected_mean_error": 2.884261293411255,
                  "gap_rejected_minus_accepted": 1.1967919022507136
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9705196917057037,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5267056473754943,
                  "rejected_mean_error": 2.639574433129931,
                  "gap_rejected_minus_accepted": 1.1128687857544368
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7112883925437927,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2856412332057954,
                  "rejected_mean_error": 2.32865592956543,
                  "gap_rejected_minus_accepted": 1.0430146963596345
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4568907022476196,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1248194428663405,
                  "rejected_mean_error": 2.0370241735070787,
                  "gap_rejected_minus_accepted": 0.9122047306407381
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9895940458509774,
              "spearman": 0.988118942443098,
              "auroc_top30_bad": 0.9959222857142856,
              "mae": 0.11958208417293936,
              "mse": 0.02587558417518526,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7632710733387885,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.043102190434932706
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20132710223197936
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5918051575660705
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9342989300409953
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.287394424533844
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9831034551452889,
              "spearman": 0.9739528516818252,
              "auroc_top30_worst": 0.9953371428571428,
              "pairwise_seed_ranking": 0.8972,
              "predicted_best_mean_error": 1.5547214360237123,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06460084223747242,
              "gap_to_oracle": 0.0035781757831574446,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5709802296161651
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8867881982945479
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1214475655078888
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.312063440998226
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.799980878829956,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.477092453877131,
                  "rejected_mean_error": 2.93627126121521,
                  "gap_rejected_minus_accepted": 1.459178807338079
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.10185045003891,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3111843748878897,
                  "rejected_mean_error": 2.5564957156348913,
                  "gap_rejected_minus_accepted": 1.2453113407470016
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5762004256248474,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1214475655078888,
                  "rejected_mean_error": 2.124573103713989,
                  "gap_rejected_minus_accepted": 1.0031255382061004
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.361835777759552,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8880852499899392,
                  "rejected_mean_error": 1.8685082550873242,
                  "gap_rejected_minus_accepted": 0.980423005097385
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.806402850151062,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4684279624621073,
                  "rejected_mean_error": 2.9773711204528808,
                  "gap_rejected_minus_accepted": 1.5089431579907735
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.131089746952057,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3016395552910585,
                  "rejected_mean_error": 2.5622852813629877,
                  "gap_rejected_minus_accepted": 1.2606457260719293
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.584930658340454,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1110288186073303,
                  "rejected_mean_error": 2.127615737915039,
                  "gap_rejected_minus_accepted": 1.0165869193077086
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3739482164382935,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8679678090034969,
                  "rejected_mean_error": 1.8724523935725983,
                  "gap_rejected_minus_accepted": 1.0044845845691013
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_object_bowl/quantile_seed_relative_q90/model.pt"
      }
    ],
    "holdout_libero_spatial": [
      {
        "variant": "quantile_action_q80",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.8,
        "best_epoch": 52,
        "best_calib_pinball": 0.10629106312990189,
        "train_time_sec": 16.104133367538452,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9693784440942462,
              "spearman": 0.9270900270071161,
              "auroc_top30_bad": 0.9971804285714286,
              "mae": 0.1738243717007339,
              "mse": 0.08745610233356417,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.491,
              "expert_lt_simvla_seed0": 0.922,
              "same_context_pred_std": 0.7269451841725958,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2589837273210287
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3399278649866581
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.493206089822948
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8245120535681645
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
              "pearson": 0.9974628510083616,
              "spearman": 0.9960984798759391,
              "auroc_top30_worst": 0.9980784761904762,
              "pairwise_seed_ranking": 0.7633,
              "predicted_best_mean_error": 1.7932289143800735,
              "seed0_mean_error": 1.850025711297989,
              "random_seed_mean_error": 1.841148916900158,
              "oracle_best_mean_error": 1.7736391132473945,
              "improvement_over_seed0": 0.056796796917915504,
              "gap_to_oracle": 0.01958980113267894,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6068896517157555
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8430493458032609
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.116370509636402
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3622928395032883
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8402536353409291
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.624605417251588,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5684262131916151,
                  "rejected_mean_error": 4.286700434684754,
                  "gap_rejected_minus_accepted": 2.7182742214931386
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2340972423553467,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3622928395032883,
                  "rejected_mean_error": 3.274136022853851,
                  "gap_rejected_minus_accepted": 1.911843183350563
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7052494883537292,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.116370509636402,
                  "rejected_mean_error": 2.564136761045456,
                  "gap_rejected_minus_accepted": 1.447766251409054
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1932896077632904,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8430493458032609,
                  "rejected_mean_error": 2.1726550651868184,
                  "gap_rejected_minus_accepted": 1.3296057193835575
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.6296657562255863,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5773509115642972,
                  "rejected_mean_error": 4.3040989089012145,
                  "gap_rejected_minus_accepted": 2.7267479973369175
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.243810772895813,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.372976756731669,
                  "rejected_mean_error": 3.281172574996948,
                  "gap_rejected_minus_accepted": 1.908195818265279
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.727925181388855,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.123082138776779,
                  "rejected_mean_error": 2.5769692838191984,
                  "gap_rejected_minus_accepted": 1.4538871450424193
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2141557335853577,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8464344425201416,
                  "rejected_mean_error": 2.184556134223938,
                  "gap_rejected_minus_accepted": 1.3381216917037964
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.872452343395536,
              "spearman": 0.8865306496293051,
              "auroc_top30_bad": 0.97496,
              "mae": 0.3249433541357517,
              "mse": 0.2085740493878294,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 0.94,
              "same_context_pred_std": 0.6540696605199562,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.27031615644693374
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.29709737261533736
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4552419393181801
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7964254129171372
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
              "pearson": 0.7562201837220495,
              "spearman": 0.8329148821215246,
              "auroc_top30_worst": 0.9289508571428572,
              "pairwise_seed_ranking": 0.7576,
              "predicted_best_mean_error": 1.5785183277130126,
              "seed0_mean_error": 1.6587522393465042,
              "random_seed_mean_error": 1.6395123422145843,
              "oracle_best_mean_error": 1.5591331604719163,
              "improvement_over_seed0": 0.08023391163349158,
              "gap_to_oracle": 0.01938516724109629,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6010506565570831
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9080327451229095
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1593522809028625
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3958103243730215
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6363912368774414
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.861173033714295,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5618633489608764,
                  "rejected_mean_error": 2.307142228126526,
                  "gap_rejected_minus_accepted": 0.7452788791656495
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.132796585559845,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3949255883502858,
                  "rejected_mean_error": 2.359245270966722,
                  "gap_rejected_minus_accepted": 0.9643196826164362
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7126969695091248,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1593522809028625,
                  "rejected_mean_error": 2.1134301928520203,
                  "gap_rejected_minus_accepted": 0.9540779119491578
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2571255266666412,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9092701860129262,
                  "rejected_mean_error": 1.8792822602718846,
                  "gap_rejected_minus_accepted": 0.9700120742589584
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.845246410369873,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5883233283625708,
                  "rejected_mean_error": 2.292612438201904,
                  "gap_rejected_minus_accepted": 0.7042891098393333
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1310206055641174,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4185793783894196,
                  "rejected_mean_error": 2.3716462869492787,
                  "gap_rejected_minus_accepted": 0.9530669085598591
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7436022758483887,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1748553416728973,
                  "rejected_mean_error": 2.1426491370201113,
                  "gap_rejected_minus_accepted": 0.967793795347214
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2868468463420868,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9138651381409357,
                  "rejected_mean_error": 1.9097035087366154,
                  "gap_rejected_minus_accepted": 0.9958383705956797
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.813329761329799,
              "spearman": 0.8036562216359593,
              "auroc_top30_bad": 0.8951504761904762,
              "mae": 0.34051277659237383,
              "mse": 0.2240215565789716,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 0.912,
              "same_context_pred_std": 0.5646034300112462,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.29399512219429014
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.45183897401094436
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6388539651334286
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0246902022957802
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
              "pearson": 0.6179745493329316,
              "spearman": 0.594819140253892,
              "auroc_top30_worst": 0.7612739047619048,
              "pairwise_seed_ranking": 0.7188,
              "predicted_best_mean_error": 1.7700080019235611,
              "seed0_mean_error": 1.8436008858680726,
              "random_seed_mean_error": 1.808576955795288,
              "oracle_best_mean_error": 1.7398507182598113,
              "improvement_over_seed0": 0.07359288394451147,
              "gap_to_oracle": 0.030157283663749812,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.1062738094329834
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3596452680917888
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5672718879699707
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6968021990139601
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114040771961213
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1518507003784184,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.766325779332055,
                  "rejected_mean_error": 2.217108757972717,
                  "gap_rejected_minus_accepted": 0.4507829786406621
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.912853866815567,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6961643502450168,
                  "rejected_mean_error": 2.15638690196668,
                  "gap_rejected_minus_accepted": 0.46022255172166315
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.690005362033844,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5672718879699707,
                  "rejected_mean_error": 2.055536266422272,
                  "gap_rejected_minus_accepted": 0.4882643784523011
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4122045934200287,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3606106736027777,
                  "rejected_mean_error": 1.9619892803174837,
                  "gap_rejected_minus_accepted": 0.601378606714706
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1791995048522947,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7955727328194513,
                  "rejected_mean_error": 2.275854263305664,
                  "gap_rejected_minus_accepted": 0.4802815304862129
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9276089370250702,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.704416753136538,
                  "rejected_mean_error": 2.2567347401664373,
                  "gap_rejected_minus_accepted": 0.5523179870298993
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.70482337474823,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5839216346740723,
                  "rejected_mean_error": 2.1032801370620726,
                  "gap_rejected_minus_accepted": 0.5193585023880003
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4574259519577026,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3763945897420247,
                  "rejected_mean_error": 2.0010019375041206,
                  "gap_rejected_minus_accepted": 0.6246073477620959
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.752151781707104,
              "spearman": 0.764827147736318,
              "auroc_top30_bad": 0.8640714285714287,
              "mae": 0.42484850852750244,
              "mse": 0.2882067417048897,
              "expert_lt_perturb_large": 0.995,
              "expert_lt_other_task": 0.53,
              "expert_lt_simvla_seed0": 0.985,
              "same_context_pred_std": 0.5061629728226421,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3102058082818985
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.46699480119347575
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7946334405727684
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.090208802305162
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
              "pearson": 0.4501569622986963,
              "spearman": 0.4790722910722911,
              "auroc_top30_worst": 0.7801333333333333,
              "pairwise_seed_ranking": 0.645,
              "predicted_best_mean_error": 1.8907239291071891,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.0355061343312264,
              "gap_to_oracle": 0.027422541975975046,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.6635866367816925
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.711135280609131
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.7785746750831604
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.835327274799347
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.101162004470825,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8811636678377788,
                  "rejected_mean_error": 2.2171439599990843,
                  "gap_rejected_minus_accepted": 0.33598029216130554
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9482709765434265,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.835327274799347,
                  "rejected_mean_error": 2.1530649638175965,
                  "gap_rejected_minus_accepted": 0.3177376890182495
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5142226815223694,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.7785746750831604,
                  "rejected_mean_error": 2.050948719024658,
                  "gap_rejected_minus_accepted": 0.27237404394149767
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2002189457416534,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.711135280609131,
                  "rejected_mean_error": 1.9826371692021687,
                  "gap_rejected_minus_accepted": 0.2715018885930378
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.103310799598694,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.9020130429002973,
                  "rejected_mean_error": 2.144183248281479,
                  "gap_rejected_minus_accepted": 0.2421702053811816
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.952868938446045,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8537035075823467,
                  "rejected_mean_error": 2.1438097310066224,
                  "gap_rejected_minus_accepted": 0.2901062234242757
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5422824025154114,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.7907279860973357,
                  "rejected_mean_error": 2.0617321407794953,
                  "gap_rejected_minus_accepted": 0.27100415468215955
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2397509217262268,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.7099246549606324,
                  "rejected_mean_error": 1.9983318662643432,
                  "gap_rejected_minus_accepted": 0.28840721130371083
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_spatial/quantile_action_q80/model.pt"
      },
      {
        "variant": "quantile_action_q90",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.9,
        "best_epoch": 28,
        "best_calib_pinball": 0.08106254041194916,
        "train_time_sec": 15.844153881072998,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9639129698532509,
              "spearman": 0.9125553411480102,
              "auroc_top30_bad": 0.9948007857142857,
              "mae": 0.2919637050829828,
              "mse": 0.15465446731843657,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.481,
              "expert_lt_simvla_seed0": 0.93,
              "same_context_pred_std": 0.7520410634903084,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2883307907879353
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.36858714921176433
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4999281723693013
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8269649806330601
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
              "pearson": 0.9956603507386408,
              "spearman": 0.9932553818500534,
              "auroc_top30_worst": 0.996360380952381,
              "pairwise_seed_ranking": 0.6981,
              "predicted_best_mean_error": 1.7995943976044655,
              "seed0_mean_error": 1.850025711297989,
              "random_seed_mean_error": 1.841148916900158,
              "oracle_best_mean_error": 1.7736391132473945,
              "improvement_over_seed0": 0.050431313693523494,
              "gap_to_oracle": 0.02595528435707095,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6083275350928307
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8467298922777176
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1174655508160591
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.363174430123965
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8402536353409291
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.8994843959808367,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5683149340218967,
                  "rejected_mean_error": 4.287701947212219,
                  "gap_rejected_minus_accepted": 2.7193870131903224
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3978288173675537,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.363174430123965,
                  "rejected_mean_error": 3.2714912509918213,
                  "gap_rejected_minus_accepted": 1.9083168208678563
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8360561728477478,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1174655508160591,
                  "rejected_mean_error": 2.563041719865799,
                  "gap_rejected_minus_accepted": 1.44557616904974
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2997888922691345,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8467298922777176,
                  "rejected_mean_error": 2.1714282163619996,
                  "gap_rejected_minus_accepted": 1.324698324084282
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.921816778182985,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.577400664753384,
                  "rejected_mean_error": 4.303651130199432,
                  "gap_rejected_minus_accepted": 2.726250465446048
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.40081387758255,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3745049750010172,
                  "rejected_mean_error": 3.276587920188904,
                  "gap_rejected_minus_accepted": 1.9020829451878867
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8567606210708618,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1243496901988983,
                  "rejected_mean_error": 2.5757017323970794,
                  "gap_rejected_minus_accepted": 1.4513520421981811
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3253287971019745,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8514963550567627,
                  "rejected_mean_error": 2.1828688300450643,
                  "gap_rejected_minus_accepted": 1.3313724749883016
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8765743439349364,
              "spearman": 0.8709813507639625,
              "auroc_top30_bad": 0.9748830476190475,
              "mae": 0.3714987989485264,
              "mse": 0.23672137220152703,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.488,
              "expert_lt_simvla_seed0": 0.932,
              "same_context_pred_std": 0.6651571458424573,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2941080141663551
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3268187658905983
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4487121488213539
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7996977260351181
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
              "pearson": 0.7825189978702942,
              "spearman": 0.8337048412830985,
              "auroc_top30_worst": 0.9217737142857143,
              "pairwise_seed_ranking": 0.7216,
              "predicted_best_mean_error": 1.5859523918628693,
              "seed0_mean_error": 1.6587522393465042,
              "random_seed_mean_error": 1.6395123422145843,
              "oracle_best_mean_error": 1.5591331604719163,
              "improvement_over_seed0": 0.07279984748363488,
              "gap_to_oracle": 0.02681923139095299,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.616709762096405
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8945013712614011
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.157415818977356
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4162370281687169
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6363912368774414
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7830886602401743,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5640120594236586,
                  "rejected_mean_error": 2.287803833961487,
                  "gap_rejected_minus_accepted": 0.7237917745378282
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3249821066856384,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4154875067280348,
                  "rejected_mean_error": 2.297690901893396,
                  "gap_rejected_minus_accepted": 0.8822033951653614
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7980360388755798,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.157415818977356,
                  "rejected_mean_error": 2.1153666547775267,
                  "gap_rejected_minus_accepted": 0.9579508358001707
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3334203958511353,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8949466886611792,
                  "rejected_mean_error": 1.884066950422468,
                  "gap_rejected_minus_accepted": 0.9891202617612889
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.863305163383484,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5932522806856366,
                  "rejected_mean_error": 2.2482518672943117,
                  "gap_rejected_minus_accepted": 0.6549995866086751
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3646222352981567,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4449694400483912,
                  "rejected_mean_error": 2.29331388170757,
                  "gap_rejected_minus_accepted": 0.8483444416591788
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8484808206558228,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1855957744121552,
                  "rejected_mean_error": 2.1319087042808533,
                  "gap_rejected_minus_accepted": 0.9463129298686981
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3687960505485535,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8935911206025926,
                  "rejected_mean_error": 1.9165337927201216,
                  "gap_rejected_minus_accepted": 1.022942672117529
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8025490970460296,
              "spearman": 0.7923444774794443,
              "auroc_top30_bad": 0.8918133333333335,
              "mae": 0.3726855128854513,
              "mse": 0.2627276795525824,
              "expert_lt_perturb_large": 0.988,
              "expert_lt_other_task": 0.524,
              "expert_lt_simvla_seed0": 0.944,
              "same_context_pred_std": 0.5758988165709802,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.339461700797081
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.43927248190641405
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6457531518042088
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0345911461790402
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
              "pearson": 0.6172625716177719,
              "spearman": 0.5661981027564661,
              "auroc_top30_worst": 0.7633706666666665,
              "pairwise_seed_ranking": 0.6984,
              "predicted_best_mean_error": 1.776885648369789,
              "seed0_mean_error": 1.8436008858680726,
              "random_seed_mean_error": 1.808576955795288,
              "oracle_best_mean_error": 1.7398507182598113,
              "improvement_over_seed0": 0.06671523749828356,
              "gap_to_oracle": 0.037034930109977715,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.094061789035797
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.371814448864032
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.585453835105896
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.722675937452296
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114040771961213
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.312154483795166,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.767885674158732,
                  "rejected_mean_error": 2.203069704532623,
                  "gap_rejected_minus_accepted": 0.435184030373891
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.082166910171509,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7221703548441574,
                  "rejected_mean_error": 2.078535060722607,
                  "gap_rejected_minus_accepted": 0.3563647058784496
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8244861960411072,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.585453835105896,
                  "rejected_mean_error": 2.0373543192863464,
                  "gap_rejected_minus_accepted": 0.45190048418045037
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.540014386177063,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3732801550112592,
                  "rejected_mean_error": 1.9577571056314058,
                  "gap_rejected_minus_accepted": 0.5844769506201466
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.347462296485901,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7950815720028348,
                  "rejected_mean_error": 2.2802747106552124,
                  "gap_rejected_minus_accepted": 0.48519313865237756
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1170217394828796,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7430592775344849,
                  "rejected_mean_error": 2.14203391377888,
                  "gap_rejected_minus_accepted": 0.39897463624439533
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8694766163825989,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5988817930221557,
                  "rejected_mean_error": 2.0883199787139892,
                  "gap_rejected_minus_accepted": 0.4894381856918335
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5958537757396698,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.368832758494786,
                  "rejected_mean_error": 2.0035495063200353,
                  "gap_rejected_minus_accepted": 0.6347167478252493
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.721135200197104,
              "spearman": 0.7488090995947049,
              "auroc_top30_bad": 0.8658238095238096,
              "mae": 0.45275987533293666,
              "mse": 0.32569580880158483,
              "expert_lt_perturb_large": 0.995,
              "expert_lt_other_task": 0.51,
              "expert_lt_simvla_seed0": 0.975,
              "same_context_pred_std": 0.5103349366287492,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3605196990817785
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5691215580739081
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7691734554357826
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1005632311329245
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
              "pearson": 0.472757331750809,
              "spearman": 0.5197309837309838,
              "auroc_top30_worst": 0.7946809523809524,
              "pairwise_seed_ranking": 0.628,
              "predicted_best_mean_error": 1.896036496758461,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.03019356667995443,
              "gap_to_oracle": 0.03273510962724702,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.679179883003235
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.7025822105407715
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.7466138648986815
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8377423065503438
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.336246967315674,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.877168372074763,
                  "rejected_mean_error": 2.253101621866226,
                  "gap_rejected_minus_accepted": 0.37593324979146314
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.114445447921753,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8377423065503438,
                  "rejected_mean_error": 2.1458198685646055,
                  "gap_rejected_minus_accepted": 0.30807756201426173
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6734771132469177,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.7466138648986815,
                  "rejected_mean_error": 2.082909529209137,
                  "gap_rejected_minus_accepted": 0.3362956643104553
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3626881837844849,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.7025822105407715,
                  "rejected_mean_error": 1.9854881925582886,
                  "gap_rejected_minus_accepted": 0.28290598201751704
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.288697862625122,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8942784945170084,
                  "rejected_mean_error": 2.2137941837310793,
                  "gap_rejected_minus_accepted": 0.3195156892140709
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1044886708259583,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8664677166938781,
                  "rejected_mean_error": 2.1055171036720277,
                  "gap_rejected_minus_accepted": 0.2390493869781496
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6988218426704407,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.7575359845161438,
                  "rejected_mean_error": 2.0949241423606875,
                  "gap_rejected_minus_accepted": 0.3373881578445437
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3626881837844849,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.7136518836021424,
                  "rejected_mean_error": 1.9970894567171733,
                  "gap_rejected_minus_accepted": 0.2834375731150309
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_spatial/quantile_action_q90/model.pt"
      },
      {
        "variant": "quantile_action_q95",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.95,
        "best_epoch": 1,
        "best_calib_pinball": 0.05151030793786049,
        "train_time_sec": 15.95012092590332,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8812125663499979,
              "spearman": 0.7888468800048952,
              "auroc_top30_bad": 0.9509303571428572,
              "mae": 0.9109037454433739,
              "mse": 1.1017333630618713,
              "expert_lt_perturb_large": 0.99,
              "expert_lt_other_task": 0.485,
              "expert_lt_simvla_seed0": 0.956,
              "same_context_pred_std": 0.7424449500157795,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.45370047775655986
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4947487923294306
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5909866813138127
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8621817004293203
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
              "pearson": 0.9343878556073607,
              "spearman": 0.8773367610985265,
              "auroc_top30_worst": 0.969109619047619,
              "pairwise_seed_ranking": 0.6185,
              "predicted_best_mean_error": 1.810337087869644,
              "seed0_mean_error": 1.850025711297989,
              "random_seed_mean_error": 1.841148916900158,
              "oracle_best_mean_error": 1.7736391132473945,
              "improvement_over_seed0": 0.039688623428344894,
              "gap_to_oracle": 0.03669797462224955,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7122945527434349
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9473102811098099
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1939567840218543
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3832034325520197
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8402536353409291
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.888437414169313,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5700503026975525,
                  "rejected_mean_error": 4.272083629131317,
                  "gap_rejected_minus_accepted": 2.7020333264337646
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.05623722076416,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3832034325520197,
                  "rejected_mean_error": 3.2114042437076566,
                  "gap_rejected_minus_accepted": 1.828200811155637
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.3442299365997314,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1939567840218543,
                  "rejected_mean_error": 2.4865504866600037,
                  "gap_rejected_minus_accepted": 1.2925937026381493
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.888639122247696,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.9473102811098099,
                  "rejected_mean_error": 2.1379014200846354,
                  "gap_rejected_minus_accepted": 1.1905911389748254
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.994867515563965,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.577745594713423,
                  "rejected_mean_error": 4.300546760559082,
                  "gap_rejected_minus_accepted": 2.7228011658456595
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.097135305404663,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.390007557074229,
                  "rejected_mean_error": 3.230080173969269,
                  "gap_rejected_minus_accepted": 1.8400726168950399
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.3690459728240967,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.2092374542951583,
                  "rejected_mean_error": 2.4908139683008192,
                  "gap_rejected_minus_accepted": 1.281576514005661
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.89242684841156,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.9522132484912872,
                  "rejected_mean_error": 2.149296532233556,
                  "gap_rejected_minus_accepted": 1.197083283742269
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.7613593199437902,
              "spearman": 0.7475088978037601,
              "auroc_top30_bad": 0.9236365714285714,
              "mae": 0.8957725847899913,
              "mse": 1.1182415564591086,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.484,
              "expert_lt_simvla_seed0": 0.952,
              "same_context_pred_std": 0.6945644250624126,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.36783904042840004
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.41116256049871447
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5673739802241325
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8449265441020329
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
              "pearson": 0.6380312367897936,
              "spearman": 0.6576499691839803,
              "auroc_top30_worst": 0.8515657142857143,
              "pairwise_seed_ranking": 0.6432,
              "predicted_best_mean_error": 1.602060034751892,
              "seed0_mean_error": 1.6587522393465042,
              "random_seed_mean_error": 1.6395123422145843,
              "oracle_best_mean_error": 1.5591331604719163,
              "improvement_over_seed0": 0.056692204594612106,
              "gap_to_oracle": 0.04292687427997577,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7326436758041381
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0632778345965421
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.270802787733078
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.446859025561225
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6363912368774414
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.435824394226074,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5754152743021648,
                  "rejected_mean_error": 2.1851749000549314,
                  "gap_rejected_minus_accepted": 0.6097596257527667
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.073268413543701,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4450531563738493,
                  "rejected_mean_error": 2.2091828708450634,
                  "gap_rejected_minus_accepted": 0.764129714471214
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.487023115158081,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.270802787733078,
                  "rejected_mean_error": 2.0019796860218046,
                  "gap_rejected_minus_accepted": 0.7311768982887266
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.8548337519168854,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.064485067091049,
                  "rejected_mean_error": 1.8274335326545394,
                  "gap_rejected_minus_accepted": 0.7629484655634904
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.489610457420349,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.589239593744278,
                  "rejected_mean_error": 2.2843660497665406,
                  "gap_rejected_minus_accepted": 0.6951264560222625
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.158182740211487,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4791134055604271,
                  "rejected_mean_error": 2.1919659205845425,
                  "gap_rejected_minus_accepted": 0.7128525150241154
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.4644235372543335,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.289557070016861,
                  "rejected_mean_error": 2.0279474086761473,
                  "gap_rejected_minus_accepted": 0.7383903386592863
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.8731541633605957,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0559151688265422,
                  "rejected_mean_error": 1.8618470812863845,
                  "gap_rejected_minus_accepted": 0.8059319124598423
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6709493553329479,
              "spearman": 0.7280610599315193,
              "auroc_top30_bad": 0.8829980952380951,
              "mae": 0.766284068492055,
              "mse": 0.9302158953987378,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.96,
              "same_context_pred_std": 0.564073502790051,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46486264395713806
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5564272307157516
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7298070638954639
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0206420694470406
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
              "pearson": 0.6249351042160147,
              "spearman": 0.6493741166928734,
              "auroc_top30_worst": 0.8135619047619048,
              "pairwise_seed_ranking": 0.5816,
              "predicted_best_mean_error": 1.8011582020521164,
              "seed0_mean_error": 1.8436008858680726,
              "random_seed_mean_error": 1.808576955795288,
              "oracle_best_mean_error": 1.7398507182598113,
              "improvement_over_seed0": 0.04244268381595617,
              "gap_to_oracle": 0.061307483792305106,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0659257078170776
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3293481465333548
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5410969245910644
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6983732379702872
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114040771961213
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9840964078903203,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7648723526530796,
                  "rejected_mean_error": 2.2301895980834963,
                  "gap_rejected_minus_accepted": 0.46531724543041664
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.5813034176826477,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.697951785846352,
                  "rejected_mean_error": 2.151036016476421,
                  "gap_rejected_minus_accepted": 0.4530842306300691
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.230758309364319,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5410969245910644,
                  "rejected_mean_error": 2.081711229801178,
                  "gap_rejected_minus_accepted": 0.5406143052101136
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.9166539907455444,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.331366016841925,
                  "rejected_mean_error": 1.9717583065353566,
                  "gap_rejected_minus_accepted": 0.6403922896934315
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.056173086166382,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7833899466196697,
                  "rejected_mean_error": 2.3854993391036987,
                  "gap_rejected_minus_accepted": 0.6021093924840291
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.5837416648864746,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.721696543821039,
                  "rejected_mean_error": 2.2054439328965687,
                  "gap_rejected_minus_accepted": 0.4837473890755297
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.237191915512085,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5566852445602417,
                  "rejected_mean_error": 2.1305165271759035,
                  "gap_rejected_minus_accepted": 0.5738312826156617
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.951062262058258,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3080666008449735,
                  "rejected_mean_error": 2.024021527346443,
                  "gap_rejected_minus_accepted": 0.7159549265014693
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.5501895932358736,
              "spearman": 0.6092353195776774,
              "auroc_top30_bad": 0.8151619047619048,
              "mae": 0.7747972005289048,
              "mse": 0.9115118556054167,
              "expert_lt_perturb_large": 0.985,
              "expert_lt_other_task": 0.49,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.44942217711596016,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9782366774231196
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8766702216565609
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8416400285549461
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1232170652175943
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
              "pearson": 0.3117861938093398,
              "spearman": 0.37483917883917883,
              "auroc_top30_worst": 0.6664,
              "pairwise_seed_ranking": 0.568,
              "predicted_best_mean_error": 1.9032027870416641,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.023027276396751395,
              "gap_to_oracle": 0.03990139991045005,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.8317710959911346
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.7984438993930816
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.7945497591495514
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8455195167859395
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.703683042526245,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.869751476711697,
                  "rejected_mean_error": 2.3198536801338197,
                  "gap_rejected_minus_accepted": 0.4501022034221227
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.454938054084778,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8455195167859395,
                  "rejected_mean_error": 2.1224882378578185,
                  "gap_rejected_minus_accepted": 0.276968721071879
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.265230417251587,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.7945497591495514,
                  "rejected_mean_error": 2.034973634958267,
                  "gap_rejected_minus_accepted": 0.24042387580871583
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.0834853649139404,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.7984438993930816,
                  "rejected_mean_error": 1.9535342962741853,
                  "gap_rejected_minus_accepted": 0.1550903968811037
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6510085821151734,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.881602915790346,
                  "rejected_mean_error": 2.327874392271042,
                  "gap_rejected_minus_accepted": 0.4462714764806959
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4459853768348694,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8528112769126892,
                  "rejected_mean_error": 2.1464864230155944,
                  "gap_rejected_minus_accepted": 0.29367514610290524
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.2874653339385986,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.767555992603302,
                  "rejected_mean_error": 2.084904134273529,
                  "gap_rejected_minus_accepted": 0.31734814167022707
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.123182773590088,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.7881696510314942,
                  "rejected_mean_error": 1.9722502009073892,
                  "gap_rejected_minus_accepted": 0.18408054987589506
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_spatial/quantile_action_q95/model.pt"
      },
      {
        "variant": "quantile_context_gated_q80",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.8,
        "best_epoch": 117,
        "best_calib_pinball": 0.036507077515125275,
        "train_time_sec": 50.749314069747925,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9996383930717891,
              "spearman": 0.9988249547013957,
              "auroc_top30_bad": 0.9997998571428571,
              "mae": 0.04585779894636944,
              "mse": 0.0031900105386400857,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8295962818075207,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0004939070791006088
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17265502723157405
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4751410443291068
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8225500807752212
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
              "pearson": 0.9997449365550426,
              "spearman": 0.9997465651978443,
              "auroc_top30_worst": 0.9998838095238095,
              "pairwise_seed_ranking": 0.94595,
              "predicted_best_mean_error": 1.7744280944168567,
              "seed0_mean_error": 1.850025711297989,
              "random_seed_mean_error": 1.841148916900158,
              "oracle_best_mean_error": 1.7736391132473945,
              "improvement_over_seed0": 0.07559761688113231,
              "gap_to_oracle": 0.0007889811694621329,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.603704564511776
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.840350562787056
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.114459955227375
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3616745361089706
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8402536353409291
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.5196831226348877,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5681369606455167,
                  "rejected_mean_error": 4.28930370759964,
                  "gap_rejected_minus_accepted": 2.7211667469541228
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1945629119873047,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3616745361089706,
                  "rejected_mean_error": 3.275990933036804,
                  "gap_rejected_minus_accepted": 1.9143163969278334
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6993584632873535,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.114459955227375,
                  "rejected_mean_error": 2.566047315454483,
                  "gap_rejected_minus_accepted": 1.451587360227108
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1978941857814789,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.840350562787056,
                  "rejected_mean_error": 2.1735546595255535,
                  "gap_rejected_minus_accepted": 1.3332040967384975
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.492125511169434,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5771077304416232,
                  "rejected_mean_error": 4.30628753900528,
                  "gap_rejected_minus_accepted": 2.7291798085636563
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.222400426864624,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3725572614669799,
                  "rejected_mean_error": 3.2824310607910157,
                  "gap_rejected_minus_accepted": 1.9098737993240358
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7201737761497498,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1212742333412171,
                  "rejected_mean_error": 2.578777189254761,
                  "gap_rejected_minus_accepted": 1.4575029559135437
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2092503011226654,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8438236622810363,
                  "rejected_mean_error": 2.1854263943036396,
                  "gap_rejected_minus_accepted": 1.3416027320226034
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9857921034201756,
              "spearman": 0.9917525174126892,
              "auroc_top30_bad": 0.9964449523809523,
              "mae": 0.0955259074093774,
              "mse": 0.02171789080613388,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7540813495200863,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.03781840446591377
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1592540420293808
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4025510268807411
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.774859649570783
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
              "pearson": 0.9656812464046366,
              "spearman": 0.988558107493189,
              "auroc_top30_worst": 0.9957668571428572,
              "pairwise_seed_ranking": 0.934,
              "predicted_best_mean_error": 1.5606680767536163,
              "seed0_mean_error": 1.6587522393465042,
              "random_seed_mean_error": 1.6395123422145843,
              "oracle_best_mean_error": 1.5591331604719163,
              "improvement_over_seed0": 0.09808416259288788,
              "gap_to_oracle": 0.001534916281699994,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4668708372116089
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7535260510750306
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.092422988319397
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3450405987849368
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6363912368774414
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5554789066314703,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5122061282263861,
                  "rejected_mean_error": 2.7540572147369384,
                  "gap_rejected_minus_accepted": 1.2418510865105523
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.118885338306427,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3441626790239056,
                  "rejected_mean_error": 2.5112096353079947,
                  "gap_rejected_minus_accepted": 1.167046956284089
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7508135437965393,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.092422988319397,
                  "rejected_mean_error": 2.1803594854354857,
                  "gap_rejected_minus_accepted": 1.0879364971160888
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1763822436332703,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7542610867335774,
                  "rejected_mean_error": 1.9310622475444952,
                  "gap_rejected_minus_accepted": 1.1768011608109177
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.566835308074951,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5325516468948788,
                  "rejected_mean_error": 2.794557571411133,
                  "gap_rejected_minus_accepted": 1.262005924516254
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.139787256717682,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.361628626279015,
                  "rejected_mean_error": 2.540690582896036,
                  "gap_rejected_minus_accepted": 1.179061956617021
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7732270956039429,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1106652147769929,
                  "rejected_mean_error": 2.2068392639160157,
                  "gap_rejected_minus_accepted": 1.0961740491390228
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1992985904216766,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7644461038566771,
                  "rejected_mean_error": 1.9600425416773015,
                  "gap_rejected_minus_accepted": 1.1955964378206243
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9877158572735598,
              "spearman": 0.9865157619526902,
              "auroc_top30_bad": 0.9907573333333334,
              "mae": 0.0834286931104958,
              "mse": 0.016257515302926868,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7490143449540606,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.01716344881057739
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17533296316862107
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5720387697637082
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9595243068973224
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
              "pearson": 0.9598951011444635,
              "spearman": 0.9739948535887625,
              "auroc_top30_worst": 0.9736228571428571,
              "pairwise_seed_ranking": 0.93,
              "predicted_best_mean_error": 1.7419089843034745,
              "seed0_mean_error": 1.8436008858680726,
              "random_seed_mean_error": 1.808576955795288,
              "oracle_best_mean_error": 1.7398507182598113,
              "improvement_over_seed0": 0.10169190156459806,
              "gap_to_oracle": 0.002058266043663215,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8759159874916077
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1802112580491946
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4371588320732116
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6141694010829113
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114040771961213
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.339344310760498,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7238155077298483,
                  "rejected_mean_error": 2.5997012023925783,
                  "gap_rejected_minus_accepted": 0.87588569466273
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0772390365600586,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6137171157396208,
                  "rejected_mean_error": 2.4032017860930566,
                  "gap_rejected_minus_accepted": 0.7894846703534357
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8674995303153992,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4371588320732116,
                  "rejected_mean_error": 2.1856493223190308,
                  "gap_rejected_minus_accepted": 0.7484904902458192
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5789707005023956,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1815854168166748,
                  "rejected_mean_error": 2.0217917406953387,
                  "gap_rejected_minus_accepted": 0.8402063238786639
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4386839151382445,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7487144316567316,
                  "rejected_mean_error": 2.6975789737701414,
                  "gap_rejected_minus_accepted": 0.9488645421134099
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0931631922721863,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6298087255202514,
                  "rejected_mean_error": 2.478190314202082,
                  "gap_rejected_minus_accepted": 0.8483815886818304
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9046592712402344,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.447310501098633,
                  "rejected_mean_error": 2.239891270637512,
                  "gap_rejected_minus_accepted": 0.7925807695388791
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5923581719398499,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1874046344605704,
                  "rejected_mean_error": 2.064672350246001,
                  "gap_rejected_minus_accepted": 0.8772677157854305
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9897677230716575,
              "spearman": 0.9761186283744373,
              "auroc_top30_bad": 0.9706345238095239,
              "mae": 0.0825961724552326,
              "mse": 0.013872659930259146,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.99,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7501415968861435,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.025613092873245476
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16798267263919114
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6619026420153677
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.055315906845033
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
              "pearson": 0.949314541081697,
              "spearman": 0.9403632403632405,
              "auroc_top30_worst": 0.9720380952380954,
              "pairwise_seed_ranking": 0.8925,
              "predicted_best_mean_error": 1.8656112876534463,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.060618775784969214,
              "gap_to_oracle": 0.0023099005222322333,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.296321085691452
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.446128068447113
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6458846926689148
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7659913846651714
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2831529140472413,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8476777961519029,
                  "rejected_mean_error": 2.5185168051719664,
                  "gap_rejected_minus_accepted": 0.6708390090200635
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.090986728668213,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7659913846651714,
                  "rejected_mean_error": 2.361072634220123,
                  "gap_rejected_minus_accepted": 0.5950812495549518
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8874601125717163,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6458846926689148,
                  "rejected_mean_error": 2.1836387014389036,
                  "gap_rejected_minus_accepted": 0.5377540087699888
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.692848026752472,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.446128068447113,
                  "rejected_mean_error": 2.070972906589508,
                  "gap_rejected_minus_accepted": 0.6248448381423952
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.294557523727417,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8609111454751757,
                  "rejected_mean_error": 2.5141003251075746,
                  "gap_rejected_minus_accepted": 0.653189179632399
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0975791811943054,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.771122802098592,
                  "rejected_mean_error": 2.391551847457886,
                  "gap_rejected_minus_accepted": 0.6204290453592938
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8990105390548706,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6514908611774444,
                  "rejected_mean_error": 2.2009692656993867,
                  "gap_rejected_minus_accepted": 0.5494784045219423
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7242565155029297,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4548325657844543,
                  "rejected_mean_error": 2.0833625626564025,
                  "gap_rejected_minus_accepted": 0.6285299968719482
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_spatial/quantile_context_gated_q80/model.pt"
      },
      {
        "variant": "quantile_context_gated_q90",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.9,
        "best_epoch": 104,
        "best_calib_pinball": 0.03205453231930733,
        "train_time_sec": 51.05867671966553,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9979169645035737,
              "spearman": 0.9977467888272299,
              "auroc_top30_bad": 0.999453,
              "mae": 0.10588428550721146,
              "mse": 0.018477595681279498,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8451836682208712,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0062809475287795066
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17306757285296917
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.47533604285568
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8229093735684951
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
              "pearson": 0.9969495412313607,
              "spearman": 0.9991874475194977,
              "auroc_top30_worst": 0.9995828571428571,
              "pairwise_seed_ranking": 0.8781,
              "predicted_best_mean_error": 1.780742926031351,
              "seed0_mean_error": 1.850025711297989,
              "random_seed_mean_error": 1.841148916900158,
              "oracle_best_mean_error": 1.7736391132473945,
              "improvement_over_seed0": 0.069282785266638,
              "gap_to_oracle": 0.0071038127839564424,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6045976085066795
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8406537087678909
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1145728869080544
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3618500571966172
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8402536353409291
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.663385415077212,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5683168754378956,
                  "rejected_mean_error": 4.287684474468231,
                  "gap_rejected_minus_accepted": 2.7193675990303356
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2712982892990112,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3618500571966172,
                  "rejected_mean_error": 3.275464369773865,
                  "gap_rejected_minus_accepted": 1.9136143125772476
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7460467219352722,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1145728869080544,
                  "rejected_mean_error": 2.565934383773804,
                  "gap_rejected_minus_accepted": 1.4513614968657493
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.233989030122757,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8406537087678909,
                  "rejected_mean_error": 2.173453610865275,
                  "gap_rejected_minus_accepted": 1.3327999020973842
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.640661931037903,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5773835791481865,
                  "rejected_mean_error": 4.30380490064621,
                  "gap_rejected_minus_accepted": 2.726421321498023
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2856401801109314,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3726885229746502,
                  "rejected_mean_error": 3.2820372762680052,
                  "gap_rejected_minus_accepted": 1.909348753293355
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7636481523513794,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1211301860809326,
                  "rejected_mean_error": 2.578921236515045,
                  "gap_rejected_minus_accepted": 1.4577910504341125
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.246896743774414,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.84391450548172,
                  "rejected_mean_error": 2.185396113236745,
                  "gap_rejected_minus_accepted": 1.3414816077550253
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9645760567511222,
              "spearman": 0.9887191501530646,
              "auroc_top30_bad": 0.9966986666666667,
              "mae": 0.16055870284996926,
              "mse": 0.0705519168916381,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.77377402243928,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.03128155687451362
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.161179745221138
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.40339141055345534
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.775605585583051
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
              "pearson": 0.9048398867863356,
              "spearman": 0.9786718659972344,
              "auroc_top30_worst": 0.9906499047619048,
              "pairwise_seed_ranking": 0.9068,
              "predicted_best_mean_error": 1.5619441958665847,
              "seed0_mean_error": 1.6587522393465042,
              "random_seed_mean_error": 1.6395123422145843,
              "oracle_best_mean_error": 1.5591331604719163,
              "improvement_over_seed0": 0.09680804347991945,
              "gap_to_oracle": 0.0028110353946684263,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46493609809875486
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7503824495734313
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.091566671180725
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3494241035569197
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6363912368774414
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6837904214859014,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5424810047149657,
                  "rejected_mean_error": 2.4815833263397216,
                  "gap_rejected_minus_accepted": 0.9391023216247558
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1893975138664246,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3485266418060091,
                  "rejected_mean_error": 2.4981456317078954,
                  "gap_rejected_minus_accepted": 1.1496189899018863
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.808166265487671,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.091566671180725,
                  "rejected_mean_error": 2.1812158025741577,
                  "gap_rejected_minus_accepted": 1.0896491313934327
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1719108521938324,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7515435140734663,
                  "rejected_mean_error": 1.9319700386251941,
                  "gap_rejected_minus_accepted": 1.1804265245517278
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7520082235336303,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5644079400433435,
                  "rejected_mean_error": 2.507850933074951,
                  "gap_rejected_minus_accepted": 0.9434429930316075
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2130109071731567,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3662882432899373,
                  "rejected_mean_error": 2.526859656212822,
                  "gap_rejected_minus_accepted": 1.1605714129228846
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8390161395072937,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1098343126773835,
                  "rejected_mean_error": 2.207670166015625,
                  "gap_rejected_minus_accepted": 1.0978358533382415
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2119717001914978,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7594133525613754,
                  "rejected_mean_error": 1.9617380675147562,
                  "gap_rejected_minus_accepted": 1.202324714953381
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9743090574425547,
              "spearman": 0.982434655102117,
              "auroc_top30_bad": 0.9891459047619048,
              "mae": 0.12307894531916827,
              "mse": 0.037390931301861184,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7464266189682753,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.028005178302526475
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17511627224683762
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5730772512853146
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9610334105451902
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
              "pearson": 0.8951754542640253,
              "spearman": 0.9651206539756441,
              "auroc_top30_worst": 0.9657874285714286,
              "pairwise_seed_ranking": 0.896,
              "predicted_best_mean_error": 1.7446301769018173,
              "seed0_mean_error": 1.8436008858680726,
              "random_seed_mean_error": 1.808576955795288,
              "oracle_best_mean_error": 1.7398507182598113,
              "improvement_over_seed0": 0.09897070896625526,
              "gap_to_oracle": 0.004779458642006018,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8771760544776916
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1856142353170958
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.439349580860138
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.615267824071811
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114040771961213
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2736827135086064,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7264684428638881,
                  "rejected_mean_error": 2.5758247861862182,
                  "gap_rejected_minus_accepted": 0.8493563433223301
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.090800642967224,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6149798888025315,
                  "rejected_mean_error": 2.3994215357417876,
                  "gap_rejected_minus_accepted": 0.7844416469392561
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9064661264419556,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.439349580860138,
                  "rejected_mean_error": 2.1834585735321044,
                  "gap_rejected_minus_accepted": 0.7441089926719664
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.620816171169281,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1866125590123309,
                  "rejected_mean_error": 2.02011244986584,
                  "gap_rejected_minus_accepted": 0.833499890853509
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3736669063568114,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.752074302567376,
                  "rejected_mean_error": 2.667340135574341,
                  "gap_rejected_minus_accepted": 0.915265833006965
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1179566383361816,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.626794252166136,
                  "rejected_mean_error": 2.48713803669763,
                  "gap_rejected_minus_accepted": 0.8603437845314941
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.923820972442627,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4504591979980468,
                  "rejected_mean_error": 2.236742573738098,
                  "gap_rejected_minus_accepted": 0.7862833757400511
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6595107018947601,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1886003736465696,
                  "rejected_mean_error": 2.064269507632536,
                  "gap_rejected_minus_accepted": 0.8756691339859664
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9882785596394317,
              "spearman": 0.9756962660385546,
              "auroc_top30_bad": 0.971677380952381,
              "mae": 0.09864322361699306,
              "mse": 0.018097882135959906,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7460077597496112,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.034831089191138746
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16930970514565707
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6633341323174536
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.055662431401511
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
              "pearson": 0.9478862865307648,
              "spearman": 0.9372455892455893,
              "auroc_top30_worst": 0.9677047619047621,
              "pairwise_seed_ranking": 0.85,
              "predicted_best_mean_error": 1.8692222526669502,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.05700781077146533,
              "gap_to_oracle": 0.0059208655357361195,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3031291139125825
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4502770457267762
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6446574547290802
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7686642082532247
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3178473472595216,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8475958773824903,
                  "rejected_mean_error": 2.5192540740966796,
                  "gap_rejected_minus_accepted": 0.6716581967141892
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.120051383972168,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7686642082532247,
                  "rejected_mean_error": 2.353054163455963,
                  "gap_rejected_minus_accepted": 0.5843899552027385
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9513171315193176,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6446574547290802,
                  "rejected_mean_error": 2.184865939378738,
                  "gap_rejected_minus_accepted": 0.540208484649658
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.737418293952942,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4502770457267762,
                  "rejected_mean_error": 2.069589914162954,
                  "gap_rejected_minus_accepted": 0.6193128684361777
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3206986665725706,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8590494381056892,
                  "rejected_mean_error": 2.530855691432953,
                  "gap_rejected_minus_accepted": 0.6718062533272637
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.119167149066925,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7735025699933369,
                  "rejected_mean_error": 2.384412543773651,
                  "gap_rejected_minus_accepted": 0.6109099737803143
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9725406765937805,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6501358699798585,
                  "rejected_mean_error": 2.2023242568969725,
                  "gap_rejected_minus_accepted": 0.552188386917114
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.751142680644989,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4623324060440064,
                  "rejected_mean_error": 2.0808626159032184,
                  "gap_rejected_minus_accepted": 0.618530209859212
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_spatial/quantile_context_gated_q90/model.pt"
      },
      {
        "variant": "quantile_context_gated_q95",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.95,
        "best_epoch": 115,
        "best_calib_pinball": 0.022842910140752792,
        "train_time_sec": 50.9378616809845,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9972640812381443,
              "spearman": 0.9965590724110145,
              "auroc_top30_bad": 0.9989784761904762,
              "mae": 0.18214280491457321,
              "mse": 0.04982155580355174,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9046674092752593,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.011484595112502575
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1742226722329855
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4756107553943992
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8233723141978184
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
              "pearson": 0.9973116948224238,
              "spearman": 0.9993351503414059,
              "auroc_top30_worst": 0.9994434285714285,
              "pairwise_seed_ranking": 0.8875,
              "predicted_best_mean_error": 1.7783429373800754,
              "seed0_mean_error": 1.850025711297989,
              "random_seed_mean_error": 1.841148916900158,
              "oracle_best_mean_error": 1.7736391132473945,
              "improvement_over_seed0": 0.07168277391791356,
              "gap_to_oracle": 0.004703824132680889,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6044625669121743
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8406203254938126
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.114654009592533
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.36184187104702
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8402536353409291
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.852290010452271,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5681526428659758,
                  "rejected_mean_error": 4.289162567615509,
                  "gap_rejected_minus_accepted": 2.7210099247495334
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4783374667167664,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.36184187104702,
                  "rejected_mean_error": 3.2754889282226562,
                  "gap_rejected_minus_accepted": 1.9136470571756363
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9160191416740417,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.114654009592533,
                  "rejected_mean_error": 2.565853261089325,
                  "gap_rejected_minus_accepted": 1.451199251496792
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3467315137386322,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8406203254938126,
                  "rejected_mean_error": 2.1734647386233013,
                  "gap_rejected_minus_accepted": 1.3328444131294885
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.800567269325257,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5771077304416232,
                  "rejected_mean_error": 4.30628753900528,
                  "gap_rejected_minus_accepted": 2.7291798085636563
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.494148552417755,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3728500207265217,
                  "rejected_mean_error": 3.28155278301239,
                  "gap_rejected_minus_accepted": 1.9087027622858683
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9437793493270874,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1212408974170684,
                  "rejected_mean_error": 2.5788105251789095,
                  "gap_rejected_minus_accepted": 1.457569627761841
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.360550194978714,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.84382533121109,
                  "rejected_mean_error": 2.185425837993622,
                  "gap_rejected_minus_accepted": 1.341600506782532
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9787900618865732,
              "spearman": 0.9880058322090782,
              "auroc_top30_bad": 0.9946704761904761,
              "mae": 0.21190571808200329,
              "mse": 0.07841841340927952,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8367914521484517,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04200552225112915
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.15995294072628022
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.40333652774095535
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7765908717870712
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
              "pearson": 0.9459513221477002,
              "spearman": 0.9842264004008964,
              "auroc_top30_worst": 0.9953889523809524,
              "pairwise_seed_ranking": 0.9124,
              "predicted_best_mean_error": 1.5619159408807755,
              "seed0_mean_error": 1.6587522393465042,
              "random_seed_mean_error": 1.6395123422145843,
              "oracle_best_mean_error": 1.5591331604719163,
              "improvement_over_seed0": 0.09683629846572872,
              "gap_to_oracle": 0.0027827804088591535,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46780422496795654
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7492809912715203
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0923108522415161
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.345802483273976
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6363912368774414
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.838823390007019,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5273535544077554,
                  "rejected_mean_error": 2.6177303791046143,
                  "gap_rejected_minus_accepted": 1.0903768246968588
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.419024705886841,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.345181024952403,
                  "rejected_mean_error": 2.50816110452524,
                  "gap_rejected_minus_accepted": 1.1629800795728369
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9858796000480652,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0923108522415161,
                  "rejected_mean_error": 2.180471621513367,
                  "gap_rejected_minus_accepted": 1.0881607692718507
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.298585295677185,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7500838313620692,
                  "rejected_mean_error": 1.9324576380794813,
                  "gap_rejected_minus_accepted": 1.182373806717412
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8952534437179565,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5498359660307566,
                  "rejected_mean_error": 2.6389986991882326,
                  "gap_rejected_minus_accepted": 1.089162733157476
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4533830881118774,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3645410813431051,
                  "rejected_mean_error": 2.532045676594689,
                  "gap_rejected_minus_accepted": 1.1675045952515837
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0104857683181763,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1109281895160674,
                  "rejected_mean_error": 2.2065762891769407,
                  "gap_rejected_minus_accepted": 1.0956480996608733
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3270434737205505,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.760949928136099,
                  "rejected_mean_error": 1.9612203976687264,
                  "gap_rejected_minus_accepted": 1.2002704695326274
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9833784791502029,
              "spearman": 0.9845599741005776,
              "auroc_top30_bad": 0.9901424761904761,
              "mae": 0.1709872338404879,
              "mse": 0.049258589897667966,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8157915685684772,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.02288535538315773
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17318833240270615
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5726890078008174
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9599636785785357
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
              "pearson": 0.9349172331474195,
              "spearman": 0.9663829994378483,
              "auroc_top30_worst": 0.9734217142857142,
              "pairwise_seed_ranking": 0.8944,
              "predicted_best_mean_error": 1.7437564651966095,
              "seed0_mean_error": 1.8436008858680726,
              "random_seed_mean_error": 1.808576955795288,
              "oracle_best_mean_error": 1.7398507182598113,
              "improvement_over_seed0": 0.09984442067146304,
              "gap_to_oracle": 0.003905746936798238,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8835376334190369
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1855288677108593
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.436326292324066
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6160993626249878
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114040771961213
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5114224910736085,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.725626163535648,
                  "rejected_mean_error": 2.583405300140381,
                  "gap_rejected_minus_accepted": 0.8577791366047329
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3051875233650208,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6156870325830475,
                  "rejected_mean_error": 2.39730462289085,
                  "gap_rejected_minus_accepted": 0.7816175903078026
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0929938554763794,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.436326292324066,
                  "rejected_mean_error": 2.186481862068176,
                  "gap_rejected_minus_accepted": 0.75015556974411
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7936542630195618,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1866649166463663,
                  "rejected_mean_error": 2.020094960069198,
                  "gap_rejected_minus_accepted": 0.8334300434228319
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5694463729858397,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7500391149520873,
                  "rejected_mean_error": 2.6856568241119385,
                  "gap_rejected_minus_accepted": 0.9356177091598512
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3530498147010803,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6286089095202358,
                  "rejected_mean_error": 2.4817516728053017,
                  "gap_rejected_minus_accepted": 0.8531427632850659
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.116472601890564,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4455607070922851,
                  "rejected_mean_error": 2.24164106464386,
                  "gap_rejected_minus_accepted": 0.7960803575515749
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.8156032860279083,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1913160274899195,
                  "rejected_mean_error": 2.063354608209375,
                  "gap_rejected_minus_accepted": 0.8720385807194557
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9900735234218747,
              "spearman": 0.9793524366973162,
              "auroc_top30_bad": 0.9761880952380952,
              "mae": 0.15233475633175111,
              "mse": 0.036126038594299345,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.83738076609667,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.026872734669595957
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1686307639554143
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6631576342619956
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0544489089672764
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
              "pearson": 0.9583096162527502,
              "spearman": 0.9452502000859507,
              "auroc_top30_worst": 0.9616523809523809,
              "pairwise_seed_ranking": 0.86,
              "predicted_best_mean_error": 1.86797717243433,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.058252891004085594,
              "gap_to_oracle": 0.004675785303115854,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2866039204597473
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4470420322418214
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6436888256073
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7677020853360494
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.54737446308136,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8460366704728868,
                  "rejected_mean_error": 2.5332869362831114,
                  "gap_rejected_minus_accepted": 0.6872502658102246
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3110121488571167,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7677020853360494,
                  "rejected_mean_error": 2.355940532207489,
                  "gap_rejected_minus_accepted": 0.5882384468714397
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.1378036737442017,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6436888256073,
                  "rejected_mean_error": 2.185834568500519,
                  "gap_rejected_minus_accepted": 0.542145742893219
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.919256180524826,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4470420322418214,
                  "rejected_mean_error": 2.070668251991272,
                  "gap_rejected_minus_accepted": 0.6236262197494504
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.554278326034546,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.858902060985565,
                  "rejected_mean_error": 2.5321820855140684,
                  "gap_rejected_minus_accepted": 0.6732800245285033
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.305374503135681,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7762375418345133,
                  "rejected_mean_error": 2.376207628250122,
                  "gap_rejected_minus_accepted": 0.5999700864156088
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.1653072834014893,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.65175834774971,
                  "rejected_mean_error": 2.200701779127121,
                  "gap_rejected_minus_accepted": 0.5489434313774111
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.9431493282318115,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4552192902565002,
                  "rejected_mean_error": 2.083233654499054,
                  "gap_rejected_minus_accepted": 0.6280143642425537
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_spatial/quantile_context_gated_q95/model.pt"
      },
      {
        "variant": "quantile_seed_relative_q90",
        "feature_mode": "M4_seed_relative",
        "kind": "mlp_big",
        "q": 0.9,
        "best_epoch": 35,
        "best_calib_pinball": 0.026328200474381447,
        "train_time_sec": 53.72617268562317,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9958114880566679,
              "spearman": 0.9954010725280539,
              "auroc_top30_bad": 0.9974754285714286,
              "mae": 0.24127735098823905,
              "mse": 0.11342180500146619,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9299608688247851,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.035674993582069874
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17382913423478602
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4756798915013671
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8247661547650893
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
              "pearson": 0.997907770373915,
              "spearman": 0.9972553668741488,
              "auroc_top30_worst": 0.9985150476190476,
              "pairwise_seed_ranking": 0.906,
              "predicted_best_mean_error": 1.7760072622597218,
              "seed0_mean_error": 1.850025711297989,
              "random_seed_mean_error": 1.841148916900158,
              "oracle_best_mean_error": 1.7736391132473945,
              "improvement_over_seed0": 0.07401844903826715,
              "gap_to_oracle": 0.002368149012327292,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6047511611580849
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8418549256563187
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.115910261452198
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3621756290197373
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8402536353409291
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.163299083709717,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5682351534432835,
                  "rejected_mean_error": 4.288419972419739,
                  "gap_rejected_minus_accepted": 2.7201848189764553
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.5655938386917114,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3621756290197373,
                  "rejected_mean_error": 3.2744876543045045,
                  "gap_rejected_minus_accepted": 1.9123120252847672
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9238235354423523,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.115910261452198,
                  "rejected_mean_error": 2.56459700922966,
                  "gap_rejected_minus_accepted": 1.448686747777462
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3026725053787231,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8418549256563187,
                  "rejected_mean_error": 2.1730532052357994,
                  "gap_rejected_minus_accepted": 1.3311982795794806
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.149620246887207,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5771077304416232,
                  "rejected_mean_error": 4.30628753900528,
                  "gap_rejected_minus_accepted": 2.7291798085636563
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.607588231563568,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3729054330190023,
                  "rejected_mean_error": 3.2813865461349487,
                  "gap_rejected_minus_accepted": 1.9084811131159465
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9583751559257507,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1222340176105499,
                  "rejected_mean_error": 2.577817404985428,
                  "gap_rejected_minus_accepted": 1.455583387374878
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.308429330587387,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8454143152236938,
                  "rejected_mean_error": 2.1848961766560873,
                  "gap_rejected_minus_accepted": 1.3394818614323936
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9870470433555962,
              "spearman": 0.9830169712008675,
              "auroc_top30_bad": 0.9970422857142858,
              "mae": 0.169562470176816,
              "mse": 0.04466611563211072,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.976,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7816532649966834,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08257559323310852
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17101200330257416
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.40955154081583023
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7754319301366807
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
              "pearson": 0.9764289200137907,
              "spearman": 0.9843630246163358,
              "auroc_top30_worst": 0.9965440000000001,
              "pairwise_seed_ranking": 0.902,
              "predicted_best_mean_error": 1.5613877606391906,
              "seed0_mean_error": 1.6587522393465042,
              "random_seed_mean_error": 1.6395123422145843,
              "oracle_best_mean_error": 1.5591331604719163,
              "improvement_over_seed0": 0.09736447870731357,
              "gap_to_oracle": 0.002254600167274301,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47126230573654176
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7866174001724292
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0951178009033202
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3441728478047386
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6363912368774414
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9141977548599245,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5002285639444988,
                  "rejected_mean_error": 2.861855293273926,
                  "gap_rejected_minus_accepted": 1.361626729329427
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3007266521453857,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3434026717121852,
                  "rejected_mean_error": 2.513484800966403,
                  "gap_rejected_minus_accepted": 1.1700821292542178
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7547626495361328,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0951178009033202,
                  "rejected_mean_error": 2.1776646728515625,
                  "gap_rejected_minus_accepted": 1.0825468719482423
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2770571410655975,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7872708476008698,
                  "rejected_mean_error": 1.9200355077883986,
                  "gap_rejected_minus_accepted": 1.1327646601875287
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.934963035583496,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5189524281024933,
                  "rejected_mean_error": 2.9169505405426026,
                  "gap_rejected_minus_accepted": 1.3979981124401093
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3608843088150024,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3603951894344493,
                  "rejected_mean_error": 2.5443517367045083,
                  "gap_rejected_minus_accepted": 1.183956547270059
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7705755233764648,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1136968519687653,
                  "rejected_mean_error": 2.203807626724243,
                  "gap_rejected_minus_accepted": 1.0901107747554777
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.308840125799179,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8020414847230154,
                  "rejected_mean_error": 1.9473767181768775,
                  "gap_rejected_minus_accepted": 1.1453352334538622
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9799084193363675,
              "spearman": 0.9767839521413312,
              "auroc_top30_bad": 0.9878438095238097,
              "mae": 0.21288887679874896,
              "mse": 0.07097290364757117,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7851210314625962,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08692971247434617
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18410402628183364
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5770888555943966
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9617123976031939
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
              "pearson": 0.9506925666288546,
              "spearman": 0.9544294512128525,
              "auroc_top30_worst": 0.9639740952380953,
              "pairwise_seed_ranking": 0.8876,
              "predicted_best_mean_error": 1.7462085065841675,
              "seed0_mean_error": 1.8436008858680726,
              "random_seed_mean_error": 1.808576955795288,
              "oracle_best_mean_error": 1.7398507182598113,
              "improvement_over_seed0": 0.0973923792839051,
              "gap_to_oracle": 0.006357788324356184,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9067788543701172
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1906512030042136
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4446414298057557
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6136942936032057
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114040771961213
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.763596177101136,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.728356228351593,
                  "rejected_mean_error": 2.558834716796875,
                  "gap_rejected_minus_accepted": 0.8304784884452818
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4145001769065857,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6130291720337395,
                  "rejected_mean_error": 2.4052612214042735,
                  "gap_rejected_minus_accepted": 0.7922320493705339
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0511348247528076,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4446414298057557,
                  "rejected_mean_error": 2.178166724586487,
                  "gap_rejected_minus_accepted": 0.7335252947807311
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6968007385730743,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1916026792968044,
                  "rejected_mean_error": 2.0184455260141427,
                  "gap_rejected_minus_accepted": 0.8268428467173383
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.827324724197388,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.750671526061164,
                  "rejected_mean_error": 2.679965124130249,
                  "gap_rejected_minus_accepted": 0.9292935980690848
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.451366662979126,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6241492970104523,
                  "rejected_mean_error": 2.4949889353343417,
                  "gap_rejected_minus_accepted": 0.8708396383238894
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0837303400039673,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4514679012298584,
                  "rejected_mean_error": 2.235733870506287,
                  "gap_rejected_minus_accepted": 0.7842659692764284
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7282366752624512,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1915696367384896,
                  "rejected_mean_error": 2.063269167660392,
                  "gap_rejected_minus_accepted": 0.8716995309219022
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9853552227420179,
              "spearman": 0.9712141683478802,
              "auroc_top30_bad": 0.9700916666666667,
              "mae": 0.1743444469552487,
              "mse": 0.04531234015540655,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8066159444375097,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08232159845530987
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17336530411988496
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6662963241375983
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0570301612243056
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
              "pearson": 0.9357850468239686,
              "spearman": 0.91995547995548,
              "auroc_top30_worst": 0.9542238095238095,
              "pairwise_seed_ranking": 0.8655,
              "predicted_best_mean_error": 1.8699541041254997,
              "seed0_mean_error": 1.9262300634384155,
              "random_seed_mean_error": 1.9081436988711358,
              "oracle_best_mean_error": 1.863301387131214,
              "improvement_over_seed0": 0.056275959312915846,
              "gap_to_oracle": 0.006652716994285601,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.308793820142746
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4583390884399414
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6521649179458617
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7663123515446981
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9147616970539092
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.73690128326416,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8477939279874165,
                  "rejected_mean_error": 2.5174716186523436,
                  "gap_rejected_minus_accepted": 0.6696776906649271
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3310129642486572,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.7663123515446981,
                  "rejected_mean_error": 2.360109733581543,
                  "gap_rejected_minus_accepted": 0.593797382036845
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0771011114120483,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6521649179458617,
                  "rejected_mean_error": 2.177358476161957,
                  "gap_rejected_minus_accepted": 0.5251935582160951
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7728623747825623,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4583390884399414,
                  "rejected_mean_error": 2.0669025665918985,
                  "gap_rejected_minus_accepted": 0.6085634781519571
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7570748805999754,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 1.8603327552477518,
                  "rejected_mean_error": 2.5193058371543886,
                  "gap_rejected_minus_accepted": 0.6589730819066368
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3486499786376953,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.7775128928820292,
                  "rejected_mean_error": 2.3723815751075743,
                  "gap_rejected_minus_accepted": 0.5948686822255451
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.079041361808777,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6596000826358794,
                  "rejected_mean_error": 2.1928600442409514,
                  "gap_rejected_minus_accepted": 0.5332599616050719
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.789811909198761,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4611196756362914,
                  "rejected_mean_error": 2.081266859372457,
                  "gap_rejected_minus_accepted": 0.6201471837361656
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_spatial/quantile_seed_relative_q90/model.pt"
      }
    ],
    "holdout_libero_goal": [
      {
        "variant": "quantile_action_q80",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.8,
        "best_epoch": 116,
        "best_calib_pinball": 0.13973967730998993,
        "train_time_sec": 16.02336096763611,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9642597698005075,
              "spearman": 0.9252831462966562,
              "auroc_top30_bad": 0.9984717142857142,
              "mae": 0.15787462311834097,
              "mse": 0.084940937091,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.479,
              "expert_lt_simvla_seed0": 0.91,
              "same_context_pred_std": 0.6663586145463433,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2569888182580471
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3466326250016689
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.49550345828831194
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8185446386039257
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2307025221720338
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9984761089018849,
              "spearman": 0.9978680497226194,
              "auroc_top30_worst": 0.9979459047619047,
              "pairwise_seed_ranking": 0.8266,
              "predicted_best_mean_error": 1.6948852023482324,
              "seed0_mean_error": 1.7593383036255836,
              "random_seed_mean_error": 1.748514448583126,
              "oracle_best_mean_error": 1.6850638110637666,
              "improvement_over_seed0": 0.06445310127735127,
              "gap_to_oracle": 0.009821391284465797,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6118024873137474
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8485033009767532
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1109555907845496
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3370813981453578
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7487053180277348
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.960425829887392,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4978049512505531,
                  "rejected_mean_error": 4.00680861902237,
                  "gap_rejected_minus_accepted": 2.5090036677718164
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.083085775375366,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3370813981453578,
                  "rejected_mean_error": 2.9835770776748656,
                  "gap_rejected_minus_accepted": 1.6464956795295078
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6613144874572754,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1109555907845496,
                  "rejected_mean_error": 2.3864550452709197,
                  "gap_rejected_minus_accepted": 1.27549945448637
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1937140822410583,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8485033009767532,
                  "rejected_mean_error": 2.0487726570447284,
                  "gap_rejected_minus_accepted": 1.2002693560679751
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9798237800598146,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5082038819127612,
                  "rejected_mean_error": 4.0195480990409855,
                  "gap_rejected_minus_accepted": 2.511344217128224
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0902934074401855,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.347422726869583,
                  "rejected_mean_error": 2.9950850338935853,
                  "gap_rejected_minus_accepted": 1.6476623070240022
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6753867268562317,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.117384712100029,
                  "rejected_mean_error": 2.401291895151138,
                  "gap_rejected_minus_accepted": 1.283907183051109
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2065183818340302,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.852458931684494,
                  "rejected_mean_error": 2.061631427605947,
                  "gap_rejected_minus_accepted": 1.209172495921453
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8335677030539306,
              "spearman": 0.8579364398962541,
              "auroc_top30_bad": 0.9366887619047619,
              "mae": 0.3678934239566326,
              "mse": 0.2451931822395548,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 0.948,
              "same_context_pred_std": 0.6120068467585056,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2639543692469597
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3154522451519966
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.474356567132473
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8479115984360377
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1699017732203008
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.677902806111131,
              "spearman": 0.7268277486257593,
              "auroc_top30_worst": 0.846016,
              "pairwise_seed_ranking": 0.7764,
              "predicted_best_mean_error": 1.6066580971479416,
              "seed0_mean_error": 1.6905601416826248,
              "random_seed_mean_error": 1.6723020417690277,
              "oracle_best_mean_error": 1.5885274814367294,
              "improvement_over_seed0": 0.0839020445346832,
              "gap_to_oracle": 0.018130615711212217,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6005413281917572
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9435702103834885
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2623135800361633
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.452129296084711
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6684940560817718
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9208067655563354,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5984840818511115,
                  "rejected_mean_error": 2.298583824157715,
                  "gap_rejected_minus_accepted": 0.7000997423066033
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1074586510658264,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4513695526911838,
                  "rejected_mean_error": 2.3184801892350655,
                  "gap_rejected_minus_accepted": 0.8671106365438817
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6702316403388977,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2623135800361633,
                  "rejected_mean_error": 2.0746745321273803,
                  "gap_rejected_minus_accepted": 0.812360952091217
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.181931585073471,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9459155645614234,
                  "rejected_mean_error": 1.9098676610400098,
                  "gap_rejected_minus_accepted": 0.9639520964785864
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9562183380126954,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.623222012122472,
                  "rejected_mean_error": 2.296603307723999,
                  "gap_rejected_minus_accepted": 0.6733812956015268
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1537966132164,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4867007325996051,
                  "rejected_mean_error": 2.295666641659207,
                  "gap_rejected_minus_accepted": 0.8089659090596018
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.713939368724823,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2788455011844635,
                  "rejected_mean_error": 2.1022747821807863,
                  "gap_rejected_minus_accepted": 0.8234292809963228
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2266065180301666,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.959498136289536,
                  "rejected_mean_error": 1.9368537584728098,
                  "gap_rejected_minus_accepted": 0.9773556221832739
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.858023150187189,
              "spearman": 0.8475976728140772,
              "auroc_top30_bad": 0.9304548571428571,
              "mae": 0.30721084851920605,
              "mse": 0.19579582524534567,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 0.956,
              "same_context_pred_std": 0.6076929026996873,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.29222067672014235
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4008624934196472
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5837795307934284
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9853454732378324
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2670785710781813
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7355244484217136,
              "spearman": 0.7325862347431904,
              "auroc_top30_worst": 0.8150095238095239,
              "pairwise_seed_ranking": 0.7804,
              "predicted_best_mean_error": 1.7788283573389054,
              "seed0_mean_error": 1.8668941221237183,
              "random_seed_mean_error": 1.8321932954788207,
              "oracle_best_mean_error": 1.7580343310832978,
              "improvement_over_seed0": 0.08806576478481287,
              "gap_to_oracle": 0.020794026255607667,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0331769914627076
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2767350375652313
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5299201091766357
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7019858984931955
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8333799670696258
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3491258144378664,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.780136449654897,
                  "rejected_mean_error": 2.312571623802185,
                  "gap_rejected_minus_accepted": 0.5324351741472881
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1005138158798218,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7016537529808988,
                  "rejected_mean_error": 2.2277169082873165,
                  "gap_rejected_minus_accepted": 0.5260631553064177
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8228188753128052,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5299201091766357,
                  "rejected_mean_error": 2.136839824962616,
                  "gap_rejected_minus_accepted": 0.6069197157859805
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5036779940128326,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2775277135471186,
                  "rejected_mean_error": 2.0190595352153515,
                  "gap_rejected_minus_accepted": 0.741531821668233
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4334587812423703,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8076635111702812,
                  "rejected_mean_error": 2.399969620704651,
                  "gap_rejected_minus_accepted": 0.5923061095343696
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1160741448402405,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7114863287318836,
                  "rejected_mean_error": 2.328183921556624,
                  "gap_rejected_minus_accepted": 0.6166975928247405
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8546092510223389,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5316804094314576,
                  "rejected_mean_error": 2.202107834815979,
                  "gap_rejected_minus_accepted": 0.6704274253845213
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5424074530601501,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2932473383252583,
                  "rejected_mean_error": 2.0601548032964616,
                  "gap_rejected_minus_accepted": 0.7669074649712033
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.8882062973141636,
              "spearman": 0.8700981970726339,
              "auroc_top30_bad": 0.9376369047619046,
              "mae": 0.35821868672966956,
              "mse": 0.27954473082136827,
              "expert_lt_perturb_large": 0.99,
              "expert_lt_other_task": 0.495,
              "expert_lt_simvla_seed0": 0.97,
              "same_context_pred_std": 0.668215166277268,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.30363055773079395
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4451194444596767
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7890501139312982
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1266290078858534
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.8607824349015514,
              "spearman": 0.7664183144183144,
              "auroc_top30_worst": 0.8709809523809524,
              "pairwise_seed_ranking": 0.7345,
              "predicted_best_mean_error": 2.2635816606879233,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.0630507555603983,
              "gap_to_oracle": 0.022171136140823222,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4872326707839967
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.7161834626197814
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.806988400220871
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8742940382957458
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.519568920135499,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.13996114982499,
                  "rejected_mean_error": 3.9475605392456057,
                  "gap_rejected_minus_accepted": 1.8075993894206155
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3420276045799255,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8742940382957458,
                  "rejected_mean_error": 3.6600022401809693,
                  "gap_rejected_minus_accepted": 1.7857082018852235
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8005865812301636,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.806988400220871,
                  "rejected_mean_error": 2.8344537773132323,
                  "gap_rejected_minus_accepted": 1.0274653770923614
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3898135423660278,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.7161834626197814,
                  "rejected_mean_error": 2.522233630816142,
                  "gap_rejected_minus_accepted": 0.8060501681963606
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.656529259681702,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1488088766733804,
                  "rejected_mean_error": 3.9270442724227905,
                  "gap_rejected_minus_accepted": 1.7782353957494101
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3547245264053345,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8847774871190388,
                  "rejected_mean_error": 3.6521972036361694,
                  "gap_rejected_minus_accepted": 1.7674197165171306
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.843075931072235,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8240246069431305,
                  "rejected_mean_error": 2.8292402255535127,
                  "gap_rejected_minus_accepted": 1.0052156186103822
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4244908392429352,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.708865990638733,
                  "rejected_mean_error": 2.5325545581181843,
                  "gap_rejected_minus_accepted": 0.8236885674794514
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_goal/quantile_action_q80/model.pt"
      },
      {
        "variant": "quantile_action_q90",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.9,
        "best_epoch": 98,
        "best_calib_pinball": 0.10591110587120056,
        "train_time_sec": 15.962323904037476,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9509542987742341,
              "spearman": 0.9043682084439432,
              "auroc_top30_bad": 0.9974861904761906,
              "mae": 0.2146607276260853,
              "mse": 0.1323134946082799,
              "expert_lt_perturb_large": 0.999,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.863,
              "same_context_pred_std": 0.6779268242260289,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2587966228425503
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3687548659205437
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5238207782417535
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8188495914638042
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2307025221720338
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9975709332830515,
              "spearman": 0.9960770216670807,
              "auroc_top30_worst": 0.995767238095238,
              "pairwise_seed_ranking": 0.7869,
              "predicted_best_mean_error": 1.6996401908099652,
              "seed0_mean_error": 1.7593383036255836,
              "random_seed_mean_error": 1.748514448583126,
              "oracle_best_mean_error": 1.6850638110637666,
              "improvement_over_seed0": 0.05969811281561843,
              "gap_to_oracle": 0.014576379746198631,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6113123530745507
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8484051489114761
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.11203860155344
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3379368209282556
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7487053180277348
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.103960108757019,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4980952675143877,
                  "rejected_mean_error": 4.004195772647858,
                  "gap_rejected_minus_accepted": 2.50610050513347
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1075040102005005,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3379368209282556,
                  "rejected_mean_error": 2.981010809326172,
                  "gap_rejected_minus_accepted": 1.6430739883979162
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6799331903457642,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.11203860155344,
                  "rejected_mean_error": 2.3853720345020295,
                  "gap_rejected_minus_accepted": 1.2733334329485895
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1971525251865387,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8484051489114761,
                  "rejected_mean_error": 2.048805374399821,
                  "gap_rejected_minus_accepted": 1.200400225488345
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.113739347457886,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5085630120833715,
                  "rejected_mean_error": 4.016315927505493,
                  "gap_rejected_minus_accepted": 2.507752915422122
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1324023604393005,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.348640400648117,
                  "rejected_mean_error": 2.991432012557983,
                  "gap_rejected_minus_accepted": 1.6427916119098662
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7022141814231873,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1179824405908585,
                  "rejected_mean_error": 2.4006941666603088,
                  "gap_rejected_minus_accepted": 1.2827117260694503
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2117199003696442,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8523563458919525,
                  "rejected_mean_error": 2.0616656228701276,
                  "gap_rejected_minus_accepted": 1.209309276978175
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8433651055434968,
              "spearman": 0.8504781600647656,
              "auroc_top30_bad": 0.9473417142857143,
              "mae": 0.3693149064719677,
              "mse": 0.2493759912078697,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.932,
              "same_context_pred_std": 0.5977183102487065,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.27128435665369033
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3116513702869415
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4676145855545998
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8411839201847712
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1699017732203008
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7410856451572745,
              "spearman": 0.7678072533806423,
              "auroc_top30_worst": 0.857462857142857,
              "pairwise_seed_ranking": 0.7708,
              "predicted_best_mean_error": 1.6077681399583816,
              "seed0_mean_error": 1.6905601416826248,
              "random_seed_mean_error": 1.6723020417690277,
              "oracle_best_mean_error": 1.5885274814367294,
              "improvement_over_seed0": 0.08279200172424317,
              "gap_to_oracle": 0.019240658521652243,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.54415944647789
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8891452713272511
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.235552044582367
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4399769169562406
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6684940560817718
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.725685214996338,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6006936767896016,
                  "rejected_mean_error": 2.278697469711304,
                  "gap_rejected_minus_accepted": 0.6780037929217022
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1085919737815857,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4392853369071619,
                  "rejected_mean_error": 2.354655621150812,
                  "gap_rejected_minus_accepted": 0.91537028424365
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6831077337265015,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.235552044582367,
                  "rejected_mean_error": 2.1014360675811767,
                  "gap_rejected_minus_accepted": 0.8658840229988098
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3231568038463593,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8891644076036569,
                  "rejected_mean_error": 1.9288250912724336,
                  "gap_rejected_minus_accepted": 1.0396606836687767
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7785946130752563,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6269858615928225,
                  "rejected_mean_error": 2.262728662490845,
                  "gap_rejected_minus_accepted": 0.6357428008980224
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1573017835617065,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.47011415923343,
                  "rejected_mean_error": 2.3448998038730924,
                  "gap_rejected_minus_accepted": 0.8747856446396625
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7383689880371094,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.256170221567154,
                  "rejected_mean_error": 2.1249500617980956,
                  "gap_rejected_minus_accepted": 0.8687798402309417
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3727085292339325,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.901774570582405,
                  "rejected_mean_error": 1.9563007351548913,
                  "gap_rejected_minus_accepted": 1.0545261645724864
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8304692202318384,
              "spearman": 0.824352858112038,
              "auroc_top30_bad": 0.9210689523809523,
              "mae": 0.3552382563918829,
              "mse": 0.24934998921654306,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.512,
              "expert_lt_simvla_seed0": 0.924,
              "same_context_pred_std": 0.6015402880401663,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3199993227720261
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.40176430662870405
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5972537915170193
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9973146748185158
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2670785710781813
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7176119641081607,
              "spearman": 0.6934537465943978,
              "auroc_top30_worst": 0.8162438095238095,
              "pairwise_seed_ranking": 0.7472,
              "predicted_best_mean_error": 1.7825045605897905,
              "seed0_mean_error": 1.8668941221237183,
              "random_seed_mean_error": 1.8321932954788207,
              "oracle_best_mean_error": 1.7580343310832978,
              "improvement_over_seed0": 0.08438956153392785,
              "gap_to_oracle": 0.02447022950649269,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0342323369979858
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3132643518157494
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5455672388076782
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7081783268370354
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8333799670696258
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4961670398712164,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7773955567147997,
                  "rejected_mean_error": 2.3372396602630614,
                  "gap_rejected_minus_accepted": 0.5598441035482618
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1370262503623962,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7084083382195316,
                  "rejected_mean_error": 2.2074963128604828,
                  "gap_rejected_minus_accepted": 0.4990879746409511
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8506783843040466,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5455672388076782,
                  "rejected_mean_error": 2.1211926953315734,
                  "gap_rejected_minus_accepted": 0.5756254565238952
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5468016862869263,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3136596734912251,
                  "rejected_mean_error": 2.0069898410184406,
                  "gap_rejected_minus_accepted": 0.6933301675272154
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5077483177185056,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8060125652949015,
                  "rejected_mean_error": 2.414828133583069,
                  "gap_rejected_minus_accepted": 0.6088155682881675
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1758415699005127,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7201469939022778,
                  "rejected_mean_error": 2.3024768677968828,
                  "gap_rejected_minus_accepted": 0.582329873894605
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.876247525215149,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5447093143463135,
                  "rejected_mean_error": 2.189078929901123,
                  "gap_rejected_minus_accepted": 0.6443696155548095
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5967470109462738,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3179781947817122,
                  "rejected_mean_error": 2.051823017431453,
                  "gap_rejected_minus_accepted": 0.7338448226497407
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.8596281043729341,
              "spearman": 0.8362178928233013,
              "auroc_top30_bad": 0.913372619047619,
              "mae": 0.3991386907622218,
              "mse": 0.32960697645278014,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.525,
              "expert_lt_simvla_seed0": 0.96,
              "same_context_pred_std": 0.6870858379185495,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3374118942767382
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.45347637322545054
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8405052818804979
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.130720628798008
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.8220589152331319,
              "spearman": 0.7020987780987781,
              "auroc_top30_worst": 0.8540238095238095,
              "pairwise_seed_ranking": 0.7185,
              "predicted_best_mean_error": 2.2671928688883782,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.05943954735994339,
              "gap_to_oracle": 0.02578234434127813,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.7844773304462433
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.7795606684684753
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8154981164932251
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8748325397173564
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.6447027206420897,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.1407994904783036,
                  "rejected_mean_error": 3.9400154733657837,
                  "gap_rejected_minus_accepted": 1.79921598288748
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.5506505966186523,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8748325397173564,
                  "rejected_mean_error": 3.6583867359161375,
                  "gap_rejected_minus_accepted": 1.783554196198781
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8542909026145935,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.8154981164932251,
                  "rejected_mean_error": 2.8259440610408784,
                  "gap_rejected_minus_accepted": 1.0104459445476532
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3544821739196777,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.7795606684684753,
                  "rejected_mean_error": 2.5011078955332438,
                  "gap_rejected_minus_accepted": 0.7215472270647685
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.688776087760925,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1497670398818123,
                  "rejected_mean_error": 3.9184208035469057,
                  "gap_rejected_minus_accepted": 1.7686537636650934
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.5599759817123413,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8838839912414551,
                  "rejected_mean_error": 3.6548776912689207,
                  "gap_rejected_minus_accepted": 1.7709937000274656
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8903956413269043,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.834123011827469,
                  "rejected_mean_error": 2.819141820669174,
                  "gap_rejected_minus_accepted": 0.9850188088417051
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3998274207115173,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.7714293432235717,
                  "rejected_mean_error": 2.5117001072565714,
                  "gap_rejected_minus_accepted": 0.7402707640329997
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_goal/quantile_action_q90/model.pt"
      },
      {
        "variant": "quantile_action_q95",
        "feature_mode": "A0_action_flat",
        "kind": "mlp",
        "q": 0.95,
        "best_epoch": 1,
        "best_calib_pinball": 0.07776877284049988,
        "train_time_sec": 15.999780893325806,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8312261291940681,
              "spearman": 0.7234333234089689,
              "auroc_top30_bad": 0.918071380952381,
              "mae": 0.7141999198660255,
              "mse": 0.7743552424307681,
              "expert_lt_perturb_large": 0.974,
              "expert_lt_other_task": 0.491,
              "expert_lt_simvla_seed0": 0.949,
              "same_context_pred_std": 0.6255193174289875,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4846073392182589
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.48921174591183664
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6639832836121321
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8811043442030748
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2307025221720338
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9047254411494021,
              "spearman": 0.8097049435276307,
              "auroc_top30_worst": 0.9144721904761905,
              "pairwise_seed_ranking": 0.6004,
              "predicted_best_mean_error": 1.7264597810804845,
              "seed0_mean_error": 1.7593383036255836,
              "random_seed_mean_error": 1.748514448583126,
              "oracle_best_mean_error": 1.6850638110637666,
              "improvement_over_seed0": 0.032878522545099154,
              "gap_to_oracle": 0.04139597001671791,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6780743158459663
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.985166864323616
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2140235980153085
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3761351547002791
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7487053180277348
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.7829781055450473,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.5081227826608552,
                  "rejected_mean_error": 3.9139481363296507,
                  "gap_rejected_minus_accepted": 2.4058253536687957
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7176669239997864,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3761351547002791,
                  "rejected_mean_error": 2.8664158080101014,
                  "gap_rejected_minus_accepted": 1.4902806533098223
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0030382871627808,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.2140235980153085,
                  "rejected_mean_error": 2.283387038040161,
                  "gap_rejected_minus_accepted": 1.0693634400248526
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5284229218959808,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.985166864323616,
                  "rejected_mean_error": 2.0032181359291075,
                  "gap_rejected_minus_accepted": 1.0180512716054915
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.7819876670837407,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.516453882124689,
                  "rejected_mean_error": 3.9452980971336364,
                  "gap_rejected_minus_accepted": 2.4288442150089473
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7704424262046814,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3870211026668549,
                  "rejected_mean_error": 2.87628990650177,
                  "gap_rejected_minus_accepted": 1.4892688038349151
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.004992127418518,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.2258516904115677,
                  "rejected_mean_error": 2.2928249168395998,
                  "gap_rejected_minus_accepted": 1.066973226428032
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.54109126329422,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.9826971569061279,
                  "rejected_mean_error": 2.0182186858654023,
                  "gap_rejected_minus_accepted": 1.0355215289592743
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.7484086624068558,
              "spearman": 0.7386352726699715,
              "auroc_top30_bad": 0.898311619047619,
              "mae": 0.7008474667012692,
              "mse": 0.7230660497100474,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.96,
              "same_context_pred_std": 0.6157185945446954,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.38920673030614855
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.41045537580251695
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6115500354409218
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8677052929957708
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1699017732203008
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6647236851764704,
              "spearman": 0.6470661728423506,
              "auroc_top30_worst": 0.8376350476190476,
              "pairwise_seed_ranking": 0.6064,
              "predicted_best_mean_error": 1.633594081401825,
              "seed0_mean_error": 1.6905601416826248,
              "random_seed_mean_error": 1.6723020417690277,
              "oracle_best_mean_error": 1.5885274814367294,
              "improvement_over_seed0": 0.05696606028079976,
              "gap_to_oracle": 0.045066599965095655,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7780401291847229
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1278858981453455
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3074107751846313
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4671882241646619
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6684940560817718
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.579470634460449,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5645650412771437,
                  "rejected_mean_error": 2.603855189323425,
                  "gap_rejected_minus_accepted": 1.0392901480462815
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6530396938323975,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4666695175583107,
                  "rejected_mean_error": 2.272678057987469,
                  "gap_rejected_minus_accepted": 0.8060085404291584
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8380812406539917,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3074107751846313,
                  "rejected_mean_error": 2.0295773369789125,
                  "gap_rejected_minus_accepted": 0.7221665617942812
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.471076637506485,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1291028624906327,
                  "rejected_mean_error": 1.848674892361416,
                  "gap_rejected_minus_accepted": 0.7195720298707833
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.6052037715911864,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.587304674386978,
                  "rejected_mean_error": 2.6198593473434446,
                  "gap_rejected_minus_accepted": 1.0325546729564665
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7038000226020813,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4868984976235557,
                  "rejected_mean_error": 2.2950796248420837,
                  "gap_rejected_minus_accepted": 0.808181127218528
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9048981666564941,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3191163294315338,
                  "rejected_mean_error": 2.062003953933716,
                  "gap_rejected_minus_accepted": 0.742887624502182
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5099488198757172,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1121369699637096,
                  "rejected_mean_error": 1.885429980283115,
                  "gap_rejected_minus_accepted": 0.7732930103194053
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6935545987923233,
              "spearman": 0.699292922534995,
              "auroc_top30_bad": 0.8385820952380952,
              "mae": 0.7265003634244204,
              "mse": 0.8376840824455208,
              "expert_lt_perturb_large": 0.956,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.956,
              "same_context_pred_std": 0.5709514633531139,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.40396682697534564
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4339938093304634
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7535722788631916
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0374317407806715
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2670785710781813
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6418714270911191,
              "spearman": 0.5423559167717867,
              "auroc_top30_worst": 0.8159085714285715,
              "pairwise_seed_ranking": 0.636,
              "predicted_best_mean_error": 1.7987253551483153,
              "seed0_mean_error": 1.8668941221237183,
              "random_seed_mean_error": 1.8321932954788207,
              "oracle_best_mean_error": 1.7580343310832978,
              "improvement_over_seed0": 0.06816876697540297,
              "gap_to_oracle": 0.04069102406501757,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0280258193016052
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3996361860862145
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6221409921646117
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7299536766528067
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8333799670696258
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2600890398025517,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7643348200056288,
                  "rejected_mean_error": 2.4547862906455995,
                  "gap_rejected_minus_accepted": 0.6904514706399707
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6353434324264526,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.729293973875911,
                  "rejected_mean_error": 2.1449728604322806,
                  "gap_rejected_minus_accepted": 0.41567888655636964
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.2468459606170654,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.6221409921646117,
                  "rejected_mean_error": 2.04461894197464,
                  "gap_rejected_minus_accepted": 0.4224779498100282
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7243480384349823,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.4006534315907537,
                  "rejected_mean_error": 1.9779300264131552,
                  "gap_rejected_minus_accepted": 0.5772765948224015
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.32215895652771,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.786987732251485,
                  "rejected_mean_error": 2.5860516309738157,
                  "gap_rejected_minus_accepted": 0.7990638987223306
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6607178449630737,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7312620259861258,
                  "rejected_mean_error": 2.269484629706731,
                  "gap_rejected_minus_accepted": 0.5382226037206053
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.288563847541809,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6273926420211793,
                  "rejected_mean_error": 2.1063956022262573,
                  "gap_rejected_minus_accepted": 0.47900296020507804
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7799945175647736,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.4221812051440041,
                  "rejected_mean_error": 2.0167171904110015,
                  "gap_rejected_minus_accepted": 0.5945359852669974
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.8224518831147567,
              "spearman": 0.7525691027235892,
              "auroc_top30_bad": 0.9028142857142857,
              "mae": 0.7416135542392731,
              "mse": 0.8593721039015504,
              "expert_lt_perturb_large": 0.96,
              "expert_lt_other_task": 0.53,
              "expert_lt_simvla_seed0": 0.995,
              "same_context_pred_std": 0.6603686386855259,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5930278781056404
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6374511144757271
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8844388967752457
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1526337009966374
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.8796698471615587,
              "spearman": 0.7195836115836116,
              "auroc_top30_worst": 0.9150142857142858,
              "pairwise_seed_ranking": 0.6265,
              "predicted_best_mean_error": 2.278157742321491,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.04847467392683047,
              "gap_to_oracle": 0.03674721777439105,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4949775958061218
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.680369972229004
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8400940794944762
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8762238799730937
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.6733198165893555,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.129888526201248,
                  "rejected_mean_error": 4.038214151859283,
                  "gap_rejected_minus_accepted": 1.9083256256580352
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.206229865550995,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8762238799730937,
                  "rejected_mean_error": 3.6542127151489256,
                  "gap_rejected_minus_accepted": 1.777988835175832
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.276083827018738,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.8400940794944762,
                  "rejected_mean_error": 2.801348098039627,
                  "gap_rejected_minus_accepted": 0.9612540185451508
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.9687698185443878,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.680369972229004,
                  "rejected_mean_error": 2.5341714609464008,
                  "gap_rejected_minus_accepted": 0.8538014887173968
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.788230228424072,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1374959058231777,
                  "rejected_mean_error": 4.028861010074616,
                  "gap_rejected_minus_accepted": 1.8913651042514381
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.251944124698639,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.886417802174886,
                  "rejected_mean_error": 3.647276258468628,
                  "gap_rejected_minus_accepted": 1.760858456293742
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.290297508239746,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.8517167913913726,
                  "rejected_mean_error": 2.8015480411052702,
                  "gap_rejected_minus_accepted": 0.9498312497138977
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.9465186595916748,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.6275424289703369,
                  "rejected_mean_error": 2.5596624120076497,
                  "gap_rejected_minus_accepted": 0.9321199830373128
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_goal/quantile_action_q95/model.pt"
      },
      {
        "variant": "quantile_context_gated_q80",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.8,
        "best_epoch": 85,
        "best_calib_pinball": 0.04212871566414833,
        "train_time_sec": 51.00488066673279,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9988579970690118,
              "spearman": 0.9982112042304655,
              "auroc_top30_bad": 0.9992565476190477,
              "mae": 0.0836603248752188,
              "mse": 0.009678374964518746,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7978855705357253,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0014601670205593108
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17460664539933204
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.47821619918644426
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8176140153427919
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2307025221720338
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9992448303990435,
              "spearman": 0.9988396831855315,
              "auroc_top30_worst": 0.9994411428571428,
              "pairwise_seed_ranking": 0.9201,
              "predicted_best_mean_error": 1.6867326594293117,
              "seed0_mean_error": 1.7593383036255836,
              "random_seed_mean_error": 1.748514448583126,
              "oracle_best_mean_error": 1.6850638110637666,
              "improvement_over_seed0": 0.07260564419627191,
              "gap_to_oracle": 0.0016688483655451503,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6094049752354622
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8478390307664871
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1106596230149268
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.336806177051862
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7487053180277348
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9414949655532845,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4976797432965703,
                  "rejected_mean_error": 4.007935490608215,
                  "gap_rejected_minus_accepted": 2.510255747311645
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1006566286087036,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.336806177051862,
                  "rejected_mean_error": 2.984402740955353,
                  "gap_rejected_minus_accepted": 1.6475965639034909
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.703253984451294,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1106596230149268,
                  "rejected_mean_error": 2.3867510130405427,
                  "gap_rejected_minus_accepted": 1.276091390025616
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.247879832983017,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8478390307664871,
                  "rejected_mean_error": 2.048994080448151,
                  "gap_rejected_minus_accepted": 1.2011550496816636
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.942047715187073,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5080162266227934,
                  "rejected_mean_error": 4.021236996650696,
                  "gap_rejected_minus_accepted": 2.513220770027903
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.107294201850891,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3470882400671642,
                  "rejected_mean_error": 2.9960884943008423,
                  "gap_rejected_minus_accepted": 1.6490002542336781
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7149481773376465,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1172542186975478,
                  "rejected_mean_error": 2.4014223885536192,
                  "gap_rejected_minus_accepted": 1.2841681698560714
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2552888095378876,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8514703333377838,
                  "rejected_mean_error": 2.0619609603881837,
                  "gap_rejected_minus_accepted": 1.2104906270504
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9797409787789438,
              "spearman": 0.9841309238163732,
              "auroc_top30_bad": 0.9931954285714285,
              "mae": 0.137490660219267,
              "mse": 0.037192954895110736,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7556305460172044,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0601518477499485
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16508409671783447
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4194366378903389
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.80590858288606
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1699017732203008
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9509183134339516,
              "spearman": 0.9753263806248837,
              "auroc_top30_worst": 0.9751649523809525,
              "pairwise_seed_ranking": 0.9264,
              "predicted_best_mean_error": 1.5902628806829453,
              "seed0_mean_error": 1.6905601416826248,
              "random_seed_mean_error": 1.6723020417690277,
              "oracle_best_mean_error": 1.5885274814367294,
              "improvement_over_seed0": 0.1002972609996795,
              "gap_to_oracle": 0.0017353992462159074,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4671887993812561
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7520273788235127
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1169268980979918
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3933660622471686
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6684940560817718
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6039165258407597,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5583493181334602,
                  "rejected_mean_error": 2.659796697616577,
                  "gap_rejected_minus_accepted": 1.1014473794831168
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1593809127807617,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3925864349816117,
                  "rejected_mean_error": 2.494453931388002,
                  "gap_rejected_minus_accepted": 1.1018674964063901
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8307788968086243,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1169268980979918,
                  "rejected_mean_error": 2.220061214065552,
                  "gap_rejected_minus_accepted": 1.10313431596756
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.261444330215454,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7535803038091324,
                  "rejected_mean_error": 1.9741162593489396,
                  "gap_rejected_minus_accepted": 1.2205359555398072
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.621395468711853,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5752283330758412,
                  "rejected_mean_error": 2.728546419143677,
                  "gap_rejected_minus_accepted": 1.1533180860678356
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.182702362537384,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4090459622482565,
                  "rejected_mean_error": 2.5261657219084483,
                  "gap_rejected_minus_accepted": 1.1171197596601918
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8620226979255676,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.132969215631485,
                  "rejected_mean_error": 2.248151067733765,
                  "gap_rejected_minus_accepted": 1.1151818521022798
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2983801066875458,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7658051540927281,
                  "rejected_mean_error": 2.00210861343751,
                  "gap_rejected_minus_accepted": 1.2363034593447817
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9873282865757604,
              "spearman": 0.9857662287043858,
              "auroc_top30_bad": 0.9883123809523809,
              "mae": 0.10819375011324882,
              "mse": 0.02193036099282112,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.7773418390494362,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.02529205673933029
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1670886276125908
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.537293293851614
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9445380430817604
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2670785710781813
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9570245130394576,
              "spearman": 0.9747360893030973,
              "auroc_top30_worst": 0.9826468571428573,
              "pairwise_seed_ranking": 0.9172,
              "predicted_best_mean_error": 1.7604203845262527,
              "seed0_mean_error": 1.8668941221237183,
              "random_seed_mean_error": 1.8321932954788207,
              "oracle_best_mean_error": 1.7580343310832978,
              "improvement_over_seed0": 0.10647373759746559,
              "gap_to_oracle": 0.0023860534429549496,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8795905938148498
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1738836721349986
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4505318671226501
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6407176819818614
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8333799670696258
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3886322736740113,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7503135636117724,
                  "rejected_mean_error": 2.580977598190308,
                  "gap_rejected_minus_accepted": 0.8306640345785354
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1784088015556335,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6401028731716607,
                  "rejected_mean_error": 2.411976251358422,
                  "gap_rejected_minus_accepted": 0.7718733781867615
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.964093565940857,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4505318671226501,
                  "rejected_mean_error": 2.2162280670166017,
                  "gap_rejected_minus_accepted": 0.7656961998939515
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.640334039926529,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1752431032756647,
                  "rejected_mean_error": 2.0532271798417816,
                  "gap_rejected_minus_accepted": 0.8779840765661169
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.458269715309143,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7721442476908367,
                  "rejected_mean_error": 2.7196429920196534,
                  "gap_rejected_minus_accepted": 0.9474987443288168
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2163931131362915,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6530346258438844,
                  "rejected_mean_error": 2.5016834206051297,
                  "gap_rejected_minus_accepted": 0.8486487947612453
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9897711277008057,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4631430282592774,
                  "rejected_mean_error": 2.2706452159881594,
                  "gap_rejected_minus_accepted": 0.8075021877288819
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6826686263084412,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1845610955404857,
                  "rejected_mean_error": 2.096771024127695,
                  "gap_rejected_minus_accepted": 0.9122099285872092
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9893826216040005,
              "spearman": 0.9878729530925017,
              "auroc_top30_bad": 0.9930226190476191,
              "mae": 0.12540354055562056,
              "mse": 0.033521095167371555,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.995,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9198985812674014,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04498210817575455
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2190160081088543
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7038861639499664
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0833018107414245
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9856288780735698,
              "spearman": 0.9886710886710888,
              "auroc_top30_worst": 0.9946095238095238,
              "pairwise_seed_ranking": 0.8655,
              "predicted_best_mean_error": 2.2453212770819664,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08131113916635524,
              "gap_to_oracle": 0.00391075253486628,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3110456228256226
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.483719852924347
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.654364538192749
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.874689033349355
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.051208066940307,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.09512276980612,
                  "rejected_mean_error": 4.3511059594154355,
                  "gap_rejected_minus_accepted": 2.2559831896093154
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.6680119037628174,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.874689033349355,
                  "rejected_mean_error": 3.6588172550201414,
                  "gap_rejected_minus_accepted": 1.7841282216707863
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.07895565032959,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.654364538192749,
                  "rejected_mean_error": 2.9870776393413543,
                  "gap_rejected_minus_accepted": 1.3327131011486053
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.769605964422226,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.483719852924347,
                  "rejected_mean_error": 2.59972150071462,
                  "gap_rejected_minus_accepted": 1.1160016477902732
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.053115987777709,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.694262206554413,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8857139762242634,
                  "rejected_mean_error": 3.6493877363204956,
                  "gap_rejected_minus_accepted": 1.7636737600962322
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.07895565032959,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6711565959453583,
                  "rejected_mean_error": 2.982108236551285,
                  "gap_rejected_minus_accepted": 1.3109516406059267
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7925698161125183,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4968347454071045,
                  "rejected_mean_error": 2.6032316398620607,
                  "gap_rejected_minus_accepted": 1.1063968944549563
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_goal/quantile_context_gated_q80/model.pt"
      },
      {
        "variant": "quantile_context_gated_q90",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.9,
        "best_epoch": 88,
        "best_calib_pinball": 0.032796986401081085,
        "train_time_sec": 51.03184199333191,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.998752475778542,
              "spearman": 0.9977611572863899,
              "auroc_top30_bad": 0.9988565238095238,
              "mae": 0.1292189771946054,
              "mse": 0.02495956217931191,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8282280723211687,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0019249733090400695
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17445836701989173
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4785457492619753
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8178717963079611
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2307025221720338
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9987439722669426,
              "spearman": 0.9990622183224662,
              "auroc_top30_worst": 0.9993988571428571,
              "pairwise_seed_ranking": 0.9002,
              "predicted_best_mean_error": 1.6880659055113791,
              "seed0_mean_error": 1.7593383036255836,
              "random_seed_mean_error": 1.748514448583126,
              "oracle_best_mean_error": 1.6850638110637666,
              "improvement_over_seed0": 0.0712723981142045,
              "gap_to_oracle": 0.003002094447612569,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6089930397868156
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8472877161264419
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1105709311127663
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.336933213686943
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7487053180277348
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.19203658103943,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.497702554338508,
                  "rejected_mean_error": 4.007730191230774,
                  "gap_rejected_minus_accepted": 2.510027636892266
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1969494819641113,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.336933213686943,
                  "rejected_mean_error": 2.9840216310501098,
                  "gap_rejected_minus_accepted": 1.6470884173631668
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7346845269203186,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1105709311127663,
                  "rejected_mean_error": 2.386839704942703,
                  "gap_rejected_minus_accepted": 1.2762687738299368
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.245224267244339,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8472877161264419,
                  "rejected_mean_error": 2.0491778519948323,
                  "gap_rejected_minus_accepted": 1.2018901358683904
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2201325178146365,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.508043487932947,
                  "rejected_mean_error": 4.020991644859314,
                  "gap_rejected_minus_accepted": 2.5129481569263667
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.206877589225769,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3469937158425649,
                  "rejected_mean_error": 2.99637206697464,
                  "gap_rejected_minus_accepted": 1.6493783511320752
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7497138977050781,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1169818538427352,
                  "rejected_mean_error": 2.401694753408432,
                  "gap_rejected_minus_accepted": 1.284712899565697
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2570520043373108,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8509280340671539,
                  "rejected_mean_error": 2.062141726811727,
                  "gap_rejected_minus_accepted": 1.211213692744573
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9689277390915234,
              "spearman": 0.9829229390065013,
              "auroc_top30_bad": 0.9926491428571429,
              "mae": 0.17220493748188018,
              "mse": 0.07124162169789171,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7982380098436714,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.03828797027468681
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16595688166618347
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.41989653669595717
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8062585966189703
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1699017732203008
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.918580868284992,
              "spearman": 0.9683992312315081,
              "auroc_top30_worst": 0.9703923809523809,
              "pairwise_seed_ranking": 0.904,
              "predicted_best_mean_error": 1.591948983669281,
              "seed0_mean_error": 1.6905601416826248,
              "random_seed_mean_error": 1.6723020417690277,
              "oracle_best_mean_error": 1.5885274814367294,
              "improvement_over_seed0": 0.09861115801334375,
              "gap_to_oracle": 0.0034215022325516653,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.467435399055481
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7544286967470095
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1185320038795472
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.394658542454624
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6684940560817718
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7718503713607796,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.581154704146915,
                  "rejected_mean_error": 2.4545482234954834,
                  "gap_rejected_minus_accepted": 0.8733935193485685
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.259115755558014,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3934838067632855,
                  "rejected_mean_error": 2.491767550047975,
                  "gap_rejected_minus_accepted": 1.0982837432846895
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8540626764297485,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1185320038795472,
                  "rejected_mean_error": 2.2184561082839966,
                  "gap_rejected_minus_accepted": 1.0999241044044494
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2179352641105652,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7554975033948977,
                  "rejected_mean_error": 1.9734758287509198,
                  "gap_rejected_minus_accepted": 1.2179783253560221
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.834057354927063,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.605944228834576,
                  "rejected_mean_error": 2.4521033573150635,
                  "gap_rejected_minus_accepted": 0.8461591284804875
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3040369749069214,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.410164535523736,
                  "rejected_mean_error": 2.5228455123447238,
                  "gap_rejected_minus_accepted": 1.1126809768209878
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8903141617774963,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.133450398683548,
                  "rejected_mean_error": 2.247669884681702,
                  "gap_rejected_minus_accepted": 1.1142194859981538
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2402423322200775,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.767091630470185,
                  "rejected_mean_error": 2.0016752016098103,
                  "gap_rejected_minus_accepted": 1.2345835711396251
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9842958758802811,
              "spearman": 0.9846289986512214,
              "auroc_top30_bad": 0.9880899047619047,
              "mae": 0.15174871197268366,
              "mse": 0.0415582782077347,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8135443015473299,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.020691197603940965
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16746863721609115
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5377545804917813
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9450949988643328
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2670785710781813
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9423028216571163,
              "spearman": 0.9707665405225859,
              "auroc_top30_worst": 0.976304761904762,
              "pairwise_seed_ranking": 0.91,
              "predicted_best_mean_error": 1.7616271131038665,
              "seed0_mean_error": 1.8668941221237183,
              "random_seed_mean_error": 1.8321932954788207,
              "oracle_best_mean_error": 1.7580343310832978,
              "improvement_over_seed0": 0.10526700901985175,
              "gap_to_oracle": 0.0035927820205687855,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8695264029502868
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1755917586195164
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4490127390861511
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6437921600936571
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8333799670696258
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5131076335906983,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7509097711245218,
                  "rejected_mean_error": 2.5756117305755617,
                  "gap_rejected_minus_accepted": 0.8247019594510399
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.299873948097229,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6431938213243555,
                  "rejected_mean_error": 2.402723157367767,
                  "gap_rejected_minus_accepted": 0.7595293360434117
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0391143560409546,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4490127390861511,
                  "rejected_mean_error": 2.2177471950531005,
                  "gap_rejected_minus_accepted": 0.7687344559669493
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6671347916126251,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1770079427252944,
                  "rejected_mean_error": 2.0526376443586076,
                  "gap_rejected_minus_accepted": 0.8756297016333132
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.569917583465576,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7746048333909776,
                  "rejected_mean_error": 2.697497720718384,
                  "gap_rejected_minus_accepted": 0.9228928873274063
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.328748345375061,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.658864102899072,
                  "rejected_mean_error": 2.4843800522032238,
                  "gap_rejected_minus_accepted": 0.8255159493041517
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.077439785003662,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.464309955596924,
                  "rejected_mean_error": 2.2694782886505127,
                  "gap_rejected_minus_accepted": 0.8051683330535888
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.7087857127189636,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.185929676843068,
                  "rejected_mean_error": 2.09630995128244,
                  "gap_rejected_minus_accepted": 0.9103802744393721
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.989826890929138,
              "spearman": 0.988861165310601,
              "auroc_top30_bad": 0.9936380952380952,
              "mae": 0.19431337269837967,
              "mse": 0.06108606974437307,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.995,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9872594689163751,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04198451220989227
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20892097184062003
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7040016622543335
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0831945947011312
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.982850344891157,
              "spearman": 0.986951870951871,
              "auroc_top30_worst": 0.9942857142857142,
              "pairwise_seed_ranking": 0.852,
              "predicted_best_mean_error": 2.2476259961724283,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.07900642007589331,
              "gap_to_oracle": 0.006215471625328206,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2916893184185028
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4887178697586059
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6546934337615966
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.871477984905243
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.316489219665527,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.095574417511622,
                  "rejected_mean_error": 4.347041130065918,
                  "gap_rejected_minus_accepted": 2.2514667125542958
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.9303835034370422,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.871477984905243,
                  "rejected_mean_error": 3.668450400352478,
                  "gap_rejected_minus_accepted": 1.7969724154472348
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.2166396379470825,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6546934337615966,
                  "rejected_mean_error": 2.9867487437725067,
                  "gap_rejected_minus_accepted": 1.33205531001091
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.8875081241130829,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4887178697586059,
                  "rejected_mean_error": 2.5980554951032,
                  "gap_rejected_minus_accepted": 1.1093376253445943
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.320564842224121,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.942222476005554,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.8861788638432821,
                  "rejected_mean_error": 3.64799307346344,
                  "gap_rejected_minus_accepted": 1.7618142096201577
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.228365898132324,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6713587474822997,
                  "rejected_mean_error": 2.981906085014343,
                  "gap_rejected_minus_accepted": 1.3105473375320433
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.8983314335346222,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.509521622657776,
                  "rejected_mean_error": 2.5990026807785034,
                  "gap_rejected_minus_accepted": 1.0894810581207275
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_goal/quantile_context_gated_q90/model.pt"
      },
      {
        "variant": "quantile_context_gated_q95",
        "feature_mode": "M3_gated_base",
        "kind": "gated",
        "q": 0.95,
        "best_epoch": 78,
        "best_calib_pinball": 0.022548744454979897,
        "train_time_sec": 51.11875772476196,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9954611592320737,
              "spearman": 0.9951928697475696,
              "auroc_top30_bad": 0.9980243571428571,
              "mae": 0.15347078300267458,
              "mse": 0.034394741556635425,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.997,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7847578612127043,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04412215533852577
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1748449728190899
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4788145850330591
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8185239268640677
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2307025221720338
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9953338555408725,
              "spearman": 0.9980010503599941,
              "auroc_top30_worst": 0.9989247619047619,
              "pairwise_seed_ranking": 0.8627,
              "predicted_best_mean_error": 1.6917125400006772,
              "seed0_mean_error": 1.7593383036255836,
              "random_seed_mean_error": 1.748514448583126,
              "oracle_best_mean_error": 1.6850638110637666,
              "improvement_over_seed0": 0.06762576362490647,
              "gap_to_oracle": 0.006648728936910597,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6109191967844964
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8481852163553238
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1108973911881448
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3372383968114854
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7487053180277348
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2216096639633203,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4981845247017014,
                  "rejected_mean_error": 4.003392457962036,
                  "gap_rejected_minus_accepted": 2.5052079332603348
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.209761142730713,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.3372383968114854,
                  "rejected_mean_error": 2.983106081676483,
                  "gap_rejected_minus_accepted": 1.6458676848649978
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7529692649841309,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1108973911881448,
                  "rejected_mean_error": 2.386513244867325,
                  "gap_rejected_minus_accepted": 1.2756158536791802
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2233413457870483,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8481852163553238,
                  "rejected_mean_error": 2.048878685251872,
                  "gap_rejected_minus_accepted": 1.200693468896548
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.1765154838562015,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5089032409588496,
                  "rejected_mean_error": 4.01325386762619,
                  "gap_rejected_minus_accepted": 2.5043506266673408
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.221820592880249,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3472647982438406,
                  "rejected_mean_error": 2.995558819770813,
                  "gap_rejected_minus_accepted": 1.6482940215269724
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.765841782093048,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1171797231435776,
                  "rejected_mean_error": 2.4014968841075897,
                  "gap_rejected_minus_accepted": 1.284317160964012
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2423998415470123,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8517098400592804,
                  "rejected_mean_error": 2.0618811248143514,
                  "gap_rejected_minus_accepted": 1.210171284755071
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9562050959532148,
              "spearman": 0.9809031864219634,
              "auroc_top30_bad": 0.9926194285714286,
              "mae": 0.20256570663452148,
              "mse": 0.10403927535033818,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7754203572328815,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08763424724340439
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1637609054327011
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4192448635697365
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8057913613080978
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1699017732203008
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8945481612361992,
              "spearman": 0.9679338475096626,
              "auroc_top30_worst": 0.9709257142857144,
              "pairwise_seed_ranking": 0.8956,
              "predicted_best_mean_error": 1.59408618247509,
              "seed0_mean_error": 1.6905601416826248,
              "random_seed_mean_error": 1.6723020417690277,
              "oracle_best_mean_error": 1.5885274814367294,
              "improvement_over_seed0": 0.09647395920753477,
              "gap_to_oracle": 0.005558701038360647,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4690513277053833
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7533744138020736
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1186059750556945
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.393988543291336
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6684940560817718
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.881870651245118,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5809374238650005,
                  "rejected_mean_error": 2.456503746032715,
                  "gap_rejected_minus_accepted": 0.8755663221677144
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.262929618358612,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3931732427730377,
                  "rejected_mean_error": 2.4926972575842763,
                  "gap_rejected_minus_accepted": 1.0995240148112386
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9063546061515808,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1186059750556945,
                  "rejected_mean_error": 2.218382137107849,
                  "gap_rejected_minus_accepted": 1.0997761620521547
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1895678341388702,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7544607624840051,
                  "rejected_mean_error": 1.9738221466859351,
                  "gap_rejected_minus_accepted": 1.21936138420193
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.945767545700073,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6002208064662085,
                  "rejected_mean_error": 2.5036141586303713,
                  "gap_rejected_minus_accepted": 0.9033933521641628
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3042832612991333,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.409230321008254,
                  "rejected_mean_error": 2.525618498287504,
                  "gap_rejected_minus_accepted": 1.1163881772792499
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9392648935317993,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1350874655246734,
                  "rejected_mean_error": 2.246032817840576,
                  "gap_rejected_minus_accepted": 1.1109453523159027
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2199323773384094,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7633973289103735,
                  "rejected_mean_error": 2.0029198058786237,
                  "gap_rejected_minus_accepted": 1.2395224769682502
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9712367319470869,
              "spearman": 0.9810736263704731,
              "auroc_top30_bad": 0.9853714285714286,
              "mae": 0.1842960077673197,
              "mse": 0.07457529910241846,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.7944412153271103,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.060755359202623364
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1664220700621605
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5379566372811794
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9456011345505715
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2670785710781813
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9017833052999549,
              "spearman": 0.9588317944523487,
              "auroc_top30_worst": 0.9677805714285714,
              "pairwise_seed_ranking": 0.8748,
              "predicted_best_mean_error": 1.7656314116716385,
              "seed0_mean_error": 1.8668941221237183,
              "random_seed_mean_error": 1.8321932954788207,
              "oracle_best_mean_error": 1.7580343310832978,
              "improvement_over_seed0": 0.1012627104520798,
              "gap_to_oracle": 0.007597080588340743,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8711939330101013
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.178124572795171
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4529848256111144
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6441710153495326
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8333799670696258
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6476787090301523,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7582845249705845,
                  "rejected_mean_error": 2.5092389459609987,
                  "gap_rejected_minus_accepted": 0.7509544209904142
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3159024715423584,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6434835172004862,
                  "rejected_mean_error": 2.4018559208312356,
                  "gap_rejected_minus_accepted": 0.7583724036307493
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0664952993392944,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4529848256111144,
                  "rejected_mean_error": 2.213775108528137,
                  "gap_rejected_minus_accepted": 0.7607902829170228
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6811562776565552,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1791167520105648,
                  "rejected_mean_error": 2.0519332075322576,
                  "gap_rejected_minus_accepted": 0.8728164555216928
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.70719141960144,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7875663444730971,
                  "rejected_mean_error": 2.580844120979309,
                  "gap_rejected_minus_accepted": 0.793277776506212
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3325840830802917,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6575311345850083,
                  "rejected_mean_error": 2.488336640691,
                  "gap_rejected_minus_accepted": 0.8308055061059918
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.1027326583862305,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.468241925239563,
                  "rejected_mean_error": 2.2655463190078735,
                  "gap_rejected_minus_accepted": 0.7973043937683104
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.721392571926117,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1882985830307007,
                  "rejected_mean_error": 2.095511870588211,
                  "gap_rejected_minus_accepted": 0.9072132875575103
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9866022220720392,
              "spearman": 0.9853465349579869,
              "auroc_top30_bad": 0.9933547619047619,
              "mae": 0.2268271995857358,
              "mse": 0.07813430258377639,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.9368979671416992,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09454153090715409
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2160880785882473
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7039600083827973
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.084040053844452
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.9791034301039778,
              "spearman": 0.9872490032490032,
              "auroc_top30_worst": 0.9912238095238095,
              "pairwise_seed_ranking": 0.819,
              "predicted_best_mean_error": 2.2532829293608665,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.07334948688745513,
              "gap_to_oracle": 0.01187240481376639,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.299353039264679
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4828508400917053
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6553935508728028
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8750505531628927
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.490183162689209,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0949588845835794,
                  "rejected_mean_error": 4.352580926418304,
                  "gap_rejected_minus_accepted": 2.257622041834725
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7777686715126038,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8750505531628927,
                  "rejected_mean_error": 3.657732695579529,
                  "gap_rejected_minus_accepted": 1.7826821424166361
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.1971805095672607,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6553935508728028,
                  "rejected_mean_error": 2.9860486266613004,
                  "gap_rejected_minus_accepted": 1.3306550757884976
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.8485609591007233,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.4828508400917053,
                  "rejected_mean_error": 2.6000111716588337,
                  "gap_rejected_minus_accepted": 1.1171603315671284
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.492914009094238,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.7964086532592773,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.887336942354838,
                  "rejected_mean_error": 3.644518837928772,
                  "gap_rejected_minus_accepted": 1.7571818955739338
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.2003458738327026,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.670657649040222,
                  "rejected_mean_error": 2.982607183456421,
                  "gap_rejected_minus_accepted": 1.3119495344161989
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.8741260766983032,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.4972928404808044,
                  "rejected_mean_error": 2.6030789415041604,
                  "gap_rejected_minus_accepted": 1.105786101023356
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_goal/quantile_context_gated_q95/model.pt"
      },
      {
        "variant": "quantile_seed_relative_q90",
        "feature_mode": "M4_seed_relative",
        "kind": "mlp_big",
        "q": 0.9,
        "best_epoch": 78,
        "best_calib_pinball": 0.03282520920038223,
        "train_time_sec": 54.773712158203125,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9976711606947809,
              "spearman": 0.9951956718740582,
              "auroc_top30_bad": 0.9965908095238096,
              "mae": 0.15691395446100015,
              "mse": 0.04047100156457167,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8487707273809251,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.008943501174449921
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17519049027562142
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.47848910632431507
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8196949871242046
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2307025221720338
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9984222052843346,
              "spearman": 0.9971153670925453,
              "auroc_top30_worst": 0.9978702857142857,
              "pairwise_seed_ranking": 0.9288,
              "predicted_best_mean_error": 1.6864203154742718,
              "seed0_mean_error": 1.7593383036255836,
              "random_seed_mean_error": 1.748514448583126,
              "oracle_best_mean_error": 1.6850638110637666,
              "improvement_over_seed0": 0.07291798815131179,
              "gap_to_oracle": 0.001356504410505277,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6102830788493157
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8481266159296036
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1113098560929298
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.337606691845258
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7487053180277348
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.2291941881179826,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4977078254024188,
                  "rejected_mean_error": 4.007682751655579,
                  "gap_rejected_minus_accepted": 2.50997492625316
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3033252358436584,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.337606691845258,
                  "rejected_mean_error": 2.982001196575165,
                  "gap_rejected_minus_accepted": 1.644394504729907
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8293487429618835,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1113098560929298,
                  "rejected_mean_error": 2.3861007799625398,
                  "gap_rejected_minus_accepted": 1.27479092386961
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.323741853237152,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8481266159296036,
                  "rejected_mean_error": 2.048898218727112,
                  "gap_rejected_minus_accepted": 1.2007716027975084
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.239607548713684,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.5081321097082563,
                  "rejected_mean_error": 4.020194048881531,
                  "gap_rejected_minus_accepted": 2.5120619391732744
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.31208735704422,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.3479408179124197,
                  "rejected_mean_error": 2.9935307607650756,
                  "gap_rejected_minus_accepted": 1.645589942852656
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.844339907169342,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.1179147554636002,
                  "rejected_mean_error": 2.4007618517875673,
                  "gap_rejected_minus_accepted": 1.282847096323967
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3267923593521118,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8518723080158234,
                  "rejected_mean_error": 2.061826968828837,
                  "gap_rejected_minus_accepted": 1.2099546608130138
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9870704607482086,
              "spearman": 0.9829027539323252,
              "auroc_top30_bad": 0.9958095238095238,
              "mae": 0.11754078930412434,
              "mse": 0.023024676835927065,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.956,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7400703138886372,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08186875620484352
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17360747575759888
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4231035821080208
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8029990396579106
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1699017732203008
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.978420769854059,
              "spearman": 0.9859092000698881,
              "auroc_top30_worst": 0.9886933333333333,
              "pairwise_seed_ranking": 0.9328,
              "predicted_best_mean_error": 1.5899248187541961,
              "seed0_mean_error": 1.6905601416826248,
              "random_seed_mean_error": 1.6723020417690277,
              "oracle_best_mean_error": 1.5885274814367294,
              "improvement_over_seed0": 0.1006353229284287,
              "gap_to_oracle": 0.001397337317466718,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4730468125343323
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7670114067120429
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1170638819694518
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3855384170754885
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6684940560817718
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.762115621566773,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5350683976809183,
                  "rejected_mean_error": 2.869324981689453,
                  "gap_rejected_minus_accepted": 1.3342565840085348
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2321823835372925,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3848875362183521,
                  "rejected_mean_error": 2.517501433436482,
                  "gap_rejected_minus_accepted": 1.1326138972181299
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.683620035648346,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1170638819694518,
                  "rejected_mean_error": 2.219924230194092,
                  "gap_rejected_minus_accepted": 1.1028603482246402
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1792449355125427,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7689110619572405,
                  "rejected_mean_error": 1.968995098943008,
                  "gap_rejected_minus_accepted": 1.2000840369857677
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.799437165260315,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5544887035422854,
                  "rejected_mean_error": 2.915203084945679,
                  "gap_rejected_minus_accepted": 1.3607143814033935
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2576589584350586,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4013530380904355,
                  "rejected_mean_error": 2.549000274567377,
                  "gap_rejected_minus_accepted": 1.1476472364769417
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7048197388648987,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1350982620716095,
                  "rejected_mean_error": 2.24602202129364,
                  "gap_rejected_minus_accepted": 1.1109237592220307
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1959019005298615,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7818183090005603,
                  "rejected_mean_error": 1.9967138072386146,
                  "gap_rejected_minus_accepted": 1.2148954982380542
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9810167945750828,
              "spearman": 0.9754830289317958,
              "auroc_top30_bad": 0.9888617142857143,
              "mae": 0.1641665374445336,
              "mse": 0.046639823076607446,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7946770347411991,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07764154714345932
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18884524666070937
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5402105721414089
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9469854846278827
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2670785710781813
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9509521766467534,
              "spearman": 0.9585446052765474,
              "auroc_top30_worst": 0.972824380952381,
              "pairwise_seed_ranking": 0.92,
              "predicted_best_mean_error": 1.761452699661255,
              "seed0_mean_error": 1.8668941221237183,
              "random_seed_mean_error": 1.8321932954788207,
              "oracle_best_mean_error": 1.7580343310832978,
              "improvement_over_seed0": 0.10544142246246335,
              "gap_to_oracle": 0.003418368577957187,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8813030600547791
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.182326129422738
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.454007489299774
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.641160479168902
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8333799670696258
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.595940661430359,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7573486149575974,
                  "rejected_mean_error": 2.517662136077881,
                  "gap_rejected_minus_accepted": 0.7603135211202836
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4121018052101135,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.640743647402862,
                  "rejected_mean_error": 2.4100580230688515,
                  "gap_rejected_minus_accepted": 0.7693143756659895
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.1099681854248047,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.454007489299774,
                  "rejected_mean_error": 2.2127524448394778,
                  "gap_rejected_minus_accepted": 0.7587449555397037
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.6473900973796844,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1831991708697602,
                  "rejected_mean_error": 2.0505694966433268,
                  "gap_rejected_minus_accepted": 0.8673703257735665
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6512206554412843,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7836259418063694,
                  "rejected_mean_error": 2.616307744979858,
                  "gap_rejected_minus_accepted": 0.8326818031734888
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.463690161705017,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.650791739397508,
                  "rejected_mean_error": 2.50834087719993,
                  "gap_rejected_minus_accepted": 0.857549137802422
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.174039125442505,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4712952365875245,
                  "rejected_mean_error": 2.262493007659912,
                  "gap_rejected_minus_accepted": 0.7911977710723874
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.671930730342865,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1934046593923417,
                  "rejected_mean_error": 2.0937916416535405,
                  "gap_rejected_minus_accepted": 0.9003869822611987
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2000,
              "pearson": 0.9848101212673415,
              "spearman": 0.9771618393620678,
              "auroc_top30_bad": 0.9828630952380951,
              "mae": 0.2012207496562678,
              "mse": 0.07555700898086391,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.99,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 1.0176474153385728,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04799438111484051
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22577538260817528
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7085517692565918
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0878901637395224
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.560086113333702
                }
              ]
            },
            "simvla_only": {
              "n": 1000,
              "contexts": 200,
              "pearson": 0.979577465740801,
              "spearman": 0.9688087528087529,
              "auroc_top30_worst": 0.9873428571428571,
              "pairwise_seed_ranking": 0.892,
              "predicted_best_mean_error": 2.2452984181046487,
              "seed0_mean_error": 2.3266324162483216,
              "random_seed_mean_error": 2.3179259487986563,
              "oracle_best_mean_error": 2.2414105245471,
              "improvement_over_seed0": 0.08133399814367293,
              "gap_to_oracle": 0.003887893557548594,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3141451323032378
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.5042682304382324
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6659830572605132
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8686320865948995
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.3207210887670517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.306693649291993,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 2.0954242747359806,
                  "rejected_mean_error": 4.348392415046692,
                  "gap_rejected_minus_accepted": 2.252968140310711
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.067661941051483,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.8686320865948995,
                  "rejected_mean_error": 3.6769880952835083,
                  "gap_rejected_minus_accepted": 1.8083560086886088
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.3289185762405396,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.6659830572605132,
                  "rejected_mean_error": 2.97545912027359,
                  "gap_rejected_minus_accepted": 1.3094760630130768
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.975356936454773,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.5042682304382324,
                  "rejected_mean_error": 2.5928720415433246,
                  "gap_rejected_minus_accepted": 1.0886038111050922
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.288706111907959,
                  "accepted_n": 180,
                  "rejected_n": 20,
                  "accepted_mean_error": 2.1037791278627185,
                  "rejected_mean_error": 4.33231201171875,
                  "gap_rejected_minus_accepted": 2.228532883856032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.055313766002655,
                  "accepted_n": 150,
                  "rejected_n": 50,
                  "accepted_mean_error": 1.881413442293803,
                  "rejected_mean_error": 3.6622893381118775,
                  "gap_rejected_minus_accepted": 1.7808758958180746
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.3520878553390503,
                  "accepted_n": 100,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.6779606711864472,
                  "rejected_mean_error": 2.975304161310196,
                  "gap_rejected_minus_accepted": 1.2973434901237486
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.9910956621170044,
                  "accepted_n": 50,
                  "rejected_n": 150,
                  "accepted_mean_error": 1.5186582159996034,
                  "rejected_mean_error": 2.595957149664561,
                  "gap_rejected_minus_accepted": 1.0772989336649577
                }
              ]
            }
          }
        },
        "checkpoint": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/outputs/checkpoints/stage8_quantile/holdout_libero_goal/quantile_seed_relative_q90/model.pt"
      }
    ]
  },
  "variants": [
    "quantile_action_q80",
    "quantile_action_q90",
    "quantile_action_q95",
    "quantile_context_gated_q80",
    "quantile_context_gated_q90",
    "quantile_context_gated_q95",
    "quantile_seed_relative_q90"
  ]
}
```
