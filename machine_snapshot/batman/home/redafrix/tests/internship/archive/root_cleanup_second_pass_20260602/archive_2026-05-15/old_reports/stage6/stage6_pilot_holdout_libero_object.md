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
      "best_epoch": 45,
      "best_calib_loss": 0.09245499223470688,
      "train_time_sec": 14.257145881652832,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.897507398886781,
            "spearman": 0.8085339013634735,
            "auroc_top30_bad": 0.8809226190476191,
            "mae": 0.21624258587658404,
            "mse": 0.23331475666882553,
            "expert_lt_perturb_large": 0.976,
            "expert_lt_other_task": 0.509,
            "expert_lt_simvla_seed0": 0.974,
            "same_context_pred_std": 0.7772298352571182,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5321362408250571
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.5588545683801174
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7192691976457835
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0208002677539985
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
            "pearson": 0.9977508655910641,
            "spearman": 0.995233910105242,
            "auroc_top30_worst": 0.9987560000000001,
            "pairwise_seed_ranking": 0.8467,
            "predicted_best_mean_error": 1.7108870810866357,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.08353731653094276,
            "gap_to_oracle": 0.009293033361434944,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7337851242423058
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8835917931318283
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0852979450106621
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3056824647506078
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0693079471588143,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4902347367538347,
                "rejected_mean_error": 4.43886815404892,
                "gap_rejected_minus_accepted": 2.9486334172950848
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9925222098827362,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3056824647506078,
                "rejected_mean_error": 3.223344919681549,
                "gap_rejected_minus_accepted": 1.9176624549309413
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.493478000164032,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0852979450106621,
                "rejected_mean_error": 2.484898211956024,
                "gap_rejected_minus_accepted": 1.399600266945362
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.069814294576645,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8835917931318283,
                "rejected_mean_error": 2.0856001736005148,
                "gap_rejected_minus_accepted": 1.2020083804686865
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1214781045913695,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4922291704350048,
                "rejected_mean_error": 4.5141814422607425,
                "gap_rejected_minus_accepted": 3.0219522718257377
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.016417980194092,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3022936797539393,
                "rejected_mean_error": 3.270816551208496,
                "gap_rejected_minus_accepted": 1.9685228714545568
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4844143986701965,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0774089356064795,
                "rejected_mean_error": 2.5114398596286773,
                "gap_rejected_minus_accepted": 1.4340309240221978
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0666162073612213,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8688818174600601,
                "rejected_mean_error": 2.102938591003418,
                "gap_rejected_minus_accepted": 1.234056773543358
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8051352347406965,
            "spearman": 0.7037252062285829,
            "auroc_top30_bad": 0.7854742857142858,
            "mae": 0.4697339663863182,
            "mse": 0.5203400092213629,
            "expert_lt_perturb_large": 0.976,
            "expert_lt_other_task": 0.496,
            "expert_lt_simvla_seed0": 0.94,
            "same_context_pred_std": 0.9036317480980877,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4837394534349442
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6985519183635711
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8198356448531151
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1107434114058812
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
            "pearson": 0.8233728693723571,
            "spearman": 0.7553773988975354,
            "auroc_top30_worst": 0.8489904761904761,
            "pairwise_seed_ranking": 0.754,
            "predicted_best_mean_error": 2.0108849207162858,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.09359608399868025,
            "gap_to_oracle": 0.021989691019058233,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2036557722091674
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1795311965621436
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4881263972759247
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6111418065676557
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.231231927871704,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.843533401356803,
                "rejected_mean_error": 4.207182624816895,
                "gap_rejected_minus_accepted": 2.363649223460092
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7739893198013306,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.609588618053316,
                "rejected_mean_error": 3.4878222668132843,
                "gap_rejected_minus_accepted": 1.8782336487599682
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.700836181640625,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4881263972759247,
                "rejected_mean_error": 2.6716702501297,
                "gap_rejected_minus_accepted": 1.1835438528537752
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.158673346042633,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1800452784989208,
                "rejected_mean_error": 2.3804895757292988,
                "gap_rejected_minus_accepted": 1.200444297230378
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.231732559204102,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8663073698679606,
                "rejected_mean_error": 4.248043718338013,
                "gap_rejected_minus_accepted": 2.3817363484700524
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.812449634075165,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.625813319083841,
                "rejected_mean_error": 3.5252882620644947,
                "gap_rejected_minus_accepted": 1.8994749429806537
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7441790103912354,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5020080108642577,
                "rejected_mean_error": 2.7069539985656736,
                "gap_rejected_minus_accepted": 1.204945987701416
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1729310154914856,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.150088371738555,
                "rejected_mean_error": 2.4260143516535426,
                "gap_rejected_minus_accepted": 1.2759259799149876
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6553303588851067,
            "spearman": 0.5688722265284117,
            "auroc_top30_bad": 0.6747977142857142,
            "mae": 0.49688185020685194,
            "mse": 0.6269863601277281,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.496,
            "expert_lt_simvla_seed0": 0.976,
            "same_context_pred_std": 0.6660953626404692,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8466206273436546
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6603469806671143
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8794609819293022
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1322271963993709
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
            "pearson": 0.8633225992920137,
            "spearman": 0.7993869850796707,
            "auroc_top30_worst": 0.8468205714285714,
            "pairwise_seed_ranking": 0.7864,
            "predicted_best_mean_error": 1.595419367671013,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.06172377479076374,
            "gap_to_oracle": 0.01552184617519381,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5413368599414825
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7930272573079818
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1097279292106628
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3619896271970988
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1061589956283577,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4742199216948615,
                "rejected_mean_error": 3.201785412788391,
                "gap_rejected_minus_accepted": 1.7275654910935296
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7518372237682343,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3610215481597305,
                "rejected_mean_error": 2.503014050733548,
                "gap_rejected_minus_accepted": 1.1419925025738173
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5047129392623901,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1097279292106628,
                "rejected_mean_error": 2.184225012397766,
                "gap_rejected_minus_accepted": 1.0744970831871032
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.001563549041748,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7939507797503242,
                "rejected_mean_error": 1.9319252875596762,
                "gap_rejected_minus_accepted": 1.137974507809352
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1606441020965574,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4818062551816304,
                "rejected_mean_error": 3.2351751279830934,
                "gap_rejected_minus_accepted": 1.753368872801463
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7974732518196106,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.350417836783404,
                "rejected_mean_error": 2.567581748205518,
                "gap_rejected_minus_accepted": 1.217163911422114
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5356738567352295,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.099220389842987,
                "rejected_mean_error": 2.2150658950805666,
                "gap_rejected_minus_accepted": 1.1158455052375795
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9526805877685547,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7716862095726861,
                "rejected_mean_error": 1.9554521626329677,
                "gap_rejected_minus_accepted": 1.1837659530602815
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.5186233918331031,
            "spearman": 0.4149378279607843,
            "auroc_top30_bad": 0.5865017142857143,
            "mae": 0.47204926555156707,
            "mse": 0.6345401557334606,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.988,
            "same_context_pred_std": 0.6310730885486917,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.611901645064354
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0097161148309708
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.050312190914154
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2624241510391236
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
            "pearson": 0.6800080247393052,
            "spearman": 0.5327295159868902,
            "auroc_top30_worst": 0.6762422857142857,
            "pairwise_seed_ranking": 0.7588,
            "predicted_best_mean_error": 1.611177745938301,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.05057338201999673,
            "gap_to_oracle": 0.019153813958167953,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.870639662027359
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3258429896564057
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4775304302692414
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5770048734539353
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8846804261207581,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6278528452184464,
                "rejected_mean_error": 1.9474573612213135,
                "gap_rejected_minus_accepted": 0.3196045160028671
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7538228631019592,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5767953570459035,
                "rejected_mean_error": 1.9083366500683867,
                "gap_rejected_minus_accepted": 0.33154129302248325
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5706622004508972,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4775304302692414,
                "rejected_mean_error": 1.8420961633682251,
                "gap_rejected_minus_accepted": 0.36456573309898377
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3450220823287964,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.3268762976407242,
                "rejected_mean_error": 1.771029178080971,
                "gap_rejected_minus_accepted": 0.4441528804402468
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8820930600166321,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6304493080245124,
                "rejected_mean_error": 1.9434675073623657,
                "gap_rejected_minus_accepted": 0.31301819933785335
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7623329162597656,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5746567552102442,
                "rejected_mean_error": 1.9202693454802982,
                "gap_rejected_minus_accepted": 0.345612590270054
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5846224427223206,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4667819018363952,
                "rejected_mean_error": 1.8567203540802002,
                "gap_rejected_minus_accepted": 0.38993845224380497
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3490039110183716,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.3533384752652002,
                "rejected_mean_error": 1.7656548558709455,
                "gap_rejected_minus_accepted": 0.41231638060574527
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
      "best_epoch": 94,
      "best_calib_loss": 0.04278723895549774,
      "train_time_sec": 17.98711633682251,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9984156931716116,
            "spearman": 0.9958888423089488,
            "auroc_top30_bad": 0.9987464523809524,
            "mae": 0.04477296473272145,
            "mse": 0.0036264084652038574,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.804035443914056,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.053857258968055245
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19996085166335106
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.61870303401649
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9871323598206043
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
            "pearson": 0.9994480864016511,
            "spearman": 0.9986509853618777,
            "auroc_top30_worst": 0.9995028571428572,
            "pairwise_seed_ranking": 0.9171,
            "predicted_best_mean_error": 1.7046675956845283,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.08975680193305013,
            "gap_to_oracle": 0.0030735479593275716,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7234839065670967
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8797101168394089
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.084147847878933
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3052747726043066
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1295607805252112,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4900454480846723,
                "rejected_mean_error": 4.4405717520713806,
                "gap_rejected_minus_accepted": 2.9505263039867082
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0064225792884827,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3052747726043066,
                "rejected_mean_error": 3.2245679961204528,
                "gap_rejected_minus_accepted": 1.9192932235161462
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5093382596969604,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.084147847878933,
                "rejected_mean_error": 2.4860483090877534,
                "gap_rejected_minus_accepted": 1.4019004612088204
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0870734751224518,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8797101168394089,
                "rejected_mean_error": 2.086894065697988,
                "gap_rejected_minus_accepted": 1.207183948858579
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.17186975479126,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4916739550232887,
                "rejected_mean_error": 4.519178380966187,
                "gap_rejected_minus_accepted": 3.0275044259428983
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0189918279647827,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3020717924833298,
                "rejected_mean_error": 3.2714822130203247,
                "gap_rejected_minus_accepted": 1.9694104205369949
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5013569593429565,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.076924547493458,
                "rejected_mean_error": 2.511924247741699,
                "gap_rejected_minus_accepted": 1.4349997002482413
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.079946219921112,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8671248971223832,
                "rejected_mean_error": 2.1035242311159768,
                "gap_rejected_minus_accepted": 1.2363993339935937
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9563701496293007,
            "spearman": 0.9459681385864438,
            "auroc_top30_bad": 0.9715032380952382,
            "mae": 0.269506267079711,
            "mse": 0.1271851545295704,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8268096091992054,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.12371366268396378
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23684903898239135
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6214725506067276
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.032930524166425
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
            "pearson": 0.9603995372410361,
            "spearman": 0.9543099857343909,
            "auroc_top30_worst": 0.9813272380952381,
            "pairwise_seed_ranking": 0.8728,
            "predicted_best_mean_error": 1.9989412519931793,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.10553975272178673,
            "gap_to_oracle": 0.010046022295951751,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7485535783767701
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9346259644207282
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2430857593059539
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.568248049886242
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.255409383773804,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8422645186053381,
                "rejected_mean_error": 4.218602569580078,
                "gap_rejected_minus_accepted": 2.3763380509747396
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.692294180393219,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5665883291174787,
                "rejected_mean_error": 3.6165483713911746,
                "gap_rejected_minus_accepted": 2.049960042273696
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9487378597259521,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2430857593059539,
                "rejected_mean_error": 2.9167108880996704,
                "gap_rejected_minus_accepted": 1.6736251287937165
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4267456829547882,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9347846941254772,
                "rejected_mean_error": 2.462417604447429,
                "gap_rejected_minus_accepted": 1.5276329103219517
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.315445184707642,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8661894883049859,
                "rejected_mean_error": 4.249104652404785,
                "gap_rejected_minus_accepted": 2.382915164099799
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.770212411880493,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5726534070815632,
                "rejected_mean_error": 3.683080381817288,
                "gap_rejected_minus_accepted": 2.1104269747357245
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9965846538543701,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.240747332572937,
                "rejected_mean_error": 2.9682146768569946,
                "gap_rejected_minus_accepted": 1.7274673442840576
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4260812997817993,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9220539047604516,
                "rejected_mean_error": 2.50283879774777,
                "gap_rejected_minus_accepted": 1.5807848929873187
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9646135860107701,
            "spearman": 0.957356080131185,
            "auroc_top30_bad": 0.9665927619047618,
            "mae": 0.20103056970834732,
            "mse": 0.07159503480448776,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6621516728409295,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11659272402524948
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.205541081738472
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.643741190803051
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0466063767353693
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
            "pearson": 0.9738821261938582,
            "spearman": 0.9673929048274592,
            "auroc_top30_worst": 0.9696579047619047,
            "pairwise_seed_ranking": 0.8336,
            "predicted_best_mean_error": 1.5920179133415222,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.06512522912025442,
            "gap_to_oracle": 0.012120391845703127,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4331880316734314
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.702265974229727
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0307193186759949
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3129170058505621
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4301062107086215,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4602715668678283,
                "rejected_mean_error": 3.3273206062316896,
                "gap_rejected_minus_accepted": 1.8670490393638612
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8518436551094055,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.312128775465832,
                "rejected_mean_error": 2.6493799549322157,
                "gap_rejected_minus_accepted": 1.3372511794663837
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5719685554504395,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0307193186759949,
                "rejected_mean_error": 2.263233622932434,
                "gap_rejected_minus_accepted": 1.2325143042564393
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.161291778087616,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.701758479538817,
                "rejected_mean_error": 1.962721648249326,
                "gap_rejected_minus_accepted": 1.260963168710509
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4906173229217528,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4650620998276604,
                "rejected_mean_error": 3.385872526168823,
                "gap_rejected_minus_accepted": 1.9208104263411627
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8440049588680267,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.305938998964381,
                "rejected_mean_error": 2.6996062350651573,
                "gap_rejected_minus_accepted": 1.3936672361007763
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.589377999305725,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0174670968055726,
                "rejected_mean_error": 2.296819188117981,
                "gap_rejected_minus_accepted": 1.2793520913124083
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1568190455436707,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.6897780081582447,
                "rejected_mean_error": 1.9830469042859613,
                "gap_rejected_minus_accepted": 1.2932688961277166
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9334620874744999,
            "spearman": 0.9279923013822167,
            "auroc_top30_bad": 0.9453546666666667,
            "mae": 0.20594034834206104,
            "mse": 0.08685280229591578,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 0.964,
            "same_context_pred_std": 0.6183025664894028,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11795990931987763
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.29515816583633425
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8036711369872093
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1485525780359904
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
            "pearson": 0.845766787385992,
            "spearman": 0.8790070583085173,
            "auroc_top30_worst": 0.9052739047619047,
            "pairwise_seed_ranking": 0.8088,
            "predicted_best_mean_error": 1.6089750335216522,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.05277609443664555,
            "gap_to_oracle": 0.01695110154151913,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.988544052362442
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1395411990965023
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3766444618701934
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.531412310596468
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2222887277603154,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6012341734833186,
                "rejected_mean_error": 2.1870254068374635,
                "gap_rejected_minus_accepted": 0.5857912333541448
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8717658519744873,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5310925314304287,
                "rejected_mean_error": 2.0451530960802073,
                "gap_rejected_minus_accepted": 0.5140605646497787
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.613044261932373,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3766444618701934,
                "rejected_mean_error": 1.9429821317672729,
                "gap_rejected_minus_accepted": 0.5663376698970795
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3588962852954865,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1389597573409826,
                "rejected_mean_error": 1.8338017256944386,
                "gap_rejected_minus_accepted": 0.6948419683534559
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.25912446975708,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.603981748951806,
                "rejected_mean_error": 2.1816755390167235,
                "gap_rejected_minus_accepted": 0.5776937900649175
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8584459722042084,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5361707628092027,
                "rejected_mean_error": 2.0345055451468816,
                "gap_rejected_minus_accepted": 0.4983347823376789
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6213484406471252,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3866203646659852,
                "rejected_mean_error": 1.9368818912506103,
                "gap_rejected_minus_accepted": 0.5502615265846251
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3523868024349213,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1320516249490162,
                "rejected_mean_error": 1.8402060407368257,
                "gap_rejected_minus_accepted": 0.7081544157878095
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
      "best_epoch": 76,
      "best_calib_loss": 0.009852774441242218,
      "train_time_sec": 46.778212785720825,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9992171978918898,
            "spearman": 0.9977443645088796,
            "auroc_top30_bad": 0.9992061428571428,
            "mae": 0.028684938068720855,
            "mse": 0.0017849202264914328,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8101723567178233,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0056218686699867244
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.199947874468565
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6186850231617689
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9866300240814686
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
            "pearson": 0.999373269690673,
            "spearman": 0.9986575491462376,
            "auroc_top30_worst": 0.9993792380952381,
            "pairwise_seed_ranking": 0.9571,
            "predicted_best_mean_error": 1.703599778831005,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09082461878657333,
            "gap_to_oracle": 0.002005731105804376,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7231860186457634
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8794275869131088
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0844411755919456
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3054832364320754
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1728255748748784,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4900100736551816,
                "rejected_mean_error": 4.440890121936798,
                "gap_rejected_minus_accepted": 2.9508800482816167
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.03606915473938,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3054832364320754,
                "rejected_mean_error": 3.223942604637146,
                "gap_rejected_minus_accepted": 1.9184593682050708
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.508459448814392,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0844411755919456,
                "rejected_mean_error": 2.4857549813747406,
                "gap_rejected_minus_accepted": 1.401313805782795
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0781383216381073,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8794275869131088,
                "rejected_mean_error": 2.086988242340088,
                "gap_rejected_minus_accepted": 1.2075606554269789
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.231905937194825,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4916858817802534,
                "rejected_mean_error": 4.519071040153503,
                "gap_rejected_minus_accepted": 3.0273851583732494
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0461833477020264,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3022523049116135,
                "rejected_mean_error": 3.2709406757354738,
                "gap_rejected_minus_accepted": 1.9686883708238603
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.501438558101654,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0770664249062538,
                "rejected_mean_error": 2.5117823703289033,
                "gap_rejected_minus_accepted": 1.4347159454226495
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0782374143600464,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8671116844415665,
                "rejected_mean_error": 2.103528635342916,
                "gap_rejected_minus_accepted": 1.2364169509013494
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9915581689344213,
            "spearman": 0.9837105685825559,
            "auroc_top30_bad": 0.9911939047619048,
            "mae": 0.10330209282805312,
            "mse": 0.022333236027940313,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8957988718564982,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08638994252681732
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20098580825328827
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5863366902947426
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0199658368825912
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
            "pearson": 0.9927144098204567,
            "spearman": 0.9908543122267599,
            "auroc_top30_worst": 0.9984914285714286,
            "pairwise_seed_ranking": 0.9192,
            "predicted_best_mean_error": 1.994593143582344,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.10988786113262194,
            "gap_to_oracle": 0.0056979138851165345,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6202448170185089
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8701008014763013
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.227440371656418
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.549628632758726
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.086318635940552,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8419764114750756,
                "rejected_mean_error": 4.221195533752441,
                "gap_rejected_minus_accepted": 2.3792191222773655
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7893704175949097,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5482422237780458,
                "rejected_mean_error": 3.6714694598993174,
                "gap_rejected_minus_accepted": 2.123227236121272
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.790719747543335,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.227440371656418,
                "rejected_mean_error": 2.9323562757492065,
                "gap_rejected_minus_accepted": 1.7049159040927886
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.281887710094452,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8709093792179522,
                "rejected_mean_error": 2.4837548227676587,
                "gap_rejected_minus_accepted": 1.6128454435497064
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.176162433624268,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8652242936028374,
                "rejected_mean_error": 4.257791404724121,
                "gap_rejected_minus_accepted": 2.3925671111212834
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.884294092655182,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.555643116089112,
                "rejected_mean_error": 3.733571245556786,
                "gap_rejected_minus_accepted": 2.177928129467674
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.804456889629364,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2275575733184814,
                "rejected_mean_error": 2.98140443611145,
                "gap_rejected_minus_accepted": 1.7538468627929686
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3007951974868774,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8678856596114144,
                "rejected_mean_error": 2.5210879926375527,
                "gap_rejected_minus_accepted": 1.6532023330261383
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9886083782512296,
            "spearman": 0.9818627310586717,
            "auroc_top30_bad": 0.9818209523809525,
            "mae": 0.10356688508722911,
            "mse": 0.022699351413430758,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7463540918151486,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05498943096399307
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18864539618492127
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.629516977250576
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.041776989897092
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
            "pearson": 0.9889551411038221,
            "spearman": 0.9773466704298691,
            "auroc_top30_worst": 0.9665676190476191,
            "pairwise_seed_ranking": 0.8992,
            "predicted_best_mean_error": 1.586599109172821,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07054403328895553,
            "gap_to_oracle": 0.006701587677002019,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.40224797534942625
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.654472675652076
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0338305918693542
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3101680560279756
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4380735397338866,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4585718941688537,
                "rejected_mean_error": 3.342617660522461,
                "gap_rejected_minus_accepted": 1.8840457663536072
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.976194143295288,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3095596977206405,
                "rejected_mean_error": 2.657070772335552,
                "gap_rejected_minus_accepted": 1.3475110746149115
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.699712097644806,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0338305918693542,
                "rejected_mean_error": 2.2601223497390746,
                "gap_rejected_minus_accepted": 1.2262917578697203
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0922073423862457,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6557637733011581,
                "rejected_mean_error": 1.9780859417950967,
                "gap_rejected_minus_accepted": 1.3223221684939386
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.499592351913452,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.463609338071611,
                "rejected_mean_error": 3.3989473819732665,
                "gap_rejected_minus_accepted": 1.9353380439016554
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0130693316459656,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3049762290429303,
                "rejected_mean_error": 2.702463980705019,
                "gap_rejected_minus_accepted": 1.3974877516620885
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7051672339439392,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.024538764476776,
                "rejected_mean_error": 2.2897475204467774,
                "gap_rejected_minus_accepted": 1.2652087559700014
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.078574776649475,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.6439674600722298,
                "rejected_mean_error": 1.9984804044432818,
                "gap_rejected_minus_accepted": 1.354512944371052
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9818204390564762,
            "spearman": 0.9744822476644479,
            "auroc_top30_bad": 0.9764533333333333,
            "mae": 0.10724149011783657,
            "mse": 0.02497572685785287,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6826815070102857,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07044030219316483
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23253457791805268
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7862291779518128
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1384640007654825
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
            "pearson": 0.956532140036016,
            "spearman": 0.939452973217903,
            "auroc_top30_worst": 0.9466179047619048,
            "pairwise_seed_ranking": 0.9052,
            "predicted_best_mean_error": 1.598391616821289,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06335951113700866,
            "gap_to_oracle": 0.006367684841156018,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8501811525821685
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.105328747190726
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3619039696216584
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5227331134365565
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.075142502784729,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5985497705936431,
                "rejected_mean_error": 2.2111850328445435,
                "gap_rejected_minus_accepted": 0.6126352622509004
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8914266526699066,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5222789814085436,
                "rejected_mean_error": 2.071537429532304,
                "gap_rejected_minus_accepted": 0.5492584481237606
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7172827124595642,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3619039696216584,
                "rejected_mean_error": 1.957722624015808,
                "gap_rejected_minus_accepted": 0.5958186543941497
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.416386067867279,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1061316481984842,
                "rejected_mean_error": 1.844767785632114,
                "gap_rejected_minus_accepted": 0.7386361374336299
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0770250320434567,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6048737083541023,
                "rejected_mean_error": 2.173647904396057,
                "gap_rejected_minus_accepted": 0.5687741960419548
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8999213576316833,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5284886605599348,
                "rejected_mean_error": 2.0573079756328037,
                "gap_rejected_minus_accepted": 0.5288193150728688
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.720984160900116,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3738981537818908,
                "rejected_mean_error": 1.9496041021347046,
                "gap_rejected_minus_accepted": 0.5757059483528137
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4275596141815186,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1147579096612477,
                "rejected_mean_error": 1.8460322656733468,
                "gap_rejected_minus_accepted": 0.7312743560120991
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
      "best_epoch": 93,
      "best_calib_loss": 0.01179075613617897,
      "train_time_sec": 45.205406665802,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9992525491640215,
            "spearman": 0.9977876587288266,
            "auroc_top30_bad": 0.9994433333333334,
            "mae": 0.02632474770408507,
            "mse": 0.0017153523054637251,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8038221505960649,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0041891086548566814
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19995041443705558
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6186456548184156
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9866891816914082
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
            "pearson": 0.9995279828720967,
            "spearman": 0.9991860190394019,
            "auroc_top30_worst": 0.9997011428571428,
            "pairwise_seed_ranking": 0.956,
            "predicted_best_mean_error": 1.7028456921577453,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09157870545983315,
            "gap_to_oracle": 0.001251644432544552,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7224315661787987
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8794411351919175
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0839366627573968
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3053011767625808
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.142132949829102,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.490010512822204,
                "rejected_mean_error": 4.440886169433594,
                "gap_rejected_minus_accepted": 2.95087565661139
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0157703161239624,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3053011767625808,
                "rejected_mean_error": 3.2244887836456297,
                "gap_rejected_minus_accepted": 1.919187606883049
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5141409635543823,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0839366627573968,
                "rejected_mean_error": 2.4862594942092895,
                "gap_rejected_minus_accepted": 1.4023228314518927
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0770054459571838,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8794411351919175,
                "rejected_mean_error": 2.086983726247152,
                "gap_rejected_minus_accepted": 1.2075425910552342
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1899796962738045,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4917397474249203,
                "rejected_mean_error": 4.518586249351501,
                "gap_rejected_minus_accepted": 3.026846501926581
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.018574297428131,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3020722368955613,
                "rejected_mean_error": 3.2714808797836303,
                "gap_rejected_minus_accepted": 1.969408642888069
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5091776847839355,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0765267129540443,
                "rejected_mean_error": 2.5123220822811128,
                "gap_rejected_minus_accepted": 1.4357953693270684
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.061201572418213,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8674714213609696,
                "rejected_mean_error": 2.103408723036448,
                "gap_rejected_minus_accepted": 1.2359373016754784
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9900818982772269,
            "spearman": 0.9819986692129304,
            "auroc_top30_bad": 0.992713142857143,
            "mae": 0.11562366912478156,
            "mse": 0.02670380983375544,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8902754318060928,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11923736792802811
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20216395952701569
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5867586527466774
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0199247240463893
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
            "pearson": 0.99283082317172,
            "spearman": 0.9912815601161985,
            "auroc_top30_worst": 0.9985798095238095,
            "pairwise_seed_ranking": 0.9212,
            "predicted_best_mean_error": 1.9942161220312118,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11026488268375423,
            "gap_to_oracle": 0.005320892333984251,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6339792835712433
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8703804932152613
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.224533744764328
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.549714194527313
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.134854745864868,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8422467815346188,
                "rejected_mean_error": 4.218762203216553,
                "gap_rejected_minus_accepted": 2.376515421681934
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8329002261161804,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5483638261590975,
                "rejected_mean_error": 3.6711054297681813,
                "gap_rejected_minus_accepted": 2.122741603609084
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8361076712608337,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.224533744764328,
                "rejected_mean_error": 2.935262902641296,
                "gap_rejected_minus_accepted": 1.710729157876968
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.219830721616745,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8720527463637221,
                "rejected_mean_error": 2.48337288689079,
                "gap_rejected_minus_accepted": 1.6113201405270678
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.222613477706909,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.86610019048055,
                "rejected_mean_error": 4.249908332824707,
                "gap_rejected_minus_accepted": 2.383808142344157
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.91074138879776,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.555433442885863,
                "rejected_mean_error": 3.7341936088743664,
                "gap_rejected_minus_accepted": 2.1787601659885034
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8494199514389038,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2229046487808228,
                "rejected_mean_error": 2.986057360649109,
                "gap_rejected_minus_accepted": 1.7631527118682861
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.234761118888855,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8704255478722709,
                "rejected_mean_error": 2.520232308357157,
                "gap_rejected_minus_accepted": 1.6498067604848863
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9872129561244626,
            "spearman": 0.9806679728351649,
            "auroc_top30_bad": 0.9793721904761904,
            "mae": 0.11836963671138542,
            "mse": 0.026929486311195388,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7360783272853844,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06239346802234649
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18546771600246428
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6289930716872215
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0442687837203344
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
            "pearson": 0.9857604601358617,
            "spearman": 0.9764411671303472,
            "auroc_top30_worst": 0.9669028571428572,
            "pairwise_seed_ranking": 0.8968,
            "predicted_best_mean_error": 1.585518905878067,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07162423658370964,
            "gap_to_oracle": 0.005621384382247907,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.42297301125526426
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.655591810743014
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0342644568443298
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.312410623597692
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5117027044296267,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4599580633905198,
                "rejected_mean_error": 3.330142137527466,
                "gap_rejected_minus_accepted": 1.870184074136946
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9784350097179413,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3118586992505012,
                "rejected_mean_error": 2.6501884578515926,
                "gap_rejected_minus_accepted": 1.3383297586010914
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6454951763153076,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0342644568443298,
                "rejected_mean_error": 2.2596884847640992,
                "gap_rejected_minus_accepted": 1.2254240279197695
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.086222529411316,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6568694080407627,
                "rejected_mean_error": 1.9777166102332011,
                "gap_rejected_minus_accepted": 1.3208472021924385
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.646018886566162,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4650840894381205,
                "rejected_mean_error": 3.3856746196746825,
                "gap_rejected_minus_accepted": 1.920590530236562
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9949130415916443,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3069989665306825,
                "rejected_mean_error": 2.6964599821302624,
                "gap_rejected_minus_accepted": 1.38946101559958
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6630488634109497,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.024967794895172,
                "rejected_mean_error": 2.289318490028381,
                "gap_rejected_minus_accepted": 1.264350695133209
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0737968683242798,
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
            "pearson": 0.9812453965835828,
            "spearman": 0.9725796468110619,
            "auroc_top30_bad": 0.9734819047619048,
            "mae": 0.1157536557302285,
            "mse": 0.027808001844661305,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6700335948565211,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08072066104412079
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22547208893299103
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7852382962226868
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1414588331858317
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
            "pearson": 0.9518158093309186,
            "spearman": 0.9398168948588128,
            "auroc_top30_worst": 0.9446491428571429,
            "pairwise_seed_ranking": 0.904,
            "predicted_best_mean_error": 1.5974714860916137,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.064279641866684,
            "gap_to_oracle": 0.005447554111480679,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8480284788608551
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1017635224912412
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3628269051074982
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.524674613878671
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.015733885765076,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6020361988544465,
                "rejected_mean_error": 2.1798071784973145,
                "gap_rejected_minus_accepted": 0.577770979642868
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8485483229160309,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5243062891916888,
                "rejected_mean_error": 2.0654684602262114,
                "gap_rejected_minus_accepted": 0.5411621710345227
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6803555488586426,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3628269051074982,
                "rejected_mean_error": 1.9567996885299683,
                "gap_rejected_minus_accepted": 0.5939727834224702
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3609668612480164,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.102774673090956,
                "rejected_mean_error": 1.8458891657907655,
                "gap_rejected_minus_accepted": 0.7431144926998094
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.01502320766449,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.608337643676334,
                "rejected_mean_error": 2.1424724864959717,
                "gap_rejected_minus_accepted": 0.5341348428196377
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8359539806842804,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.532123321199162,
                "rejected_mean_error": 2.0465193797671604,
                "gap_rejected_minus_accepted": 0.5143960585679983
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6830697059631348,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.375006055355072,
                "rejected_mean_error": 1.9484962005615234,
                "gap_rejected_minus_accepted": 0.5734901452064514
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3595047891139984,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1114418856681338,
                "rejected_mean_error": 1.8471494288368022,
                "gap_rejected_minus_accepted": 0.7357075431686684
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
      "best_epoch": 97,
      "best_calib_loss": 0.011718510650098324,
      "train_time_sec": 50.77289700508118,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994961550595198,
            "spearman": 0.9980794721478161,
            "auroc_top30_bad": 0.9993925238095238,
            "mae": 0.024351087517057248,
            "mse": 0.0011404217965191694,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8111020982160916,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0033381272107362745
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19993606678843498
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6186773577183485
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9866595460553964
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
            "pearson": 0.9996034358727488,
            "spearman": 0.9988059105761793,
            "auroc_top30_worst": 0.9995720000000001,
            "pairwise_seed_ranking": 0.9678,
            "predicted_best_mean_error": 1.7026783728003503,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09174602481722816,
            "gap_to_oracle": 0.0010843250751495503,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.72447921282053
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8794404694318771
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0840904497504233
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.305325922926267
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1310172796249405,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899350988533762,
                "rejected_mean_error": 4.4415648951530455,
                "gap_rejected_minus_accepted": 2.9516297962996694
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0291929841041565,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.305325922926267,
                "rejected_mean_error": 3.2244145451545716,
                "gap_rejected_minus_accepted": 1.9190886222283046
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5129458904266357,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0840904497504233,
                "rejected_mean_error": 2.4861057072162627,
                "gap_rejected_minus_accepted": 1.4020152574658393
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0862228274345398,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8794404694318771,
                "rejected_mean_error": 2.0869839481671653,
                "gap_rejected_minus_accepted": 1.2075434787352881
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1829122543334964,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491642521388001,
                "rejected_mean_error": 4.519461283683777,
                "gap_rejected_minus_accepted": 3.0278187622957757
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0322954058647156,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.302182143410047,
                "rejected_mean_error": 3.2711511602401733,
                "gap_rejected_minus_accepted": 1.9689690168301264
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5142122507095337,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0768738577961923,
                "rejected_mean_error": 2.511974937438965,
                "gap_rejected_minus_accepted": 1.4351010796427728
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.081809639930725,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8669155179262161,
                "rejected_mean_error": 2.103594024181366,
                "gap_rejected_minus_accepted": 1.2366785062551497
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9912171884816928,
            "spearman": 0.9833971718610648,
            "auroc_top30_bad": 0.9929432380952382,
            "mae": 0.12117674904320083,
            "mse": 0.024891069099307148,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9028816172752974,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09723710161447525
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20540707671642303
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.586469148695469
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.020483033410708
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
            "pearson": 0.994456400246264,
            "spearman": 0.9932947658846503,
            "auroc_top30_worst": 0.9996678095238095,
            "pairwise_seed_ranking": 0.9344,
            "predicted_best_mean_error": 1.9922963635921478,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11218464112281823,
            "gap_to_oracle": 0.0034011338949202496,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6234561660289765
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.871498515113042
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.222476959180832
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5482580685602831
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.139468669891358,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.842774604452981,
                "rejected_mean_error": 4.214011796951294,
                "gap_rejected_minus_accepted": 2.3712371924983127
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8802220821380615,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5470734712217509,
                "rejected_mean_error": 3.67496824950075,
                "gap_rejected_minus_accepted": 2.127894778278999
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7793518900871277,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.222476959180832,
                "rejected_mean_error": 2.9373196882247923,
                "gap_rejected_minus_accepted": 1.7148427290439603
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1962656676769257,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.873046694376979,
                "rejected_mean_error": 2.4830408637017296,
                "gap_rejected_minus_accepted": 1.6099941693247506
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.20306544303894,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8664221413930258,
                "rejected_mean_error": 4.247010774612427,
                "gap_rejected_minus_accepted": 2.3805886332194013
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.9125359058380127,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548569416617328,
                "rejected_mean_error": 3.7359048109205943,
                "gap_rejected_minus_accepted": 2.1810478692588617
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.817071557044983,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2210778217315674,
                "rejected_mean_error": 2.987884187698364,
                "gap_rejected_minus_accepted": 1.7668063659667967
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1824535727500916,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8643942579390511,
                "rejected_mean_error": 2.522264240259793,
                "gap_rejected_minus_accepted": 1.6578699823207417
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9915204393251229,
            "spearman": 0.9873604726910209,
            "auroc_top30_bad": 0.9876236190476191,
            "mae": 0.09672147037351228,
            "mse": 0.018040177524389425,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7609872349023892,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05124140018224716
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17631111223697662
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6268982905745506
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0409715510924658
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
            "pearson": 0.9900610143129902,
            "spearman": 0.9886581011571849,
            "auroc_top30_worst": 0.9844022857142857,
            "pairwise_seed_ranking": 0.8948,
            "predicted_best_mean_error": 1.5857495884895325,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07139355397224412,
            "gap_to_oracle": 0.005852066993713434,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4048345255851746
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6548800248748217
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.025539031124115
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3063223845541858
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6373619556427026,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4601152403619555,
                "rejected_mean_error": 3.3287275447845457,
                "gap_rejected_minus_accepted": 1.8686123044225902
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9298072457313538,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3054777640161546,
                "rejected_mean_error": 2.6692904908055315,
                "gap_rejected_minus_accepted": 1.363812726789377
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6184855103492737,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.025539031124115,
                "rejected_mean_error": 2.268413910484314,
                "gap_rejected_minus_accepted": 1.242874879360199
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.009111911058426,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6563259048964649,
                "rejected_mean_error": 1.9778981646453304,
                "gap_rejected_minus_accepted": 1.3215722597488655
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7924251079559324,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.466823774708642,
                "rejected_mean_error": 3.37001745223999,
                "gap_rejected_minus_accepted": 1.9031936775313483
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9318999946117401,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3011730587418704,
                "rejected_mean_error": 2.713752756043086,
                "gap_rejected_minus_accepted": 1.4125796973012155
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6304020285606384,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0150158562660216,
                "rejected_mean_error": 2.2992704286575316,
                "gap_rejected_minus_accepted": 1.28425457239151
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9928875267505646,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.645200370796143,
                "rejected_mean_error": 1.9980650387983272,
                "gap_rejected_minus_accepted": 1.352864668002184
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9858006404335005,
            "spearman": 0.9804596033160924,
            "auroc_top30_bad": 0.9839299047619048,
            "mae": 0.10185754692184487,
            "mse": 0.020504273205689164,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6952308205559791,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07818466621637345
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21622883472442628
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7836258689880371
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1374903162638346
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
            "pearson": 0.9673384156308318,
            "spearman": 0.9638436489239354,
            "auroc_top30_worst": 0.9692982857142858,
            "pairwise_seed_ranking": 0.8928,
            "predicted_best_mean_error": 1.598633529663086,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06311759829521169,
            "gap_to_oracle": 0.0066095976829529945,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8453878252506256
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1057443955960946
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3590964285373688
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5184955154972544
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0403869390487674,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5957030125988854,
                "rejected_mean_error": 2.2368058547973635,
                "gap_rejected_minus_accepted": 0.6411028421984781
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8671865165233612,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.518239911140729,
                "rejected_mean_error": 2.083628831580043,
                "gap_rejected_minus_accepted": 0.5653889204393141
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6555941700935364,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3590964285373688,
                "rejected_mean_error": 1.9605301651000977,
                "gap_rejected_minus_accepted": 0.6014337365627289
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.282753199338913,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1065125150231128,
                "rejected_mean_error": 1.8446405590407495,
                "gap_rejected_minus_accepted": 0.7381280440176368
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.040386939048767,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6007412309116786,
                "rejected_mean_error": 2.2108402013778687,
                "gap_rejected_minus_accepted": 0.6100989704661901
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8683653771877289,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5239354540957486,
                "rejected_mean_error": 2.070823048788404,
                "gap_rejected_minus_accepted": 0.5468875946926552
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6842862367630005,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3696237416267396,
                "rejected_mean_error": 1.953878514289856,
                "gap_rejected_minus_accepted": 0.5842547726631164
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2941104471683502,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1174096275889684,
                "rejected_mean_error": 1.8451389061575905,
                "gap_rejected_minus_accepted": 0.727729278568622
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
      "best_epoch": 98,
      "best_calib_loss": 0.010307460092008114,
      "train_time_sec": 42.89663791656494,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997475111680116,
            "spearman": 0.998817486663451,
            "auroc_top30_bad": 0.9996830952380952,
            "mae": 0.024105386745079886,
            "mse": 0.0010418491049794599,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7957274138938693,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0005691585540771485
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19970580584406852
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6186239487141371
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9864589750428995
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
            "pearson": 0.9998352324223669,
            "spearman": 0.9995163691406432,
            "auroc_top30_worst": 0.9998190476190476,
            "pairwise_seed_ranking": 0.9629,
            "predicted_best_mean_error": 1.7026852279305458,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09173916968703266,
            "gap_to_oracle": 0.0010911802053450437,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7222285426259041
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.879089408659935
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0838287435889244
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051215232133866
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1324111223220825,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.489938205924299,
                "rejected_mean_error": 4.44153693151474,
                "gap_rejected_minus_accepted": 2.9515987255904412
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.009243071079254,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051215232133866,
                "rejected_mean_error": 3.2250277442932127,
                "gap_rejected_minus_accepted": 1.9199062210798261
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5027364492416382,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0838287435889244,
                "rejected_mean_error": 2.486367413377762,
                "gap_rejected_minus_accepted": 1.4025386697888373
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0750635862350464,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.879089408659935,
                "rejected_mean_error": 2.0871009684244792,
                "gap_rejected_minus_accepted": 1.2080115597645442
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.178086757659912,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4916815290517278,
                "rejected_mean_error": 4.519110214710236,
                "gap_rejected_minus_accepted": 3.027428685658508
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.019699454307556,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019926101764043,
                "rejected_mean_error": 3.271719759941101,
                "gap_rejected_minus_accepted": 1.9697271497646969
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4958511590957642,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0765541670918464,
                "rejected_mean_error": 2.5122946281433105,
                "gap_rejected_minus_accepted": 1.4357404610514641
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0736099779605865,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8665813828706741,
                "rejected_mean_error": 2.103705402533213,
                "gap_rejected_minus_accepted": 1.237124019662539
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9926222595186507,
            "spearman": 0.9884072233677078,
            "auroc_top30_bad": 0.9936419047619048,
            "mae": 0.10381139624589122,
            "mse": 0.022587214269113556,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9224468092285264,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0653846897482872
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19127064101696015
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5846094938874244
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.019134463540713
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
            "pearson": 0.9928671909518216,
            "spearman": 0.994799235839511,
            "auroc_top30_worst": 0.9979550476190476,
            "pairwise_seed_ranking": 0.9228,
            "predicted_best_mean_error": 1.9932814639806749,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11119954073429117,
            "gap_to_oracle": 0.00438623428344731,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6186040151119232
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8662143937097146
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2212493327617646
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5521783720392155
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.235224056243896,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8426810890568628,
                "rejected_mean_error": 4.214853435516358,
                "gap_rejected_minus_accepted": 2.372172346459495
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.879635751247406,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5507885672812018,
                "rejected_mean_error": 3.6638466999553643,
                "gap_rejected_minus_accepted": 2.1130581326741624
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8812992572784424,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2212493327617646,
                "rejected_mean_error": 2.9385473146438597,
                "gap_rejected_minus_accepted": 1.717297981882095
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2537494599819183,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8676778317069094,
                "rejected_mean_error": 2.484834304486929,
                "gap_rejected_minus_accepted": 1.6171564727800198
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.281530284881592,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8661772516038684,
                "rejected_mean_error": 4.249214782714843,
                "gap_rejected_minus_accepted": 2.383037531110975
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.897545576095581,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5583100063915558,
                "rejected_mean_error": 3.7256552378336587,
                "gap_rejected_minus_accepted": 2.167345231442103
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8887447714805603,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.221043532371521,
                "rejected_mean_error": 2.9879184770584106,
                "gap_rejected_minus_accepted": 1.7668749446868897
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.261661946773529,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8677580753962199,
                "rejected_mean_error": 2.5211309755549713,
                "gap_rejected_minus_accepted": 1.6533729001587516
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9924494848394291,
            "spearman": 0.9875629861640989,
            "auroc_top30_bad": 0.9855466666666667,
            "mae": 0.08572862181430682,
            "mse": 0.013540339612555394,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.776122022799889,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03300312495231628
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18085166730880736
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6264887790083885
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0426914565642675
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
            "pearson": 0.9917161932258102,
            "spearman": 0.9890499964479978,
            "auroc_top30_worst": 0.9814979047619048,
            "pairwise_seed_ranking": 0.8984,
            "predicted_best_mean_error": 1.589316455721855,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.06782668673992154,
            "gap_to_oracle": 0.009418934226036013,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.40463173198699953
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6535704495050968
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0237430045127869
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3071806676733468
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7546752214431787,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4587711629337734,
                "rejected_mean_error": 3.3408242416381837,
                "gap_rejected_minus_accepted": 1.8820530787044103
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.115901231765747,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3065578612472102,
                "rejected_mean_error": 2.6660571006921154,
                "gap_rejected_minus_accepted": 1.3594992394449052
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7177219986915588,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0237430045127869,
                "rejected_mean_error": 2.270209937095642,
                "gap_rejected_minus_accepted": 1.246466932582855
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.103839933872223,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6547751849451766,
                "rejected_mean_error": 1.9784161746183861,
                "gap_rejected_minus_accepted": 1.3236409896732095
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.883040404319763,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4638889373673334,
                "rejected_mean_error": 3.3964309883117676,
                "gap_rejected_minus_accepted": 1.9325420509444342
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.140336751937866,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3010333658539674,
                "rejected_mean_error": 2.7141674000119407,
                "gap_rejected_minus_accepted": 1.4131340341579732
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7344641089439392,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0128855862617492,
                "rejected_mean_error": 2.301400698661804,
                "gap_rejected_minus_accepted": 1.288515112400055
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0891670882701874,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.641842334043412,
                "rejected_mean_error": 1.9991963559930974,
                "gap_rejected_minus_accepted": 1.3573540219496856
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9906925909037029,
            "spearman": 0.9827953301648932,
            "auroc_top30_bad": 0.9800739047619048,
            "mae": 0.07510303019387647,
            "mse": 0.012316286320835791,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.724408590039598,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.043991619288921355
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2151450795173645
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7828827467918396
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.137695791244507
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
            "pearson": 0.9747914760415718,
            "spearman": 0.9643384501366082,
            "auroc_top30_worst": 0.9641752380952381,
            "pairwise_seed_ranking": 0.9088,
            "predicted_best_mean_error": 1.59854119682312,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.0632099311351777,
            "gap_to_oracle": 0.006517264842986981,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8483355247974396
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1001055910228155
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3584071598529817
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5207627283802418
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0934186697006227,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5939943278895483,
                "rejected_mean_error": 2.2521840171813965,
                "gap_rejected_minus_accepted": 0.6581896892918482
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9193397164344788,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5205186810602882,
                "rejected_mean_error": 2.076807082651522,
                "gap_rejected_minus_accepted": 0.5562884015912339
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.743529498577118,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3584071598529817,
                "rejected_mean_error": 1.9612194337844848,
                "gap_rejected_minus_accepted": 0.6028122739315032
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4599513411521912,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1013241104615001,
                "rejected_mean_error": 1.846373718728887,
                "gap_rejected_minus_accepted": 0.7450496082673868
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0764080286026,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5986779152022468,
                "rejected_mean_error": 2.2294100427627566,
                "gap_rejected_minus_accepted": 0.6307321275605098
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9185457825660706,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5304649115246247,
                "rejected_mean_error": 2.051441960864597,
                "gap_rejected_minus_accepted": 0.5209770493399721
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7558642625808716,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3696566557884216,
                "rejected_mean_error": 1.9538456001281739,
                "gap_rejected_minus_accepted": 0.5841889443397523
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4752894341945648,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1110458667316134,
                "rejected_mean_error": 1.8472828469811913,
                "gap_rejected_minus_accepted": 0.7362369802495778
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
      "best_epoch": 83,
      "best_calib_loss": 0.012855453416705132,
      "train_time_sec": 35.6038293838501,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997948056491411,
            "spearman": 0.9988893511223504,
            "auroc_top30_bad": 0.9998259523809524,
            "mae": 0.015674075905872723,
            "mse": 0.00048357560868771756,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8140378068199601,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0011060406863689423
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19972050439715386
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.618550791093707
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.98636773605148
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
            "pearson": 0.9998491800780704,
            "spearman": 0.9996213484088449,
            "auroc_top30_worst": 0.9999272380952381,
            "pairwise_seed_ranking": 0.9697,
            "predicted_best_mean_error": 1.7020884504020215,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09233594721555693,
            "gap_to_oracle": 0.000494402676820771,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7217029795050621
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8789122173070908
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0838233848452568
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051515078783036
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.159972333908082,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899359589616457,
                "rejected_mean_error": 4.44155715417862,
                "gap_rejected_minus_accepted": 2.951621195216974
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0332486629486084,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051515078783036,
                "rejected_mean_error": 3.224937790298462,
                "gap_rejected_minus_accepted": 1.9197862824201584
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5151765942573547,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0838233848452568,
                "rejected_mean_error": 2.4863727721214293,
                "gap_rejected_minus_accepted": 1.4025493872761725
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0899112522602081,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8789122173070908,
                "rejected_mean_error": 2.0871600322087605,
                "gap_rejected_minus_accepted": 1.2082478149016698
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2030826091766365,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0307822823524475,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019949396848678,
                "rejected_mean_error": 3.2717127714157104,
                "gap_rejected_minus_accepted": 1.9697178317308426
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.514013648033142,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.076417521774769,
                "rejected_mean_error": 2.512431273460388,
                "gap_rejected_minus_accepted": 1.436013751685619
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0804762244224548,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.866622593998909,
                "rejected_mean_error": 2.1036916654904685,
                "gap_rejected_minus_accepted": 1.2370690714915595
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9892590324627203,
            "spearman": 0.9799639300616585,
            "auroc_top30_bad": 0.9890453333333333,
            "mae": 0.1225161082120082,
            "mse": 0.028680087361244826,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8801270951732173,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10157856047153473
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20883302147388458
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5890469096779823
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0201956326564152
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
            "pearson": 0.9918148800015949,
            "spearman": 0.9870686596279423,
            "auroc_top30_worst": 0.9993264761904762,
            "pairwise_seed_ranking": 0.924,
            "predicted_best_mean_error": 1.9928494362831115,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11163156843185451,
            "gap_to_oracle": 0.003954206585883968,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6413079965114593
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8728530276089143
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2288737945079804
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.54910141785643
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.030405950546265,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8422581895987193,
                "rejected_mean_error": 4.218659530639648,
                "gap_rejected_minus_accepted": 2.3764013410409293
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.79448539018631,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5479035442068838,
                "rejected_mean_error": 3.6724833345260866,
                "gap_rejected_minus_accepted": 2.1245797903192027
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7107416987419128,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2288737945079804,
                "rejected_mean_error": 2.930922852897644,
                "gap_rejected_minus_accepted": 1.7020490583896635
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1691696047782898,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8736528122958284,
                "rejected_mean_error": 2.4828383931482616,
                "gap_rejected_minus_accepted": 1.6091855808524334
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.139854764938354,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.86610019048055,
                "rejected_mean_error": 4.249908332824707,
                "gap_rejected_minus_accepted": 2.383808142344157
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.896841585636139,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548569416617328,
                "rejected_mean_error": 3.7359048109205943,
                "gap_rejected_minus_accepted": 2.1810478692588617
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7076008915901184,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.22887234210968,
                "rejected_mean_error": 2.9800896673202515,
                "gap_rejected_minus_accepted": 1.7512173252105714
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1654751300811768,
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
            "pearson": 0.9875010593134774,
            "spearman": 0.9800169553052798,
            "auroc_top30_bad": 0.9771664761904761,
            "mae": 0.1125271110022326,
            "mse": 0.025291646583361412,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7481729272334032,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04772544294595718
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18668061640262604
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6309032059073448
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0470887343327204
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
            "pearson": 0.9858361525241068,
            "spearman": 0.9748880120883279,
            "auroc_top30_worst": 0.9653394285714285,
            "pairwise_seed_ranking": 0.8972,
            "predicted_best_mean_error": 1.5851510070562362,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07199213540554039,
            "gap_to_oracle": 0.005253485560417159,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3979224681854248
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.655114064231897
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0357282172203064
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.313207923031565
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5320700168609647,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.458779909822676,
                "rejected_mean_error": 3.3407455196380615,
                "gap_rejected_minus_accepted": 1.8819656098153856
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9956132471561432,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3122374274178528,
                "rejected_mean_error": 2.6490546933378276,
                "gap_rejected_minus_accepted": 1.3368172659199749
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.630995273590088,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0357282172203064,
                "rejected_mean_error": 2.2582247243881226,
                "gap_rejected_minus_accepted": 1.2224965071678162
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0553998053073883,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6565929914054017,
                "rejected_mean_error": 1.977808945779485,
                "gap_rejected_minus_accepted": 1.3212159543740833
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7007012128829957,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4650840894381205,
                "rejected_mean_error": 3.3856746196746825,
                "gap_rejected_minus_accepted": 1.920590530236562
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.03250515460968,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3061595520871208,
                "rejected_mean_error": 2.6989515773833745,
                "gap_rejected_minus_accepted": 1.3927920252962538
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6526355743408203,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.024027718067169,
                "rejected_mean_error": 2.290258566856384,
                "gap_rejected_minus_accepted": 1.266230848789215
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0286013185977936,
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
            "pearson": 0.9822627421086951,
            "spearman": 0.9747318788534446,
            "auroc_top30_bad": 0.9758133333333333,
            "mae": 0.10873585276038265,
            "mse": 0.02444783286153528,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6920725506053776,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05933846098184586
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2186034812927246
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7846025319099427
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1398778722127278
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
            "pearson": 0.9541843486060015,
            "spearman": 0.9408743700955969,
            "auroc_top30_worst": 0.9458529523809523,
            "pairwise_seed_ranking": 0.8952,
            "predicted_best_mean_error": 1.597500007033348,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06425112092494967,
            "gap_to_oracle": 0.005476075053215013,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8429002306461334
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1024348920163436
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3631564859867096
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5243588818479448
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.039750146865845,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6005441110663945,
                "rejected_mean_error": 2.1932359685897826,
                "gap_rejected_minus_accepted": 0.5926918575233882
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8634983599185944,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5238440383142189,
                "rejected_mean_error": 2.066852259178893,
                "gap_rejected_minus_accepted": 0.543008220864674
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6599483489990234,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3631564859867096,
                "rejected_mean_error": 1.956470107650757,
                "gap_rejected_minus_accepted": 0.5933136216640473
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3244695365428925,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1035430295208393,
                "rejected_mean_error": 1.845632500302448,
                "gap_rejected_minus_accepted": 0.7420894707816088
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.035345458984375,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6089872394667732,
                "rejected_mean_error": 2.136626124382019,
                "gap_rejected_minus_accepted": 0.5276388849152458
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8609682321548462,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5319785628726776,
                "rejected_mean_error": 2.046949059244186,
                "gap_rejected_minus_accepted": 0.5149704963715085
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.672176480293274,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3765804476737975,
                "rejected_mean_error": 1.946921808242798,
                "gap_rejected_minus_accepted": 0.5703413605690004
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.323017418384552,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1102779886079213,
                "rejected_mean_error": 1.8475415438891731,
                "gap_rejected_minus_accepted": 0.7372635552812519
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
      "best_epoch": 91,
      "best_calib_loss": 0.011913173831999302,
      "train_time_sec": 50.67736601829529,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.999539101747478,
            "spearman": 0.998271429066146,
            "auroc_top30_bad": 0.9993373333333333,
            "mae": 0.025415279920753348,
            "mse": 0.0011472810111504866,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8071438350844312,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.000802094005048275
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1999029907643795
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6187785414904357
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9865687399367491
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
            "pearson": 0.9995827592203406,
            "spearman": 0.998709047700331,
            "auroc_top30_worst": 0.9993933333333334,
            "pairwise_seed_ranking": 0.9699,
            "predicted_best_mean_error": 1.7027751961350441,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.0916492014825343,
            "gap_to_oracle": 0.0011811484098434022,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7229952399134636
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8795901995420456
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0841013453364372
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.305242746090889
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.137995409965516,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899903989301788,
                "rejected_mean_error": 4.441067194461822,
                "gap_rejected_minus_accepted": 2.9510767955316433
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0205798745155334,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.305242746090889,
                "rejected_mean_error": 3.2246640756607055,
                "gap_rejected_minus_accepted": 1.9194213295698164
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5173924565315247,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0841013453364372,
                "rejected_mean_error": 2.486094811630249,
                "gap_rejected_minus_accepted": 1.4019934662938116
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1006484031677246,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8795901995420456,
                "rejected_mean_error": 2.086934038130442,
                "gap_rejected_minus_accepted": 1.2073438385883966
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1728445053100587,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4917491519782278,
                "rejected_mean_error": 4.518501608371735,
                "gap_rejected_minus_accepted": 3.026752456393507
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.035052239894867,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3020513692299525,
                "rejected_mean_error": 3.2715434827804564,
                "gap_rejected_minus_accepted": 1.969492113550504
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5135080218315125,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0770106409192086,
                "rejected_mean_error": 2.5118381543159485,
                "gap_rejected_minus_accepted": 1.4348275133967399
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0958385467529297,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8670482612848281,
                "rejected_mean_error": 2.103549776395162,
                "gap_rejected_minus_accepted": 1.236501515110334
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9899881687107777,
            "spearman": 0.9808087975302822,
            "auroc_top30_bad": 0.993464380952381,
            "mae": 0.11979828105653141,
            "mse": 0.02687053051106444,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.881247683829594,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1168227089047432
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2133824615716934
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5855025271058083
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0190503286123276
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
            "pearson": 0.995253218506686,
            "spearman": 0.9948086238775194,
            "auroc_top30_worst": 0.9997287619047619,
            "pairwise_seed_ranking": 0.9148,
            "predicted_best_mean_error": 1.9930239454507828,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11145705926418326,
            "gap_to_oracle": 0.004128715753555223,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6270902602672577
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8660987782745789
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2217300496578216
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5481582146400072
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.064912605285644,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8426799332035912,
                "rejected_mean_error": 4.214863838195801,
                "gap_rejected_minus_accepted": 2.3721839049922098
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.830203890800476,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5468772664713886,
                "rejected_mean_error": 3.6755556100473616,
                "gap_rejected_minus_accepted": 2.128678343575973
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7545010447502136,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2217300496578216,
                "rejected_mean_error": 2.938066597747803,
                "gap_rejected_minus_accepted": 1.7163365480899813
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1442863047122955,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8679288449569251,
                "rejected_mean_error": 2.4847504548100297,
                "gap_rejected_minus_accepted": 1.6168216098531045
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.1464332103729244,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.86610019048055,
                "rejected_mean_error": 4.249908332824707,
                "gap_rejected_minus_accepted": 2.383808142344157
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.882329821586609,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548626369333522,
                "rejected_mean_error": 3.7358879059080095,
                "gap_rejected_minus_accepted": 2.181025268974657
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.77656888961792,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2227279586791993,
                "rejected_mean_error": 2.9862340507507326,
                "gap_rejected_minus_accepted": 1.7635060920715333
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.156640738248825,
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
            "pearson": 0.9890837889860318,
            "spearman": 0.9844342214842187,
            "auroc_top30_bad": 0.9842449523809524,
            "mae": 0.1097966582057068,
            "mse": 0.02580106177471518,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7392922369075652,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.061071137249469755
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18499358792304993
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6268686718344688
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.041864414493243
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
            "pearson": 0.9881863645104944,
            "spearman": 0.9826567179882998,
            "auroc_top30_worst": 0.9728975238095239,
            "pairwise_seed_ranking": 0.9024,
            "predicted_best_mean_error": 1.5857196326255798,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07142350983619683,
            "gap_to_oracle": 0.005822111129760721,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4000246937274933
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6546685678454546
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0257851124763488
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3103885090808625
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.541403102874756,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.460263835536109,
                "rejected_mean_error": 3.327390188217163,
                "gap_rejected_minus_accepted": 1.867126352681054
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9192759990692139,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.309834426660548,
                "rejected_mean_error": 2.6562483409723154,
                "gap_rejected_minus_accepted": 1.3464139143117675
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5916529297828674,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0257851124763488,
                "rejected_mean_error": 2.26816782913208,
                "gap_rejected_minus_accepted": 1.242382716655731
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.00715571641922,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6558697800666761,
                "rejected_mean_error": 1.9780505307837764,
                "gap_rejected_minus_accepted": 1.3221807507171004
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.706281638145447,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.466823774708642,
                "rejected_mean_error": 3.37001745223999,
                "gap_rejected_minus_accepted": 1.9031936775313483
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9223272502422333,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3046475919810208,
                "rejected_mean_error": 2.7034394589681474,
                "gap_rejected_minus_accepted": 1.3987918669871267
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6112852692604065,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0151805109977723,
                "rejected_mean_error": 2.299105773925781,
                "gap_rejected_minus_accepted": 1.283925262928009
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9901357591152191,
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
            "pearson": 0.9794881266021314,
            "spearman": 0.9762184813840137,
            "auroc_top30_bad": 0.9822666666666667,
            "mae": 0.1225618237038154,
            "mse": 0.029480198243668643,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6733850465848249,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10603183966875077
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22815395042896272
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7844511681556702
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1382377991358439
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
            "pearson": 0.9635170560497791,
            "spearman": 0.9610422596110463,
            "auroc_top30_worst": 0.9658636190476191,
            "pairwise_seed_ranking": 0.8964,
            "predicted_best_mean_error": 1.5983976516723633,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06335347628593446,
            "gap_to_oracle": 0.0063737196922302175,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8414238426685333
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1041572656577978
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3586076336383819
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5193619386537243
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0076900243759157,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5978983600669436,
                "rejected_mean_error": 2.217047727584839,
                "gap_rejected_minus_accepted": 0.6191493675178954
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8416892886161804,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.51880502207811,
                "rejected_mean_error": 2.081937109700407,
                "gap_rejected_minus_accepted": 0.5631320876222969
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.626878023147583,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3586076336383819,
                "rejected_mean_error": 1.9610189599990844,
                "gap_rejected_minus_accepted": 0.6024113263607025
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2661319375038147,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1047773525928155,
                "rejected_mean_error": 1.8452201810692266,
                "gap_rejected_minus_accepted": 0.7404428284764111
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0079097986221313,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6032799892955356,
                "rejected_mean_error": 2.187991375923157,
                "gap_rejected_minus_accepted": 0.5847113866276212
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8497981131076813,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5260095899117823,
                "rejected_mean_error": 2.0646664869217646,
                "gap_rejected_minus_accepted": 0.5386568970099823
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6464842557907104,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3691071372032166,
                "rejected_mean_error": 1.954395118713379,
                "gap_rejected_minus_accepted": 0.5852879815101624
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2648204863071442,
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
    },
    {
      "variant": "full_engineered_simvla_focused",
      "feature_mode": "M2_engineered",
      "model_kind": "mlp_big",
      "train_setting": "simvla_focused",
      "train_rows": 10000,
      "input_dim": 1562,
      "best_epoch": 100,
      "best_calib_loss": 0.011964534409344196,
      "train_time_sec": 46.6933217048645,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997909379931035,
            "spearman": 0.9987299252929566,
            "auroc_top30_bad": 0.9998614761904762,
            "mae": 0.021714458905328138,
            "mse": 0.0008773504546595003,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7993162338684374,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0004664169922471046
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19979040498137474
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6185724278897047
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9863726791203022
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
            "pearson": 0.9998277800472044,
            "spearman": 0.9995913483356148,
            "auroc_top30_worst": 0.9999104761904762,
            "pairwise_seed_ranking": 0.9621,
            "predicted_best_mean_error": 1.7028317261338235,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09159267148375494,
            "gap_to_oracle": 0.0012376784086227666,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7219498561024665
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8789597381353378
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0837647107958794
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.305152065396309
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1033336639404303,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899380582637256,
                "rejected_mean_error": 4.4415382604599,
                "gap_rejected_minus_accepted": 2.9516002021961745
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9961638152599335,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.305152065396309,
                "rejected_mean_error": 3.2249361177444458,
                "gap_rejected_minus_accepted": 1.9197840523481369
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4957867860794067,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0837647107958794,
                "rejected_mean_error": 2.486431446170807,
                "gap_rejected_minus_accepted": 1.4026667353749276
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0765540897846222,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8789597381353378,
                "rejected_mean_error": 2.087144191932678,
                "gap_rejected_minus_accepted": 1.2081844537973403
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1546965837478647,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.00765061378479,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.301984580874443,
                "rejected_mean_error": 3.271743847846985,
                "gap_rejected_minus_accepted": 1.969759266972542
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4863952994346619,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0764070175290108,
                "rejected_mean_error": 2.512441777706146,
                "gap_rejected_minus_accepted": 1.4360347601771353
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.068590372800827,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8664964920282364,
                "rejected_mean_error": 2.1037336994806926,
                "gap_rejected_minus_accepted": 1.237237207452456
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9905532249845735,
            "spearman": 0.9831734555887311,
            "auroc_top30_bad": 0.9899017142857143,
            "mae": 0.12156463736671248,
            "mse": 0.025318637768971183,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8819985988462283,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06986275911331177
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20143854606151582
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5885776628136635
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0207994451284408
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
            "pearson": 0.9917240096326152,
            "spearman": 0.9872596275581617,
            "auroc_top30_worst": 0.9989424761904763,
            "pairwise_seed_ranking": 0.926,
            "predicted_best_mean_error": 1.9921978133916856,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11228319132328046,
            "gap_to_oracle": 0.0033025836944580167,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6243486187458038
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8731572462771183
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2310946504116058
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5497434257126566
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.149435329437258,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8416408649815454,
                "rejected_mean_error": 4.224215452194214,
                "gap_rejected_minus_accepted": 2.3825745872126682
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7944588661193848,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5484518178817175,
                "rejected_mean_error": 3.6708420168477507,
                "gap_rejected_minus_accepted": 2.122390198966033
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.778636395931244,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2310946504116058,
                "rejected_mean_error": 2.9287019969940187,
                "gap_rejected_minus_accepted": 1.6976073465824129
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2098315358161926,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8745985026367176,
                "rejected_mean_error": 2.4825224901848695,
                "gap_rejected_minus_accepted": 1.607923987548152
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.252984857559204,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8649051147037081,
                "rejected_mean_error": 4.260664014816284,
                "gap_rejected_minus_accepted": 2.3957589001125763
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.911795675754547,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5549441582378856,
                "rejected_mean_error": 3.7356459299723306,
                "gap_rejected_minus_accepted": 2.1807017717344452
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7922537922859192,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2352552146911622,
                "rejected_mean_error": 2.9737067947387694,
                "gap_rejected_minus_accepted": 1.7384515800476072
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2224274575710297,
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
            "pearson": 0.9905372543787223,
            "spearman": 0.9833272736574232,
            "auroc_top30_bad": 0.9791321904761905,
            "mae": 0.10620080196347845,
            "mse": 0.023768813482564714,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7359696989834663,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04197088241577149
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18307565245628357
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6297674572348595
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0426652221282324
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
            "pearson": 0.9885509995482681,
            "spearman": 0.9764462175015793,
            "auroc_top30_worst": 0.966134857142857,
            "pairwise_seed_ranking": 0.896,
            "predicted_best_mean_error": 1.5854873530864715,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07165578937530515,
            "gap_to_oracle": 0.005589831590652405,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3994347310066223
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6546212600973936
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0325188073158265
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3098485095541614
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.451309490203858,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4584602244165208,
                "rejected_mean_error": 3.343622688293457,
                "gap_rejected_minus_accepted": 1.8851624638769364
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9280570447444916,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.308986277755831,
                "rejected_mean_error": 2.658787368204647,
                "gap_rejected_minus_accepted": 1.349801090448816
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6304497122764587,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0325188073158265,
                "rejected_mean_error": 2.2614341342926028,
                "gap_rejected_minus_accepted": 1.2289153269767763
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0716110169887543,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6558226383151338,
                "rejected_mean_error": 1.978066278241869,
                "gap_rejected_minus_accepted": 1.3222436399267352
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5557626724243163,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.463609338071611,
                "rejected_mean_error": 3.3989473819732665,
                "gap_rejected_minus_accepted": 1.9353380439016554
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.961399883031845,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3044732493512772,
                "rejected_mean_error": 2.7039569521707203,
                "gap_rejected_minus_accepted": 1.3994837028194431
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.656639039516449,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0212811760902405,
                "rejected_mean_error": 2.293005108833313,
                "gap_rejected_minus_accepted": 1.2717239327430725
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0616575181484222,
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
            "pearson": 0.9871892491679878,
            "spearman": 0.9802375375334625,
            "auroc_top30_bad": 0.9826255238095238,
            "mae": 0.10501712344149128,
            "mse": 0.020670235973696462,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6824414958980549,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.060461247444152835
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21712114386558531
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.783395823097229
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1378702665964762
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
            "pearson": 0.9627962134063632,
            "spearman": 0.9534283580341492,
            "auroc_top30_worst": 0.9599664761904761,
            "pairwise_seed_ranking": 0.908,
            "predicted_best_mean_error": 1.5978444011211395,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06390672683715826,
            "gap_to_oracle": 0.0058204691410064235,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8471461298465729
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1058513977779791
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3608923828601838
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.521517653613965
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0264488697052,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5978861604531607,
                "rejected_mean_error": 2.217157524108887,
                "gap_rejected_minus_accepted": 0.6192713636557261
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.849821925163269,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.520996082204383,
                "rejected_mean_error": 2.0753779297057813,
                "gap_rejected_minus_accepted": 0.5543818475013982
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6695156693458557,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3608923828601838,
                "rejected_mean_error": 1.9587342107772827,
                "gap_rejected_minus_accepted": 0.597841827917099
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3381526172161102,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1070475564025843,
                "rejected_mean_error": 1.8444618312373615,
                "gap_rejected_minus_accepted": 0.7374142748347772
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0193086385726926,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6046582341194153,
                "rejected_mean_error": 2.17558717250824,
                "gap_rejected_minus_accepted": 0.5709289383888245
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8473025262355804,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.527410276114622,
                "rejected_mean_error": 2.0605088945419068,
                "gap_rejected_minus_accepted": 0.5330986184272848
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6926656365394592,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3710599780082702,
                "rejected_mean_error": 1.9524422779083253,
                "gap_rejected_minus_accepted": 0.5813822999000551
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3420116603374481,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1158619125684102,
                "rejected_mean_error": 1.8456603288650513,
                "gap_rejected_minus_accepted": 0.7297984162966411
              }
            ]
          }
        }
      }
    }
  ]
}
```
