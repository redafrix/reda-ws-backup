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
      "best_epoch": 18,
      "best_calib_loss": 0.09585082530975342,
      "train_time_sec": 14.09476351737976,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.8931863239803015,
            "spearman": 0.8010742140975731,
            "auroc_top30_bad": 0.8779642380952382,
            "mae": 0.23615759802758693,
            "mse": 0.23905254795629308,
            "expert_lt_perturb_large": 0.978,
            "expert_lt_other_task": 0.503,
            "expert_lt_simvla_seed0": 0.969,
            "same_context_pred_std": 0.7632670241858371,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5852128063440323
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.5702243961334229
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7233807664573193
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.018205334909757
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
            "pearson": 0.9969669816172098,
            "spearman": 0.9922756859942861,
            "auroc_top30_worst": 0.9967577142857144,
            "pairwise_seed_ranking": 0.8016,
            "predicted_best_mean_error": 1.7188930582404136,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.07553133937716483,
            "gap_to_oracle": 0.017299010515212876,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7335797246098519
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8845656050920486
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0868930024504662
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3065423922459285
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0351518869400027,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4908238607446354,
                "rejected_mean_error": 4.433566038131714,
                "gap_rejected_minus_accepted": 2.9427421773870783
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9559860527515411,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3065423922459285,
                "rejected_mean_error": 3.220765137195587,
                "gap_rejected_minus_accepted": 1.9142227449496585
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4960726499557495,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0868930024504662,
                "rejected_mean_error": 2.48330315451622,
                "gap_rejected_minus_accepted": 1.396410152065754
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0939728319644928,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8845656050920486,
                "rejected_mean_error": 2.0852755696137746,
                "gap_rejected_minus_accepted": 1.2007099645217258
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0929725170135502,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.492092719508542,
                "rejected_mean_error": 4.515409500598907,
                "gap_rejected_minus_accepted": 3.023316781090365
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9673294126987457,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3023930543661117,
                "rejected_mean_error": 3.2705184273719787,
                "gap_rejected_minus_accepted": 1.968125373005867
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4887945652008057,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0790652762055397,
                "rejected_mean_error": 2.509783519029617,
                "gap_rejected_minus_accepted": 1.4307182428240774
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0949659049510956,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8720887137651443,
                "rejected_mean_error": 2.1018696255683897,
                "gap_rejected_minus_accepted": 1.2297809118032454
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.7920429803980258,
            "spearman": 0.6670608820161141,
            "auroc_top30_bad": 0.7634361904761904,
            "mae": 0.48664381366372106,
            "mse": 0.5344800667625185,
            "expert_lt_perturb_large": 0.972,
            "expert_lt_other_task": 0.524,
            "expert_lt_simvla_seed0": 0.924,
            "same_context_pred_std": 0.8554539715253973,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.842194367825985
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7251391080141067
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8336789081931114
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1192762445370357
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
            "pearson": 0.8159143161415068,
            "spearman": 0.7065316214602378,
            "auroc_top30_worst": 0.8418438095238097,
            "pairwise_seed_ranking": 0.7412,
            "predicted_best_mean_error": 2.0126449496746064,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.09183605504035963,
            "gap_to_oracle": 0.023749719977378847,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3191365654468536
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3172414649564486
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.5133049760818482
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5949732449962133
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.257523107528686,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8425512992805906,
                "rejected_mean_error": 4.216021543502808,
                "gap_rejected_minus_accepted": 2.373470244222217
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.5921940207481384,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5942245459416633,
                "rejected_mean_error": 3.533816310163504,
                "gap_rejected_minus_accepted": 1.9395917642218408
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7141055464744568,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.5133049760818482,
                "rejected_mean_error": 2.6464916713237763,
                "gap_rejected_minus_accepted": 1.133186695241928
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2662429213523865,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.317924697844746,
                "rejected_mean_error": 2.3344316693736498,
                "gap_rejected_minus_accepted": 1.0165069715289037
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.265967226028442,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8651520199245877,
                "rejected_mean_error": 4.2584418678283695,
                "gap_rejected_minus_accepted": 2.393289847903782
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.6410791277885437,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6057274201337028,
                "rejected_mean_error": 3.584908311329191,
                "gap_rejected_minus_accepted": 1.979180891195488
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7252783179283142,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5187286579608916,
                "rejected_mean_error": 2.6902333514690397,
                "gap_rejected_minus_accepted": 1.1715046935081481
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2736802101135254,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.2894424441314878,
                "rejected_mean_error": 2.3790661882270467,
                "gap_rejected_minus_accepted": 1.089623744095559
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6290687213719424,
            "spearman": 0.5261543845427084,
            "auroc_top30_bad": 0.6433699047619048,
            "mae": 0.5365440615594387,
            "mse": 0.6895658785008046,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.516,
            "expert_lt_simvla_seed0": 0.984,
            "same_context_pred_std": 0.6578878096197672,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.770465366601944
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7791323990821838
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9194131303906441
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1363430451631547
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
            "pearson": 0.8187345528692248,
            "spearman": 0.7285051907233222,
            "auroc_top30_worst": 0.7980007619047619,
            "pairwise_seed_ranking": 0.7536,
            "predicted_best_mean_error": 1.6041682881116868,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.05297485435008986,
            "gap_to_oracle": 0.02427076661586769,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5700261850357056
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8821823549194213
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1574424994468688
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3766922078280053
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1001535892486576,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4810045104026794,
                "rejected_mean_error": 3.14072411441803,
                "gap_rejected_minus_accepted": 1.6597196040153503
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7948403060436249,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.376434391756068,
                "rejected_mean_error": 2.4568740045681547,
                "gap_rejected_minus_accepted": 1.0804396128120868
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3970510959625244,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1574424994468688,
                "rejected_mean_error": 2.13651044216156,
                "gap_rejected_minus_accepted": 0.9790679427146913
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.007766991853714,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8829912467124744,
                "rejected_mean_error": 1.9021817804527894,
                "gap_rejected_minus_accepted": 1.019190533740315
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1314904928207397,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.486814173857371,
                "rejected_mean_error": 3.1901038599014284,
                "gap_rejected_minus_accepted": 1.7032896860440574
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8386300206184387,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3786785185018324,
                "rejected_mean_error": 2.4836968675492304,
                "gap_rejected_minus_accepted": 1.105018349047398
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4178446531295776,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1343616595268249,
                "rejected_mean_error": 2.1799246253967284,
                "gap_rejected_minus_accepted": 1.0455629658699035
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.000914216041565,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8674457669258118,
                "rejected_mean_error": 1.923190921385658,
                "gap_rejected_minus_accepted": 1.0557451544598462
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.5065880680404276,
            "spearman": 0.403507852261644,
            "auroc_top30_bad": 0.5889100952380952,
            "mae": 0.480231638365984,
            "mse": 0.605594338357108,
            "expert_lt_perturb_large": 0.992,
            "expert_lt_other_task": 0.516,
            "expert_lt_simvla_seed0": 0.98,
            "same_context_pred_std": 0.6015480649594738,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8460773131847381
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9733226293802262
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0564626631975174
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2608916835228603
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
            "pearson": 0.6930718377373912,
            "spearman": 0.5743085596716163,
            "auroc_top30_worst": 0.7071619047619048,
            "pairwise_seed_ranking": 0.7512,
            "predicted_best_mean_error": 1.6144513345956801,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.04729979336261758,
            "gap_to_oracle": 0.0224274026155471,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.914995190858841
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3024925708961792
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4714895466327667
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5723410482917513
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9486339569091797,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6255625941223568,
                "rejected_mean_error": 1.9680696210861206,
                "gap_rejected_minus_accepted": 0.3425070269637638
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7880309522151947,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5720712427713828,
                "rejected_mean_error": 1.9224788068582455,
                "gap_rejected_minus_accepted": 0.3504075640868627
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5339611172676086,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4714895466327667,
                "rejected_mean_error": 1.8481370470046996,
                "gap_rejected_minus_accepted": 0.37664750037193295
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3382644653320312,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.303267081800741,
                "rejected_mean_error": 1.7789157144287988,
                "gap_rejected_minus_accepted": 0.4756486326280578
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9532729029655456,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6296155211660597,
                "rejected_mean_error": 1.95097158908844,
                "gap_rejected_minus_accepted": 0.32135606792238036
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7874723076820374,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5691184446135944,
                "rejected_mean_error": 1.9367084578862266,
                "gap_rejected_minus_accepted": 0.3675900132726322
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5468175411224365,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.461482973575592,
                "rejected_mean_error": 1.8620192823410033,
                "gap_rejected_minus_accepted": 0.40053630876541124
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3459376394748688,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.2949263226418268,
                "rejected_mean_error": 1.7853338163804242,
                "gap_rejected_minus_accepted": 0.4904074937385974
              }
            ]
          }
        }
      }
    },
    {
      "variant": "context_only_baseline",
      "feature_mode": "A1_context",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 968,
      "best_epoch": 25,
      "best_calib_loss": 0.17081879079341888,
      "train_time_sec": 17.623217582702637,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.4923143323100977,
            "spearman": 0.4305318220505387,
            "auroc_top30_bad": 0.773704119047619,
            "mae": 0.6156970664516092,
            "mse": 0.8911201544147159,
            "expert_lt_perturb_large": 0.5005,
            "expert_lt_other_task": 0.501,
            "expert_lt_simvla_seed0": 0.5005,
            "same_context_pred_std": 2.388008289067628e-10,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8292186559587718
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9151986087560654
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0332718461334705
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1667654568771522
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
            "pearson": 0.9125653337679073,
            "spearman": 0.988981475146116,
            "auroc_top30_worst": 0.9961590476190475,
            "pairwise_seed_ranking": 0.5002,
            "predicted_best_mean_error": 1.7944723930060864,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": -4.7995388507970915e-05,
            "gap_to_oracle": 0.09287834528088568,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7451473169922829
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8876368058919907
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0885776896834374
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3071221149365106
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6036500692367617,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4934601064721744,
                "rejected_mean_error": 4.4098398265838625,
                "gap_rejected_minus_accepted": 2.916379720111688
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9796038568019867,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3071221149365106,
                "rejected_mean_error": 3.2190259691238405,
                "gap_rejected_minus_accepted": 1.9119038541873299
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4924801588058472,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0885776896834374,
                "rejected_mean_error": 2.481618467283249,
                "gap_rejected_minus_accepted": 1.3930407775998117
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0665092170238495,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8876368058919907,
                "rejected_mean_error": 2.084251836013794,
                "gap_rejected_minus_accepted": 1.1966150301218033
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.603650069236756,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4949683384431733,
                "rejected_mean_error": 4.489528930187225,
                "gap_rejected_minus_accepted": 2.994560591744052
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9796038568019867,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3033279517889023,
                "rejected_mean_error": 3.267713735103607,
                "gap_rejected_minus_accepted": 1.9643857833147047
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4924801588058472,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0813340681195258,
                "rejected_mean_error": 2.5075147271156313,
                "gap_rejected_minus_accepted": 1.4261806589961055
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0665092170238495,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8728018385171891,
                "rejected_mean_error": 2.1016319173177083,
                "gap_rejected_minus_accepted": 1.2288300788005193
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.4564156047805636,
            "spearman": 0.3875774524235044,
            "auroc_top30_bad": 0.7707813333333333,
            "mae": 0.7978782820403576,
            "mse": 1.0345389517689716,
            "expert_lt_perturb_large": 0.498,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.5,
            "same_context_pred_std": 1.430511474609375e-10,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7898882079124451
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8758317484617233
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0920641078472137
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2671134936650594
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
            "pearson": 0.920597477484816,
            "spearman": 0.9051309969565884,
            "auroc_top30_worst": 0.9894857142857143,
            "pairwise_seed_ranking": 0.5,
            "predicted_best_mean_error": 2.104481004714966,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.0,
            "gap_to_oracle": 0.11558577501773848,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8639313147068024
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9547613990039397
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2921736785411835
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5675288617674477
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.329655957221985,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8467005349000296,
                "rejected_mean_error": 4.178678422927857,
                "gap_rejected_minus_accepted": 2.3319778880278275
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0130808353424072,
                "accepted_n": 940,
                "rejected_n": 310,
                "accepted_mean_error": 1.5689469683360546,
                "rejected_mean_error": 3.6292346915891094,
                "gap_rejected_minus_accepted": 2.0602877232530545
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4700658917427063,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2921736785411835,
                "rejected_mean_error": 2.867622968864441,
                "gap_rejected_minus_accepted": 1.5754492903232575
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0991995334625244,
                "accepted_n": 315,
                "rejected_n": 935,
                "accepted_mean_error": 0.955765437039118,
                "rejected_mean_error": 2.4586168897980674,
                "gap_rejected_minus_accepted": 1.5028514527589494
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.329655957221985,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.868506366941664,
                "rejected_mean_error": 4.228252744674682,
                "gap_rejected_minus_accepted": 2.3597463777330185
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0113980770111084,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5741173838549118,
                "rejected_mean_error": 3.678734926950364,
                "gap_rejected_minus_accepted": 2.1046175430954523
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4700658917427063,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2908802890777589,
                "rejected_mean_error": 2.918081720352173,
                "gap_rejected_minus_accepted": 1.627201431274414
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0993502736091614,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9511836483365014,
                "rejected_mean_error": 2.4930250338692077,
                "gap_rejected_minus_accepted": 1.5418413855327064
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.4364461218508322,
            "spearman": 0.382030182674212,
            "auroc_top30_bad": 0.687847619047619,
            "mae": 0.6386376934826374,
            "mse": 0.705880201693691,
            "expert_lt_perturb_large": 0.5,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.5,
            "same_context_pred_std": 0.0,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.781783440232277
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8830820301532746
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.095109594118595
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2488013337612152
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
            "pearson": 0.9169789331819715,
            "spearman": 0.8777215861894825,
            "auroc_top30_worst": 0.8641371428571429,
            "pairwise_seed_ranking": 0.5,
            "predicted_best_mean_error": 1.6571431424617766,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.0,
            "gap_to_oracle": 0.07724562096595755,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4754497966766357
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6740485744980665
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0825606169700623
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.355792204899066
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0132601499557503,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.467857352097829,
                "rejected_mean_error": 3.259048539161682,
                "gap_rejected_minus_accepted": 1.7911911870638528
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.760238528251648,
                "accepted_n": 940,
                "rejected_n": 310,
                "accepted_mean_error": 1.3566735428064427,
                "rejected_mean_error": 2.527249865378103,
                "gap_rejected_minus_accepted": 1.17057632257166
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.504591464996338,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0825606169700623,
                "rejected_mean_error": 2.211392324638367,
                "gap_rejected_minus_accepted": 1.1288317076683045
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1440857648849487,
                "accepted_n": 315,
                "rejected_n": 935,
                "accepted_mean_error": 0.6839513008556669,
                "rejected_mean_error": 1.9714181055997144,
                "gap_rejected_minus_accepted": 1.2874668047440476
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0132601499557494,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4749138453271653,
                "rejected_mean_error": 3.297206816673279,
                "gap_rejected_minus_accepted": 1.8222929713461136
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7598207294940948,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.356883776697883,
                "rejected_mean_error": 2.548389196395874,
                "gap_rejected_minus_accepted": 1.191505419697991
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.504591464996338,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0781856102943421,
                "rejected_mean_error": 2.2361006746292116,
                "gap_rejected_minus_accepted": 1.1579150643348695
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.152561604976654,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.6716297212101164,
                "rejected_mean_error": 1.989161033043887,
                "gap_rejected_minus_accepted": 1.3175313118337706
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.18169358448535583,
            "spearman": 0.2147712655530271,
            "auroc_top30_bad": 0.592767619047619,
            "mae": 0.6255171647548675,
            "mse": 0.6384571807914459,
            "expert_lt_perturb_large": 0.502,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.5,
            "same_context_pred_std": 1.430511474609375e-10,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0075680235028266
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1349724535942078
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3069685193181038
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3783880963007609
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
            "pearson": 0.6698955032224522,
            "spearman": 0.6516072338714027,
            "auroc_top30_worst": 0.7243123809523809,
            "pairwise_seed_ranking": 0.5,
            "predicted_best_mean_error": 1.6617511279582977,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.0,
            "gap_to_oracle": 0.06972719597816468,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.917170252084732
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1429310334989657
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4387871250629425
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5792641279095017
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.796423637866974,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6244917670620813,
                "rejected_mean_error": 1.977707064628601,
                "gap_rejected_minus_accepted": 0.3532152975665197
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.663554310798645,
                "accepted_n": 940,
                "rejected_n": 310,
                "accepted_mean_error": 1.5798609525916425,
                "rejected_mean_error": 1.9022494373782988,
                "gap_rejected_minus_accepted": 0.32238848478665627
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4207191467285156,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4387871250629425,
                "rejected_mean_error": 1.880839468574524,
                "gap_rejected_minus_accepted": 0.4420523435115815
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2272270917892456,
                "accepted_n": 315,
                "rejected_n": 935,
                "accepted_mean_error": 1.1509742385811277,
                "rejected_mean_error": 1.8312403592196378,
                "gap_rejected_minus_accepted": 0.6802661206385101
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.7964236378669738,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6277056532435947,
                "rejected_mean_error": 1.968160400390625,
                "gap_rejected_minus_accepted": 0.3404547471470303
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.662861406803131,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5825043703145523,
                "rejected_mean_error": 1.8969756308056058,
                "gap_rejected_minus_accepted": 0.31447126049105356
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4207191467285156,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4471571440696716,
                "rejected_mean_error": 1.8763451118469239,
                "gap_rejected_minus_accepted": 0.4291879677772523
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2276513576507568,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1575698218648396,
                "rejected_mean_error": 1.8316090011341686,
                "gap_rejected_minus_accepted": 0.674039179269329
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
      "best_epoch": 78,
      "best_calib_loss": 0.03793690726161003,
      "train_time_sec": 17.705259323120117,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9983978439256206,
            "spearman": 0.995652299663837,
            "auroc_top30_bad": 0.9989954761904761,
            "mae": 0.051458052269555625,
            "mse": 0.004337200008644234,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7940335292689145,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.057148159757256504
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20038293597102166
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6187567916363478
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9868903805394967
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
            "pearson": 0.9995492783971428,
            "spearman": 0.9987571737502571,
            "auroc_top30_worst": 0.9995819047619048,
            "pairwise_seed_ranking": 0.9191,
            "predicted_best_mean_error": 1.7049932811558246,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.08943111646175383,
            "gap_to_oracle": 0.0033992334306238714,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7240459977984428
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8796705912351608
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0841739722132684
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3053486754655839
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1100328207016013,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899946920010778,
                "rejected_mean_error": 4.44102855682373,
                "gap_rejected_minus_accepted": 2.9510338648226524
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.995339274406433,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3053486754655839,
                "rejected_mean_error": 3.224346287536621,
                "gap_rejected_minus_accepted": 1.918997612071037
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4848453402519226,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0841739722132684,
                "rejected_mean_error": 2.486022184753418,
                "gap_rejected_minus_accepted": 1.4018482125401497
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.05804443359375,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8796705912351608,
                "rejected_mean_error": 2.086907240899404,
                "gap_rejected_minus_accepted": 1.2072366496642433
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1939287900924684,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4916764552394548,
                "rejected_mean_error": 4.5191558790206905,
                "gap_rejected_minus_accepted": 3.0274794237812355
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0070051550865173,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3020609250466029,
                "rejected_mean_error": 3.2715148153305056,
                "gap_rejected_minus_accepted": 1.9694538902839027
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4847800731658936,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.076834258377552,
                "rejected_mean_error": 2.512014536857605,
                "gap_rejected_minus_accepted": 1.4351802784800527
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0484976172447205,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8679204536676407,
                "rejected_mean_error": 2.103259045600891,
                "gap_rejected_minus_accepted": 1.2353385919332505
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9598409898561683,
            "spearman": 0.942996284345091,
            "auroc_top30_bad": 0.9685363809523809,
            "mae": 0.2477018689930439,
            "mse": 0.11429542597515747,
            "expert_lt_perturb_large": 0.992,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.8219487018640186,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.12631468814611435
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2378870963573456
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6312989648222923
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0307895375331242
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
            "pearson": 0.9734760314617777,
            "spearman": 0.9641802911873865,
            "auroc_top30_worst": 0.9910095238095238,
            "pairwise_seed_ranking": 0.8772,
            "predicted_best_mean_error": 2.000058636665344,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.1044223680496219,
            "gap_to_oracle": 0.011163406968116574,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.655073575258255
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9457317658532889
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.229147856092453
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5552899508016196
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.213652658462525,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8429575855202145,
                "rejected_mean_error": 4.212364967346192,
                "gap_rejected_minus_accepted": 2.369407381825977
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7380468249320984,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.554013587208415,
                "rejected_mean_error": 3.6541922473298096,
                "gap_rejected_minus_accepted": 2.1001786601213945
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9406092762947083,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.229147856092453,
                "rejected_mean_error": 2.9306487913131716,
                "gap_rejected_minus_accepted": 1.7015009352207187
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4773590564727783,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9476401584026531,
                "rejected_mean_error": 2.4581233031467287,
                "gap_rejected_minus_accepted": 1.5104831447440756
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.2687139987945555,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.866945367389255,
                "rejected_mean_error": 4.242301740646362,
                "gap_rejected_minus_accepted": 2.375356373257107
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8026509881019592,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5619088723697765,
                "rejected_mean_error": 3.7149728896125915,
                "gap_rejected_minus_accepted": 2.153064017242815
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9549219012260437,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2271885681152344,
                "rejected_mean_error": 2.9817734413146972,
                "gap_rejected_minus_accepted": 1.7545848731994629
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5033204555511475,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9337363479629396,
                "rejected_mean_error": 2.4989030013747393,
                "gap_rejected_minus_accepted": 1.5651666534117998
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9396266145318459,
            "spearman": 0.938800859950826,
            "auroc_top30_bad": 0.9585219047619048,
            "mae": 0.24288957881629467,
            "mse": 0.11281288858632861,
            "expert_lt_perturb_large": 0.988,
            "expert_lt_other_task": 0.956,
            "expert_lt_simvla_seed0": 0.988,
            "same_context_pred_std": 0.6318117637046705,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.12488592910766602
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2683095282793045
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6540035924196244
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0503891388813655
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
            "pearson": 0.9463586562029827,
            "spearman": 0.9433861064871083,
            "auroc_top30_worst": 0.9646933333333333,
            "pairwise_seed_ranking": 0.8088,
            "predicted_best_mean_error": 1.5926125829219817,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.06453055953979492,
            "gap_to_oracle": 0.012715061426162633,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6331948680877686
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.77272781299857
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.033537048435211
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3139178684906665
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6111528635025025,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.459580568154653,
                "rejected_mean_error": 3.3335395946502686,
                "gap_rejected_minus_accepted": 1.8739590264956156
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.855874627828598,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3130899929186068,
                "rejected_mean_error": 2.6465024445384455,
                "gap_rejected_minus_accepted": 1.3334124516198387
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.610802948474884,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.033537048435211,
                "rejected_mean_error": 2.2604158931732177,
                "gap_rejected_minus_accepted": 1.2268788447380066
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1016680002212524,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7727802922360052,
                "rejected_mean_error": 1.9389971793334029,
                "gap_rejected_minus_accepted": 1.1662168870973977
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6676891326904295,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4650840894381205,
                "rejected_mean_error": 3.3856746196746825,
                "gap_rejected_minus_accepted": 1.920590530236562
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8730845153331757,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3074984757657995,
                "rejected_mean_error": 2.6949773118609475,
                "gap_rejected_minus_accepted": 1.387478836095148
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.629152238368988,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.023262444972992,
                "rejected_mean_error": 2.2910238399505616,
                "gap_rejected_minus_accepted": 1.2677613949775697
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.116280436515808,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8015048011900887,
                "rejected_mean_error": 1.9454063269543775,
                "gap_rejected_minus_accepted": 1.1439015257642888
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9344397417038839,
            "spearman": 0.9312858074829243,
            "auroc_top30_bad": 0.9463177142857143,
            "mae": 0.21145660910904407,
            "mse": 0.08622065133492213,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.972,
            "expert_lt_simvla_seed0": 0.976,
            "same_context_pred_std": 0.6159039743185829,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.12640042048692704
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2888127128839493
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7977210790038108
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1463032904942831
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
            "pearson": 0.8466186352340888,
            "spearman": 0.8818922395470333,
            "auroc_top30_worst": 0.9103177142857143,
            "pairwise_seed_ranking": 0.824,
            "predicted_best_mean_error": 1.6059593741893767,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.05579175376892098,
            "gap_to_oracle": 0.013935442209243698,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0704878242015838
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1525915184846292
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3773600029468536
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5290344939874942
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.189162588119507,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5969620908366309,
                "rejected_mean_error": 2.2254741506576536,
                "gap_rejected_minus_accepted": 0.6285120598210228
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.853512167930603,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5286718132719794,
                "rejected_mean_error": 2.052399782707897,
                "gap_rejected_minus_accepted": 0.5237279694359176
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6095871925354004,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3773600029468536,
                "rejected_mean_error": 1.9422665906906127,
                "gap_rejected_minus_accepted": 0.5649065877437591
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3567187786102295,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1532165825176544,
                "rejected_mean_error": 1.8290393070388375,
                "gap_rejected_minus_accepted": 0.6758227245211832
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2242549419403077,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6020307644208271,
                "rejected_mean_error": 2.1992343997955324,
                "gap_rejected_minus_accepted": 0.5972036353747052
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8594767153263092,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.534779434854334,
                "rejected_mean_error": 2.038635359870063,
                "gap_rejected_minus_accepted": 0.5038559250157288
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6143825054168701,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3859329771995545,
                "rejected_mean_error": 1.937569278717041,
                "gap_rejected_minus_accepted": 0.5516363015174865
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3628151416778564,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1591846734758406,
                "rejected_mean_error": 1.8310649602170934,
                "gap_rejected_minus_accepted": 0.6718802867412528
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
      "best_epoch": 100,
      "best_calib_loss": 0.010006251744925976,
      "train_time_sec": 42.83611178398132,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998915673255746,
            "spearman": 0.999096771411424,
            "auroc_top30_bad": 0.9999174285714286,
            "mae": 0.01132086474756943,
            "mse": 0.0002595031160630665,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8064453114383493,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00019051821529865264
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19962382974028586
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6185486939400434
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9862975513915221
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
            "pearson": 0.9998790680055901,
            "spearman": 0.9996727478189021,
            "auroc_top30_worst": 0.9999459047619048,
            "pairwise_seed_ranking": 0.9635,
            "predicted_best_mean_error": 1.7024521715044976,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09197222611308087,
            "gap_to_oracle": 0.0008581237792968377,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7219879130721092
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8790168828725815
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0837691184878349
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3051171576738358
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1448600053787237,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4899325315091345,
                "rejected_mean_error": 4.441588001251221,
                "gap_rejected_minus_accepted": 2.9516554697420863
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0261977910995483,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3051171576738358,
                "rejected_mean_error": 3.2250408409118654,
                "gap_rejected_minus_accepted": 1.9199236832380295
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5136431455612183,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0837691184878349,
                "rejected_mean_error": 2.486427038478851,
                "gap_rejected_minus_accepted": 1.4026579199910163
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0871086716651917,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8790168828725815,
                "rejected_mean_error": 2.0871251436869303,
                "gap_rejected_minus_accepted": 1.2081082608143487
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1829046487808235,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0283783078193665,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3019650521675745,
                "rejected_mean_error": 3.2718024339675904,
                "gap_rejected_minus_accepted": 1.9698373818000159
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5117363333702087,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0763876371979713,
                "rejected_mean_error": 2.5124611580371856,
                "gap_rejected_minus_accepted": 1.4360735208392144
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0775606334209442,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8664861694574356,
                "rejected_mean_error": 2.103737140337626,
                "gap_rejected_minus_accepted": 1.2372509708801904
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9933359290002877,
            "spearman": 0.9896280048498495,
            "auroc_top30_bad": 0.9935436190476191,
            "mae": 0.10170423793653026,
            "mse": 0.021485267268671955,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.9249022336304673,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05607700729370117
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18836072795391082
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5845386438012123
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.019022407825788
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
            "pearson": 0.9926170858643586,
            "spearman": 0.9945576843249181,
            "auroc_top30_worst": 0.9980068571428571,
            "pairwise_seed_ranking": 0.9244,
            "predicted_best_mean_error": 1.9930256152153014,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.1114553894996646,
            "gap_to_oracle": 0.004130385518073876,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6172386305332184
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8652064646474826
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2233175595760346
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5528042332640588
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.2263829708099365,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.842187925418218,
                "rejected_mean_error": 4.21929190826416,
                "gap_rejected_minus_accepted": 2.377103982845942
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8516125082969666,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5515472889900717,
                "rejected_mean_error": 3.661575382890793,
                "gap_rejected_minus_accepted": 2.110028093900721
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8775267004966736,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2233175595760346,
                "rejected_mean_error": 2.9364790878295897,
                "gap_rejected_minus_accepted": 1.713161528253555
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2837861478328705,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8660306792480116,
                "rejected_mean_error": 2.4853845272400084,
                "gap_rejected_minus_accepted": 1.6193538479919969
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.250928974151611,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8656025314331055,
                "rejected_mean_error": 4.254387264251709,
                "gap_rejected_minus_accepted": 2.3887847328186034
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.8946176767349243,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.559065182578755,
                "rejected_mean_error": 3.7234136831192743,
                "gap_rejected_minus_accepted": 2.1643485005405196
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.878698706626892,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2218901548385621,
                "rejected_mean_error": 2.9870718545913695,
                "gap_rejected_minus_accepted": 1.7651816997528074
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2988595962524414,
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
            "pearson": 0.9925022272743167,
            "spearman": 0.9896153758739514,
            "auroc_top30_bad": 0.9913211428571429,
            "mae": 0.08288252230063081,
            "mse": 0.01398261363381265,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.777948510144286,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0407092120051384
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17867488670349121
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.626630233991146
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0394672230005264
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
            "pearson": 0.9914486797310381,
            "spearman": 0.9913674840111899,
            "auroc_top30_worst": 0.9866483809523809,
            "pairwise_seed_ranking": 0.9036,
            "predicted_best_mean_error": 1.5857084472179412,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07143469524383539,
            "gap_to_oracle": 0.005810925722122162,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.40599280977249147
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6525416343640058
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0249540028572082
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3040754945674684
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.767056107521057,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4598634139696758,
                "rejected_mean_error": 3.3309939823150634,
                "gap_rejected_minus_accepted": 1.8711305683453876
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0606454014778137,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.303270105682035,
                "rejected_mean_error": 2.67589935936486,
                "gap_rejected_minus_accepted": 1.3726292536828248
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.74562007188797,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0249540028572082,
                "rejected_mean_error": 2.2689989387512206,
                "gap_rejected_minus_accepted": 1.2440449358940124
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1062073409557343,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.653864084722135,
                "rejected_mean_error": 1.9787205229319529,
                "gap_rejected_minus_accepted": 1.3248564382098178
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.9132110595703122,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4655003004603915,
                "rejected_mean_error": 3.381928720474243,
                "gap_rejected_minus_accepted": 1.9164284200138517
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.100319266319275,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2993908652009811,
                "rejected_mean_error": 2.719042759093027,
                "gap_rejected_minus_accepted": 1.419651893892046
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7632796168327332,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0154623284339905,
                "rejected_mean_error": 2.298823956489563,
                "gap_rejected_minus_accepted": 1.2833616280555726
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0877486169338226,
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
            "pearson": 0.9918242970409104,
            "spearman": 0.9853011511960748,
            "auroc_top30_bad": 0.9860556190476191,
            "mae": 0.07219605894414707,
            "mse": 0.010991093618209427,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.724738850712722,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03993674349784851
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21510946426391603
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7828163515090942
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.136545462544759
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
            "pearson": 0.9795830509328,
            "spearman": 0.9723984616950155,
            "auroc_top30_worst": 0.9721478095238095,
            "pairwise_seed_ranking": 0.916,
            "predicted_best_mean_error": 1.5979301118850708,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06382101607322688,
            "gap_to_oracle": 0.005906179904937803,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8465706388950348
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1014700231070702
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.358108776140213
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5177495600635817
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0328285455703736,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5921765259901683,
                "rejected_mean_error": 2.2685442342758178,
                "gap_rejected_minus_accepted": 0.6763677082856494
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8908412754535675,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5174151995202394,
                "rejected_mean_error": 2.0860976967186975,
                "gap_rejected_minus_accepted": 0.5686824971984581
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.731981635093689,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.358108776140213,
                "rejected_mean_error": 1.9615178174972534,
                "gap_rejected_minus_accepted": 0.6034090413570403
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4433498978614807,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1023163232750024,
                "rejected_mean_error": 1.846042275174323,
                "gap_rejected_minus_accepted": 0.7437259518993207
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0355817079544067,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.598184163040585,
                "rejected_mean_error": 2.2338538122177125,
                "gap_rejected_minus_accepted": 0.6356696491771274
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.892313539981842,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5247947509913522,
                "rejected_mean_error": 2.0682724373681203,
                "gap_rejected_minus_accepted": 0.5434776863767681
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.750980257987976,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3704585938453675,
                "rejected_mean_error": 1.953043662071228,
                "gap_rejected_minus_accepted": 0.5825850682258604
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4861798286437988,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1135094913225325,
                "rejected_mean_error": 1.8464528558088495,
                "gap_rejected_minus_accepted": 0.732943364486317
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
      "best_epoch": 82,
      "best_calib_loss": 0.011147607117891312,
      "train_time_sec": 46.791295766830444,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9991676421876562,
            "spearman": 0.9977414112718966,
            "auroc_top30_bad": 0.9990399047619049,
            "mae": 0.03665488357953293,
            "mse": 0.002688390946799345,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7932229788769856,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.001856320470571518
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2000017466723919
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6189059046715498
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9867549972355366
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
            "pearson": 0.9991779229705866,
            "spearman": 0.99778066096712,
            "auroc_top30_worst": 0.9988676190476189,
            "pairwise_seed_ranking": 0.9532,
            "predicted_best_mean_error": 1.7034196034669875,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.09100479415059093,
            "gap_to_oracle": 0.0018255557417867774,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7238112427592277
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8799366033315659
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.085433112990856
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3054124829212825
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0837096929550176,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4900259111656082,
                "rejected_mean_error": 4.440747584342956,
                "gap_rejected_minus_accepted": 2.9507216731773482
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9991288781166077,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3054124829212825,
                "rejected_mean_error": 3.2241548651695253,
                "gap_rejected_minus_accepted": 1.9187423822482428
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5307708978652954,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.085433112990856,
                "rejected_mean_error": 2.48476304397583,
                "gap_rejected_minus_accepted": 1.399329930984974
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1094950735569,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8799366033315659,
                "rejected_mean_error": 2.0868185702006024,
                "gap_rejected_minus_accepted": 1.2068819668690365
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.15658187866211,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.491615736650096,
                "rejected_mean_error": 4.51970234632492,
                "gap_rejected_minus_accepted": 3.0280866096748245
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0067299604415894,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3022277581294377,
                "rejected_mean_error": 3.2710143160820007,
                "gap_rejected_minus_accepted": 1.968786557952563
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5293435454368591,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0778349140286445,
                "rejected_mean_error": 2.5110138812065124,
                "gap_rejected_minus_accepted": 1.4331789671778679
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1000565886497498,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8670594993829727,
                "rejected_mean_error": 2.103546030362447,
                "gap_rejected_minus_accepted": 1.2364865309794744
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9910169528740764,
            "spearman": 0.9811154301638485,
            "auroc_top30_bad": 0.9918163809523809,
            "mae": 0.11624822124426255,
            "mse": 0.02463880954524043,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8640223960047309,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0879616283774376
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2084882184267044
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5871002008080483
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0202213851690292
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
            "pearson": 0.9938553092088407,
            "spearman": 0.9912247895198654,
            "auroc_top30_worst": 0.999104,
            "pairwise_seed_ranking": 0.9328,
            "predicted_best_mean_error": 1.9926819672584535,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.11179903745651254,
            "gap_to_oracle": 0.003786737561225939,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6319306137561798
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8708714337494129
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2255804124355316
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5492872051529285
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.9740374088287362,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8417533616754744,
                "rejected_mean_error": 4.223202981948853,
                "gap_rejected_minus_accepted": 2.3814496202733784
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.710655093193054,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5474645074619937,
                "rejected_mean_error": 3.6737976394141443,
                "gap_rejected_minus_accepted": 2.1263331319521503
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8017146587371826,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2255804124355316,
                "rejected_mean_error": 2.934216234970093,
                "gap_rejected_minus_accepted": 1.7086358225345613
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2379570305347443,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8726019865979021,
                "rejected_mean_error": 2.4831894160334813,
                "gap_rejected_minus_accepted": 1.6105874294355793
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.052271175384521,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8649384869469536,
                "rejected_mean_error": 4.260363664627075,
                "gap_rejected_minus_accepted": 2.3954251776801216
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7888328433036804,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.555659858938207,
                "rejected_mean_error": 3.73352154852852,
                "gap_rejected_minus_accepted": 2.177861689590313
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8189041018486023,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2262081689834594,
                "rejected_mean_error": 2.982753840446472,
                "gap_rejected_minus_accepted": 1.7565456714630128
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.241435706615448,
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
            "pearson": 0.9884128074969845,
            "spearman": 0.9810888803660316,
            "auroc_top30_bad": 0.9783466666666667,
            "mae": 0.11621609291154182,
            "mse": 0.02590942653325518,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7261587154187648,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0506977299451828
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19278470723629
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.628393255841732
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0430799684762955
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
            "pearson": 0.9891172393894143,
            "spearman": 0.9764673160110823,
            "auroc_top30_worst": 0.9644891428571428,
            "pairwise_seed_ranking": 0.9,
            "predicted_best_mean_error": 1.5849800544977188,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.07216308796405779,
            "gap_to_oracle": 0.005082533001899758,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4141486554145813
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6552839749134504
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0304614537239074
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3116557199690642
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3849961280822765,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4593859228028192,
                "rejected_mean_error": 3.3352914028167726,
                "gap_rejected_minus_accepted": 1.8759054800139534
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.94041907787323,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.311046410077664,
                "rejected_mean_error": 2.6526201350239518,
                "gap_rejected_minus_accepted": 1.3415737249462878
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6431729197502136,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0304614537239074,
                "rejected_mean_error": 2.2634914878845214,
                "gap_rejected_minus_accepted": 1.233030034160614
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1131675839424133,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.6565458496538595,
                "rejected_mean_error": 1.9778246932375774,
                "gap_rejected_minus_accepted": 1.321278843583718
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4783543586730956,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4646776609950596,
                "rejected_mean_error": 3.3893324756622314,
                "gap_rejected_minus_accepted": 1.9246548146671718
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9495557248592377,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3053095618033792,
                "rejected_mean_error": 2.701474564416068,
                "gap_rejected_minus_accepted": 1.3961650026126886
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6624818444252014,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0186369767189025,
                "rejected_mean_error": 2.2956493082046507,
                "gap_rejected_minus_accepted": 1.2770123314857482
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1045548915863037,
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
            "pearson": 0.9814066409112427,
            "spearman": 0.9772212483903052,
            "auroc_top30_bad": 0.9833043809523809,
            "mae": 0.11595436991126899,
            "mse": 0.028323448243948973,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6586649340727337,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08515568715333939
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2346058634996414
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7839969267845154
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.140009450785319
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
            "pearson": 0.9617571830786019,
            "spearman": 0.9584553328994131,
            "auroc_top30_worst": 0.964096,
            "pairwise_seed_ranking": 0.8996,
            "predicted_best_mean_error": 1.5971899464130401,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.06456118154525758,
            "gap_to_oracle": 0.005166014432907096,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8472784550189972
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.102117860641999
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3605711447238922
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5211894661188126
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0222843647003175,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5995582767327627,
                "rejected_mean_error": 2.202108477592468,
                "gap_rejected_minus_accepted": 0.6025502008597055
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8741943538188934,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5208696898235965,
                "rejected_mean_error": 2.075756299229095,
                "gap_rejected_minus_accepted": 0.5548866094054985
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7029491066932678,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3605711447238922,
                "rejected_mean_error": 1.9590554489135743,
                "gap_rejected_minus_accepted": 0.5984843041896821
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3688403964042664,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1029310200732356,
                "rejected_mean_error": 1.8458369388906017,
                "gap_rejected_minus_accepted": 0.7429059188173661
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0347627878189085,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.606230595111847,
                "rejected_mean_error": 2.161435923576355,
                "gap_rejected_minus_accepted": 0.555205328464508
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8669512867927551,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5271042033950275,
                "rejected_mean_error": 2.061417396106417,
                "gap_rejected_minus_accepted": 0.5343131927113896
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.73024982213974,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3723606171607972,
                "rejected_mean_error": 1.9511416387557983,
                "gap_rejected_minus_accepted": 0.5787810215950011
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3742740750312805,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1110525935415239,
                "rejected_mean_error": 1.8472805807297243,
                "gap_rejected_minus_accepted": 0.7362279871882005
              }
            ]
          }
        }
      }
    }
  ]
}
```
