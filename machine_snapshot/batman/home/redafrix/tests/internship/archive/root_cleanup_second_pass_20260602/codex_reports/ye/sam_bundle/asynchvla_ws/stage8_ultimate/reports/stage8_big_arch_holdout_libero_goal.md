# Stage 6 Experiments: holdout_libero_goal

```json
{
  "split": "holdout_libero_goal",
  "results": [
    {
      "variant": "action_only_baseline",
      "feature_mode": "A0_action_flat",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 70,
      "best_epoch": 143,
      "best_calib_loss": 0.05894235894083977,
      "train_time_sec": 22.322622776031494,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9766080685201248,
            "spearman": 0.9425877328603045,
            "auroc_top30_bad": 0.999206,
            "mae": 0.10801814125180244,
            "mse": 0.04334380523654917,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.512,
            "expert_lt_simvla_seed0": 0.969,
            "same_context_pred_std": 0.7422800384703601,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.30239745666086676
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.31734297662973404
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4839858330875635
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8176413098673025
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
            "pearson": 0.9992624742550602,
            "spearman": 0.9986361159454445,
            "auroc_top30_worst": 0.999256761904762,
            "pairwise_seed_ranking": 0.8966,
            "predicted_best_mean_error": 1.688722225368023,
            "seed0_mean_error": 1.7593383036255836,
            "random_seed_mean_error": 1.748514448583126,
            "oracle_best_mean_error": 1.6850638110637666,
            "improvement_over_seed0": 0.07061607825756067,
            "gap_to_oracle": 0.0036584143042563966,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6097133167386055
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8476919272661209
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.110674784529209
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3370143478155136
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7487053180277348
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8466570377349854,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4976591014398468,
                "rejected_mean_error": 4.008121267318725,
                "gap_rejected_minus_accepted": 2.5104621658788786
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9841949343681335,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3370143478155136,
                "rejected_mean_error": 2.983778228664398,
                "gap_rejected_minus_accepted": 1.6467638808488845
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5911007523536682,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.110674784529209,
                "rejected_mean_error": 2.3867358515262604,
                "gap_rejected_minus_accepted": 1.2760610669970514
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1463402807712555,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8476919272661209,
                "rejected_mean_error": 2.049043114948273,
                "gap_rejected_minus_accepted": 1.2013511876821519
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8597995042800908,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.508100390235583,
                "rejected_mean_error": 4.02047952413559,
                "gap_rejected_minus_accepted": 2.5123791339000068
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.000438392162323,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.347307906548182,
                "rejected_mean_error": 2.995429494857788,
                "gap_rejected_minus_accepted": 1.648121588309606
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5952793955802917,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1170493315458299,
                "rejected_mean_error": 2.4016272757053376,
                "gap_rejected_minus_accepted": 1.2845779441595078
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1563718020915985,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8514489123821258,
                "rejected_mean_error": 2.061968100706736,
                "gap_rejected_minus_accepted": 1.2105191883246103
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8447549400951725,
            "spearman": 0.8346761597889775,
            "auroc_top30_bad": 0.9210651428571428,
            "mae": 0.3297028628706932,
            "mse": 0.21724211046045902,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.484,
            "expert_lt_simvla_seed0": 0.964,
            "same_context_pred_std": 0.6713258038148642,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.35427001368999483
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.35102030731439593
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4995632374763489
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8407161330620447
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
            "pearson": 0.6536707799070309,
            "spearman": 0.6766677933233878,
            "auroc_top30_worst": 0.8252891428571429,
            "pairwise_seed_ranking": 0.7932,
            "predicted_best_mean_error": 1.6043013107776642,
            "seed0_mean_error": 1.6905601416826248,
            "random_seed_mean_error": 1.6723020417690277,
            "oracle_best_mean_error": 1.5885274814367294,
            "improvement_over_seed0": 0.08625883090496056,
            "gap_to_oracle": 0.015773829340934853,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0548043177127837
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0556339212717154
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2734469254493714
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.448339712454566
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6684940560817718
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5323673963546756,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5995854676034715,
                "rejected_mean_error": 2.2886713523864746,
                "gap_rejected_minus_accepted": 0.689085884783003
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.975842833518982,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4470878447005435,
                "rejected_mean_error": 2.3312979540504966,
                "gap_rejected_minus_accepted": 0.884210109349953
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5163434147834778,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2734469254493714,
                "rejected_mean_error": 2.0635411867141724,
                "gap_rejected_minus_accepted": 0.790094261264801
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0397614240646362,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0546960468871145,
                "rejected_mean_error": 1.8735301039771057,
                "gap_rejected_minus_accepted": 0.8188340570899912
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.556570243835449,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6257476553652022,
                "rejected_mean_error": 2.2738725185394286,
                "gap_rejected_minus_accepted": 0.6481248631742265
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0558056831359863,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4712318196334941,
                "rejected_mean_error": 2.3415823039554415,
                "gap_rejected_minus_accepted": 0.8703504843219474
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5401731729507446,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2829078810214996,
                "rejected_mean_error": 2.09821240234375,
                "gap_rejected_minus_accepted": 0.8153045213222505
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.091058611869812,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0665622424511683,
                "rejected_mean_error": 1.900784032867554,
                "gap_rejected_minus_accepted": 0.8342217904163858
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8876448164881698,
            "spearman": 0.8555945743572881,
            "auroc_top30_bad": 0.9332815238095239,
            "mae": 0.27864426067769527,
            "mse": 0.15376924256528526,
            "expert_lt_perturb_large": 0.992,
            "expert_lt_other_task": 0.484,
            "expert_lt_simvla_seed0": 0.956,
            "same_context_pred_std": 0.6892938004726229,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3432194321453571
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3840748748421669
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5837589734256268
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9888708968758583
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
            "pearson": 0.7429743237097897,
            "spearman": 0.7292380598003584,
            "auroc_top30_worst": 0.7951177142857142,
            "pairwise_seed_ranking": 0.7964,
            "predicted_best_mean_error": 1.774801570892334,
            "seed0_mean_error": 1.8668941221237183,
            "random_seed_mean_error": 1.8321932954788207,
            "oracle_best_mean_error": 1.7580343310832978,
            "improvement_over_seed0": 0.09209255123138438,
            "gap_to_oracle": 0.01676723980903616,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0747545199394226
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3031527396195974
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.5301485246658326
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7047216360375825
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8333799670696258
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.17980968952179,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.772499491320716,
                "rejected_mean_error": 2.3813042488098146,
                "gap_rejected_minus_accepted": 0.6088047574890987
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9867943823337555,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.7037364738727965,
                "rejected_mean_error": 2.221482053732339,
                "gap_rejected_minus_accepted": 0.5177455798595425
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.730488896369934,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.5301485246658326,
                "rejected_mean_error": 2.136611409473419,
                "gap_rejected_minus_accepted": 0.6064628848075864
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3438591063022614,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.3033509368713672,
                "rejected_mean_error": 2.010433421127315,
                "gap_rejected_minus_accepted": 0.707082484255948
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1974522829055783,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7990563265482584,
                "rejected_mean_error": 2.4774342823028563,
                "gap_rejected_minus_accepted": 0.6783779557545979
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.007654845714569,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.7171500793752823,
                "rejected_mean_error": 2.3113724712341552,
                "gap_rejected_minus_accepted": 0.5942223918588729
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7624396085739136,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5399660511016846,
                "rejected_mean_error": 2.1938221931457518,
                "gap_rejected_minus_accepted": 0.6538561420440672
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4122191667556763,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.2992941311427526,
                "rejected_mean_error": 2.0581176484969848,
                "gap_rejected_minus_accepted": 0.7588235173542321
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.8770682340683853,
            "spearman": 0.8600116196406357,
            "auroc_top30_bad": 0.9253321428571428,
            "mae": 0.40154448038339613,
            "mse": 0.3383321594283357,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.495,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7419386182513441,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4961475382745266
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.4853658159971237
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7806898366212844
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.134291345189015
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
            "pearson": 0.8106683123570677,
            "spearman": 0.7204056964056965,
            "auroc_top30_worst": 0.8356809523809524,
            "pairwise_seed_ranking": 0.7705,
            "predicted_best_mean_error": 2.255670658648014,
            "seed0_mean_error": 2.3266324162483216,
            "random_seed_mean_error": 2.3179259487986563,
            "oracle_best_mean_error": 2.2414105245471,
            "improvement_over_seed0": 0.07096175760030743,
            "gap_to_oracle": 0.01426013410091409,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.695924289226532
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.769788010597229
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.82613125371933
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8799387272198995
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.3207210887670517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2658899545669557,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 2.1452633175585003,
                "rejected_mean_error": 3.8998410296440125,
                "gap_rejected_minus_accepted": 1.7545777120855122
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.280391812324524,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8799387272198995,
                "rejected_mean_error": 3.6430681734085084,
                "gap_rejected_minus_accepted": 1.763129446188609
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6938456892967224,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.82613125371933,
                "rejected_mean_error": 2.8153109238147738,
                "gap_rejected_minus_accepted": 0.9891796700954438
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2977891862392426,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.769788010597229,
                "rejected_mean_error": 2.504365448156993,
                "gap_rejected_minus_accepted": 0.7345774375597638
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2713062763214107,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 2.152312178081936,
                "rejected_mean_error": 3.8955145597457888,
                "gap_rejected_minus_accepted": 1.7432023816638527
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.303270637989044,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8876227966944377,
                "rejected_mean_error": 3.6436612749099733,
                "gap_rejected_minus_accepted": 1.7560384782155356
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7134893536567688,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.8446207201480866,
                "rejected_mean_error": 2.8086441123485564,
                "gap_rejected_minus_accepted": 0.9640233922004697
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3117264807224274,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.8161704874038695,
                "rejected_mean_error": 2.4967863925298057,
                "gap_rejected_minus_accepted": 0.6806159051259362
              }
            ]
          }
        }
      }
    },
    {
      "variant": "full_old_baseline",
      "feature_mode": "A2_full_old",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1038,
      "best_epoch": 139,
      "best_calib_loss": 0.015575692988932133,
      "train_time_sec": 27.922168016433716,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996406557838466,
            "spearman": 0.9986733899476179,
            "auroc_top30_bad": 0.9996395238095238,
            "mae": 0.023481631528276013,
            "mse": 0.000982304455026212,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7750376619307733,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.002053371459245682
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17376327041983605
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4779352417975664
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8174279449164867
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
            "pearson": 0.9996834182155653,
            "spearman": 0.9994390178335605,
            "auroc_top30_worst": 0.9997369523809524,
            "pairwise_seed_ranking": 0.9292,
            "predicted_best_mean_error": 1.6866410748362541,
            "seed0_mean_error": 1.7593383036255836,
            "random_seed_mean_error": 1.748514448583126,
            "oracle_best_mean_error": 1.6850638110637666,
            "improvement_over_seed0": 0.0726972287893295,
            "gap_to_oracle": 0.0015772637724875693,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6090286987423896
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8472189205408096
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1103679792046548
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3367551236867905
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7487053180277348
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.9055327653884886,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4976607222623295,
                "rejected_mean_error": 4.008106679916382,
                "gap_rejected_minus_accepted": 2.510445957654052
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.03285551071167,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3367551236867905,
                "rejected_mean_error": 2.984555901050568,
                "gap_rejected_minus_accepted": 1.6478007773637773
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6110207438468933,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1103679792046548,
                "rejected_mean_error": 2.3870426568508147,
                "gap_rejected_minus_accepted": 1.27667467764616
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1597403287887573,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8472189205408096,
                "rejected_mean_error": 2.0492007838567097,
                "gap_rejected_minus_accepted": 1.2019818633159
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.9140497684478768,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5080162266227934,
                "rejected_mean_error": 4.021236996650696,
                "gap_rejected_minus_accepted": 2.513220770027903
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0431381464004517,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3471124079227448,
                "rejected_mean_error": 2.9960159907341004,
                "gap_rejected_minus_accepted": 1.6489035828113556
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6251418590545654,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1170121892690659,
                "rejected_mean_error": 2.4016644179821016,
                "gap_rejected_minus_accepted": 1.2846522287130357
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1709080636501312,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8510282137393952,
                "rejected_mean_error": 2.0621083335876467,
                "gap_rejected_minus_accepted": 1.2110801198482515
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9760055817553139,
            "spearman": 0.9767666585064098,
            "auroc_top30_bad": 0.9931565714285715,
            "mae": 0.13750389712685718,
            "mse": 0.03602023942897983,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.968,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.695671236501491,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07231616246700287
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17574499773979188
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4271366684556007
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8056867297569911
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
            "pearson": 0.9508803990293162,
            "spearman": 0.9698730610387593,
            "auroc_top30_worst": 0.9764937142857142,
            "pairwise_seed_ranking": 0.9232,
            "predicted_best_mean_error": 1.5913556073904038,
            "seed0_mean_error": 1.6905601416826248,
            "random_seed_mean_error": 1.6723020417690277,
            "oracle_best_mean_error": 1.5885274814367294,
            "improvement_over_seed0": 0.09920453429222098,
            "gap_to_oracle": 0.002828125953674432,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4925780506134033
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7847915009046212
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1171096875190736
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.393610344449086
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6684940560817718
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5148567199707035,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5524548583030702,
                "rejected_mean_error": 2.7128468360900877,
                "gap_rejected_minus_accepted": 1.1603919777870175
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0443952679634094,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3926931640636195,
                "rejected_mean_error": 2.4941344261169434,
                "gap_rejected_minus_accepted": 1.1014412620533238
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6802535653114319,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1171096875190736,
                "rejected_mean_error": 2.2198784246444703,
                "gap_rejected_minus_accepted": 1.1027687371253967
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2048279941082,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7857774755063529,
                "rejected_mean_error": 1.9633609607990676,
                "gap_rejected_minus_accepted": 1.1775834852927147
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5388556718826294,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5686230904526182,
                "rejected_mean_error": 2.7879936027526857,
                "gap_rejected_minus_accepted": 1.2193705123000675
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.075189173221588,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4095809270035138,
                "rejected_mean_error": 2.52457781065078,
                "gap_rejected_minus_accepted": 1.1149968836472663
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7020803689956665,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.132272160768509,
                "rejected_mean_error": 2.248848122596741,
                "gap_rejected_minus_accepted": 1.116575961828232
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2430585622787476,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7965403497219086,
                "rejected_mean_error": 1.9917539753378395,
                "gap_rejected_minus_accepted": 1.195213625615931
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9749575335529324,
            "spearman": 0.9681118085875404,
            "auroc_top30_bad": 0.9811725714285715,
            "mae": 0.13180144558087922,
            "mse": 0.0349110053026395,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 0.992,
            "same_context_pred_std": 0.7166873278862406,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05882568481564522
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17730420957803728
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5544132241666317
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9492429015437762
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
            "pearson": 0.9445151029938109,
            "spearman": 0.944322888910649,
            "auroc_top30_worst": 0.9705691428571428,
            "pairwise_seed_ranking": 0.9068,
            "predicted_best_mean_error": 1.7642887923717498,
            "seed0_mean_error": 1.8668941221237183,
            "random_seed_mean_error": 1.8321932954788207,
            "oracle_best_mean_error": 1.7580343310832978,
            "improvement_over_seed0": 0.10260532975196845,
            "gap_to_oracle": 0.0062544612884520845,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9194234189987183
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2034360082485738
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.461943724632263
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6471031191887886
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8333799670696258
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.32584502696991,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7493636599116855,
                "rejected_mean_error": 2.589526731491089,
                "gap_rejected_minus_accepted": 0.8401630715794033
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1315248608589172,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6466640593402542,
                "rejected_mean_error": 2.392334617364902,
                "gap_rejected_minus_accepted": 0.7456705580246477
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8319793939590454,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.461943724632263,
                "rejected_mean_error": 2.2048162095069883,
                "gap_rejected_minus_accepted": 0.7428724848747252
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.467031180858612,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.204402802470393,
                "rejected_mean_error": 2.043486533259124,
                "gap_rejected_minus_accepted": 0.8390837307887311
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3849496364593508,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7729760519663493,
                "rejected_mean_error": 2.712156753540039,
                "gap_rejected_minus_accepted": 0.9391807015736897
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.194064736366272,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6629837847010975,
                "rejected_mean_error": 2.4721517903464183,
                "gap_rejected_minus_accepted": 0.8091680056453208
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8601794242858887,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4724625453948974,
                "rejected_mean_error": 2.261325698852539,
                "gap_rejected_minus_accepted": 0.7888631534576418
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4804483354091644,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.213024896288675,
                "rejected_mean_error": 2.0871816153194813,
                "gap_rejected_minus_accepted": 0.8741567190308064
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9811666268729283,
            "spearman": 0.9784514368832187,
            "auroc_top30_bad": 0.982875,
            "mae": 0.1496040183119767,
            "mse": 0.04671170397881032,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9095630909334376,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06519472658634186
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2014048635363579
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7102196844816208
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0915824244817098
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
            "pearson": 0.956585749370014,
            "spearman": 0.9518204318204321,
            "auroc_top30_worst": 0.9707619047619047,
            "pairwise_seed_ranking": 0.87,
            "predicted_best_mean_error": 2.2475582125782965,
            "seed0_mean_error": 2.3266324162483216,
            "random_seed_mean_error": 2.3179259487986563,
            "oracle_best_mean_error": 2.2414105245471,
            "improvement_over_seed0": 0.07907420367002516,
            "gap_to_oracle": 0.006147688031196363,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3337446296215056
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4995745458602905
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6702749905586243
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8745581555366515
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.3207210887670517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.12849383354187,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 2.098572965330548,
                "rejected_mean_error": 4.320054199695587,
                "gap_rejected_minus_accepted": 2.221481234365039
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3176156878471375,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8745581555366515,
                "rejected_mean_error": 3.659209888458252,
                "gap_rejected_minus_accepted": 1.7846517329216005
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9640077352523804,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6702749905586243,
                "rejected_mean_error": 2.971167186975479,
                "gap_rejected_minus_accepted": 1.3008921964168547
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6788834631443024,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4995745458602905,
                "rejected_mean_error": 2.5944366030693056,
                "gap_rejected_minus_accepted": 1.094862057209015
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.142029523849487,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 2.10287932422426,
                "rejected_mean_error": 4.3404102444648744,
                "gap_rejected_minus_accepted": 2.2375309202406144
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3014663457870483,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8856867090861003,
                "rejected_mean_error": 3.6494695377349853,
                "gap_rejected_minus_accepted": 1.763782828648885
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9731863141059875,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.680050218105316,
                "rejected_mean_error": 2.9732146143913267,
                "gap_rejected_minus_accepted": 1.2931643962860107
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.693239986896515,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.520178246498108,
                "rejected_mean_error": 2.5954504728317263,
                "gap_rejected_minus_accepted": 1.0752722263336183
              }
            ]
          }
        }
      }
    },
    {
      "variant": "context_gated_action",
      "feature_mode": "M3_gated_base",
      "model_kind": "gated",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1456,
      "best_epoch": 160,
      "best_calib_loss": 0.008475352078676224,
      "train_time_sec": 67.08747363090515,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996538035623443,
            "spearman": 0.9988384256577068,
            "auroc_top30_bad": 0.9997974761904762,
            "mae": 0.02490126029374078,
            "mse": 0.0010293684955250445,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7780843193738292,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0024436401128768923
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17380489458441734
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4778387301236391
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8173583882669608
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
            "pearson": 0.9997978706563929,
            "spearman": 0.9996060592802422,
            "auroc_top30_worst": 0.9996234285714285,
            "pairwise_seed_ranking": 0.9626,
            "predicted_best_mean_error": 1.6855437299907208,
            "seed0_mean_error": 1.7593383036255836,
            "random_seed_mean_error": 1.748514448583126,
            "oracle_best_mean_error": 1.6850638110637666,
            "improvement_over_seed0": 0.07379457363486286,
            "gap_to_oracle": 0.0004799189269542037,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6086157806515694
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8468066130876541
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1103239346146583
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3367884138822554
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7487053180277348
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8929978609085096,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4976579161286354,
                "rejected_mean_error": 4.0081319351196285,
                "gap_rejected_minus_accepted": 2.510474018990993
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.021271228790283,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3367884138822554,
                "rejected_mean_error": 2.9844560304641723,
                "gap_rejected_minus_accepted": 1.6476676165819168
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6189834475517273,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1103239346146583,
                "rejected_mean_error": 2.3870867014408113,
                "gap_rejected_minus_accepted": 1.276762766826153
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.173027515411377,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8468066130876541,
                "rejected_mean_error": 2.049338219674428,
                "gap_rejected_minus_accepted": 1.202531606586774
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8720129489898683,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5080162266227934,
                "rejected_mean_error": 4.021236996650696,
                "gap_rejected_minus_accepted": 2.513220770027903
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0339571833610535,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.347224472284317,
                "rejected_mean_error": 2.9956797976493834,
                "gap_rejected_minus_accepted": 1.6484553253650664
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6278873682022095,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1169860283136368,
                "rejected_mean_error": 2.4016905789375307,
                "gap_rejected_minus_accepted": 1.2847045506238939
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1825866997241974,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8504856221675873,
                "rejected_mean_error": 2.062289197444916,
                "gap_rejected_minus_accepted": 1.2118035752773286
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9872313820322669,
            "spearman": 0.9858962704708742,
            "auroc_top30_bad": 0.9954163809523809,
            "mae": 0.0905575682675466,
            "mse": 0.018681793845259736,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7445671182980846,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06301585733890533
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17025631170272826
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4179932561993599
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8027036977847417
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
            "pearson": 0.974185306471155,
            "spearman": 0.9854166782826743,
            "auroc_top30_worst": 0.9848106666666667,
            "pairwise_seed_ranking": 0.9448,
            "predicted_best_mean_error": 1.5890201278924942,
            "seed0_mean_error": 1.6905601416826248,
            "random_seed_mean_error": 1.6723020417690277,
            "oracle_best_mean_error": 1.5885274814367294,
            "improvement_over_seed0": 0.10154001379013056,
            "gap_to_oracle": 0.0004926464557648558,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4648612494468689
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7512672705910145
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1159564616203308
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3882654992375039
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6684940560817718
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.605153417587281,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5419772747357687,
                "rejected_mean_error": 2.8071450881958007,
                "gap_rejected_minus_accepted": 1.265167813460032
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1313416957855225,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3873677175480121,
                "rejected_mean_error": 2.5100767372515254,
                "gap_rejected_minus_accepted": 1.1227090197035132
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7184356451034546,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1159564616203308,
                "rejected_mean_error": 2.221031650543213,
                "gap_rejected_minus_accepted": 1.1050751889228823
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.151974469423294,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7523603513598823,
                "rejected_mean_error": 1.9745237781500231,
                "gap_rejected_minus_accepted": 1.2221634267901407
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6226179599761963,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5591376062234243,
                "rejected_mean_error": 2.8733629608154296,
                "gap_rejected_minus_accepted": 1.3142253545920053
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.170910358428955,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4038887446258157,
                "rejected_mean_error": 2.5414736535814075,
                "gap_rejected_minus_accepted": 1.1375849089555918
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7567787170410156,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1321322996616363,
                "rejected_mean_error": 2.2489879837036133,
                "gap_rejected_minus_accepted": 1.116855684041977
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.189341425895691,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7634222512207334,
                "rejected_mean_error": 2.002911409592246,
                "gap_rejected_minus_accepted": 1.2394891583715126
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.988949210908568,
            "spearman": 0.9858999487218024,
            "auroc_top30_bad": 0.990903619047619,
            "mae": 0.08156543671004474,
            "mse": 0.015526384453887224,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7747501598868038,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04811264917254448
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16854938911199568
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5371373009622097
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9440592508912087
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
            "pearson": 0.9687825797273928,
            "spearman": 0.9791828735890392,
            "auroc_top30_worst": 0.983384380952381,
            "pairwise_seed_ranking": 0.9368,
            "predicted_best_mean_error": 1.7597594358921052,
            "seed0_mean_error": 1.8668941221237183,
            "random_seed_mean_error": 1.8321932954788207,
            "oracle_best_mean_error": 1.7580343310832978,
            "improvement_over_seed0": 0.10713468623161315,
            "gap_to_oracle": 0.0017251048088073873,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8685509848594666
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.175048640714242
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4497196682929994
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6349537685862991
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8333799670696258
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4310784816741946,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.746744627157847,
                "rejected_mean_error": 2.613098026275635,
                "gap_rejected_minus_accepted": 0.8663533991177879
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.147680401802063,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6346573504592463,
                "rejected_mean_error": 2.4282780238233816,
                "gap_rejected_minus_accepted": 0.7936206733641353
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9150943160057068,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4497196682929994,
                "rejected_mean_error": 2.2170402658462525,
                "gap_rejected_minus_accepted": 0.7673205975532531
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.553109049797058,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1759480030391924,
                "rejected_mean_error": 2.0529917117244025,
                "gap_rejected_minus_accepted": 0.8770437086852101
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5282615423202515,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7714853307935927,
                "rejected_mean_error": 2.7255732440948486,
                "gap_rejected_minus_accepted": 0.9540879133012559
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.17622834444046,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6488300536405593,
                "rejected_mean_error": 2.5141636587324596,
                "gap_rejected_minus_accepted": 0.8653336050919003
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9476163387298584,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4648329067230224,
                "rejected_mean_error": 2.2689553375244143,
                "gap_rejected_minus_accepted": 0.8041224308013919
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5973557531833649,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.182928859241425,
                "rejected_mean_error": 2.097320921918288,
                "gap_rejected_minus_accepted": 0.9143920626768627
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9908593626932185,
            "spearman": 0.9894596550246898,
            "auroc_top30_bad": 0.9938130952380951,
            "mae": 0.09777344797854312,
            "mse": 0.024489574656168373,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.913039671964339,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04324180081486702
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20776913851499557
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7036798539161682
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0825859088102976
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
            "pearson": 0.9882495521610388,
            "spearman": 0.9903261063261065,
            "auroc_top30_worst": 0.9958761904761905,
            "pairwise_seed_ranking": 0.8935,
            "predicted_best_mean_error": 2.2430624690651895,
            "seed0_mean_error": 2.3266324162483216,
            "random_seed_mean_error": 2.3179259487986563,
            "oracle_best_mean_error": 2.2414105245471,
            "improvement_over_seed0": 0.08356994718313215,
            "gap_to_oracle": 0.0016519445180893655,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2941986417770386
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4810047192573548
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6558046007156373
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8609907857577006
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.3207210887670517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.9230276584625243,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 2.0958699802557628,
                "rejected_mean_error": 4.344381065368652,
                "gap_rejected_minus_accepted": 2.2485110851128893
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.594610810279846,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8609907857577006,
                "rejected_mean_error": 3.699911997795105,
                "gap_rejected_minus_accepted": 1.8389212120374043
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.044469475746155,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6558046007156373,
                "rejected_mean_error": 2.985637576818466,
                "gap_rejected_minus_accepted": 1.3298329761028287
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7083081007003784,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4810047192573548,
                "rejected_mean_error": 2.600626545270284,
                "gap_rejected_minus_accepted": 1.1196218260129294
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.928144001960754,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 2.1037791278627185,
                "rejected_mean_error": 4.33231201171875,
                "gap_rejected_minus_accepted": 2.228532883856032
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.5871971249580383,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8688580735524496,
                "rejected_mean_error": 3.6999554443359375,
                "gap_rejected_minus_accepted": 1.8310973707834879
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.045799136161804,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6730096471309661,
                "rejected_mean_error": 2.9802551853656767,
                "gap_rejected_minus_accepted": 1.3072455382347106
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.734616369009018,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4961021780967712,
                "rejected_mean_error": 2.603475828965505,
                "gap_rejected_minus_accepted": 1.107373650868734
              }
            ]
          }
        }
      }
    },
    {
      "variant": "seed_relative_rater",
      "feature_mode": "M4_seed_relative",
      "model_kind": "mlp_big",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 135,
      "best_calib_loss": 0.008382142521440983,
      "train_time_sec": 70.5927345752716,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994522128473944,
            "spearman": 0.9983396972162837,
            "auroc_top30_bad": 0.9995361904761906,
            "mae": 0.03682902822187098,
            "mse": 0.0027481623961542983,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7894263834778708,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0019397343099117278
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17427753663659096
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4779826921492815
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8175089620769024
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
            "pearson": 0.9993521857129419,
            "spearman": 0.998846960177823,
            "auroc_top30_worst": 0.9984941904761906,
            "pairwise_seed_ranking": 0.9615,
            "predicted_best_mean_error": 1.6854562475085257,
            "seed0_mean_error": 1.7593383036255836,
            "random_seed_mean_error": 1.748514448583126,
            "oracle_best_mean_error": 1.6850638110637666,
            "improvement_over_seed0": 0.07388205611705789,
            "gap_to_oracle": 0.00039243644475916994,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6090292600989342
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.847416352391243
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.110705762255192
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3370086376269659
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7487053180277348
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.924907755851746,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4976920116808679,
                "rejected_mean_error": 4.007825075149536,
                "gap_rejected_minus_accepted": 2.5101330634686683
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.028457224369049,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3370086376269659,
                "rejected_mean_error": 2.9837953592300415,
                "gap_rejected_minus_accepted": 1.6467867216030756
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6341203451156616,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.110705762255192,
                "rejected_mean_error": 2.386704873800278,
                "gap_rejected_minus_accepted": 1.275999111545086
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1794337034225464,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.847416352391243,
                "rejected_mean_error": 2.0491349732398985,
                "gap_rejected_minus_accepted": 1.2017186208486554
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.926937913894654,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.508043487932947,
                "rejected_mean_error": 4.020991644859314,
                "gap_rejected_minus_accepted": 2.5129481569263667
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.046548843383789,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.34708282939593,
                "rejected_mean_error": 2.996104726314545,
                "gap_rejected_minus_accepted": 1.6490218969186148
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6435048580169678,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.116971683382988,
                "rejected_mean_error": 2.4017049238681794,
                "gap_rejected_minus_accepted": 1.2847332404851914
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1883240342140198,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8507224709987641,
                "rejected_mean_error": 2.0622102478345234,
                "gap_rejected_minus_accepted": 1.2114877768357593
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9888298081007629,
            "spearman": 0.9843148558337659,
            "auroc_top30_bad": 0.9955771428571428,
            "mae": 0.09586083368324885,
            "mse": 0.01795607895720508,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7081475657582881,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06083632236719132
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16865514364242554
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4190767878174782
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8047662122805913
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
            "pearson": 0.9841498347640518,
            "spearman": 0.9898428555794277,
            "auroc_top30_worst": 0.9870262857142857,
            "pairwise_seed_ranking": 0.9244,
            "predicted_best_mean_error": 1.5905591502189635,
            "seed0_mean_error": 1.6905601416826248,
            "random_seed_mean_error": 1.6723020417690277,
            "oracle_best_mean_error": 1.5885274814367294,
            "improvement_over_seed0": 0.10000099146366126,
            "gap_to_oracle": 0.002031668782234153,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46540371131896974
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7543978492418925
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1134885043144227
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3869857908184848
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6684940560817718
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5083400964736944,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5364094316164651,
                "rejected_mean_error": 2.8572556762695314,
                "gap_rejected_minus_accepted": 1.3208462446530662
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.012242317199707,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3861383300835193,
                "rejected_mean_error": 2.5137570441340484,
                "gap_rejected_minus_accepted": 1.1276187140505292
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.627505898475647,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1134885043144227,
                "rejected_mean_error": 2.223499607849121,
                "gap_rejected_minus_accepted": 1.1100111035346985
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0941935181617737,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7550207881120067,
                "rejected_mean_error": 1.9736350730236465,
                "gap_rejected_minus_accepted": 1.2186142849116397
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5076831579208374,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.554294541809294,
                "rejected_mean_error": 2.9169505405426026,
                "gap_rejected_minus_accepted": 1.3626559987333087
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0485183000564575,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.402291124676638,
                "rejected_mean_error": 2.5462157953353155,
                "gap_rejected_minus_accepted": 1.1439246706586774
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.630547285079956,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1309445517063141,
                "rejected_mean_error": 2.2501757316589357,
                "gap_rejected_minus_accepted": 1.1192311799526216
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1167364716529846,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7680088910791609,
                "rejected_mean_error": 2.0013661779821876,
                "gap_rejected_minus_accepted": 1.2333572869030267
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9875275539784003,
            "spearman": 0.9838726171768881,
            "auroc_top30_bad": 0.9932929523809524,
            "mae": 0.08749697766331965,
            "mse": 0.017219483708496925,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.7424427281416243,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06402416288852691
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17780557397603988
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5384312127053738
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9423457158366839
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
            "pearson": 0.9752363963183422,
            "spearman": 0.9840880067123244,
            "auroc_top30_worst": 0.9910339047619048,
            "pairwise_seed_ranking": 0.9228,
            "predicted_best_mean_error": 1.7605700478553772,
            "seed0_mean_error": 1.8668941221237183,
            "random_seed_mean_error": 1.8321932954788207,
            "oracle_best_mean_error": 1.7580343310832978,
            "improvement_over_seed0": 0.10632407426834112,
            "gap_to_oracle": 0.0025357167720794216,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.874985044002533
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1759557767938345
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4478314448356628
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.636571804788321
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8333799670696258
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3924510717391967,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.748637124962277,
                "rejected_mean_error": 2.5960655460357667,
                "gap_rejected_minus_accepted": 0.8474284210734897
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.115390717983246,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.636031244900336,
                "rejected_mean_error": 2.4241651193783307,
                "gap_rejected_minus_accepted": 0.7881338744779947
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8832435011863708,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4478314448356628,
                "rejected_mean_error": 2.2189284893035888,
                "gap_rejected_minus_accepted": 0.7710970444679259
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5162433385849,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1770806683899877,
                "rejected_mean_error": 2.0526133507267517,
                "gap_rejected_minus_accepted": 0.875532682336764
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.478866720199585,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7722248819139268,
                "rejected_mean_error": 2.718917284011841,
                "gap_rejected_minus_accepted": 0.9466924020979142
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.148568570613861,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6521254631287274,
                "rejected_mean_error": 2.504382046442183,
                "gap_rejected_minus_accepted": 0.8522565833134557
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9087292551994324,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4619965200424194,
                "rejected_mean_error": 2.271791724205017,
                "gap_rejected_minus_accepted": 0.8097952041625978
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5432631075382233,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1868110176116702,
                "rejected_mean_error": 2.096013028991414,
                "gap_rejected_minus_accepted": 0.9092020113797437
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9908140108678691,
            "spearman": 0.9881145792440874,
            "auroc_top30_bad": 0.9944833333333333,
            "mae": 0.09886896336431948,
            "mse": 0.02368099453550238,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.99,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.920870468401092,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06897469162940979
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21336028790473938
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7044890427589416
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0828059808413188
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
            "pearson": 0.9886357596445595,
            "spearman": 0.9865394305394306,
            "auroc_top30_worst": 0.9945380952380952,
            "pairwise_seed_ranking": 0.9095,
            "predicted_best_mean_error": 2.244566216766834,
            "seed0_mean_error": 2.3266324162483216,
            "random_seed_mean_error": 2.3179259487986563,
            "oracle_best_mean_error": 2.2414105245471,
            "improvement_over_seed0": 0.08206619948148752,
            "gap_to_oracle": 0.0031556922197339965,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3052605879306793
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4862453298568725
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6552036640644074
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8650935708681742
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.3207210887670517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.917295098304749,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 2.094915620883306,
                "rejected_mean_error": 4.352970299720764,
                "gap_rejected_minus_accepted": 2.258054678837458
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7828598022460938,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8650935708681742,
                "rejected_mean_error": 3.687603642463684,
                "gap_rejected_minus_accepted": 1.82251007159551
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.0111066102981567,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6552036640644074,
                "rejected_mean_error": 2.9862385134696963,
                "gap_rejected_minus_accepted": 1.3310348494052888
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7131086587905884,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4862453298568725,
                "rejected_mean_error": 2.5988796750704446,
                "gap_rejected_minus_accepted": 1.112634345213572
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.914802312850952,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 2.1037791278627185,
                "rejected_mean_error": 4.33231201171875,
                "gap_rejected_minus_accepted": 2.228532883856032
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.791804790496826,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8763225158055623,
                "rejected_mean_error": 3.677562117576599,
                "gap_rejected_minus_accepted": 1.8012396017710368
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.018012285232544,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6707446849346161,
                "rejected_mean_error": 2.982520147562027,
                "gap_rejected_minus_accepted": 1.311775462627411
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.723361611366272,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.5059186434745788,
                "rejected_mean_error": 2.600203673839569,
                "gap_rejected_minus_accepted": 1.0942850303649903
              }
            ]
          }
        }
      }
    },
    {
      "variant": "seed_relative_pairwise",
      "feature_mode": "M4_seed_relative",
      "model_kind": "mlp_big_pairwise",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 105,
      "best_calib_loss": 0.009226636961102486,
      "train_time_sec": 81.04666113853455,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993864639365215,
            "spearman": 0.9983755158644463,
            "auroc_top30_bad": 0.9994626190476191,
            "mae": 0.05718469827384069,
            "mse": 0.006861882276812381,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8054181196656636,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0009892609417438507
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17390361667275428
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4779621080905199
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.817509225577116
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
            "pearson": 0.9993709620166851,
            "spearman": 0.9989971219678607,
            "auroc_top30_worst": 0.9991750476190476,
            "pairwise_seed_ranking": 0.9677,
            "predicted_best_mean_error": 1.6857333699166774,
            "seed0_mean_error": 1.7593383036255836,
            "random_seed_mean_error": 1.748514448583126,
            "oracle_best_mean_error": 1.6850638110637666,
            "improvement_over_seed0": 0.0736049337089062,
            "gap_to_oracle": 0.0006695588529108676,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6092056260704994
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8471979534387588
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1105144303441048
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3370001329183578
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7487053180277348
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0385301113128667,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4976773470838864,
                "rejected_mean_error": 4.007957056522369,
                "gap_rejected_minus_accepted": 2.5102797094384828
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1103658080101013,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3370001329183578,
                "rejected_mean_error": 2.9838208733558655,
                "gap_rejected_minus_accepted": 1.6468207404375077
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6646613478660583,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1105144303441048,
                "rejected_mean_error": 2.386896205711365,
                "gap_rejected_minus_accepted": 1.2763817753672602
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1937130391597748,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8471979534387588,
                "rejected_mean_error": 2.0492077728907265,
                "gap_rejected_minus_accepted": 1.2020098194519677
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0344791412353525,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5080162266227934,
                "rejected_mean_error": 4.021236996650696,
                "gap_rejected_minus_accepted": 2.513220770027903
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1222251057624817,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3471313246885936,
                "rejected_mean_error": 2.995959240436554,
                "gap_rejected_minus_accepted": 1.6488279157479602
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6777305603027344,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1170283266305923,
                "rejected_mean_error": 2.401648280620575,
                "gap_rejected_minus_accepted": 1.2846199539899827
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1983765065670013,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8510826141834259,
                "rejected_mean_error": 2.062090200106303,
                "gap_rejected_minus_accepted": 1.2110075859228773
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9870334490348158,
            "spearman": 0.9779332494834707,
            "auroc_top30_bad": 0.9965744761904762,
            "mae": 0.10198204011122398,
            "mse": 0.01951401011364582,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7196894434834158,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09408886793255807
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1884991609096527
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4189433938622475
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8037933358589808
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
            "pearson": 0.9875220119452348,
            "spearman": 0.9899639354649188,
            "auroc_top30_worst": 0.9841127619047618,
            "pairwise_seed_ranking": 0.9396,
            "predicted_best_mean_error": 1.5896395703554154,
            "seed0_mean_error": 1.6905601416826248,
            "random_seed_mean_error": 1.6723020417690277,
            "oracle_best_mean_error": 1.5885274814367294,
            "improvement_over_seed0": 0.10092057132720944,
            "gap_to_oracle": 0.0011120889186859717,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4685960741043091
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7497010706708982
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1147060853004456
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3881978024678951
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6684940560817718
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6381062507629403,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5326105070643954,
                "rejected_mean_error": 2.891445997238159,
                "gap_rejected_minus_accepted": 1.3588354901737638
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0586840510368347,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3873964810829407,
                "rejected_mean_error": 2.509990630439295,
                "gap_rejected_minus_accepted": 1.1225941493563545
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5691532492637634,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1147060853004456,
                "rejected_mean_error": 2.2222820268630983,
                "gap_rejected_minus_accepted": 1.1075759415626527
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0269286334514618,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.750582220264898,
                "rejected_mean_error": 1.9751177536385291,
                "gap_rejected_minus_accepted": 1.2245355333736312
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.674027609825134,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.550678687757916,
                "rejected_mean_error": 2.949493227005005,
                "gap_rejected_minus_accepted": 1.398814539247089
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.06679904460907,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4038091548942626,
                "rejected_mean_error": 2.5417098961179216,
                "gap_rejected_minus_accepted": 1.137900741223659
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5755903124809265,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1334084408283234,
                "rejected_mean_error": 2.2477118425369262,
                "gap_rejected_minus_accepted": 1.1143034017086029
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0697502195835114,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7647884199543605,
                "rejected_mean_error": 2.0024511495376016,
                "gap_rejected_minus_accepted": 1.2376627295832412
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9881862664208773,
            "spearman": 0.9826506500754947,
            "auroc_top30_bad": 0.9919779047619048,
            "mae": 0.08747713453789256,
            "mse": 0.016774703206428744,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.760758043287979,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07278382807970046
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18590453552007674
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5379986744821071
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9429363780935606
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
            "pearson": 0.987139051695773,
            "spearman": 0.985903602882306,
            "auroc_top30_worst": 0.9951055238095238,
            "pairwise_seed_ranking": 0.9424,
            "predicted_best_mean_error": 1.759391058921814,
            "seed0_mean_error": 1.8668941221237183,
            "random_seed_mean_error": 1.8321932954788207,
            "oracle_best_mean_error": 1.7580343310832978,
            "improvement_over_seed0": 0.10750306320190428,
            "gap_to_oracle": 0.0013567278385162584,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8659746308326721
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1748049513269694
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4505784003257751
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6329388966057092
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8333799670696258
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5215619564056397,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7428055612246196,
                "rejected_mean_error": 2.6485496196746827,
                "gap_rejected_minus_accepted": 0.9057440584500631
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2179301381111145,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6323055467203562,
                "rejected_mean_error": 2.4353184075401235,
                "gap_rejected_minus_accepted": 0.8030128608197673
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9020599126815796,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4505784003257751,
                "rejected_mean_error": 2.2161815338134767,
                "gap_rejected_minus_accepted": 0.7656031334877016
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4725874066352844,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1758204551931388,
                "rejected_mean_error": 2.053034318422177,
                "gap_rejected_minus_accepted": 0.877213863229038
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6602603912353517,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7669861147138808,
                "rejected_mean_error": 2.766066188812256,
                "gap_rejected_minus_accepted": 0.9990800740983752
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2928369641304016,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.646880709551235,
                "rejected_mean_error": 2.5199498070610895,
                "gap_rejected_minus_accepted": 0.8730690975098545
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9485414028167725,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4678795108795166,
                "rejected_mean_error": 2.2659087333679198,
                "gap_rejected_minus_accepted": 0.7980292224884031
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5088828802108765,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1866100004741125,
                "rejected_mean_error": 2.0960807513425697,
                "gap_rejected_minus_accepted": 0.9094707508684572
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9914667926140954,
            "spearman": 0.9872131637061224,
            "auroc_top30_bad": 0.9939476190476191,
            "mae": 0.11573822447111343,
            "mse": 0.026409773111813948,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9678488831605959,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06444939017295838
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21023184373974801
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7052818348407746
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.082919162193934
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
            "pearson": 0.9863526954756865,
            "spearman": 0.979950115950116,
            "auroc_top30_worst": 0.9938761904761904,
            "pairwise_seed_ranking": 0.9175,
            "predicted_best_mean_error": 2.2428122052550314,
            "seed0_mean_error": 2.3266324162483216,
            "random_seed_mean_error": 2.3179259487986563,
            "oracle_best_mean_error": 2.2414105245471,
            "improvement_over_seed0": 0.08382021099329018,
            "gap_to_oracle": 0.001401680707931341,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3094154930114745
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.494969885826111
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6572136042118073
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8655108981132507
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.3207210887670517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.141586112976074,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 2.0952171258131664,
                "rejected_mean_error": 4.35025675535202,
                "gap_rejected_minus_accepted": 2.2550396295388535
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.924834668636322,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8655108981132507,
                "rejected_mean_error": 3.6863516607284548,
                "gap_rejected_minus_accepted": 1.8208407626152041
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.1081260442733765,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6572136042118073,
                "rejected_mean_error": 2.984228573322296,
                "gap_rejected_minus_accepted": 1.3270149691104889
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7578613460063934,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.494969885826111,
                "rejected_mean_error": 2.5959714897473654,
                "gap_rejected_minus_accepted": 1.1010016039212545
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.112185478210449,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 2.1037791278627185,
                "rejected_mean_error": 4.33231201171875,
                "gap_rejected_minus_accepted": 2.228532883856032
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8911567330360413,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8765856377283732,
                "rejected_mean_error": 3.6767727518081665,
                "gap_rejected_minus_accepted": 1.8001871140797934
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.121522068977356,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.672626074552536,
                "rejected_mean_error": 2.980638757944107,
                "gap_rejected_minus_accepted": 1.3080126833915708
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7704829573631287,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.5110999655723572,
                "rejected_mean_error": 2.598476566473643,
                "gap_rejected_minus_accepted": 1.0873766009012857
              }
            ]
          }
        }
      }
    },
    {
      "variant": "per_step_error_head",
      "feature_mode": "M4_seed_relative",
      "model_kind": "perstep",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 110,
      "best_calib_loss": 0.009329722262918949,
      "train_time_sec": 54.78388261795044,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9990090940373013,
            "spearman": 0.9977211260163537,
            "auroc_top30_bad": 0.9982424285714286,
            "mae": 0.05112459106064462,
            "mse": 0.005401594817279219,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7983070363595377,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.000543388307094574
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1739248602569103
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47813053756058216
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8180876621743043
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
            "pearson": 0.9986815024369131,
            "spearman": 0.99726625301065,
            "auroc_top30_worst": 0.9976127619047619,
            "pairwise_seed_ranking": 0.9541,
            "predicted_best_mean_error": 1.6859323482215405,
            "seed0_mean_error": 1.7593383036255836,
            "random_seed_mean_error": 1.748514448583126,
            "oracle_best_mean_error": 1.6850638110637666,
            "improvement_over_seed0": 0.07340595540404315,
            "gap_to_oracle": 0.0008685371577739076,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6095226487517357
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8482590851068497
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1113331307530403
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3372970554113388
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7487053180277348
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.987127304077149,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4978106054266294,
                "rejected_mean_error": 4.006757731437683,
                "gap_rejected_minus_accepted": 2.508947126011054
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.086575150489807,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3372970554113388,
                "rejected_mean_error": 2.9829301058769224,
                "gap_rejected_minus_accepted": 1.6456330504655836
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6691532135009766,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1113331307530403,
                "rejected_mean_error": 2.386077505302429,
                "gap_rejected_minus_accepted": 1.2747443745493887
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.189441055059433,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8482590851068497,
                "rejected_mean_error": 2.0488540623346965,
                "gap_rejected_minus_accepted": 1.2005949772278468
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.9399501085281394,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.508213652835952,
                "rejected_mean_error": 4.019460160732269,
                "gap_rejected_minus_accepted": 2.511246507896317
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1126527786254883,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3473481323719025,
                "rejected_mean_error": 2.9953088173866274,
                "gap_rejected_minus_accepted": 1.6479606850147248
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6882076859474182,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1178998786211014,
                "rejected_mean_error": 2.400776728630066,
                "gap_rejected_minus_accepted": 1.2828768500089647
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2026213109493256,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8521568744182587,
                "rejected_mean_error": 2.0617321133613586,
                "gap_rejected_minus_accepted": 1.2095752389431
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9881991508001435,
            "spearman": 0.9857571076025631,
            "auroc_top30_bad": 0.9965043809523809,
            "mae": 0.10264786339743968,
            "mse": 0.02087448795904419,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7033143425734286,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06324776366353035
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1709937347650528
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.41903225466012956
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8022218428373337
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
            "pearson": 0.9804457900780634,
            "spearman": 0.9903629332242773,
            "auroc_top30_worst": 0.9886537142857142,
            "pairwise_seed_ranking": 0.9272,
            "predicted_best_mean_error": 1.589909031867981,
            "seed0_mean_error": 1.6905601416826248,
            "random_seed_mean_error": 1.6723020417690277,
            "oracle_best_mean_error": 1.5885274814367294,
            "improvement_over_seed0": 0.10065110981464387,
            "gap_to_oracle": 0.0013815504312515436,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4736092896461487
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7529240863827559
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1132412346839904
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3861585682007804
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6684940560817718
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5108731985092176,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5395086716016133,
                "rejected_mean_error": 2.829362516403198,
                "gap_rejected_minus_accepted": 1.2898538448015848
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.005215883255005,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3854665376460666,
                "rejected_mean_error": 2.5157681288429723,
                "gap_rejected_minus_accepted": 1.1303015911969057
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5917656421661377,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1132412346839904,
                "rejected_mean_error": 2.2237468774795532,
                "gap_rejected_minus_accepted": 1.1105056427955629
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.062041163444519,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7541078258627139,
                "rejected_mean_error": 1.9739400433374443,
                "gap_rejected_minus_accepted": 1.2198322174747305
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5435546875,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5557373344898224,
                "rejected_mean_error": 2.903965406417847,
                "gap_rejected_minus_accepted": 1.3482280719280244
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0165775418281555,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4024584396956439,
                "rejected_mean_error": 2.545719161866203,
                "gap_rejected_minus_accepted": 1.1432607221705593
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.596286654472351,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1307016537189483,
                "rejected_mean_error": 2.250418629646301,
                "gap_rejected_minus_accepted": 1.1197169759273529
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1134217381477356,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.765948210916822,
                "rejected_mean_error": 2.0020604178229755,
                "gap_rejected_minus_accepted": 1.2361122069061534
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9827840232392053,
            "spearman": 0.9795913083487868,
            "auroc_top30_bad": 0.9903801904761905,
            "mae": 0.10148818731401615,
            "mse": 0.02360703552190039,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.7447781479271197,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07241937792301179
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18557906712293626
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5392583890855313
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9440501189510028
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
            "pearson": 0.950881018909076,
            "spearman": 0.964155063907241,
            "auroc_top30_worst": 0.9773287619047618,
            "pairwise_seed_ranking": 0.9296,
            "predicted_best_mean_error": 1.7604817552566527,
            "seed0_mean_error": 1.8668941221237183,
            "random_seed_mean_error": 1.8321932954788207,
            "oracle_best_mean_error": 1.7580343310832978,
            "improvement_over_seed0": 0.10641236686706557,
            "gap_to_oracle": 0.002447424173354973,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.878893786907196
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1788697519745581
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4523015862464905
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6414764155584103
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8333799670696258
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4151095867156984,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.759641902870602,
                "rejected_mean_error": 2.49702254486084,
                "gap_rejected_minus_accepted": 0.7373806419902378
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.140004873275757,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6408392863314332,
                "rejected_mean_error": 2.4097717173945026,
                "gap_rejected_minus_accepted": 0.7689324310630694
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.894873023033142,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4523015862464905,
                "rejected_mean_error": 2.2144583478927613,
                "gap_rejected_minus_accepted": 0.7621567616462708
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4663942754268646,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.180474788045731,
                "rejected_mean_error": 2.0514795626240327,
                "gap_rejected_minus_accepted": 0.8710047745783018
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.498811244964599,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.785934844546848,
                "rejected_mean_error": 2.595527620315552,
                "gap_rejected_minus_accepted": 0.809592775768704
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.18482506275177,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.652956660418587,
                "rejected_mean_error": 2.501914841788156,
                "gap_rejected_minus_accepted": 0.8489581813695688
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9150273203849792,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4665111865997313,
                "rejected_mean_error": 2.2672770576477053,
                "gap_rejected_minus_accepted": 0.8007658710479739
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4770410656929016,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.190444168590364,
                "rejected_mean_error": 2.094789026255276,
                "gap_rejected_minus_accepted": 0.9043448576649122
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9889446280916687,
            "spearman": 0.9858343067725691,
            "auroc_top30_bad": 0.990902380952381,
            "mae": 0.11067780308633371,
            "mse": 0.027703122645675447,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9335386590632996,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04546497523784637
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21949562165141107
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7052224856615067
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0835275541941325
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
            "pearson": 0.985456381267931,
            "spearman": 0.9846708366708369,
            "auroc_top30_worst": 0.9963523809523809,
            "pairwise_seed_ranking": 0.8995,
            "predicted_best_mean_error": 2.2446185514330863,
            "seed0_mean_error": 2.3266324162483216,
            "random_seed_mean_error": 2.3179259487986563,
            "oracle_best_mean_error": 2.2414105245471,
            "improvement_over_seed0": 0.08201386481523532,
            "gap_to_oracle": 0.0032080268859862038,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.310980086326599
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4931459975242616
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6551634635925292
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8600119725863138
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.3207210887670517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.9476460456848144,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 2.097096652322345,
                "rejected_mean_error": 4.333341016769409,
                "gap_rejected_minus_accepted": 2.2362443644470638
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.742343842983246,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8600119725863138,
                "rejected_mean_error": 3.702848437309265,
                "gap_rejected_minus_accepted": 1.8428364647229514
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.080074906349182,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6551634635925292,
                "rejected_mean_error": 2.9862787139415743,
                "gap_rejected_minus_accepted": 1.331115250349045
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.752795785665512,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4931459975242616,
                "rejected_mean_error": 2.5965794525146486,
                "gap_rejected_minus_accepted": 1.103433454990387
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.963065505027771,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 2.1060607194900514,
                "rejected_mean_error": 4.3117776870727536,
                "gap_rejected_minus_accepted": 2.205716967582702
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.739131808280945,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8688090626398723,
                "rejected_mean_error": 3.7001024770736692,
                "gap_rejected_minus_accepted": 1.831293414433797
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.0858370065689087,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6707348656654357,
                "rejected_mean_error": 2.982529966831207,
                "gap_rejected_minus_accepted": 1.3117951011657714
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.757624626159668,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.5113980746269227,
                "rejected_mean_error": 2.5983771967887876,
                "gap_rejected_minus_accepted": 1.086979122161865
              }
            ]
          }
        }
      }
    },
    {
      "variant": "full_engineered_mlp",
      "feature_mode": "M2_engineered",
      "model_kind": "mlp_big",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1562,
      "best_epoch": 148,
      "best_calib_loss": 0.010288304649293423,
      "train_time_sec": 72.4830687046051,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9984555271558802,
            "spearman": 0.9969401551357188,
            "auroc_top30_bad": 0.9990660476190476,
            "mae": 0.07663460469787751,
            "mse": 0.01371605532977517,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8106859917690631,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.009245974853634834
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17522379717230796
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47832315371334555
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8178442959487439
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
            "pearson": 0.998527415789793,
            "spearman": 0.9967795876151833,
            "auroc_top30_worst": 0.997804,
            "pairwise_seed_ranking": 0.9563,
            "predicted_best_mean_error": 1.6856150580644607,
            "seed0_mean_error": 1.7593383036255836,
            "random_seed_mean_error": 1.748514448583126,
            "oracle_best_mean_error": 1.6850638110637666,
            "improvement_over_seed0": 0.07372324556112297,
            "gap_to_oracle": 0.0005512470006940884,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6100605142712593
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.849189189362526
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1119470915913583
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3382901169538497
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7487053180277348
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1112253189086942,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4977706525127092,
                "rejected_mean_error": 4.007117307662964,
                "gap_rejected_minus_accepted": 2.5093466551502543
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.142931640148163,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3382901169538497,
                "rejected_mean_error": 2.9799509212493898,
                "gap_rejected_minus_accepted": 1.64166080429554
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6732832789421082,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1119470915913583,
                "rejected_mean_error": 2.3854635444641112,
                "gap_rejected_minus_accepted": 1.273516452872753
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1844264566898346,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.849189189362526,
                "rejected_mean_error": 2.048544027582804,
                "gap_rejected_minus_accepted": 1.199354838220278
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1206104993820194,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5081365766127903,
                "rejected_mean_error": 4.0201538467407225,
                "gap_rejected_minus_accepted": 2.512017270127932
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1618669629096985,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3488194084962208,
                "rejected_mean_error": 2.990894989013672,
                "gap_rejected_minus_accepted": 1.642075580517451
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.68540620803833,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.118104900240898,
                "rejected_mean_error": 2.4005717070102692,
                "gap_rejected_minus_accepted": 1.2824668067693712
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1901774108409882,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.853370646238327,
                "rejected_mean_error": 2.0613275227546692,
                "gap_rejected_minus_accepted": 1.2079568765163422
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9850550513490965,
            "spearman": 0.9798912157058973,
            "auroc_top30_bad": 0.9960091428571428,
            "mae": 0.10808076151504038,
            "mse": 0.021852197712531326,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7069055209997679,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07487265112996101
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18668813767433168
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4189987446427345
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8034376283725103
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
            "pearson": 0.9806238311426796,
            "spearman": 0.9892148769375213,
            "auroc_top30_worst": 0.987303619047619,
            "pairwise_seed_ranking": 0.9308,
            "predicted_best_mean_error": 1.591174110531807,
            "seed0_mean_error": 1.6905601416826248,
            "random_seed_mean_error": 1.6723020417690277,
            "oracle_best_mean_error": 1.5885274814367294,
            "improvement_over_seed0": 0.0993860311508179,
            "gap_to_oracle": 0.002646629095077513,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.47648281955718996
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7499001754017977
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.114340347957611
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3874953084790123
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6684940560817718
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5938050031661994,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.53630755270852,
                "rejected_mean_error": 2.85817258644104,
                "gap_rejected_minus_accepted": 1.32186503373252
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0784443020820618,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3865809938696432,
                "rejected_mean_error": 2.5124318812982724,
                "gap_rejected_minus_accepted": 1.1258508874286293
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5996366739273071,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.114340347957611,
                "rejected_mean_error": 2.2226477642059326,
                "gap_rejected_minus_accepted": 1.1083074162483215
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0550897419452667,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7508765064870206,
                "rejected_mean_error": 1.975019448849282,
                "gap_rejected_minus_accepted": 1.2241429423622614
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6141507387161256,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5547290951675838,
                "rejected_mean_error": 2.9130395603179933,
                "gap_rejected_minus_accepted": 1.3583104651504094
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0972869992256165,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4046124763348524,
                "rejected_mean_error": 2.539325434064108,
                "gap_rejected_minus_accepted": 1.1347129577292556
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6176229119300842,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.131088706254959,
                "rejected_mean_error": 2.2500315771102906,
                "gap_rejected_minus_accepted": 1.1189428708553315
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0836698114871979,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7643831121543098,
                "rejected_mean_error": 2.0025876970852123,
                "gap_rejected_minus_accepted": 1.2382045849309025
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9854915845642658,
            "spearman": 0.9819328426509774,
            "auroc_top30_bad": 0.9934765714285715,
            "mae": 0.10457396548688866,
            "mse": 0.02126352867251141,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7454604915171127,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08294860363006591
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18767618364095687
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5391843661248684
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.942363072582086
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
            "pearson": 0.9767785943374259,
            "spearman": 0.9828051694113086,
            "auroc_top30_worst": 0.9927192380952381,
            "pairwise_seed_ranking": 0.9244,
            "predicted_best_mean_error": 1.7603719379901885,
            "seed0_mean_error": 1.8668941221237183,
            "random_seed_mean_error": 1.8321932954788207,
            "oracle_best_mean_error": 1.7580343310832978,
            "improvement_over_seed0": 0.10652218413352976,
            "gap_to_oracle": 0.0023376069068907768,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8796159582138061
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.178516486325325
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4482918774604798
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6349212294067148
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8333799670696258
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4875781297683717,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7471817130512661,
                "rejected_mean_error": 2.609164253234863,
                "gap_rejected_minus_accepted": 0.861982540183597
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.208255887031555,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6342151070226345,
                "rejected_mean_error": 2.4296019282965613,
                "gap_rejected_minus_accepted": 0.7953868212739268
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.927522897720337,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4482918774604798,
                "rejected_mean_error": 2.218468056678772,
                "gap_rejected_minus_accepted": 0.7701761792182922
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4890907406806946,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.17961692181639,
                "rejected_mean_error": 2.051766128397548,
                "gap_rejected_minus_accepted": 0.8721492065811578
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5879567384719846,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7697792604234484,
                "rejected_mean_error": 2.7409278774261474,
                "gap_rejected_minus_accepted": 0.971148617002699
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2558265328407288,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6491299160024062,
                "rejected_mean_error": 2.513273591086978,
                "gap_rejected_minus_accepted": 0.8641436750845717
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.95609450340271,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4631648635864258,
                "rejected_mean_error": 2.2706233806610108,
                "gap_rejected_minus_accepted": 0.8074585170745849
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5146376192569733,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1897792362031483,
                "rejected_mean_error": 2.0950130409097927,
                "gap_rejected_minus_accepted": 0.9052338047066444
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9895170708359919,
            "spearman": 0.9857537254523913,
            "auroc_top30_bad": 0.9940119047619047,
            "mae": 0.13557379309734108,
            "mse": 0.03530999612825156,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9545518458135583,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0796677366644144
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22610421785712242
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7040144234895707
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.083506148258845
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
            "pearson": 0.9878249477282353,
            "spearman": 0.9861013941013941,
            "auroc_top30_worst": 0.9951380952380952,
            "pairwise_seed_ranking": 0.8995,
            "predicted_best_mean_error": 2.2449921146035194,
            "seed0_mean_error": 2.3266324162483216,
            "random_seed_mean_error": 2.3179259487986563,
            "oracle_best_mean_error": 2.2414105245471,
            "improvement_over_seed0": 0.08164030164480218,
            "gap_to_oracle": 0.003581590056419337,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3106298172473907
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4859519901275635
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6574918212890626
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8631656889915467
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.3207210887670517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.164600896835327,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 2.094434322383669,
                "rejected_mean_error": 4.357301986217498,
                "gap_rejected_minus_accepted": 2.2628676638338296
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.9039148688316345,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8631656889915467,
                "rejected_mean_error": 3.6933872880935668,
                "gap_rejected_minus_accepted": 1.83022159910202
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.140514850616455,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6574918212890626,
                "rejected_mean_error": 2.9839503562450407,
                "gap_rejected_minus_accepted": 1.326458534955978
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7671508193016052,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4859519901275635,
                "rejected_mean_error": 2.5989774549802145,
                "gap_rejected_minus_accepted": 1.113025464852651
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.155360889434815,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 2.1027985480096607,
                "rejected_mean_error": 4.341137230396271,
                "gap_rejected_minus_accepted": 2.23833868238661
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.884196400642395,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8742657820383708,
                "rejected_mean_error": 3.6837323188781737,
                "gap_rejected_minus_accepted": 1.8094665368398029
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.140291929244995,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.673849003314972,
                "rejected_mean_error": 2.9794158291816712,
                "gap_rejected_minus_accepted": 1.3055668258666993
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.79604971408844,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.5009668064117432,
                "rejected_mean_error": 2.6018542861938476,
                "gap_rejected_minus_accepted": 1.1008874797821044
              }
            ]
          }
        }
      }
    },
    {
      "variant": "full_engineered_simvla_focused",
      "feature_mode": "M2_engineered",
      "model_kind": "mlp_big",
      "train_setting": "simvla_focused",
      "train_rows": 10000,
      "input_dim": 1562,
      "best_epoch": 144,
      "best_calib_loss": 0.009044556878507137,
      "train_time_sec": 72.44721388816833,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994679937265551,
            "spearman": 0.9984906249434753,
            "auroc_top30_bad": 0.9994292380952381,
            "mae": 0.027886471004074473,
            "mse": 0.001470257720029214,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7770658506741308,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0006569971293210983
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17420850313305855
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47794146900475026
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8175795295099417
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
            "pearson": 0.9993573858820338,
            "spearman": 0.9987536666301168,
            "auroc_top30_worst": 0.9985662857142857,
            "pairwise_seed_ranking": 0.9679,
            "predicted_best_mean_error": 1.6853933587372303,
            "seed0_mean_error": 1.7593383036255836,
            "random_seed_mean_error": 1.748514448583126,
            "oracle_best_mean_error": 1.6850638110637666,
            "improvement_over_seed0": 0.07394494488835335,
            "gap_to_oracle": 0.00032954767346371483,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6091202360987663
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8472354392290116
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.110599275934696
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3369456652084986
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7487053180277348
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8984586477279666,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4976317469875018,
                "rejected_mean_error": 4.008367457389832,
                "gap_rejected_minus_accepted": 2.51073571040233
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.016762614250183,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3369456652084986,
                "rejected_mean_error": 2.983984276485443,
                "gap_rejected_minus_accepted": 1.6470386112769444
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6140285730361938,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.110599275934696,
                "rejected_mean_error": 2.3868113601207734,
                "gap_rejected_minus_accepted": 1.2762120841860773
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1518549919128418,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8472354392290116,
                "rejected_mean_error": 2.0491952776273092,
                "gap_rejected_minus_accepted": 1.2019598383982977
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.930239248275757,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5080162266227934,
                "rejected_mean_error": 4.021236996650696,
                "gap_rejected_minus_accepted": 2.513220770027903
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0240809321403503,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3472512638568879,
                "rejected_mean_error": 2.9955994229316714,
                "gap_rejected_minus_accepted": 1.6483481590747835
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6304583549499512,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1172993386983872,
                "rejected_mean_error": 2.40137726855278,
                "gap_rejected_minus_accepted": 1.284077929854393
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1635416746139526,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8506543447971344,
                "rejected_mean_error": 2.0622329565684,
                "gap_rejected_minus_accepted": 1.2115786117712655
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9889271085151313,
            "spearman": 0.9846115532573642,
            "auroc_top30_bad": 0.9966506666666667,
            "mae": 0.09787236144176117,
            "mse": 0.020277999751936688,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6956081603550318,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07317058405280114
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1694118323802948
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.41808143011331556
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8034329504728317
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
            "pearson": 0.9837877208806571,
            "spearman": 0.9908185418358668,
            "auroc_top30_worst": 0.9881782857142858,
            "pairwise_seed_ranking": 0.942,
            "predicted_best_mean_error": 1.5893396731615066,
            "seed0_mean_error": 1.6905601416826248,
            "random_seed_mean_error": 1.6723020417690277,
            "oracle_best_mean_error": 1.5885274814367294,
            "improvement_over_seed0": 0.10122046852111821,
            "gap_to_oracle": 0.0008121917247772004,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46612153911590576
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7494095546694902
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1133597758293152
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3867847302448013
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6684940560817718
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4562353849411016,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5371088457637363,
                "rejected_mean_error": 2.850960948944092,
                "gap_rejected_minus_accepted": 1.3138521031803556
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9763388633728027,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3859043050728332,
                "rejected_mean_error": 2.5144576237986263,
                "gap_rejected_minus_accepted": 1.128553318725793
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6274033784866333,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1133597758293152,
                "rejected_mean_error": 2.2236283363342286,
                "gap_rejected_minus_accepted": 1.1102685605049134
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0529266893863678,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7507043058118119,
                "rejected_mean_error": 1.9750769715935088,
                "gap_rejected_minus_accepted": 1.224372665781697
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4753382921218874,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.55548160566224,
                "rejected_mean_error": 2.906266965866089,
                "gap_rejected_minus_accepted": 1.3507853602038489
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9931321144104004,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4015367976165711,
                "rejected_mean_error": 2.548454829624721,
                "gap_rejected_minus_accepted": 1.1469180320081498
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.648275375366211,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1309507296085357,
                "rejected_mean_error": 2.250169553756714,
                "gap_rejected_minus_accepted": 1.1192188241481782
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0833496451377869,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7625579971169668,
                "rejected_mean_error": 2.003202575413301,
                "gap_rejected_minus_accepted": 1.240644578296334
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9862464375245246,
            "spearman": 0.9833750344863452,
            "auroc_top30_bad": 0.9906956190476192,
            "mae": 0.09733005622218979,
            "mse": 0.01970296284536732,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.7270869803068325,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05709449738264084
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.175676071703434
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5389566783845424
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.943001333741347
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
            "pearson": 0.9645419998621444,
            "spearman": 0.9734443554843876,
            "auroc_top30_worst": 0.9858529523809524,
            "pairwise_seed_ranking": 0.9328,
            "predicted_best_mean_error": 1.7599092080593108,
            "seed0_mean_error": 1.8668941221237183,
            "random_seed_mean_error": 1.8321932954788207,
            "oracle_best_mean_error": 1.7580343310832978,
            "improvement_over_seed0": 0.10698491406440747,
            "gap_to_oracle": 0.0018748769760130735,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8801763424873352
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1804013724128406
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.448830064868927
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.640254261968995
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8333799670696258
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3650428056716923,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.754064833694034,
                "rejected_mean_error": 2.5472161674499514,
                "gap_rejected_minus_accepted": 0.7931513337559173
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.079928398132324,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6394646865581117,
                "rejected_mean_error": 2.4138867333293343,
                "gap_rejected_minus_accepted": 0.7744220467712226
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8190852999687195,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.448830064868927,
                "rejected_mean_error": 2.217929869270325,
                "gap_rejected_minus_accepted": 0.7690998044013979
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4736452996730804,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1820370920549947,
                "rejected_mean_error": 2.0509576830563705,
                "gap_rejected_minus_accepted": 0.8689205910013758
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4190565824508665,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7843366792466906,
                "rejected_mean_error": 2.6099111080169677,
                "gap_rejected_minus_accepted": 0.8255744287702771
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.122725248336792,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.655916129841524,
                "rejected_mean_error": 2.4931303849295965,
                "gap_rejected_minus_accepted": 0.8372142550880726
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8409289717674255,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.462780704498291,
                "rejected_mean_error": 2.2710075397491454,
                "gap_rejected_minus_accepted": 0.8082268352508544
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4873827993869781,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.20056314506228,
                "rejected_mean_error": 2.0913799593155398,
                "gap_rejected_minus_accepted": 0.8908168142532598
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.990839259306856,
            "spearman": 0.9863937912197365,
            "auroc_top30_bad": 0.992732142857143,
            "mae": 0.09839676540392782,
            "mse": 0.023210749379407942,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9155977589118399,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06236700691282749
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22315693512558937
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7046298841238022
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0831495610872905
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
            "pearson": 0.9886338189816242,
            "spearman": 0.9821553221553222,
            "auroc_top30_worst": 0.9949190476190477,
            "pairwise_seed_ranking": 0.905,
            "predicted_best_mean_error": 2.2445057454705237,
            "seed0_mean_error": 2.3266324162483216,
            "random_seed_mean_error": 2.3179259487986563,
            "oracle_best_mean_error": 2.2414105245471,
            "improvement_over_seed0": 0.0821266707777979,
            "gap_to_oracle": 0.003095220923423625,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3077843570709229
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4949635305404663
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.656174322605133
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8625032280286153
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.3207210887670517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.9467199802398683,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 2.0951352873113422,
                "rejected_mean_error": 4.350993301868439,
                "gap_rejected_minus_accepted": 2.2558580145570963
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7236915230751038,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8625032280286153,
                "rejected_mean_error": 3.695374670982361,
                "gap_rejected_minus_accepted": 1.8328714429537456
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9832322597503662,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.656174322605133,
                "rejected_mean_error": 2.98526785492897,
                "gap_rejected_minus_accepted": 1.329093532323837
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7078523635864258,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4949635305404663,
                "rejected_mean_error": 2.5959736081759135,
                "gap_rejected_minus_accepted": 1.1010100776354472
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.9445140838623045,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 2.1037791278627185,
                "rejected_mean_error": 4.33231201171875,
                "gap_rejected_minus_accepted": 2.228532883856032
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.697983205318451,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8734519147872926,
                "rejected_mean_error": 3.6861739206314086,
                "gap_rejected_minus_accepted": 1.812722005844116
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.989353060722351,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6700553858280183,
                "rejected_mean_error": 2.9832094466686248,
                "gap_rejected_minus_accepted": 1.3131540608406065
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.709272861480713,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.512566339969635,
                "rejected_mean_error": 2.597987775007884,
                "gap_rejected_minus_accepted": 1.085421435038249
              }
            ]
          }
        }
      }
    },
    {
      "variant": "seed_relative_simvla_focused",
      "feature_mode": "M4_seed_relative",
      "model_kind": "mlp_big_pairwise",
      "train_setting": "simvla_focused",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 125,
      "best_calib_loss": 0.008422575891017914,
      "train_time_sec": 79.96041440963745,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996534598761759,
            "spearman": 0.9985136029115731,
            "auroc_top30_bad": 0.9996710952380953,
            "mae": 0.023324654999691847,
            "mse": 0.0009549285809531374,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7716367608818585,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0011763361543416977
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17372413098216058
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4779273568421602
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.817395834304889
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
            "pearson": 0.9996550309238216,
            "spearman": 0.9992678393627135,
            "auroc_top30_worst": 0.9994087619047619,
            "pairwise_seed_ranking": 0.9645,
            "predicted_best_mean_error": 1.6856635997593403,
            "seed0_mean_error": 1.7593383036255836,
            "random_seed_mean_error": 1.748514448583126,
            "oracle_best_mean_error": 1.6850638110637666,
            "improvement_over_seed0": 0.07367470386624331,
            "gap_to_oracle": 0.0005997886955737552,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6092626278996468
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8470229323625564
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1104996240735054
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.336801255774498
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7487053180277348
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8934638261795045,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4976608043313027,
                "rejected_mean_error": 4.008105941295624,
                "gap_rejected_minus_accepted": 2.5104451369643215
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.02360337972641,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.336801255774498,
                "rejected_mean_error": 2.9844175047874453,
                "gap_rejected_minus_accepted": 1.6476162490129473
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6149219274520874,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1104996240735054,
                "rejected_mean_error": 2.3869110119819643,
                "gap_rejected_minus_accepted": 1.2764113879084589
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1716657876968384,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8470229323625564,
                "rejected_mean_error": 2.0492661132494607,
                "gap_rejected_minus_accepted": 1.2022431808869043
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8934638261795045,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5080162266227934,
                "rejected_mean_error": 4.021236996650696,
                "gap_rejected_minus_accepted": 2.513220770027903
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.043700158596039,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.347169694185257,
                "rejected_mean_error": 2.995844131946564,
                "gap_rejected_minus_accepted": 1.648674437761307
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6235255002975464,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1170021287202836,
                "rejected_mean_error": 2.4016744785308837,
                "gap_rejected_minus_accepted": 1.2846723498106
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.177231341600418,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8508794291019439,
                "rejected_mean_error": 2.062157928466797,
                "gap_rejected_minus_accepted": 1.2112784993648529
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9884386873387884,
            "spearman": 0.9779790265651308,
            "auroc_top30_bad": 0.9963466666666666,
            "mae": 0.09347446028531849,
            "mse": 0.017856089846724852,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.706477987170742,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09045027616620063
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19425701155662536
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4188068879723549
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8033567443927129
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
            "pearson": 0.9899366633897182,
            "spearman": 0.9884703158210023,
            "auroc_top30_worst": 0.9837043809523809,
            "pairwise_seed_ranking": 0.9424,
            "predicted_best_mean_error": 1.5893896543979644,
            "seed0_mean_error": 1.6905601416826248,
            "random_seed_mean_error": 1.6723020417690277,
            "oracle_best_mean_error": 1.5885274814367294,
            "improvement_over_seed0": 0.10117048728466038,
            "gap_to_oracle": 0.0008621729612350304,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4725486268997192
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7502257386461283
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1150577151298522
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3887597545504824
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6684940560817718
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.536942481994629,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5324382399982877,
                "rejected_mean_error": 2.89299640083313,
                "gap_rejected_minus_accepted": 1.3605581608348423
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0598124861717224,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3880252193743035,
                "rejected_mean_error": 2.5081084330622763,
                "gap_rejected_minus_accepted": 1.1200832136879728
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6195600032806396,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1150577151298522,
                "rejected_mean_error": 2.221930397033691,
                "gap_rejected_minus_accepted": 1.106872681903839
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0775310695171356,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7515391707420349,
                "rejected_mean_error": 1.974798089284907,
                "gap_rejected_minus_accepted": 1.2232589185428722
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.547271990776062,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5500858318805695,
                "rejected_mean_error": 2.9548289299011232,
                "gap_rejected_minus_accepted": 1.4047430980205537
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.079927682876587,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4054401202954072,
                "rejected_mean_error": 2.5368687765938893,
                "gap_rejected_minus_accepted": 1.131428656298482
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.623271882534027,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1327942192554474,
                "rejected_mean_error": 2.2483260641098024,
                "gap_rejected_minus_accepted": 1.115531844854355
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1129688918590546,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7629882272273775,
                "rejected_mean_error": 2.0030576315793125,
                "gap_rejected_minus_accepted": 1.2400694043519351
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9868687549921948,
            "spearman": 0.9816169705785766,
            "auroc_top30_bad": 0.986888380952381,
            "mae": 0.0943207498252159,
            "mse": 0.018297961354976088,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7201376574053192,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06911832481622696
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18670869189500808
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5386066410005093
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9423608592311541
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
            "pearson": 0.9862442478948746,
            "spearman": 0.9848249554079715,
            "auroc_top30_worst": 0.9948647619047619,
            "pairwise_seed_ranking": 0.9384,
            "predicted_best_mean_error": 1.7595791444778441,
            "seed0_mean_error": 1.8668941221237183,
            "random_seed_mean_error": 1.8321932954788207,
            "oracle_best_mean_error": 1.7580343310832978,
            "improvement_over_seed0": 0.10731497764587417,
            "gap_to_oracle": 0.0015448133945463738,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8676287589073182
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1742125652157342
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.452939225101471
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.632959389419698
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8333799670696258
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.480005764961243,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7426126144727072,
                "rejected_mean_error": 2.6502861404418945,
                "gap_rejected_minus_accepted": 0.9076735259691873
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.153206765651703,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.63251323016756,
                "rejected_mean_error": 2.434696684249293,
                "gap_rejected_minus_accepted": 0.802183454081733
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7974482774734497,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.452939225101471,
                "rejected_mean_error": 2.2138207090377806,
                "gap_rejected_minus_accepted": 0.7608814839363096
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4693802893161774,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1752708771358282,
                "rejected_mean_error": 2.053217902127554,
                "gap_rejected_minus_accepted": 0.8779470249917258
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.598430895805359,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7685227160983616,
                "rejected_mean_error": 2.752236776351929,
                "gap_rejected_minus_accepted": 0.9837140602535672
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.210862398147583,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6468975033989564,
                "rejected_mean_error": 2.5198999586559476,
                "gap_rejected_minus_accepted": 0.8730024552569913
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.809815764427185,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4643302812576293,
                "rejected_mean_error": 2.269457962989807,
                "gap_rejected_minus_accepted": 0.8051276817321777
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4773157238960266,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1863620262297372,
                "rejected_mean_error": 2.09616429346768,
                "gap_rejected_minus_accepted": 0.9098022672379427
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9909480408080436,
            "spearman": 0.98650666193595,
            "auroc_top30_bad": 0.9925505952380953,
            "mae": 0.10690325604496502,
            "mse": 0.02502373399045228,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8792808238985867,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.058910690695047375
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20862042739987374
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7039144476652145
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0837165778477986
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
            "pearson": 0.9893995588922386,
            "spearman": 0.9851967101523003,
            "auroc_top30_worst": 0.9940857142857142,
            "pairwise_seed_ranking": 0.892,
            "predicted_best_mean_error": 2.2447601148486136,
            "seed0_mean_error": 2.3266324162483216,
            "random_seed_mean_error": 2.3179259487986563,
            "oracle_best_mean_error": 2.2414105245471,
            "improvement_over_seed0": 0.08187230139970803,
            "gap_to_oracle": 0.0033495903015134942,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2940966069698334
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4827873616218568
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6587557880878447
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8638390437761942
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.3207210887670517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.9188316345214846,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 2.094321572913064,
                "rejected_mean_error": 4.358316731452942,
                "gap_rejected_minus_accepted": 2.263995158539878
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.6791948080062866,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8638390437761942,
                "rejected_mean_error": 3.6913672237396242,
                "gap_rejected_minus_accepted": 1.82752817996343
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.931734561920166,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6587557880878447,
                "rejected_mean_error": 2.9826863894462585,
                "gap_rejected_minus_accepted": 1.3239306013584138
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6108584702014923,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4827873616218568,
                "rejected_mean_error": 2.600032331148783,
                "gap_rejected_minus_accepted": 1.1172449695269264
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.895966053009033,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 2.1021911515129936,
                "rejected_mean_error": 4.346603798866272,
                "gap_rejected_minus_accepted": 2.244412647353278
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.6641497015953064,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.874155740737915,
                "rejected_mean_error": 3.684062442779541,
                "gap_rejected_minus_accepted": 1.809906702041626
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9269508123397827,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.673662040233612,
                "rejected_mean_error": 2.979602792263031,
                "gap_rejected_minus_accepted": 1.305940752029419
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.626318335533142,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4977436900138854,
                "rejected_mean_error": 2.602928658326467,
                "gap_rejected_minus_accepted": 1.1051849683125816
              }
            ]
          }
        }
      }
    },
    {
      "variant": "heteroscedastic_head",
      "feature_mode": "M4_seed_relative",
      "model_kind": "hetero",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 160,
      "best_calib_loss": 0.01132895052433014,
      "train_time_sec": 56.56343173980713,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997732635295288,
            "spearman": 0.9989221790896966,
            "auroc_top30_bad": 0.9998736190476191,
            "mae": 0.01379827236449346,
            "mse": 0.00042873133434927213,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.997,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7604431028405704,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00258338788151741
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17367271980643273
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4778358371764421
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8172488168895244
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
            "pearson": 0.9998274416088183,
            "spearman": 0.9997157360206291,
            "auroc_top30_worst": 0.9998664761904762,
            "pairwise_seed_ranking": 0.9648,
            "predicted_best_mean_error": 1.6854259830415248,
            "seed0_mean_error": 1.7593383036255836,
            "random_seed_mean_error": 1.748514448583126,
            "oracle_best_mean_error": 1.6850638110637666,
            "improvement_over_seed0": 0.07391232058405883,
            "gap_to_oracle": 0.00036217197775822996,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.608547981441021
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.847004002213478
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1103014842152596
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3366850798368455
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7487053180277348
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8644605398178125,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4976224539081255,
                "rejected_mean_error": 4.008451095104218,
                "gap_rejected_minus_accepted": 2.5108286411960923
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9815132021903992,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3366850798368455,
                "rejected_mean_error": 2.984766032600403,
                "gap_rejected_minus_accepted": 1.6480809527635574
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5910513997077942,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1103014842152596,
                "rejected_mean_error": 2.38710915184021,
                "gap_rejected_minus_accepted": 1.2768076676249502
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1514872014522552,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.847004002213478,
                "rejected_mean_error": 2.0492724232991537,
                "gap_rejected_minus_accepted": 1.2022684210856758
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8729698419570924,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5080162266227934,
                "rejected_mean_error": 4.021236996650696,
                "gap_rejected_minus_accepted": 2.513220770027903
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9997827112674713,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3469774175484974,
                "rejected_mean_error": 2.9964209618568423,
                "gap_rejected_minus_accepted": 1.6494435443083448
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.599754512310028,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1168898319005967,
                "rejected_mean_error": 2.401786775350571,
                "gap_rejected_minus_accepted": 1.2848969434499742
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1613519191741943,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8505425856113434,
                "rejected_mean_error": 2.0622702096303303,
                "gap_rejected_minus_accepted": 1.211727624018987
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9841719511909719,
            "spearman": 0.9754525217749218,
            "auroc_top30_bad": 0.9959520000000001,
            "mae": 0.10949071959899738,
            "mse": 0.02483876197395407,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.96,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6967562087820977,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11675166296958923
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1914724713563919
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.42526921478509905
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8039094419558843
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
            "pearson": 0.9834254654068291,
            "spearman": 0.9884417400587138,
            "auroc_top30_worst": 0.9908510476190476,
            "pairwise_seed_ranking": 0.9428,
            "predicted_best_mean_error": 1.58919113779068,
            "seed0_mean_error": 1.6905601416826248,
            "random_seed_mean_error": 1.6723020417690277,
            "oracle_best_mean_error": 1.5885274814367294,
            "improvement_over_seed0": 0.10136900389194481,
            "gap_to_oracle": 0.0006636563539506035,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4684336347579956
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.77417159309754
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1145008406639099
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3857928274918212
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6684940560817718
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5681522607803347,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5340749706162347,
                "rejected_mean_error": 2.8782658252716065,
                "gap_rejected_minus_accepted": 1.3441908546553718
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1170806288719177,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3850624519961876,
                "rejected_mean_error": 2.516977803775678,
                "gap_rejected_minus_accepted": 1.1319153517794902
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6864356994628906,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1145008406639099,
                "rejected_mean_error": 2.222487271499634,
                "gap_rejected_minus_accepted": 1.1079864308357241
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1428940892219543,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7751431819349052,
                "rejected_mean_error": 1.9669132915225074,
                "gap_rejected_minus_accepted": 1.191770109587602
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6052939653396607,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5534097503291235,
                "rejected_mean_error": 2.9249136638641358,
                "gap_rejected_minus_accepted": 1.3715039135350122
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.152764081954956,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3998299947078214,
                "rejected_mean_error": 2.553521054131644,
                "gap_rejected_minus_accepted": 1.1536910594238226
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.699389100074768,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1315272648334502,
                "rejected_mean_error": 2.249593018531799,
                "gap_rejected_minus_accepted": 1.118065753698349
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1947115063667297,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7856286172828977,
                "rejected_mean_error": 1.995430120491089,
                "gap_rejected_minus_accepted": 1.2098015032081912
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9816697302937074,
            "spearman": 0.9789025028253333,
            "auroc_top30_bad": 0.9887565714285714,
            "mae": 0.11490995521768928,
            "mse": 0.027263695430609237,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7460943538934266,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08144523060321808
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17747217522859574
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5402321901261806
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.94476365985473
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
            "pearson": 0.9602028314236922,
            "spearman": 0.9683542632667286,
            "auroc_top30_worst": 0.9813150476190476,
            "pairwise_seed_ranking": 0.9352,
            "predicted_best_mean_error": 1.7603661839962006,
            "seed0_mean_error": 1.8668941221237183,
            "random_seed_mean_error": 1.8321932954788207,
            "oracle_best_mean_error": 1.7580343310832978,
            "improvement_over_seed0": 0.10652793812751771,
            "gap_to_oracle": 0.002331852912902832,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8945832204818726
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1793634056662903
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4537369641304017
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6393313333551005
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8333799670696258
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.645041918754578,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.745793720404307,
                "rejected_mean_error": 2.621656187057495,
                "gap_rejected_minus_accepted": 0.875862466653188
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1657946705818176,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6387937185349561,
                "rejected_mean_error": 2.41589535006319,
                "gap_rejected_minus_accepted": 0.7771016315282337
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.887881100177765,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4537369641304017,
                "rejected_mean_error": 2.21302297000885,
                "gap_rejected_minus_accepted": 0.7592860058784485
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.48783677816391,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1805290808312048,
                "rejected_mean_error": 2.0514614264000697,
                "gap_rejected_minus_accepted": 0.8709323455688649
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7999492645263673,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7718852933247884,
                "rejected_mean_error": 2.721973581314087,
                "gap_rejected_minus_accepted": 0.9500882879892985
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2002830505371094,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6556013006577517,
                "rejected_mean_error": 2.4940648779036505,
                "gap_rejected_minus_accepted": 0.8384635772458988
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.91116064786911,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4712304544448853,
                "rejected_mean_error": 2.262557789802551,
                "gap_rejected_minus_accepted": 0.7913273353576658
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5094795227050781,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1926435705215213,
                "rejected_mean_error": 2.0940480512731217,
                "gap_rejected_minus_accepted": 0.9014044807516004
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9938945891920362,
            "spearman": 0.9885857655098194,
            "auroc_top30_bad": 0.9923892857142858,
            "mae": 0.09021690421155654,
            "mse": 0.016473560092378284,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.995,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9239952035631052,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06441435240209102
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1993367760181427
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7028442744016647
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.084373387893041
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
            "pearson": 0.9916036778562385,
            "spearman": 0.9864547224547225,
            "auroc_top30_worst": 0.9972,
            "pairwise_seed_ranking": 0.9015,
            "predicted_best_mean_error": 2.24300469070673,
            "seed0_mean_error": 2.3266324162483216,
            "random_seed_mean_error": 2.3179259487986563,
            "oracle_best_mean_error": 2.2414105245471,
            "improvement_over_seed0": 0.08362772554159159,
            "gap_to_oracle": 0.0015941661596299284,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2986923444271088
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4841381869316101
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.659809246301651
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8639478335380555
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.3207210887670517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.9542521238327026,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 2.094260543849733,
                "rejected_mean_error": 4.358865993022919,
                "gap_rejected_minus_accepted": 2.2646054491731857
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7068504095077515,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8639478335380555,
                "rejected_mean_error": 3.6910408544540405,
                "gap_rejected_minus_accepted": 1.827093020915985
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.0841137170791626,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.659809246301651,
                "rejected_mean_error": 2.9816329312324523,
                "gap_rejected_minus_accepted": 1.3218236849308014
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7178093791007996,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4841381869316101,
                "rejected_mean_error": 2.599582056045532,
                "gap_rejected_minus_accepted": 1.115443869113922
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.9482935428619386,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 2.1021911515129936,
                "rejected_mean_error": 4.346603798866272,
                "gap_rejected_minus_accepted": 2.244412647353278
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.708908438682556,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.872049887975057,
                "rejected_mean_error": 3.690380001068115,
                "gap_rejected_minus_accepted": 1.8183301130930583
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.0674408674240112,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6760885953903197,
                "rejected_mean_error": 2.977176237106323,
                "gap_rejected_minus_accepted": 1.3010876417160033
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7419149577617645,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.5073853349685669,
                "rejected_mean_error": 2.5997147766749062,
                "gap_rejected_minus_accepted": 1.0923294417063394
              }
            ]
          }
        }
      }
    },
    {
      "variant": "heteroscedastic_simvla_focused",
      "feature_mode": "M4_seed_relative",
      "model_kind": "hetero",
      "train_setting": "simvla_focused",
      "train_rows": 10000,
      "input_dim": 1526,
      "best_epoch": 147,
      "best_calib_loss": 0.009461717680096626,
      "train_time_sec": 56.745667695999146,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997305386679608,
            "spearman": 0.9988826246621585,
            "auroc_top30_bad": 0.9997996666666666,
            "mae": 0.02389382505462272,
            "mse": 0.0009596960342520316,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7531156986356822,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.002099292680621147
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17357230127453804
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47783917482197286
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8172833655218283
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
            "pearson": 0.9997060031636301,
            "spearman": 0.9995228154929012,
            "auroc_top30_worst": 0.9996542857142857,
            "pairwise_seed_ranking": 0.9618,
            "predicted_best_mean_error": 1.6854764601290226,
            "seed0_mean_error": 1.7593383036255836,
            "random_seed_mean_error": 1.748514448583126,
            "oracle_best_mean_error": 1.6850638110637666,
            "improvement_over_seed0": 0.073861843496561,
            "gap_to_oracle": 0.0004126490652560655,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.608864783346653
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8469374387025833
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1103142193436624
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.336758540892601
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7487053180277348
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8436170339584352,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4976203420493337,
                "rejected_mean_error": 4.0084701018333435,
                "gap_rejected_minus_accepted": 2.51084975978401
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.975319653749466,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.336758540892601,
                "rejected_mean_error": 2.984545649433136,
                "gap_rejected_minus_accepted": 1.647787108540535
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.553274154663086,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1103142193436624,
                "rejected_mean_error": 2.3870964167118074,
                "gap_rejected_minus_accepted": 1.276782197368145
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.12470543384552,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8469374387025833,
                "rejected_mean_error": 2.0492946111361188,
                "gap_rejected_minus_accepted": 1.2023571724335356
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8409692287445076,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5080162266227934,
                "rejected_mean_error": 4.021236996650696,
                "gap_rejected_minus_accepted": 2.513220770027903
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.983077496290207,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.346985999504725,
                "rejected_mean_error": 2.996395215988159,
                "gap_rejected_minus_accepted": 1.649409216483434
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5617907643318176,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1167931777238846,
                "rejected_mean_error": 2.401883429527283,
                "gap_rejected_minus_accepted": 1.2850902518033982
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1326250731945038,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8506355001926422,
                "rejected_mean_error": 2.062239238103231,
                "gap_rejected_minus_accepted": 1.2116037379105886
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9856851265374567,
            "spearman": 0.9855148367674639,
            "auroc_top30_bad": 0.9971177142857143,
            "mae": 0.0993234521992039,
            "mse": 0.02106725487233059,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7277251049792933,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05713835892081261
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1703101969242096
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.42316828523874284
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8016303919553757
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
            "pearson": 0.9719074045543897,
            "spearman": 0.9861826696849086,
            "auroc_top30_worst": 0.9905005714285714,
            "pairwise_seed_ranking": 0.926,
            "predicted_best_mean_error": 1.5892812842130661,
            "seed0_mean_error": 1.6905601416826248,
            "random_seed_mean_error": 1.6723020417690277,
            "oracle_best_mean_error": 1.5885274814367294,
            "improvement_over_seed0": 0.10127885746955867,
            "gap_to_oracle": 0.0007538027763367428,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4692269253730774
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7715456082652776
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1142080891609192
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3875298799355147
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6684940560817718
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6042024612426773,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5422019574377273,
                "rejected_mean_error": 2.8051229438781737,
                "gap_rejected_minus_accepted": 1.2629209864404465
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.165326774120331,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3865706988688848,
                "rejected_mean_error": 2.5124627005177946,
                "gap_rejected_minus_accepted": 1.1258920016489098
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7157232761383057,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1142080891609192,
                "rejected_mean_error": 2.2227800230026244,
                "gap_rejected_minus_accepted": 1.1085719338417053
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1414403319358826,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7729219954234724,
                "rejected_mean_error": 1.9676552673795815,
                "gap_rejected_minus_accepted": 1.194733271956109
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6462572336196897,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5575712417231666,
                "rejected_mean_error": 2.887460241317749,
                "gap_rejected_minus_accepted": 1.3298889995945822
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.207502543926239,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4016238165730461,
                "rejected_mean_error": 2.5481965352618503,
                "gap_rejected_minus_accepted": 1.1465727186888042
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7452038526535034,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1307705080509185,
                "rejected_mean_error": 2.250349775314331,
                "gap_rejected_minus_accepted": 1.1195792672634124
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.179240882396698,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7862960265742408,
                "rejected_mean_error": 1.9952052713715456,
                "gap_rejected_minus_accepted": 1.2089092447973049
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9788075981761778,
            "spearman": 0.9775764774532953,
            "auroc_top30_bad": 0.9868510476190475,
            "mae": 0.11839053949974478,
            "mse": 0.032763564287845034,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7654889948756024,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0591652889251709
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1728917529940605
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5467488837659359
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9465216253240903
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
            "pearson": 0.9461888381324685,
            "spearman": 0.9556923020710167,
            "auroc_top30_worst": 0.9684297142857143,
            "pairwise_seed_ranking": 0.9208,
            "predicted_best_mean_error": 1.761561069250107,
            "seed0_mean_error": 1.8668941221237183,
            "random_seed_mean_error": 1.8321932954788207,
            "oracle_best_mean_error": 1.7580343310832978,
            "improvement_over_seed0": 0.10533305287361139,
            "gap_to_oracle": 0.0035267381668091513,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8907807745933533
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1918083009047387
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4565241963386535
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6432691556431338
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8333799670696258
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.690772390365601,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7461956106291876,
                "rejected_mean_error": 2.6180391750335694,
                "gap_rejected_minus_accepted": 0.8718435644043818
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.174275755882263,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.642932356803369,
                "rejected_mean_error": 2.4035058802309126,
                "gap_rejected_minus_accepted": 0.7605735234275437
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8718794584274292,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4565241963386535,
                "rejected_mean_error": 2.2102357378005983,
                "gap_rejected_minus_accepted": 0.7537115414619449
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5141768753528595,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1926046777457093,
                "rejected_mean_error": 2.047427635755203,
                "gap_rejected_minus_accepted": 0.8548229580094937
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.81927604675293,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7718852933247884,
                "rejected_mean_error": 2.721973581314087,
                "gap_rejected_minus_accepted": 0.9500882879892985
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2083305716514587,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6604688868803137,
                "rejected_mean_error": 2.479616645782713,
                "gap_rejected_minus_accepted": 0.8191477589023994
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.890388309955597,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4697426404953002,
                "rejected_mean_error": 2.264045603752136,
                "gap_rejected_minus_accepted": 0.7943029632568359
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5424658954143524,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.2020497586992052,
                "rejected_mean_error": 2.0908791215662013,
                "gap_rejected_minus_accepted": 0.8888293628669961
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9904480071798939,
            "spearman": 0.9900914411491806,
            "auroc_top30_bad": 0.9923595238095237,
            "mae": 0.09962694787408691,
            "mse": 0.024084220455798267,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9357005217521953,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03714945636689663
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19555737733840942
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7035063464641571
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0829189371267955
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
            "pearson": 0.9791732214292509,
            "spearman": 0.9841217761217762,
            "auroc_top30_worst": 0.9967142857142858,
            "pairwise_seed_ranking": 0.9035,
            "predicted_best_mean_error": 2.243211270868778,
            "seed0_mean_error": 2.3266324162483216,
            "random_seed_mean_error": 2.3179259487986563,
            "oracle_best_mean_error": 2.2414105245471,
            "improvement_over_seed0": 0.08342114537954348,
            "gap_to_oracle": 0.0018007463216780373,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3038232243061065
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.486162661075592
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6574604668617248
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.871345218817393
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.3207210887670517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.8722190618515016,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 2.104510876999961,
                "rejected_mean_error": 4.266612994670868,
                "gap_rejected_minus_accepted": 2.1621021176709068
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.674823820590973,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.871345218817393,
                "rejected_mean_error": 3.668848698616028,
                "gap_rejected_minus_accepted": 1.797503479798635
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.061950445175171,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6574604668617248,
                "rejected_mean_error": 2.9839817106723787,
                "gap_rejected_minus_accepted": 1.326521243810654
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.7187551259994507,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.486162661075592,
                "rejected_mean_error": 2.5989072313308714,
                "gap_rejected_minus_accepted": 1.1127445702552794
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.8806719064712523,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 2.1153491629494563,
                "rejected_mean_error": 4.22818169593811,
                "gap_rejected_minus_accepted": 2.1128325329886537
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.62453830242157,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8768745295206706,
                "rejected_mean_error": 3.6759060764312745,
                "gap_rejected_minus_accepted": 1.799031546910604
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.060818910598755,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6747974789142608,
                "rejected_mean_error": 2.9784673535823822,
                "gap_rejected_minus_accepted": 1.3036698746681215
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.728789508342743,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.5116644024848938,
                "rejected_mean_error": 2.598288420836131,
                "gap_rejected_minus_accepted": 1.0866240183512372
              }
            ]
          }
        }
      }
    }
  ]
}
```
