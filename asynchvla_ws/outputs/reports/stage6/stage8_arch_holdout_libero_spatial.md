# Stage 6 Experiments: holdout_libero_spatial

```json
{
  "split": "holdout_libero_spatial",
  "results": [
    {
      "variant": "action_only_baseline",
      "feature_mode": "A0_action_flat",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 70,
      "best_epoch": 82,
      "best_calib_loss": 0.037868328392505646,
      "train_time_sec": 16.766286849975586,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9792403570914966,
            "spearman": 0.9417512345183893,
            "auroc_top30_bad": 0.9990060714285713,
            "mae": 0.11290462050363421,
            "mse": 0.04490765813850017,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.512,
            "expert_lt_simvla_seed0": 0.973,
            "same_context_pred_std": 0.7817772377683052,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.2929429337829351
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.31947041643857954
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4828962941512466
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8231369526058435
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
            "pearson": 0.9990829264725343,
            "spearman": 0.9981265291090612,
            "auroc_top30_worst": 0.9985405714285714,
            "pairwise_seed_ranking": 0.8696,
            "predicted_best_mean_error": 1.778290801167488,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07173491013050093,
            "gap_to_oracle": 0.004651687920093517,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.605202734053135
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8424011141061782
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1152433529496193
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3620498639822005
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4395495891571044,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681576256553331,
                "rejected_mean_error": 4.289117722511292,
                "gap_rejected_minus_accepted": 2.7209600968559586
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1009960770606995,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3620498639822005,
                "rejected_mean_error": 3.2748649494171143,
                "gap_rejected_minus_accepted": 1.9128150854349137
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6110109090805054,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1152433529496193,
                "rejected_mean_error": 2.565263917732239,
                "gap_rejected_minus_accepted": 1.4500205647826196
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1211319863796234,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8424011141061782,
                "rejected_mean_error": 2.1728711424191793,
                "gap_rejected_minus_accepted": 1.330470028313001
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4208622932434087,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1166871786117554,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3730644019444784,
                "rejected_mean_error": 3.2809096393585206,
                "gap_rejected_minus_accepted": 1.9078452374140422
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.634925365447998,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1218951780796051,
                "rejected_mean_error": 2.578156244516373,
                "gap_rejected_minus_accepted": 1.4562610664367677
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1313129365444183,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8459226965904236,
                "rejected_mean_error": 2.184726716200511,
                "gap_rejected_minus_accepted": 1.3388040196100872
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.917698634641415,
            "spearman": 0.8986252149260842,
            "auroc_top30_bad": 0.9804586666666666,
            "mae": 0.23698172634243966,
            "mse": 0.11395632941960607,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.508,
            "expert_lt_simvla_seed0": 0.972,
            "same_context_pred_std": 0.6761705631534015,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3075507264137268
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.31068253037929533
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.43527221912145614
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7904085442622503
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
            "pearson": 0.8223718860129366,
            "spearman": 0.8650087546142565,
            "auroc_top30_worst": 0.9340739047619049,
            "pairwise_seed_ranking": 0.8,
            "predicted_best_mean_error": 1.5750469883680345,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.0837052509784697,
            "gap_to_oracle": 0.01591382789611817,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5663780450820923
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8888634003889866
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1375269666671752
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3921891539844113
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.273492193222046,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.564808976173401,
                "rejected_mean_error": 2.280631583213806,
                "gap_rejected_minus_accepted": 0.7158226070404052
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.995132327079773,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.391451784488104,
                "rejected_mean_error": 2.369644485723477,
                "gap_rejected_minus_accepted": 0.978192701235373
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6081399321556091,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1375269666671752,
                "rejected_mean_error": 2.1352555070877077,
                "gap_rejected_minus_accepted": 0.9977285404205325
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1452390253543854,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8882974155794698,
                "rejected_mean_error": 1.8862881056781513,
                "gap_rejected_minus_accepted": 0.9979906900986815
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2992724180221553,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5967092520660824,
                "rejected_mean_error": 2.2171391248703003,
                "gap_rejected_minus_accepted": 0.6204298728042179
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0143209099769592,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4060894953694574,
                "rejected_mean_error": 2.4087194317863103,
                "gap_rejected_minus_accepted": 1.002629936416853
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.664631962776184,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1566705572605134,
                "rejected_mean_error": 2.160833921432495,
                "gap_rejected_minus_accepted": 1.0041633641719816
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1684177815914154,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.886195380063284,
                "rejected_mean_error": 1.91902540584299,
                "gap_rejected_minus_accepted": 1.032830025779706
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8351324188044136,
            "spearman": 0.8175509037835587,
            "auroc_top30_bad": 0.9028921904761904,
            "mae": 0.3350338322788477,
            "mse": 0.21976631998150992,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.496,
            "expert_lt_simvla_seed0": 0.956,
            "same_context_pred_std": 0.6447819296792491,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.42726255559921267
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.41975835832357405
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6394372623860836
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.014836945593357
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
            "pearson": 0.5963875504870892,
            "spearman": 0.6051805113810846,
            "auroc_top30_worst": 0.7654857142857143,
            "pairwise_seed_ranking": 0.738,
            "predicted_best_mean_error": 1.7737827475070953,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.06981813836097728,
            "gap_to_oracle": 0.033932029247284,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2151547288894653
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.40302496861953
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.569374960899353
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6894782251640679
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0674815416336063,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7536343875461156,
                "rejected_mean_error": 2.3313312840461733,
                "gap_rejected_minus_accepted": 0.5776968965000577
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.843380481004715,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.689130863614118,
                "rejected_mean_error": 2.177442419452789,
                "gap_rejected_minus_accepted": 0.48831155583867103
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5679911971092224,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.569374960899353,
                "rejected_mean_error": 2.0534331934928893,
                "gap_rejected_minus_accepted": 0.4840582325935363
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.298413723707199,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.4022742306081633,
                "rejected_mean_error": 1.9480717847543185,
                "gap_rejected_minus_accepted": 0.5457975541461553
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1008152961730957,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7743973037931655,
                "rejected_mean_error": 2.4664331245422364,
                "gap_rejected_minus_accepted": 0.6920358207490709
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8666093945503235,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.7128146829452107,
                "rejected_mean_error": 2.231807551686726,
                "gap_rejected_minus_accepted": 0.5189928687415153
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.618998110294342,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5728577690124512,
                "rejected_mean_error": 2.1143440027236937,
                "gap_rejected_minus_accepted": 0.5414862337112425
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.339726209640503,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.398391021622552,
                "rejected_mean_error": 1.9935913748919645,
                "gap_rejected_minus_accepted": 0.5952003532694126
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.7736363014414694,
            "spearman": 0.7728744119475381,
            "auroc_top30_bad": 0.8612785714285716,
            "mae": 0.42801323025487364,
            "mse": 0.3312851393518809,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.495,
            "expert_lt_simvla_seed0": 0.975,
            "same_context_pred_std": 0.6089221548028599,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5015440803021193
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.43451488298922775
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7790457070060074
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0886986967151364
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
            "pearson": 0.40255770973475824,
            "spearman": 0.4491798531798532,
            "auroc_top30_worst": 0.779495238095238,
            "pairwise_seed_ranking": 0.7015,
            "predicted_best_mean_error": 1.894793106019497,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.03143695741891861,
            "gap_to_oracle": 0.03149171888828284,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.8743035101890564
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.7849603495597839
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.7683348460197448
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.8247555481592814
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.025514101982117,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8749677420987023,
                "rejected_mean_error": 2.272907291650772,
                "gap_rejected_minus_accepted": 0.39793954955206967
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.893858551979065,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.8247555481592814,
                "rejected_mean_error": 2.184780143737793,
                "gap_rejected_minus_accepted": 0.36002459557851174
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4096729755401611,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.7683348460197448,
                "rejected_mean_error": 2.0611885480880736,
                "gap_rejected_minus_accepted": 0.29285370206832884
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1254202127456665,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.7849603495597839,
                "rejected_mean_error": 1.9580288128852845,
                "gap_rejected_minus_accepted": 0.17306846332550063
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0277210235595704,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8908149831824832,
                "rejected_mean_error": 2.244965785741806,
                "gap_rejected_minus_accepted": 0.35415080255932274
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9138199388980865,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.8390594943364462,
                "rejected_mean_error": 2.187741770744324,
                "gap_rejected_minus_accepted": 0.34868227640787763
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.437764585018158,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.7910194730758666,
                "rejected_mean_error": 2.061440653800964,
                "gap_rejected_minus_accepted": 0.2704211807250976
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1409513354301453,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.795339162349701,
                "rejected_mean_error": 1.9698603638013203,
                "gap_rejected_minus_accepted": 0.1745212014516193
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
      "best_epoch": 120,
      "best_calib_loss": 0.014005123637616634,
      "train_time_sec": 21.17378306388855,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994814662424584,
            "spearman": 0.9984686947484384,
            "auroc_top30_bad": 0.9996540952380952,
            "mae": 0.02511068892816511,
            "mse": 0.001231003367031776,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.803943898971271,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0023399667516350747
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17262863769233228
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47520385868400333
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8226735284000635
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
            "pearson": 0.9994037800054014,
            "spearman": 0.9994148799765951,
            "auroc_top30_worst": 0.9994655238095238,
            "pairwise_seed_ranking": 0.9259,
            "predicted_best_mean_error": 1.7752127844691277,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07481292682886131,
            "gap_to_oracle": 0.0015736712217331306,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.604477164208889
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8406802168130875
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.114521618950367
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3617549824794133
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.425919389724732,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5682635285920568,
                "rejected_mean_error": 4.28816459608078,
                "gap_rejected_minus_accepted": 2.7199010674887236
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1201112866401672,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3617549824794133,
                "rejected_mean_error": 3.275749593925476,
                "gap_rejected_minus_accepted": 1.9139946114460629
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6182777881622314,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.114521618950367,
                "rejected_mean_error": 2.565985651731491,
                "gap_rejected_minus_accepted": 1.451464032781124
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1400174796581268,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8406802168130875,
                "rejected_mean_error": 2.1734447748502097,
                "gap_rejected_minus_accepted": 1.3327645580371223
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.424468421936035,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5774023093117608,
                "rejected_mean_error": 4.303636329174042,
                "gap_rejected_minus_accepted": 2.726234019862281
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.145624876022339,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3726339616775514,
                "rejected_mean_error": 3.282200960159302,
                "gap_rejected_minus_accepted": 1.9095669984817505
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6309216618537903,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.121213522195816,
                "rejected_mean_error": 2.5788379004001616,
                "gap_rejected_minus_accepted": 1.4576243782043456
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1534485518932343,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8440729193687438,
                "rejected_mean_error": 2.185343308607737,
                "gap_rejected_minus_accepted": 1.3412703892389932
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9772491511966688,
            "spearman": 0.9795191985533931,
            "auroc_top30_bad": 0.9948350476190475,
            "mae": 0.13023562608447392,
            "mse": 0.033219545529072796,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6990027614855258,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06852484375238418
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17153964812755584
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40894294987916946
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7772273884852727
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
            "pearson": 0.9520207426142288,
            "spearman": 0.9755389570169325,
            "auroc_top30_worst": 0.9926765714285714,
            "pairwise_seed_ranking": 0.9132,
            "predicted_best_mean_error": 1.5629553759098054,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.0957968634366988,
            "gap_to_oracle": 0.003822215437889076,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.48788874673843385
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7818828479219706
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0973565855026246
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3475615014907902
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4654508352279665,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5168128369649252,
                "rejected_mean_error": 2.712596836090088,
                "gap_rejected_minus_accepted": 1.1957839991251626
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.092413008213043,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3467949418909648,
                "rejected_mean_error": 2.503329666277852,
                "gap_rejected_minus_accepted": 1.156534724386887
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5942233204841614,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0973565855026246,
                "rejected_mean_error": 2.175425888252258,
                "gap_rejected_minus_accepted": 1.0780693027496335
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.212267428636551,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7823824804430952,
                "rejected_mean_error": 1.9216684415348058,
                "gap_rejected_minus_accepted": 1.1392859610917105
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4795936584472655,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5350261657767825,
                "rejected_mean_error": 2.772286901473999,
                "gap_rejected_minus_accepted": 1.2372607356972163
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1094971299171448,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3648789612685932,
                "rejected_mean_error": 2.531042763165065,
                "gap_rejected_minus_accepted": 1.166163801896472
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6306903958320618,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1148594372272491,
                "rejected_mean_error": 2.2026450414657592,
                "gap_rejected_minus_accepted": 1.0877856042385101
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.229552447795868,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7980054366210151,
                "rejected_mean_error": 1.9487364563074978,
                "gap_rejected_minus_accepted": 1.1507310196864826
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9701225694673821,
            "spearman": 0.965243659527886,
            "auroc_top30_bad": 0.9806041904761905,
            "mae": 0.14308252265157645,
            "mse": 0.04389207261940041,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 0.972,
            "same_context_pred_std": 0.6658617670091368,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07639632794260978
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19917211776971816
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5869481834352016
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9627050209959348
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
            "pearson": 0.9419451689872256,
            "spearman": 0.9457099805756087,
            "auroc_top30_worst": 0.973336380952381,
            "pairwise_seed_ranking": 0.896,
            "predicted_best_mean_error": 1.7440624445676804,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.09953844130039213,
            "gap_to_oracle": 0.004211726307869146,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9092397937774658
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2046146408105507
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4480931913375854
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6176736033928674
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2202031612396245,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7283096918000116,
                "rejected_mean_error": 2.5592535457611083,
                "gap_rejected_minus_accepted": 0.8309438539610967
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9814906120300293,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.616631963527826,
                "rejected_mean_error": 2.394475867953925,
                "gap_rejected_minus_accepted": 0.7778439044260992
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.73226398229599,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4480931913375854,
                "rejected_mean_error": 2.174714963054657,
                "gap_rejected_minus_accepted": 0.7266217717170718
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4584989547729492,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.2052603647731746,
                "rejected_mean_error": 2.013883246874224,
                "gap_rejected_minus_accepted": 0.8086228821010495
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2677463054656983,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.753498182826572,
                "rejected_mean_error": 2.6545252132415773,
                "gap_rejected_minus_accepted": 0.9010270304150052
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0100156664848328,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6285355632955378,
                "rejected_mean_error": 2.4819693830278187,
                "gap_rejected_minus_accepted": 0.8534338197322808
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7529261112213135,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4535119876861573,
                "rejected_mean_error": 2.2336897840499876,
                "gap_rejected_minus_accepted": 0.7801777963638303
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4697429835796356,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.2091527779897053,
                "rejected_mean_error": 2.057345435581105,
                "gap_rejected_minus_accepted": 0.8481926575913998
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.977757570630639,
            "spearman": 0.9615782934911636,
            "auroc_top30_bad": 0.9630196428571427,
            "mae": 0.17864289861937868,
            "mse": 0.050455034949724836,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.985,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6478511788851692,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08078573275357485
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1861059045866132
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6719167789258063
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0553176577910781
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
            "pearson": 0.8991015761686072,
            "spearman": 0.9083092190341466,
            "auroc_top30_worst": 0.9742547619047619,
            "pairwise_seed_ranking": 0.885,
            "predicted_best_mean_error": 1.8671287116408348,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.05910135179758069,
            "gap_to_oracle": 0.0038273245096207553,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.3679382801055908
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.501183115005493
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6435771470069884
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7679306899706522
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1101781606674193,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.850251608159807,
                "rejected_mean_error": 2.4953524971008303,
                "gap_rejected_minus_accepted": 0.6451008889410232
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9097963273525238,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7679306899706522,
                "rejected_mean_error": 2.3552547183036805,
                "gap_rejected_minus_accepted": 0.5873240283330283
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7161840200424194,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6435771470069884,
                "rejected_mean_error": 2.18594624710083,
                "gap_rejected_minus_accepted": 0.5423691000938415
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5011406242847443,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.501183115005493,
                "rejected_mean_error": 2.0526212244033815,
                "gap_rejected_minus_accepted": 0.5514381093978884
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.110253429412842,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8629708581500584,
                "rejected_mean_error": 2.4955629110336304,
                "gap_rejected_minus_accepted": 0.632592052883572
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.90626859664917,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.776493968963623,
                "rejected_mean_error": 2.375438346862793,
                "gap_rejected_minus_accepted": 0.5989443778991701
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7262576818466187,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.652212131023407,
                "rejected_mean_error": 2.2002479958534242,
                "gap_rejected_minus_accepted": 0.5480358648300172
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.524189054965973,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.51967928647995,
                "rejected_mean_error": 2.061746989091237,
                "gap_rejected_minus_accepted": 0.5420677026112872
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
      "best_epoch": 108,
      "best_calib_loss": 0.008296546526253223,
      "train_time_sec": 50.90702676773071,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9999019890888681,
            "spearman": 0.9990802834932049,
            "auroc_top30_bad": 0.9999043333333333,
            "mae": 0.010384960058284924,
            "mse": 0.0002176475847266036,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8023901051125563,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0011611065343022347
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17245053027570248
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47501103465408084
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8224576942116022
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
            "pearson": 0.9999377529987453,
            "spearman": 0.9998861475474458,
            "auroc_top30_worst": 0.9999571428571429,
            "pairwise_seed_ranking": 0.9611,
            "predicted_best_mean_error": 1.7741251992285252,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.0759005120694638,
            "gap_to_oracle": 0.00048608598113064616,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6038160747885704
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8402380964517593
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1143408769726753
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3616019977966944
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4553040504455574,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5680998291770618,
                "rejected_mean_error": 4.289637890815735,
                "gap_rejected_minus_accepted": 2.721538061638673
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1245256662368774,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3616019977966944,
                "rejected_mean_error": 3.2762085479736327,
                "gap_rejected_minus_accepted": 1.9146065501769383
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.627032220363617,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1143408769726753,
                "rejected_mean_error": 2.5661663937091825,
                "gap_rejected_minus_accepted": 1.4518255167365073
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1408248245716095,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8402380964517593,
                "rejected_mean_error": 2.1735921483039857,
                "gap_rejected_minus_accepted": 1.3333540518522264
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.412567043304445,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1567530035972595,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3725387153625488,
                "rejected_mean_error": 3.282486699104309,
                "gap_rejected_minus_accepted": 1.9099479837417603
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.650738775730133,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1211057188510896,
                "rejected_mean_error": 2.578945703744888,
                "gap_rejected_minus_accepted": 1.4578399848937986
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1498266756534576,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8436812901496887,
                "rejected_mean_error": 2.1854738516807557,
                "gap_rejected_minus_accepted": 1.3417925615310669
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9874491636014326,
            "spearman": 0.9888494606589825,
            "auroc_top30_bad": 0.9972700952380953,
            "mae": 0.08998784272205085,
            "mse": 0.01822760270836635,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7411598864447733,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04868695032596588
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.162097004199028
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40252900401353836
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.775275817656517
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
            "pearson": 0.9715799059434862,
            "spearman": 0.9868854147106655,
            "auroc_top30_worst": 0.992688761904762,
            "pairwise_seed_ranking": 0.9416,
            "predicted_best_mean_error": 1.5603282136917114,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.0984240256547928,
            "gap_to_oracle": 0.0011950532197950725,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46527370834350584
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7578777682322723
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0915063680648804
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3471341720267909
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.585165333747864,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.508904514948527,
                "rejected_mean_error": 2.783771734237671,
                "gap_rejected_minus_accepted": 1.274867219289144
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.125594675540924,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3464021362133698,
                "rejected_mean_error": 2.5045055733702055,
                "gap_rejected_minus_accepted": 1.1581034371568357
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6981570720672607,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0915063680648804,
                "rejected_mean_error": 2.1812761056900025,
                "gap_rejected_minus_accepted": 1.089769737625122
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1532002389431,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7586368057674493,
                "rejected_mean_error": 1.929600561250363,
                "gap_rejected_minus_accepted": 1.1709637554829138
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6436466217041015,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5263359484407637,
                "rejected_mean_error": 2.850498857498169,
                "gap_rejected_minus_accepted": 1.3241629090574052
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1491597294807434,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.363469691359423,
                "rejected_mean_error": 2.5352258341653005,
                "gap_rejected_minus_accepted": 1.1717561428058774
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7199560403823853,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1116376202106475,
                "rejected_mean_error": 2.2058668584823606,
                "gap_rejected_minus_accepted": 1.0942292382717131
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1754668354988098,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7664818238644373,
                "rejected_mean_error": 1.9593567108725483,
                "gap_rejected_minus_accepted": 1.192874887008111
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9859570257873721,
            "spearman": 0.9852145894024148,
            "auroc_top30_bad": 0.9894087619047619,
            "mae": 0.08632990662585945,
            "mse": 0.018677923676575586,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.7180967812024935,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.038505117535591125
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17478460129499435
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5727324866712094
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9600281368533771
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
            "pearson": 0.9523556490938284,
            "spearman": 0.9701053611735132,
            "auroc_top30_worst": 0.9736655238095238,
            "pairwise_seed_ranking": 0.9376,
            "predicted_best_mean_error": 1.741837732553482,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10176315331459063,
            "gap_to_oracle": 0.0019870142936706525,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8868397870063782
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.184026793600657
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4393260396003724
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6127549474046174
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.345066952705384,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7252814967367385,
                "rejected_mean_error": 2.5865073013305664,
                "gap_rejected_minus_accepted": 0.8612258045938279
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.012446403503418,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.612381353894827,
                "rejected_mean_error": 2.4072005364079825,
                "gap_rejected_minus_accepted": 0.7948191825131554
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.812020480632782,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4393260396003724,
                "rejected_mean_error": 2.18348211479187,
                "gap_rejected_minus_accepted": 0.7441560751914975
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.502666711807251,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1854907527518348,
                "rejected_mean_error": 2.020487183440584,
                "gap_rejected_minus_accepted": 0.8349964306887494
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.424348449707031,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7504408831066556,
                "rejected_mean_error": 2.682040910720825,
                "gap_rejected_minus_accepted": 0.9316000276141696
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0319010615348816,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6235610367780062,
                "rejected_mean_error": 2.496735041103666,
                "gap_rejected_minus_accepted": 0.8731740043256597
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8309992551803589,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4484578409194946,
                "rejected_mean_error": 2.2387439308166504,
                "gap_rejected_minus_accepted": 0.7902860898971558
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5199407041072845,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1922717453941467,
                "rejected_mean_error": 2.0630326283806784,
                "gap_rejected_minus_accepted": 0.8707608829865316
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9900299474876024,
            "spearman": 0.9727532754652263,
            "auroc_top30_bad": 0.9659178571428572,
            "mae": 0.09821696265018545,
            "mse": 0.016855975403407983,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7209926541101729,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04077295506373048
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16961962796002628
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6635689851082861
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0588097646261254
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
            "pearson": 0.94799802786533,
            "spearman": 0.9152678432678434,
            "auroc_top30_worst": 0.9705142857142857,
            "pairwise_seed_ranking": 0.9115,
            "predicted_best_mean_error": 1.8646962240338325,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.06153383940458301,
            "gap_to_oracle": 0.0013948369026184348,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2900814342498779
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4568535947799683
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6605586161613464
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7631287428538005
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.23510582447052,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.843517624007331,
                "rejected_mean_error": 2.555958354473114,
                "gap_rejected_minus_accepted": 0.7124407304657829
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0261029601097107,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7631287428538005,
                "rejected_mean_error": 2.369660559654236,
                "gap_rejected_minus_accepted": 0.6065318168004354
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.854097843170166,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6605586161613464,
                "rejected_mean_error": 2.168964777946472,
                "gap_rejected_minus_accepted": 0.5084061617851257
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6160702407360077,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4568535947799683,
                "rejected_mean_error": 2.067397731145223,
                "gap_rejected_minus_accepted": 0.6105441363652548
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2514196157455446,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8537567880418566,
                "rejected_mean_error": 2.5784895420074463,
                "gap_rejected_minus_accepted": 0.7247327539655897
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.024988055229187,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7702764439582825,
                "rejected_mean_error": 2.394090921878815,
                "gap_rejected_minus_accepted": 0.6238144779205324
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8583497405052185,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6677320003509521,
                "rejected_mean_error": 2.184728126525879,
                "gap_rejected_minus_accepted": 0.5169961261749267
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.6497353911399841,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.465999219417572,
                "rejected_mean_error": 2.0796403447786966,
                "gap_rejected_minus_accepted": 0.6136411253611247
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
      "best_epoch": 96,
      "best_calib_loss": 0.008041086606681347,
      "train_time_sec": 55.529476165771484,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9991368241053727,
            "spearman": 0.9978822290906001,
            "auroc_top30_bad": 0.9991924761904761,
            "mae": 0.032450115465958516,
            "mse": 0.00186884003745126,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8092073096391493,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0023963244557380675
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17284386840760707
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4756361640915275
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8231645176718633
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
            "pearson": 0.9989193104970651,
            "spearman": 0.9979728068949121,
            "auroc_top30_worst": 0.9981990476190477,
            "pairwise_seed_ranking": 0.9551,
            "predicted_best_mean_error": 1.7742520278990268,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07577368339896218,
            "gap_to_oracle": 0.0006129146516322681,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6044007534384728
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8414492670297623
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1152674594521523
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.361913753358523
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4415972709655773,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5682001456485855,
                "rejected_mean_error": 4.288735042572021,
                "gap_rejected_minus_accepted": 2.7205348969234358
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1527984738349915,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.361913753358523,
                "rejected_mean_error": 3.275273281288147,
                "gap_rejected_minus_accepted": 1.9133595279296238
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.654466152191162,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1152674594521523,
                "rejected_mean_error": 2.5652398112297057,
                "gap_rejected_minus_accepted": 1.4499723517775533
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1563575267791748,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8414492670297623,
                "rejected_mean_error": 2.1731884247779845,
                "gap_rejected_minus_accepted": 1.3317391577482223
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.433413767814636,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5773755447069804,
                "rejected_mean_error": 4.303877210617065,
                "gap_rejected_minus_accepted": 2.7265016659100847
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1711632013320923,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3728413114547728,
                "rejected_mean_error": 3.2815789108276365,
                "gap_rejected_minus_accepted": 1.9087375993728637
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.668803870677948,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1223594505786896,
                "rejected_mean_error": 2.577691972017288,
                "gap_rejected_minus_accepted": 1.4553325214385986
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.169671356678009,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8450853066444397,
                "rejected_mean_error": 2.1850058461825053,
                "gap_rejected_minus_accepted": 1.3399205395380656
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9889550250001597,
            "spearman": 0.9845265211495554,
            "auroc_top30_bad": 0.996919619047619,
            "mae": 0.09210306760091316,
            "mse": 0.01765446907114688,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7063741129285686,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07814091235399247
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1722997358083725
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4028512720704079
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7749734653234481
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
            "pearson": 0.9851603683292817,
            "spearman": 0.9905330484051511,
            "auroc_top30_worst": 0.9975100952380952,
            "pairwise_seed_ranking": 0.9312,
            "predicted_best_mean_error": 1.5602541329860686,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09849810636043554,
            "gap_to_oracle": 0.0011209725141523297,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4673081593513489
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7528410869149061
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0947474561691284
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3430546065891729
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4719185113906863,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4983412880367704,
                "rejected_mean_error": 2.8788407764434814,
                "gap_rejected_minus_accepted": 1.380499488406711
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0407480597496033,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3421849475471799,
                "rejected_mean_error": 2.5171301924763396,
                "gap_rejected_minus_accepted": 1.1749452449291597
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5769214630126953,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0947474561691284,
                "rejected_mean_error": 2.1780350175857546,
                "gap_rejected_minus_accepted": 1.0832875614166262
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0529286861419678,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7541811304351392,
                "rejected_mean_error": 1.9310889565321272,
                "gap_rejected_minus_accepted": 1.176907826096988
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4948259353637696,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5163743952910105,
                "rejected_mean_error": 2.9401528358459474,
                "gap_rejected_minus_accepted": 1.423778440554937
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0733348727226257,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3588235061117673,
                "rejected_mean_error": 2.5490168919638982,
                "gap_rejected_minus_accepted": 1.190193385852131
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.587914526462555,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1137635748386383,
                "rejected_mean_error": 2.2037409038543703,
                "gap_rejected_minus_accepted": 1.089977329015732
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.089280217885971,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7691621520216503,
                "rejected_mean_error": 1.9584537126163748,
                "gap_rejected_minus_accepted": 1.1892915605947245
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9845643675350388,
            "spearman": 0.982586721065668,
            "auroc_top30_bad": 0.9933725714285714,
            "mae": 0.10102633323327682,
            "mse": 0.022018897828032267,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6927759140997308,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06708641916513443
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18959687370061876
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5747604095876216
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9582477506915729
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
            "pearson": 0.9693555230297088,
            "spearman": 0.9767294130033373,
            "auroc_top30_worst": 0.9834392380952381,
            "pairwise_seed_ranking": 0.9164,
            "predicted_best_mean_error": 1.7428799850940704,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.1007209007740022,
            "gap_to_oracle": 0.003029266834259081,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8910648636817932
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1917819657768958
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4355484112739563
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.610251612945406
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2879314661026005,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7234491240713332,
                "rejected_mean_error": 2.602998655319214,
                "gap_rejected_minus_accepted": 0.8795495312478807
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0157951712608337,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6098795766000942,
                "rejected_mean_error": 2.414689882494771,
                "gap_rejected_minus_accepted": 0.804810305894677
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7941144704818726,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4355484112739563,
                "rejected_mean_error": 2.187259743118286,
                "gap_rejected_minus_accepted": 0.7517113318443298
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4775662124156952,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1925896807981375,
                "rejected_mean_error": 2.018115823271435,
                "gap_rejected_minus_accepted": 0.8255261424732974
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3601565599441527,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7487985308965046,
                "rejected_mean_error": 2.6968220806121828,
                "gap_rejected_minus_accepted": 0.9480235497156781
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0336264967918396,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.62052328637577,
                "rejected_mean_error": 2.505751855789669,
                "gap_rejected_minus_accepted": 0.885228569413899
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8147030472755432,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4452061729431152,
                "rejected_mean_error": 2.2419955987930296,
                "gap_rejected_minus_accepted": 0.7967894258499144
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4880579710006714,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.20221465731424,
                "rejected_mean_error": 2.0596828773059945,
                "gap_rejected_minus_accepted": 0.8574682199917545
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.986905468034234,
            "spearman": 0.9698866858703737,
            "auroc_top30_bad": 0.9632773809523809,
            "mae": 0.11643095758127618,
            "mse": 0.024286518461603474,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7085933691389564,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07804277377203107
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1724835897758603
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6616252826489508
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0575734669392307
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
            "pearson": 0.9531724198760962,
            "spearman": 0.9273673953673954,
            "auroc_top30_worst": 0.9649809523809524,
            "pairwise_seed_ranking": 0.9035,
            "predicted_best_mean_error": 1.8657283148169517,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.06050174862146385,
            "gap_to_oracle": 0.002426927685737601,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2934223437309265
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4496774611473084
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6544986412525178
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7614254655838013
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.237622857093811,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8468261779679191,
                "rejected_mean_error": 2.5261813688278196,
                "gap_rejected_minus_accepted": 0.6793551908599005
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9724620282649994,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7614254655838013,
                "rejected_mean_error": 2.3747703914642333,
                "gap_rejected_minus_accepted": 0.613344925880432
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7612414956092834,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6544986412525178,
                "rejected_mean_error": 2.175024752855301,
                "gap_rejected_minus_accepted": 0.5205261116027831
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.575973242521286,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4496774611473084,
                "rejected_mean_error": 2.069789775689443,
                "gap_rejected_minus_accepted": 0.6201123145421346
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2434802055358887,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8588474578327603,
                "rejected_mean_error": 2.532673513889313,
                "gap_rejected_minus_accepted": 0.6738260560565525
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9811332821846008,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.768564188480377,
                "rejected_mean_error": 2.3992276883125303,
                "gap_rejected_minus_accepted": 0.6306634998321532
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.768162190914154,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6607888698577882,
                "rejected_mean_error": 2.191671257019043,
                "gap_rejected_minus_accepted": 0.5308823871612547
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5805215537548065,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.456432433128357,
                "rejected_mean_error": 2.0828292735417686,
                "gap_rejected_minus_accepted": 0.6263968404134117
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
      "best_epoch": 107,
      "best_calib_loss": 0.006677134893834591,
      "train_time_sec": 61.464592933654785,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994030716211482,
            "spearman": 0.9980034573150591,
            "auroc_top30_bad": 0.9993815714285715,
            "mae": 0.031194778033961847,
            "mse": 0.001802375826062044,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8194246812901924,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0034678641483187676
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1728452033251524
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47521742453426125
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8229901382436355
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
            "pearson": 0.9994299663591473,
            "spearman": 0.998928954069158,
            "auroc_top30_worst": 0.9989041904761905,
            "pairwise_seed_ranking": 0.9643,
            "predicted_best_mean_error": 1.7740681992173195,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07595751208066948,
            "gap_to_oracle": 0.0004290859699249694,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6049600160717964
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8406506377458572
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1147692432045937
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3619111805359523
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.5056962013244632,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681219244334432,
                "rejected_mean_error": 4.289439033508301,
                "gap_rejected_minus_accepted": 2.7213171090748576
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.153155505657196,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3619111805359523,
                "rejected_mean_error": 3.2752809997558594,
                "gap_rejected_minus_accepted": 1.9133698192199071
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6582017540931702,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1147692432045937,
                "rejected_mean_error": 2.5657380274772645,
                "gap_rejected_minus_accepted": 1.4509687842726708
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1549908518791199,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8406506377458572,
                "rejected_mean_error": 2.1734546345392864,
                "gap_rejected_minus_accepted": 1.3328039967934293
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.447411203384401,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1607940793037415,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3729101495742797,
                "rejected_mean_error": 3.2813723964691164,
                "gap_rejected_minus_accepted": 1.9084622468948367
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.67666894197464,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.121369829416275,
                "rejected_mean_error": 2.5786815931797027,
                "gap_rejected_minus_accepted": 1.4573117637634276
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1572034657001495,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8442430753707886,
                "rejected_mean_error": 2.185286589940389,
                "gap_rejected_minus_accepted": 1.3410435145696005
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9909112975339469,
            "spearman": 0.9839717264772297,
            "auroc_top30_bad": 0.9987451428571429,
            "mae": 0.08364963804795952,
            "mse": 0.014051439125676078,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.976,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7167691107716737,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08088699951767922
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17801242952346802
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40284453650712965
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7735457168340683
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
            "pearson": 0.9918000526296931,
            "spearman": 0.9965432174996594,
            "auroc_top30_worst": 0.9991009523809524,
            "pairwise_seed_ranking": 0.9312,
            "predicted_best_mean_error": 1.560111884355545,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09864035499095913,
            "gap_to_oracle": 0.0009787238836287404,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46727479457855225
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7480235103613291
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0917003959655762
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.342802558880625
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.559196496009827,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.497080921596951,
                "rejected_mean_error": 2.8901840744018554,
                "gap_rejected_minus_accepted": 1.3931031528049045
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.064602315425873,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3419542231198436,
                "rejected_mean_error": 2.517820891480857,
                "gap_rejected_minus_accepted": 1.1758666683610135
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5719210505485535,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0917003959655762,
                "rejected_mean_error": 2.1810820777893065,
                "gap_rejected_minus_accepted": 1.0893816818237303
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0188585817813873,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7494642285112375,
                "rejected_mean_error": 1.9326646132046792,
                "gap_rejected_minus_accepted": 1.1832003846934418
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5764347076416017,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5157854431205326,
                "rejected_mean_error": 2.945453405380249,
                "gap_rejected_minus_accepted": 1.4296679622597164
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0702664852142334,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3588356221104687,
                "rejected_mean_error": 2.548980928602673,
                "gap_rejected_minus_accepted": 1.190145306492204
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5695729851722717,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1112985203266144,
                "rejected_mean_error": 2.206205958366394,
                "gap_rejected_minus_accepted": 1.0949074380397796
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.031731516122818,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7621347000674595,
                "rejected_mean_error": 1.9608212499057545,
                "gap_rejected_minus_accepted": 1.1986865498382948
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9882002465168681,
            "spearman": 0.9856393517235498,
            "auroc_top30_bad": 0.9958811428571428,
            "mae": 0.08482634563293687,
            "mse": 0.015509044515238178,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7180117262594388,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0755295872092247
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18417544869184493
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5738794717252255
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9569892242074013
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
            "pearson": 0.9826232698935433,
            "spearman": 0.9869715751097848,
            "auroc_top30_worst": 0.9888731428571429,
            "pairwise_seed_ranking": 0.918,
            "predicted_best_mean_error": 1.7422933537960053,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10130753207206733,
            "gap_to_oracle": 0.002442635536193949,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.880055272102356
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.180557665725549
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4340582949638367
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.607944403820709
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.452106881141663,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.719737677521176,
                "rejected_mean_error": 2.6364016742706298,
                "gap_rejected_minus_accepted": 0.9166639967494539
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.114388167858124,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6073990979469446,
                "rejected_mean_error": 2.4221154687503654,
                "gap_rejected_minus_accepted": 0.8147163708034209
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8269160389900208,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4340582949638367,
                "rejected_mean_error": 2.188749859428406,
                "gap_rejected_minus_accepted": 0.7546915644645691
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.493402361869812,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1818782222537567,
                "rejected_mean_error": 2.0216939305546697,
                "gap_rejected_minus_accepted": 0.839815708300913
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5468297481536863,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7417262125015258,
                "rejected_mean_error": 2.7604729461669923,
                "gap_rejected_minus_accepted": 1.0187467336654665
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1864511370658875,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.619038435864576,
                "rejected_mean_error": 2.5101592692117842,
                "gap_rejected_minus_accepted": 0.8911208333472083
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.838036596775055,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.44249831199646,
                "rejected_mean_error": 2.244703459739685,
                "gap_rejected_minus_accepted": 0.8022051477432248
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4995915293693542,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1887433983030773,
                "rejected_mean_error": 2.06422132285521,
                "gap_rejected_minus_accepted": 0.8754779245521327
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9901760928461134,
            "spearman": 0.983873713007505,
            "auroc_top30_bad": 0.9881285714285715,
            "mae": 0.09496313994954653,
            "mse": 0.016521778713503642,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7324583119568314,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08546131366863846
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17727300099283458
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6608466180600225
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.050693025432527
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
            "pearson": 0.9823921898646232,
            "spearman": 0.977957513957514,
            "auroc_top30_worst": 0.9881761904761904,
            "pairwise_seed_ranking": 0.918,
            "predicted_best_mean_error": 1.8647223982214927,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.06150766521692286,
            "gap_to_oracle": 0.00142101109027859,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2700722587108613
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4445733075141907
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.637933468580246
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7606226326624552
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3048421621322635,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8409775270356072,
                "rejected_mean_error": 2.578819227218628,
                "gap_rejected_minus_accepted": 0.7378417001830209
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0773942470550537,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7606226326624552,
                "rejected_mean_error": 2.3771788902282713,
                "gap_rejected_minus_accepted": 0.6165562575658161
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8078102469444275,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.637933468580246,
                "rejected_mean_error": 2.191589925527573,
                "gap_rejected_minus_accepted": 0.5536564569473268
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5716554820537567,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4445733075141907,
                "rejected_mean_error": 2.0714911602338155,
                "gap_rejected_minus_accepted": 0.6269178527196249
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.318059349060058,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8509235898653666,
                "rejected_mean_error": 2.603988325595856,
                "gap_rejected_minus_accepted": 0.7530647357304892
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0679097175598145,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7680630159378052,
                "rejected_mean_error": 2.4007312059402466,
                "gap_rejected_minus_accepted": 0.6326681900024413
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.838705062866211,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6466595339775085,
                "rejected_mean_error": 2.2058005928993225,
                "gap_rejected_minus_accepted": 0.559141058921814
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5586790442466736,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4543498945236206,
                "rejected_mean_error": 2.0835234530766806,
                "gap_rejected_minus_accepted": 0.62917355855306
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
      "best_epoch": 116,
      "best_calib_loss": 0.007693306542932987,
      "train_time_sec": 41.74898052215576,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9995803861144565,
            "spearman": 0.9990353819573834,
            "auroc_top30_bad": 0.9997055714285714,
            "mae": 0.03485302544220344,
            "mse": 0.0034949892643669775,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8327340634032401,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00011610902845859527
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1723916396945715
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4750624132141471
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8226529404789209
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
            "pearson": 0.9993014048940982,
            "spearman": 0.9992751629629716,
            "auroc_top30_worst": 0.9993059047619048,
            "pairwise_seed_ranking": 0.9674,
            "predicted_best_mean_error": 1.7740072233080864,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07601848798990263,
            "gap_to_oracle": 0.0003681100606918175,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6039488607048988
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.840451169514656
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.114672446167469
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3618505570491155
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.6274292707443245,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5682035540805923,
                "rejected_mean_error": 4.28870436668396,
                "gap_rejected_minus_accepted": 2.720500812603367
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.166634976863861,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3618505570491155,
                "rejected_mean_error": 3.2754628702163697,
                "gap_rejected_minus_accepted": 1.9136123131672542
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6567432284355164,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.114672446167469,
                "rejected_mean_error": 2.565834824514389,
                "gap_rejected_minus_accepted": 1.4511623783469199
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.16315758228302,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.840451169514656,
                "rejected_mean_error": 2.1735211239496866,
                "gap_rejected_minus_accepted": 1.3330699544350306
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.576975440979006,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1891124844551086,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3727004629770914,
                "rejected_mean_error": 3.282001456260681,
                "gap_rejected_minus_accepted": 1.9093009932835896
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6895328164100647,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1213449375629425,
                "rejected_mean_error": 2.5787064850330355,
                "gap_rejected_minus_accepted": 1.457361547470093
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1790814399719238,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8438240637779236,
                "rejected_mean_error": 2.185426260471344,
                "gap_rejected_minus_accepted": 1.3416021966934206
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9889251795808068,
            "spearman": 0.9887007679030653,
            "auroc_top30_bad": 0.997992380952381,
            "mae": 0.08785156629022858,
            "mse": 0.017734161150240593,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7114706522620776,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04732944288849831
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1660916111946106
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40359996162652967
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7742928553660711
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
            "pearson": 0.9802038709910826,
            "spearman": 0.9911671157549542,
            "auroc_top30_worst": 0.996120380952381,
            "pairwise_seed_ranking": 0.9284,
            "predicted_best_mean_error": 1.561667867064476,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09708437228202826,
            "gap_to_oracle": 0.00253470659255961,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4764111328125
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7517126164375207
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0922760353088379
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3437973373988543
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.42312502861023,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5023196923997668,
                "rejected_mean_error": 2.8430351371765137,
                "gap_rejected_minus_accepted": 1.3407154447767469
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.003251791000366,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3430223400081363,
                "rejected_mean_error": 2.51462336584402,
                "gap_rejected_minus_accepted": 1.1716010258358835
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6012588739395142,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0922760353088379,
                "rejected_mean_error": 2.180506438446045,
                "gap_rejected_minus_accepted": 1.0882304031372072
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0850891768932343,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7535386253088808,
                "rejected_mean_error": 1.9313035820438869,
                "gap_rejected_minus_accepted": 1.1777649567350061
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4548245191574094,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5206976171334585,
                "rejected_mean_error": 2.901243839263916,
                "gap_rejected_minus_accepted": 1.3805462221304576
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.016580879688263,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.360217152591695,
                "rejected_mean_error": 2.544880195269509,
                "gap_rejected_minus_accepted": 1.184663042677814
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6339582204818726,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1106595594882964,
                "rejected_mean_error": 2.2068449192047117,
                "gap_rejected_minus_accepted": 1.0961853597164153
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1252073049545288,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7624403394403911,
                "rejected_mean_error": 1.9607182804913443,
                "gap_rejected_minus_accepted": 1.1982779410509532
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9868417571910949,
            "spearman": 0.9836532211454969,
            "auroc_top30_bad": 0.9922140952380953,
            "mae": 0.09370676298810622,
            "mse": 0.018511059088763507,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7025880561037099,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0421978959441185
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1944573495745659
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.573460536044836
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9597542922616005
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
            "pearson": 0.9738625761699472,
            "spearman": 0.9740584102375363,
            "auroc_top30_worst": 0.976368761904762,
            "pairwise_seed_ranking": 0.9272,
            "predicted_best_mean_error": 1.7422982298135758,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10130265605449673,
            "gap_to_oracle": 0.0024475115537645475,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8861781449317933
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1853787067991037
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4385024664878845
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6107268482764392
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3264218568801884,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.721027746041616,
                "rejected_mean_error": 2.6247910575866698,
                "gap_rejected_minus_accepted": 0.9037633115450538
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0389976501464844,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.610078297849653,
                "rejected_mean_error": 2.414094988530436,
                "gap_rejected_minus_accepted": 0.8040166906807831
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7904489040374756,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4385024664878845,
                "rejected_mean_error": 2.184305687904358,
                "gap_rejected_minus_accepted": 0.7458032214164736
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.458607167005539,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1858418759065694,
                "rejected_mean_error": 2.0203698925681914,
                "gap_rejected_minus_accepted": 0.834528016661622
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4263214588165285,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.743670499059889,
                "rejected_mean_error": 2.7429743671417235,
                "gap_rejected_minus_accepted": 0.9993038680818345
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1005914211273193,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6213194590838835,
                "rejected_mean_error": 2.5033886129893954,
                "gap_rejected_minus_accepted": 0.8820691539055119
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8176356554031372,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.44578302192688,
                "rejected_mean_error": 2.2414187498092653,
                "gap_rejected_minus_accepted": 0.7956357278823853
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4683047533035278,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1921938052253118,
                "rejected_mean_error": 2.0630588862985215,
                "gap_rejected_minus_accepted": 0.8708650810732097
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9866811997133412,
            "spearman": 0.9768987089504754,
            "auroc_top30_bad": 0.9729142857142857,
            "mae": 0.10778425934410393,
            "mse": 0.020385437172910643,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.995,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7259015948577766,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05684131231158972
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17236364720016717
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6609620622433722
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0566490491256118
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
            "pearson": 0.9358615123896339,
            "spearman": 0.9366810366810367,
            "auroc_top30_worst": 0.9656428571428571,
            "pairwise_seed_ranking": 0.9155,
            "predicted_best_mean_error": 1.864935013949871,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.06129504948854447,
            "gap_to_oracle": 0.0016336268186569747,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.287382069826126
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4436185231208802
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6476746609210968
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7648968281745911
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.40177800655365,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8556305172708298,
                "rejected_mean_error": 2.4469423151016234,
                "gap_rejected_minus_accepted": 0.5913117978307936
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0345221161842346,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7648968281745911,
                "rejected_mean_error": 2.364356303691864,
                "gap_rejected_minus_accepted": 0.5994594755172729
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7936722040176392,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6476746609210968,
                "rejected_mean_error": 2.181848733186722,
                "gap_rejected_minus_accepted": 0.5341740722656252
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.576576977968216,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4436185231208802,
                "rejected_mean_error": 2.0718094216982523,
                "gap_rejected_minus_accepted": 0.6281908985773721
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4021382093429566,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8719895097944472,
                "rejected_mean_error": 2.414395046234131,
                "gap_rejected_minus_accepted": 0.5424055364396838
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.027137339115143,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7709099181493124,
                "rejected_mean_error": 2.392190499305725,
                "gap_rejected_minus_accepted": 0.6212805811564126
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8133741617202759,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6547445273399353,
                "rejected_mean_error": 2.1977155995368958,
                "gap_rejected_minus_accepted": 0.5429710721969605
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5984450280666351,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4535306334495544,
                "rejected_mean_error": 2.0837965401013694,
                "gap_rejected_minus_accepted": 0.630265906651815
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
      "best_epoch": 115,
      "best_calib_loss": 0.008065130561590195,
      "train_time_sec": 55.52217984199524,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998630952320264,
            "spearman": 0.9990686726932277,
            "auroc_top30_bad": 0.9998449523809524,
            "mae": 0.016640386301576292,
            "mse": 0.0005717850128879479,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8131566928877925,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0007529318705201148
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1724240600556135
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47504787077754734
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8224994279215733
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
            "pearson": 0.999856073686963,
            "spearman": 0.9997743629349636,
            "auroc_top30_worst": 0.9998721904761905,
            "pairwise_seed_ranking": 0.961,
            "predicted_best_mean_error": 1.7740286352932453,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.0759970760047437,
            "gap_to_oracle": 0.0003895220458507431,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6038189488053322
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8402816651582717
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.114432358801365
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3616185534556706
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.49781620502472,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681219244334432,
                "rejected_mean_error": 4.289439033508301,
                "gap_rejected_minus_accepted": 2.7213171090748576
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1470927596092224,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3616185534556706,
                "rejected_mean_error": 3.276158880996704,
                "gap_rejected_minus_accepted": 1.9145403275410335
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6441670060157776,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.114432358801365,
                "rejected_mean_error": 2.5660749118804933,
                "gap_rejected_minus_accepted": 1.4516425530791284
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1587803959846497,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8402816651582717,
                "rejected_mean_error": 2.1735776254018147,
                "gap_rejected_minus_accepted": 1.333295960243543
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.4619088649749763,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1771671772003174,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.372542857170105,
                "rejected_mean_error": 3.2824742736816406,
                "gap_rejected_minus_accepted": 1.9099314165115355
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6603214740753174,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1211004011631012,
                "rejected_mean_error": 2.578951021432877,
                "gap_rejected_minus_accepted": 1.4578506202697756
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1705314218997955,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8437981719970703,
                "rejected_mean_error": 2.1854348910649617,
                "gap_rejected_minus_accepted": 1.3416367190678913
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9889460701506255,
            "spearman": 0.9871425019987901,
            "auroc_top30_bad": 0.9982880000000001,
            "mae": 0.09144431468357152,
            "mse": 0.01782897105807806,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7057471475512038,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07696703866124154
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1664993848323822
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4020249282956123
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.773644490536054
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
            "pearson": 0.9834616088718204,
            "spearman": 0.993471774637936,
            "auroc_top30_worst": 0.9992380952380953,
            "pairwise_seed_ranking": 0.9384,
            "predicted_best_mean_error": 1.560132944226265,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09861929512023915,
            "gap_to_oracle": 0.0009997837543487265,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46970237398147585
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7489926429131092
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0918056179046631
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3427203034541246
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.475290036201477,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.503102375878228,
                "rejected_mean_error": 2.835990985870361,
                "gap_rejected_minus_accepted": 1.332888609992133
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0161219239234924,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3418902177820846,
                "rejected_mean_error": 2.5180124985143397,
                "gap_rejected_minus_accepted": 1.176122280732255
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.582757294178009,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0918056179046631,
                "rejected_mean_error": 2.18097685585022,
                "gap_rejected_minus_accepted": 1.0891712379455567
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0430286824703217,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.750044675680776,
                "rejected_mean_error": 1.9324707178321439,
                "gap_rejected_minus_accepted": 1.1824260421513677
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5129529237747192,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5213138624032339,
                "rejected_mean_error": 2.8956976318359375,
                "gap_rejected_minus_accepted": 1.3743837694327037
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0382121205329895,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3587402113299956,
                "rejected_mean_error": 2.5492641320304266,
                "gap_rejected_minus_accepted": 1.190523920700431
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.595045566558838,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1106176645755768,
                "rejected_mean_error": 2.2068868141174316,
                "gap_rejected_minus_accepted": 1.0962691495418548
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.09945809841156,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7643831121543098,
                "rejected_mean_error": 1.960063763480773,
                "gap_rejected_minus_accepted": 1.1956806513264633
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9885714675440888,
            "spearman": 0.9858752165379849,
            "auroc_top30_bad": 0.993583619047619,
            "mae": 0.08785161815779884,
            "mse": 0.01651806960703313,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6995251772494601,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.051465501844882966
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18135024570226668
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5729626432836056
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9583658957441648
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
            "pearson": 0.9761384898223769,
            "spearman": 0.9796286133630221,
            "auroc_top30_worst": 0.9797973333333334,
            "pairwise_seed_ranking": 0.9204,
            "predicted_best_mean_error": 1.7424434130191804,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.1011574728488922,
            "gap_to_oracle": 0.002592694759369074,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8747465138435364
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1836344150778575
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4363152567863464
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.612154800055632
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.329966306686402,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7215250755416023,
                "rejected_mean_error": 2.620315092086792,
                "gap_rejected_minus_accepted": 0.8987900165451899
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0772570371627808,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6117554715374363,
                "rejected_mean_error": 2.409074184231865,
                "gap_rejected_minus_accepted": 0.7973187126944286
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7930002808570862,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4363152567863464,
                "rejected_mean_error": 2.186492897605896,
                "gap_rejected_minus_accepted": 0.7501776408195497
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4680817127227783,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.184108073147722,
                "rejected_mean_error": 2.0209490604054583,
                "gap_rejected_minus_accepted": 0.8368409872577363
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.411792206764221,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7450223482979668,
                "rejected_mean_error": 2.7308077239990234,
                "gap_rejected_minus_accepted": 0.9857853757010566
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1021499633789062,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6210802940123858,
                "rejected_mean_error": 2.5040985156619358,
                "gap_rejected_minus_accepted": 0.8830182216495499
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8124509453773499,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.444160391807556,
                "rejected_mean_error": 2.243041379928589,
                "gap_rejected_minus_accepted": 0.7988809881210328
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5054911971092224,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.190206662056938,
                "rejected_mean_error": 2.0637283516440164,
                "gap_rejected_minus_accepted": 0.8735216895870783
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9906696242777819,
            "spearman": 0.9831161054261965,
            "auroc_top30_bad": 0.9817238095238096,
            "mae": 0.08454587507545284,
            "mse": 0.013964540831711315,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7334918081133995,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06050573142245412
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1728085405305028
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6619712922610342
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.052637931269904
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
            "pearson": 0.9644260835024486,
            "spearman": 0.9625996585996587,
            "auroc_top30_worst": 0.9854857142857143,
            "pairwise_seed_ranking": 0.921,
            "predicted_best_mean_error": 1.8648130229115487,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.061417040526866806,
            "gap_to_oracle": 0.0015116357803346414,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.269529848098755
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4452728924751281
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.64047092461586
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7611635152498881
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.345330333709717,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8482445624139574,
                "rejected_mean_error": 2.5134159088134767,
                "gap_rejected_minus_accepted": 0.6651713463995192
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0593276023864746,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7611635152498881,
                "rejected_mean_error": 2.375556242465973,
                "gap_rejected_minus_accepted": 0.614392727216085
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8506212830543518,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.64047092461586,
                "rejected_mean_error": 2.1890524694919584,
                "gap_rejected_minus_accepted": 0.5485815448760984
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.604815423488617,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4452728924751281,
                "rejected_mean_error": 2.0712579652468364,
                "gap_rejected_minus_accepted": 0.6259850727717082
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.339719033241272,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8594655434290568,
                "rejected_mean_error": 2.527110743522644,
                "gap_rejected_minus_accepted": 0.6676452000935871
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.050788998603821,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7680669260025024,
                "rejected_mean_error": 2.400719475746155,
                "gap_rejected_minus_accepted": 0.6326525497436526
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8737401366233826,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6466442787647246,
                "rejected_mean_error": 2.205815848112106,
                "gap_rejected_minus_accepted": 0.5591715693473815
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5861074328422546,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.45626699924469,
                "rejected_mean_error": 2.0828844181696575,
                "gap_rejected_minus_accepted": 0.6266174189249676
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
      "best_epoch": 107,
      "best_calib_loss": 0.00945836491882801,
      "train_time_sec": 55.43087315559387,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996310225757766,
            "spearman": 0.9984614779870855,
            "auroc_top30_bad": 0.9997630952380951,
            "mae": 0.021449335981189643,
            "mse": 0.0008697285229344752,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8133507779225526,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0022213659659028055
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17311956960856914
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4750956101641059
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8226496628751357
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
            "pearson": 0.9997645689956347,
            "spearman": 0.9995512101580484,
            "auroc_top30_worst": 0.999719619047619,
            "pairwise_seed_ranking": 0.9589,
            "predicted_best_mean_error": 1.7740626649856568,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.0759630463123322,
            "gap_to_oracle": 0.0004235517382622511,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6041926081776618
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8405288673639297
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1145167482495308
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.361750747148196
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.456966853141786,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.5681154932777086,
                "rejected_mean_error": 4.289496913909912,
                "gap_rejected_minus_accepted": 2.7213814206322033
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1202991008758545,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.361750747148196,
                "rejected_mean_error": 3.2757622999191285,
                "gap_rejected_minus_accepted": 1.9140115527709325
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6302974224090576,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1145167482495308,
                "rejected_mean_error": 2.5659905224323274,
                "gap_rejected_minus_accepted": 1.4514737741827966
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1482880115509033,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8405288673639297,
                "rejected_mean_error": 2.1734952246665955,
                "gap_rejected_minus_accepted": 1.3329663573026658
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.42895851135254,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1351834535598755,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3726007639567057,
                "rejected_mean_error": 3.2823005533218383,
                "gap_rejected_minus_accepted": 1.9096997893651326
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6548138856887817,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1214498460292817,
                "rejected_mean_error": 2.578601576566696,
                "gap_rejected_minus_accepted": 1.4571517305374144
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1606799364089966,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8438793053627014,
                "rejected_mean_error": 2.1854078466097513,
                "gap_rejected_minus_accepted": 1.34152854124705
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9860648299106887,
            "spearman": 0.9850036409947679,
            "auroc_top30_bad": 0.997248761904762,
            "mae": 0.09772591725220207,
            "mse": 0.02157305809739102,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7043818657643003,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07248033708333969
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1727991719722748
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.40485213519334795
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7748303961833318
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
            "pearson": 0.9774637790485449,
            "spearman": 0.9884431101715907,
            "auroc_top30_worst": 0.9973546666666666,
            "pairwise_seed_ranking": 0.9308,
            "predicted_best_mean_error": 1.5604918574094773,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09826038193702691,
            "gap_to_oracle": 0.0013586969375609659,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.46682951736450196
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.753444309035937
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0948813177108765
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3436503002384323
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4156015396118167,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.503447178310818,
                "rejected_mean_error": 2.832887763977051,
                "gap_rejected_minus_accepted": 1.3294405856662328
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.022351622581482,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.342943242545316,
                "rejected_mean_error": 2.514860152817382,
                "gap_rejected_minus_accepted": 1.171916910272066
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5757338404655457,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0948813177108765,
                "rejected_mean_error": 2.1779011560440065,
                "gap_rejected_minus_accepted": 1.08301983833313
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0161460936069489,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7542755466680557,
                "rejected_mean_error": 1.9310574172782287,
                "gap_rejected_minus_accepted": 1.176781870610173
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4382609128952026,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5209694153732725,
                "rejected_mean_error": 2.8987976551055907,
                "gap_rejected_minus_accepted": 1.3778282397323183
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.037160336971283,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3595844897675642,
                "rejected_mean_error": 2.5467580992078025,
                "gap_rejected_minus_accepted": 1.1871736094402383
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5869053602218628,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1146230680942535,
                "rejected_mean_error": 2.202881410598755,
                "gap_rejected_minus_accepted": 1.0882583425045016
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.040052205324173,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7667660150263045,
                "rejected_mean_error": 1.9592609673260368,
                "gap_rejected_minus_accepted": 1.1924949522997323
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9846701831554981,
            "spearman": 0.9816838545992975,
            "auroc_top30_bad": 0.9921699047619047,
            "mae": 0.09946076232280798,
            "mse": 0.021452297420595016,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6952191915242545,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05634780588746071
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18612861350774765
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5741319096982479
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.959178504272302
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
            "pearson": 0.9714952666409572,
            "spearman": 0.9751451708707324,
            "auroc_top30_worst": 0.9770666666666667,
            "pairwise_seed_ranking": 0.9172,
            "predicted_best_mean_error": 1.7425780894756318,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10102279639244083,
            "gap_to_oracle": 0.002727371215820451,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8881410579681397
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1844191312407837
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4367899348258972
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6135498190612427
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.310151505470276,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7205710977448359,
                "rejected_mean_error": 2.6289008922576906,
                "gap_rejected_minus_accepted": 0.9083297945128548
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.039056122303009,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.613193295363301,
                "rejected_mean_error": 2.40476990012696,
                "gap_rejected_minus_accepted": 0.791576604763659
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.79332035779953,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4367899348258972,
                "rejected_mean_error": 2.1860182195663453,
                "gap_rejected_minus_accepted": 0.7492282847404481
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.485722839832306,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1854169747699945,
                "rejected_mean_error": 2.020511828593536,
                "gap_rejected_minus_accepted": 0.8350948538235414
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4308697462081907,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7459682575861613,
                "rejected_mean_error": 2.7222945404052736,
                "gap_rejected_minus_accepted": 0.9763262828191124
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.067417621612549,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6242292743315672,
                "rejected_mean_error": 2.4947515423335727,
                "gap_rejected_minus_accepted": 0.8705222680020055
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8294002413749695,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.445065710067749,
                "rejected_mean_error": 2.242136061668396,
                "gap_rejected_minus_accepted": 0.797070351600647
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.508175641298294,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.187995681687007,
                "rejected_mean_error": 2.0644732273836186,
                "gap_rejected_minus_accepted": 0.8764775456966116
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9864096034188706,
            "spearman": 0.9714639728416326,
            "auroc_top30_bad": 0.9689773809523808,
            "mae": 0.10774113512019899,
            "mse": 0.0219993537294823,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7110748127894378,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06996327484026552
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17250414542108775
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6633458504714072
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0581630678201714
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
            "pearson": 0.9428551599610013,
            "spearman": 0.9280765000765002,
            "auroc_top30_worst": 0.951442857142857,
            "pairwise_seed_ranking": 0.921,
            "predicted_best_mean_error": 1.864861823618412,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.0613682398200035,
            "gap_to_oracle": 0.001560436487197947,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.285879558324814
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4466323390007019
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6514258077144623
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.766869042078654
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.297745633125305,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8483152548472086,
                "rejected_mean_error": 2.512779676914215,
                "gap_rejected_minus_accepted": 0.6644644220670064
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9956800937652588,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.766869042078654,
                "rejected_mean_error": 2.3584396619796753,
                "gap_rejected_minus_accepted": 0.5915706199010213
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7842456698417664,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6514258077144623,
                "rejected_mean_error": 2.1780975863933563,
                "gap_rejected_minus_accepted": 0.5266717786788939
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.575339436531067,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4466323390007019,
                "rejected_mean_error": 2.0708048164049786,
                "gap_rejected_minus_accepted": 0.6241724774042767
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2985279321670533,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8599929849306742,
                "rejected_mean_error": 2.522363770008087,
                "gap_rejected_minus_accepted": 0.6623707850774128
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.982166826725006,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.77516348918279,
                "rejected_mean_error": 2.3794297862052916,
                "gap_rejected_minus_accepted": 0.6042662970225015
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7920840978622437,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6536606872081756,
                "rejected_mean_error": 2.1987994396686554,
                "gap_rejected_minus_accepted": 0.5451387524604798
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.583880752325058,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4572707104682923,
                "rejected_mean_error": 2.08254984776179,
                "gap_rejected_minus_accepted": 0.6252791372934976
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
      "best_epoch": 120,
      "best_calib_loss": 0.006530808284878731,
      "train_time_sec": 61.15886974334717,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9994554231765251,
            "spearman": 0.9981636471345139,
            "auroc_top30_bad": 0.9993684047619048,
            "mae": 0.03725615732895094,
            "mse": 0.002734938668694629,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8262542518478819,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0032740197107195856
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17309651388823985
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47525774290412665
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8227712879965703
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
            "pearson": 0.999561317556861,
            "spearman": 0.99907980134717,
            "auroc_top30_worst": 0.9995419047619047,
            "pairwise_seed_ranking": 0.965,
            "predicted_best_mean_error": 1.7740852531790734,
            "seed0_mean_error": 1.850025711297989,
            "random_seed_mean_error": 1.841148916900158,
            "oracle_best_mean_error": 1.7736391132473945,
            "improvement_over_seed0": 0.07594045811891559,
            "gap_to_oracle": 0.00044613993167885724,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6047256632447243
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8407910828828812
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1148231270432472
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3617649102926255
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8402536353409291
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.564348053932192,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.568100977877776,
                "rejected_mean_error": 4.289627552509308,
                "gap_rejected_minus_accepted": 2.721526574631532
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1885836124420166,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3617649102926255,
                "rejected_mean_error": 3.27571981048584,
                "gap_rejected_minus_accepted": 1.9139549001932143
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.676188349723816,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.1148231270432472,
                "rejected_mean_error": 2.565684143638611,
                "gap_rejected_minus_accepted": 1.4508610165953637
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1643881499767303,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8407910828828812,
                "rejected_mean_error": 2.1734078194936117,
                "gap_rejected_minus_accepted": 1.3326167366107304
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.5148164987564106,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.5771077304416232,
                "rejected_mean_error": 4.30628753900528,
                "gap_rejected_minus_accepted": 2.7291798085636563
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2297272086143494,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.3727525062561035,
                "rejected_mean_error": 3.281845326423645,
                "gap_rejected_minus_accepted": 1.9090928201675417
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6958653330802917,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.1214720470905304,
                "rejected_mean_error": 2.5785793755054476,
                "gap_rejected_minus_accepted": 1.4571073284149172
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1755729019641876,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8443252849578857,
                "rejected_mean_error": 2.1852591867446898,
                "gap_rejected_minus_accepted": 1.340933901786804
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9909824866061713,
            "spearman": 0.9830896142626924,
            "auroc_top30_bad": 0.9971139047619048,
            "mae": 0.08481975901873375,
            "mse": 0.013685240744430767,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.724970821982196,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08585399362444877
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17491567544937134
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.403042931997776
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7747768802404403
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
            "pearson": 0.9922349201673075,
            "spearman": 0.9925554456034854,
            "auroc_top30_worst": 0.9960441904761905,
            "pairwise_seed_ranking": 0.9356,
            "predicted_best_mean_error": 1.5605587395429612,
            "seed0_mean_error": 1.6587522393465042,
            "random_seed_mean_error": 1.6395123422145843,
            "oracle_best_mean_error": 1.5591331604719163,
            "improvement_over_seed0": 0.09819349980354297,
            "gap_to_oracle": 0.0014255790710449023,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4668586115837097
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7539002878161577
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0944733489990235
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.344345755287325
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6363912368774414
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5539666414260878,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4962557866838244,
                "rejected_mean_error": 2.8976102886199953,
                "gap_rejected_minus_accepted": 1.4013545019361708
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.060366988182068,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3434670939643967,
                "rejected_mean_error": 2.5132919458535534,
                "gap_rejected_minus_accepted": 1.1698248518891567
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5866997241973877,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0944733489990235,
                "rejected_mean_error": 2.1783091247558595,
                "gap_rejected_minus_accepted": 1.083835775756836
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0442330539226532,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.754711843336733,
                "rejected_mean_error": 1.9309116746343695,
                "gap_rejected_minus_accepted": 1.1761998312976365
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.603066921234131,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5145636761188508,
                "rejected_mean_error": 2.9564493083953858,
                "gap_rejected_minus_accepted": 1.441885632276535
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.060900032520294,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3604687294539284,
                "rejected_mean_error": 2.5441334512498646,
                "gap_rejected_minus_accepted": 1.1836647217959362
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5981804728507996,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1134805271625519,
                "rejected_mean_error": 2.2040239515304565,
                "gap_rejected_minus_accepted": 1.0905434243679046
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.081191211938858,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7643285029464297,
                "rejected_mean_error": 1.9600821612352994,
                "gap_rejected_minus_accepted": 1.1957536582888697
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9843204387678495,
            "spearman": 0.9822468560014972,
            "auroc_top30_bad": 0.9953249523809524,
            "mae": 0.08708084447826041,
            "mse": 0.020595064969872855,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7082927328201459,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.090824521869421
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2040598655819893
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5738200980603695
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9567412766416867
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
            "pearson": 0.9806868595914744,
            "spearman": 0.9890011009118104,
            "auroc_top30_worst": 0.9925851428571429,
            "pairwise_seed_ranking": 0.9328,
            "predicted_best_mean_error": 1.7425017523765565,
            "seed0_mean_error": 1.8436008858680726,
            "random_seed_mean_error": 1.808576955795288,
            "oracle_best_mean_error": 1.7398507182598113,
            "improvement_over_seed0": 0.10109913349151611,
            "gap_to_oracle": 0.0026510341167451656,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8768055233955383
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1817388116167142
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4348400080680848
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.606767953522424
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8114040771961213
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4652183771133425,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7177460168732537,
                "rejected_mean_error": 2.6543266201019287,
                "gap_rejected_minus_accepted": 0.936580603228675
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0801591277122498,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6063800536835589,
                "rejected_mean_error": 2.425166090075581,
                "gap_rejected_minus_accepted": 0.8187860363920223
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.811529517173767,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4348400080680848,
                "rejected_mean_error": 2.187968146324158,
                "gap_rejected_minus_accepted": 0.753128138256073
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.477989286184311,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1831216048508788,
                "rejected_mean_error": 2.0212785850339663,
                "gap_rejected_minus_accepted": 0.8381569801830875
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.593466854095459,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7404456885655721,
                "rejected_mean_error": 2.7719976615905764,
                "gap_rejected_minus_accepted": 1.0315519730250042
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.131540596485138,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6185779016923139,
                "rejected_mean_error": 2.5115262515961176,
                "gap_rejected_minus_accepted": 0.8929483499038038
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8268260955810547,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4421957035064696,
                "rejected_mean_error": 2.2450060682296753,
                "gap_rejected_minus_accepted": 0.8028103647232057
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5026942789554596,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1897771226035223,
                "rejected_mean_error": 2.0638730627967714,
                "gap_rejected_minus_accepted": 0.8740959401932491
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2000,
            "pearson": 0.9895836249315132,
            "spearman": 0.9822939535490968,
            "auroc_top30_bad": 0.9851809523809524,
            "mae": 0.09624114262815874,
            "mse": 0.01684270868900871,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7261500593737236,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08618003683164716
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.17122962851077317
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6618435769118368
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0508861668929457
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
            "pearson": 0.9767649758336703,
            "spearman": 0.9706404106404108,
            "auroc_top30_worst": 0.9857095238095237,
            "pairwise_seed_ranking": 0.915,
            "predicted_best_mean_error": 1.865003071129322,
            "seed0_mean_error": 1.9262300634384155,
            "random_seed_mean_error": 1.9081436988711358,
            "oracle_best_mean_error": 1.863301387131214,
            "improvement_over_seed0": 0.061226992309093564,
            "gap_to_oracle": 0.0017016839981078835,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.2767283749580383
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.4473005900382996
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.6383671078681945
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7597145719528198
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.9147616970539092
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3332833290100097,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.8423467270533245,
                "rejected_mean_error": 2.5664964270591737,
                "gap_rejected_minus_accepted": 0.7241497000058492
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0231688618659973,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.7597145719528198,
                "rejected_mean_error": 2.3799030723571777,
                "gap_rejected_minus_accepted": 0.6201885004043579
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.836923897266388,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.6383671078681945,
                "rejected_mean_error": 2.191156286239624,
                "gap_rejected_minus_accepted": 0.5527891783714294
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5964060425758362,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 1.4473005900382996,
                "rejected_mean_error": 2.0705820660591128,
                "gap_rejected_minus_accepted": 0.6232814760208132
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3831915140151976,
                "accepted_n": 180,
                "rejected_n": 20,
                "accepted_mean_error": 1.8536654935942756,
                "rejected_mean_error": 2.579311192035675,
                "gap_rejected_minus_accepted": 0.7256456984413995
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.058746576309204,
                "accepted_n": 150,
                "rejected_n": 50,
                "accepted_mean_error": 1.7676084740956624,
                "rejected_mean_error": 2.402094831466675,
                "gap_rejected_minus_accepted": 0.6344863573710127
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8628309965133667,
                "accepted_n": 100,
                "rejected_n": 100,
                "accepted_mean_error": 1.6459057331085205,
                "rejected_mean_error": 2.2065543937683105,
                "gap_rejected_minus_accepted": 0.56064866065979
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.605071246623993,
                "accepted_n": 50,
                "rejected_n": 150,
                "accepted_mean_error": 1.4596882939338685,
                "rejected_mean_error": 2.081743986606598,
                "gap_rejected_minus_accepted": 0.6220556926727296
              }
            ]
          }
        }
      }
    }
  ]
}
```
