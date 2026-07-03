# Stage 6 Experiments: holdout_libero_object

```json
{
  "split": "holdout_libero_object",
  "results": [
    {
      "variant": "action_only_baseline",
      "feature_mode": "A0_action_flat",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 70,
      "best_epoch": 68,
      "best_calib_loss": 0.08968953043222427,
      "train_time_sec": 16.914888858795166,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9000481894501575,
            "spearman": 0.8115578920627115,
            "auroc_top30_bad": 0.8808205238095238,
            "mae": 0.21516864623203874,
            "mse": 0.23149133617495937,
            "expert_lt_perturb_large": 0.985,
            "expert_lt_other_task": 0.529,
            "expert_lt_simvla_seed0": 0.978,
            "same_context_pred_std": 0.778264872696975,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5752051155418157
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.5622185401558876
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.717035526868701
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0139168863256773
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
            "pearson": 0.99874460652149,
            "spearman": 0.9962516579857964,
            "auroc_top30_worst": 0.9987586666666667,
            "pairwise_seed_ranking": 0.8541,
            "predicted_best_mean_error": 1.7089485592246056,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.08547583839297279,
            "gap_to_oracle": 0.007354511499404914,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7308737818598747
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8822598344087601
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0849555878520012
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3056709358135858
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.062153148651123,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899976939029165,
                "rejected_mean_error": 4.441001539707184,
                "gap_rejected_minus_accepted": 2.9510038458042676
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9879677295684814,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3056709358135858,
                "rejected_mean_error": 3.223379506492615,
                "gap_rejected_minus_accepted": 1.9177085706790291
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4857751727104187,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0849555878520012,
                "rejected_mean_error": 2.4852405691146853,
                "gap_rejected_minus_accepted": 1.400284981262684
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0680371522903442,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8822598344087601,
                "rejected_mean_error": 2.0860441598415376,
                "gap_rejected_minus_accepted": 1.2037843254327774
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0985556602478033,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.49171771834294,
                "rejected_mean_error": 4.518784511089325,
                "gap_rejected_minus_accepted": 3.0270667927463846
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9823845028877258,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3023498595952987,
                "rejected_mean_error": 3.270648011684418,
                "gap_rejected_minus_accepted": 1.9682981520891192
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4791232347488403,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0776337245106697,
                "rejected_mean_error": 2.511215070724487,
                "gap_rejected_minus_accepted": 1.4335813462138174
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0601653754711151,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8694086567163467,
                "rejected_mean_error": 2.102762977917989,
                "gap_rejected_minus_accepted": 1.2333543212016425
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8187225748677535,
            "spearman": 0.7158248247103871,
            "auroc_top30_bad": 0.7852967619047619,
            "mae": 0.45889376013875005,
            "mse": 0.4888751615137482,
            "expert_lt_perturb_large": 0.988,
            "expert_lt_other_task": 0.476,
            "expert_lt_simvla_seed0": 0.952,
            "same_context_pred_std": 0.9169422677308321,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5302662250399589
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6823012785673142
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7833036580204964
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.111979402867953
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
            "pearson": 0.8312832107205566,
            "spearman": 0.7547148479455027,
            "auroc_top30_worst": 0.8552106666666666,
            "pairwise_seed_ranking": 0.7812,
            "predicted_best_mean_error": 2.0081228021383284,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.09635820257663763,
            "gap_to_oracle": 0.01922757244110085,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.116944165468216
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2159259154055364
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4910143243312837
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6071212405779722
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.28104305267334,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8435191028118134,
                "rejected_mean_error": 4.207311311721802,
                "gap_rejected_minus_accepted": 2.3637922089099885
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.704388439655304,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.607100894350634,
                "rejected_mean_error": 3.4952695419232302,
                "gap_rejected_minus_accepted": 1.8881686475725963
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7611008286476135,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4910143243312837,
                "rejected_mean_error": 2.668782323074341,
                "gap_rejected_minus_accepted": 1.1777679987430572
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2052069306373596,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.2146062082566393,
                "rejected_mean_error": 2.368944676034351,
                "gap_rejected_minus_accepted": 1.1543384677777118
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.297116231918335,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8663247532314724,
                "rejected_mean_error": 4.247887268066406,
                "gap_rejected_minus_accepted": 2.3815625148349335
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7492408752441406,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6187681476062632,
                "rejected_mean_error": 3.546200120259845,
                "gap_rejected_minus_accepted": 1.9274319726535818
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8012652397155762,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5186108016967774,
                "rejected_mean_error": 2.6903512077331544,
                "gap_rejected_minus_accepted": 1.171740406036377
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.186683475971222,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1695352480525063,
                "rejected_mean_error": 2.4194627302215697,
                "gap_rejected_minus_accepted": 1.2499274821690634
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6262629071880883,
            "spearman": 0.5437379499477937,
            "auroc_top30_bad": 0.6576129523809524,
            "mae": 0.5211130581974983,
            "mse": 0.6966565896166379,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.488,
            "expert_lt_simvla_seed0": 0.972,
            "same_context_pred_std": 0.6705404044275924,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8459021203517914
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7912348584651947
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9259916263461113
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1254711721340815
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
            "pearson": 0.8305842428369958,
            "spearman": 0.7753051930273237,
            "auroc_top30_worst": 0.8426148571428571,
            "pairwise_seed_ranking": 0.7868,
            "predicted_best_mean_error": 1.5995966371297836,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.057546505331993014,
            "gap_to_oracle": 0.019699115633964537,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6307910251617431
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8945311388144126
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1360750840187073
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3470518679888264
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.113592505455017,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4737419287893507,
                "rejected_mean_error": 3.2060873489379884,
                "gap_rejected_minus_accepted": 1.7323454201486377
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7727437317371368,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.347046151932174,
                "rejected_mean_error": 2.544850939759812,
                "gap_rejected_minus_accepted": 1.197804787827638
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4033885598182678,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1360750840187073,
                "rejected_mean_error": 2.1578778575897215,
                "gap_rejected_minus_accepted": 1.0218027735710142
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9799093753099442,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8943343120641982,
                "rejected_mean_error": 1.8983926881848177,
                "gap_rejected_minus_accepted": 1.0040583761206194
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1718366146087646,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.476923782295651,
                "rejected_mean_error": 3.279117383956909,
                "gap_rejected_minus_accepted": 1.8021936016612583
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.835066020488739,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3358011656903965,
                "rejected_mean_error": 2.6109677401800004,
                "gap_rejected_minus_accepted": 1.275166574489604
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4501161575317383,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1141974053382873,
                "rejected_mean_error": 2.200088879585266,
                "gap_rejected_minus_accepted": 1.0858914742469787
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9546204656362534,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8570225503709581,
                "rejected_mean_error": 1.9267024863212503,
                "gap_rejected_minus_accepted": 1.0696799359502922
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.4957928460250225,
            "spearman": 0.3829202599419322,
            "auroc_top30_bad": 0.5697405714285714,
            "mae": 0.4890008652538061,
            "mse": 0.6699890552089486,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.488,
            "expert_lt_simvla_seed0": 0.992,
            "same_context_pred_std": 0.6350003040627684,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8464365108013153
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.044331127858162
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0443124338626861
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2584265179316203
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
            "pearson": 0.6739430548105185,
            "spearman": 0.5438473983023351,
            "auroc_top30_worst": 0.6849950476190476,
            "pairwise_seed_ranking": 0.7492,
            "predicted_best_mean_error": 1.6138793796300888,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.04787174832820895,
            "gap_to_oracle": 0.021855447649955728,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9263472511768341
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2964038387514079
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4773203211307526
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5842940416226763
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8977292060852051,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6333305233054691,
                "rejected_mean_error": 1.8981582584381103,
                "gap_rejected_minus_accepted": 0.26482773513264113
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7866886258125305,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5839507148830716,
                "rejected_mean_error": 1.886916297693222,
                "gap_rejected_minus_accepted": 0.3029655828101505
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5087588429450989,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4773203211307526,
                "rejected_mean_error": 1.8423062725067139,
                "gap_rejected_minus_accepted": 0.36498595137596124
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3282354176044464,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.2982273201782482,
                "rejected_mean_error": 1.7805992207125132,
                "gap_rejected_minus_accepted": 0.48237190053426504
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8916483640670776,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6368554690149095,
                "rejected_mean_error": 1.8858120584487914,
                "gap_rejected_minus_accepted": 0.24895658943388188
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7925669252872467,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5821112276398561,
                "rejected_mean_error": 1.8981425781098624,
                "gap_rejected_minus_accepted": 0.3160313504700063
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.522340178489685,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.462559820652008,
                "rejected_mean_error": 1.8609424352645874,
                "gap_rejected_minus_accepted": 0.3983826146125793
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3333453834056854,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.3023529213572305,
                "rejected_mean_error": 1.7828318071875342,
                "gap_rejected_minus_accepted": 0.48047888583030374
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
      "best_epoch": 109,
      "best_calib_loss": 0.03327767923474312,
      "train_time_sec": 21.649608612060547,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9986890043846486,
            "spearman": 0.9969164901392883,
            "auroc_top30_bad": 0.9993972857142857,
            "mae": 0.038899739058036356,
            "mse": 0.0029853599604510103,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8141352425789685,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03888923093676567
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19992061030268668
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6187663383215666
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9866963211993376
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
            "pearson": 0.9996338606201739,
            "spearman": 0.9990017858400475,
            "auroc_top30_worst": 0.9998100952380953,
            "pairwise_seed_ranking": 0.9311,
            "predicted_best_mean_error": 1.7040708274245262,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09035357019305224,
            "gap_to_oracle": 0.002476779699325471,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7227367836833
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8797143276929855
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0840263824820517
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051859272559483
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1321511030197158,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.489973513437642,
                "rejected_mean_error": 4.441219163894654,
                "gap_rejected_minus_accepted": 2.951245650457012
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0296343564987183,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051859272559483,
                "rejected_mean_error": 3.224834532165527,
                "gap_rejected_minus_accepted": 1.919648604909579
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5148146152496338,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0840263824820517,
                "rejected_mean_error": 2.4861697744846345,
                "gap_rejected_minus_accepted": 1.4021433920025828
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0830354690551758,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8797143276929855,
                "rejected_mean_error": 2.086892662080129,
                "gap_rejected_minus_accepted": 1.2071783343871436
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2026053428649903,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4916569997535811,
                "rejected_mean_error": 4.519330978393555,
                "gap_rejected_minus_accepted": 3.0276739786399736
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0336159467697144,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3020937540133795,
                "rejected_mean_error": 3.271416328430176,
                "gap_rejected_minus_accepted": 1.9693225744167964
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5135487914085388,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0766962624192238,
                "rejected_mean_error": 2.512152532815933,
                "gap_rejected_minus_accepted": 1.4354562703967093
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.077272742986679,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8676338502168656,
                "rejected_mean_error": 2.1033545800844826,
                "gap_rejected_minus_accepted": 1.2357207298676172
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9680763599458697,
            "spearman": 0.9570583396259137,
            "auroc_top30_bad": 0.9753881904761904,
            "mae": 0.22489439894258975,
            "mse": 0.09520492063180302,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8374732676041265,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11342184311151504
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22317860403060913
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6063076517701149
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0280047995011012
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
            "pearson": 0.9767494793250984,
            "spearman": 0.9686713184456439,
            "auroc_top30_worst": 0.9910308571428571,
            "pairwise_seed_ranking": 0.874,
            "predicted_best_mean_error": 1.99696462392807,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.10751638078689596,
            "gap_to_oracle": 0.00806939423084252,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6518214194774627
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9441498849445429
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2335121263027191
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5538761601455684
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.150960397720337,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8423752145502303,
                "rejected_mean_error": 4.21760630607605,
                "gap_rejected_minus_accepted": 2.3752310915258192
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.829689681529999,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5525199612214955,
                "rejected_mean_error": 3.6586635813545496,
                "gap_rejected_minus_accepted": 2.106143620133054
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8816596269607544,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2335121263027191,
                "rejected_mean_error": 2.926284521102905,
                "gap_rejected_minus_accepted": 1.692772394800186
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4517238438129425,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9441144804413707,
                "rejected_mean_error": 2.4593010376204547,
                "gap_rejected_minus_accepted": 1.5151865571790841
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.239423751831055,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.86634343041314,
                "rejected_mean_error": 4.247719173431396,
                "gap_rejected_minus_accepted": 2.381375743018256
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.92958402633667,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.560255371950527,
                "rejected_mean_error": 3.7198808987935386,
                "gap_rejected_minus_accepted": 2.1596255268430116
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9004234075546265,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2300172662734985,
                "rejected_mean_error": 2.978944743156433,
                "gap_rejected_minus_accepted": 1.7489274768829346
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4448252618312836,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9580082666306269,
                "rejected_mean_error": 2.4907258309145024,
                "gap_rejected_minus_accepted": 1.5327175642838755
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9672900316004255,
            "spearman": 0.9599050578572018,
            "auroc_top30_bad": 0.9688860952380952,
            "mae": 0.19026463743001223,
            "mse": 0.06437960584957275,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6717556486263443,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10815303719043731
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2221839498758316
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6385120008826256
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.045895267701149
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
            "pearson": 0.9771178657122174,
            "spearman": 0.971521073357487,
            "auroc_top30_worst": 0.969103238095238,
            "pairwise_seed_ranking": 0.86,
            "predicted_best_mean_error": 1.5860538923740386,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07108925008773803,
            "gap_to_oracle": 0.006156370878219519,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.42588798904418945
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6621311860970962
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0335016522407532
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3105309723155585
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6532058715820312,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4596901870833503,
                "rejected_mean_error": 3.3325530242919923,
                "gap_rejected_minus_accepted": 1.872862837208642
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8668005466461182,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3098709137360849,
                "rejected_mean_error": 2.656139112889957,
                "gap_rejected_minus_accepted": 1.346268199153872
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6398360133171082,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0335016522407532,
                "rejected_mean_error": 2.260451289367676,
                "gap_rejected_minus_accepted": 1.2269496371269226
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.05307537317276,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6634685597099816,
                "rejected_mean_error": 1.9755121977759273,
                "gap_rejected_minus_accepted": 1.3120436380659457
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7576774120330807,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4643141012721592,
                "rejected_mean_error": 3.392604513168335,
                "gap_rejected_minus_accepted": 1.9282904118961757
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8653481900691986,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3063948234134817,
                "rejected_mean_error": 2.6982532323352872,
                "gap_rejected_minus_accepted": 1.3918584089218056
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6495726704597473,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0253691115379333,
                "rejected_mean_error": 2.28891717338562,
                "gap_rejected_minus_accepted": 1.2635480618476869
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0553008615970612,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.6458986552934798,
                "rejected_mean_error": 1.9978297878714169,
                "gap_rejected_minus_accepted": 1.351931132577937
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9523077404326605,
            "spearman": 0.9425769301033817,
            "auroc_top30_bad": 0.955056761904762,
            "mae": 0.18750108400434257,
            "mse": 0.06580289635844704,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 0.98,
            "same_context_pred_std": 0.6317041612245735,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11703861367702484
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2590071686506271
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8005795890212059
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1444595225016276
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
            "pearson": 0.9031125275063189,
            "spearman": 0.9010878895922494,
            "auroc_top30_worst": 0.9271801904761905,
            "pairwise_seed_ranking": 0.8204,
            "predicted_best_mean_error": 1.6075789086818695,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.054172219276428235,
            "gap_to_oracle": 0.015554976701736445,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9000144515037537
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1340488210702553
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3755306877613067
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.524793333113829
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.126634693145752,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5936824844413333,
                "rejected_mean_error": 2.254990608215332,
                "gap_rejected_minus_accepted": 0.6613081237739988
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.904200553894043,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.524070185588289,
                "rejected_mean_error": 2.0661752623871874,
                "gap_rejected_minus_accepted": 0.5421050767988984
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6139450073242188,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3755306877613067,
                "rejected_mean_error": 1.9440959058761598,
                "gap_rejected_minus_accepted": 0.568565218114853
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4136789739131927,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1356954445092442,
                "rejected_mean_error": 1.834892152499491,
                "gap_rejected_minus_accepted": 0.6991967079902468
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1209909439086916,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5976836986011929,
                "rejected_mean_error": 2.2383579921722414,
                "gap_rejected_minus_accepted": 0.6406742935710485
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.939134955406189,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5335259389749822,
                "rejected_mean_error": 2.0423560539881387,
                "gap_rejected_minus_accepted": 0.5088301150131564
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6186895370483398,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.384863778591156,
                "rejected_mean_error": 1.9386384773254395,
                "gap_rejected_minus_accepted": 0.5537746987342835
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4082523584365845,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1287321921378848,
                "rejected_mean_error": 1.8413243523256027,
                "gap_rejected_minus_accepted": 0.7125921601877179
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
      "best_epoch": 95,
      "best_calib_loss": 0.011706523597240448,
      "train_time_sec": 51.221139430999756,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9995841307927145,
            "spearman": 0.9985251915035149,
            "auroc_top30_bad": 0.9996184285714286,
            "mae": 0.02268582043866627,
            "mse": 0.0009987050734161778,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8081176598497168,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00027046261727809904
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19976076132655143
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.61869039876163
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9864951786657175
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
            "pearson": 0.9996480176182547,
            "spearman": 0.9991706890387879,
            "auroc_top30_worst": 0.9996379047619047,
            "pairwise_seed_ranking": 0.9602,
            "predicted_best_mean_error": 1.7026057395339012,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09181865808367728,
            "gap_to_oracle": 0.0010116918087004212,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7226915786862373
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8791967880964279
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0839647102713585
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3052900057077408
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1427760601043713,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899899764524567,
                "rejected_mean_error": 4.441070996761322,
                "gap_rejected_minus_accepted": 2.9510810203088655
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0210540890693665,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3052900057077408,
                "rejected_mean_error": 3.22452229681015,
                "gap_rejected_minus_accepted": 1.9192322911024093
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.511379063129425,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0839647102713585,
                "rejected_mean_error": 2.486231446695328,
                "gap_rejected_minus_accepted": 1.4022667364239694
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0848629176616669,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8791967880964279,
                "rejected_mean_error": 2.0870651752789815,
                "gap_rejected_minus_accepted": 1.2078683871825535
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1839099884033204,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4917422084344758,
                "rejected_mean_error": 4.518564100265503,
                "gap_rejected_minus_accepted": 3.0268218918310272
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0247230529785156,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3021763175725938,
                "rejected_mean_error": 3.271168637752533,
                "gap_rejected_minus_accepted": 1.968992320179939
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4958140850067139,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0766231289505959,
                "rejected_mean_error": 2.5122256662845612,
                "gap_rejected_minus_accepted": 1.4356025373339654
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0806500017642975,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8664280973672867,
                "rejected_mean_error": 2.103756497701009,
                "gap_rejected_minus_accepted": 1.2373284003337224
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9918581008580007,
            "spearman": 0.9845610214374254,
            "auroc_top30_bad": 0.9932822857142858,
            "mae": 0.11289730654619634,
            "mse": 0.025316783439583053,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.964,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9383703374598633,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0941659470796585
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19833982539176942
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5844575280785561
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0190118537664414
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
            "pearson": 0.9919471346703895,
            "spearman": 0.9935876321200847,
            "auroc_top30_worst": 0.9979215238095238,
            "pairwise_seed_ranking": 0.9256,
            "predicted_best_mean_error": 1.9926551493406295,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11182585537433654,
            "gap_to_oracle": 0.0037599196434019433,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6231670114994049
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8652930984703394
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2241177392482758
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5536115925385754
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.173413562774658,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8428016737567054,
                "rejected_mean_error": 4.213768173217773,
                "gap_rejected_minus_accepted": 2.370966499461068
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8539748191833496,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5521894367362035,
                "rejected_mean_error": 3.6596530428328835,
                "gap_rejected_minus_accepted": 2.10746360609668
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8637389540672302,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2241177392482758,
                "rejected_mean_error": 2.9356789081573487,
                "gap_rejected_minus_accepted": 1.7115611689090728
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.261861264705658,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8666666752804583,
                "rejected_mean_error": 2.4851720760573444,
                "gap_rejected_minus_accepted": 1.6185054007768862
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.214750003814697,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8661772516038684,
                "rejected_mean_error": 4.249214782714843,
                "gap_rejected_minus_accepted": 2.383037531110975
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.92071270942688,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5588921289392972,
                "rejected_mean_error": 3.7239273502713157,
                "gap_rejected_minus_accepted": 2.1650352213320185
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8904756903648376,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2234393348693848,
                "rejected_mean_error": 2.985522674560547,
                "gap_rejected_minus_accepted": 1.7620833396911622
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3104986548423767,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8669613486244565,
                "rejected_mean_error": 2.5213993915262067,
                "gap_rejected_minus_accepted": 1.6544380429017502
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9931142533246936,
            "spearman": 0.9899665137165633,
            "auroc_top30_bad": 0.9926506666666668,
            "mae": 0.07999326845658943,
            "mse": 0.013144831280827314,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.964,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7947213400865631,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.042843345701694485
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1784853694677353
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6260792688727379
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0387120758295059
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
            "pearson": 0.9912708840249271,
            "spearman": 0.9911145353693027,
            "auroc_top30_worst": 0.9859169523809523,
            "pairwise_seed_ranking": 0.8932,
            "predicted_best_mean_error": 1.5867604256868362,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07038271677494046,
            "gap_to_oracle": 0.006862904191017094,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4114252314567566
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6527178027690985
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0236260939598083
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.304002724540259
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8396106958389287,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4596411175727844,
                "rejected_mean_error": 3.332994649887085,
                "gap_rejected_minus_accepted": 1.8733535323143005
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0418867468833923,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.303328882477454,
                "rejected_mean_error": 2.6757234045491813,
                "gap_rejected_minus_accepted": 1.3723945220717273
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7150967121124268,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0236260939598083,
                "rejected_mean_error": 2.2703268476486205,
                "gap_rejected_minus_accepted": 1.2467007536888122
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0961240828037262,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6540019599774394,
                "rejected_mean_error": 1.9786744664165736,
                "gap_rejected_minus_accepted": 1.3246725064391343
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.9583882093429565,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4644762629932828,
                "rejected_mean_error": 3.3911450576782225,
                "gap_rejected_minus_accepted": 1.9266687946849397
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.054350256919861,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2999590224123256,
                "rejected_mean_error": 2.717356324195862,
                "gap_rejected_minus_accepted": 1.4173973017835362
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7276000380516052,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.01331410074234,
                "rejected_mean_error": 2.300972184181213,
                "gap_rejected_minus_accepted": 1.2876580834388731
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0818795263767242,
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
            "pearson": 0.9907185023239476,
            "spearman": 0.9826228578327766,
            "auroc_top30_bad": 0.9818849523809524,
            "mae": 0.07764661177862435,
            "mse": 0.012311614343600298,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7330631346366214,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05522713887691498
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21598850150108337
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7827145929336548
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1371456363042196
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
            "pearson": 0.9777300506800631,
            "spearman": 0.9663521105613508,
            "auroc_top30_worst": 0.9676190476190477,
            "pairwise_seed_ranking": 0.916,
            "predicted_best_mean_error": 1.598580536365509,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.0631705915927887,
            "gap_to_oracle": 0.006556604385375975,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8436746151447296
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1003489487637312
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3583470736026764
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5202140179333656
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0656811237335204,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5937990523709191,
                "rejected_mean_error": 2.25394149684906,
                "gap_rejected_minus_accepted": 0.6601424444781407
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.897306889295578,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5199101309956964,
                "rejected_mean_error": 2.078628844346482,
                "gap_rejected_minus_accepted": 0.5587187133507858
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7260809540748596,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3583470736026764,
                "rejected_mean_error": 1.9612795200347901,
                "gap_rejected_minus_accepted": 0.6029324464321137
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4369242191314697,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1012943606978407,
                "rejected_mean_error": 1.8463836564834497,
                "gap_rejected_minus_accepted": 0.745089295785609
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0505422353744507,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5993640282418993,
                "rejected_mean_error": 2.223235025405884,
                "gap_rejected_minus_accepted": 0.6238709971639846
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8868105113506317,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5279226280788687,
                "rejected_mean_error": 2.0589881037908886,
                "gap_rejected_minus_accepted": 0.5310654757120199
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7346412539482117,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.368727153301239,
                "rejected_mean_error": 1.9547751026153564,
                "gap_rejected_minus_accepted": 0.5860479493141173
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4549427032470703,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1108840278216772,
                "rejected_mean_error": 1.8473373702503144,
                "gap_rejected_minus_accepted": 0.7364533424286372
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
      "best_epoch": 120,
      "best_calib_loss": 0.01145037543028593,
      "train_time_sec": 54.03317403793335,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997076145598845,
            "spearman": 0.9986494582406077,
            "auroc_top30_bad": 0.9997359523809525,
            "mae": 0.018316179943671795,
            "mse": 0.000676698527994937,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8071631174291604,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0010596794486045838
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1997750137269497
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6186291745394469
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9864278151015441
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
            "pearson": 0.9997458884417008,
            "spearman": 0.9991897389675701,
            "auroc_top30_worst": 0.9998537142857142,
            "pairwise_seed_ranking": 0.9632,
            "predicted_best_mean_error": 1.7023848095536231,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09203958806395529,
            "gap_to_oracle": 0.0007907618284224149,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7224774269461631
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8794264578580856
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0840901797175408
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051783138513564
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.155492949485779,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899307362172338,
                "rejected_mean_error": 4.441604158878326,
                "gap_rejected_minus_accepted": 2.9516734226610923
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0177422165870667,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051783138513564,
                "rejected_mean_error": 3.224857372379303,
                "gap_rejected_minus_accepted": 1.9196790585279466
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5039615035057068,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0840901797175408,
                "rejected_mean_error": 2.4861059772491454,
                "gap_rejected_minus_accepted": 1.4020157975316045
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0755141973495483,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8794264578580856,
                "rejected_mean_error": 2.086988618691762,
                "gap_rejected_minus_accepted": 1.2075621608336764
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2318535804748536,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491642521388001,
                "rejected_mean_error": 4.519461283683777,
                "gap_rejected_minus_accepted": 3.0278187622957757
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.019946873188019,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019957639773687,
                "rejected_mean_error": 3.271710298538208,
                "gap_rejected_minus_accepted": 1.9697145345608393
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5015884041786194,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0767802615761757,
                "rejected_mean_error": 2.512068533658981,
                "gap_rejected_minus_accepted": 1.4352882720828055
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0689741671085358,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8675586725473404,
                "rejected_mean_error": 2.103379639307658,
                "gap_rejected_minus_accepted": 1.2358209667603175
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9904193796326841,
            "spearman": 0.9817514745708846,
            "auroc_top30_bad": 0.9898552380952382,
            "mae": 0.11652018740495004,
            "mse": 0.025340469735596245,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8782292391684109,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08072170525789261
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20780168430805207
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.586306336081028
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0207791561524073
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
            "pearson": 0.9919274280106044,
            "spearman": 0.9889728031825941,
            "auroc_top30_worst": 0.9985919999999999,
            "pairwise_seed_ranking": 0.9336,
            "predicted_best_mean_error": 1.9926112941503524,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11186971056461359,
            "gap_to_oracle": 0.00371606445312489,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6269070279598236
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8719517706105342
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2285430938243866
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5505202900308537
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.036846685409547,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8420163301626842,
                "rejected_mean_error": 4.220836265563965,
                "gap_rejected_minus_accepted": 2.378819935401281
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7783055305480957,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5493864105694322,
                "rejected_mean_error": 3.668044210622867,
                "gap_rejected_minus_accepted": 2.118657800053435
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.767330288887024,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2285430938243866,
                "rejected_mean_error": 2.9312535535812376,
                "gap_rejected_minus_accepted": 1.702710459756851
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2234980165958405,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8732970670198861,
                "rejected_mean_error": 2.482957228016319,
                "gap_rejected_minus_accepted": 1.609660160996433
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.13493971824646,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8655182372199164,
                "rejected_mean_error": 4.25514591217041,
                "gap_rejected_minus_accepted": 2.3896276749504937
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.861549735069275,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5570837954148888,
                "rejected_mean_error": 3.729294943431067,
                "gap_rejected_minus_accepted": 2.172211148016178
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7763586640357971,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2247626695632934,
                "rejected_mean_error": 2.984199339866638,
                "gap_rejected_minus_accepted": 1.7594366703033448
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2083362340927124,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8700367723192487,
                "rejected_mean_error": 2.520363286217266,
                "gap_rejected_minus_accepted": 1.6503265138980172
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9892019555190347,
            "spearman": 0.9807872453045826,
            "auroc_top30_bad": 0.9797630476190476,
            "mae": 0.10480125826873736,
            "mse": 0.02195718164378303,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7447328851361438,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04489315229654312
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18985564820766448
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6304197318434716
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.042384348066648
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
            "pearson": 0.9868060576885263,
            "spearman": 0.9694343238619674,
            "auroc_top30_worst": 0.9589668571428571,
            "pairwise_seed_ranking": 0.9084,
            "predicted_best_mean_error": 1.5849684100151062,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07217473244667039,
            "gap_to_oracle": 0.0050708885192871644,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4111691529750824
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6559059994343
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0362161160469054
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3113636432298974
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.494133663177491,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.459015063656701,
                "rejected_mean_error": 3.338629135131836,
                "gap_rejected_minus_accepted": 1.879614071475135
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.919625848531723,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3109093380966717,
                "rejected_mean_error": 2.6530304751076255,
                "gap_rejected_minus_accepted": 1.3421211370109538
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.654233157634735,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0362161160469054,
                "rejected_mean_error": 2.2577368255615236,
                "gap_rejected_minus_accepted": 1.221520709514618
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.061540424823761,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6572878094146046,
                "rejected_mean_error": 1.977576845419954,
                "gap_rejected_minus_accepted": 1.3202890360053494
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.627932524681091,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4650840894381205,
                "rejected_mean_error": 3.3856746196746825,
                "gap_rejected_minus_accepted": 1.920590530236562
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9233414232730865,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3046800092579847,
                "rejected_mean_error": 2.7033432362571594,
                "gap_rejected_minus_accepted": 1.3986632269991748
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6748414039611816,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0288913559913635,
                "rejected_mean_error": 2.28539492893219,
                "gap_rejected_minus_accepted": 1.2565035729408265
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0428203344345093,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.6485171753262716,
                "rejected_mean_error": 1.9969476126732035,
                "gap_rejected_minus_accepted": 1.348430437346932
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9842535882079635,
            "spearman": 0.9784192578358598,
            "auroc_top30_bad": 0.9811078095238096,
            "mae": 0.10344133497600223,
            "mse": 0.021900383189920932,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6879466033981089,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07810456967353821
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2189815901517868
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7839389393806457
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1376459822972615
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
            "pearson": 0.9688564242282038,
            "spearman": 0.9566972092117009,
            "auroc_top30_worst": 0.9586422857142857,
            "pairwise_seed_ranking": 0.9092,
            "predicted_best_mean_error": 1.5974996016025542,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.0642515263557435,
            "gap_to_oracle": 0.0054756696224211865,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8451504843235016
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1023312808038332
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.361391943025589
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5213348748905065
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0592648506164553,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5947600790924497,
                "rejected_mean_error": 2.2452922563552855,
                "gap_rejected_minus_accepted": 0.6505321772628359
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8720471560955048,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5207371536479306,
                "rejected_mean_error": 2.0761530608795704,
                "gap_rejected_minus_accepted": 0.5554159072316398
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7101922631263733,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.361391943025589,
                "rejected_mean_error": 1.9582346506118775,
                "gap_rejected_minus_accepted": 0.5968427075862885
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3644540309906006,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1031103047509543,
                "rejected_mean_error": 1.845777049772004,
                "gap_rejected_minus_accepted": 0.7426667450210498
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.054368019104004,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6003666912184822,
                "rejected_mean_error": 2.2142110586166384,
                "gap_rejected_minus_accepted": 0.6138443673981562
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8759800791740417,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5277673047494122,
                "rejected_mean_error": 2.05944914287991,
                "gap_rejected_minus_accepted": 0.5316818381304977
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7239936590194702,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3734211077690124,
                "rejected_mean_error": 1.950081148147583,
                "gap_rejected_minus_accepted": 0.5766600403785707
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3611346185207367,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1119997548678564,
                "rejected_mean_error": 1.846961483598393,
                "gap_rejected_minus_accepted": 0.7349617287305366
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
      "best_epoch": 104,
      "best_calib_loss": 0.011554568074643612,
      "train_time_sec": 60.335283041000366,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994941402582034,
            "spearman": 0.9979776741681585,
            "auroc_top30_bad": 0.9993520476190475,
            "mae": 0.027085301012733726,
            "mse": 0.0013055122842407826,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8139941622934704,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0019243607372045517
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20007857882380486
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6187572772234678
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9869400355478127
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
            "pearson": 0.9995490850641529,
            "spearman": 0.9985668249906386,
            "auroc_top30_worst": 0.9995942857142858,
            "pairwise_seed_ranking": 0.9647,
            "predicted_best_mean_error": 1.7030223517417908,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.0914020458757876,
            "gap_to_oracle": 0.0014283040165901095,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7245407460331916
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8798575666189193
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0842194727778436
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3052788170735041
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.197749614715579,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899408831000327,
                "rejected_mean_error": 4.441512836933136,
                "gap_rejected_minus_accepted": 2.9515719538331027
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0516122579574585,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3052788170735041,
                "rejected_mean_error": 3.2245558627128603,
                "gap_rejected_minus_accepted": 1.9192770456393562
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5326685309410095,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0842194727778436,
                "rejected_mean_error": 2.485976684188843,
                "gap_rejected_minus_accepted": 1.4017572114109993
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0981160700321198,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8798575666189193,
                "rejected_mean_error": 2.0868449157714846,
                "gap_rejected_minus_accepted": 1.2069873491525653
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2539619684219367,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0698999762535095,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.302065108180046,
                "rejected_mean_error": 3.2715022659301756,
                "gap_rejected_minus_accepted": 1.9694371577501295
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.535054862499237,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0768505728840827,
                "rejected_mean_error": 2.511998222351074,
                "gap_rejected_minus_accepted": 1.4351476494669915
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0859736800193787,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8670634251832962,
                "rejected_mean_error": 2.103544721762339,
                "gap_rejected_minus_accepted": 1.236481296579043
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9899428334648588,
            "spearman": 0.9805423314231458,
            "auroc_top30_bad": 0.9946567619047619,
            "mae": 0.11314185913789497,
            "mse": 0.026687064831334307,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8839257997691393,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10789891874790192
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22745304358005525
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5869787660241127
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.018526737443606
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
            "pearson": 0.9955583618097592,
            "spearman": 0.9935696117565517,
            "auroc_top30_worst": 0.9999177142857143,
            "pairwise_seed_ranking": 0.9268,
            "predicted_best_mean_error": 1.9927052171230317,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.1117757875919343,
            "gap_to_oracle": 0.0038099874258041844,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6296152741909027
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8677738800835915
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.222180722951889
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5475141766673721
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.068378973007203,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8428834235668183,
                "rejected_mean_error": 4.213032424926758,
                "gap_rejected_minus_accepted": 2.3701490013599393
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8416879773139954,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.546229514489179,
                "rejected_mean_error": 3.6774947270036886,
                "gap_rejected_minus_accepted": 2.13126521251451
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.784369170665741,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.222180722951889,
                "rejected_mean_error": 2.9376159244537354,
                "gap_rejected_minus_accepted": 1.7154352015018464
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.177090972661972,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8689381896306912,
                "rejected_mean_error": 2.4844132884462207,
                "gap_rejected_minus_accepted": 1.6154750988155295
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.139669561386108,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.86610019048055,
                "rejected_mean_error": 4.249908332824707,
                "gap_rejected_minus_accepted": 2.383808142344157
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.921819567680359,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548569416617328,
                "rejected_mean_error": 3.7359048109205943,
                "gap_rejected_minus_accepted": 2.1810478692588617
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7809529304504395,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2205396680831908,
                "rejected_mean_error": 2.9884223413467406,
                "gap_rejected_minus_accepted": 1.7678826732635498
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1882701218128204,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.867253375431848,
                "rejected_mean_error": 2.521301008163289,
                "gap_rejected_minus_accepted": 1.6540476327314408
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9885456140887104,
            "spearman": 0.9815876905498981,
            "auroc_top30_bad": 0.9784830476190476,
            "mae": 0.1039018028536233,
            "mse": 0.022608540731929777,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7557054450200368,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06097551560401916
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18524472053050994
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6294238663077354
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0438459220488867
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
            "pearson": 0.9856510288681757,
            "spearman": 0.9790313378760565,
            "auroc_top30_worst": 0.9670582857142859,
            "pairwise_seed_ranking": 0.8956,
            "predicted_best_mean_error": 1.5860271649360658,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07111597752571086,
            "gap_to_oracle": 0.00612964344024669,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.39975051498413083
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.65428799448105
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0314667088508607
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3113798076537118
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.571315765380861,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.459661145793067,
                "rejected_mean_error": 3.332814395904541,
                "gap_rejected_minus_accepted": 1.873153250111474
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0003638565540314,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.310629454150144,
                "rejected_mean_error": 2.6538683385513844,
                "gap_rejected_minus_accepted": 1.3432388844012404
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6328925490379333,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0314667088508607,
                "rejected_mean_error": 2.2624862327575683,
                "gap_rejected_minus_accepted": 1.2310195239067077
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9954093247652054,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6556048654138852,
                "rejected_mean_error": 1.978139024152318,
                "gap_rejected_minus_accepted": 1.3225341587384327
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7286349534988403,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4650840894381205,
                "rejected_mean_error": 3.3856746196746825,
                "gap_rejected_minus_accepted": 1.920590530236562
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0181979537010193,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3052084410891813,
                "rejected_mean_error": 2.7017747163772583,
                "gap_rejected_minus_accepted": 1.396566275288077
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.636669397354126,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0179526944160462,
                "rejected_mean_error": 2.2963335905075075,
                "gap_rejected_minus_accepted": 1.2783808960914613
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9920246452093124,
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
            "pearson": 0.9810330184057886,
            "spearman": 0.9763527369651298,
            "auroc_top30_bad": 0.980455619047619,
            "mae": 0.11385938923385219,
            "mse": 0.02642986582453166,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6840251195782393,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0830416447520256
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22592207856178284
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7862651903152466
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1383523014704386
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
            "pearson": 0.964724080505996,
            "spearman": 0.9542641453210531,
            "auroc_top30_worst": 0.9630049523809524,
            "pairwise_seed_ranking": 0.8992,
            "predicted_best_mean_error": 1.5983132905960082,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06343783736228947,
            "gap_to_oracle": 0.006289358615875207,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8413697311878204
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1011135877133944
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3624485973834992
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5203009778057843
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0434732913970945,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5983007899655237,
                "rejected_mean_error": 2.2134258584976196,
                "gap_rejected_minus_accepted": 0.6151250685320959
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8761315643787384,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5198474075712796,
                "rejected_mean_error": 2.078816613831078,
                "gap_rejected_minus_accepted": 0.5589692062597986
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6388070583343506,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3624485973834992,
                "rejected_mean_error": 1.9571779962539673,
                "gap_rejected_minus_accepted": 0.594729398870468
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3464590013027191,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1023164756191424,
                "rejected_mean_error": 1.8460422242845518,
                "gap_rejected_minus_accepted": 0.7437257486654094
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.039391803741455,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6072737500402663,
                "rejected_mean_error": 2.152047529220581,
                "gap_rejected_minus_accepted": 0.5447737791803149
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8690488040447235,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.528368586206181,
                "rejected_mean_error": 2.0576643868098183,
                "gap_rejected_minus_accepted": 0.5292958006036372
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6437860131263733,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3749944891929626,
                "rejected_mean_error": 1.9485077667236328,
                "gap_rejected_minus_accepted": 0.5735132775306702
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3493479788303375,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.111446373992496,
                "rejected_mean_error": 1.847147916727525,
                "gap_rejected_minus_accepted": 0.7357015427350291
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
      "best_epoch": 120,
      "best_calib_loss": 0.011072713881731033,
      "train_time_sec": 42.00961256027222,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9999260450534465,
            "spearman": 0.9992544844071615,
            "auroc_top30_bad": 0.9999023809523809,
            "mae": 0.00989280416137708,
            "mse": 0.00018691679934608002,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8097860788278827,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00019051821529865264
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1995973285615444
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6185372411698103
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.986293015430371
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
            "pearson": 0.9999370004247601,
            "spearman": 0.9998602045304048,
            "auroc_top30_worst": 0.9999767619047619,
            "pairwise_seed_ranking": 0.9757,
            "predicted_best_mean_error": 1.7020305799841882,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09239381763339027,
            "gap_to_oracle": 0.0004365322589874321,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7210368183255196
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.87866714656353
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0837862924933435
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3050926523129145
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1506618738174446,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.489922976328267,
                "rejected_mean_error": 4.441673997879028,
                "gap_rejected_minus_accepted": 2.951751021550761
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.038052022457123,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3050926523129145,
                "rejected_mean_error": 3.225114356994629,
                "gap_rejected_minus_accepted": 1.9200217046817145
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.520631492137909,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0837862924933435,
                "rejected_mean_error": 2.486409864473343,
                "gap_rejected_minus_accepted": 1.4026235719799993
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0927367210388184,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.87866714656353,
                "rejected_mean_error": 2.087241722456614,
                "gap_rejected_minus_accepted": 1.2085745758930844
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.205993700027466,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.042540192604065,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019707630872726,
                "rejected_mean_error": 3.2717853012084963,
                "gap_rejected_minus_accepted": 1.9698145381212238
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5135903358459473,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0763718727231026,
                "rejected_mean_error": 2.5124769225120542,
                "gap_rejected_minus_accepted": 1.4361050497889516
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0878922641277313,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8663671995401383,
                "rejected_mean_error": 2.1037767969767254,
                "gap_rejected_minus_accepted": 1.237409597436587
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9906694783361396,
            "spearman": 0.9815023501314034,
            "auroc_top30_bad": 0.9885889523809523,
            "mae": 0.11251779077357714,
            "mse": 0.024613460372037203,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.880258516635002,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07705744636058807
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20928863949775695
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5867168248772621
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0206338271856308
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
            "pearson": 0.9938151617830236,
            "spearman": 0.9892340523737937,
            "auroc_top30_worst": 0.9997531428571428,
            "pairwise_seed_ranking": 0.9228,
            "predicted_best_mean_error": 1.992207842350006,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11227316236495999,
            "gap_to_oracle": 0.0033126126527784905,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.631594761133194
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8696033644179503
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2322077550411223
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.547533694964482
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.117966175079346,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8426250236034394,
                "rejected_mean_error": 4.215358024597168,
                "gap_rejected_minus_accepted": 2.372733000993729
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.77921462059021,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5457592400758982,
                "rejected_mean_error": 3.6789025452952036,
                "gap_rejected_minus_accepted": 2.1331433052193054
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.805702567100525,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2322077550411223,
                "rejected_mean_error": 2.927588892364502,
                "gap_rejected_minus_accepted": 1.6953811373233796
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2293601632118225,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8707618289671767,
                "rejected_mean_error": 2.4838041111651963,
                "gap_rejected_minus_accepted": 1.6130422821980197
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.205631065368652,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8664221413930258,
                "rejected_mean_error": 4.247010774612427,
                "gap_rejected_minus_accepted": 2.3805886332194013
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8453330397605896,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548569416617328,
                "rejected_mean_error": 3.7359048109205943,
                "gap_rejected_minus_accepted": 2.1810478692588617
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8045194745063782,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2321157894134522,
                "rejected_mean_error": 2.9768462200164794,
                "gap_rejected_minus_accepted": 1.7447304306030271
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2555455565452576,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8705015901535277,
                "rejected_mean_error": 2.5202066898345947,
                "gap_rejected_minus_accepted": 1.649705099681067
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.988868355033105,
            "spearman": 0.9805749464560946,
            "auroc_top30_bad": 0.9759710476190476,
            "mae": 0.10667440449811838,
            "mse": 0.023748270792087606,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.742626824478342,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03664750438928604
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18412271807193756
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6286571157813072
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0463910755395889
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
            "pearson": 0.986482427454613,
            "spearman": 0.9766297880510645,
            "auroc_top30_worst": 0.9653638095238095,
            "pairwise_seed_ranking": 0.9096,
            "predicted_best_mean_error": 1.5842525517940522,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07289059066772441,
            "gap_to_oracle": 0.004355030298233142,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.41749586415290835
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6548922163171645
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0311292637825011
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3114965741695372
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.524586415290833,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4591102761692472,
                "rejected_mean_error": 3.337772222518921,
                "gap_rejected_minus_accepted": 1.8786619463496737
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9623989462852478,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3108566517890963,
                "rejected_mean_error": 2.653188197376629,
                "gap_rejected_minus_accepted": 1.3423315455875326
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.642086923122406,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0311292637825011,
                "rejected_mean_error": 2.262823677825928,
                "gap_rejected_minus_accepted": 1.2316944140434267
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0648313760757446,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6560804419243298,
                "rejected_mean_error": 1.9779801602806328,
                "gap_rejected_minus_accepted": 1.321899718356303
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6619738101959225,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4650840894381205,
                "rejected_mean_error": 3.3856746196746825,
                "gap_rejected_minus_accepted": 1.920590530236562
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9640863239765167,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3061373409102945,
                "rejected_mean_error": 2.6990175057971286,
                "gap_rejected_minus_accepted": 1.392880164886834
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6610336303710938,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0231261086463928,
                "rejected_mean_error": 2.2911601762771605,
                "gap_rejected_minus_accepted": 1.2680340676307678
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0394870936870575,
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
            "pearson": 0.9867036392470426,
            "spearman": 0.9779124724024846,
            "auroc_top30_bad": 0.9796975238095238,
            "mae": 0.09951850335800118,
            "mse": 0.01883005006695341,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.696579558058223,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06684048396348953
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21626834630966185
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7851024291992188
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1393220830917359
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
            "pearson": 0.9575612965161383,
            "spearman": 0.9524304673474993,
            "auroc_top30_worst": 0.9607497142857143,
            "pairwise_seed_ranking": 0.9068,
            "predicted_best_mean_error": 1.5969863193035125,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06476480865478518,
            "gap_to_oracle": 0.004962387323379502,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8434595940113068
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1011422311839385
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3610886805057525
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5212466410800083
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.10048828125,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.600984284427431,
                "rejected_mean_error": 2.189274408340454,
                "gap_rejected_minus_accepted": 0.5882901239130232
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9069909751415253,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5209613631667296,
                "rejected_mean_error": 2.0754818649718554,
                "gap_rejected_minus_accepted": 0.5545205018051258
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6947347521781921,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3610886805057525,
                "rejected_mean_error": 1.9585379131317138,
                "gap_rejected_minus_accepted": 0.5974492326259613
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3695254623889923,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1022111387869802,
                "rejected_mean_error": 1.8460774115081022,
                "gap_rejected_minus_accepted": 0.743866272721122
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.081588864326477,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6084087846014234,
                "rejected_mean_error": 2.141832218170166,
                "gap_rejected_minus_accepted": 0.5334234335687424
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9026910662651062,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5274193366581106,
                "rejected_mean_error": 2.060482000547742,
                "gap_rejected_minus_accepted": 0.5330626638896316
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6995573043823242,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3725298838615418,
                "rejected_mean_error": 1.9509723720550538,
                "gap_rejected_minus_accepted": 0.578442488193512
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3682821989059448,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1118491954273648,
                "rejected_mean_error": 1.8470122068323553,
                "gap_rejected_minus_accepted": 0.7351630114049905
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
      "best_epoch": 119,
      "best_calib_loss": 0.010894420556724072,
      "train_time_sec": 55.92370915412903,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994717233125411,
            "spearman": 0.9988572484406779,
            "auroc_top30_bad": 0.9998119047619048,
            "mae": 0.027563675586005497,
            "mse": 0.0024853638201623313,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7909367126306804,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0003986814171075821
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1996829391658306
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.618662318894267
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9864072946051756
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
            "pearson": 0.9992725027449675,
            "spearman": 0.9993183121327,
            "auroc_top30_worst": 0.9997752380952382,
            "pairwise_seed_ranking": 0.9644,
            "predicted_best_mean_error": 1.7024821221828461,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09194227543473232,
            "gap_to_oracle": 0.0008880744576453825,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.721872347176075
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8791380563497543
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0840167390704154
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.305228193561236
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1000993013381968,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.489957872649034,
                "rejected_mean_error": 4.441359930992126,
                "gap_rejected_minus_accepted": 2.9514020583430924
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9929618835449219,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.305228193561236,
                "rejected_mean_error": 3.224707733249664,
                "gap_rejected_minus_accepted": 1.919479539688428
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5009857416152954,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0840167390704154,
                "rejected_mean_error": 2.486179417896271,
                "gap_rejected_minus_accepted": 1.4021626788258554
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0782117247581482,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8791380563497543,
                "rejected_mean_error": 2.087084752527873,
                "gap_rejected_minus_accepted": 1.2079466961781185
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1542115449905395,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491642521388001,
                "rejected_mean_error": 4.519461283683777,
                "gap_rejected_minus_accepted": 3.0278187622957757
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9916147589683533,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.302245419859886,
                "rejected_mean_error": 3.2709613308906555,
                "gap_rejected_minus_accepted": 1.9687159110307695
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4919344782829285,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0769672375321389,
                "rejected_mean_error": 2.5118815577030182,
                "gap_rejected_minus_accepted": 1.4349143201708794
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.077654391527176,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8667670537233353,
                "rejected_mean_error": 2.103643512248993,
                "gap_rejected_minus_accepted": 1.2368764585256575
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9911717391291768,
            "spearman": 0.9829840995460654,
            "auroc_top30_bad": 0.9903649523809523,
            "mae": 0.11428989896459309,
            "mse": 0.02301188219539081,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8668677740265052,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08932233214378357
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20251721796989441
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5880030792832375
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.02009321966966
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
            "pearson": 0.9929185832908942,
            "spearman": 0.9881495496637118,
            "auroc_top30_worst": 0.9992868571428571,
            "pairwise_seed_ranking": 0.9308,
            "predicted_best_mean_error": 1.992465193748474,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11201581096649194,
            "gap_to_oracle": 0.0035699640512465436,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6278644301891327
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8708837241507493
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.231122076177597
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.549318220410774
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.070854949951173,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8418221654627058,
                "rejected_mean_error": 4.222583747863769,
                "gap_rejected_minus_accepted": 2.3807615824010635
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7798080444335938,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5480435648684567,
                "rejected_mean_error": 3.672064167242081,
                "gap_rejected_minus_accepted": 2.124020602373624
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7910626530647278,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.231122076177597,
                "rejected_mean_error": 2.9286745712280275,
                "gap_rejected_minus_accepted": 1.6975524950504306
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2136452496051788,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8723322441593145,
                "rejected_mean_error": 2.4832795220988793,
                "gap_rejected_minus_accepted": 1.6109472779395646
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.139067888259888,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8649051147037081,
                "rejected_mean_error": 4.260664014816284,
                "gap_rejected_minus_accepted": 2.3957589001125763
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.842150568962097,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548569416617328,
                "rejected_mean_error": 3.7359048109205943,
                "gap_rejected_minus_accepted": 2.1810478692588617
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8003877401351929,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2339226303100586,
                "rejected_mean_error": 2.975039379119873,
                "gap_rejected_minus_accepted": 1.7411167488098145
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2163513600826263,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8673294177131047,
                "rejected_mean_error": 2.5212753896407265,
                "gap_rejected_minus_accepted": 1.6539459719276217
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9877525328787148,
            "spearman": 0.9819012893494059,
            "auroc_top30_bad": 0.982544380952381,
            "mae": 0.12314508110300296,
            "mse": 0.030512507843135417,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7253152109493102,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04175995886325836
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18772934889793397
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6294725996375083
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.042243328754107
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
            "pearson": 0.9861594996307073,
            "spearman": 0.9745769350252386,
            "auroc_top30_worst": 0.9697645714285714,
            "pairwise_seed_ranking": 0.894,
            "predicted_best_mean_error": 1.5860869413614274,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07105620110034927,
            "gap_to_oracle": 0.006189419865608281,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4146583845615387
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.656132236505166
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0342075907707213
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.309160167283849
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3932981014251724,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4595278876092699,
                "rejected_mean_error": 3.334013719558716,
                "gap_rejected_minus_accepted": 1.874485831949446
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8883107006549835,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3087254124619028,
                "rejected_mean_error": 2.659568297215544,
                "gap_rejected_minus_accepted": 1.3508428847536411
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6532220840454102,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0342075907707213,
                "rejected_mean_error": 2.2597453508377074,
                "gap_rejected_minus_accepted": 1.2255377600669861
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1175424456596375,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6573946095122316,
                "rejected_mean_error": 1.977541169400149,
                "gap_rejected_minus_accepted": 1.3201465598879174
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5004357814788816,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.46417668528027,
                "rejected_mean_error": 3.393841257095337,
                "gap_rejected_minus_accepted": 1.9296645718150671
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9043332934379578,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3031962520298472,
                "rejected_mean_error": 2.707747404537504,
                "gap_rejected_minus_accepted": 1.4045511525076566
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6655879020690918,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.024927442073822,
                "rejected_mean_error": 2.2893588428497313,
                "gap_rejected_minus_accepted": 1.2644314007759094
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1029143035411835,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.6442655022182162,
                "rejected_mean_error": 1.9983799945224414,
                "gap_rejected_minus_accepted": 1.3541144923042252
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.985037154458422,
            "spearman": 0.9800594959511725,
            "auroc_top30_bad": 0.9839809523809525,
            "mae": 0.10903975937763855,
            "mse": 0.023237832356339364,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6782157902114097,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07305762106180191
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22487686655521394
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7835030833244324
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1378792974472045
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
            "pearson": 0.9676940192161213,
            "spearman": 0.9626734680790197,
            "auroc_top30_worst": 0.9704350476190476,
            "pairwise_seed_ranking": 0.9084,
            "predicted_best_mean_error": 1.598143383860588,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06360774409770964,
            "gap_to_oracle": 0.00611945188045504,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8446013634204864
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1052115136423173
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3588387424945831
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.518734051125136
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.02937490940094,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5968327590359581,
                "rejected_mean_error": 2.2266381368637087,
                "gap_rejected_minus_accepted": 0.6298053778277506
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8648052513599396,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5181785341324394,
                "rejected_mean_error": 2.083812570419555,
                "gap_rejected_minus_accepted": 0.5656340362871157
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6790230870246887,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3588387424945831,
                "rejected_mean_error": 1.9607878511428833,
                "gap_rejected_minus_accepted": 0.6019491086483002
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.376905769109726,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1060447400560776,
                "rejected_mean_error": 1.8447968168472404,
                "gap_rejected_minus_accepted": 0.7387520767911628
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.02928740978241,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6024233963754442,
                "rejected_mean_error": 2.1957007122039793,
                "gap_rejected_minus_accepted": 0.5932773158285352
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8615569472312927,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5239912293811533,
                "rejected_mean_error": 2.070657493576171,
                "gap_rejected_minus_accepted": 0.5466662641950175
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6885764002799988,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3704021744728088,
                "rejected_mean_error": 1.9531000814437867,
                "gap_rejected_minus_accepted": 0.5826979069709779
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3959227502346039,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.112287694499606,
                "rejected_mean_error": 1.8468644771983918,
                "gap_rejected_minus_accepted": 0.7345767826987857
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
      "best_epoch": 113,
      "best_calib_loss": 0.014124050736427307,
      "train_time_sec": 55.69582486152649,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993740857094275,
            "spearman": 0.9981189914307924,
            "auroc_top30_bad": 0.9996134761904761,
            "mae": 0.02529562477520655,
            "mse": 0.0014498941635329487,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8122492868691188,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.01090954564511776
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19984813117384911
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6186549022167921
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9866306065539518
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
            "pearson": 0.9996671685378448,
            "spearman": 0.9993133373165006,
            "auroc_top30_worst": 0.9998470476190476,
            "pairwise_seed_ranking": 0.9619,
            "predicted_best_mean_error": 1.7027408022880555,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09168359532952297,
            "gap_to_oracle": 0.0011467545628547349,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7228537470698356
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8792301774740219
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.083977014529705
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3052141532182693
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.156919860839844,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899954303039444,
                "rejected_mean_error": 4.441021912097931,
                "gap_rejected_minus_accepted": 2.951026481793986
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.054629623889923,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3052141532182693,
                "rejected_mean_error": 3.2247498542785644,
                "gap_rejected_minus_accepted": 1.9195357010602951
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5366994142532349,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.083977014529705,
                "rejected_mean_error": 2.486219142436981,
                "gap_rejected_minus_accepted": 1.402242127907276
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.100704938173294,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8792301774740219,
                "rejected_mean_error": 2.0870540454864503,
                "gap_rejected_minus_accepted": 1.2078238680124285
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.209478259086609,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4917231916387876,
                "rejected_mean_error": 4.518735251426697,
                "gap_rejected_minus_accepted": 3.027012059787909
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.058828294277191,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3020834743579228,
                "rejected_mean_error": 3.2714471673965453,
                "gap_rejected_minus_accepted": 1.9693636930386225
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5374515652656555,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0765537880063056,
                "rejected_mean_error": 2.5122950072288512,
                "gap_rejected_minus_accepted": 1.4357412192225456
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0919100940227509,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8668224993944168,
                "rejected_mean_error": 2.1036250303586326,
                "gap_rejected_minus_accepted": 1.2368025309642157
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9890790855539451,
            "spearman": 0.9778046617268179,
            "auroc_top30_bad": 0.9869561904761904,
            "mae": 0.12633196293059312,
            "mse": 0.03136409832181538,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9015188741500542,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09733984190225602
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21348243598937988
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5888057035088539
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0203476090510686
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
            "pearson": 0.9909110479098826,
            "spearman": 0.9836643914401191,
            "auroc_top30_worst": 0.9990339047619048,
            "pairwise_seed_ranking": 0.926,
            "predicted_best_mean_error": 1.9929261837005616,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11155482101440439,
            "gap_to_oracle": 0.004030954003334086,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6395472724437714
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8730828833694642
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.24151534781456
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.548582991906829
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.20369110107422,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8418729435337915,
                "rejected_mean_error": 4.222126745223999,
                "gap_rejected_minus_accepted": 2.3802538016902077
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8356603384017944,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.54721210793599,
                "rejected_mean_error": 3.6745532252156314,
                "gap_rejected_minus_accepted": 2.1273411172796415
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.778595507144928,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.24151534781456,
                "rejected_mean_error": 2.9182812995910643,
                "gap_rejected_minus_accepted": 1.6767659517765043
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2136600613594055,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8745243773102379,
                "rejected_mean_error": 2.4825472513665003,
                "gap_rejected_minus_accepted": 1.6080228740562625
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.304464817047119,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.865689720577664,
                "rejected_mean_error": 4.253602561950683,
                "gap_rejected_minus_accepted": 2.3879128413730193
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8822673559188843,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.555643116089112,
                "rejected_mean_error": 3.733571245556786,
                "gap_rejected_minus_accepted": 2.177928129467674
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7948265671730042,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2396324939727783,
                "rejected_mean_error": 2.9693295154571535,
                "gap_rejected_minus_accepted": 1.7296970214843752
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2133073508739471,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8705015901535277,
                "rejected_mean_error": 2.5202066898345947,
                "gap_rejected_minus_accepted": 1.649705099681067
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.988249141912233,
            "spearman": 0.9807956076320727,
            "auroc_top30_bad": 0.9767542857142856,
            "mae": 0.10573250634972746,
            "mse": 0.022648902256950553,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7569965084778956,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04765219628810882
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1896556506872177
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6296635450720787
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0440865735610325
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
            "pearson": 0.9856146588499949,
            "spearman": 0.9738535031382421,
            "auroc_top30_worst": 0.9617737142857143,
            "pairwise_seed_ranking": 0.9036,
            "predicted_best_mean_error": 1.5863216346502305,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07082150781154617,
            "gap_to_oracle": 0.006424113154411382,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4127987673282623
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6537512928629533
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.033162616252899
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3113420993915752
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.484281325340271,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4584905518955655,
                "rejected_mean_error": 3.3433497409820556,
                "gap_rejected_minus_accepted": 1.88485918908649
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0103800296783447,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3106918747804208,
                "rejected_mean_error": 2.653681475514421,
                "gap_rejected_minus_accepted": 1.342989600734
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.700146734714508,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.033162616252899,
                "rejected_mean_error": 2.2607903253555297,
                "gap_rejected_minus_accepted": 1.2276277091026306
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1289288997650146,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6551567816886658,
                "rejected_mean_error": 1.9782887042014041,
                "gap_rejected_minus_accepted": 1.3231319225127383
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5749926567077637,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.463609338071611,
                "rejected_mean_error": 3.3989473819732665,
                "gap_rejected_minus_accepted": 1.9353380439016554
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.040271520614624,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3073696054239323,
                "rejected_mean_error": 2.6953598317645846,
                "gap_rejected_minus_accepted": 1.3879902263406523
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.712749183177948,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0262758564949035,
                "rejected_mean_error": 2.2880104284286498,
                "gap_rejected_minus_accepted": 1.2617345719337463
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1219677925109863,
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
            "pearson": 0.9839194589988569,
            "spearman": 0.9786253994322068,
            "auroc_top30_bad": 0.9819680000000001,
            "mae": 0.10044421855581195,
            "mse": 0.021993908159173847,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6921974465219719,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07369648003578186
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22139208877086639
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7843920981407165
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.138007374127706
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
            "pearson": 0.9653115582471332,
            "spearman": 0.9583087185335799,
            "auroc_top30_worst": 0.9623801904761905,
            "pairwise_seed_ranking": 0.9056,
            "predicted_best_mean_error": 1.597873631954193,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06387749600410464,
            "gap_to_oracle": 0.005849699974060041,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.848952255487442
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1026385152378144
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.35938006939888
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.520791570928051
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.062365078926087,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5960875390635596,
                "rejected_mean_error": 2.2333451166152956,
                "gap_rejected_minus_accepted": 0.637257577551736
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8983489871025085,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5203545654914168,
                "rejected_mean_error": 2.0772983806963548,
                "gap_rejected_minus_accepted": 0.556943815204938
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7106426358222961,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.35938006939888,
                "rejected_mean_error": 1.9602465242385865,
                "gap_rejected_minus_accepted": 0.6008664548397065
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.417457103729248,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1039977676380937,
                "rejected_mean_error": 1.8454805973881463,
                "gap_rejected_minus_accepted": 0.7414828297500526
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0754729747772216,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6035464607344734,
                "rejected_mean_error": 2.185593132972717,
                "gap_rejected_minus_accepted": 0.5820466722382438
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8988472521305084,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5281051923246944,
                "rejected_mean_error": 2.058446206743755,
                "gap_rejected_minus_accepted": 0.5303410144190606
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7314477562904358,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3715087866783142,
                "rejected_mean_error": 1.9519934692382812,
                "gap_rejected_minus_accepted": 0.580484682559967
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4548258185386658,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1126711359099737,
                "rejected_mean_error": 1.8467352964023855,
                "gap_rejected_minus_accepted": 0.7340641604924119
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
      "best_epoch": 84,
      "best_calib_loss": 0.011188148520886898,
      "train_time_sec": 62.67303824424744,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9992429001959701,
            "spearman": 0.9975655087499464,
            "auroc_top30_bad": 0.9992693333333333,
            "mae": 0.03083673845525518,
            "mse": 0.0017796192432200865,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8167225029215501,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.004507951930165291
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20042094120383264
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6187671102255583
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9870586581210296
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
            "pearson": 0.9994507046184284,
            "spearman": 0.9983885351275028,
            "auroc_top30_worst": 0.9995973333333333,
            "pairwise_seed_ranking": 0.9605,
            "predicted_best_mean_error": 1.7029375860095024,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09148681160807604,
            "gap_to_oracle": 0.0013435382843016708,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7254694600701332
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.880394557929039
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.084294607245922
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051890701532365
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1684885501861584,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899376976688703,
                "rejected_mean_error": 4.441541505813599,
                "gap_rejected_minus_accepted": 2.9516038081447284
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0508710741996765,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051890701532365,
                "rejected_mean_error": 3.2248251034736635,
                "gap_rejected_minus_accepted": 1.919636033320427
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.510714590549469,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.084294607245922,
                "rejected_mean_error": 2.485901549720764,
                "gap_rejected_minus_accepted": 1.401606942474842
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.077237844467163,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.880394557929039,
                "rejected_mean_error": 2.0866659186681114,
                "gap_rejected_minus_accepted": 1.2062713607390725
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.233563971519471,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.061391234397888,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019856477181118,
                "rejected_mean_error": 3.271740647315979,
                "gap_rejected_minus_accepted": 1.9697549995978672
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5123884677886963,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.07692519313097,
                "rejected_mean_error": 2.511923602104187,
                "gap_rejected_minus_accepted": 1.4349984089732168
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.071862518787384,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.869395702958107,
                "rejected_mean_error": 2.102767295837402,
                "gap_rejected_minus_accepted": 1.2333715928792952
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9908627588611402,
            "spearman": 0.9823758841012475,
            "auroc_top30_bad": 0.9937546666666666,
            "mae": 0.11448631091456409,
            "mse": 0.02474202128863738,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.886088973494665,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09411804848909378
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21217345504760743
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.586676706469059
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0188772044897079
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
            "pearson": 0.9953226022830176,
            "spearman": 0.9929145564893163,
            "auroc_top30_worst": 0.9999451428571429,
            "pairwise_seed_ranking": 0.9288,
            "predicted_best_mean_error": 1.9921461515426635,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11233485317230252,
            "gap_to_oracle": 0.003250921845435961,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6354710447788239
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8672703988850117
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2222602244853973
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5466628370445166
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.123828220367432,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8434178791840872,
                "rejected_mean_error": 4.208222324371338,
                "gap_rejected_minus_accepted": 2.364804445187251
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7896435856819153,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5453399841851587,
                "rejected_mean_error": 3.680157634016043,
                "gap_rejected_minus_accepted": 2.134817649830884
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7437638640403748,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2222602244853973,
                "rejected_mean_error": 2.937536422920227,
                "gap_rejected_minus_accepted": 1.7152761984348297
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.169544279575348,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8689384002464647,
                "rejected_mean_error": 2.484413218091112,
                "gap_rejected_minus_accepted": 1.615474817844647
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.216780662536621,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8669701374901666,
                "rejected_mean_error": 4.242078809738159,
                "gap_rejected_minus_accepted": 2.375108672247993
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8557454347610474,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548569416617328,
                "rejected_mean_error": 3.7359048109205943,
                "gap_rejected_minus_accepted": 2.1810478692588617
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.777776062488556,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2222430114746095,
                "rejected_mean_error": 2.986718997955322,
                "gap_rejected_minus_accepted": 1.7644759864807127
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2249694466590881,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8669613486244565,
                "rejected_mean_error": 2.5213993915262067,
                "gap_rejected_minus_accepted": 1.6544380429017502
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9881169152529079,
            "spearman": 0.9827992072372992,
            "auroc_top30_bad": 0.9840518095238096,
            "mae": 0.11106610559839318,
            "mse": 0.026211209467580016,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7406646648247219,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06213776063919067
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19660929288864135
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6266203080534934
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0422134984572728
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
            "pearson": 0.99001407582469,
            "spearman": 0.9870594006140166,
            "auroc_top30_worst": 0.9787001904761905,
            "pairwise_seed_ranking": 0.892,
            "predicted_best_mean_error": 1.585949072599411,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07119406986236565,
            "gap_to_oracle": 0.006051551103591901,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4031876103878021
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6556772159842345
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0239040677070617
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3088001312096236
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.514443802833558,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4594990510410732,
                "rejected_mean_error": 3.3342732486724853,
                "gap_rejected_minus_accepted": 1.874774197631412
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9391759932041168,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3081434986125697,
                "rejected_mean_error": 2.661310320464186,
                "gap_rejected_minus_accepted": 1.3531668218516164
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6066452264785767,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0239040677070617,
                "rejected_mean_error": 2.2700488739013673,
                "gap_rejected_minus_accepted": 1.2461448061943057
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9786911010742188,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6572368965743068,
                "rejected_mean_error": 1.9775938525907257,
                "gap_rejected_minus_accepted": 1.3203569560164188
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.668957161903381,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4650840894381205,
                "rejected_mean_error": 3.3856746196746825,
                "gap_rejected_minus_accepted": 1.920590530236562
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9427745044231415,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3035148257877738,
                "rejected_mean_error": 2.706801796716357,
                "gap_rejected_minus_accepted": 1.4032869709285831
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6223467588424683,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0137814164161683,
                "rejected_mean_error": 2.3005048685073852,
                "gap_rejected_minus_accepted": 1.286723452091217
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9796064049005508,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.6463249439284915,
                "rejected_mean_error": 1.997686171914167,
                "gap_rejected_minus_accepted": 1.3513612279856755
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9824721129804916,
            "spearman": 0.9804766241832581,
            "auroc_top30_bad": 0.9862902857142858,
            "mae": 0.10450965702039393,
            "mse": 0.024521437820083525,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6901157059604273,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07713740533590317
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23055124642848968
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7849360611915588
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1379978075663248
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
            "pearson": 0.968212533274472,
            "spearman": 0.9695690434361879,
            "auroc_top30_worst": 0.9780510476190476,
            "pairwise_seed_ranking": 0.8996,
            "predicted_best_mean_error": 1.5977297327518463,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06402139520645145,
            "gap_to_oracle": 0.005705800771713232,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8424416868686676
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1029678244048204
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3602201490879058
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5161670577615054
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0258533477783205,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5973078646394943,
                "rejected_mean_error": 2.2223621864318845,
                "gap_rejected_minus_accepted": 0.6250543217923903
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8735996186733246,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5158008292810385,
                "rejected_mean_error": 2.0909304919715126,
                "gap_rejected_minus_accepted": 0.575129662690474
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6463066339492798,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3602201490879058,
                "rejected_mean_error": 1.9594064445495605,
                "gap_rejected_minus_accepted": 0.5991862954616547
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2957697212696075,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1038811683845215,
                "rejected_mean_error": 1.8455195467652734,
                "gap_rejected_minus_accepted": 0.7416383783807519
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.018677997589111,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6068504028850132,
                "rejected_mean_error": 2.155857653617859,
                "gap_rejected_minus_accepted": 0.5490072507328458
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8724171221256256,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5233165672756135,
                "rejected_mean_error": 2.07266006204817,
                "gap_rejected_minus_accepted": 0.5493434947725566
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6539122462272644,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3710393233299256,
                "rejected_mean_error": 1.95246293258667,
                "gap_rejected_minus_accepted": 0.5814236092567444
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3058545887470245,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1116502502607921,
                "rejected_mean_error": 1.8470792311398103,
                "gap_rejected_minus_accepted": 0.7354289808790182
              }
            ]
          }
        }
      }
    }
  ]
}
```
