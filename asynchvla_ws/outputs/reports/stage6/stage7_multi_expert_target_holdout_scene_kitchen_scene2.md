# Stage 7 Multi-Expert Target Experiments: holdout_scene_kitchen_scene2

```json
{
  "split": "holdout_scene_kitchen_scene2",
  "by_target": {
    "target_chunk_l2_single_expert": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 79,
        "best_calib_loss": 0.05486587435007095,
        "train_time_sec": 11.139407396316528,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9602781167993357,
              "spearman": 0.9383448383627352,
              "auroc_top30_bad": 0.9994456666666667,
              "mae": 0.1114983075339347,
              "mse": 0.04496247708806283,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.539,
              "expert_lt_simvla_seed0": 0.979,
              "same_context_pred_std": 0.6640917209226472,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.30483907197788357
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.31785018376857044
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4757353914253414
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7866464177762469
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1139734886761754
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.997805132485057,
              "spearman": 0.9978858032193815,
              "auroc_top30_worst": 0.9988944761904762,
              "pairwise_seed_ranking": 0.8762,
              "predicted_best_mean_error": 1.4554842622876167,
              "seed0_mean_error": 1.5283110035955907,
              "random_seed_mean_error": 1.5151066114902496,
              "oracle_best_mean_error": 1.45196512183547,
              "improvement_over_seed0": 0.07282674130797395,
              "gap_to_oracle": 0.0035191404521466296,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5893533744812012
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7988419937133789
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0482635529994964
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2619088574091593
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5148110565423965
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3268517017364503,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3964549090862275,
                  "rejected_mean_error": 2.580016383647919,
                  "gap_rejected_minus_accepted": 1.1835614745616914
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9288584291934967,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2619088574091593,
                  "rejected_mean_error": 2.273517653942108,
                  "gap_rejected_minus_accepted": 1.0116087965329488
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5285276174545288,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0482635529994964,
                  "rejected_mean_error": 1.9813585600852965,
                  "gap_rejected_minus_accepted": 0.9330950070858002
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1220237612724304,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7988419937133789,
                  "rejected_mean_error": 1.7534674108187358,
                  "gap_rejected_minus_accepted": 0.9546254171053569
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3713873863220214,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.406793698105547,
                  "rejected_mean_error": 2.6219667530059816,
                  "gap_rejected_minus_accepted": 1.2151730549004345
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9418293833732605,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2700899423360825,
                  "rejected_mean_error": 2.302974187374115,
                  "gap_rejected_minus_accepted": 1.0328842450380327
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5445303320884705,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0530970888733864,
                  "rejected_mean_error": 2.003524918317795,
                  "gap_rejected_minus_accepted": 0.9504278294444084
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1214986145496368,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7999053684473038,
                  "rejected_mean_error": 1.7711128819783528,
                  "gap_rejected_minus_accepted": 0.9712075135310491
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.895200286625186,
              "spearman": 0.867227983820852,
              "auroc_top30_bad": 0.9568853333333334,
              "mae": 0.3176762039542198,
              "mse": 0.17076591671294714,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.484,
              "expert_lt_simvla_seed0": 0.964,
              "same_context_pred_std": 0.712550118425345,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.33826596796512604
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3964666492938995
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5617647737026215
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9451748591184617
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3029261555254459
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8234488526378523,
              "spearman": 0.8118425153552099,
              "auroc_top30_worst": 0.8913889523809524,
              "pairwise_seed_ranking": 0.7712,
              "predicted_best_mean_error": 1.8412163933515548,
              "seed0_mean_error": 1.917619425535202,
              "random_seed_mean_error": 1.8991771894693374,
              "oracle_best_mean_error": 1.8251729023456573,
              "improvement_over_seed0": 0.07640303218364708,
              "gap_to_oracle": 0.016043491005897526,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9114685845375061
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1713486686348915
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4266281532287597
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6696043060278334
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.901424583721161
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.483404564857483,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7953877484003702,
                  "rejected_mean_error": 2.8557561016082764,
                  "gap_rejected_minus_accepted": 1.0603683532079062
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1788150668144226,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6699400594420215,
                  "rejected_mean_error": 2.5943990222181377,
                  "gap_rejected_minus_accepted": 0.9244589627761162
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.857126235961914,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4266281532287597,
                  "rejected_mean_error": 2.376221014213562,
                  "gap_rejected_minus_accepted": 0.9495928609848023
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2304958403110504,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1706559936078593,
                  "rejected_mean_error": 2.1455340487216557,
                  "gap_rejected_minus_accepted": 0.9748780551137963
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5167032003402707,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.810078152815501,
                  "rejected_mean_error": 2.885490880012512,
                  "gap_rejected_minus_accepted": 1.075412727197011
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1923301815986633,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6725829530527248,
                  "rejected_mean_error": 2.6449499073482694,
                  "gap_rejected_minus_accepted": 0.9723669542955446
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9016372561454773,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.431280406475067,
                  "rejected_mean_error": 2.403958444595337,
                  "gap_rejected_minus_accepted": 0.9726780381202698
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2680319547653198,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1432653315483579,
                  "rejected_mean_error": 2.1784980775200746,
                  "gap_rejected_minus_accepted": 1.0352327459717168
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.803506915029312,
              "spearman": 0.8119288058893838,
              "auroc_top30_bad": 0.9559870476190476,
              "mae": 0.402810096848011,
              "mse": 0.3461287693800378,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.488,
              "expert_lt_simvla_seed0": 0.952,
              "same_context_pred_std": 0.6390805949311935,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.39611591172218324
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.432676725769043
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5261815275907517
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8444610942761104
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2224939480662347
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7081504741533545,
              "spearman": 0.7548477058865318,
              "auroc_top30_worst": 0.8281813333333333,
              "pairwise_seed_ranking": 0.7936,
              "predicted_best_mean_error": 1.6651385083198547,
              "seed0_mean_error": 1.7280002343654632,
              "random_seed_mean_error": 1.7201814349889755,
              "oracle_best_mean_error": 1.6515287026166916,
              "improvement_over_seed0": 0.06286172604560858,
              "gap_to_oracle": 0.013609805703163058,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7488794345855713
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8435379811204397
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.192797557258606
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4123789734169365
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7233014276504517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.421395516395569,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.581659061961704,
                  "rejected_mean_error": 2.998082718849182,
                  "gap_rejected_minus_accepted": 1.4164236568874782
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.038311779499054,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4112055893259852,
                  "rejected_mean_error": 2.6575947200147487,
                  "gap_rejected_minus_accepted": 1.2463891306887636
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.469654142856598,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.192797557258606,
                  "rejected_mean_error": 2.2538052980422973,
                  "gap_rejected_minus_accepted": 1.0610077407836913
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.976917952299118,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8432040585877415,
                  "rejected_mean_error": 2.017293398319212,
                  "gap_rejected_minus_accepted": 1.1740893397314704
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4587024211883546,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.577892464796702,
                  "rejected_mean_error": 3.078970160484314,
                  "gap_rejected_minus_accepted": 1.5010776956876117
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0398231148719788,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4127287294137925,
                  "rejected_mean_error": 2.663806130015661,
                  "gap_rejected_minus_accepted": 1.2510774006018686
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4464905858039856,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1963603749275207,
                  "rejected_mean_error": 2.2596400938034056,
                  "gap_rejected_minus_accepted": 1.063279718875885
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9554329365491867,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8484944625506325,
                  "rejected_mean_error": 2.024304317918053,
                  "gap_rejected_minus_accepted": 1.1758098553674206
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.8480698990494062,
              "spearman": 0.8333579860255571,
              "auroc_top30_bad": 0.9095481049562681,
              "mae": 0.31355603088225636,
              "mse": 0.16776161360096906,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6227497893547191,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3466387344258172
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.38521815823657174
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.643534757409777
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9408157673052379
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1861764596828392
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.6512398835518799,
              "spearman": 0.512231785895773,
              "auroc_top30_worst": 0.7502623906705539,
              "pairwise_seed_ranking": 0.7371428571428571,
              "predicted_best_mean_error": 1.6296224687780654,
              "seed0_mean_error": 1.6977024810654777,
              "random_seed_mean_error": 1.668839773961476,
              "oracle_best_mean_error": 1.6144805014133454,
              "improvement_over_seed0": 0.06808001228741234,
              "gap_to_oracle": 0.015141967364719955,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4198108341012683
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4895852698598588
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.493643810749054
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.570608196258545
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6719353059359958
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.305853509902955,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.5903873082191224,
                  "rejected_mean_error": 2.4058672853878567,
                  "gap_rejected_minus_accepted": 0.8154799771687342
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7274430394172668,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.570608196258545,
                  "rejected_mean_error": 1.975916634968349,
                  "gap_rejected_minus_accepted": 0.40530843870980404
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4211360216140747,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.493643810749054,
                  "rejected_mean_error": 1.850226801122938,
                  "gap_rejected_minus_accepted": 0.35658299037388397
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0823992490768433,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.4895852698598588,
                  "rejected_mean_error": 1.7327186512947081,
                  "gap_rejected_minus_accepted": 0.2431333814348493
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3721331834793093,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6103318494463723,
                  "rejected_mean_error": 2.484038165637425,
                  "gap_rejected_minus_accepted": 0.8737063161910528
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7851708233356476,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5820907956077939,
                  "rejected_mean_error": 2.044537537438529,
                  "gap_rejected_minus_accepted": 0.462446741830735
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4522171020507812,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.5081020508493697,
                  "rejected_mean_error": 1.8873029112815858,
                  "gap_rejected_minus_accepted": 0.3792008604322161
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0811794102191925,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.4944667407444545,
                  "rejected_mean_error": 1.765447727839152,
                  "gap_rejected_minus_accepted": 0.27098098709469753
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
        "best_epoch": 72,
        "best_calib_loss": 0.007333488669246435,
        "train_time_sec": 35.270612955093384,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9996640614635753,
              "spearman": 0.9988778111667661,
              "auroc_top30_bad": 0.9998871904761906,
              "mae": 0.016552731419866906,
              "mse": 0.00047267794216581126,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6734659058158582,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0015535242296755313
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16863021546453238
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4673116459839046
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7864102716758847
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1139734886761754
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9996221405643164,
              "spearman": 0.9996029559840993,
              "auroc_top30_worst": 0.9997769523809523,
              "pairwise_seed_ranking": 0.95695,
              "predicted_best_mean_error": 1.4526684155464173,
              "seed0_mean_error": 1.5283110035955907,
              "random_seed_mean_error": 1.5151066114902496,
              "oracle_best_mean_error": 1.45196512183547,
              "improvement_over_seed0": 0.07564258804917334,
              "gap_to_oracle": 0.0007032937109472392,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5871958502531052
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7976694789886475
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0476421925544739
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.261542710272471
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5148110565423965
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2949628353118903,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3961556468274858,
                  "rejected_mean_error": 2.582709743976593,
                  "gap_rejected_minus_accepted": 1.1865540971491073
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9131730198860168,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.261542710272471,
                  "rejected_mean_error": 2.274616095352173,
                  "gap_rejected_minus_accepted": 1.0130733850797018
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5185067653656006,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0476421925544739,
                  "rejected_mean_error": 1.9819799205303192,
                  "gap_rejected_minus_accepted": 0.9343377279758454
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1051374971866608,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7976694789886475,
                  "rejected_mean_error": 1.753858249060313,
                  "gap_rejected_minus_accepted": 0.9561887700716655
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3403199434280397,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4065879614154497,
                  "rejected_mean_error": 2.623818383216858,
                  "gap_rejected_minus_accepted": 1.217230421801408
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9348766803741455,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2697326813141505,
                  "rejected_mean_error": 2.304045970439911,
                  "gap_rejected_minus_accepted": 1.0343132891257605
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.53396874666214,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0526790040135383,
                  "rejected_mean_error": 2.0039430031776426,
                  "gap_rejected_minus_accepted": 0.9512639991641043
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1152687966823578,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7986411873102188,
                  "rejected_mean_error": 1.7715342756907144,
                  "gap_rejected_minus_accepted": 0.9728930883804956
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9912019216608949,
              "spearman": 0.9898402669910425,
              "auroc_top30_bad": 0.9971885714285714,
              "mae": 0.08479925547093153,
              "mse": 0.016302456493837686,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.964,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7783436767681134,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06817109560966492
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17481751787662506
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5115612970471383
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9107640808820725
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3029261555254459
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9843875411592273,
              "spearman": 0.9890035416342667,
              "auroc_top30_worst": 0.9836586666666667,
              "pairwise_seed_ranking": 0.9368,
              "predicted_best_mean_error": 1.826215281844139,
              "seed0_mean_error": 1.917619425535202,
              "random_seed_mean_error": 1.8991771894693374,
              "oracle_best_mean_error": 1.8251729023456573,
              "improvement_over_seed0": 0.09140414369106287,
              "gap_to_oracle": 0.001042379498481738,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7607675342559814
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0356754125692906
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.335198366546631
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6144912444960589
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.901424583721161
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.648937892913819,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7646174080106947,
                  "rejected_mean_error": 3.1326891651153566,
                  "gap_rejected_minus_accepted": 1.368071757104662
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3274053931236267,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6136756707917155,
                  "rejected_mean_error": 2.76283267130867,
                  "gap_rejected_minus_accepted": 1.1491570005169545
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9487239718437195,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.335198366546631,
                  "rejected_mean_error": 2.467650800895691,
                  "gap_rejected_minus_accepted": 1.13245243434906
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.368760734796524,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0367059924732,
                  "rejected_mean_error": 2.1902793532629024,
                  "gap_rejected_minus_accepted": 1.1535733607897023
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.696535348892212,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7759618714120653,
                  "rejected_mean_error": 3.1925374126434325,
                  "gap_rejected_minus_accepted": 1.4165755412313672
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3531861901283264,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6252707360900023,
                  "rejected_mean_error": 2.7853845830947632,
                  "gap_rejected_minus_accepted": 1.160113847004761
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.962268352508545,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.341797191143036,
                  "rejected_mean_error": 2.493441659927368,
                  "gap_rejected_minus_accepted": 1.1516444687843321
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3699578642845154,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0391517735662914,
                  "rejected_mean_error": 2.2135737681771346,
                  "gap_rejected_minus_accepted": 1.1744219946108432
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9716153494082951,
              "spearman": 0.9824061764775883,
              "auroc_top30_bad": 0.9990994285714286,
              "mae": 0.13935040934309365,
              "mse": 0.07379572731809053,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6763171683972865,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08393305712938309
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20185864279270171
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.46423210456371305
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7776115484714508
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2224939480662347
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9694015513296961,
              "spearman": 0.9936838103576388,
              "auroc_top30_worst": 0.9999420952380953,
              "pairwise_seed_ranking": 0.9252,
              "predicted_best_mean_error": 1.6542533482313155,
              "seed0_mean_error": 1.7280002343654632,
              "random_seed_mean_error": 1.7201814349889755,
              "oracle_best_mean_error": 1.6515287026166916,
              "improvement_over_seed0": 0.0737468861341477,
              "gap_to_oracle": 0.002724645614623933,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5032225432395935
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.749176348440158
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.008203497505188
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2616438619109358
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7233014276504517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5729269266128543,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4969019205305312,
                  "rejected_mean_error": 3.7608969917297363,
                  "gap_rejected_minus_accepted": 2.263995071199205
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1498674154281616,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2606466661268008,
                  "rejected_mean_error": 3.108309451764384,
                  "gap_rejected_minus_accepted": 1.8476627856375831
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.48306143283844,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.008203497505188,
                  "rejected_mean_error": 2.4383993577957153,
                  "gap_rejected_minus_accepted": 1.4301958602905274
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.117071270942688,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7502460477832026,
                  "rejected_mean_error": 2.048345540669074,
                  "gap_rejected_minus_accepted": 1.2980994928858713
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5553779125213625,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4943998122215272,
                  "rejected_mean_error": 3.830404033660889,
                  "gap_rejected_minus_accepted": 2.336004221439362
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.181750237941742,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2599209830722706,
                  "rejected_mean_error": 3.1173783294738286,
                  "gap_rejected_minus_accepted": 1.857457346401558
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4653719663619995,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0030460448265075,
                  "rejected_mean_error": 2.4529544239044188,
                  "gap_rejected_minus_accepted": 1.4499083790779113
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1274062395095825,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7501943707466125,
                  "rejected_mean_error": 2.0574214611461454,
                  "gap_rejected_minus_accepted": 1.3072270903995329
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9871928663934191,
              "spearman": 0.9766247673932369,
              "auroc_top30_bad": 0.976681243926142,
              "mae": 0.09569008451221245,
              "mse": 0.017789996541312872,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9785714285714285,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7184899529155455,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.051093900842326026
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1829085223163877
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5556743306347302
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9152789965981529
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1861764596828392
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9507168740568722,
              "spearman": 0.9191086395803139,
              "auroc_top30_worst": 0.9188726919339164,
              "pairwise_seed_ranking": 0.9014285714285715,
              "predicted_best_mean_error": 1.6167258509567806,
              "seed0_mean_error": 1.6977024810654777,
              "random_seed_mean_error": 1.668839773961476,
              "oracle_best_mean_error": 1.6144805014133454,
              "improvement_over_seed0": 0.08097663010869716,
              "gap_to_oracle": 0.002245349543435138,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0246913467134748
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.235079050745283
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4216830897331239
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5345534136181787
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6719353059359958
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.138548231124878,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.5918255701897637,
                  "rejected_mean_error": 2.3929229276520867,
                  "gap_rejected_minus_accepted": 0.801097357462323
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9456661641597748,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5345534136181787,
                  "rejected_mean_error": 2.0840809828894478,
                  "gap_rejected_minus_accepted": 0.5495275692712691
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7074052095413208,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4216830897331239,
                  "rejected_mean_error": 1.922187522138868,
                  "gap_rejected_minus_accepted": 0.5005044324057442
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.501996248960495,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.235079050745283,
                  "rejected_mean_error": 1.8175540576662337,
                  "gap_rejected_minus_accepted": 0.5824750069209508
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.166893959045411,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.609111726284027,
                  "rejected_mean_error": 2.4950192740985324,
                  "gap_rejected_minus_accepted": 0.8859075478145053
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.973763257265091,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5540998822166807,
                  "rejected_mean_error": 2.1285102776118685,
                  "gap_rejected_minus_accepted": 0.5744103953951878
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.732030987739563,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.448102070604052,
                  "rejected_mean_error": 1.9473028915269035,
                  "gap_rejected_minus_accepted": 0.49920082092285156
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5288409292697906,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.249675236429487,
                  "rejected_mean_error": 1.8470448959441412,
                  "gap_rejected_minus_accepted": 0.5973696595146543
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
        "best_epoch": 72,
        "best_calib_loss": 0.009327500127255917,
        "train_time_sec": 41.497315883636475,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9988532386291886,
              "spearman": 0.9977938191206933,
              "auroc_top30_bad": 0.9992751904761905,
              "mae": 0.027981114324617373,
              "mse": 0.001482301817098106,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6716683701433721,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0016078383140265941
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16920238501876592
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.46755253198072316
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7867767316177487
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1139734886761754
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9979401199093495,
              "spearman": 0.997865705474577,
              "auroc_top30_worst": 0.9986855238095238,
              "pairwise_seed_ranking": 0.9606,
              "predicted_best_mean_error": 1.4528683392703534,
              "seed0_mean_error": 1.5283110035955907,
              "random_seed_mean_error": 1.5151066114902496,
              "oracle_best_mean_error": 1.45196512183547,
              "improvement_over_seed0": 0.07544266432523727,
              "gap_to_oracle": 0.0009032174348833077,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5882499651908875
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7985614237785339
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0484724155902863
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2620056213696798
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5148110565423965
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3121564388275146,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3964354226589202,
                  "rejected_mean_error": 2.580191761493683,
                  "gap_rejected_minus_accepted": 1.1837563388347627
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.90761798620224,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2620056213696798,
                  "rejected_mean_error": 2.2732273620605468,
                  "gap_rejected_minus_accepted": 1.011221740690867
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.523336112499237,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0484724155902863,
                  "rejected_mean_error": 1.9811496974945069,
                  "gap_rejected_minus_accepted": 0.9326772819042206
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.10453400015831,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7985614237785339,
                  "rejected_mean_error": 1.7535609341303509,
                  "gap_rejected_minus_accepted": 0.954999510351817
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.354067659378052,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.406764752500587,
                  "rejected_mean_error": 2.6222272634506227,
                  "gap_rejected_minus_accepted": 1.2154625109500357
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9395800828933716,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2699609214862189,
                  "rejected_mean_error": 2.303361249923706,
                  "gap_rejected_minus_accepted": 1.033400328437487
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5489963293075562,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0533610633015633,
                  "rejected_mean_error": 2.003260943889618,
                  "gap_rejected_minus_accepted": 0.9498998805880547
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1039137542247772,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7996081749200821,
                  "rejected_mean_error": 1.7712119464874267,
                  "gap_rejected_minus_accepted": 0.9716037715673447
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9880509474146881,
              "spearman": 0.9829170410767031,
              "auroc_top30_bad": 0.9974910476190476,
              "mae": 0.09936558264297855,
              "mse": 0.020228287205186754,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7779966964871474,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1103597485423088
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19903178403377533
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5114872169613838
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9109963404417037
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3029261555254459
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9857135504921347,
              "spearman": 0.9921863814312842,
              "auroc_top30_worst": 0.9915398095238095,
              "pairwise_seed_ranking": 0.9284,
              "predicted_best_mean_error": 1.8273741245269775,
              "seed0_mean_error": 1.917619425535202,
              "random_seed_mean_error": 1.8991771894693374,
              "oracle_best_mean_error": 1.8251729023456573,
              "improvement_over_seed0": 0.09024530100822448,
              "gap_to_oracle": 0.0022012221813201283,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7732540459632874
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0361385055077381
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3360704977035522
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6101300176272768
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.901424583721161
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6665385484695436,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7648410143322415,
                  "rejected_mean_error": 3.1306767082214355,
                  "gap_rejected_minus_accepted": 1.365835693889194
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.37418794631958,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6093245469900435,
                  "rejected_mean_error": 2.775858240005688,
                  "gap_rejected_minus_accepted": 1.1665336930156447
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9594030380249023,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3360704977035522,
                  "rejected_mean_error": 2.4667786697387695,
                  "gap_rejected_minus_accepted": 1.1307081720352172
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.374585747718811,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0371572110599603,
                  "rejected_mean_error": 2.1901286260295447,
                  "gap_rejected_minus_accepted": 1.1529714149695844
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.725738215446472,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7773317948977152,
                  "rejected_mean_error": 3.180208101272583,
                  "gap_rejected_minus_accepted": 1.402876306374868
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.41898912191391,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6187887201334703,
                  "rejected_mean_error": 2.804624852680025,
                  "gap_rejected_minus_accepted": 1.1858361325465545
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9741421341896057,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3415840516090394,
                  "rejected_mean_error": 2.493654799461365,
                  "gap_rejected_minus_accepted": 1.1520707478523255
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4001624882221222,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0394421352280512,
                  "rejected_mean_error": 2.2134759457991087,
                  "gap_rejected_minus_accepted": 1.1740338105710575
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9666527964625031,
              "spearman": 0.9573698120643206,
              "auroc_top30_bad": 0.9983558095238094,
              "mae": 0.15592455433465002,
              "mse": 0.07314449365649303,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.6475716040278837,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13674295711517334
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2366432663679123
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4848922364473343
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7779029980182648
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2224939480662347
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9782705163465658,
              "spearman": 0.9927370316397004,
              "auroc_top30_worst": 0.999472761904762,
              "pairwise_seed_ranking": 0.9192,
              "predicted_best_mean_error": 1.654304592370987,
              "seed0_mean_error": 1.7280002343654632,
              "random_seed_mean_error": 1.7201814349889755,
              "oracle_best_mean_error": 1.6515287026166916,
              "improvement_over_seed0": 0.07369564199447631,
              "gap_to_oracle": 0.0027758897542953243,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.518191677570343
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7519652793804804
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0085337409973145
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2583669022456416
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7233014276504517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7399646043777466,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4907569188012018,
                  "rejected_mean_error": 3.8162020072937013,
                  "gap_rejected_minus_accepted": 2.3254450884924998
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.271467447280884,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2572669850596752,
                  "rejected_mean_error": 3.1184268995595814,
                  "gap_rejected_minus_accepted": 1.8611599144999063
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4313231110572815,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0085337409973145,
                  "rejected_mean_error": 2.438069114303589,
                  "gap_rejected_minus_accepted": 1.4295353733062743
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0504808723926544,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7531576129955987,
                  "rejected_mean_error": 2.047372947380408,
                  "gap_rejected_minus_accepted": 1.2942153343848095
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7344619274139403,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4903555199835035,
                  "rejected_mean_error": 3.866802663803101,
                  "gap_rejected_minus_accepted": 2.3764471438195973
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.327612519264221,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2572528853773433,
                  "rejected_mean_error": 3.125297921044486,
                  "gap_rejected_minus_accepted": 1.8680450356671425
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4175466299057007,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0029555535316468,
                  "rejected_mean_error": 2.4530449151992797,
                  "gap_rejected_minus_accepted": 1.450089361667633
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0739286839962006,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7502584334403749,
                  "rejected_mean_error": 2.0573998785273915,
                  "gap_rejected_minus_accepted": 1.3071414450870167
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9853416919220448,
              "spearman": 0.9826938012840296,
              "auroc_top30_bad": 0.9892808551992225,
              "mae": 0.08616908589999574,
              "mse": 0.01586889566557056,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9857142857142858,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6773299035724134,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08124837587986673
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20377193378550665
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5574031318511282
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9114567639430364
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1861764596828392
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9805874279428557,
              "spearman": 0.9716191724006433,
              "auroc_top30_worst": 0.9772206025267249,
              "pairwise_seed_ranking": 0.9164285714285715,
              "predicted_best_mean_error": 1.6156220819268907,
              "seed0_mean_error": 1.6977024810654777,
              "random_seed_mean_error": 1.668839773961476,
              "oracle_best_mean_error": 1.6144805014133454,
              "improvement_over_seed0": 0.082080399138587,
              "gap_to_oracle": 0.0011415805135452928,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0229725122451783
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2346715722765242
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4075007006100246
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5236636740820748
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6719353059359958
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.044001841545105,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.5879096411523366,
                  "rejected_mean_error": 2.428166288988931,
                  "gap_rejected_minus_accepted": 0.8402566478365945
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8482037484645844,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5236636740820748,
                  "rejected_mean_error": 2.116750201497759,
                  "gap_rejected_minus_accepted": 0.5930865274156842
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6943624019622803,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4075007006100246,
                  "rejected_mean_error": 1.9363699112619672,
                  "gap_rejected_minus_accepted": 0.5288692106519426
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3940529823303223,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2346715722765242,
                  "rejected_mean_error": 1.8176898838224864,
                  "gap_rejected_minus_accepted": 0.5830183115459622
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0123526811599732,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6068684581726316,
                  "rejected_mean_error": 2.5152086871010915,
                  "gap_rejected_minus_accepted": 0.9083402289284599
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8998421728610992,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.543989830925351,
                  "rejected_mean_error": 2.1588404314858574,
                  "gap_rejected_minus_accepted": 0.6148506005605063
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7279720306396484,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.430674924169268,
                  "rejected_mean_error": 1.9647300379616874,
                  "gap_rejected_minus_accepted": 0.5340551137924194
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4241391718387604,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.246507808140346,
                  "rejected_mean_error": 1.848100705373855,
                  "gap_rejected_minus_accepted": 0.601592897233509
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
        "best_epoch": 49,
        "best_calib_loss": 0.009548784233629704,
        "train_time_sec": 28.948766708374023,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9987260483800837,
              "spearman": 0.9977077284017521,
              "auroc_top30_bad": 0.9995814285714285,
              "mae": 0.027655256402206122,
              "mse": 0.0015645414350222056,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6716927079285955,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.004623507048934698
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1696882917150855
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4675389390937984
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7867249706581235
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1139734886761754
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9986447228569005,
              "spearman": 0.9984425639296652,
              "auroc_top30_worst": 0.999144,
              "pairwise_seed_ranking": 0.9565,
              "predicted_best_mean_error": 1.4524389708936214,
              "seed0_mean_error": 1.5283110035955907,
              "random_seed_mean_error": 1.5151066114902496,
              "oracle_best_mean_error": 1.45196512183547,
              "improvement_over_seed0": 0.0758720327019693,
              "gap_to_oracle": 0.00047384905815128775,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5875000538825988
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7981806708335877
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0484732151031495
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2616600030581155
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5148110565423965
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2795935153961184,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3962873389720918,
                  "rejected_mean_error": 2.58152451467514,
                  "gap_rejected_minus_accepted": 1.1852371757030484
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9107054471969604,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2616600030581155,
                  "rejected_mean_error": 2.274264216995239,
                  "gap_rejected_minus_accepted": 1.0126042139371236
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.529463768005371,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0484732151031495,
                  "rejected_mean_error": 1.9811488979816436,
                  "gap_rejected_minus_accepted": 0.9326756828784941
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.111240029335022,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7981806708335877,
                  "rejected_mean_error": 1.7536878517786663,
                  "gap_rejected_minus_accepted": 0.9555071809450786
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.306864929199219,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.4065673408574528,
                  "rejected_mean_error": 2.6240039682388305,
                  "gap_rejected_minus_accepted": 1.2174366273813777
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.934706300497055,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2699441910187403,
                  "rejected_mean_error": 2.3034114413261415,
                  "gap_rejected_minus_accepted": 1.0334672503074012
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5355581641197205,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.053706815779209,
                  "rejected_mean_error": 2.002915191411972,
                  "gap_rejected_minus_accepted": 0.9492083756327627
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1156458854675293,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7995194817781448,
                  "rejected_mean_error": 1.7712415108680726,
                  "gap_rejected_minus_accepted": 0.9717220290899278
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9889234452990068,
              "spearman": 0.9869027818106976,
              "auroc_top30_bad": 0.9966384761904762,
              "mae": 0.1017347622588628,
              "mse": 0.0211584129994673,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7647585659199366,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07580770009756088
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18505758798122407
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5121730597615242
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9119951571861903
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3029261555254459
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9806163009028053,
              "spearman": 0.9881055355372731,
              "auroc_top30_worst": 0.9858133333333333,
              "pairwise_seed_ranking": 0.9264,
              "predicted_best_mean_error": 1.8263175945281982,
              "seed0_mean_error": 1.917619425535202,
              "random_seed_mean_error": 1.8991771894693374,
              "oracle_best_mean_error": 1.8251729023456573,
              "improvement_over_seed0": 0.09130183100700373,
              "gap_to_oracle": 0.001144692182540874,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7638225975036621
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0375534548209264
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.337338084793091
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6114341016771443
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.901424583721161
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5436958074569715,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7658874275419447,
                  "rejected_mean_error": 3.1212589893341063,
                  "gap_rejected_minus_accepted": 1.3553715617921616
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3255878686904907,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6106363695230148,
                  "rejected_mean_error": 2.771931154659381,
                  "gap_rejected_minus_accepted": 1.161294785136366
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.933117687702179,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.337338084793091,
                  "rejected_mean_error": 2.465511082649231,
                  "gap_rejected_minus_accepted": 1.12817299785614
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3222702741622925,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0386623505967112,
                  "rejected_mean_error": 2.189625841958037,
                  "gap_rejected_minus_accepted": 1.1509634913613258
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5833178997039794,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7773317948977152,
                  "rejected_mean_error": 3.180208101272583,
                  "gap_rejected_minus_accepted": 1.402876306374868
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3569262623786926,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6213921936438045,
                  "rejected_mean_error": 2.796897082101731,
                  "gap_rejected_minus_accepted": 1.1755048884579267
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9554831981658936,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3443017315864563,
                  "rejected_mean_error": 2.490937119483948,
                  "gap_rejected_minus_accepted": 1.1466353878974915
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3541024029254913,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0394421352280512,
                  "rejected_mean_error": 2.2134759457991087,
                  "gap_rejected_minus_accepted": 1.1740338105710575
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.969116345599341,
              "spearman": 0.9728807393521344,
              "auroc_top30_bad": 0.998472380952381,
              "mae": 0.15036334946726743,
              "mse": 0.07741413328935794,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6519451811770659,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09964229321479798
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21486678640842438
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.46761410353183747
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7775826173623402
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2224939480662347
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9705090732730062,
              "spearman": 0.9925979559666919,
              "auroc_top30_worst": 0.9997104761904761,
              "pairwise_seed_ranking": 0.9324,
              "predicted_best_mean_error": 1.6538608875274659,
              "seed0_mean_error": 1.7280002343654632,
              "random_seed_mean_error": 1.7201814349889755,
              "oracle_best_mean_error": 1.6515287026166916,
              "improvement_over_seed0": 0.07413934683799739,
              "gap_to_oracle": 0.0023321849107742487,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5162898659706116
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7530123482529933
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0086756399154664
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.258487234745961
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7233014276504517
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6261893033981325,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.493075378841824,
                  "rejected_mean_error": 3.7953358669281005,
                  "gap_rejected_minus_accepted": 2.3022604880862767
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.193082094192505,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.257432095905251,
                  "rejected_mean_error": 3.1179326220442314,
                  "gap_rejected_minus_accepted": 1.8605005261389804
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4343767762184143,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0086756399154664,
                  "rejected_mean_error": 2.437927215385437,
                  "gap_rejected_minus_accepted": 1.4292515754699708
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0559536516666412,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7537957089015851,
                  "rejected_mean_error": 2.0471597947458573,
                  "gap_rejected_minus_accepted": 1.293364085844272
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.613828492164612,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.492868902153439,
                  "rejected_mean_error": 3.844182224273682,
                  "gap_rejected_minus_accepted": 2.3513133221202427
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.254704773426056,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.256153654605947,
                  "rejected_mean_error": 3.1285607171437095,
                  "gap_rejected_minus_accepted": 1.8724070625377625
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4265276193618774,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0031077284812928,
                  "rejected_mean_error": 2.452892740249634,
                  "gap_rejected_minus_accepted": 1.449785011768341
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0508008301258087,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7492875210822575,
                  "rejected_mean_error": 2.057726977343228,
                  "gap_rejected_minus_accepted": 1.3084394562609702
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9858207396339632,
              "spearman": 0.982874648378999,
              "auroc_top30_bad": 0.9902696793002915,
              "mae": 0.08515991014695032,
              "mse": 0.01557053936332127,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9857142857142858,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7002179961072839,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07633704702769006
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.189866518335683
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.559061532829489
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.911304241333689
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1861764596828392
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9631220729546456,
              "spearman": 0.9595534101673093,
              "auroc_top30_worst": 0.9680077745383868,
              "pairwise_seed_ranking": 0.91,
              "predicted_best_mean_error": 1.617756543840681,
              "seed0_mean_error": 1.6977024810654777,
              "random_seed_mean_error": 1.668839773961476,
              "oracle_best_mean_error": 1.6144805014133454,
              "improvement_over_seed0": 0.07994593722479681,
              "gap_to_oracle": 0.0032760424273354793,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0617338725498744
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2466573388235909
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.408250413281577
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5261890511285692
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6719353059359958
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.035060095787048,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.5881554132416136,
                  "rejected_mean_error": 2.425954340185438,
                  "gap_rejected_minus_accepted": 0.8377989269438244
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9186067879199982,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5261890511285692,
                  "rejected_mean_error": 2.1091740703582764,
                  "gap_rejected_minus_accepted": 0.5829850192297072
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7087910771369934,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.408250413281577,
                  "rejected_mean_error": 1.935620198590415,
                  "gap_rejected_minus_accepted": 0.5273697853088379
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.485179841518402,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2466573388235909,
                  "rejected_mean_error": 1.8136946283067976,
                  "gap_rejected_minus_accepted": 0.5670372894832068
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.035475564002991,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.607087930989644,
                  "rejected_mean_error": 2.5132334317479814,
                  "gap_rejected_minus_accepted": 0.9061455007583374
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9545564949512482,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5503975221088955,
                  "rejected_mean_error": 2.1396173579352245,
                  "gap_rejected_minus_accepted": 0.589219835826329
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7163456678390503,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4281750151089259,
                  "rejected_mean_error": 1.9672299470220294,
                  "gap_rejected_minus_accepted": 0.5390549319131035
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.498728722333908,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.2637456280844552,
                  "rejected_mean_error": 1.8423547653924852,
                  "gap_rejected_minus_accepted": 0.57860913730803
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
        "best_epoch": 39,
        "best_calib_loss": 0.061259925365448,
        "train_time_sec": 10.710383892059326,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9659540573446208,
              "spearman": 0.936186404773606,
              "auroc_top30_bad": 0.9986592857142857,
              "mae": 0.11082212742057164,
              "mse": 0.03848030315707588,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.505,
              "expert_lt_simvla_seed0": 0.968,
              "same_context_pred_std": 0.6633732474760966,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.30984582643955944
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.32215313795208933
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45800251290923916
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7647754046369034
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0947616972393124
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9965355348900903,
              "spearman": 0.9967217066207107,
              "auroc_top30_worst": 0.9987428571428572,
              "pairwise_seed_ranking": 0.823,
              "predicted_best_mean_error": 1.4341827961206437,
              "seed0_mean_error": 1.5024782748818397,
              "random_seed_mean_error": 1.489593738168478,
              "oracle_best_mean_error": 1.42773129427433,
              "improvement_over_seed0": 0.06829547876119602,
              "gap_to_oracle": 0.006451501846313601,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5612729603648186
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7607904669523239
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0134886668562888
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2306802282253901
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4892081375062465
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.309222435951233,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3687962827086448,
                  "rejected_mean_error": 2.572914830684662,
                  "gap_rejected_minus_accepted": 1.204118547976017
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9173945486545563,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2306802282253901,
                  "rejected_mean_error": 2.264791865348816,
                  "gap_rejected_minus_accepted": 1.0341116371234258
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5133116841316223,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0134886668562888,
                  "rejected_mean_error": 1.9649276081562042,
                  "gap_rejected_minus_accepted": 0.9514389412999154
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0721501111984253,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7607904669523239,
                  "rejected_mean_error": 1.7320140276908875,
                  "gap_rejected_minus_accepted": 0.9712235607385636
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3511783838272096,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3789773464865154,
                  "rejected_mean_error": 2.6139866304397583,
                  "gap_rejected_minus_accepted": 1.235009283953243
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.946398764848709,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2385550674597423,
                  "rejected_mean_error": 2.294247897148132,
                  "gap_rejected_minus_accepted": 1.0556928296883898
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.539924681186676,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0187270883321762,
                  "rejected_mean_error": 1.9862294614315033,
                  "gap_rejected_minus_accepted": 0.9675023730993271
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0755704045295715,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7621658895015716,
                  "rejected_mean_error": 1.7492490700085959,
                  "gap_rejected_minus_accepted": 0.9870831805070243
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8788932527942701,
              "spearman": 0.8576786339731947,
              "auroc_top30_bad": 0.9277188571428571,
              "mae": 0.3447393627494574,
              "mse": 0.20596289225473782,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.532,
              "expert_lt_simvla_seed0": 0.964,
              "same_context_pred_std": 0.7071765644714074,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.366600058734417
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4205842200756073
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.639621329587698
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.020990881383419
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3668533629089594
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.770974546477154,
              "spearman": 0.7517646201373569,
              "auroc_top30_worst": 0.8844099047619048,
              "pairwise_seed_ranking": 0.7844,
              "predicted_best_mean_error": 1.9246192054748534,
              "seed0_mean_error": 2.0036536955833437,
              "random_seed_mean_error": 1.9847015753984452,
              "oracle_best_mean_error": 1.9103146924972534,
              "improvement_over_seed0": 0.07903449010849029,
              "gap_to_oracle": 0.014304512977600048,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9909879198074341
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3260947148769329
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5598609354972839
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.768055087150033
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9867968246936798
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.500607943534851,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8916475975778368,
                  "rejected_mean_error": 2.8431398687362672,
                  "gap_rejected_minus_accepted": 0.9514922711584304
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.199409067630768,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7673904907868792,
                  "rejected_mean_error": 2.6436138690089264,
                  "gap_rejected_minus_accepted": 0.8762233782220472
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8256444334983826,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5598609354972839,
                  "rejected_mean_error": 2.4137327138900755,
                  "gap_rejected_minus_accepted": 0.8538717783927916
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2508539259433746,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3259859782057448,
                  "rejected_mean_error": 2.2075372675439717,
                  "gap_rejected_minus_accepted": 0.8815512893382269
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.548866319656372,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.9058090877532958,
                  "rejected_mean_error": 2.884255166053772,
                  "gap_rejected_minus_accepted": 0.9784460783004763
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.19847172498703,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7766359687488984,
                  "rejected_mean_error": 2.6774999641236805,
                  "gap_rejected_minus_accepted": 0.9008639953747821
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8449023962020874,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5721322364807129,
                  "rejected_mean_error": 2.4351751546859743,
                  "gap_rejected_minus_accepted": 0.8630429182052615
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2739618122577667,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3126715705508278,
                  "rejected_mean_error": 2.236444464979325,
                  "gap_rejected_minus_accepted": 0.9237728944284971
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.778723182256146,
              "spearman": 0.820171447128858,
              "auroc_top30_bad": 0.966560761904762,
              "mae": 0.43303422421216964,
              "mse": 0.43247365060942977,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.532,
              "expert_lt_simvla_seed0": 0.956,
              "same_context_pred_std": 0.6401967026756401,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.37397872912883756
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4251894574165344
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.543724456846714
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8935892188310623
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2662243917644025
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6734608074808659,
              "spearman": 0.7750334191573883,
              "auroc_top30_worst": 0.8647497142857143,
              "pairwise_seed_ranking": 0.7528,
              "predicted_best_mean_error": 1.7343595257997513,
              "seed0_mean_error": 1.7913558595180512,
              "random_seed_mean_error": 1.7836234430074691,
              "oracle_best_mean_error": 1.7148182896375657,
              "improvement_over_seed0": 0.05699633371829993,
              "gap_to_oracle": 0.019541236162185616,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6134021551609039
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8468811813837442
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2239903972625732
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4926704716072408
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7866378999710082
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.375497388839722,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6506620199415418,
                  "rejected_mean_error": 3.010420820236206,
                  "gap_rejected_minus_accepted": 1.3597588002946641
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.075521469116211,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4915705725884616,
                  "rejected_mean_error": 2.669954467886172,
                  "gap_rejected_minus_accepted": 1.1783838952977106
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5177450776100159,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2239903972625732,
                  "rejected_mean_error": 2.349285402679443,
                  "gap_rejected_minus_accepted": 1.12529500541687
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9880377948284149,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8463897952637353,
                  "rejected_mean_error": 2.1007229125359776,
                  "gap_rejected_minus_accepted": 1.2543331172722425
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.407939386367798,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.645957044230567,
                  "rejected_mean_error": 3.0999451971054075,
                  "gap_rejected_minus_accepted": 1.4539881528748404
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1067326068878174,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.483804333337488,
                  "rejected_mean_error": 2.704246897546072,
                  "gap_rejected_minus_accepted": 1.220442564208584
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4732629656791687,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.192793008327484,
                  "rejected_mean_error": 2.389918710708618,
                  "gap_rejected_minus_accepted": 1.197125702381134
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9864311963319778,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8318652520104061,
                  "rejected_mean_error": 2.114606705897632,
                  "gap_rejected_minus_accepted": 1.2827414538872262
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.8250221576709597,
              "spearman": 0.8181387192384336,
              "auroc_top30_bad": 0.8999878522837705,
              "mae": 0.34371352867888555,
              "mse": 0.20800987168983648,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.4857142857142857,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6358630908161184,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.29364793449640275
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3871077856847218
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6602526281774044
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9502445340014639
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1954890575472799
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.5975885493931344,
              "spearman": 0.5020816194085527,
              "auroc_top30_worst": 0.738357628765792,
              "pairwise_seed_ranking": 0.755,
              "predicted_best_mean_error": 1.6484816338334765,
              "seed0_mean_error": 1.7152771362236567,
              "random_seed_mean_error": 1.6870648052011217,
              "oracle_best_mean_error": 1.6339054865496498,
              "improvement_over_seed0": 0.06679550239018028,
              "gap_to_oracle": 0.014576147283826613,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4275371423789434
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4865734553337098
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.505978742667607
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.592711459114438
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.690144100700106
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2584401369094858,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6154390738123938,
                  "rejected_mean_error": 2.362489342689514,
                  "gap_rejected_minus_accepted": 0.7470502688771203
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8216992020606995,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.592711459114438,
                  "rejected_mean_error": 1.9824420254571098,
                  "gap_rejected_minus_accepted": 0.3897305663426718
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3664536476135254,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.505978742667607,
                  "rejected_mean_error": 1.874309458732605,
                  "gap_rejected_minus_accepted": 0.368330716064998
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9906788021326065,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.4865734553337098,
                  "rejected_mean_error": 1.7580009824889047,
                  "gap_rejected_minus_accepted": 0.2714275271551949
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3357234001159677,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6340596647489638,
                  "rejected_mean_error": 2.4462343794958934,
                  "gap_rejected_minus_accepted": 0.8121747147469296
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8795771598815918,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.6020998829887028,
                  "rejected_mean_error": 2.054808895928519,
                  "gap_rejected_minus_accepted": 0.45270901293981614
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3702298402786255,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.5123478276388986,
                  "rejected_mean_error": 1.918206444808415,
                  "gap_rejected_minus_accepted": 0.40585861716951643
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0059151202440262,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.4767810753413608,
                  "rejected_mean_error": 1.7947758231844222,
                  "gap_rejected_minus_accepted": 0.31799474784306136
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
        "best_epoch": 27,
        "best_calib_loss": 0.01907186210155487,
        "train_time_sec": 35.06122136116028,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9992356906019193,
              "spearman": 0.998229812555115,
              "auroc_top30_bad": 0.9998155952380953,
              "mae": 0.04145395858001429,
              "mse": 0.002252953768355968,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.663855148212263,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05948883719253354
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1854222443963401
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.449504618252581
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7643307019321558
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0947616972393124
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9995139954474137,
              "spearman": 0.9996010286400219,
              "auroc_top30_worst": 0.9998363809523809,
              "pairwise_seed_ranking": 0.9334,
              "predicted_best_mean_error": 1.4288804573714733,
              "seed0_mean_error": 1.5024782748818397,
              "random_seed_mean_error": 1.489593738168478,
              "oracle_best_mean_error": 1.42773129427433,
              "improvement_over_seed0": 0.07359781751036643,
              "gap_to_oracle": 0.001149163097143191,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5515759510397911
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7596446360349656
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.012761722791195
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2301598772923152
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4892081375062465
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3081351757049564,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3683932284182971,
                  "rejected_mean_error": 2.5765423192977903,
                  "gap_rejected_minus_accepted": 1.2081490908794932
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9224460124969482,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2301598772923152,
                  "rejected_mean_error": 2.2663529181480406,
                  "gap_rejected_minus_accepted": 1.0361930408557254
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5261276960372925,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.012761722791195,
                  "rejected_mean_error": 1.9656545522212983,
                  "gap_rejected_minus_accepted": 0.9528928294301033
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1130644381046295,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7596446360349656,
                  "rejected_mean_error": 1.732395971330007,
                  "gap_rejected_minus_accepted": 0.9727513352950414
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3418854475021362,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3787130422724618,
                  "rejected_mean_error": 2.6163653683662416,
                  "gap_rejected_minus_accepted": 1.2376523260937797
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9421842992305756,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2380525651772818,
                  "rejected_mean_error": 2.2957554039955137,
                  "gap_rejected_minus_accepted": 1.057702838818232
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5403233766555786,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0178385323286057,
                  "rejected_mean_error": 1.9871180174350738,
                  "gap_rejected_minus_accepted": 0.9692794851064681
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1143212914466858,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7613313987255096,
                  "rejected_mean_error": 1.7495272336006165,
                  "gap_rejected_minus_accepted": 0.9881958348751069
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9741545693283099,
              "spearman": 0.9691261341970778,
              "auroc_top30_bad": 0.9775573333333334,
              "mae": 0.1521097280085087,
              "mse": 0.04771736932289654,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.782467521071422,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1196734054684639
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2562798325419426
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5658298616707325
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9867209255417188
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3668533629089594
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.941440785112914,
              "spearman": 0.9317596972542064,
              "auroc_top30_worst": 0.956736,
              "pairwise_seed_ranking": 0.9092,
              "predicted_best_mean_error": 1.9116981233358383,
              "seed0_mean_error": 2.0036536955833437,
              "random_seed_mean_error": 1.9847015753984452,
              "oracle_best_mean_error": 1.9103146924972534,
              "improvement_over_seed0": 0.09195557224750539,
              "gap_to_oracle": 0.0013834308385849425,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8507221446037293
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1223186306082285
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4702358553886414
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7284418934825132
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9867968246936798
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.596204257011414,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8595298744307625,
                  "rejected_mean_error": 3.1321993770599366,
                  "gap_rejected_minus_accepted": 1.272669502629174
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3668421506881714,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7278126319800777,
                  "rejected_mean_error": 2.762094551762834,
                  "gap_rejected_minus_accepted": 1.0342819197827562
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9598975777626038,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4702358553886414,
                  "rejected_mean_error": 2.503357793998718,
                  "gap_rejected_minus_accepted": 1.0331219386100767
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4196902811527252,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1238403543115805,
                  "rejected_mean_error": 2.2750629668810833,
                  "gap_rejected_minus_accepted": 1.1512226125695029
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.621954321861267,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8729254282845391,
                  "rejected_mean_error": 3.180208101272583,
                  "gap_rejected_minus_accepted": 1.307282672988044
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.379268229007721,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7394446491557647,
                  "rejected_mean_error": 2.787893246090601,
                  "gap_rejected_minus_accepted": 1.0484485969348365
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.969473659992218,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.481364520072937,
                  "rejected_mean_error": 2.52594287109375,
                  "gap_rejected_minus_accepted": 1.044578351020813
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4277868866920471,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.130160507701692,
                  "rejected_mean_error": 2.297932149254702,
                  "gap_rejected_minus_accepted": 1.1677716415530097
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9527583635346978,
              "spearman": 0.9767959162746015,
              "auroc_top30_bad": 0.9981089523809524,
              "mae": 0.19977759359404446,
              "mse": 0.1339008773310763,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6586112593598942,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11533558493852615
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2190978503704071
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.49245262686014174
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7939451288461685
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2662243917644025
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9436125241462968,
              "spearman": 0.987599685887799,
              "auroc_top30_worst": 0.9949135238095238,
              "pairwise_seed_ranking": 0.9008,
              "predicted_best_mean_error": 1.7188768733739852,
              "seed0_mean_error": 1.7913558595180512,
              "random_seed_mean_error": 1.7836234430074691,
              "oracle_best_mean_error": 1.7148182896375657,
              "improvement_over_seed0": 0.072478986144066,
              "gap_to_oracle": 0.004058583736419541,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.503046268939972
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7511981712319912
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0069647325515747
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.268490892229304
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7866378999710082
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.563035869598389,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5671042544047038,
                  "rejected_mean_error": 3.762440710067749,
                  "gap_rejected_minus_accepted": 2.1953364556630452
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.155940532684326,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2673606531597126,
                  "rejected_mean_error": 3.341151574930063,
                  "gap_rejected_minus_accepted": 2.0737909217703505
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.51714026927948,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0069647325515747,
                  "rejected_mean_error": 2.566311067390442,
                  "gap_rejected_minus_accepted": 1.5593463348388672
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1315181255340576,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7521306910453894,
                  "rejected_mean_error": 2.13220967840614,
                  "gap_rejected_minus_accepted": 1.3800789873607506
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5476937294006348,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5661834300888908,
                  "rejected_mean_error": 3.8179077243804933,
                  "gap_rejected_minus_accepted": 2.2517242942916025
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.166514277458191,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2679251231611732,
                  "rejected_mean_error": 3.345031219815451,
                  "gap_rejected_minus_accepted": 2.0771060966542776
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5008864998817444,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.00206329870224,
                  "rejected_mean_error": 2.5806484203338624,
                  "gap_rejected_minus_accepted": 1.5785851216316225
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1257940232753754,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7508940422345721,
                  "rejected_mean_error": 2.141885776570774,
                  "gap_rejected_minus_accepted": 1.3909917343362022
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9803302104931702,
              "spearman": 0.9674448465231275,
              "auroc_top30_bad": 0.9757361516034985,
              "mae": 0.12332146063846137,
              "mse": 0.025827232561738578,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9714285714285714,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7161897623430554,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10507439917751721
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22693664201668332
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5603698834138258
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9215679521645819
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1954890575472799
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9477097924637258,
              "spearman": 0.9157169008799725,
              "auroc_top30_worst": 0.9262293488824102,
              "pairwise_seed_ranking": 0.8964285714285715,
              "predicted_best_mean_error": 1.6371976937566484,
              "seed0_mean_error": 1.7152771362236567,
              "random_seed_mean_error": 1.6870648052011217,
              "oracle_best_mean_error": 1.6339054865496498,
              "improvement_over_seed0": 0.07807944246700838,
              "gap_to_oracle": 0.003292207206998521,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0225807326180594
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2546760436466762
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4310904240608215
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5467152808961415
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.690144100700106
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.135689210891724,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6109538394307332,
                  "rejected_mean_error": 2.4028564521244595,
                  "gap_rejected_minus_accepted": 0.7919026126937263
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9655471444129944,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5467152808961415,
                  "rejected_mean_error": 2.1204305601119997,
                  "gap_rejected_minus_accepted": 0.5737152792158582
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7551852464675903,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4310904240608215,
                  "rejected_mean_error": 1.9491977773393903,
                  "gap_rejected_minus_accepted": 0.5181073532785687
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5276165902614594,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2546760436466762,
                  "rejected_mean_error": 1.835300119717916,
                  "gap_rejected_minus_accepted": 0.5806240760712398
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.189045763015747,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.626615325609843,
                  "rejected_mean_error": 2.5132334317479814,
                  "gap_rejected_minus_accepted": 0.8866181061381384
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9802433848381042,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5696260611216226,
                  "rejected_mean_error": 2.152230361529759,
                  "gap_rejected_minus_accepted": 0.5826043004081363
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.765949308872223,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4521019680159433,
                  "rejected_mean_error": 1.9784523044313704,
                  "gap_rejected_minus_accepted": 0.5263503364154272
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.541961520910263,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.2634109258651733,
                  "rejected_mean_error": 1.8658992063431512,
                  "gap_rejected_minus_accepted": 0.6024882804779779
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
        "best_calib_loss": 0.01882568746805191,
        "train_time_sec": 41.33513879776001,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9991271062479359,
              "spearman": 0.9984025753903341,
              "auroc_top30_bad": 0.9995695476190475,
              "mae": 0.027643137142551132,
              "mse": 0.001200284071090623,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6593103128230682,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05825017204764299
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18510984887136148
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.44960216381675566
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.764498647841656
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0947616972393124
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9987492351951911,
              "spearman": 0.9987421696935659,
              "auroc_top30_worst": 0.9992619047619047,
              "pairwise_seed_ranking": 0.9601,
              "predicted_best_mean_error": 1.428410239368677,
              "seed0_mean_error": 1.5024782748818397,
              "random_seed_mean_error": 1.489593738168478,
              "oracle_best_mean_error": 1.42773129427433,
              "improvement_over_seed0": 0.07406803551316266,
              "gap_to_oracle": 0.000678945094346961,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5521017258763313
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7598338078260422
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.013005578792095
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.230418097615242
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4892081375062465
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.286602830886841,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3684203376703792,
                  "rejected_mean_error": 2.5762983360290526,
                  "gap_rejected_minus_accepted": 1.2078779983586734
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9041898548603058,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.230418097615242,
                  "rejected_mean_error": 2.26557825717926,
                  "gap_rejected_minus_accepted": 1.0351601595640183
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4935951232910156,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.013005578792095,
                  "rejected_mean_error": 1.9654106962203979,
                  "gap_rejected_minus_accepted": 0.9524051174283028
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0909213423728943,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7598338078260422,
                  "rejected_mean_error": 1.7323329140663146,
                  "gap_rejected_minus_accepted": 0.9724991062402725
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.315446949005127,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3786077216598722,
                  "rejected_mean_error": 2.617313253879547,
                  "gap_rejected_minus_accepted": 1.2387055322196747
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9344937205314636,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2381875545978547,
                  "rejected_mean_error": 2.2953504357337953,
                  "gap_rejected_minus_accepted": 1.0571628811359406
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5094842314720154,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.018004438996315,
                  "rejected_mean_error": 1.9869521107673644,
                  "gap_rejected_minus_accepted": 0.9689476717710495
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0933767259120941,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7613972909450532,
                  "rejected_mean_error": 1.7495052695274353,
                  "gap_rejected_minus_accepted": 0.9881079785823822
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9773446543570115,
              "spearman": 0.97008153958328,
              "auroc_top30_bad": 0.9801676190476191,
              "mae": 0.15435362577992492,
              "mse": 0.044660869353720156,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7593220930295498,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15449498707056045
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2597339223265648
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5684026536285878
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9832389794866244
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3668533629089594
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9582229299179854,
              "spearman": 0.9521383629685524,
              "auroc_top30_worst": 0.972327619047619,
              "pairwise_seed_ranking": 0.9188,
              "predicted_best_mean_error": 1.911686942100525,
              "seed0_mean_error": 2.0036536955833437,
              "random_seed_mean_error": 1.9847015753984452,
              "oracle_best_mean_error": 1.9103146924972534,
              "improvement_over_seed0": 0.0919667534828188,
              "gap_to_oracle": 0.0013722496032715359,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8386447319984436
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1185051273459043
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4654563035011292
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7112886580958295
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9867968246936798
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.596241497993469,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8594537697368199,
                  "rejected_mean_error": 3.13288431930542,
                  "gap_rejected_minus_accepted": 1.2734305495686002
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3395296931266785,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7104832671240784,
                  "rejected_mean_error": 2.813971915564979,
                  "gap_rejected_minus_accepted": 1.1034886484409006
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9420289993286133,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4654563035011292,
                  "rejected_mean_error": 2.5081373458862304,
                  "gap_rejected_minus_accepted": 1.0426810423851012
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.379323273897171,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.120376598149443,
                  "rejected_mean_error": 2.276220016698318,
                  "gap_rejected_minus_accepted": 1.1558434185488753
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6008807897567747,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8729233831829495,
                  "rejected_mean_error": 3.1802265071868896,
                  "gap_rejected_minus_accepted": 1.30730312400394
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.387315511703491,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7242971837201857,
                  "rejected_mean_error": 2.832854770478748,
                  "gap_rejected_minus_accepted": 1.1085575867585624
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9554654359817505,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4749620103836059,
                  "rejected_mean_error": 2.532345380783081,
                  "gap_rejected_minus_accepted": 1.057383370399475
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3996406495571136,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.136408115190173,
                  "rejected_mean_error": 2.2958273403147325,
                  "gap_rejected_minus_accepted": 1.1594192251245594
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9617758255173763,
              "spearman": 0.9763850647517459,
              "auroc_top30_bad": 0.9986704761904762,
              "mae": 0.17229253592733293,
              "mse": 0.11462331814944962,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.6490226578103366,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10694927567243576
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21842220962047576
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.48986678988933563
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7909018520593644
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2662243917644025
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9565938813355019,
              "spearman": 0.9880731366868075,
              "auroc_top30_worst": 0.9998841904761905,
              "pairwise_seed_ranking": 0.9308,
              "predicted_best_mean_error": 1.7176981284618378,
              "seed0_mean_error": 1.7913558595180512,
              "random_seed_mean_error": 1.7836234430074691,
              "oracle_best_mean_error": 1.7148182896375657,
              "improvement_over_seed0": 0.07365773105621343,
              "gap_to_oracle": 0.0028798388242721185,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5040338311195374
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7512286387574978
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0083342851638795
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.26243925780884
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7866378999710082
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7230293273925783,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5601340908474393,
                  "rejected_mean_error": 3.8251721820831297,
                  "gap_rejected_minus_accepted": 2.2650380912356907
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2483930587768555,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2601087302001335,
                  "rejected_mean_error": 3.3628610056429245,
                  "gap_rejected_minus_accepted": 2.102752275442791
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.405021071434021,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0083342851638795,
                  "rejected_mean_error": 2.564941514778137,
                  "gap_rejected_minus_accepted": 1.5566072296142577
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.018008142709732,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7522669343140941,
                  "rejected_mean_error": 2.1321641670474376,
                  "gap_rejected_minus_accepted": 1.3798972327333434
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7098737716674806,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5607506590419344,
                  "rejected_mean_error": 3.866802663803101,
                  "gap_rejected_minus_accepted": 2.3060520047611663
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.286992132663727,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2727080956499843,
                  "rejected_mean_error": 3.3308341427454873,
                  "gap_rejected_minus_accepted": 2.058126047095503
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.41201251745224,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0022237696647645,
                  "rejected_mean_error": 2.5804879493713377,
                  "gap_rejected_minus_accepted": 1.5782641797065733
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0230884552001953,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7524836214761885,
                  "rejected_mean_error": 2.1413502498744004,
                  "gap_rejected_minus_accepted": 1.3888666283982118
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9804972356442812,
              "spearman": 0.976707918253875,
              "auroc_top30_bad": 0.9940476190476191,
              "mae": 0.1036671968922019,
              "mse": 0.02150804889923883,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9928571428571429,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6607416969407319,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.14931639560631343
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21940647406237465
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5609723643532821
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9157779141692888
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1954890575472799
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9752598155386816,
              "spearman": 0.9744976739019583,
              "auroc_top30_worst": 0.980242954324587,
              "pairwise_seed_ranking": 0.8985714285714286,
              "predicted_best_mean_error": 1.6358563448701586,
              "seed0_mean_error": 1.7152771362236567,
              "random_seed_mean_error": 1.6870648052011217,
              "oracle_best_mean_error": 1.6339054865496498,
              "improvement_over_seed0": 0.07942079135349811,
              "gap_to_oracle": 0.001950858320508786,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0376209020614624
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2530778414862496
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.41605696780341
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5363088080996559
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.690144100700106
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0087186813354494,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6084154202824548,
                  "rejected_mean_error": 2.4257022244589668,
                  "gap_rejected_minus_accepted": 0.817286804176512
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8634890615940094,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5363088080996559,
                  "rejected_mean_error": 2.1516499785014562,
                  "gap_rejected_minus_accepted": 0.6153411704018004
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6741405725479126,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.41605696780341,
                  "rejected_mean_error": 1.9642312335968017,
                  "gap_rejected_minus_accepted": 0.5481742657933917
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4274618029594421,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2530778414862496,
                  "rejected_mean_error": 1.8358328537713913,
                  "gap_rejected_minus_accepted": 0.5827550122851417
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0050414323806764,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.626615325609843,
                  "rejected_mean_error": 2.5132334317479814,
                  "gap_rejected_minus_accepted": 0.8866181061381384
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.889197677373886,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.558569380215236,
                  "rejected_mean_error": 2.185400404248919,
                  "gap_rejected_minus_accepted": 0.6268310240336827
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7031907439231873,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4384433780397687,
                  "rejected_mean_error": 1.9921108944075447,
                  "gap_rejected_minus_accepted": 0.553667516367776
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4670377373695374,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.2627426658357892,
                  "rejected_mean_error": 1.8661219596862793,
                  "gap_rejected_minus_accepted": 0.60337929385049
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
        "best_epoch": 48,
        "best_calib_loss": 0.02032691240310669,
        "train_time_sec": 29.027923107147217,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995155179189925,
              "spearman": 0.9988182582847225,
              "auroc_top30_bad": 0.9998816666666667,
              "mae": 0.01990107717688661,
              "mse": 0.0006612295253727666,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6657251533097913,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05768702987837605
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18489600370181725
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4494250083816703
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.764305937489712
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0947616972393124
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9995177333638093,
              "spearman": 0.9995985497279225,
              "auroc_top30_worst": 0.9998207619047619,
              "pairwise_seed_ranking": 0.953,
              "predicted_best_mean_error": 1.4284766005277634,
              "seed0_mean_error": 1.5024782748818397,
              "random_seed_mean_error": 1.489593738168478,
              "oracle_best_mean_error": 1.42773129427433,
              "improvement_over_seed0": 0.07400167435407634,
              "gap_to_oracle": 0.0007453062534332755,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5517402659058571
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7594884563207627
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0127355444788932
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2302292678753535
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4892081375062465
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2955626964569094,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3683846091098255,
                  "rejected_mean_error": 2.5766198930740356,
                  "gap_rejected_minus_accepted": 1.20823528396421
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8948870599269867,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2302292678753535,
                  "rejected_mean_error": 2.266144746398926,
                  "gap_rejected_minus_accepted": 1.0359154785235725
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.491453766822815,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0127355444788932,
                  "rejected_mean_error": 1.9656807305336,
                  "gap_rejected_minus_accepted": 0.9529451860547067
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0724430978298187,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7594884563207627,
                  "rejected_mean_error": 1.7324480312347412,
                  "gap_rejected_minus_accepted": 0.9729595749139786
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.317859172821045,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3785576256778505,
                  "rejected_mean_error": 2.617764117717743,
                  "gap_rejected_minus_accepted": 1.2392064920398924
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9186835885047913,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2380368012587228,
                  "rejected_mean_error": 2.29580269575119,
                  "gap_rejected_minus_accepted": 1.0577658944924673
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.506108283996582,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.017884610056877,
                  "rejected_mean_error": 1.9870719397068024,
                  "gap_rejected_minus_accepted": 0.9691873296499254
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0712741017341614,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7610388572216034,
                  "rejected_mean_error": 1.749624747435252,
                  "gap_rejected_minus_accepted": 0.9885858902136486
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9774633893712846,
              "spearman": 0.9713860835949849,
              "auroc_top30_bad": 0.9791607619047619,
              "mae": 0.1609777408497408,
              "mse": 0.05063390406161706,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7425460805683298,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13579724878072738
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24556007932424545
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5695915293514728
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9841178441564242
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3668533629089594
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9541499756673013,
              "spearman": 0.9452192221160158,
              "auroc_top30_worst": 0.9691733333333333,
              "pairwise_seed_ranking": 0.9332,
              "predicted_best_mean_error": 1.9113634572029115,
              "seed0_mean_error": 2.0036536955833437,
              "random_seed_mean_error": 1.9847015753984452,
              "oracle_best_mean_error": 1.9103146924972534,
              "improvement_over_seed0": 0.09229023838043227,
              "gap_to_oracle": 0.0010487647056580673,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8455384039878845
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.125332028628924
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.464512884426117
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.713099706719425
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9867968246936798
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.556200695037842,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8603626811239455,
                  "rejected_mean_error": 3.124704116821289,
                  "gap_rejected_minus_accepted": 1.2643414356973435
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3109476566314697,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7125609099801347,
                  "rejected_mean_error": 2.8077522626700113,
                  "gap_rejected_minus_accepted": 1.0951913526898767
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.88103187084198,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.464512884426117,
                  "rejected_mean_error": 2.5090807649612428,
                  "gap_rejected_minus_accepted": 1.0445678805351257
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3073585331439972,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1268441248625611,
                  "rejected_mean_error": 2.2740595728763267,
                  "gap_rejected_minus_accepted": 1.1472154480137655
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6123307466506955,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8720856873194376,
                  "rejected_mean_error": 3.1877657699584963,
                  "gap_rejected_minus_accepted": 1.3156800826390587
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3484256267547607,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7252393438216838,
                  "rejected_mean_error": 2.8300582000187466,
                  "gap_rejected_minus_accepted": 1.1048188561970629
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8927152156829834,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.472589599609375,
                  "rejected_mean_error": 2.534717791557312,
                  "gap_rejected_minus_accepted": 1.0621281919479368
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3194126784801483,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1353539020296126,
                  "rejected_mean_error": 2.296182503037274,
                  "gap_rejected_minus_accepted": 1.1608286010076614
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9596059315056946,
              "spearman": 0.9716463823474356,
              "auroc_top30_bad": 0.9979207619047619,
              "mae": 0.18653003892400302,
              "mse": 0.12307938365844738,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.6425072684914004,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.16149576830863951
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23134363746643066
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4942469815015793
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.791794313454628
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2662243917644025
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9524997927436402,
              "spearman": 0.986694538940505,
              "auroc_top30_worst": 0.9996007619047619,
              "pairwise_seed_ranking": 0.9248,
              "predicted_best_mean_error": 1.7168575245141984,
              "seed0_mean_error": 1.7913558595180512,
              "random_seed_mean_error": 1.7836234430074691,
              "oracle_best_mean_error": 1.7148182896375657,
              "improvement_over_seed0": 0.07449833500385283,
              "gap_to_oracle": 0.0020392348766327117,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5161791558265686
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7561915434705906
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0071837303161622
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.267013587931326
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7866378999710082
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.548767733573914,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5658975669013129,
                  "rejected_mean_error": 3.7733008975982667,
                  "gap_rejected_minus_accepted": 2.2074033306969536
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2021126747131348,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2646882180343189,
                  "rejected_mean_error": 3.349151804043462,
                  "gap_rejected_minus_accepted": 2.084463586009143
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.421148657798767,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0071837303161622,
                  "rejected_mean_error": 2.5660920696258547,
                  "gap_rejected_minus_accepted": 1.5589083393096925
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.02530437707901,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7577293888448526,
                  "rejected_mean_error": 2.1303394623856153,
                  "gap_rejected_minus_accepted": 1.3726100735407627
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5355508089065553,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5625143461757236,
                  "rejected_mean_error": 3.850929479598999,
                  "gap_rejected_minus_accepted": 2.2884151334232756
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2573870420455933,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.266364265571941,
                  "rejected_mean_error": 3.3496642415485685,
                  "gap_rejected_minus_accepted": 2.0832999759766277
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4072498083114624,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0018821206092834,
                  "rejected_mean_error": 2.580829598426819,
                  "gap_rejected_minus_accepted": 1.5789474778175354
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0266536474227905,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7564809085830809,
                  "rejected_mean_error": 2.1400035702608484,
                  "gap_rejected_minus_accepted": 1.3835226616777674
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9854716016756967,
              "spearman": 0.978527240026913,
              "auroc_top30_bad": 0.9896865889212828,
              "mae": 0.09213160659020235,
              "mse": 0.015722955680496895,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9857142857142858,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6863996035933422,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.12907303699425288
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20561422352279934
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5600592994477067
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9176634026567141
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1954890575472799
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9681097251748499,
              "spearman": 0.9568946525546843,
              "auroc_top30_worst": 0.9658503401360544,
              "pairwise_seed_ranking": 0.8892857142857142,
              "predicted_best_mean_error": 1.635811049597604,
              "seed0_mean_error": 1.7152771362236567,
              "random_seed_mean_error": 1.6870648052011217,
              "oracle_best_mean_error": 1.6339054865496498,
              "improvement_over_seed0": 0.07946608662605281,
              "gap_to_oracle": 0.0019055630479540842,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0304214937346323
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2516851581845965
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4207087319237846
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.539735399427868
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.690144100700106
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0466301679611205,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6080643621702042,
                  "rejected_mean_error": 2.4288617474692207,
                  "gap_rejected_minus_accepted": 0.8207973852990165
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8963640928268433,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.539735399427868,
                  "rejected_mean_error": 2.1413702045168197,
                  "gap_rejected_minus_accepted": 0.6016348050889517
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6917527318000793,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4207087319237846,
                  "rejected_mean_error": 1.9595794694764272,
                  "gap_rejected_minus_accepted": 0.5388707375526427
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4518208503723145,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2516851581845965,
                  "rejected_mean_error": 1.836297081538609,
                  "gap_rejected_minus_accepted": 0.5846119233540126
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0302686691284184,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.626615325609843,
                  "rejected_mean_error": 2.5132334317479814,
                  "gap_rejected_minus_accepted": 0.8866181061381384
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.917902946472168,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.559399167696635,
                  "rejected_mean_error": 2.182911041804722,
                  "gap_rejected_minus_accepted": 0.6235118741080872
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7000341415405273,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4408725772585187,
                  "rejected_mean_error": 1.9896816951887948,
                  "gap_rejected_minus_accepted": 0.5488091179302761
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4708914458751678,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.2621354750224523,
                  "rejected_mean_error": 1.8663243566240584,
                  "gap_rejected_minus_accepted": 0.6041888816016061
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
        "best_epoch": 39,
        "best_calib_loss": 0.061474353075027466,
        "train_time_sec": 10.594154596328735,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9707139341506927,
              "spearman": 0.9374009572108112,
              "auroc_top30_bad": 0.9990519523809525,
              "mae": 0.10402690538822208,
              "mse": 0.03406835669569051,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.502,
              "expert_lt_simvla_seed0": 0.987,
              "same_context_pred_std": 0.6726928964581094,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2916057849628851
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3054660823038779
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4280263452756684
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7423959755552001
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0775018667796394
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9968774057603796,
              "spearman": 0.9973202094047442,
              "auroc_top30_worst": 0.9991068571428572,
              "pairwise_seed_ranking": 0.8425,
              "predicted_best_mean_error": 1.4293704737722874,
              "seed0_mean_error": 1.4983853181004525,
              "random_seed_mean_error": 1.4854410899877548,
              "oracle_best_mean_error": 1.423666303306818,
              "improvement_over_seed0": 0.06901484432816507,
              "gap_to_oracle": 0.005704170465469449,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5534178259968757
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7550735156774521
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0071964119315147
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2253350598573685
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4851105762660504
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3187823534011844,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3641921346121364,
                  "rejected_mean_error": 2.573376551151276,
                  "gap_rejected_minus_accepted": 1.2091844165391394
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.914511799812317,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2253350598573685,
                  "rejected_mean_error": 2.264437125492096,
                  "gap_rejected_minus_accepted": 1.0391020656347274
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.496575117111206,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0071964119315147,
                  "rejected_mean_error": 1.9630247406005858,
                  "gap_rejected_minus_accepted": 0.9558283286690712
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0738753080368042,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7550735156774521,
                  "rejected_mean_error": 1.7284562631289164,
                  "gap_rejected_minus_accepted": 0.9733827474514644
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3671399116516114,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.374457681245274,
                  "rejected_mean_error": 2.613734049797058,
                  "gap_rejected_minus_accepted": 1.239276368551784
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9439424276351929,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2333566704591115,
                  "rejected_mean_error": 2.293471261024475,
                  "gap_rejected_minus_accepted": 1.0601145905653637
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.517957091331482,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0120842467546463,
                  "rejected_mean_error": 1.9846863894462585,
                  "gap_rejected_minus_accepted": 0.9726021426916123
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0756298303604126,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7574401979446411,
                  "rejected_mean_error": 1.7453670248190563,
                  "gap_rejected_minus_accepted": 0.9879268268744151
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.884535332368004,
              "spearman": 0.8643750668849016,
              "auroc_top30_bad": 0.933376,
              "mae": 0.34719660987257955,
              "mse": 0.2167138145067096,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.7087855463540391,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.35121381041407584
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3890965659379959
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6271542038679123
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0119707125266393
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3638644678533076
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7738984817437107,
              "spearman": 0.7566841425178512,
              "auroc_top30_worst": 0.8700251428571429,
              "pairwise_seed_ranking": 0.7744,
              "predicted_best_mean_error": 1.9266800439357759,
              "seed0_mean_error": 2.002922800064087,
              "random_seed_mean_error": 1.9839035757780075,
              "oracle_best_mean_error": 1.9094995954036713,
              "improvement_over_seed0": 0.076242756128311,
              "gap_to_oracle": 0.017180448532104542,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9768799324035644
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3313292383383482
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5537932670593262
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.771247064126834
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9860241752624512
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.453348207473755,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8872211990356444,
                  "rejected_mean_error": 2.8752509613037107,
                  "gap_rejected_minus_accepted": 0.9880297622680663
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.12552011013031,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7699383071036323,
                  "rejected_mean_error": 2.632901039367286,
                  "gap_rejected_minus_accepted": 0.8629627322636535
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7950283288955688,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5537932670593262,
                  "rejected_mean_error": 2.418255083465576,
                  "gap_rejected_minus_accepted": 0.8644618164062499
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.141307294368744,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.33417405297581,
                  "rejected_mean_error": 2.203771334574851,
                  "gap_rejected_minus_accepted": 0.8695972815990411
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4881749868392946,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.9027394231160482,
                  "rejected_mean_error": 2.9045731925964358,
                  "gap_rejected_minus_accepted": 1.0018337694803876
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1196155548095703,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7726704653571634,
                  "rejected_mean_error": 2.6863702062576538,
                  "gap_rejected_minus_accepted": 0.9136997409004903
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8208823204040527,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.56477366065979,
                  "rejected_mean_error": 2.441071939468384,
                  "gap_rejected_minus_accepted": 0.876298278808594
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.12870654463768,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3544202352327013,
                  "rejected_mean_error": 2.2214022737773345,
                  "gap_rejected_minus_accepted": 0.8669820385446332
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8113303442121012,
              "spearman": 0.850738063085488,
              "auroc_top30_bad": 0.9757287619047619,
              "mae": 0.4009658259868622,
              "mse": 0.3937747479495571,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.6447444136144719,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3547339984178543
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3911615450143814
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5268457611322402
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8823863680442174
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2635805361151695
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7230059217495156,
              "spearman": 0.8165426414992906,
              "auroc_top30_worst": 0.8956434285714285,
              "pairwise_seed_ranking": 0.7776,
              "predicted_best_mean_error": 1.7327957507371903,
              "seed0_mean_error": 1.7897299077510833,
              "random_seed_mean_error": 1.7819887889623642,
              "oracle_best_mean_error": 1.7131504658460617,
              "improvement_over_seed0": 0.05693415701389304,
              "gap_to_oracle": 0.0196452848911286,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6029980216026306
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8077901097444388
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1819615343093872
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.453066212663264
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850427648544311
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3379502773284915,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6412497762044271,
                  "rejected_mean_error": 3.0791796627044676,
                  "gap_rejected_minus_accepted": 1.4379298865000405
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0006919503211975,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4527472471351175,
                  "rejected_mean_error": 2.779806023969437,
                  "gap_rejected_minus_accepted": 1.3270587768343194
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5100395679473877,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1819615343093872,
                  "rejected_mean_error": 2.388123995399475,
                  "gap_rejected_minus_accepted": 1.2061624610900878
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9802188575267792,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8101774419839389,
                  "rejected_mean_error": 2.1106914799648515,
                  "gap_rejected_minus_accepted": 1.3005140379809126
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.365313458442688,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.641743446720971,
                  "rejected_mean_error": 3.1216080570220948,
                  "gap_rejected_minus_accepted": 1.4798646103011237
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0029929280281067,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4393054957695823,
                  "rejected_mean_error": 2.8298785591882374,
                  "gap_rejected_minus_accepted": 1.390573063418655
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.493335485458374,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1827333006858827,
                  "rejected_mean_error": 2.396726514816284,
                  "gap_rejected_minus_accepted": 1.2139932141304013
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9804946780204773,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8031456356956845,
                  "rejected_mean_error": 2.1221085662510304,
                  "gap_rejected_minus_accepted": 1.3189629305553459
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.8565249896434705,
              "spearman": 0.8401222715130283,
              "auroc_top30_bad": 0.9093294460641399,
              "mae": 0.31358732213931423,
              "mse": 0.16857892109540124,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6329298512859972,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3371307974415166
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3684618608866419
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6161900583335331
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9479209898908934
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.194224164666874
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.666792841512524,
              "spearman": 0.5531660735167682,
              "auroc_top30_worst": 0.7627502429543246,
              "pairwise_seed_ranking": 0.7564285714285715,
              "predicted_best_mean_error": 1.6457035320145743,
              "seed0_mean_error": 1.7149599373340607,
              "random_seed_mean_error": 1.686807851280485,
              "oracle_best_mean_error": 1.6336392905030932,
              "improvement_over_seed0": 0.0692564053194864,
              "gap_to_oracle": 0.01206424151148111,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3520060879843576
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4581912881987436
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4871403159414018
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.589698702267238
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.689799051965986
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3098806381225594,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6102359149191114,
                  "rejected_mean_error": 2.4058672853878567,
                  "gap_rejected_minus_accepted": 0.7956313704687452
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7667824625968933,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.589698702267238,
                  "rejected_mean_error": 1.9901001010622297,
                  "gap_rejected_minus_accepted": 0.4004013987949917
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.441606879234314,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4871403159414018,
                  "rejected_mean_error": 1.89245778799057,
                  "gap_rejected_minus_accepted": 0.4053174720491681
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.035267412662506,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.4581912881987436,
                  "rejected_mean_error": 1.7670016398884,
                  "gap_rejected_minus_accepted": 0.30881035168965654
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.37421395778656,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6282866776935638,
                  "rejected_mean_error": 2.4950192740985324,
                  "gap_rejected_minus_accepted": 0.8667325964049686
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8115101754665375,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.6028015783854894,
                  "rejected_mean_error": 2.051435014179775,
                  "gap_rejected_minus_accepted": 0.4486334357942854
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4532690048217773,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.5032859648977006,
                  "rejected_mean_error": 1.9266339097704206,
                  "gap_rejected_minus_accepted": 0.42334794487272
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0376635193824768,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.48716835635049,
                  "rejected_mean_error": 1.7908904643285841,
                  "gap_rejected_minus_accepted": 0.30372210797809407
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
        "best_epoch": 42,
        "best_calib_loss": 0.02084255777299404,
        "train_time_sec": 34.87693119049072,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9994896363492448,
              "spearman": 0.9985980744420356,
              "auroc_top30_bad": 0.9998380952380952,
              "mae": 0.02247462910397444,
              "mse": 0.0008548743019387514,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6681894910561631,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05666605843021534
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.174693048147019
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4210228355723899
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7418532326193836
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0775018667796394
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9995726061928747,
              "spearman": 0.9996027885600736,
              "auroc_top30_worst": 0.999764,
              "pairwise_seed_ranking": 0.9421,
              "predicted_best_mean_error": 1.4246910658180714,
              "seed0_mean_error": 1.4983853181004525,
              "random_seed_mean_error": 1.4854410899877548,
              "oracle_best_mean_error": 1.423666303306818,
              "improvement_over_seed0": 0.07369425228238113,
              "gap_to_oracle": 0.0010247625112533854,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5468883737921715
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7534823293447495
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.006683046424389
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2248356858809788
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4851105762660504
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.290578770637513,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3637772371702723,
                  "rejected_mean_error": 2.5771106281280516,
                  "gap_rejected_minus_accepted": 1.2133333909577793
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8957829177379608,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2248356858809788,
                  "rejected_mean_error": 2.2659352474212646,
                  "gap_rejected_minus_accepted": 1.0410995615402858
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4952252507209778,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.006683046424389,
                  "rejected_mean_error": 1.9635381061077117,
                  "gap_rejected_minus_accepted": 0.9568550596833227
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0772214531898499,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7534823293447495,
                  "rejected_mean_error": 1.7289866585731506,
                  "gap_rejected_minus_accepted": 0.9755043292284011
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.311785912513733,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3740809157821867,
                  "rejected_mean_error": 2.6171249389648437,
                  "gap_rejected_minus_accepted": 1.243044023182657
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9193340837955475,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.232723569949468,
                  "rejected_mean_error": 2.2953705625534058,
                  "gap_rejected_minus_accepted": 1.0626469926039377
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4992439150810242,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0120164822340012,
                  "rejected_mean_error": 1.9847541539669036,
                  "gap_rejected_minus_accepted": 0.9727376717329024
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0775609612464905,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7552705566883087,
                  "rejected_mean_error": 1.746090238571167,
                  "gap_rejected_minus_accepted": 0.9908196818828583
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9738746694369513,
              "spearman": 0.9679116244792701,
              "auroc_top30_bad": 0.9774285714285714,
              "mae": 0.16014671960920096,
              "mse": 0.052435339239517945,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7604246348080426,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1451988673210144
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2476660004377365
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5625909448504448
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9815662497758866
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3638644678533076
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9421119763878609,
              "spearman": 0.9346951917409229,
              "auroc_top30_worst": 0.960359619047619,
              "pairwise_seed_ranking": 0.9252,
              "predicted_best_mean_error": 1.9106984065771102,
              "seed0_mean_error": 2.002922800064087,
              "random_seed_mean_error": 1.9839035757780075,
              "oracle_best_mean_error": 1.9094995954036713,
              "improvement_over_seed0": 0.09222439348697664,
              "gap_to_oracle": 0.0011988111734388962,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.842653657913208
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1214137100256407
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4652987173080445
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7255232138420218
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9860241752624512
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.613868737220765,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8606541885799832,
                  "rejected_mean_error": 3.114354055404663,
                  "gap_rejected_minus_accepted": 1.25369986682468
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3256202936172485,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.724885106722853,
                  "rejected_mean_error": 2.767772760634986,
                  "gap_rejected_minus_accepted": 1.042887653912133
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.91473388671875,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4652987173080445,
                  "rejected_mean_error": 2.5067496332168577,
                  "gap_rejected_minus_accepted": 1.0414509159088132
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3592014014720917,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1229600434105236,
                  "rejected_mean_error": 2.274326281206585,
                  "gap_rejected_minus_accepted": 1.1513662377960614
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.647950792312622,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8721133221520319,
                  "rejected_mean_error": 3.180208101272583,
                  "gap_rejected_minus_accepted": 1.3080947791205513
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.342579960823059,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7397222506171242,
                  "rejected_mean_error": 2.784168875406659,
                  "gap_rejected_minus_accepted": 1.0444466247895348
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9211243391036987,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4720003032684326,
                  "rejected_mean_error": 2.533845296859741,
                  "gap_rejected_minus_accepted": 1.0618449935913086
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.363657385110855,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1352436845264737,
                  "rejected_mean_error": 2.2952425020901277,
                  "gap_rejected_minus_accepted": 1.159998817563654
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9513864625581572,
              "spearman": 0.9724679298950832,
              "auroc_top30_bad": 0.9979146666666667,
              "mae": 0.20273808805346488,
              "mse": 0.13619865101771642,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6695533157694158,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1269132500886917
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2296776139497757
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4914692664384842
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7916759914239248
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2635805361151695
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9439130388690238,
              "spearman": 0.9883838881176885,
              "auroc_top30_worst": 0.995904,
              "pairwise_seed_ranking": 0.9172,
              "predicted_best_mean_error": 1.7158163447380066,
              "seed0_mean_error": 1.7897299077510833,
              "random_seed_mean_error": 1.7819887889623642,
              "oracle_best_mean_error": 1.7131504658460617,
              "improvement_over_seed0": 0.07391356301307672,
              "gap_to_oracle": 0.0026658788919449172,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5028368415832519
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.750304160400843
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0073385637283325
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2602620438726218
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850427648544311
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5447159051895145,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5669919361538358,
                  "rejected_mean_error": 3.7475002231597903,
                  "gap_rejected_minus_accepted": 2.1805082870059547
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.181920349597931,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2591641492497578,
                  "rejected_mean_error": 3.3593183649233738,
                  "gap_rejected_minus_accepted": 2.1001542156736157
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5015733242034912,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0073385637283325,
                  "rejected_mean_error": 2.56274696598053,
                  "gap_rejected_minus_accepted": 1.5554084022521975
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.098604828119278,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7512027594609002,
                  "rejected_mean_error": 2.1303916674031775,
                  "gap_rejected_minus_accepted": 1.3791889079422774
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5264952421188354,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5717110599411859,
                  "rejected_mean_error": 3.751899538040161,
                  "gap_rejected_minus_accepted": 2.1801884780989753
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2235220074653625,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2551605443265987,
                  "rejected_mean_error": 3.376467542042808,
                  "gap_rejected_minus_accepted": 2.121306997716209
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.499998152256012,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0017865252494813,
                  "rejected_mean_error": 2.5776732902526858,
                  "gap_rejected_minus_accepted": 1.5758867650032045
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0777900516986847,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7504889208172995,
                  "rejected_mean_error": 2.1398485290175455,
                  "gap_rejected_minus_accepted": 1.389359608200246
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9827163795133012,
              "spearman": 0.9673099346478417,
              "auroc_top30_bad": 0.9690719144800777,
              "mae": 0.11085601298670683,
              "mse": 0.020991501098745487,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9714285714285714,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7173422893267125,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08505152272326606
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21036786011287145
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5567364497057029
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9212831644926752
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.194224164666874
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9425362299874965,
              "spearman": 0.9025442675830533,
              "auroc_top30_worst": 0.9140330417881438,
              "pairwise_seed_ranking": 0.9014285714285715,
              "predicted_best_mean_error": 1.6363374888896942,
              "seed0_mean_error": 1.7149599373340607,
              "random_seed_mean_error": 1.686807851280485,
              "oracle_best_mean_error": 1.6336392905030932,
              "improvement_over_seed0": 0.0786224484443665,
              "gap_to_oracle": 0.002698198386601014,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0229968241282872
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2507760763168334
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.435252251284463
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5498827879769461
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.689799051965986
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1042052268981934,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6102365573247275,
                  "rejected_mean_error": 2.4058615037373134,
                  "gap_rejected_minus_accepted": 0.795624946412586
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9046590626239777,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5498827879769461,
                  "rejected_mean_error": 2.1095478439331057,
                  "gap_rejected_minus_accepted": 0.5596650559561596
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7483012676239014,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.435252251284463,
                  "rejected_mean_error": 1.9443458526475088,
                  "gap_rejected_minus_accepted": 0.5090936013630458
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4942534565925598,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2507760763168334,
                  "rejected_mean_error": 1.8361400438490367,
                  "gap_rejected_minus_accepted": 0.5853639675322033
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1617574453353883,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6286735288680545,
                  "rejected_mean_error": 2.4915376135281155,
                  "gap_rejected_minus_accepted": 0.862864084660061
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.921383410692215,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5700227896372476,
                  "rejected_mean_error": 2.1497713804244993,
                  "gap_rejected_minus_accepted": 0.5797485907872517
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7551344633102417,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4582434909684316,
                  "rejected_mean_error": 1.9716763836996896,
                  "gap_rejected_minus_accepted": 0.5134328927312579
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5190835893154144,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.261263152531215,
                  "rejected_mean_error": 1.8661921989350092,
                  "gap_rejected_minus_accepted": 0.6049290464037942
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
        "best_epoch": 80,
        "best_calib_loss": 0.02110111340880394,
        "train_time_sec": 41.29243755340576,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9989890410717119,
              "spearman": 0.9979324564953466,
              "auroc_top30_bad": 0.9995955238095239,
              "mae": 0.029338945889589376,
              "mse": 0.0014419638211784853,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6745897127335311,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.056759597169002515
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1751902003920637
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4213528277355712
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7420114932986287
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0775018667796394
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.998582497008683,
              "spearman": 0.9985541943661331,
              "auroc_top30_worst": 0.9991325714285714,
              "pairwise_seed_ranking": 0.9625,
              "predicted_best_mean_error": 1.424459674745798,
              "seed0_mean_error": 1.4983853181004525,
              "random_seed_mean_error": 1.4854410899877548,
              "oracle_best_mean_error": 1.423666303306818,
              "improvement_over_seed0": 0.07392564335465446,
              "gap_to_oracle": 0.0007933714389800617,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5477107309699059
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7541266091585159
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0069752899050712
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2250484146674474
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4851105762660504
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.302414774894715,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3639284885923069,
                  "rejected_mean_error": 2.5757493653297425,
                  "gap_rejected_minus_accepted": 1.2118208767374357
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8973531424999237,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2250484146674474,
                  "rejected_mean_error": 2.265297061061859,
                  "gap_rejected_minus_accepted": 1.0402486463944116
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4904853105545044,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0069752899050712,
                  "rejected_mean_error": 1.9632458626270295,
                  "gap_rejected_minus_accepted": 0.9562705727219583
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0795426070690155,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7541266091585159,
                  "rejected_mean_error": 1.7287718986352285,
                  "gap_rejected_minus_accepted": 0.9746452894767126
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3380099296569825,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3740506615241368,
                  "rejected_mean_error": 2.6173972272872925,
                  "gap_rejected_minus_accepted": 1.2433465657631557
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9379780292510986,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2326909172534943,
                  "rejected_mean_error": 2.295468520641327,
                  "gap_rejected_minus_accepted": 1.0627776033878327
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.509553074836731,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0122442909479141,
                  "rejected_mean_error": 1.9845263452529907,
                  "gap_rejected_minus_accepted": 0.9722820543050765
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0849833488464355,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7562471160888672,
                  "rejected_mean_error": 1.7457647187709808,
                  "gap_rejected_minus_accepted": 0.9895176026821136
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9753934877234227,
              "spearman": 0.9661046294361535,
              "auroc_top30_bad": 0.9775992380952381,
              "mae": 0.16819301228951664,
              "mse": 0.05057922391673867,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7627425830923173,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15163443702459337
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.26655685667991635
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5632504801630974
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9809073415676752
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3638644678533076
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9536365323129509,
              "spearman": 0.9446659270821935,
              "auroc_top30_worst": 0.9721020952380953,
              "pairwise_seed_ranking": 0.9152,
              "predicted_best_mean_error": 1.9108204309940338,
              "seed0_mean_error": 2.002922800064087,
              "random_seed_mean_error": 1.9839035757780075,
              "oracle_best_mean_error": 1.9094995954036713,
              "improvement_over_seed0": 0.09210236907005309,
              "gap_to_oracle": 0.0013208355903624458,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8497107028961182
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1230920595236313
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4669495779037476
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7091508328533376
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9860241752624512
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.567551827430725,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8602606377071804,
                  "rejected_mean_error": 3.117896013259888,
                  "gap_rejected_minus_accepted": 1.2576353755527074
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.322234034538269,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7083369484578788,
                  "rejected_mean_error": 2.817311496399462,
                  "gap_rejected_minus_accepted": 1.1089745479415833
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9322274327278137,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4669495779037476,
                  "rejected_mean_error": 2.505098772621155,
                  "gap_rejected_minus_accepted": 1.0381491947174073
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.32286536693573,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1245387952548627,
                  "rejected_mean_error": 2.273798907324751,
                  "gap_rejected_minus_accepted": 1.1492601120698884
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.617096400260925,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8721112770504422,
                  "rejected_mean_error": 3.1802265071868896,
                  "gap_rejected_minus_accepted": 1.3081152301364474
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3471134305000305,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7246516337369215,
                  "rejected_mean_error": 2.828902293765356,
                  "gap_rejected_minus_accepted": 1.1042506600284343
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9666189551353455,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4780979385375976,
                  "rejected_mean_error": 2.5277476615905763,
                  "gap_rejected_minus_accepted": 1.0496497230529787
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3413787186145782,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1320370435714722,
                  "rejected_mean_error": 2.296322814283524,
                  "gap_rejected_minus_accepted": 1.164285770712052
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9606419404994959,
              "spearman": 0.9713366853785524,
              "auroc_top30_bad": 0.9987550476190477,
              "mae": 0.18290705819460562,
              "mse": 0.1089491429938671,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.6743114205695317,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13956134206056595
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2330962106227875
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4893929145336151
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7890661884148915
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2635805361151695
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9572414023330764,
              "spearman": 0.9911898547135072,
              "auroc_top30_worst": 0.9998140952380953,
              "pairwise_seed_ranking": 0.9148,
              "predicted_best_mean_error": 1.7161718327999116,
              "seed0_mean_error": 1.7897299077510833,
              "random_seed_mean_error": 1.7819887889623642,
              "oracle_best_mean_error": 1.7131504658460617,
              "improvement_over_seed0": 0.07355807495117173,
              "gap_to_oracle": 0.0030213669538499133,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.50289595079422
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7506856673803085
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.007309895133972
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2638830686174731
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850427648544311
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6291248321533205,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.560739092508952,
                  "rejected_mean_error": 3.803775815963745,
                  "gap_rejected_minus_accepted": 2.243036723454793
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2643814086914062,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2628449146877359,
                  "rejected_mean_error": 3.3482995878774138,
                  "gap_rejected_minus_accepted": 2.0854546731896777
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.424817681312561,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.007309895133972,
                  "rejected_mean_error": 2.56277563457489,
                  "gap_rejected_minus_accepted": 1.5554657394409181
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0335292518138885,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7519069970987095,
                  "rejected_mean_error": 2.1301564204654673,
                  "gap_rejected_minus_accepted": 1.378249423366758
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6166075229644776,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5597590486208597,
                  "rejected_mean_error": 3.859467639923096,
                  "gap_rejected_minus_accepted": 2.2997085913022364
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.329025387763977,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2665100604455102,
                  "rejected_mean_error": 3.3427792957850864,
                  "gap_rejected_minus_accepted": 2.076269235339576
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4003832340240479,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0028210043907166,
                  "rejected_mean_error": 2.57663881111145,
                  "gap_rejected_minus_accepted": 1.5738178067207333
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.034778118133545,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7496174431982494,
                  "rejected_mean_error": 2.1401421284293107,
                  "gap_rejected_minus_accepted": 1.3905246852310613
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9833675392874792,
              "spearman": 0.9770486400784132,
              "auroc_top30_bad": 0.9921501457725947,
              "mae": 0.10377559057004483,
              "mse": 0.019612797701305352,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9928571428571429,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6769708170481116,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.14492615163326264
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.215243233527456
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5571352129536016
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9145139374193691
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.194224164666874
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9766180571560541,
              "spearman": 0.9697165212873611,
              "auroc_top30_worst": 0.9830029154518951,
              "pairwise_seed_ranking": 0.9135714285714286,
              "predicted_best_mean_error": 1.635468966620309,
              "seed0_mean_error": 1.7149599373340607,
              "random_seed_mean_error": 1.686807851280485,
              "oracle_best_mean_error": 1.6336392905030932,
              "improvement_over_seed0": 0.07949097071375166,
              "gap_to_oracle": 0.0018296761172158504,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0298858489309037
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2502894456045968
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4181411225455147
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5335813397452944
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.689799051965986
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9633156776428222,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.607508599379706,
                  "rejected_mean_error": 2.430413125242506,
                  "gap_rejected_minus_accepted": 0.8229045258627998
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8055185377597809,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5335813397452944,
                  "rejected_mean_error": 2.1584521886280603,
                  "gap_rejected_minus_accepted": 0.6248708488827659
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6333449482917786,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4181411225455147,
                  "rejected_mean_error": 1.961456981386457,
                  "gap_rejected_minus_accepted": 0.5433158588409424
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3920259773731232,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2502894456045968,
                  "rejected_mean_error": 1.836302254086449,
                  "gap_rejected_minus_accepted": 0.5860128084818523
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9580358386039736,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6258581640228393,
                  "rejected_mean_error": 2.5168758971350536,
                  "gap_rejected_minus_accepted": 0.8910177331122142
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8213794529438019,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5557092326028006,
                  "rejected_mean_error": 2.192712051527841,
                  "gap_rejected_minus_accepted": 0.6370028189250403
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6587995886802673,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4378915599414281,
                  "rejected_mean_error": 1.9920283147266933,
                  "gap_rejected_minus_accepted": 0.5541367547852651
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.415739744901657,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.260672426223755,
                  "rejected_mean_error": 1.8663891077041626,
                  "gap_rejected_minus_accepted": 0.6057166814804076
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
        "best_epoch": 49,
        "best_calib_loss": 0.021088803187012672,
        "train_time_sec": 29.038257598876953,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9993979043163649,
              "spearman": 0.9983755581551308,
              "auroc_top30_bad": 0.9998269523809524,
              "mae": 0.0348750793638872,
              "mse": 0.0019368278841125897,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6884130311910714,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05796433198894374
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1743468035853468
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4209600546556991
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7419381012412098
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0775018667796394
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9993890437079387,
              "spearman": 0.9994753260670005,
              "auroc_top30_worst": 0.9997714285714285,
              "pairwise_seed_ranking": 0.9532,
              "predicted_best_mean_error": 1.4243156912624837,
              "seed0_mean_error": 1.4983853181004525,
              "random_seed_mean_error": 1.4854410899877548,
              "oracle_best_mean_error": 1.423666303306818,
              "improvement_over_seed0": 0.0740696268379688,
              "gap_to_oracle": 0.0006493879556657145,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5468892691731453
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.753415471148491
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0066515518546104
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2249071505467097
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4851105762660504
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3435975313186646,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3638451953662767,
                  "rejected_mean_error": 2.5764990043640137,
                  "gap_rejected_minus_accepted": 1.212653808997737
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9406263530254364,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2249071505467097,
                  "rejected_mean_error": 2.2657208534240723,
                  "gap_rejected_minus_accepted": 1.0408137028773625
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.510121762752533,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0066515518546104,
                  "rejected_mean_error": 1.9635696006774903,
                  "gap_rejected_minus_accepted": 0.9569180488228799
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0843209028244019,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.753415471148491,
                  "rejected_mean_error": 1.7290089446385701,
                  "gap_rejected_minus_accepted": 0.9755934734900792
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.376767134666443,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3739460720618566,
                  "rejected_mean_error": 2.618338532447815,
                  "gap_rejected_minus_accepted": 1.2443924603859582
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.965535432100296,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2327088077068329,
                  "rejected_mean_error": 2.295414849281311,
                  "gap_rejected_minus_accepted": 1.0627060415744782
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5205082893371582,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.011859090924263,
                  "rejected_mean_error": 1.984911545276642,
                  "gap_rejected_minus_accepted": 0.9730524543523789
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0926835238933563,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7548700129985809,
                  "rejected_mean_error": 1.7462237531344096,
                  "gap_rejected_minus_accepted": 0.9913537401358287
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9734904319134818,
              "spearman": 0.9673688141102015,
              "auroc_top30_bad": 0.9756594285714286,
              "mae": 0.1661959120599553,
              "mse": 0.05369360024158392,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7836763101289039,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13441439795494078
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2588330155134201
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.563256133544445
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9819004939953486
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3638644678533076
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9406607998283503,
              "spearman": 0.9344834693654206,
              "auroc_top30_worst": 0.9630201904761905,
              "pairwise_seed_ranking": 0.9276,
              "predicted_best_mean_error": 1.9110900468826293,
              "seed0_mean_error": 2.002922800064087,
              "random_seed_mean_error": 1.9839035757780075,
              "oracle_best_mean_error": 1.9094995954036713,
              "improvement_over_seed0": 0.09183275318145756,
              "gap_to_oracle": 0.0015904514789579771,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8335136070251464
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1283912853552744
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4706643974304199
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7154504045494583
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9860241752624512
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.642404365539551,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8588629718356662,
                  "rejected_mean_error": 3.1304750061035156,
                  "gap_rejected_minus_accepted": 1.2716120342678494
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3895301818847656,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7148648506803725,
                  "rejected_mean_error": 2.797769501567268,
                  "gap_rejected_minus_accepted": 1.0829046508868954
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9354954361915588,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4706643974304199,
                  "rejected_mean_error": 2.5013839530944826,
                  "gap_rejected_minus_accepted": 1.0307195556640627
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2935906052589417,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1293824301740993,
                  "rejected_mean_error": 2.2721809161510893,
                  "gap_rejected_minus_accepted": 1.14279848597699
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.686810350418091,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8707433986663817,
                  "rejected_mean_error": 3.1925374126434325,
                  "gap_rejected_minus_accepted": 1.3217940139770508
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4187278747558594,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7275485597192284,
                  "rejected_mean_error": 2.820303481722635,
                  "gap_rejected_minus_accepted": 1.0927549220034067
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9646299481391907,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.481258358001709,
                  "rejected_mean_error": 2.524587242126465,
                  "gap_rejected_minus_accepted": 1.043328884124756
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3384356498718262,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1397838024866014,
                  "rejected_mean_error": 2.2937129436329724,
                  "gap_rejected_minus_accepted": 1.153929141146371
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9619954297597376,
              "spearman": 0.9749478372555751,
              "auroc_top30_bad": 0.9985622857142857,
              "mae": 0.18814189349049704,
              "mse": 0.11442752056793763,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.676359694564774,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11975286984443664
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2251271670103073
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4915834617614746
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7889763241291046
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2635805361151695
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9562130382558955,
              "spearman": 0.9863215241737756,
              "auroc_top30_worst": 0.999463619047619,
              "pairwise_seed_ranking": 0.9352,
              "predicted_best_mean_error": 1.7150735206604004,
              "seed0_mean_error": 1.7897299077510833,
              "random_seed_mean_error": 1.7819887889623642,
              "oracle_best_mean_error": 1.7131504658460617,
              "improvement_over_seed0": 0.0746563870906829,
              "gap_to_oracle": 0.0019230548143387427,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5171521911621094
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7535539028736261
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0100857730865478
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2691957556616777
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7850427648544311
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6144529581069946,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5587575075361464,
                  "rejected_mean_error": 3.8216100807189943,
                  "gap_rejected_minus_accepted": 2.262852573182848
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.191788673400879,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2669918895912782,
                  "rejected_mean_error": 3.335885161408982,
                  "gap_rejected_minus_accepted": 2.0688932718177035
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4432921409606934,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0100857730865478,
                  "rejected_mean_error": 2.5599997566223145,
                  "gap_rejected_minus_accepted": 1.5499139835357667
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0047496557235718,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7543106071484356,
                  "rejected_mean_error": 2.1293535069696676,
                  "gap_rejected_minus_accepted": 1.375042899821232
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6024692058563232,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5584190758069356,
                  "rejected_mean_error": 3.871527395248413,
                  "gap_rejected_minus_accepted": 2.3131083194414774
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2545740604400635,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2714235715687594,
                  "rejected_mean_error": 3.328194746895442,
                  "gap_rejected_minus_accepted": 2.0567711753266824
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4431374669075012,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0050572113990783,
                  "rejected_mean_error": 2.5744026041030885,
                  "gap_rejected_minus_accepted": 1.5693453927040102
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0214103162288666,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7542923017153664,
                  "rejected_mean_error": 2.138567176094667,
                  "gap_rejected_minus_accepted": 1.3842748743793005
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9839706538565729,
              "spearman": 0.9756878046261289,
              "auroc_top30_bad": 0.989608843537415,
              "mae": 0.10227516771427222,
              "mse": 0.018727965008197706,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9857142857142858,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7119889905930497,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1333020068705082
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2107407295703888
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5582601494661399
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9161719855949992
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.194224164666874
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9616536621568803,
              "spearman": 0.949346777092548,
              "auroc_top30_worst": 0.9571720116618075,
              "pairwise_seed_ranking": 0.9007142857142857,
              "predicted_best_mean_error": 1.635525234256472,
              "seed0_mean_error": 1.7149599373340607,
              "random_seed_mean_error": 1.686807851280485,
              "oracle_best_mean_error": 1.6336392905030932,
              "improvement_over_seed0": 0.07943470307758882,
              "gap_to_oracle": 0.0018859437533786938,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.033467732157026
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.256847606386457
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4203555624825615
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5436616627375286
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.689799051965986
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0939019680023194,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.608645352295467,
                  "rejected_mean_error": 2.420182349000658,
                  "gap_rejected_minus_accepted": 0.8115369967051913
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.956668645143509,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5436616627375286,
                  "rejected_mean_error": 2.1282112196513583,
                  "gap_rejected_minus_accepted": 0.5845495569138297
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7406685948371887,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4203555624825615,
                  "rejected_mean_error": 1.9592425414494106,
                  "gap_rejected_minus_accepted": 0.5388869789668491
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4863812327384949,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.256847606386457,
                  "rejected_mean_error": 1.8341162004924956,
                  "gap_rejected_minus_accepted": 0.5772685941060385
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.087606167793274,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6262628823991805,
                  "rejected_mean_error": 2.5132334317479814,
                  "gap_rejected_minus_accepted": 0.8869705493488009
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9970220029354095,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5637585708073207,
                  "rejected_mean_error": 2.1685640369142805,
                  "gap_rejected_minus_accepted": 0.6048054661069597
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7572165727615356,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4405684334891182,
                  "rejected_mean_error": 1.989351441179003,
                  "gap_rejected_minus_accepted": 0.5487830076898847
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5038706362247467,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.2651214599609375,
                  "rejected_mean_error": 1.864906096458435,
                  "gap_rejected_minus_accepted": 0.5997846364974975
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
        "best_epoch": 76,
        "best_calib_loss": 0.06343822181224823,
        "train_time_sec": 10.70787262916565,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9793352143830925,
              "spearman": 0.9591613492031146,
              "auroc_top30_bad": 0.9993877142857143,
              "mae": 0.08705274569310714,
              "mse": 0.02646933834397971,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.52,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7161893153691283,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08974621386802756
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18345082618845626
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3278130640076008
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6757870939603385
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0274437544964952
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9977736786671135,
              "spearman": 0.9980294109211291,
              "auroc_top30_worst": 0.9990697142857142,
              "pairwise_seed_ranking": 0.8747,
              "predicted_best_mean_error": 1.4270040138363838,
              "seed0_mean_error": 1.4977671349048614,
              "random_seed_mean_error": 1.4848491892814637,
              "oracle_best_mean_error": 1.4230901091992856,
              "improvement_over_seed0": 0.0707631210684776,
              "gap_to_oracle": 0.003913904637098176,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5474433286786079
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7526011017084122
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.006013239967823
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.224615926527977
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4845065901339054
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2796963930130008,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3633489171730147,
                  "rejected_mean_error": 2.5749256467819213,
                  "gap_rejected_minus_accepted": 1.2115767296089066
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8899285793304443,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.224615926527977,
                  "rejected_mean_error": 2.2641785809516906,
                  "gap_rejected_minus_accepted": 1.0395626544237135
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4822306632995605,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.006013239967823,
                  "rejected_mean_error": 1.9629999402999878,
                  "gap_rejected_minus_accepted": 0.9569867003321648
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0652616620063782,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7526011017084122,
                  "rejected_mean_error": 1.7284750862757365,
                  "gap_rejected_minus_accepted": 0.9758739845673243
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3115521907806396,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3736993749936421,
                  "rejected_mean_error": 2.614376974105835,
                  "gap_rejected_minus_accepted": 1.240677599112193
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9165720343589783,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2322909404436748,
                  "rejected_mean_error": 2.294195718288422,
                  "gap_rejected_minus_accepted": 1.061904777844747
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5016391277313232,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0113113689422608,
                  "rejected_mean_error": 1.9842229008674621,
                  "gap_rejected_minus_accepted": 0.9729115319252013
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0635945200920105,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7542985651493073,
                  "rejected_mean_error": 1.7455899914900461,
                  "gap_rejected_minus_accepted": 0.9912914263407389
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.89511020621211,
              "spearman": 0.864889374355367,
              "auroc_top30_bad": 0.9304346666666667,
              "mae": 0.3543283702328801,
              "mse": 0.21653698709721367,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.516,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.761147820274331,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3404817539155483
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4089067896962166
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6012387853682041
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0021703089356422
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3556984712809323
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7902619232397957,
              "spearman": 0.7628086108608592,
              "auroc_top30_worst": 0.8817447619047619,
              "pairwise_seed_ranking": 0.7824,
              "predicted_best_mean_error": 1.9241979578733444,
              "seed0_mean_error": 2.0026443390846254,
              "random_seed_mean_error": 1.9835996059179306,
              "oracle_best_mean_error": 1.909254893541336,
              "improvement_over_seed0": 0.078446381211281,
              "gap_to_oracle": 0.014943064332008316,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9481694278717041
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3027334658381267
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5600781816482543
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7674144702171213
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9857149640083314
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.459637832641602,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.88375684844123,
                  "rejected_mean_error": 2.9033380041122436,
                  "gap_rejected_minus_accepted": 1.0195811556710137
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.130500614643097,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.766801334114441,
                  "rejected_mean_error": 2.6410570445532997,
                  "gap_rejected_minus_accepted": 0.8742557104388586
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.748276174068451,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.5600781816482543,
                  "rejected_mean_error": 2.411351746368408,
                  "gap_rejected_minus_accepted": 0.8512735647201539
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2771981358528137,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.3034305814356089,
                  "rejected_mean_error": 2.213628530438707,
                  "gap_rejected_minus_accepted": 0.9101979490030983
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.477763271331787,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.9038154157002767,
                  "rejected_mean_error": 2.892104649543762,
                  "gap_rejected_minus_accepted": 0.9882892338434854
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1543598771095276,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7761970356823926,
                  "rejected_mean_error": 2.6747974460087125,
                  "gap_rejected_minus_accepted": 0.8986004103263199
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7611718773841858,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5754854650497436,
                  "rejected_mean_error": 2.4298032131195066,
                  "gap_rejected_minus_accepted": 0.854317748069763
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2868886590003967,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.3320142541612898,
                  "rejected_mean_error": 2.2285785388181556,
                  "gap_rejected_minus_accepted": 0.8965642846568658
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.7843737064840977,
              "spearman": 0.8215777091288409,
              "auroc_top30_bad": 0.9659718095238095,
              "mae": 0.43793452199101446,
              "mse": 0.44373403900828395,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.516,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.6831636338586271,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4127937446832657
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.424173101568222
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5307058738589286
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8828808551708858
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2596822590589523
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6725751427966916,
              "spearman": 0.7700463250216482,
              "auroc_top30_worst": 0.8566735238095238,
              "pairwise_seed_ranking": 0.7784,
              "predicted_best_mean_error": 1.7282486375570296,
              "seed0_mean_error": 1.7879177272319793,
              "random_seed_mean_error": 1.7802261937856674,
              "oracle_best_mean_error": 1.711424299120903,
              "improvement_over_seed0": 0.05966908967494966,
              "gap_to_oracle": 0.01682433843612663,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6964472949504852
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8405236435624269
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.210353944015503
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.491077906287301
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7832511980056762
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.346281313896179,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.65155757077535,
                  "rejected_mean_error": 2.968493843078613,
                  "gap_rejected_minus_accepted": 1.3169362723032632
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9904531240463257,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4906041372801986,
                  "rejected_mean_error": 2.6593224309122983,
                  "gap_rejected_minus_accepted": 1.1687182936320997
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.460710048675537,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.210353944015503,
                  "rejected_mean_error": 2.3561484519958498,
                  "gap_rejected_minus_accepted": 1.1457945079803469
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9538820385932922,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8407459188574038,
                  "rejected_mean_error": 2.0980902080093147,
                  "gap_rejected_minus_accepted": 1.2573442891519109
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3596963644027706,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6497799928983052,
                  "rejected_mean_error": 3.0311573362350464,
                  "gap_rejected_minus_accepted": 1.3813773433367411
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9913482666015625,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4992802962262364,
                  "rejected_mean_error": 2.644666927201407,
                  "gap_rejected_minus_accepted": 1.1453866309751708
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.445723533630371,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2167153010368348,
                  "rejected_mean_error": 2.3591201534271242,
                  "gap_rejected_minus_accepted": 1.1424048523902894
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9543008655309677,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8348368803660074,
                  "rejected_mean_error": 2.109009135534419,
                  "gap_rejected_minus_accepted": 1.2741722551684118
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.8753781913901192,
              "spearman": 0.842695444050561,
              "auroc_top30_bad": 0.9223226433430516,
              "mae": 0.3021174811891147,
              "mse": 0.1537085541864386,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.4857142857142857,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6450158573368384,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4056189922349794
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4050395978774343
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.602433439301593
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9427106407568568
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1926598759953464
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.6956211433402031,
              "spearman": 0.579885405013946,
              "auroc_top30_worst": 0.7700388726919339,
              "pairwise_seed_ranking": 0.76,
              "predicted_best_mean_error": 1.6486736216715403,
              "seed0_mean_error": 1.7149599373340607,
              "random_seed_mean_error": 1.686807851280485,
              "oracle_best_mean_error": 1.6336392905030932,
              "improvement_over_seed0": 0.06628631566252041,
              "gap_to_oracle": 0.015034331168447101,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3322742538792747
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.418331790310996
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5045082998275756
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5863197290329707
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.689799051965986
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2369671583175665,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6123853906752572,
                  "rejected_mean_error": 2.3865220035825456,
                  "gap_rejected_minus_accepted": 0.7741366129072884
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6768964231014252,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5863197290329707,
                  "rejected_mean_error": 2.000237020765032,
                  "gap_rejected_minus_accepted": 0.4139172917320615
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4321579337120056,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.5045082998275756,
                  "rejected_mean_error": 1.8750898041043962,
                  "gap_rejected_minus_accepted": 0.3705815042768206
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.115865707397461,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.418331790310996,
                  "rejected_mean_error": 1.780288139184316,
                  "gap_rejected_minus_accepted": 0.36195634887331996
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3494920015335086,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6282866776935638,
                  "rejected_mean_error": 2.4950192740985324,
                  "gap_rejected_minus_accepted": 0.8667325964049686
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7193923890590668,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.6043411073230562,
                  "rejected_mean_error": 2.0468164273670744,
                  "gap_rejected_minus_accepted": 0.44247532004401813
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.428842306137085,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.5129527722086225,
                  "rejected_mean_error": 1.9169671024594988,
                  "gap_rejected_minus_accepted": 0.4040143302508763
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1177183985710144,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.4172869954790388,
                  "rejected_mean_error": 1.8141842512857347,
                  "gap_rejected_minus_accepted": 0.3968972558066959
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
        "best_epoch": 34,
        "best_calib_loss": 0.024189190939068794,
        "train_time_sec": 35.134830474853516,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9992863172632003,
              "spearman": 0.9961615164485068,
              "auroc_top30_bad": 0.9998693333333333,
              "mae": 0.033709516214183534,
              "mse": 0.0018467386160438601,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.979,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7290547515830204,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.012486190166207962
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.08099463494149968
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.32489648167355917
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6754639642269351
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0274437544964952
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9994584589951615,
              "spearman": 0.9996082966563132,
              "auroc_top30_worst": 0.9997853333333334,
              "pairwise_seed_ranking": 0.9312,
              "predicted_best_mean_error": 1.4244494289457799,
              "seed0_mean_error": 1.4977671349048614,
              "random_seed_mean_error": 1.4848491892814637,
              "oracle_best_mean_error": 1.4230901091992856,
              "improvement_over_seed0": 0.07331770595908149,
              "gap_to_oracle": 0.0013593197464942808,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5454137027859688
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7516807145357132
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0055031524777411
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2240902549505235
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4845065901339054
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.329991984367371,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3631671526233355,
                  "rejected_mean_error": 2.5765615277290346,
                  "gap_rejected_minus_accepted": 1.213394375105699
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9196897447109222,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2240902549505235,
                  "rejected_mean_error": 2.2657555956840514,
                  "gap_rejected_minus_accepted": 1.041665340733528
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.508991003036499,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0055031524777411,
                  "rejected_mean_error": 1.9635100277900697,
                  "gap_rejected_minus_accepted": 0.9580068753123285
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.086086481809616,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7516807145357132,
                  "rejected_mean_error": 1.7287818819999694,
                  "gap_rejected_minus_accepted": 0.9771011674642562
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.356722617149353,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3733405900001525,
                  "rejected_mean_error": 2.6176060390472413,
                  "gap_rejected_minus_accepted": 1.2442654490470888
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9428196847438812,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2318996537526448,
                  "rejected_mean_error": 2.295369578361511,
                  "gap_rejected_minus_accepted": 1.0634699246088664
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5214499235153198,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0105914838314056,
                  "rejected_mean_error": 1.9849427859783173,
                  "gap_rejected_minus_accepted": 0.9743513021469117
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0846689343452454,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.753237871646881,
                  "rejected_mean_error": 1.745943555990855,
                  "gap_rejected_minus_accepted": 0.9927056843439739
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9687226648522966,
              "spearman": 0.9549119837648958,
              "auroc_top30_bad": 0.9785828571428571,
              "mae": 0.1765372557837516,
              "mse": 0.06391832556459205,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.94,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8152997982488885,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.22193786543607713
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2736283836841583
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5459944706380367
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9695249628345172
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3556984712809323
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9399483077610313,
              "spearman": 0.9305982163188585,
              "auroc_top30_worst": 0.9525820952380953,
              "pairwise_seed_ranking": 0.914,
              "predicted_best_mean_error": 1.9107829822301865,
              "seed0_mean_error": 2.0026443390846254,
              "random_seed_mean_error": 1.9835996059179306,
              "oracle_best_mean_error": 1.909254893541336,
              "improvement_over_seed0": 0.09186135685443886,
              "gap_to_oracle": 0.0015280886888504597,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8456291933059692
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1285528112680485
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4625788404464721
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7312108340548045
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9857149640083314
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5911137342453006,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8601836847729154,
                  "rejected_mean_error": 3.115496477127075,
                  "gap_rejected_minus_accepted": 1.2553127923541596
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.355631172657013,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7306551010911466,
                  "rejected_mean_error": 2.749264777277986,
                  "gap_rejected_minus_accepted": 1.0186096761868395
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.961054801940918,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4625788404464721,
                  "rejected_mean_error": 2.5088510875701906,
                  "gap_rejected_minus_accepted": 1.0462722471237185
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.390732228755951,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1294891788555792,
                  "rejected_mean_error": 2.27173275563353,
                  "gap_rejected_minus_accepted": 1.1422435767779509
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.613526391983032,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8714203808042738,
                  "rejected_mean_error": 3.1836599636077882,
                  "gap_rejected_minus_accepted": 1.3122395828035145
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.39014333486557,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7452848907460503,
                  "rejected_mean_error": 2.7665525428832525,
                  "gap_rejected_minus_accepted": 1.0212676521372022
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9732325673103333,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4698124675750732,
                  "rejected_mean_error": 2.5354762105941773,
                  "gap_rejected_minus_accepted": 1.065663743019104
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4334268867969513,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1334277467122154,
                  "rejected_mean_error": 2.2954820145897687,
                  "gap_rejected_minus_accepted": 1.1620542678775534
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9330154270599225,
              "spearman": 0.9467331113414346,
              "auroc_top30_bad": 0.9976220952380952,
              "mae": 0.2360806901603937,
              "mse": 0.1656772130806987,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.86,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7315105634836326,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.30874746966362
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.28554391989707945
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.48111616988182065
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.788304516506195
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2596822590589523
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9279476560791868,
              "spearman": 0.9840634306965956,
              "auroc_top30_worst": 0.9934415238095238,
              "pairwise_seed_ranking": 0.8944,
              "predicted_best_mean_error": 1.715511971950531,
              "seed0_mean_error": 1.7879177272319793,
              "random_seed_mean_error": 1.7802261937856674,
              "oracle_best_mean_error": 1.711424299120903,
              "improvement_over_seed0": 0.07240575528144833,
              "gap_to_oracle": 0.004087672829627964,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5034125943183899
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7518771315614382
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0082801031112671
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2755540531835576
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7832511980056762
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.535886764526367,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5672469639248319,
                  "rejected_mean_error": 3.7272893047332762,
                  "gap_rejected_minus_accepted": 2.1600423408084444
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1330769658088684,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2731933569577358,
                  "rejected_mean_error": 3.310165565615645,
                  "gap_rejected_minus_accepted": 2.036972208657909
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5218201279640198,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0082801031112671,
                  "rejected_mean_error": 2.5582222929000853,
                  "gap_rejected_minus_accepted": 1.5499421897888181
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0975285470485687,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7531897764617261,
                  "rejected_mean_error": 2.127337884177775,
                  "gap_rejected_minus_accepted": 1.3741481077160487
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5092023372650147,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5712530631489223,
                  "rejected_mean_error": 3.737899703979492,
                  "gap_rejected_minus_accepted": 2.16664664083057
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.147663414478302,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2718201547382988,
                  "rejected_mean_error": 3.319826394792587,
                  "gap_rejected_minus_accepted": 2.0480062400542884
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5091145634651184,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.002340190410614,
                  "rejected_mean_error": 2.573495264053345,
                  "gap_rejected_minus_accepted": 1.5711550736427309
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0860262215137482,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7496476258550372,
                  "rejected_mean_error": 2.137709258711912,
                  "gap_rejected_minus_accepted": 1.388061632856875
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9700587586645772,
              "spearman": 0.9452272239921181,
              "auroc_top30_bad": 0.9626773566569485,
              "mae": 0.14901840773677189,
              "mse": 0.042614289778888356,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.8642857142857143,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7669569570413853,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.24553699110235486
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2588690777761596
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5550922637113503
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9222110005645525
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1926598759953464
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9311138583122989,
              "spearman": 0.8856973177496281,
              "auroc_top30_worst": 0.9022351797862003,
              "pairwise_seed_ranking": 0.8814285714285715,
              "predicted_best_mean_error": 1.6371373219149454,
              "seed0_mean_error": 1.7149599373340607,
              "random_seed_mean_error": 1.686807851280485,
              "oracle_best_mean_error": 1.6336392905030932,
              "improvement_over_seed0": 0.07782261541911528,
              "gap_to_oracle": 0.0034980314118522315,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0361676761082241
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2585206249782017
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4374955286298479
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5538568891797746
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.689799051965986
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.164900660514832,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6100692605215405,
                  "rejected_mean_error": 2.407367174965995,
                  "gap_rejected_minus_accepted": 0.7972979144444543
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9793213903903961,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5538568891797746,
                  "rejected_mean_error": 2.09762554032462,
                  "gap_rejected_minus_accepted": 0.5437686511448454
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7957478761672974,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4374955286298479,
                  "rejected_mean_error": 1.942102575302124,
                  "gap_rejected_minus_accepted": 0.5046070466722761
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.504520207643509,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2585206249782017,
                  "rejected_mean_error": 1.8335585276285806,
                  "gap_rejected_minus_accepted": 0.5750379026503789
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.20494978427887,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6262628823991805,
                  "rejected_mean_error": 2.5132334317479814,
                  "gap_rejected_minus_accepted": 0.8869705493488009
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0059803128242493,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.586993600073315,
                  "rejected_mean_error": 2.0988589491162983,
                  "gap_rejected_minus_accepted": 0.5118653490429834
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8066516518592834,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4582429834774562,
                  "rejected_mean_error": 1.971676891190665,
                  "gap_rejected_minus_accepted": 0.5134339077132088
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5315331816673279,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.2753607715879167,
                  "rejected_mean_error": 1.8614929925827752,
                  "gap_rejected_minus_accepted": 0.5861322209948585
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
        "best_epoch": 52,
        "best_calib_loss": 0.022095365449786186,
        "train_time_sec": 41.44769072532654,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9983259869062955,
              "spearman": 0.9951687045236743,
              "auroc_top30_bad": 0.999077619047619,
              "mae": 0.052554607647215014,
              "mse": 0.004779160620299359,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.957,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7468768013427713,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.013376701032742858
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.08169592554299161
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3250184440182056
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6760333333205121
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0274437544964952
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9975842215452745,
              "spearman": 0.9978001874399548,
              "auroc_top30_worst": 0.9988043809523809,
              "pairwise_seed_ranking": 0.9562,
              "predicted_best_mean_error": 1.4239003732800484,
              "seed0_mean_error": 1.4977671349048614,
              "random_seed_mean_error": 1.4848491892814637,
              "oracle_best_mean_error": 1.4230901091992856,
              "improvement_over_seed0": 0.07386676162481298,
              "gap_to_oracle": 0.0008102640807627903,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5464069694876671
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.752357139134407
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0063198650479317
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2245375851710638
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4845065901339054
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3818054676055906,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3634009086357222,
                  "rejected_mean_error": 2.5744577236175537,
                  "gap_rejected_minus_accepted": 1.2110568149818315
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9729706943035126,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2245375851710638,
                  "rejected_mean_error": 2.2644136050224306,
                  "gap_rejected_minus_accepted": 1.0398760198513668
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5382505655288696,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0063198650479317,
                  "rejected_mean_error": 1.962693315219879,
                  "gap_rejected_minus_accepted": 0.9563734501719474
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1015536487102509,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.752357139134407,
                  "rejected_mean_error": 1.7285564071337383,
                  "gap_rejected_minus_accepted": 0.9761992679993312
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.414991283416748,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3735927854643928,
                  "rejected_mean_error": 2.6153362798690796,
                  "gap_rejected_minus_accepted": 1.2417434944046868
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0013067424297333,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2326534860928853,
                  "rejected_mean_error": 2.29310808134079,
                  "gap_rejected_minus_accepted": 1.0604545952479045
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5579090118408203,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.011589482307434,
                  "rejected_mean_error": 1.9839447875022889,
                  "gap_rejected_minus_accepted": 0.9723553051948548
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.108458012342453,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7540288133621216,
                  "rejected_mean_error": 1.7456799087524415,
                  "gap_rejected_minus_accepted": 0.9916510953903199
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9742641175932005,
              "spearman": 0.9556108445830557,
              "auroc_top30_bad": 0.9797927619047618,
              "mae": 0.17338000862537883,
              "mse": 0.05532965249560531,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.924,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8461970781986885,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.24919966974854468
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.27710051929950713
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5462615845143795
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9693187128980955
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3556984712809323
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9611803280033128,
              "spearman": 0.9530936019799054,
              "auroc_top30_worst": 0.9783466666666666,
              "pairwise_seed_ranking": 0.922,
              "predicted_best_mean_error": 1.910868402838707,
              "seed0_mean_error": 2.0026443390846254,
              "random_seed_mean_error": 1.9835996059179306,
              "oracle_best_mean_error": 1.909254893541336,
              "improvement_over_seed0": 0.09177593624591829,
              "gap_to_oracle": 0.0016135092973710297,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8382553424835205
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1232734593825462
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4645379934310914
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7068352032063612
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9857149640083314
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.726455903053284,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8564705419540406,
                  "rejected_mean_error": 3.1489147624969482,
                  "gap_rejected_minus_accepted": 1.2924442205429076
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.387487769126892,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7060214789979868,
                  "rejected_mean_error": 2.8230082402214074,
                  "gap_rejected_minus_accepted": 1.1169867612234206
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.008138656616211,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4645379934310914,
                  "rejected_mean_error": 2.506891934585571,
                  "gap_rejected_minus_accepted": 1.0423539411544798
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.414745271205902,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.124534306815638,
                  "rejected_mean_error": 2.2733879049915897,
                  "gap_rejected_minus_accepted": 1.1488535981759518
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.726455903053284,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8712737385431926,
                  "rejected_mean_error": 3.1849797439575194,
                  "gap_rejected_minus_accepted": 1.3137060054143268
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.413929283618927,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7209176207608718,
                  "rejected_mean_error": 2.8388807887122747,
                  "gap_rejected_minus_accepted": 1.1179631679514028
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.0252866744995117,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4771359548568725,
                  "rejected_mean_error": 2.528152723312378,
                  "gap_rejected_minus_accepted": 1.0510167684555054
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4497275352478027,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1334191844576882,
                  "rejected_mean_error": 2.295484899199583,
                  "gap_rejected_minus_accepted": 1.1620657147418947
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9519445520628376,
              "spearman": 0.9494930013501852,
              "auroc_top30_bad": 0.9990148571428572,
              "mae": 0.20145022092801518,
              "mse": 0.11741148463711058,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.864,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.765427872034101,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.29686117070913315
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2854707593917847
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4824631217002869
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.785041097609202
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2596822590589523
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9553202552316638,
              "spearman": 0.9859591508218566,
              "auroc_top30_worst": 0.9993142857142857,
              "pairwise_seed_ranking": 0.932,
              "predicted_best_mean_error": 1.7136507607698441,
              "seed0_mean_error": 1.7879177272319793,
              "random_seed_mean_error": 1.7802261937856674,
              "oracle_best_mean_error": 1.711424299120903,
              "improvement_over_seed0": 0.07426696646213515,
              "gap_to_oracle": 0.002226461648941136,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5075757622718811
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7519795862145913
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.008342137336731
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2759225777725676
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7832511980056762
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.797131323814392,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5584432888031006,
                  "rejected_mean_error": 3.8065223808288575,
                  "gap_rejected_minus_accepted": 2.248079092025757
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.317885398864746,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2738620960089033,
                  "rejected_mean_error": 3.308163621555121,
                  "gap_rejected_minus_accepted": 2.034301525546218
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4769604206085205,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.008342137336731,
                  "rejected_mean_error": 2.5581602586746217,
                  "gap_rejected_minus_accepted": 1.5498181213378908
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0626433789730072,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7532113944760527,
                  "rejected_mean_error": 2.127330662791986,
                  "gap_rejected_minus_accepted": 1.3741192683159333
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7901724576950073,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5597195559077792,
                  "rejected_mean_error": 3.8417012691497803,
                  "gap_rejected_minus_accepted": 2.281981713242001
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.360878825187683,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2829696733683826,
                  "rejected_mean_error": 3.286731791874719,
                  "gap_rejected_minus_accepted": 2.0037621185063363
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4804831147193909,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0024062542915344,
                  "rejected_mean_error": 2.5734292001724244,
                  "gap_rejected_minus_accepted": 1.57102294588089
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.060672402381897,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.748773749858614,
                  "rejected_mean_error": 2.1380036661331667,
                  "gap_rejected_minus_accepted": 1.3892299162745527
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9731307097457289,
              "spearman": 0.9587391103983286,
              "auroc_top30_bad": 0.9884693877551021,
              "mae": 0.12741095757926815,
              "mse": 0.03602013378472135,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.8642857142857143,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7566139418826694,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.24508585184812545
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2796488993508475
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.554090433950935
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9132565030455589
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1926598759953464
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9653857942193739,
              "spearman": 0.9592420742549619,
              "auroc_top30_worst": 0.9686588921282799,
              "pairwise_seed_ranking": 0.8992857142857142,
              "predicted_best_mean_error": 1.6356817347662789,
              "seed0_mean_error": 1.7149599373340607,
              "random_seed_mean_error": 1.686807851280485,
              "oracle_best_mean_error": 1.6336392905030932,
              "improvement_over_seed0": 0.07927820256778184,
              "gap_to_oracle": 0.002042444263185672,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0347880516733443
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2538960341044834
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4187852971894401
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5396988945915586
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.689799051965986
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.041977334022522,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6080093667620705,
                  "rejected_mean_error": 2.425906218801226,
                  "gap_rejected_minus_accepted": 0.8178968520391554
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8869367837905884,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5396988945915586,
                  "rejected_mean_error": 2.140099524089268,
                  "gap_rejected_minus_accepted": 0.6004006294977096
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7518829107284546,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4187852971894401,
                  "rejected_mean_error": 1.9608128067425319,
                  "gap_rejected_minus_accepted": 0.5420275095530918
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.505971521139145,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2538960341044834,
                  "rejected_mean_error": 1.8351000579198202,
                  "gap_rejected_minus_accepted": 0.5812040238153369
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.042035293579102,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6262628823991805,
                  "rejected_mean_error": 2.5132334317479814,
                  "gap_rejected_minus_accepted": 0.8869705493488009
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9224072694778442,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.562913966178894,
                  "rejected_mean_error": 2.1710978507995606,
                  "gap_rejected_minus_accepted": 0.6081838846206666
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.769450843334198,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.43862635578428,
                  "rejected_mean_error": 1.9912935188838414,
                  "gap_rejected_minus_accepted": 0.5526671630995614
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.524862915277481,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.2693602800369264,
                  "rejected_mean_error": 1.8634931564331054,
                  "gap_rejected_minus_accepted": 0.5941328763961791
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
        "best_epoch": 57,
        "best_calib_loss": 0.025813966989517212,
        "train_time_sec": 28.89898920059204,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.99941280486184,
              "spearman": 0.9967405515657907,
              "auroc_top30_bad": 0.9997986666666667,
              "mae": 0.0243542834373191,
              "mse": 0.001042235333712357,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.985,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7283783633081975,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.012504480807925574
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.07884992842404172
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.32491300067170525
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.675570286896918
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0274437544964952
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9994153658311542,
              "spearman": 0.9995357263894179,
              "auroc_top30_worst": 0.9998420952380952,
              "pairwise_seed_ranking": 0.9555,
              "predicted_best_mean_error": 1.423675792068243,
              "seed0_mean_error": 1.4977671349048614,
              "random_seed_mean_error": 1.4848491892814637,
              "oracle_best_mean_error": 1.4230901091992856,
              "improvement_over_seed0": 0.07409134283661833,
              "gap_to_oracle": 0.0005856828689574378,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5454105905890465
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7516451350450516
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0055175599694253
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.224102505437533
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4845065901339054
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2984471559524535,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3632128977841802,
                  "rejected_mean_error": 2.576149821281433,
                  "gap_rejected_minus_accepted": 1.212936923497253
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9056872129440308,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.224102505437533,
                  "rejected_mean_error": 2.2657188442230223,
                  "gap_rejected_minus_accepted": 1.0416163387854893
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4974473118782043,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0055175599694253,
                  "rejected_mean_error": 1.9634956202983855,
                  "gap_rejected_minus_accepted": 0.9579780603289603
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0733935832977295,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7516451350450516,
                  "rejected_mean_error": 1.72879374183019,
                  "gap_rejected_minus_accepted": 0.9771486067851384
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3250234127044678,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.373290293481615,
                  "rejected_mean_error": 2.6180587077140807,
                  "gap_rejected_minus_accepted": 1.2447684142324658
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9307469427585602,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2318696654637655,
                  "rejected_mean_error": 2.2954595432281493,
                  "gap_rejected_minus_accepted": 1.0635898777643837
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5088142156600952,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0106055274009704,
                  "rejected_mean_error": 1.9849287424087525,
                  "gap_rejected_minus_accepted": 0.9743232150077821
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0787299871444702,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7531408877372742,
                  "rejected_mean_error": 1.7459758839607238,
                  "gap_rejected_minus_accepted": 0.9928349962234496
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9722298521481723,
              "spearman": 0.9575185587207297,
              "auroc_top30_bad": 0.9789363809523809,
              "mae": 0.18462181316076312,
              "mse": 0.06912332222330768,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.944,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8148711220992289,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.22797011488676072
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.27113079187870026
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5466417430341244
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9683061374942462
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3556984712809323
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9523016049096112,
              "spearman": 0.9464425272592175,
              "auroc_top30_worst": 0.9716693333333334,
              "pairwise_seed_ranking": 0.9244,
              "predicted_best_mean_error": 1.9106740489006042,
              "seed0_mean_error": 2.0026443390846254,
              "random_seed_mean_error": 1.9835996059179306,
              "oracle_best_mean_error": 1.909254893541336,
              "improvement_over_seed0": 0.09197029018402114,
              "gap_to_oracle": 0.001419155359268176,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.83818359375
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1255636161718614
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.461361231803894
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7089177272213039
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9857149640083314
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5900742530822756,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8589757814407348,
                  "rejected_mean_error": 3.1263676071166993,
                  "gap_rejected_minus_accepted": 1.2673918256759644
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3312782645225525,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7083226546661068,
                  "rejected_mean_error": 2.8161194172149266,
                  "gap_rejected_minus_accepted": 1.1077967625488199
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9100875854492188,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.461361231803894,
                  "rejected_mean_error": 2.5100686962127687,
                  "gap_rejected_minus_accepted": 1.0487074644088747
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2917072772979736,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.126709921291461,
                  "rejected_mean_error": 2.272661152237126,
                  "gap_rejected_minus_accepted": 1.1459512309456648
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.650807237625122,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.871803921063741,
                  "rejected_mean_error": 3.180208101272583,
                  "gap_rejected_minus_accepted": 1.3084041802088422
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3625088930130005,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7203974245703795,
                  "rejected_mean_error": 2.840424863118974,
                  "gap_rejected_minus_accepted": 1.1200274385485947
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9216095805168152,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4725613584518433,
                  "rejected_mean_error": 2.532727319717407,
                  "gap_rejected_minus_accepted": 1.0601659612655638
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3077726662158966,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1369693809085422,
                  "rejected_mean_error": 2.2942888437107922,
                  "gap_rejected_minus_accepted": 1.15731946280225
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9518284844311455,
              "spearman": 0.9493576873118147,
              "auroc_top30_bad": 0.998472380952381,
              "mae": 0.2115167992899078,
              "mse": 0.13888688459926138,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.872,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.7109355078747333,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.30364427423477175
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2842556725502014
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.48232874722480773
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7860641102790833
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2596822590589523
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9584373761098137,
              "spearman": 0.9878392098810944,
              "auroc_top30_worst": 0.9993051428571428,
              "pairwise_seed_ranking": 0.9216,
              "predicted_best_mean_error": 1.7137403535842894,
              "seed0_mean_error": 1.7879177272319793,
              "random_seed_mean_error": 1.7802261937856674,
              "oracle_best_mean_error": 1.711424299120903,
              "improvement_over_seed0": 0.07417737364768984,
              "gap_to_oracle": 0.002316054463386452,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5390931434631347
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7528158261989936
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0075834442138671
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.258815603215557
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7832511980056762
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.640628242492676,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5570566715664333,
                  "rejected_mean_error": 3.8190019359588625,
                  "gap_rejected_minus_accepted": 2.261945264392429
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1935532689094543,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2577089838437108,
                  "rejected_mean_error": 3.3565197432764804,
                  "gap_rejected_minus_accepted": 2.0988107594327694
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3986731171607971,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0075834442138671,
                  "rejected_mean_error": 2.5589189517974855,
                  "gap_rejected_minus_accepted": 1.5513355075836184
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.026336908340454,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7541815350992611,
                  "rejected_mean_error": 2.127006592338342,
                  "gap_rejected_minus_accepted": 1.372825057239081
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6369564533233643,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5575807441605463,
                  "rejected_mean_error": 3.860950574874878,
                  "gap_rejected_minus_accepted": 2.3033698307143315
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2676708698272705,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2554791072473168,
                  "rejected_mean_error": 3.3683307738531205,
                  "gap_rejected_minus_accepted": 2.1128516666058035
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3996192812919617,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0018821206092834,
                  "rejected_mean_error": 2.5739533338546754,
                  "gap_rejected_minus_accepted": 1.572071213245392
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0321536660194397,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.75107013706177,
                  "rejected_mean_error": 2.137230016968467,
                  "gap_rejected_minus_accepted": 1.386159879906697
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9726279672026097,
              "spearman": 0.9599045827920365,
              "auroc_top30_bad": 0.9909548104956268,
              "mae": 0.12150322053643842,
              "mse": 0.03750206127344348,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.750044244957435,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.24758528577429909
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.27720115763800485
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5549127363945756
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9127890283578918
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1926598759953464
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9693884815996866,
              "spearman": 0.9611000838777222,
              "auroc_top30_worst": 0.9692419825072887,
              "pairwise_seed_ranking": 0.9121428571428571,
              "predicted_best_mean_error": 1.6357956094401223,
              "seed0_mean_error": 1.7149599373340607,
              "random_seed_mean_error": 1.686807851280485,
              "oracle_best_mean_error": 1.6336392905030932,
              "improvement_over_seed0": 0.07916432789393846,
              "gap_to_oracle": 0.002156318937029056,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0368706243378776
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.255076219013759
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4172546887397766
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5399299219676426
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.689799051965986
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.048008441925049,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6081037267806038,
                  "rejected_mean_error": 2.4250569786344256,
                  "gap_rejected_minus_accepted": 0.8169532518538218
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8943182826042175,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5399299219676426,
                  "rejected_mean_error": 2.139406441961016,
                  "gap_rejected_minus_accepted": 0.5994765199933734
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7000473141670227,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4172546887397766,
                  "rejected_mean_error": 1.9623434151921952,
                  "gap_rejected_minus_accepted": 0.5450887264524187
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4741512537002563,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.255076219013759,
                  "rejected_mean_error": 1.8347066629500617,
                  "gap_rejected_minus_accepted": 0.5796304439363027
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0701104402542114,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6262628823991805,
                  "rejected_mean_error": 2.5132334317479814,
                  "gap_rejected_minus_accepted": 0.8869705493488009
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9134398698806763,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5630248376301357,
                  "rejected_mean_error": 2.1707652364458356,
                  "gap_rejected_minus_accepted": 0.6077403988157
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7159311771392822,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4386134999138969,
                  "rejected_mean_error": 1.9913063747542246,
                  "gap_rejected_minus_accepted": 0.5526928748403277
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4933720529079437,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.2661775384630476,
                  "rejected_mean_error": 1.864554070291065,
                  "gap_rejected_minus_accepted": 0.5983765318280174
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
        "best_epoch": 66,
        "best_calib_loss": 0.09986625611782074,
        "train_time_sec": 10.736005544662476,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.965934373939187,
              "spearman": 0.9195400333716601,
              "auroc_top30_bad": 0.9993369047619047,
              "mae": 0.13318924723735368,
              "mse": 0.04150476109615007,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5697409974269585,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.13794619277119635
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.14043688859343528
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.05660165721178055
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.2501924601316452
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.5763885291039944
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.996326245781309,
              "spearman": 0.9969832516233299,
              "auroc_top30_worst": 0.9987634285714285,
              "pairwise_seed_ranking": 0.83215,
              "predicted_best_mean_error": 0.9221724024116993,
              "seed0_mean_error": 0.9891108637154102,
              "random_seed_mean_error": 0.9764430523514748,
              "oracle_best_mean_error": 0.9150177699029446,
              "improvement_over_seed0": 0.06693846130371095,
              "gap_to_oracle": 0.007154632508754699,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05022719746828079
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2550467267274857
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5072460357308388
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7204471087217331
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.975946728593111
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7627878665924073,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.8566371441748407,
                  "rejected_mean_error": 2.049732988357544,
                  "gap_rejected_minus_accepted": 1.1930958441827033
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.380268633365631,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7204471087217331,
                  "rejected_mean_error": 1.742445588207245,
                  "gap_rejected_minus_accepted": 1.0219984794855117
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9722144305706024,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5072460357308388,
                  "rejected_mean_error": 1.4446474214553833,
                  "gap_rejected_minus_accepted": 0.9374013857245445
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.568852499127388,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.2550467267274857,
                  "rejected_mean_error": 1.216246729214986,
                  "gap_rejected_minus_accepted": 0.9612000024875005
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7954192757606506,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8666230539811982,
                  "rejected_mean_error": 2.0915011513233184,
                  "gap_rejected_minus_accepted": 1.22487809734212
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3969276547431946,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.728190027753512,
                  "rejected_mean_error": 1.7718733716011048,
                  "gap_rejected_minus_accepted": 1.0436833438475928
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9891702234745026,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5120956935286521,
                  "rejected_mean_error": 1.4661260339021682,
                  "gap_rejected_minus_accepted": 0.9540303403735161
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5778606086969376,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.2556852082014084,
                  "rejected_mean_error": 1.2335860822200775,
                  "gap_rejected_minus_accepted": 0.9779008740186691
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8998366513529497,
              "spearman": 0.8748255642556942,
              "auroc_top30_bad": 0.9677592380952381,
              "mae": 0.5076513925661716,
              "mse": 0.3832279364331006,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6420208109926464,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.22533199501037599
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23215021455287935
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.40190642231702806
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7989052707513173
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1917876716971398
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.845993282395755,
              "spearman": 0.8682055430435476,
              "auroc_top30_worst": 0.9216365714285715,
              "pairwise_seed_ranking": 0.8054,
              "predicted_best_mean_error": 1.7496646244525909,
              "seed0_mean_error": 1.8282812159061432,
              "random_seed_mean_error": 1.8093355172872543,
              "oracle_best_mean_error": 1.7350634887218475,
              "improvement_over_seed0": 0.07861659145355238,
              "gap_to_oracle": 0.014601135730743398,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8541651997566223
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8533284039451525
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2277885995864868
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.533515683432886
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114202166080475
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9329328775405885,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.671409493393368,
                  "rejected_mean_error": 3.071516725540161,
                  "gap_rejected_minus_accepted": 1.4001072321467931
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.618892341852188,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.532696787104917,
                  "rejected_mean_error": 2.645809524737227,
                  "gap_rejected_minus_accepted": 1.1131127376323098
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3335784673690796,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2277885995864868,
                  "rejected_mean_error": 2.395051833629608,
                  "gap_rejected_minus_accepted": 1.1672632340431213
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8953352719545364,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8559313218433636,
                  "rejected_mean_error": 2.1305963362039346,
                  "gap_rejected_minus_accepted": 1.2746650143605711
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9684023737907408,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.685667434533437,
                  "rejected_mean_error": 3.111805248260498,
                  "gap_rejected_minus_accepted": 1.4261378137270608
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6190126538276672,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5369528458717672,
                  "rejected_mean_error": 2.69301780632564,
                  "gap_rejected_minus_accepted": 1.1560649604538726
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3657483458518982,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2564297747611999,
                  "rejected_mean_error": 2.4001326570510866,
                  "gap_rejected_minus_accepted": 1.1437028822898867
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9224620312452316,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8414225786451309,
                  "rejected_mean_error": 2.1607523076037034,
                  "gap_rejected_minus_accepted": 1.3193297289585724
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8134653019006938,
              "spearman": 0.8376658984963211,
              "auroc_top30_bad": 0.965367619047619,
              "mae": 0.5971151014792268,
              "mse": 0.6511721837663307,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.52,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.5722292636838824,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.34867491137981416
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3693125457048416
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5026600876808166
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8370252574046453
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2210977756500243
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7318592956607218,
              "spearman": 0.8173661899303616,
              "auroc_top30_worst": 0.8696472380952381,
              "pairwise_seed_ranking": 0.7628,
              "predicted_best_mean_error": 1.687611334323883,
              "seed0_mean_error": 1.7466381919384002,
              "random_seed_mean_error": 1.7389194325208663,
              "oracle_best_mean_error": 1.6701291526556015,
              "improvement_over_seed0": 0.0590268576145172,
              "gap_to_oracle": 0.017482181668281527,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5931167271137238
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7781255558515207
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.147823976612091
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4530474312269865
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.741942658138275
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8587928771972657,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5856350056330364,
                  "rejected_mean_error": 3.148711530685425,
                  "gap_rejected_minus_accepted": 1.5630765250523886
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4969914555549622,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.452344237803904,
                  "rejected_mean_error": 2.608887450001872,
                  "gap_rejected_minus_accepted": 1.156543212197968
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0224485397338867,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.147823976612091,
                  "rejected_mean_error": 2.336061339664459,
                  "gap_rejected_minus_accepted": 1.1882373630523682
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5047388076782227,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7803414324982859,
                  "rejected_mean_error": 2.063160570225059,
                  "gap_rejected_minus_accepted": 1.282819137726773
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8941596269607544,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5919541303316753,
                  "rejected_mean_error": 3.1387947463989256,
                  "gap_rejected_minus_accepted": 1.5468406160672503
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5071232914924622,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4382139976649362,
                  "rejected_mean_error": 2.662119530496143,
                  "gap_rejected_minus_accepted": 1.223905532831207
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.04030042886734,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1513368639945984,
                  "rejected_mean_error": 2.341939519882202,
                  "gap_rejected_minus_accepted": 1.1906026558876037
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.48576176166534424,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7822520903178624,
                  "rejected_mean_error": 2.071538322430881,
                  "gap_rejected_minus_accepted": 1.2892862321130187
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.8266073266790278,
              "spearman": 0.8214444345701646,
              "auroc_top30_bad": 0.8989747327502429,
              "mae": 0.5295694526061822,
              "mse": 0.42980047870366817,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.5428571428571428,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5425086497856758,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3378055383052145
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3409044228707041
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5469243751892022
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8662150889351254
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1175981296811786
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.6006168367837629,
              "spearman": 0.47772300409942525,
              "auroc_top30_worst": 0.7717298347910593,
              "pairwise_seed_ranking": 0.7371428571428571,
              "predicted_best_mean_error": 1.5699222786085947,
              "seed0_mean_error": 1.636711407985006,
              "random_seed_mean_error": 1.6086368956736157,
              "oracle_best_mean_error": 1.5554576026541846,
              "improvement_over_seed0": 0.06678912937641135,
              "gap_to_oracle": 0.014464675954410033,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3557146770613535
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4121617555618287
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.451730602809361
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4911992514701116
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.611691865154675
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6764998078346254,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.5324030237538473,
                  "rejected_mean_error": 2.3252914377621243,
                  "gap_rejected_minus_accepted": 0.792888414008277
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.2309176921844482,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.4911992514701116,
                  "rejected_mean_error": 1.9731697062083653,
                  "gap_rejected_minus_accepted": 0.48197045473825373
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.994370311498642,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.451730602809361,
                  "rejected_mean_error": 1.7716531274999892,
                  "gap_rejected_minus_accepted": 0.3199225246906281
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5738069862127304,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.4121617555618287,
                  "rejected_mean_error": 1.678201901685624,
                  "gap_rejected_minus_accepted": 0.26604014612379534
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7201772689819341,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.546764411150463,
                  "rejected_mean_error": 2.4462343794958934,
                  "gap_rejected_minus_accepted": 0.8994699683454304
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.2817028164863586,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5001923952783858,
                  "rejected_mean_error": 2.0462684461048672,
                  "gap_rejected_minus_accepted": 0.5460760508264815
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9986265599727631,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4707657200949533,
                  "rejected_mean_error": 1.802657095875059,
                  "gap_rejected_minus_accepted": 0.33189137578010564
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.59454745054245,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.4168767486299787,
                  "rejected_mean_error": 1.709989627770015,
                  "gap_rejected_minus_accepted": 0.29311287914003636
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
        "best_epoch": 41,
        "best_calib_loss": 0.06652499735355377,
        "train_time_sec": 35.16021013259888,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9777892153636792,
              "spearman": 0.9652639027511178,
              "auroc_top30_bad": 0.9996010476190477,
              "mae": 0.13554192347917707,
              "mse": 0.036200167854338834,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.887,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.5814899180564328,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.2773756632804871
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.2473395566344261
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.06027940036654472
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.25024483573436734
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.5763885291039944
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9984547410761727,
              "spearman": 0.9990748907549735,
              "auroc_top30_worst": 0.9995689523809523,
              "pairwise_seed_ranking": 0.9236,
              "predicted_best_mean_error": 0.9170097538232803,
              "seed0_mean_error": 0.9891108637154102,
              "random_seed_mean_error": 0.9764430523514748,
              "oracle_best_mean_error": 0.9150177699029446,
              "improvement_over_seed0": 0.07210110989212992,
              "gap_to_oracle": 0.001991983920335727,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.047918259859085086
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2535071676969528
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5064463668942452
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7197825979630152
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.975946728593111
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8174360036849981,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.8564251057902972,
                  "rejected_mean_error": 2.0516413338184356,
                  "gap_rejected_minus_accepted": 1.1952162280281384
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4306103885173798,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7197825979630152,
                  "rejected_mean_error": 1.7444391204833984,
                  "gap_rejected_minus_accepted": 1.0246565225203832
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0070016980171204,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5064463668942452,
                  "rejected_mean_error": 1.445447090291977,
                  "gap_rejected_minus_accepted": 0.9390007233977318
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5912253558635712,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.2535071676969528,
                  "rejected_mean_error": 1.2167599155584972,
                  "gap_rejected_minus_accepted": 0.9632527478615444
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8463115811347963,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8665795506702529,
                  "rejected_mean_error": 2.091892681121826,
                  "gap_rejected_minus_accepted": 1.2253131304515732
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4547235369682312,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.727631984591484,
                  "rejected_mean_error": 1.7735475010871886,
                  "gap_rejected_minus_accepted": 1.0459155164957046
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0187257528305054,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5113035364747047,
                  "rejected_mean_error": 1.4669181909561158,
                  "gap_rejected_minus_accepted": 0.955614654481411
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6019901186227798,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.2544819492101669,
                  "rejected_mean_error": 1.2339871685504913,
                  "gap_rejected_minus_accepted": 0.9795052193403244
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.967109585207045,
              "spearman": 0.9478018682679237,
              "auroc_top30_bad": 0.9887192380952381,
              "mae": 0.3737318482727744,
              "mse": 0.19751343138265154,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.844,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6890794506180399,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10102968549728393
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.14581947021484376
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3522097664117813
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7762481604735056
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1917876716971398
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9754205590658375,
              "spearman": 0.9824216422538512,
              "auroc_top30_worst": 0.9851306666666666,
              "pairwise_seed_ranking": 0.9116,
              "predicted_best_mean_error": 1.7362723780870437,
              "seed0_mean_error": 1.8282812159061432,
              "random_seed_mean_error": 1.8093355172872543,
              "oracle_best_mean_error": 1.7350634887218475,
              "improvement_over_seed0": 0.09200883781909952,
              "gap_to_oracle": 0.001208889365196253,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5421326026916504
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7500494126325998
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1785234694480895
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4990645878986
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114202166080475
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0685543298721316,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6648127363522847,
                  "rejected_mean_error": 3.1308875389099122,
                  "gap_rejected_minus_accepted": 1.4660748025576276
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8268652260303497,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4982250579647727,
                  "rejected_mean_error": 2.749004445517787,
                  "gap_rejected_minus_accepted": 1.2507793875530142
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4654954075813293,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1785234694480895,
                  "rejected_mean_error": 2.4443169637680056,
                  "gap_rejected_minus_accepted": 1.265793494319916
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8614168763160706,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7512766709342932,
                  "rejected_mean_error": 2.1655556806378073,
                  "gap_rejected_minus_accepted": 1.414279009703514
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0911245584487914,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6780671175320943,
                  "rejected_mean_error": 3.180208101272583,
                  "gap_rejected_minus_accepted": 1.5021409837404889
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8553540110588074,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5049894624215396,
                  "rejected_mean_error": 2.787893246090601,
                  "gap_rejected_minus_accepted": 1.2829037836690615
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.47751784324646,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.185419050693512,
                  "rejected_mean_error": 2.4711433811187744,
                  "gap_rejected_minus_accepted": 1.2857243304252624
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8876052349805832,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7460433623147389,
                  "rejected_mean_error": 2.192885412570627,
                  "gap_rejected_minus_accepted": 1.446842050255888
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9471699429394331,
              "spearman": 0.9480954302089956,
              "auroc_top30_bad": 0.9968137142857143,
              "mae": 0.48068183525452624,
              "mse": 0.3662514968196648,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.86,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.624522888969376,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.22668621718883514
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2825042200088501
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45427388920783995
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7674712503433228
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2210977756500243
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9360996688864541,
              "spearman": 0.9853672497710398,
              "auroc_top30_worst": 0.9968121904761904,
              "pairwise_seed_ranking": 0.9,
              "predicted_best_mean_error": 1.6749549785852431,
              "seed0_mean_error": 1.7466381919384002,
              "random_seed_mean_error": 1.7389194325208663,
              "oracle_best_mean_error": 1.6701291526556015,
              "improvement_over_seed0": 0.07168321335315708,
              "gap_to_oracle": 0.004825825929641647,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5174518027305604
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7538699700664251
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.011157878112793
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2621651952708963
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.741942658138275
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0137878179550173,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5312561197280883,
                  "rejected_mean_error": 3.638121503829956,
                  "gap_rejected_minus_accepted": 2.1068653841018676
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6844378113746643,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2607343689227435,
                  "rejected_mean_error": 3.1824927124352502,
                  "gap_rejected_minus_accepted": 1.9217583435125067
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0607247352600098,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.011157878112793,
                  "rejected_mean_error": 2.472727438163757,
                  "gap_rejected_minus_accepted": 1.4615695600509642
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6089280694723129,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7553119767969028,
                  "rejected_mean_error": 2.071521530347293,
                  "gap_rejected_minus_accepted": 1.3162095535503902
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9796203017234801,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.538827684985267,
                  "rejected_mean_error": 3.6169327545166015,
                  "gap_rejected_minus_accepted": 2.0781050695313343
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7087861597537994,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.261959909436537,
                  "rejected_mean_error": 3.1852864273010737,
                  "gap_rejected_minus_accepted": 1.9233265178645367
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.056407392024994,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0059282069206237,
                  "rejected_mean_error": 2.4873481769561767,
                  "gap_rejected_minus_accepted": 1.481419970035553
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6303559690713882,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.750745399603768,
                  "rejected_mean_error": 2.0821528759869663,
                  "gap_rejected_minus_accepted": 1.3314074763831982
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9441650647227654,
              "spearman": 0.9324106829388134,
              "auroc_top30_bad": 0.9627308066083576,
              "mae": 0.31911508440526504,
              "mse": 0.1389552193657709,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.8642857142857143,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.627641828814555,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.125785943120718
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19171092714582172
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4839520641735622
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8442559123039246
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1175981296811786
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9119990249398467,
              "spearman": 0.8782430984553029,
              "auroc_top30_worst": 0.9213313896987367,
              "pairwise_seed_ranking": 0.8721428571428571,
              "predicted_best_mean_error": 1.5601151334387915,
              "seed0_mean_error": 1.636711407985006,
              "random_seed_mean_error": 1.6086368956736157,
              "oracle_best_mean_error": 1.5554576026541846,
              "improvement_over_seed0": 0.07659627454621454,
              "gap_to_oracle": 0.004657530784606845,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0324221006461551
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1808089736529759
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.356485696690423
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4605484364146277
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.611691865154675
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6984560251235963,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.5230950517313822,
                  "rejected_mean_error": 2.4090631859643117,
                  "gap_rejected_minus_accepted": 0.8859681342329295
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4981307685375214,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.4605484364146277,
                  "rejected_mean_error": 2.065122151374817,
                  "gap_rejected_minus_accepted": 0.6045737149601891
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3066152334213257,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.356485696690423,
                  "rejected_mean_error": 1.866898033618927,
                  "gap_rejected_minus_accepted": 0.5104123369285039
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.06843963265419,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.1808089736529759,
                  "rejected_mean_error": 1.7553194956552414,
                  "gap_rejected_minus_accepted": 0.5745105220022655
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7600262522697452,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.5413438673057254,
                  "rejected_mean_error": 2.4950192740985324,
                  "gap_rejected_minus_accepted": 0.953675406792807
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.537584364414215,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.4812037496339707,
                  "rejected_mean_error": 2.103234383038112,
                  "gap_rejected_minus_accepted": 0.6220306334041412
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3194385170936584,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.3818564985479627,
                  "rejected_mean_error": 1.8915663174220494,
                  "gap_rejected_minus_accepted": 0.5097098188740867
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0841930210590363,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.1959637863295418,
                  "rejected_mean_error": 1.7836272818701608,
                  "gap_rejected_minus_accepted": 0.587663495540619
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
        "best_epoch": 15,
        "best_calib_loss": 0.27546459436416626,
        "train_time_sec": 364.4337692260742,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.012823723790103245,
              "spearman": -0.057948014291218576,
              "auroc_top30_bad": 0.46389885714285717,
              "mae": 0.7381548099084302,
              "mse": 0.8735144095052907,
              "expert_lt_perturb_large": 0.744,
              "expert_lt_other_task": 0.773,
              "expert_lt_simvla_seed0": 0.528,
              "same_context_pred_std": 0.0004856824384100667,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8071108757555485
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.676972757101059
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6080395650625229
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.579349481010437
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.5763885291039944
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.01521009819002548,
              "spearman": -0.28016557024662275,
              "auroc_top30_worst": 0.41982095238095246,
              "pairwise_seed_ranking": 0.5345,
              "predicted_best_mean_error": 0.947676969498396,
              "seed0_mean_error": 0.9891108637154102,
              "random_seed_mean_error": 0.9764430523514748,
              "oracle_best_mean_error": 0.9150177699029446,
              "improvement_over_seed0": 0.04143389421701427,
              "gap_to_oracle": 0.03265919959545138,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2423210743665696
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1840106643199921
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1019105457782745
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.015056311058998
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.975946728593111
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.1266050421454591e-07,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9968180834783448,
                  "rejected_mean_error": 0.788104534626007,
                  "gap_rejected_minus_accepted": -0.20871354885233773
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 4.128014735593766e-10,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.015056311058998,
                  "rejected_mean_error": 0.8586179811954499,
                  "gap_rejected_minus_accepted": -0.15643832986354822
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 5.620753157613984e-13,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.1019105457782745,
                  "rejected_mean_error": 0.8499829114079476,
                  "gap_rejected_minus_accepted": -0.25192763437032695
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 9.769915447554127e-16,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 1.1840106643199921,
                  "rejected_mean_error": 0.9065920833508173,
                  "gap_rejected_minus_accepted": -0.2774185809691748
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.1740890215605765e-07,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.010701404677497,
                  "rejected_mean_error": 0.7947959950566292,
                  "gap_rejected_minus_accepted": -0.21590540962086768
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 4.381723456292619e-10,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.0311030514240265,
                  "rejected_mean_error": 0.8631343005895614,
                  "gap_rejected_minus_accepted": -0.16796875083446505
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 5.449819740453721e-13,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.11831374335289,
                  "rejected_mean_error": 0.8599079840779305,
                  "gap_rejected_minus_accepted": -0.25840575927495957
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0848135714547444e-15,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 1.2095354907512665,
                  "rejected_mean_error": 0.9156359880367915,
                  "gap_rejected_minus_accepted": -0.29389950271447507
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.02087276541827897,
              "spearman": -0.19800061378794662,
              "auroc_top30_bad": 0.4102620952380952,
              "mae": 1.2150354106951298,
              "mse": 2.3487298751768155,
              "expert_lt_perturb_large": 0.54,
              "expert_lt_other_task": 0.832,
              "expert_lt_simvla_seed0": 0.416,
              "same_context_pred_std": 0.0015844892707971244,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0711728560328484
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2758235616445541
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.410373513185978
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3486572863340378
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1917876716971398
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": -0.01648936727560245,
              "spearman": -0.2743230079507251,
              "auroc_top30_worst": 0.427712,
              "pairwise_seed_ranking": 0.4824,
              "predicted_best_mean_error": 1.795262957572937,
              "seed0_mean_error": 1.8282812159061432,
              "random_seed_mean_error": 1.8093355172872543,
              "oracle_best_mean_error": 1.7350634887218475,
              "improvement_over_seed0": 0.03301825833320615,
              "gap_to_oracle": 0.06019946885108962,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3177541189193727
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.7848576475412419
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 2.044216027164459
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 2.032520067907854
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114202166080475
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 4.623828914418499e-07,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8861288963423835,
                  "rejected_mean_error": 1.1390420989990235,
                  "gap_rejected_minus_accepted": -0.7470867973433599
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.793442671096159e-09,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 2.0341026943928404,
                  "rejected_mean_error": 1.1447956744855203,
                  "gap_rejected_minus_accepted": -0.8893070199073201
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 5.819242874030572e-12,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 2.044216027164459,
                  "rejected_mean_error": 1.5786244060516357,
                  "gap_rejected_minus_accepted": -0.4655916211128235
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.9247589423866526e-14,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.7861712915828813,
                  "rejected_mean_error": 1.8198544893218969,
                  "gap_rejected_minus_accepted": 0.033683197739015514
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 5.121744948155536e-07,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.9077917149331836,
                  "rejected_mean_error": 1.1126867246627807,
                  "gap_rejected_minus_accepted": -0.7951049902704028
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.605007625751e-09,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 2.0671113818724525,
                  "rejected_mean_error": 1.1193726280378917,
                  "gap_rejected_minus_accepted": -0.9477387538345607
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 6.15988531883771e-12,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 2.074303512573242,
                  "rejected_mean_error": 1.5822589192390442,
                  "gap_rejected_minus_accepted": -0.4920445933341979
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 3.2343775213986535e-14,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.7900991458741446,
                  "rejected_mean_error": 1.8411446940452658,
                  "gap_rejected_minus_accepted": 0.05104554817112117
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.015815161596563352,
              "spearman": -0.15357796014067493,
              "auroc_top30_bad": 0.44469790476190485,
              "mae": 1.2227256273694826,
              "mse": 2.4825879686796486,
              "expert_lt_perturb_large": 0.508,
              "expert_lt_other_task": 0.732,
              "expert_lt_simvla_seed0": 0.388,
              "same_context_pred_std": 0.0004537180989390683,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.25592199331522
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2137872022867202
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.339278533923626
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3378400129159291
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2210977756500243
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": -0.03037071777306868,
              "spearman": -0.3236178997874559,
              "auroc_top30_worst": 0.39357561904761906,
              "pairwise_seed_ranking": 0.5342,
              "predicted_best_mean_error": 1.7155088366270066,
              "seed0_mean_error": 1.7466381919384002,
              "random_seed_mean_error": 1.7389194325208663,
              "oracle_best_mean_error": 1.6701291526556015,
              "improvement_over_seed0": 0.031129355311393603,
              "gap_to_oracle": 0.04537968397140513,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.7196024289131164
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.6497477394266007
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.9717709052085877
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.9718663732507336
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.741942658138275
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6288189215174505e-07,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7915311482217577,
                  "rejected_mean_error": 1.2956462473869323,
                  "gap_rejected_minus_accepted": -0.4958849008348254
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 8.37665270481125e-09,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.973133771689241,
                  "rejected_mean_error": 1.0498465769968854,
                  "gap_rejected_minus_accepted": -0.9232871946923555
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 3.3562484388904856e-12,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.9717709052085877,
                  "rejected_mean_error": 1.5121144110679627,
                  "gap_rejected_minus_accepted": -0.4596564941406249
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 8.703808810497731e-17,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.6550443661860383,
                  "rejected_mean_error": 1.7709705827711995,
                  "gap_rejected_minus_accepted": 0.11592621658516111
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.4286308243072182e-07,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8004079294204711,
                  "rejected_mean_error": 1.262710554599762,
                  "gap_rejected_minus_accepted": -0.5376973748207092
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 8.228580039570943e-09,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.9921990645760521,
                  "rejected_mean_error": 1.017751157283783,
                  "gap_rejected_minus_accepted": -0.9744479072922692
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 3.778804309392814e-12,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 2.0016549324989317,
                  "rejected_mean_error": 1.4916214513778687,
                  "gap_rejected_minus_accepted": -0.510033481121063
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 7.411853113416266e-17,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.672770070651221,
                  "rejected_mean_error": 1.7715242434950436,
                  "gap_rejected_minus_accepted": 0.0987541728438226
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.041695580825770434,
              "spearman": 0.07746473991481234,
              "auroc_top30_bad": 0.5556195335276968,
              "mae": 1.1351748951010934,
              "mse": 1.8098029615322484,
              "expert_lt_perturb_large": 0.6428571428571429,
              "expert_lt_other_task": 0.75,
              "expert_lt_simvla_seed0": 0.5785714285714286,
              "same_context_pred_std": 8.927655422742517e-07,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.5512630532894816
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1639721674152783
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.022288289453302
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0760397623266493
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1175981296811786
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": null,
              "spearman": null,
              "auroc_top30_worst": null,
              "pairwise_seed_ranking": 0.5046428571428572,
              "predicted_best_mean_error": 1.6008050731250218,
              "seed0_mean_error": 1.636711407985006,
              "random_seed_mean_error": 1.6086368956736157,
              "oracle_best_mean_error": 1.5554576026541846,
              "improvement_over_seed0": 0.03590633485998418,
              "gap_to_oracle": 0.0453474704708372,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.718403137581689
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.6375563832691737
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.635775066273553
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6452092484065464
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.611691865154675
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.305412083985049e-10,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6225842096502818,
                  "rejected_mean_error": 1.513660764694214,
                  "gap_rejected_minus_accepted": -0.10892344495606787
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.80606202336664e-12,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.6452092484065464,
                  "rejected_mean_error": 1.511139715399061,
                  "gap_rejected_minus_accepted": -0.13406953300748548
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 6.180634414096504e-14,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.635775066273553,
                  "rejected_mean_error": 1.5876086640357971,
                  "gap_rejected_minus_accepted": -0.04816640223775592
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.447469937355779e-16,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.6375563832691737,
                  "rejected_mean_error": 1.6030703591165087,
                  "gap_rejected_minus_accepted": -0.034486024152664996
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.3386021319172806e-10,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6562452841372717,
                  "rejected_mean_error": 1.4609065226146154,
                  "gap_rejected_minus_accepted": -0.19533876152265628
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 3.3881515757068492e-12,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.6762865571748642,
                  "rejected_mean_error": 1.5179859604154313,
                  "gap_rejected_minus_accepted": -0.15830059675943287
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 6.91595997864055e-14,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.661818757227489,
                  "rejected_mean_error": 1.611604058742523,
                  "gap_rejected_minus_accepted": -0.05021469848496585
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 2.1777889406309945e-16,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.691453492641449,
                  "rejected_mean_error": 1.6184640464328583,
                  "gap_rejected_minus_accepted": -0.07298944620859071
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
        "best_epoch": 40,
        "best_calib_loss": 0.07903344929218292,
        "train_time_sec": 29.22080945968628,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9650396583072293,
              "spearman": 0.8953460921968911,
              "auroc_top30_bad": 0.9998765238095239,
              "mae": 0.12815396896576386,
              "mse": 0.04210733974813132,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.336,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5812577543597824,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.018133965656161308
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.08792315646409989
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.057046846306324006
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.2498579820394516
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.5763885291039944
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.998827667963543,
              "spearman": 0.9994382313775158,
              "auroc_top30_worst": 0.9996106666666666,
              "pairwise_seed_ranking": 0.9448,
              "predicted_best_mean_error": 0.9161204338669777,
              "seed0_mean_error": 0.9891108637154102,
              "random_seed_mean_error": 0.9764430523514748,
              "oracle_best_mean_error": 0.9150177699029446,
              "improvement_over_seed0": 0.07299042984843251,
              "gap_to_oracle": 0.0011026639640331348,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.047250880360603334
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2532762425661087
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5063478895068169
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7199744550784429
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.975946728593111
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7721308112144472,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.8563958944810761,
                  "rejected_mean_error": 2.051904235601425,
                  "gap_rejected_minus_accepted": 1.1955083411203489
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3836245238780975,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7199744550784429,
                  "rejected_mean_error": 1.7438635491371155,
                  "gap_rejected_minus_accepted": 1.0238890940586725
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.968685120344162,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5063478895068169,
                  "rejected_mean_error": 1.4455455676794051,
                  "gap_rejected_minus_accepted": 0.9391976781725883
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5739275068044662,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.2532762425661087,
                  "rejected_mean_error": 1.2168368906021119,
                  "gap_rejected_minus_accepted": 0.9635606480360032
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8080781936645507,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8664919682674938,
                  "rejected_mean_error": 2.0926809227466583,
                  "gap_rejected_minus_accepted": 1.2261889544791647
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.404064416885376,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7278378115097681,
                  "rejected_mean_error": 1.7729300203323364,
                  "gap_rejected_minus_accepted": 1.0450922088225683
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.974348396062851,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5112843827605248,
                  "rejected_mean_error": 1.4669373446702958,
                  "gap_rejected_minus_accepted": 0.955652961909771
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5766313672065735,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.2543441325426102,
                  "rejected_mean_error": 1.2340331074396769,
                  "gap_rejected_minus_accepted": 0.9796889748970667
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9536802541474629,
              "spearman": 0.8940784700377273,
              "auroc_top30_bad": 0.9873584761904762,
              "mae": 0.4228661905200806,
              "mse": 0.2611395643399206,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.448,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6857528271682338,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.32517774146795275
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3031946426391602
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3549701152563095
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7758879203001658
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1917876716971398
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9704612747107393,
              "spearman": 0.9754598283902902,
              "auroc_top30_worst": 0.9767680000000001,
              "pairwise_seed_ranking": 0.9196,
              "predicted_best_mean_error": 1.7367234128713607,
              "seed0_mean_error": 1.8282812159061432,
              "random_seed_mean_error": 1.8093355172872543,
              "oracle_best_mean_error": 1.7350634887218475,
              "improvement_over_seed0": 0.09155780303478256,
              "gap_to_oracle": 0.0016599241495132144,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6017167043685913
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7506798677719556
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1807404204368592
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5026365473453425
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8114202166080475
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0352031230926517,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.665737638314565,
                  "rejected_mean_error": 3.1225634212493896,
                  "gap_rejected_minus_accepted": 1.4568257829348246
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7448525130748749,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5018965348744469,
                  "rejected_mean_error": 2.73801347470512,
                  "gap_rejected_minus_accepted": 1.2361169398306733
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4071965217590332,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1807404204368592,
                  "rejected_mean_error": 2.442100012779236,
                  "gap_rejected_minus_accepted": 1.2613595923423766
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9028062671422958,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7514128037534964,
                  "rejected_mean_error": 2.165510206174189,
                  "gap_rejected_minus_accepted": 1.4140974024206927
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.082978940010071,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6780650724305046,
                  "rejected_mean_error": 3.1802265071868896,
                  "gap_rejected_minus_accepted": 1.502161434756385
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.779344618320465,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5091877241823124,
                  "rejected_mean_error": 2.7754317389594183,
                  "gap_rejected_minus_accepted": 1.266244014777106
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.421915352344513,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1857888436317443,
                  "rejected_mean_error": 2.470773588180542,
                  "gap_rejected_minus_accepted": 1.2849847445487976
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9465277940034866,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7515263226297166,
                  "rejected_mean_error": 2.191038212036704,
                  "gap_rejected_minus_accepted": 1.4395118894069874
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9410960706443308,
              "spearman": 0.8851730734994542,
              "auroc_top30_bad": 0.9955062857142858,
              "mae": 0.5385543442398323,
              "mse": 0.4404862984875739,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.312,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6216754465873966,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4968603907823563
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4067125545978546
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4604263868331909
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7670158130009969
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2210977756500243
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9487096391956532,
              "spearman": 0.9824705853891746,
              "auroc_top30_worst": 0.9979611428571429,
              "pairwise_seed_ranking": 0.89,
              "predicted_best_mean_error": 1.6754932137727738,
              "seed0_mean_error": 1.7466381919384002,
              "random_seed_mean_error": 1.7389194325208663,
              "oracle_best_mean_error": 1.6701291526556015,
              "improvement_over_seed0": 0.07114497816562637,
              "gap_to_oracle": 0.0053640611171723585,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5474396021366119
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7593450643695318
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0131675733566283
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.267193189307825
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.741942658138275
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8991724967956543,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5190825995339288,
                  "rejected_mean_error": 3.7476831855773924,
                  "gap_rejected_minus_accepted": 2.2286005860434637
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.612969994544983,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2653141286355327,
                  "rejected_mean_error": 3.1687826969372197,
                  "gap_rejected_minus_accepted": 1.903468568301687
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9963791966438293,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0131675733566283,
                  "rejected_mean_error": 2.470717742919922,
                  "gap_rejected_minus_accepted": 1.4575501695632938
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6056611090898514,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7606338500595702,
                  "rejected_mean_error": 2.0697437861304144,
                  "gap_rejected_minus_accepted": 1.3091099360708442
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.883996832370758,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.519687372578515,
                  "rejected_mean_error": 3.789195566177368,
                  "gap_rejected_minus_accepted": 2.269508193598853
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6601873636245728,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2685894835441507,
                  "rejected_mean_error": 3.1656081676483154,
                  "gap_rejected_minus_accepted": 1.8970186841041647
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9957666993141174,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0065804715156554,
                  "rejected_mean_error": 2.486695912361145,
                  "gap_rejected_minus_accepted": 1.4801154408454895
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6114077270030975,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7593244001978919,
                  "rejected_mean_error": 2.0792626244499086,
                  "gap_rejected_minus_accepted": 1.3199382242520166
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9357627584734882,
              "spearman": 0.896349690681229,
              "auroc_top30_bad": 0.9482385811467444,
              "mae": 0.38710852552345304,
              "mse": 0.20544972770034575,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.37857142857142856,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6307499341344028,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2290635425065245
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3068372046947479
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4874972481387002
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8509737354233151
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1175981296811786
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.8933932213001219,
              "spearman": 0.81191630420237,
              "auroc_top30_worst": 0.8621088435374149,
              "pairwise_seed_ranking": 0.8835714285714286,
              "predicted_best_mean_error": 1.5580593769039426,
              "seed0_mean_error": 1.636711407985006,
              "random_seed_mean_error": 1.6086368956736157,
              "oracle_best_mean_error": 1.5554576026541846,
              "improvement_over_seed0": 0.07865203108106344,
              "gap_to_oracle": 0.0026017742497579377,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0357961603573391
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.188954301902226
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3751726904937198
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4775493518511453
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.611691865154675
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6186082243919373,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.5232645860740117,
                  "rejected_mean_error": 2.407537376880646,
                  "gap_rejected_minus_accepted": 0.8842727908066341
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3811104893684387,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.4775493518511453,
                  "rejected_mean_error": 2.014119405065264,
                  "gap_rejected_minus_accepted": 0.5365700532141187
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2309537529945374,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.3751726904937198,
                  "rejected_mean_error": 1.8482110398156302,
                  "gap_rejected_minus_accepted": 0.47303834932191036
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9979881048202515,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.188954301902226,
                  "rejected_mean_error": 1.7526043862388248,
                  "gap_rejected_minus_accepted": 0.5636500843365988
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.653685820102692,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.5403318419342948,
                  "rejected_mean_error": 2.5041275024414062,
                  "gap_rejected_minus_accepted": 0.9637956605071114
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4082725048065186,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.4923721398626055,
                  "rejected_mean_error": 2.0697292123522075,
                  "gap_rejected_minus_accepted": 0.577357072489602
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2571419477462769,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.398431771993637,
                  "rejected_mean_error": 1.874991043976375,
                  "gap_rejected_minus_accepted": 0.47655927198273806
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9996470063924789,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.1998078942298889,
                  "rejected_mean_error": 1.7823459125700452,
                  "gap_rejected_minus_accepted": 0.5825380183401563
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
        "best_epoch": 58,
        "best_calib_loss": 0.06193377077579498,
        "train_time_sec": 10.741392612457275,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9789250855730883,
              "spearman": 0.9549475780834361,
              "auroc_top30_bad": 0.9994560952380952,
              "mae": 0.08498737066709436,
              "mse": 0.026141922000628953,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.513,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6946848251844546,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.14855492632603273
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2194394759265706
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.35694685391290115
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6975679963595545
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.045240304220235
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9978268591352648,
              "spearman": 0.9981445195576026,
              "auroc_top30_worst": 0.9995209523809524,
              "pairwise_seed_ranking": 0.8652,
              "predicted_best_mean_error": 1.4347459546625614,
              "seed0_mean_error": 1.5048673850893974,
              "random_seed_mean_error": 1.491976180613041,
              "oracle_best_mean_error": 1.430465862095356,
              "improvement_over_seed0": 0.07012143042683605,
              "gap_to_oracle": 0.004280092567205296,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5551347511410714
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7604859325170517
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0143274375796318
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2317353696107864
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4916307791888714
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2795821905136116,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3706347314185567,
                  "rejected_mean_error": 2.580595209121704,
                  "gap_rejected_minus_accepted": 1.2099604777031474
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9033794701099396,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2317353696107864,
                  "rejected_mean_error": 2.2713170079231264,
                  "gap_rejected_minus_accepted": 1.03958163831234
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.478274166584015,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0143274375796318,
                  "rejected_mean_error": 1.968934120798111,
                  "gap_rejected_minus_accepted": 0.9546066832184792
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0517570972442627,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7604859325170517,
                  "rejected_mean_error": 1.735345728079478,
                  "gap_rejected_minus_accepted": 0.9748597955624263
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3125493049621584,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.38057230439451,
                  "rejected_mean_error": 2.623523111343384,
                  "gap_rejected_minus_accepted": 1.242950806948874
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9302668869495392,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2396379937330881,
                  "rejected_mean_error": 2.300555559158325,
                  "gap_rejected_minus_accepted": 1.060917565425237
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.499226450920105,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.019084432721138,
                  "rejected_mean_error": 1.990650337457657,
                  "gap_rejected_minus_accepted": 0.971565904736519
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0592701137065887,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7625866343975067,
                  "rejected_mean_error": 1.7522943019866943,
                  "gap_rejected_minus_accepted": 0.9897076675891876
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8922663657905179,
              "spearman": 0.8582207787048687,
              "auroc_top30_bad": 0.9334704761904762,
              "mae": 0.3477892524689436,
              "mse": 0.21471073949654432,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.73173489145135,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3694597134590149
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4160406324863434
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6158692594170571
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.004043193046252
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3575492349803449
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.784699409700964,
              "spearman": 0.761790823546127,
              "auroc_top30_worst": 0.8818072380952381,
              "pairwise_seed_ranking": 0.7724,
              "predicted_best_mean_error": 1.9274504014253617,
              "seed0_mean_error": 2.00393310713768,
              "random_seed_mean_error": 1.984880185008049,
              "oracle_best_mean_error": 1.9105618946552276,
              "improvement_over_seed0": 0.0764827057123183,
              "gap_to_oracle": 0.016888506770134093,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0394034700393677
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.3150585356813211
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.548433663749695
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7713532601592383
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9870045333862305
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.412350797653198,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8813738627963597,
                  "rejected_mean_error": 2.937680568695068,
                  "gap_rejected_minus_accepted": 1.0563067058987086
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1217604875564575,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7706844459348452,
                  "rejected_mean_error": 2.634582558759866,
                  "gap_rejected_minus_accepted": 0.8638981128250207
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7303174138069153,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.548433663749695,
                  "rejected_mean_error": 2.425575403022766,
                  "gap_rejected_minus_accepted": 0.8771417392730712
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2716801166534424,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.315076776015492,
                  "rejected_mean_error": 2.2114585227747483,
                  "gap_rejected_minus_accepted": 0.8963817467592563
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4258570671081543,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.9000843119621278,
                  "rejected_mean_error": 2.9385722637176515,
                  "gap_rejected_minus_accepted": 1.0384879517555237
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1343953013420105,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7793047998678237,
                  "rejected_mean_error": 2.670686971573603,
                  "gap_rejected_minus_accepted": 0.891382171705779
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.740259051322937,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5605262179374695,
                  "rejected_mean_error": 2.447339996337891,
                  "gap_rejected_minus_accepted": 0.8868137784004213
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2725286781787872,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.311059398310525,
                  "rejected_mean_error": 2.2373611480794486,
                  "gap_rejected_minus_accepted": 0.9263017497689237
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.7815472964233148,
              "spearman": 0.817258878089033,
              "auroc_top30_bad": 0.9665516190476191,
              "mae": 0.4342441069036722,
              "mse": 0.44663373091030717,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.665268821116642,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.44286035019159314
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.42703920469284057
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5278372843146324
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8880211709976197
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2602940951883792
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6769530717741168,
              "spearman": 0.7796695309244999,
              "auroc_top30_worst": 0.863768380952381,
              "pairwise_seed_ranking": 0.7816,
              "predicted_best_mean_error": 1.7272832005023957,
              "seed0_mean_error": 1.7883586795330049,
              "random_seed_mean_error": 1.7806851657629013,
              "oracle_best_mean_error": 1.7118634194135667,
              "improvement_over_seed0": 0.06107547903060917,
              "gap_to_oracle": 0.015419781088829021,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.621098892211914
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8232103664523516
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2046937044143677
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4825127635683333
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7837100900650025
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2891559839248665,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6550077391730416,
                  "rejected_mean_error": 2.9420312480926514,
                  "gap_rejected_minus_accepted": 1.2870235089196098
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9859227538108826,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4805573267005423,
                  "rejected_mean_error": 2.6912313017982266,
                  "gap_rejected_minus_accepted": 1.2106739750976843
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4959315657615662,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2046937044143677,
                  "rejected_mean_error": 2.362726475715637,
                  "gap_rejected_minus_accepted": 1.1580327713012692
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9789987206459045,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8240028983487869,
                  "rejected_mean_error": 2.104295309923247,
                  "gap_rejected_minus_accepted": 1.28029241157446
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3233925104141235,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6579774488343133,
                  "rejected_mean_error": 2.961789755821228,
                  "gap_rejected_minus_accepted": 1.3038123069869145
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0098723769187927,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4845059086932217,
                  "rejected_mean_error": 2.690270872343154,
                  "gap_rejected_minus_accepted": 1.2057649636499324
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4791457056999207,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1980466084480286,
                  "rejected_mean_error": 2.378670750617981,
                  "gap_rejected_minus_accepted": 1.1806241421699526
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9779115319252014,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.819737660506415,
                  "rejected_mean_error": 2.114685546905599,
                  "gap_rejected_minus_accepted": 1.2949478863991843
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.8434932952313371,
              "spearman": 0.8241640532251094,
              "auroc_top30_bad": 0.904458211856171,
              "mae": 0.33245025387832094,
              "mse": 0.19421710708699602,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.5071428571428571,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6427855961955521,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3808910608291626
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3981529928105218
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.633235526319061
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9478710558868589
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1938488221168517
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.6249989680056856,
              "spearman": 0.5067362294908473,
              "auroc_top30_worst": 0.7349854227405248,
              "pairwise_seed_ranking": 0.7607142857142857,
              "predicted_best_mean_error": 1.648757576090949,
              "seed0_mean_error": 1.7152731818812235,
              "random_seed_mean_error": 1.6871695714337485,
              "oracle_best_mean_error": 1.6339827316147941,
              "improvement_over_seed0": 0.06651560579027449,
              "gap_to_oracle": 0.014774844476154847,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3871601351669856
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4839340315546308
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.5209198944909232
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5900216295605614
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6901565422330584
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2494107484817514,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6154528977378966,
                  "rejected_mean_error": 2.362489342689514,
                  "gap_rejected_minus_accepted": 0.7470364449516176
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7397926449775696,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5900216295605614,
                  "rejected_mean_error": 1.9905612802505492,
                  "gap_rejected_minus_accepted": 0.40053965068998787
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.370923638343811,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.5209198944909232,
                  "rejected_mean_error": 1.8593931899751936,
                  "gap_rejected_minus_accepted": 0.3384732954842704
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9915495365858078,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.4839340315546308,
                  "rejected_mean_error": 1.7588973791258675,
                  "gap_rejected_minus_accepted": 0.27496334757123675
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.384307336807252,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.634055271035149,
                  "rejected_mean_error": 2.4462343794958934,
                  "gap_rejected_minus_accepted": 0.8121791084607444
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7808682024478912,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.6000988188244047,
                  "rejected_mean_error": 2.060796271051679,
                  "gap_rejected_minus_accepted": 0.46069745222727443
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3781085014343262,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.532537909916469,
                  "rejected_mean_error": 1.8980084538459778,
                  "gap_rejected_minus_accepted": 0.36547054392950873
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0074808597564697,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.490287869317191,
                  "rejected_mean_error": 1.7902682860692343,
                  "gap_rejected_minus_accepted": 0.29998041675204323
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
        "best_epoch": 68,
        "best_calib_loss": 0.022921709343791008,
        "train_time_sec": 35.15462779998779,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995311824173815,
              "spearman": 0.9981312588208671,
              "auroc_top30_bad": 0.9998673333333333,
              "mae": 0.03299612955362536,
              "mse": 0.0015920005233604965,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.989,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7214869368374145,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.047281428438844156
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.11524161557164044
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3534598109613173
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6972831871993219
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.045240304220235
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9996085457020694,
              "spearman": 0.9996894399875479,
              "auroc_top30_worst": 0.9998811428571429,
              "pairwise_seed_ranking": 0.9388,
              "predicted_best_mean_error": 1.4314962183535098,
              "seed0_mean_error": 1.5048673850893974,
              "random_seed_mean_error": 1.491976180613041,
              "oracle_best_mean_error": 1.430465862095356,
              "improvement_over_seed0": 0.07337116673588762,
              "gap_to_oracle": 0.0010303562581537307,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5536911523938179
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7594701811552048
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0135573865771295
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2314844186385472
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4916307791888714
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3213207960128788,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3702723119722473,
                  "rejected_mean_error": 2.583856984138489,
                  "gap_rejected_minus_accepted": 1.2135846721662416
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9350464642047882,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2314844186385472,
                  "rejected_mean_error": 2.272069860839844,
                  "gap_rejected_minus_accepted": 1.0405854422012968
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.532271385192871,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0135573865771295,
                  "rejected_mean_error": 1.9697041718006134,
                  "gap_rejected_minus_accepted": 0.956146785223484
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1169061362743378,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7594701811552048,
                  "rejected_mean_error": 1.7356843118667602,
                  "gap_rejected_minus_accepted": 0.9762141307115554
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3659741640090943,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3805053153965208,
                  "rejected_mean_error": 2.624126012325287,
                  "gap_rejected_minus_accepted": 1.2436206969287662
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9526599049568176,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2393616457780203,
                  "rejected_mean_error": 2.301384603023529,
                  "gap_rejected_minus_accepted": 1.0620229572455087
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5400946736335754,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0187382000684737,
                  "rejected_mean_error": 1.990996570110321,
                  "gap_rejected_minus_accepted": 0.9722583700418472
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1184237599372864,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7612003481388092,
                  "rejected_mean_error": 1.75275639740626,
                  "gap_rejected_minus_accepted": 0.9915560492674509
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9711759961657115,
              "spearman": 0.9607577947415249,
              "auroc_top30_bad": 0.9783078095238095,
              "mae": 0.17058137823194267,
              "mse": 0.060125179827425754,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.928,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8120335956253019,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1789018852710724
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.26738757137060165
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5482597979903221
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9716017556111017
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3575492349803449
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9415681886604462,
              "spearman": 0.9327680818995725,
              "auroc_top30_worst": 0.9574064761904761,
              "pairwise_seed_ranking": 0.912,
              "predicted_best_mean_error": 1.9118865250349044,
              "seed0_mean_error": 2.00393310713768,
              "random_seed_mean_error": 1.984880185008049,
              "oracle_best_mean_error": 1.9105618946552276,
              "improvement_over_seed0": 0.09204658210277561,
              "gap_to_oracle": 0.0013246303796767833,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8427104110717774
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1189391949237921
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.466755584526062
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.7293310472960157
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9870045333862305
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.57630250453949,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8618906256357828,
                  "rejected_mean_error": 3.113029703140259,
                  "gap_rejected_minus_accepted": 1.2511390775044762
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.336755871772766,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7279597440676857,
                  "rejected_mean_error": 2.7624836630714587,
                  "gap_rejected_minus_accepted": 1.034523919003773
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.947722315788269,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.466755584526062,
                  "rejected_mean_error": 2.5072534822463988,
                  "gap_rejected_minus_accepted": 1.0404978977203367
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4152037799358368,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.120178175810427,
                  "rejected_mean_error": 2.276563391359791,
                  "gap_rejected_minus_accepted": 1.1563852155493641
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6276461839675904,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8732338404655458,
                  "rejected_mean_error": 3.1802265071868896,
                  "gap_rejected_minus_accepted": 1.3069926667213438
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3698941469192505,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7425629222456784,
                  "rejected_mean_error": 2.7797461956266374,
                  "gap_rejected_minus_accepted": 1.037183273380959
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9562362432479858,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4769588770866393,
                  "rejected_mean_error": 2.5309073371887205,
                  "gap_rejected_minus_accepted": 1.0539484601020812
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4113121628761292,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1340754287583488,
                  "rejected_mean_error": 2.296986763490075,
                  "gap_rejected_minus_accepted": 1.1629113347317264
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9360350846937582,
              "spearman": 0.950147645814475,
              "auroc_top30_bad": 0.9981173333333333,
              "mae": 0.2338042788386345,
              "mse": 0.15838826219038837,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.720731292523591,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.27547011864185333
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.27755289030075075
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4821260938286781
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.78906742319266
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2602940951883792
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9344716145131265,
              "spearman": 0.9856914135625048,
              "auroc_top30_worst": 0.9954651428571428,
              "pairwise_seed_ranking": 0.894,
              "predicted_best_mean_error": 1.7159104281663895,
              "seed0_mean_error": 1.7883586795330049,
              "random_seed_mean_error": 1.7806851657629013,
              "oracle_best_mean_error": 1.7118634194135667,
              "improvement_over_seed0": 0.07244825136661537,
              "gap_to_oracle": 0.004047008752822823,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5175788087844848
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7513577534984319
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0085657991409303
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2611354672069996
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7837100900650025
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5278537750244143,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5681244854397245,
                  "rejected_mean_error": 3.7239805316925048,
                  "gap_rejected_minus_accepted": 2.1558560462527803
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1597211360931396,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2600385047328384,
                  "rejected_mean_error": 3.3513787017462735,
                  "gap_rejected_minus_accepted": 2.091340197013435
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5474359393119812,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0085657991409303,
                  "rejected_mean_error": 2.5588543809890747,
                  "gap_rejected_minus_accepted": 1.5502885818481444
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1243723332881927,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7525934062826748,
                  "rejected_mean_error": 2.128149281125695,
                  "gap_rejected_minus_accepted": 1.37555587484302
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.514693808555603,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5723743033409119,
                  "rejected_mean_error": 3.732218065261841,
                  "gap_rejected_minus_accepted": 2.159843761920929
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.186969220638275,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2620539241296085,
                  "rejected_mean_error": 3.35056485827007,
                  "gap_rejected_minus_accepted": 2.0885109341404613
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.52713280916214,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.003007704257965,
                  "rejected_mean_error": 2.5737096548080443,
                  "gap_rejected_minus_accepted": 1.5707019505500792
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1145541965961456,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.752414726075672,
                  "rejected_mean_error": 2.137366535510609,
                  "gap_rejected_minus_accepted": 1.384951809434937
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9718800126913749,
              "spearman": 0.9535358515572027,
              "auroc_top30_bad": 0.9811103012633625,
              "mae": 0.1376076143580888,
              "mse": 0.03513651288276125,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.8928571428571429,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7422380057399423,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.25631111892206326
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2773479610681534
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5561020650182451
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9166950909296672
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1938488221168517
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9539724134254521,
              "spearman": 0.9386393616546739,
              "auroc_top30_worst": 0.9515451895043732,
              "pairwise_seed_ranking": 0.8785714285714286,
              "predicted_best_mean_error": 1.6374978389058794,
              "seed0_mean_error": 1.7152731818812235,
              "random_seed_mean_error": 1.6871695714337485,
              "oracle_best_mean_error": 1.6339827316147941,
              "improvement_over_seed0": 0.07777534297534405,
              "gap_to_oracle": 0.0035151072910852843,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0345180409295218
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2540766177858624
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4287679253305707
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.540049046107701
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6901565422330584
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0958414077758794,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6100656168801444,
                  "rejected_mean_error": 2.410974870409284,
                  "gap_rejected_minus_accepted": 0.8009092535291398
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9309073090553284,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.540049046107701,
                  "rejected_mean_error": 2.140479030609131,
                  "gap_rejected_minus_accepted": 0.6004299845014298
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7592413425445557,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4287679253305707,
                  "rejected_mean_error": 1.951545159135546,
                  "gap_rejected_minus_accepted": 0.5227772338049752
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5126257240772247,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2540766177858624,
                  "rejected_mean_error": 1.8355165170487904,
                  "gap_rejected_minus_accepted": 0.5814398992629279
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1057650804519663,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.626610931896028,
                  "rejected_mean_error": 2.5132334317479814,
                  "gap_rejected_minus_accepted": 0.8866224998519534
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9491782486438751,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5627978983379545,
                  "rejected_mean_error": 2.17269903251103,
                  "gap_rejected_minus_accepted": 0.6099011341730756
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.764323115348816,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4518014141491482,
                  "rejected_mean_error": 1.9787449496132987,
                  "gap_rejected_minus_accepted": 0.5269435354641505
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5324169993400574,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.2669832910810197,
                  "rejected_mean_error": 1.8647031454812912,
                  "gap_rejected_minus_accepted": 0.5977198544002715
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
        "best_epoch": 65,
        "best_calib_loss": 0.02129068598151207,
        "train_time_sec": 41.29413843154907,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9991457468227801,
              "spearman": 0.997398702847438,
              "auroc_top30_bad": 0.9996587142857143,
              "mae": 0.04941903896299191,
              "mse": 0.0040426330476221175,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7395167266410093,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.047673677453072744
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.115949413128756
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.35360249279839917
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6974869257615879
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.045240304220235
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9988264372369792,
              "spearman": 0.9987631168463466,
              "auroc_top30_worst": 0.999651238095238,
              "pairwise_seed_ranking": 0.9559,
              "predicted_best_mean_error": 1.4312747594714166,
              "seed0_mean_error": 1.5048673850893974,
              "random_seed_mean_error": 1.491976180613041,
              "oracle_best_mean_error": 1.430465862095356,
              "improvement_over_seed0": 0.07359262561798086,
              "gap_to_oracle": 0.0008088973760604912,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5546883227229118
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7600309900999069
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0140897953867913
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2317096272706984
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4916307791888714
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3792223930358887,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.370328842818737,
                  "rejected_mean_error": 2.5833482065200806,
                  "gap_rejected_minus_accepted": 1.2130193637013436
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.967092514038086,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2317096272706984,
                  "rejected_mean_error": 2.27139423494339,
                  "gap_rejected_minus_accepted": 1.0396846076726916
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5252041816711426,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0140897953867913,
                  "rejected_mean_error": 1.9691717629909515,
                  "gap_rejected_minus_accepted": 0.9550819676041602
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.097333550453186,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7600309900999069,
                  "rejected_mean_error": 1.7354973755518595,
                  "gap_rejected_minus_accepted": 0.9754663854519525
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4031418323516847,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3804714610179265,
                  "rejected_mean_error": 2.6244307017326354,
                  "gap_rejected_minus_accepted": 1.2439592407147089
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9957275390625,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2397835234800973,
                  "rejected_mean_error": 2.3001189699172975,
                  "gap_rejected_minus_accepted": 1.0603354464372001
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5351025462150574,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.019340349316597,
                  "rejected_mean_error": 1.990394420862198,
                  "gap_rejected_minus_accepted": 0.9710540715456011
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0964871644973755,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7620409905910492,
                  "rejected_mean_error": 1.7524761832555136,
                  "gap_rejected_minus_accepted": 0.9904351926644643
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9740866220834368,
              "spearman": 0.9586380549706124,
              "auroc_top30_bad": 0.9800662857142858,
              "mae": 0.16815660397559404,
              "mse": 0.052058937872108746,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.936,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8385296001451115,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.20255005806684495
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.28420719454288484
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5495156318068505
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9697793553908666
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3575492349803449
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9585599606388405,
              "spearman": 0.9519858442149404,
              "auroc_top30_worst": 0.9734460952380953,
              "pairwise_seed_ranking": 0.926,
              "predicted_best_mean_error": 1.911745864391327,
              "seed0_mean_error": 2.00393310713768,
              "random_seed_mean_error": 1.984880185008049,
              "oracle_best_mean_error": 1.9105618946552276,
              "improvement_over_seed0": 0.09218724274635304,
              "gap_to_oracle": 0.001183969736099355,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8536012182235718
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1145604650179546
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4611375289916992
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.710699980447033
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9870045333862305
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7145380973815927,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.859602283053928,
                  "rejected_mean_error": 3.133624786376953,
                  "gap_rejected_minus_accepted": 1.274022503323025
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4059616327285767,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7100916270130853,
                  "rejected_mean_error": 2.8159738409633452,
                  "gap_rejected_minus_accepted": 1.10588221395026
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9943401217460632,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4611375289916992,
                  "rejected_mean_error": 2.5128715377807618,
                  "gap_rejected_minus_accepted": 1.0517340087890625
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3707244396209717,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1160541117762606,
                  "rejected_mean_error": 2.277941013603862,
                  "gap_rejected_minus_accepted": 1.1618869018276012
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7616896867752074,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8732338404655458,
                  "rejected_mean_error": 3.1802265071868896,
                  "gap_rejected_minus_accepted": 1.3069926667213438
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.423425257205963,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7224818598777853,
                  "rejected_mean_error": 2.8393518886868914,
                  "gap_rejected_minus_accepted": 1.116870028809106
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 2.020062565803528,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4687515664100648,
                  "rejected_mean_error": 2.5391146478652953,
                  "gap_rejected_minus_accepted": 1.0703630814552305
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3535650074481964,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1355812559052119,
                  "rejected_mean_error": 2.2964794527400625,
                  "gap_rejected_minus_accepted": 1.1608981968348506
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9567136131298937,
              "spearman": 0.9492166943886139,
              "auroc_top30_bad": 0.9988921904761905,
              "mae": 0.1996887066557072,
              "mse": 0.10536348210327999,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.904,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7397482696104165,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.27676857805252075
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.28385340528488157
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4861908432602882
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7860544977267583
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2602940951883792
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9638950294921405,
              "spearman": 0.990715089097657,
              "auroc_top30_worst": 0.999384380952381,
              "pairwise_seed_ranking": 0.9172,
              "predicted_best_mean_error": 1.7146816217899323,
              "seed0_mean_error": 1.7883586795330049,
              "random_seed_mean_error": 1.7806851657629013,
              "oracle_best_mean_error": 1.7118634194135667,
              "improvement_over_seed0": 0.07367705774307254,
              "gap_to_oracle": 0.0028182023763656527,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5079760565757752
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7532609028693957
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0070587501525878
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2578961861921525
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7837100900650025
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7912994146347048,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5562650464375813,
                  "rejected_mean_error": 3.830715482711792,
                  "gap_rejected_minus_accepted": 2.2744504362742104
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3089513182640076,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2568179617060413,
                  "rejected_mean_error": 3.361019752276972,
                  "gap_rejected_minus_accepted": 2.1042017905709307
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4261848330497742,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0070587501525878,
                  "rejected_mean_error": 2.560361429977417,
                  "gap_rejected_minus_accepted": 1.5533026798248293
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.040835201740265,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7542289423104673,
                  "rejected_mean_error": 2.1276029387812985,
                  "gap_rejected_minus_accepted": 1.3733739964708311
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.770175004005432,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5531366737683614,
                  "rejected_mean_error": 3.905356731414795,
                  "gap_rejected_minus_accepted": 2.3522200576464334
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3786025047302246,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2555268394118324,
                  "rejected_mean_error": 3.3699389033847384,
                  "gap_rejected_minus_accepted": 2.114412063972906
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4147316217422485,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0024877095222473,
                  "rejected_mean_error": 2.574229649543762,
                  "gap_rejected_minus_accepted": 1.571741940021515
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.038116842508316,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7532178844724383,
                  "rejected_mean_error": 2.1370959527352276,
                  "gap_rejected_minus_accepted": 1.3838780682627894
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.974516546983252,
              "spearman": 0.9638109093446521,
              "auroc_top30_bad": 0.9909232264334306,
              "mae": 0.12737508690916002,
              "mse": 0.03227628744110235,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.8785714285714286,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7409706008848693,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.21907467107687678
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2667369947263173
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5553105475221362
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9145012869153704
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1938488221168517
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9724644743073292,
              "spearman": 0.9684214282653053,
              "auroc_top30_worst": 0.9741107871720117,
              "pairwise_seed_ranking": 0.8964285714285715,
              "predicted_best_mean_error": 1.6363541075161525,
              "seed0_mean_error": 1.7152731818812235,
              "random_seed_mean_error": 1.6871695714337485,
              "oracle_best_mean_error": 1.6339827316147941,
              "improvement_over_seed0": 0.07891907436507095,
              "gap_to_oracle": 0.0023713759013583857,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0371250186647687
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2484141887937272
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.41864791563579
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5367113715126401
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6901565422330584
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.095329189300537,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6080445174186948,
                  "rejected_mean_error": 2.42916476556233,
                  "gap_rejected_minus_accepted": 0.8211202481436353
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9314005672931671,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5367113715126401,
                  "rejected_mean_error": 2.1504920543943133,
                  "gap_rejected_minus_accepted": 0.6137806828816732
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7222958207130432,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.41864791563579,
                  "rejected_mean_error": 1.9616651688303266,
                  "gap_rejected_minus_accepted": 0.5430172531945365
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4517046809196472,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2484141887937272,
                  "rejected_mean_error": 1.837403993379502,
                  "gap_rejected_minus_accepted": 0.5889898045857749
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.074510669708252,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.6276227018189808,
                  "rejected_mean_error": 2.5041275024414062,
                  "gap_rejected_minus_accepted": 0.8765048006224254
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9583018124103546,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5587841170174734,
                  "rejected_mean_error": 2.1847403764724733,
                  "gap_rejected_minus_accepted": 0.6259562594549999
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7310676574707031,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.4385972448757716,
                  "rejected_mean_error": 1.9919491188866751,
                  "gap_rejected_minus_accepted": 0.5533518740109036
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4698911309242249,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.2645869084766932,
                  "rejected_mean_error": 1.8655019396827335,
                  "gap_rejected_minus_accepted": 0.6009150312060403
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
        "best_epoch": 79,
        "best_calib_loss": 0.02479643188416958,
        "train_time_sec": 29.223994970321655,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995235311933597,
              "spearman": 0.99700753743985,
              "auroc_top30_bad": 0.9998399761904762,
              "mae": 0.026509741051169114,
              "mse": 0.0012127428772181546,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.997,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7190911131006033,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.052444345922442154
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.11496223949398846
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3534125508199446
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6972794417070225
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.045240304220235
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9995568560766145,
              "spearman": 0.9995333568212784,
              "auroc_top30_worst": 0.9997780952380952,
              "pairwise_seed_ranking": 0.9571,
              "predicted_best_mean_error": 1.4308704060316086,
              "seed0_mean_error": 1.5048673850893974,
              "random_seed_mean_error": 1.491976180613041,
              "oracle_best_mean_error": 1.430465862095356,
              "improvement_over_seed0": 0.07399697905778879,
              "gap_to_oracle": 0.0004045439362525549,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5537572624087334
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7594981312513351
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.013702879178524
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.231468794941902
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4916307791888714
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3220369815826416,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.370322384165393,
                  "rejected_mean_error": 2.583406334400177,
                  "gap_rejected_minus_accepted": 1.2130839502347839
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9238701164722443,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.231468794941902,
                  "rejected_mean_error": 2.272116731929779,
                  "gap_rejected_minus_accepted": 1.040647936987877
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5017927885055542,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.013702879178524,
                  "rejected_mean_error": 1.9695586791992188,
                  "gap_rejected_minus_accepted": 0.9558558000206947
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0827946066856384,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7594981312513351,
                  "rejected_mean_error": 1.7356749951680501,
                  "gap_rejected_minus_accepted": 0.976176863916715
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.353645181655884,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3804580004347695,
                  "rejected_mean_error": 2.6245518469810487,
                  "gap_rejected_minus_accepted": 1.2440938465462792
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.949087768793106,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2393506888548533,
                  "rejected_mean_error": 2.30141747379303,
                  "gap_rejected_minus_accepted": 1.0620667849381766
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.515666902065277,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0190034381151198,
                  "rejected_mean_error": 1.990731332063675,
                  "gap_rejected_minus_accepted": 0.9717278939485552
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.081375002861023,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7612650492191315,
                  "rejected_mean_error": 1.752734830379486,
                  "gap_rejected_minus_accepted": 0.9914697811603546
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9734796649011072,
              "spearman": 0.9623802056404241,
              "auroc_top30_bad": 0.9776380952380953,
              "mae": 0.18267338014021517,
              "mse": 0.0632956990182375,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7945300158830939,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15585502499341966
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.26785066026449206
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5495995067954064
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.973158288025856
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3575492349803449
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9503949635891911,
              "spearman": 0.9395276105776709,
              "auroc_top30_worst": 0.9614902857142857,
              "pairwise_seed_ranking": 0.9224,
              "predicted_best_mean_error": 1.911479249715805,
              "seed0_mean_error": 2.00393310713768,
              "random_seed_mean_error": 1.984880185008049,
              "oracle_best_mean_error": 1.9105618946552276,
              "improvement_over_seed0": 0.09245385742187495,
              "gap_to_oracle": 0.0009173550605774405,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8485810346603394
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1163504872566614
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4703112768173219
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.714909569032665
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9870045333862305
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.537749147415163,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8617834748162163,
                  "rejected_mean_error": 3.1139940605163576,
                  "gap_rejected_minus_accepted": 1.2522105857001413
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3100693225860596,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.714130840026709,
                  "rejected_mean_error": 2.8038820115902934,
                  "gap_rejected_minus_accepted": 1.0897511715635844
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8883274793624878,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4703112768173219,
                  "rejected_mean_error": 2.5036977899551394,
                  "gap_rejected_minus_accepted": 1.0333865131378175
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3012939095497131,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1175503129014572,
                  "rejected_mean_error": 2.2774412153624675,
                  "gap_rejected_minus_accepted": 1.1598909024610102
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.590790486335754,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8747759339544507,
                  "rejected_mean_error": 3.166347665786743,
                  "gap_rejected_minus_accepted": 1.2915717318322923
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.337082028388977,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.7270622301229182,
                  "rejected_mean_error": 2.8257561865307035,
                  "gap_rejected_minus_accepted": 1.0986939564077853
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9203792810440063,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4778035550117492,
                  "rejected_mean_error": 2.530062659263611,
                  "gap_rejected_minus_accepted": 1.0522591042518616
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3159256279468536,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1375529151114205,
                  "rejected_mean_error": 2.2958152039165802,
                  "gap_rejected_minus_accepted": 1.1582622888051597
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9569349652975976,
              "spearman": 0.9559712705638953,
              "auroc_top30_bad": 0.9985196190476191,
              "mae": 0.19606696464344858,
              "mse": 0.11832029282227202,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.948,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.7088055683046491,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.20541974478960037
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2821514620542526
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4880926156878471
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7858143140872319
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2602940951883792
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9637572995570581,
              "spearman": 0.9903707422532751,
              "auroc_top30_worst": 0.9996952380952381,
              "pairwise_seed_ranking": 0.924,
              "predicted_best_mean_error": 1.7145229066610337,
              "seed0_mean_error": 1.7883586795330049,
              "random_seed_mean_error": 1.7806851657629013,
              "oracle_best_mean_error": 1.7118634194135667,
              "improvement_over_seed0": 0.07383577287197118,
              "gap_to_oracle": 0.0026594872474670073,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5171521911621094
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7514211336771647
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0074025913238525
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2579438340689328
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7837100900650025
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6379671335220336,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.557934547000461,
                  "rejected_mean_error": 3.815689977645874,
                  "gap_rejected_minus_accepted": 2.257755430645413
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2295258045196533,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2568434653694374,
                  "rejected_mean_error": 3.3609434042494897,
                  "gap_rejected_minus_accepted": 2.1040999388800525
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.446351408958435,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0074025913238525,
                  "rejected_mean_error": 2.5600175888061525,
                  "gap_rejected_minus_accepted": 1.5526149974823
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0448289811611176,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7524954248160219,
                  "rejected_mean_error": 2.1281820113274685,
                  "gap_rejected_minus_accepted": 1.3756865865114465
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6183839797973634,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5568248958057826,
                  "rejected_mean_error": 3.872162733078003,
                  "gap_rejected_minus_accepted": 2.3153378372722204
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3044515252113342,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2555268394118324,
                  "rejected_mean_error": 3.3699389033847384,
                  "gap_rejected_minus_accepted": 2.114412063972906
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4377193450927734,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.002777856349945,
                  "rejected_mean_error": 2.5739395027160645,
                  "gap_rejected_minus_accepted": 1.5711616463661195
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0335703194141388,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7506219441928561,
                  "rejected_mean_error": 2.137970520850809,
                  "gap_rejected_minus_accepted": 1.3873485766579527
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 1400,
              "pearson": 0.9784508772099411,
              "spearman": 0.9677710561057717,
              "auroc_top30_bad": 0.9861856171039844,
              "mae": 0.11388992989701884,
              "mse": 0.026773419763507826,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.9214285714285714,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7404301564819858,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15638544208237104
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.25794796402965275
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5583998005730765
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9151907892454239
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1938488221168517
                }
              ]
            },
            "simvla_only": {
              "n": 700,
              "contexts": 140,
              "pearson": 0.9630135096867385,
              "spearman": 0.9500310233869281,
              "auroc_top30_worst": 0.9668513119533527,
              "pairwise_seed_ranking": 0.905,
              "predicted_best_mean_error": 1.63635305251394,
              "seed0_mean_error": 1.7152731818812235,
              "random_seed_mean_error": 1.6871695714337485,
              "oracle_best_mean_error": 1.6339827316147941,
              "improvement_over_seed0": 0.07892012936728343,
              "gap_to_oracle": 0.0023703208991459057,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0364719765526909
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.2638824939727784
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4219163806097848
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5402790394283477
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6901565422330584
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1037514448165893,
                  "accepted_n": 630,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.6067351950539484,
                  "rejected_mean_error": 2.440948666845049,
                  "gap_rejected_minus_accepted": 0.8342134717911007
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9286174178123474,
                  "accepted_n": 525,
                  "rejected_n": 175,
                  "accepted_mean_error": 1.5402790394283477,
                  "rejected_mean_error": 2.139789050647191,
                  "gap_rejected_minus_accepted": 0.5995100112188432
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7568410634994507,
                  "accepted_n": 350,
                  "rejected_n": 350,
                  "accepted_mean_error": 1.4219163806097848,
                  "rejected_mean_error": 1.958396703856332,
                  "gap_rejected_minus_accepted": 0.5364803232465472
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5015661716461182,
                  "accepted_n": 175,
                  "rejected_n": 525,
                  "accepted_mean_error": 1.2638824939727784,
                  "rejected_mean_error": 1.8322478916531517,
                  "gap_rejected_minus_accepted": 0.5683653976803733
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1037514448165893,
                  "accepted_n": 126,
                  "rejected_n": 14,
                  "accepted_mean_error": 1.625069895434001,
                  "rejected_mean_error": 2.527102759906224,
                  "gap_rejected_minus_accepted": 0.9020328644722229
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9485940635204315,
                  "accepted_n": 105,
                  "rejected_n": 35,
                  "accepted_mean_error": 1.5611604145595006,
                  "rejected_mean_error": 2.177611483846392,
                  "gap_rejected_minus_accepted": 0.6164510692868914
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7796845436096191,
                  "accepted_n": 70,
                  "rejected_n": 70,
                  "accepted_mean_error": 1.440747514792851,
                  "rejected_mean_error": 1.9897988489695957,
                  "gap_rejected_minus_accepted": 0.5490513341767447
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.5169121325016022,
                  "accepted_n": 35,
                  "rejected_n": 105,
                  "accepted_mean_error": 1.2786936351231166,
                  "rejected_mean_error": 1.860799697467259,
                  "gap_rejected_minus_accepted": 0.5821060623441423
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
