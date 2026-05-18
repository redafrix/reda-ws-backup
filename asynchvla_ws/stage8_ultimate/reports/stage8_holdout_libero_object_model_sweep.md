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
      "best_epoch": 33,
      "best_calib_loss": 0.09690046310424805,
      "train_time_sec": 11.32198190689087,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.8984445886098809,
            "spearman": 0.8055465324169037,
            "auroc_top30_bad": 0.8758962619047618,
            "mae": 0.21549334211945534,
            "mse": 0.2351103069383159,
            "expert_lt_perturb_large": 0.985,
            "expert_lt_other_task": 0.507,
            "expert_lt_simvla_seed0": 0.984,
            "same_context_pred_std": 0.7844956813512997,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.613705628991127
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.567715773409605
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7172630711644888
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0151302677194278
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
            "pearson": 0.9978372741267105,
            "spearman": 0.9954038181359322,
            "auroc_top30_worst": 0.9985020952380952,
            "pairwise_seed_ranking": 0.8313,
            "predicted_best_mean_error": 1.7117316836714744,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.082692713946104,
            "gap_to_oracle": 0.010137635946273704,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7310088904500007
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8838402929544449
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.085425824201107
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3055448781569798
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.051021409034729,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4901814054846763,
                "rejected_mean_error": 4.439348135471344,
                "gap_rejected_minus_accepted": 2.949166729986668
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9988314807415009,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3055448781569798,
                "rejected_mean_error": 3.223757679462433,
                "gap_rejected_minus_accepted": 1.9182128013054531
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5027227997779846,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.085425824201107,
                "rejected_mean_error": 2.4847703327655792,
                "gap_rejected_minus_accepted": 1.3993445085644722
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.082377403974533,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8838402929544449,
                "rejected_mean_error": 2.085517340326309,
                "gap_rejected_minus_accepted": 1.2016770473718643
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.129109287261963,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4917796128657128,
                "rejected_mean_error": 4.518227460384369,
                "gap_rejected_minus_accepted": 3.0264478475186563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0157275795936584,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.302654429634412,
                "rejected_mean_error": 3.2697343015670777,
                "gap_rejected_minus_accepted": 1.9670798719326656
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.504529595375061,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0776717513203622,
                "rejected_mean_error": 2.511177043914795,
                "gap_rejected_minus_accepted": 1.4335052925944327
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0862887799739838,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8710920411348343,
                "rejected_mean_error": 2.1022018497784933,
                "gap_rejected_minus_accepted": 1.2311098086436592
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.7996070425184716,
            "spearman": 0.6732936994122192,
            "auroc_top30_bad": 0.7487352380952381,
            "mae": 0.4885624865114689,
            "mse": 0.5316674865328831,
            "expert_lt_perturb_large": 0.992,
            "expert_lt_other_task": 0.496,
            "expert_lt_simvla_seed0": 0.936,
            "same_context_pred_std": 0.8903557523847014,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0057000687718392
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7156839508771896
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7946328526139259
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1222241844177245
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
            "pearson": 0.8057404165994356,
            "spearman": 0.7254775853296546,
            "auroc_top30_worst": 0.8461531428571429,
            "pairwise_seed_ranking": 0.7508,
            "predicted_best_mean_error": 2.010802610993385,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.09367839372158082,
            "gap_to_oracle": 0.021907381296157658,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2134955778121947
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.260612570704558
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.5004921269893645
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5977309030701103
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.194786548614502,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8430032006104786,
                "rejected_mean_error": 4.2119544315338135,
                "gap_rejected_minus_accepted": 2.3689512309233347
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.812385380268097,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5971517329727445,
                "rejected_mean_error": 3.5250534531407465,
                "gap_rejected_minus_accepted": 1.927901720168002
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.749844253063202,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.5004921269893645,
                "rejected_mean_error": 2.65930452041626,
                "gap_rejected_minus_accepted": 1.1588123934268955
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2183133661746979,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.2615816349419542,
                "rejected_mean_error": 2.353252777899342,
                "gap_rejected_minus_accepted": 1.091671142957388
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.230950880050659,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8660761578877767,
                "rejected_mean_error": 4.250124626159668,
                "gap_rejected_minus_accepted": 2.384048468271891
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8430910110473633,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6101941373896471,
                "rejected_mean_error": 3.571649960109166,
                "gap_rejected_minus_accepted": 1.9614558227195187
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7933674454689026,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.516835277557373,
                "rejected_mean_error": 2.6921267318725586,
                "gap_rejected_minus_accepted": 1.1752914543151856
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.202196478843689,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.2217005004012396,
                "rejected_mean_error": 2.401888340392852,
                "gap_rejected_minus_accepted": 1.1801878399916126
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6389902232716421,
            "spearman": 0.5265831680932392,
            "auroc_top30_bad": 0.6484015238095238,
            "mae": 0.5045176321834326,
            "mse": 0.6715332729293028,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.508,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.6857716434165683,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8213082028627395
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9996134185314178
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8921677903056144
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1294038734674454
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
            "pearson": 0.8718079589270886,
            "spearman": 0.8035767042410907,
            "auroc_top30_worst": 0.843599238095238,
            "pairwise_seed_ranking": 0.7812,
            "predicted_best_mean_error": 1.6012181396484375,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.05592500281333912,
            "gap_to_oracle": 0.02132061815261843,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4331564564704895
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7856883477324095
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1172629092216493
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.355779553590807
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.056358623504639,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.475963625854916,
                "rejected_mean_error": 3.1860920753479003,
                "gap_rejected_minus_accepted": 1.7101284494929843
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.787946343421936,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3557182977268256,
                "rejected_mean_error": 2.5188899154480273,
                "gap_rejected_minus_accepted": 1.1631716177212017
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.515981376171112,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1172629092216493,
                "rejected_mean_error": 2.1766900323867797,
                "gap_rejected_minus_accepted": 1.0594271231651304
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0476047694683075,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7854485504162578,
                "rejected_mean_error": 1.9347654132603835,
                "gap_rejected_minus_accepted": 1.1493168628441257
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0896874666213985,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4818062551816304,
                "rejected_mean_error": 3.2351751279830934,
                "gap_rejected_minus_accepted": 1.753368872801463
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8266207575798035,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3471011659678291,
                "rejected_mean_error": 2.5774264695152405,
                "gap_rejected_minus_accepted": 1.2303253035474113
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5427160859107971,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1019128861427308,
                "rejected_mean_error": 2.212373398780823,
                "gap_rejected_minus_accepted": 1.1104605126380922
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9995332360267639,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.78166772732659,
                "rejected_mean_error": 1.9520894053148077,
                "gap_rejected_minus_accepted": 1.1704216779882177
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.48807254868628924,
            "spearman": 0.3675344878780972,
            "auroc_top30_bad": 0.5698899047619048,
            "mae": 0.48644499200880525,
            "mse": 0.6692662302070039,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.496,
            "expert_lt_simvla_seed0": 0.976,
            "same_context_pred_std": 0.6309684664297512,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.1519310606718063
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.070987619304657
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0531687322854997
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2653494241555532
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
            "pearson": 0.6909249508163144,
            "spearman": 0.5710108691269563,
            "auroc_top30_worst": 0.696448,
            "pairwise_seed_ranking": 0.732,
            "predicted_best_mean_error": 1.6146127796173095,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.04713834834098818,
            "gap_to_oracle": 0.0225888476371765,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9442159297466278
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.301656103764589
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.464255390405655
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.575709338794385
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.8990084171295167,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6269590186278025,
                "rejected_mean_error": 1.9555018005371094,
                "gap_rejected_minus_accepted": 0.32854278190930697
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7492358088493347,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5755606571981722,
                "rejected_mean_error": 1.9120328601556844,
                "gap_rejected_minus_accepted": 0.33647220295751223
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5242775678634644,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.464255390405655,
                "rejected_mean_error": 1.8553712032318115,
                "gap_rejected_minus_accepted": 0.3911158128261565
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3180880546569824,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.301099754846134,
                "rejected_mean_error": 1.7796396987796974,
                "gap_rejected_minus_accepted": 0.47853994393356336
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.905975329875946,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6310775685310364,
                "rejected_mean_error": 1.93781316280365,
                "gap_rejected_minus_accepted": 0.30673559427261354
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.737359881401062,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5720099449795197,
                "rejected_mean_error": 1.9281257504508609,
                "gap_rejected_minus_accepted": 0.35611580547134114
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5337017178535461,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4565692830085755,
                "rejected_mean_error": 1.86693297290802,
                "gap_rejected_minus_accepted": 0.4103636898994445
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3248369097709656,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.3044097546547178,
                "rejected_mean_error": 1.7821388633493433,
                "gap_rejected_minus_accepted": 0.4777291086946256
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
      "best_epoch": 71,
      "best_calib_loss": 0.035903677344322205,
      "train_time_sec": 14.608626127243042,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9981855541908801,
            "spearman": 0.9954698900434548,
            "auroc_top30_bad": 0.9988034285714285,
            "mae": 0.05174868757389486,
            "mse": 0.004478672945865629,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7929687481351004,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05903398574888706
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20022797148823737
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6191281459778547
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9870313587168853
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
            "pearson": 0.9992365616200322,
            "spearman": 0.9981342704532813,
            "auroc_top30_worst": 0.9995601904761906,
            "pairwise_seed_ranking": 0.9204,
            "predicted_best_mean_error": 1.7043605015277863,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09006389608979215,
            "gap_to_oracle": 0.0027664538025855556,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.723782465994358
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8803500004529953
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0844680684924126
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.305403702600797
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1281734704971327,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.490039182656341,
                "rejected_mean_error": 4.4406281409263615,
                "gap_rejected_minus_accepted": 2.9505889582700204
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0072834491729736,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.305403702600797,
                "rejected_mean_error": 3.2241812061309814,
                "gap_rejected_minus_accepted": 1.9187775035301844
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4870046973228455,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0844680684924126,
                "rejected_mean_error": 2.4857280884742736,
                "gap_rejected_minus_accepted": 1.401260019981861
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.067717283964157,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8803500004529953,
                "rejected_mean_error": 2.086680771160126,
                "gap_rejected_minus_accepted": 1.2063307707071305
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1792439699172976,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491752867334419,
                "rejected_mean_error": 4.518468170166016,
                "gap_rejected_minus_accepted": 3.026715302831597
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.017721712589264,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3024539587100348,
                "rejected_mean_error": 3.27033571434021,
                "gap_rejected_minus_accepted": 1.967881755630175
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.486146628856659,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0770455926060676,
                "rejected_mean_error": 2.5118032026290895,
                "gap_rejected_minus_accepted": 1.434757610023022
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0582334995269775,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8680746995210648,
                "rejected_mean_error": 2.103207630316416,
                "gap_rejected_minus_accepted": 1.2351329307953516
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9623307890932474,
            "spearman": 0.9456418301149604,
            "auroc_top30_bad": 0.9663165714285713,
            "mae": 0.24052233122736216,
            "mse": 0.1067847846510671,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.8311211654546705,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11848252075910569
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23049640448093414
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6173040980696678
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0336402346690496
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
            "pearson": 0.9743680437984186,
            "spearman": 0.9615594234029864,
            "auroc_top30_worst": 0.9903451428571428,
            "pairwise_seed_ranking": 0.884,
            "predicted_best_mean_error": 1.9961112602949143,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.10836974442005176,
            "gap_to_oracle": 0.007216030597686718,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6432747275829315
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9371764821310838
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2400662995815277
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5554426937405743
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.135945081710815,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.841613898038864,
                "rejected_mean_error": 4.224458154678345,
                "gap_rejected_minus_accepted": 2.3828442566394807
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8408140540122986,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.554187522849253,
                "rejected_mean_error": 3.6536715518171414,
                "gap_rejected_minus_accepted": 2.0994840289678884
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.965743064880371,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2400662995815277,
                "rejected_mean_error": 2.9197303478240966,
                "gap_rejected_minus_accepted": 1.6796640482425689
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4039375483989716,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9388684861766644,
                "rejected_mean_error": 2.461053434850821,
                "gap_rejected_minus_accepted": 1.5221849486741563
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.189318990707397,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8647513760460748,
                "rejected_mean_error": 4.262047662734985,
                "gap_rejected_minus_accepted": 2.3972962866889103
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.9032158851623535,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5605862421147965,
                "rejected_mean_error": 3.718898792115469,
                "gap_rejected_minus_accepted": 2.1583125500006726
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9876823425292969,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2426230278015136,
                "rejected_mean_error": 2.966338981628418,
                "gap_rejected_minus_accepted": 1.7237159538269045
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3953346610069275,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9213565077100482,
                "rejected_mean_error": 2.503073749695232,
                "gap_rejected_minus_accepted": 1.5817172419851842
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9517758635359166,
            "spearman": 0.9486357792506599,
            "auroc_top30_bad": 0.9609531428571428,
            "mae": 0.22464801993966102,
            "mse": 0.09454134738833588,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6400961667743543,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11850099372863769
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.25068442046642303
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6431044457316398
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0516233291228612
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
            "pearson": 0.9644641019003166,
            "spearman": 0.9592637425047953,
            "auroc_top30_worst": 0.9693897142857142,
            "pairwise_seed_ranking": 0.8304,
            "predicted_best_mean_error": 1.5930018101930619,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.06414133226871477,
            "gap_to_oracle": 0.013104288697242783,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5158460223674775
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7038986518596991
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.035916554737091
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3099395840534016
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5541555166244514,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.459486448764801,
                "rejected_mean_error": 3.3343866691589357,
                "gap_rejected_minus_accepted": 1.8749002203941347
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.921213984489441,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3091882397932584,
                "rejected_mean_error": 2.6581827725846168,
                "gap_rejected_minus_accepted": 1.3489945327913584
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6443374752998352,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.035916554737091,
                "rejected_mean_error": 2.258036386871338,
                "gap_rejected_minus_accepted": 1.2221198321342468
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1204157173633575,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7053956943578994,
                "rejected_mean_error": 1.961506655465577,
                "gap_rejected_minus_accepted": 1.2561109611076775
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.570992040634155,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.465161349773407,
                "rejected_mean_error": 3.3849792766571043,
                "gap_rejected_minus_accepted": 1.9198179268836972
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9344534873962402,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.304008439581662,
                "rejected_mean_error": 2.7053366256138633,
                "gap_rejected_minus_accepted": 1.4013281860322013
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.659000039100647,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0264543232917787,
                "rejected_mean_error": 2.287831961631775,
                "gap_rejected_minus_accepted": 1.2613776383399962
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1129449605941772,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7093466482465229,
                "rejected_mean_error": 1.9764542608337605,
                "gap_rejected_minus_accepted": 1.2671076125872376
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9358428498718068,
            "spearman": 0.9251717896702047,
            "auroc_top30_bad": 0.945056761904762,
            "mae": 0.2056359628662467,
            "mse": 0.08296915681809448,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.968,
            "expert_lt_simvla_seed0": 0.984,
            "same_context_pred_std": 0.6308916917750366,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11955345809459686
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.27035082795619964
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8130650680780411
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1480671482086182
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
            "pearson": 0.8167638613861821,
            "spearman": 0.8417488968632941,
            "auroc_top30_worst": 0.8974201904761906,
            "pairwise_seed_ranking": 0.8088,
            "predicted_best_mean_error": 1.6057030193805695,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.05604810857772824,
            "gap_to_oracle": 0.01367908740043644,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.017365008354187
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1819992943260915
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.394563517332077
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5318641561244342
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.155718350410462,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5975790050559573,
                "rejected_mean_error": 2.219921922683716,
                "gap_rejected_minus_accepted": 0.6223429176277586
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9042201042175293,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.531372112455592,
                "rejected_mean_error": 2.044316139464942,
                "gap_rejected_minus_accepted": 0.5129440270093502
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6068392992019653,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.394563517332077,
                "rejected_mean_error": 1.9250630763053893,
                "gap_rejected_minus_accepted": 0.5304995589733124
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.404502034187317,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1829758340748735,
                "rejected_mean_error": 1.8190983830928293,
                "gap_rejected_minus_accepted": 0.6361225490179558
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.174026036262512,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6036825442314149,
                "rejected_mean_error": 2.184368381500244,
                "gap_rejected_minus_accepted": 0.580685837268829
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9202232956886292,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5363541041466005,
                "rejected_mean_error": 2.0339613414946056,
                "gap_rejected_minus_accepted": 0.49760723734800516
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6121890544891357,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3961157231330872,
                "rejected_mean_error": 1.9273865327835082,
                "gap_rejected_minus_accepted": 0.5312708096504211
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3982796370983124,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1979872149134438,
                "rejected_mean_error": 1.8179924462568313,
                "gap_rejected_minus_accepted": 0.6200052313433875
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
      "best_epoch": 80,
      "best_calib_loss": 0.011893178336322308,
      "train_time_sec": 35.704198598861694,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996931932055045,
            "spearman": 0.9986907223982527,
            "auroc_top30_bad": 0.999699380952381,
            "mae": 0.02116010422008112,
            "mse": 0.0008753237744395383,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7989189827109734,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0013232924938201905
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19970005800127982
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6186140475004911
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9864202288925648
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
            "pearson": 0.9996777024218367,
            "spearman": 0.9993646752865568,
            "auroc_top30_worst": 0.9997112380952381,
            "pairwise_seed_ranking": 0.9537,
            "predicted_best_mean_error": 1.7032309954166411,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.0911934022009373,
            "gap_to_oracle": 0.0016369476914404046,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7230975925326347
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8791320270299912
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.083904745900631
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3052045129060745
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.103269648551942,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899437088900143,
                "rejected_mean_error": 4.441487404823303,
                "gap_rejected_minus_accepted": 2.951543695933289
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0061853528022766,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3052045129060745,
                "rejected_mean_error": 3.224778775215149,
                "gap_rejected_minus_accepted": 1.9195742623090746
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.514126479625702,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.083904745900631,
                "rejected_mean_error": 2.4862914110660554,
                "gap_rejected_minus_accepted": 1.4023866651654244
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0926665663719177,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8791320270299912,
                "rejected_mean_error": 2.0870867623011273,
                "gap_rejected_minus_accepted": 1.2079547352711362
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1757642269134525,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4916475952002737,
                "rejected_mean_error": 4.519415619373322,
                "gap_rejected_minus_accepted": 3.0277680241730485
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0084052085876465,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3021474419037502,
                "rejected_mean_error": 3.2712552647590636,
                "gap_rejected_minus_accepted": 1.9691078228553134
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5074452757835388,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0764331954121589,
                "rejected_mean_error": 2.5124155998229982,
                "gap_rejected_minus_accepted": 1.4359824044108394
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0943891108036041,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8666328288316727,
                "rejected_mean_error": 2.103688253879547,
                "gap_rejected_minus_accepted": 1.2370554250478745
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9917925583376879,
            "spearman": 0.9871112016845476,
            "auroc_top30_bad": 0.9942674285714286,
            "mae": 0.10964471548614092,
            "mse": 0.026566161010879545,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9296609591469913,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06573811930418015
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1965625226020813
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.58521424690485
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0190508418798447
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
            "pearson": 0.9917662892310455,
            "spearman": 0.9941591842298781,
            "auroc_top30_worst": 0.9959862857142857,
            "pairwise_seed_ranking": 0.9204,
            "predicted_best_mean_error": 1.9940633519887925,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11041765272617354,
            "gap_to_oracle": 0.005168122291564936,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6255542571544648
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8683080920615257
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.220887256383896
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5524993917263392
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.285702419281006,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.842167464653651,
                "rejected_mean_error": 4.219476055145264,
                "gap_rejected_minus_accepted": 2.3773085904916127
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.859451413154602,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5511099295720474,
                "rejected_mean_error": 3.662884666515996,
                "gap_rejected_minus_accepted": 2.111774736943949
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.853402018547058,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.220887256383896,
                "rejected_mean_error": 2.9389093910217285,
                "gap_rejected_minus_accepted": 1.7180221346378326
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2823392748832703,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8702265465031036,
                "rejected_mean_error": 2.4839829195016474,
                "gap_rejected_minus_accepted": 1.6137563729985438
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.327768087387085,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8657708411746554,
                "rejected_mean_error": 4.252872476577759,
                "gap_rejected_minus_accepted": 2.387101635403103
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.960425615310669,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5584830600310138,
                "rejected_mean_error": 3.7251415706816173,
                "gap_rejected_minus_accepted": 2.1666585106506036
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8649222254753113,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.219932942390442,
                "rejected_mean_error": 2.98902906703949,
                "gap_rejected_minus_accepted": 1.769096124649048
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.289660930633545,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8688368872990684,
                "rejected_mean_error": 2.5207675255556157,
                "gap_rejected_minus_accepted": 1.6519306382565473
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9921043159875582,
            "spearman": 0.9896187636807975,
            "auroc_top30_bad": 0.9920807619047618,
            "mae": 0.08380471135429107,
            "mse": 0.014878468573859722,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7771810848017222,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04382417643070221
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18361528158187868
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6264572506308556
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0395840987126033
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
            "pearson": 0.9904475406547096,
            "spearman": 0.9897190108921672,
            "auroc_top30_worst": 0.9851580952380953,
            "pairwise_seed_ranking": 0.882,
            "predicted_best_mean_error": 1.5883352745771409,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.06880786788463578,
            "gap_to_oracle": 0.008437753081321775,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4167518632411957
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.654404936119532
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.024188499546051
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3049226386079402
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7869904756546022,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.459389454152849,
                "rejected_mean_error": 3.3352596206665037,
                "gap_rejected_minus_accepted": 1.8758701665136548
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.02694571018219,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3042581934430175,
                "rejected_mean_error": 2.672941409741728,
                "gap_rejected_minus_accepted": 1.3686832162987104
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7085348963737488,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.024188499546051,
                "rejected_mean_error": 2.269764442062378,
                "gap_rejected_minus_accepted": 1.245575942516327
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1101824343204498,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6558861288780602,
                "rejected_mean_error": 1.9780450695479566,
                "gap_rejected_minus_accepted": 1.3221589406698964
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.9204721689224242,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4644762629932828,
                "rejected_mean_error": 3.3911450576782225,
                "gap_rejected_minus_accepted": 1.9266687946849397
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0408244132995605,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3011129632353144,
                "rejected_mean_error": 2.713931134768895,
                "gap_rejected_minus_accepted": 1.4128181715335804
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7195971012115479,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0142167115211487,
                "rejected_mean_error": 2.300069573402405,
                "gap_rejected_minus_accepted": 1.2858528618812561
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1096201539039612,
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
            "pearson": 0.9899972143411132,
            "spearman": 0.982987249537937,
            "auroc_top30_bad": 0.9837211428571428,
            "mae": 0.07885167689705268,
            "mse": 0.013054465175138457,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7285433685723339,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.057205447793006896
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2149772829055786
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7826668264389038
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.136572038904826
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
            "pearson": 0.975985697226982,
            "spearman": 0.9661823824527248,
            "auroc_top30_worst": 0.9673478095238094,
            "pairwise_seed_ranking": 0.9148,
            "predicted_best_mean_error": 1.5985954656600951,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06315566229820258,
            "gap_to_oracle": 0.006571533679962105,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8516852657794952
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1017529147748764
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3591982773303986
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5191661475627407
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0705690860748294,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5921014934380848,
                "rejected_mean_error": 2.2692195272445677,
                "gap_rejected_minus_accepted": 0.6771180338064828
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8890648782253265,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5185788833280764,
                "rejected_mean_error": 2.0826140809744693,
                "gap_rejected_minus_accepted": 0.5640351976463929
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7179154753684998,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3591982773303986,
                "rejected_mean_error": 1.960428316307068,
                "gap_rejected_minus_accepted": 0.6012300389766694
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4303731322288513,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1027085743963527,
                "rejected_mean_error": 1.8459112457175646,
                "gap_rejected_minus_accepted": 0.7432026713212119
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0667956590652463,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5973208101590475,
                "rejected_mean_error": 2.2416239881515505,
                "gap_rejected_minus_accepted": 0.644303177992503
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8923282325267792,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.524402321022462,
                "rejected_mean_error": 2.0694372691805403,
                "gap_rejected_minus_accepted": 0.5450349481580783
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7322770953178406,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3722515959739685,
                "rejected_mean_error": 1.951250659942627,
                "gap_rejected_minus_accepted": 0.5789990639686584
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4500089287757874,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1141011819006905,
                "rejected_mean_error": 1.8462535162023044,
                "gap_rejected_minus_accepted": 0.7321523343016139
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
      "best_epoch": 74,
      "best_calib_loss": 0.014101549983024597,
      "train_time_sec": 41.93081784248352,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.99924213656917,
            "spearman": 0.9976838685867907,
            "auroc_top30_bad": 0.9992604761904761,
            "mae": 0.031100450760745843,
            "mse": 0.0017233893684102408,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8037111819169656,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0031446447521448137
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20006476296782494
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6187628022402525
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9866739324231942
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
            "pearson": 0.9992696817723572,
            "spearman": 0.9980812145392025,
            "auroc_top30_worst": 0.9993773333333333,
            "pairwise_seed_ranking": 0.9626,
            "predicted_best_mean_error": 1.7035630056262017,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09086139199137677,
            "gap_to_oracle": 0.001968957901000934,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7248055937886239
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8809535397291184
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0843204471468926
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3054641095717747
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.130383610725403,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899479297995568,
                "rejected_mean_error": 4.441449416637421,
                "gap_rejected_minus_accepted": 2.951501486837864
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.009387791156769,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3054641095717747,
                "rejected_mean_error": 3.223999985218048,
                "gap_rejected_minus_accepted": 1.9185358756462734
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5085758566856384,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0843204471468926,
                "rejected_mean_error": 2.4858757098197937,
                "gap_rejected_minus_accepted": 1.401555262672901
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0867322981357574,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8809535397291184,
                "rejected_mean_error": 2.0864795914014183,
                "gap_rejected_minus_accepted": 1.2055260516722999
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.193407464027405,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4916700470778677,
                "rejected_mean_error": 4.519213552474976,
                "gap_rejected_minus_accepted": 3.027543505397108
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0300657153129578,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3020785638888677,
                "rejected_mean_error": 3.271461898803711,
                "gap_rejected_minus_accepted": 1.9693833349148433
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.504756212234497,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.077118653357029,
                "rejected_mean_error": 2.511730141878128,
                "gap_rejected_minus_accepted": 1.434611488521099
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0795955061912537,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8675436197519303,
                "rejected_mean_error": 2.103384656906128,
                "gap_rejected_minus_accepted": 1.2358410371541977
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9888888562084113,
            "spearman": 0.9780124096308833,
            "auroc_top30_bad": 0.9935649523809523,
            "mae": 0.1323780738196161,
            "mse": 0.031193772425270574,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8809250297435608,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11884718894958496
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2248401668071747
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5879590249657631
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.019374659069379
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
            "pearson": 0.9949052761332775,
            "spearman": 0.9935772426094354,
            "auroc_top30_worst": 0.9994666666666666,
            "pairwise_seed_ranking": 0.9244,
            "predicted_best_mean_error": 1.992057240843773,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11242376387119313,
            "gap_to_oracle": 0.0031620111465453515,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6282646596431732
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8655443557370932
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2222010915279389
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.549209974563198
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.0703755855560315,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8426833759678736,
                "rejected_mean_error": 4.214832853317261,
                "gap_rejected_minus_accepted": 2.372149477349387
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.805007517337799,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5472984091004032,
                "rejected_mean_error": 3.6742948731675313,
                "gap_rejected_minus_accepted": 2.126996464067128
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7243866920471191,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2222010915279389,
                "rejected_mean_error": 2.9375955558776856,
                "gap_rejected_minus_accepted": 1.7153944643497467
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.114940732717514,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8670562226741839,
                "rejected_mean_error": 2.485041949766804,
                "gap_rejected_minus_accepted": 1.6179857270926203
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.153279256820679,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8664221413930258,
                "rejected_mean_error": 4.247010774612427,
                "gap_rejected_minus_accepted": 2.3805886332194013
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8161286115646362,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.555659858938207,
                "rejected_mean_error": 3.73352154852852,
                "gap_rejected_minus_accepted": 2.177861689590313
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7499067187309265,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2214583129882812,
                "rejected_mean_error": 2.9875036964416504,
                "gap_rejected_minus_accepted": 1.7660453834533691
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1602535545825958,
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
            "pearson": 0.9871837274878728,
            "spearman": 0.9819205200972686,
            "auroc_top30_bad": 0.9844152380952381,
            "mae": 0.11977944480431252,
            "mse": 0.028028469135914072,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7351712750747318,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0690955416560173
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19886402492523195
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6276071934103966
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0415495765924454
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
            "pearson": 0.9881181335400764,
            "spearman": 0.9822568723563984,
            "auroc_top30_worst": 0.9716754285714286,
            "pairwise_seed_ranking": 0.894,
            "predicted_best_mean_error": 1.5864365677833556,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07070657467842101,
            "gap_to_oracle": 0.006539046287536543,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4192735636234283
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6547704249238356
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0255629242897033
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.309360394536305
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4936386346817025,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4589547424846225,
                "rejected_mean_error": 3.339172025680542,
                "gap_rejected_minus_accepted": 1.8802172831959196
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9166604578495026,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3084572345622703,
                "rejected_mean_error": 2.6603711173176383,
                "gap_rejected_minus_accepted": 1.351913882755368
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.586679995059967,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0255629242897033,
                "rejected_mean_error": 2.2683900173187257,
                "gap_rejected_minus_accepted": 1.2428270930290224
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9808250665664673,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6560970436269864,
                "rejected_mean_error": 1.9779746145677923,
                "gap_rejected_minus_accepted": 1.321877570940806
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6403588533401487,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4643141012721592,
                "rejected_mean_error": 3.392604513168335,
                "gap_rejected_minus_accepted": 1.9282904118961757
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9234278500080109,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3046209879100004,
                "rejected_mean_error": 2.7035184266075256,
                "gap_rejected_minus_accepted": 1.3988974386975253
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5817539691925049,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0150954003334045,
                "rejected_mean_error": 2.299190884590149,
                "gap_rejected_minus_accepted": 1.2840954842567445
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9632359743118286,
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
            "pearson": 0.9764514747082471,
            "spearman": 0.9787055807291472,
            "auroc_top30_bad": 0.9865127619047619,
            "mae": 0.12749666921267125,
            "mse": 0.033762662790609445,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6606309059755957,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09157327497005463
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.24226921887397765
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7837945086479187
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1375757905960082
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
            "pearson": 0.9727053204646948,
            "spearman": 0.9758168933228119,
            "auroc_top30_worst": 0.9796906666666666,
            "pairwise_seed_ranking": 0.892,
            "predicted_best_mean_error": 1.5981725873947144,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06357854056358336,
            "gap_to_oracle": 0.006148655414581317,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8485360786914825
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1020746438358076
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3585708424091338
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5168495564890314
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9795846700668338,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5945980914698707,
                "rejected_mean_error": 2.246750144958496,
                "gap_rejected_minus_accepted": 0.6521520534886251
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8436191976070404,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.516300507040899,
                "rejected_mean_error": 2.089434651521067,
                "gap_rejected_minus_accepted": 0.5731341444801681
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6319270730018616,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3585708424091338,
                "rejected_mean_error": 1.9610557512283324,
                "gap_rejected_minus_accepted": 0.6024849088191986
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.261248379945755,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1028861330149653,
                "rejected_mean_error": 1.8458519331800771,
                "gap_rejected_minus_accepted": 0.7429658001651118
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.964488673210144,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.603270964887407,
                "rejected_mean_error": 2.1880725955963136,
                "gap_rejected_minus_accepted": 0.5848016307089066
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.832432746887207,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5245981340739816,
                "rejected_mean_error": 2.068856046313331,
                "gap_rejected_minus_accepted": 0.5442579122393496
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6357576251029968,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3699890418052674,
                "rejected_mean_error": 1.953513214111328,
                "gap_rejected_minus_accepted": 0.5835241723060607
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2681530714035034,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1134193520697335,
                "rejected_mean_error": 1.8464832235785091,
                "gap_rejected_minus_accepted": 0.7330638715087756
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
      "best_epoch": 73,
      "best_calib_loss": 0.012577542103827,
      "train_time_sec": 29.214632749557495,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.999782563965125,
            "spearman": 0.9988305577807544,
            "auroc_top30_bad": 0.9998176190476191,
            "mae": 0.015435101244091903,
            "mse": 0.0005038585247303308,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8068222176019815,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0012269511520862579
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19979726375937462
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6185566470593215
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9864166153093179
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
            "pearson": 0.9998531515146989,
            "spearman": 0.9996331945933103,
            "auroc_top30_worst": 0.9999215238095238,
            "pairwise_seed_ranking": 0.9681,
            "predicted_best_mean_error": 1.7023747981786728,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09204959943890567,
            "gap_to_oracle": 0.0007807504534720344,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7217345339655876
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8789535760641098
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0838284743666649
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051250769217808
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1553110361099264,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899512385196156,
                "rejected_mean_error": 4.441419638156891,
                "gap_rejected_minus_accepted": 2.951468399637275
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0315256118774414,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051250769217808,
                "rejected_mean_error": 3.2250170831680296,
                "gap_rejected_minus_accepted": 1.9198920062462488
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.520415186882019,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0838284743666649,
                "rejected_mean_error": 2.4863676826000214,
                "gap_rejected_minus_accepted": 1.4025392082333565
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0904902517795563,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8789535760641098,
                "rejected_mean_error": 2.0871462459564207,
                "gap_rejected_minus_accepted": 1.2081926698923109
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2277327537536626,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0330920815467834,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019903146823246,
                "rejected_mean_error": 3.27172664642334,
                "gap_rejected_minus_accepted": 1.9697363317410153
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5140469074249268,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0765170286297798,
                "rejected_mean_error": 2.512331766605377,
                "gap_rejected_minus_accepted": 1.4358147379755972
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0849010050296783,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8665162054300308,
                "rejected_mean_error": 2.103727128346761,
                "gap_rejected_minus_accepted": 1.23721092291673
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9896629035991837,
            "spearman": 0.98151654929529,
            "auroc_top30_bad": 0.9897493333333334,
            "mae": 0.1235286910244809,
            "mse": 0.02753885192838361,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8752716792842495,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10212084192037582
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2046624948501587
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5872121289849281
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0206660154104232
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
            "pearson": 0.9924451450669809,
            "spearman": 0.989267715371338,
            "auroc_top30_worst": 0.9993843809523809,
            "pairwise_seed_ranking": 0.9236,
            "predicted_best_mean_error": 1.9922175097465515,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11226349496841448,
            "gap_to_oracle": 0.003322280049324,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6380813271999359
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8707498857417167
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2296723981380462
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
                "threshold": 4.062600421905518,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8425918374326493,
                "rejected_mean_error": 4.215656700134278,
                "gap_rejected_minus_accepted": 2.3730648627016286
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.80431067943573,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.547689249415026,
                "rejected_mean_error": 3.673124849605865,
                "gap_rejected_minus_accepted": 2.1254356001908388
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.736802101135254,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2296723981380462,
                "rejected_mean_error": 2.9301242492675783,
                "gap_rejected_minus_accepted": 1.7004518511295321
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1835186779499054,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8713893337181201,
                "rejected_mean_error": 2.4835944964511674,
                "gap_rejected_minus_accepted": 1.6122051627330474
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.181363868713379,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.86610019048055,
                "rejected_mean_error": 4.249908332824707,
                "gap_rejected_minus_accepted": 2.383808142344157
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8892528414726257,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5548569416617328,
                "rejected_mean_error": 3.7359048109205943,
                "gap_rejected_minus_accepted": 2.1810478692588617
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7290366291999817,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2294907751083375,
                "rejected_mean_error": 2.9794712343215943,
                "gap_rejected_minus_accepted": 1.7499804592132568
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.169659048318863,
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
            "pearson": 0.9867975690852011,
            "spearman": 0.9773802396058663,
            "auroc_top30_bad": 0.9712510476190476,
            "mae": 0.11877021987433063,
            "mse": 0.029099815082547,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7447492365615517,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04605262416601181
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1795374329328537
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6315780479788781
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0459330655018488
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
            "pearson": 0.9821336798482543,
            "spearman": 0.965325220176141,
            "auroc_top30_worst": 0.9523230476190476,
            "pairwise_seed_ranking": 0.8888,
            "predicted_best_mean_error": 1.5850204796791076,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07212266278266899,
            "gap_to_oracle": 0.005122958183288562,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.41825109910964964
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6560455673398116
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.039367518901825
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3142583167502113
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5020400285720834,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4590016306241353,
                "rejected_mean_error": 3.338750032424927,
                "gap_rejected_minus_accepted": 1.8797484018007915
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9330522418022156,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3136146013230372,
                "rejected_mean_error": 2.6449319714555344,
                "gap_rejected_minus_accepted": 1.3313173701324972
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6247842907905579,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.039367518901825,
                "rejected_mean_error": 2.254585422706604,
                "gap_rejected_minus_accepted": 1.215217903804779
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0478110611438751,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6574269314162647,
                "rejected_mean_error": 1.9775303724354079,
                "gap_rejected_minus_accepted": 1.320103441019143
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.61963517665863,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4650840894381205,
                "rejected_mean_error": 3.3856746196746825,
                "gap_rejected_minus_accepted": 1.920590530236562
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9333585500717163,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.308724858862831,
                "rejected_mean_error": 2.691337095366584,
                "gap_rejected_minus_accepted": 1.3826122365037528
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.651886761188507,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0274699501991271,
                "rejected_mean_error": 2.2868163347244264,
                "gap_rejected_minus_accepted": 1.2593463845252992
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0365636348724365,
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
            "pearson": 0.9831802244042493,
            "spearman": 0.9741700040907985,
            "auroc_top30_bad": 0.9744693333333334,
            "mae": 0.1105029800401544,
            "mse": 0.02469674009695343,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6808726370982853,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07201834338903428
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21448871507644654
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.785596419620514
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1397408579508463
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
            "pearson": 0.9540473214116227,
            "spearman": 0.9395301541952987,
            "auroc_top30_worst": 0.9428175238095238,
            "pairwise_seed_ranking": 0.896,
            "predicted_best_mean_error": 1.5978919959068298,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06385913205146787,
            "gap_to_oracle": 0.005868063926696809,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8435108091831207
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1037054219498084
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3643271908283234
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5234593992103647
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0371596574783326,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6000533741050296,
                "rejected_mean_error": 2.1976526012420656,
                "gap_rejected_minus_accepted": 0.5975992271370361
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8574344515800476,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5231015313587677,
                "rejected_mean_error": 2.069075035591857,
                "gap_rejected_minus_accepted": 0.5459735042330891
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.655518889427185,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3643271908283234,
                "rejected_mean_error": 1.955299402809143,
                "gap_rejected_minus_accepted": 0.5909722119808196
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3457853198051453,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1048095002532385,
                "rejected_mean_error": 1.8452094423096614,
                "gap_rejected_minus_accepted": 0.7403999420564229
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0476502180099487,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6072207649548849,
                "rejected_mean_error": 2.1525243949890136,
                "gap_rejected_minus_accepted": 0.5453036300341287
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.864181786775589,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5287478056183472,
                "rejected_mean_error": 2.056538767284817,
                "gap_rejected_minus_accepted": 0.52779096166647
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6518630981445312,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3775546641349792,
                "rejected_mean_error": 1.9459475917816162,
                "gap_rejected_minus_accepted": 0.5683929276466371
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.347642719745636,
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
      "variant": "full_engineered_simvla_focused",
      "feature_mode": "M2_engineered",
      "model_kind": "mlp_big",
      "train_setting": "simvla_focused",
      "train_rows": 10000,
      "input_dim": 1562,
      "best_epoch": 74,
      "best_calib_loss": 0.012740487232804298,
      "train_time_sec": 39.12223672866821,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997112875653342,
            "spearman": 0.9986131214133246,
            "auroc_top30_bad": 0.9997015238095238,
            "mae": 0.020729570244484335,
            "mse": 0.0008236080736865329,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8134574459062673,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0021064845323562624
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19977690846323967
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6186122930020094
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.986385284247001
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
            "pearson": 0.9997966085374812,
            "spearman": 0.9993695148147654,
            "auroc_top30_worst": 0.9997706666666666,
            "pairwise_seed_ranking": 0.9585,
            "predicted_best_mean_error": 1.7027677580714227,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09165663954615577,
            "gap_to_oracle": 0.0011737103462219345,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7223997156023979
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8792606364011765
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0838825732111932
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051614407777787
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.168958234786988,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899320450292692,
                "rejected_mean_error": 4.441592379570007,
                "gap_rejected_minus_accepted": 2.951660334540738
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0407798290252686,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051614407777787,
                "rejected_mean_error": 3.2249079916000367,
                "gap_rejected_minus_accepted": 1.919746550822258
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5283015370368958,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0838825732111932,
                "rejected_mean_error": 2.4863135837554933,
                "gap_rejected_minus_accepted": 1.4024310105443
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.089720904827118,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8792606364011765,
                "rejected_mean_error": 2.087043892510732,
                "gap_rejected_minus_accepted": 1.2077832561095554
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.2140964746475227,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0379185676574707,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019932609001796,
                "rejected_mean_error": 3.2717178077697753,
                "gap_rejected_minus_accepted": 1.9697245468695956
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.525352418422699,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0766077297329903,
                "rejected_mean_error": 2.5122410655021667,
                "gap_rejected_minus_accepted": 1.4356333357691764
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.084125816822052,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8669634252786637,
                "rejected_mean_error": 2.1035780550638834,
                "gap_rejected_minus_accepted": 1.2366146297852199
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9894625205938126,
            "spearman": 0.9798559570691437,
            "auroc_top30_bad": 0.9903420952380952,
            "mae": 0.1221441742040087,
            "mse": 0.028369688406075066,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8872908273165901,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10633292555809021
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20458612990379332
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5872560579895973
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0199536015590032
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
            "pearson": 0.9920620960884915,
            "spearman": 0.9875700226368147,
            "auroc_top30_worst": 0.9990064761904761,
            "pairwise_seed_ranking": 0.9296,
            "predicted_best_mean_error": 1.9926271644830704,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.1118538402318956,
            "gap_to_oracle": 0.003731934785842883,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6571080181598663
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8715835212705991
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2314605060100556
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5497053814277466
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.123478984832763,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8418171622753143,
                "rejected_mean_error": 4.222628776550293,
                "gap_rejected_minus_accepted": 2.3808116142749784
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7893146276474,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5484137329945824,
                "rejected_mean_error": 3.6709560281552447,
                "gap_rejected_minus_accepted": 2.1225422951606623
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7947598695755005,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2314605060100556,
                "rejected_mean_error": 2.928336141395569,
                "gap_rejected_minus_accepted": 1.6968756353855132
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2082554399967194,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.873491511082116,
                "rejected_mean_error": 2.482892274983792,
                "gap_rejected_minus_accepted": 1.6094007639016759
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.2298485279083256,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8650252861446805,
                "rejected_mean_error": 4.259582471847534,
                "gap_rejected_minus_accepted": 2.394557185702854
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.929598391056061,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5549441582378856,
                "rejected_mean_error": 3.7356459299723306,
                "gap_rejected_minus_accepted": 2.1807017717344452
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7920595407485962,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2339226303100586,
                "rejected_mean_error": 2.975039379119873,
                "gap_rejected_minus_accepted": 1.7411167488098145
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1876754760742188,
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
            "pearson": 0.9889908208615306,
            "spearman": 0.9821392829795721,
            "auroc_top30_bad": 0.9827443809523809,
            "mae": 0.10775329422061158,
            "mse": 0.022534800970685647,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7388083091986473,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05397330766916275
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19087385427951814
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6294184569716453
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0424183286269506
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
            "pearson": 0.9892854093876766,
            "spearman": 0.9782292320187086,
            "auroc_top30_worst": 0.9688655238095238,
            "pairwise_seed_ranking": 0.8984,
            "predicted_best_mean_error": 1.5841491931676865,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07299394929409009,
            "gap_to_oracle": 0.004251671671867463,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.41975499653816223
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6555046169803693
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0318740881919861
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3098407459538628
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.392761635780335,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.458648336675432,
                "rejected_mean_error": 3.341929677963257,
                "gap_rejected_minus_accepted": 1.883281341287825
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.93238165974617,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3091995527166693,
                "rejected_mean_error": 2.658148906101434,
                "gap_rejected_minus_accepted": 1.3489493533847647
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6707007884979248,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0318740881919861,
                "rejected_mean_error": 2.2620788534164427,
                "gap_rejected_minus_accepted": 1.2302047652244565
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1188831329345703,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6566681898059175,
                "rejected_mean_error": 1.9777838261430265,
                "gap_rejected_minus_accepted": 1.321115636337109
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5101858377456665,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4641851909955343,
                "rejected_mean_error": 3.393764705657959,
                "gap_rejected_minus_accepted": 1.9295795146624248
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9563515484333038,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3051518778749966,
                "rejected_mean_error": 2.7019426103622193,
                "gap_rejected_minus_accepted": 1.3967907324872226
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6836556196212769,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0219790902137755,
                "rejected_mean_error": 2.2923071947097777,
                "gap_rejected_minus_accepted": 1.2703281044960022
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.097068190574646,
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
            "pearson": 0.9828180390710219,
            "spearman": 0.9770208637262625,
            "auroc_top30_bad": 0.9815725714285715,
            "mae": 0.10396180287948832,
            "mse": 0.023576021122356433,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6866745806278663,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08888971042633056
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22860700752735139
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7841751097679138
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1388608894983927
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
            "pearson": 0.9605188311560466,
            "spearman": 0.9523787778424179,
            "auroc_top30_worst": 0.9615542857142857,
            "pairwise_seed_ranking": 0.9076,
            "predicted_best_mean_error": 1.597651682138443,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06409944581985472,
            "gap_to_oracle": 0.005627750158309963,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8422000725269317
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1022643107825365
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.360763138818741
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5209974374916
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0664747953414917,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5987444796297285,
                "rejected_mean_error": 2.2094326515197755,
                "gap_rejected_minus_accepted": 0.610688171890047
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.881611853837967,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.520387433159186,
                "rejected_mean_error": 2.0771999877100935,
                "gap_rejected_minus_accepted": 0.5568125545509075
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7003304362297058,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.360763138818741,
                "rejected_mean_error": 1.9588634548187256,
                "gap_rejected_minus_accepted": 0.5981003159999847
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3596448004245758,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1032183365509534,
                "rejected_mean_error": 1.8457409623083971,
                "gap_rejected_minus_accepted": 0.7425226257574438
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0589659452438354,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.607415539158715,
                "rejected_mean_error": 2.150771427154541,
                "gap_rejected_minus_accepted": 0.5433558879958258
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.887706607580185,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5280083982064763,
                "rejected_mean_error": 2.05873351626926,
                "gap_rejected_minus_accepted": 0.5307251180627837
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7161461114883423,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3731699280738832,
                "rejected_mean_error": 1.9503323278427125,
                "gap_rejected_minus_accepted": 0.5771623997688293
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.360502004623413,
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
    }
  ]
}
```
