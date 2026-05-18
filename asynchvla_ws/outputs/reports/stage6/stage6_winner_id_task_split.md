# Stage 6 Experiments: id_task_split

```json
{
  "split": "id_task_split",
  "results": [
    {
      "variant": "action_only_baseline",
      "feature_mode": "A0_action_flat",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 70,
      "best_epoch": 59,
      "best_calib_loss": 0.07995900511741638,
      "train_time_sec": 14.038421869277954,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.8880763781616289,
            "spearman": 0.8233024849426249,
            "auroc_top30_bad": 0.8923487857142858,
            "mae": 0.2055236773185432,
            "mse": 0.22635168700293243,
            "expert_lt_perturb_large": 0.98,
            "expert_lt_other_task": 0.511,
            "expert_lt_simvla_seed0": 0.952,
            "same_context_pred_std": 0.7906042478168215,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5029864741712808
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.534077775940299
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6895913952872157
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.003433808413148
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9976869203733413,
            "spearman": 0.9968674754265485,
            "auroc_top30_worst": 0.9986158095238096,
            "pairwise_seed_ranking": 0.8376,
            "predicted_best_mean_error": 1.6333604720532895,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.07308987805247291,
            "gap_to_oracle": 0.010213951140642274,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.523840233206749
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7340483886241913
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.012033515048027
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2510503586292268
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.09151520729065,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4533945267068016,
                "rejected_mean_error": 3.9128717074394226,
                "gap_rejected_minus_accepted": 2.459477180732621
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.040269672870636,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2510503586292268,
                "rejected_mean_error": 3.0442179032325747,
                "gap_rejected_minus_accepted": 1.793167544603348
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.518812119960785,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.012033515048027,
                "rejected_mean_error": 2.3866509745121003,
                "gap_rejected_minus_accepted": 1.3746174594640732
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0627015829086304,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7340483886241913,
                "rejected_mean_error": 2.0211068634986877,
                "gap_rejected_minus_accepted": 1.2870584748744964
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0807732343673706,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4560139651430977,
                "rejected_mean_error": 3.960377814769745,
                "gap_rejected_minus_accepted": 2.504363849626647
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.038324773311615,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2501477185090384,
                "rejected_mean_error": 3.075358244895935,
                "gap_rejected_minus_accepted": 1.8252105263868967
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5243072509765625,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0088710905313492,
                "rejected_mean_error": 2.4040296096801756,
                "gap_rejected_minus_accepted": 1.3951585191488265
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0602591633796692,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7229821856021881,
                "rejected_mean_error": 2.034273071606954,
                "gap_rejected_minus_accepted": 1.3112908860047658
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.7156613791677653,
            "spearman": 0.6966782220953875,
            "auroc_top30_bad": 0.8236407619047619,
            "mae": 0.4177190965294838,
            "mse": 0.4168734045941261,
            "expert_lt_perturb_large": 0.948,
            "expert_lt_other_task": 0.508,
            "expert_lt_simvla_seed0": 0.94,
            "same_context_pred_std": 0.7148384357752118,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7077811455726624
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6839590770959854
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8202303595662117
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1118954602718354
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.8435762432203399,
            "spearman": 0.8467062663080105,
            "auroc_top30_worst": 0.9050057142857144,
            "pairwise_seed_ranking": 0.7676,
            "predicted_best_mean_error": 1.6678981424570083,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.06009747731685655,
            "gap_to_oracle": 0.018825887918472173,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.673391292333603
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9764067577436949
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2246941858768463
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4754379339881543
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4814536809921264,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.611160843875673,
                "rejected_mean_error": 2.77619278717041,
                "gap_rejected_minus_accepted": 1.1650319432947371
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1096901893615723,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.473871752222167,
                "rejected_mean_error": 2.487419220205313,
                "gap_rejected_minus_accepted": 1.0135474679831462
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7278523445129395,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2246941858768463,
                "rejected_mean_error": 2.230633890533447,
                "gap_rejected_minus_accepted": 1.0059397046566008
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3395645320415497,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9772974200332507,
                "rejected_mean_error": 1.978320123037381,
                "gap_rejected_minus_accepted": 1.0010227030041303
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5026013135910032,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6049001789093018,
                "rejected_mean_error": 2.8358545875549317,
                "gap_rejected_minus_accepted": 1.2309544086456299
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.144300878047943,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4708644209061077,
                "rejected_mean_error": 2.491226321174985,
                "gap_rejected_minus_accepted": 1.0203619002688773
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7393509149551392,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.219582859992981,
                "rejected_mean_error": 2.2364083795547485,
                "gap_rejected_minus_accepted": 1.0168255195617675
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3315710127353668,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9638631646595304,
                "rejected_mean_error": 1.98543061802094,
                "gap_rejected_minus_accepted": 1.0215674533614096
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.5948654968162301,
            "spearman": 0.5313863691450076,
            "auroc_top30_bad": 0.7190144761904762,
            "mae": 0.5240463355660439,
            "mse": 0.5669241143154007,
            "expert_lt_perturb_large": 0.952,
            "expert_lt_other_task": 0.508,
            "expert_lt_simvla_seed0": 0.912,
            "same_context_pred_std": 0.6909240101053192,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.597134923696518
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7258196958303451
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.8746786076664924
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0175211535374324
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.7329838354583067,
            "spearman": 0.6346275948484488,
            "auroc_top30_worst": 0.8656822857142856,
            "pairwise_seed_ranking": 0.7164,
            "predicted_best_mean_error": 1.4247454595565796,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.057313749194145114,
            "gap_to_oracle": 0.023288943290710407,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.869531662940979
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9763932293997362
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0790684097766876
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1762881766377227
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6521250247955326,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2848382909827762,
                "rejected_mean_error": 3.145446336746216,
                "gap_rejected_minus_accepted": 1.8606080457634397
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.068841576576233,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1753894264313811,
                "rejected_mean_error": 2.3555398622450356,
                "gap_rejected_minus_accepted": 1.1801504358136545
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6015543937683105,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0790684097766876,
                "rejected_mean_error": 1.8627297813415526,
                "gap_rejected_minus_accepted": 0.783661371564865
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1012459099292755,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9772421968059418,
                "rejected_mean_error": 1.6358026273731487,
                "gap_rejected_minus_accepted": 0.6585604305672069
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6721864223480223,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2985288263691797,
                "rejected_mean_error": 3.1338326501846314,
                "gap_rejected_minus_accepted": 1.8353038238154518
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1045788526535034,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.176840860416545,
                "rejected_mean_error": 2.388024782377576,
                "gap_rejected_minus_accepted": 1.2111839219610312
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5940499305725098,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0721423523426057,
                "rejected_mean_error": 1.891976065158844,
                "gap_rejected_minus_accepted": 0.8198337128162383
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.118068516254425,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9775516111699362,
                "rejected_mean_error": 1.6520270090052152,
                "gap_rejected_minus_accepted": 0.674475397835279
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
      "best_epoch": 92,
      "best_calib_loss": 0.12719054520130157,
      "train_time_sec": 17.27740979194641,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.4745567640690398,
            "spearman": 0.41525130687844225,
            "auroc_top30_bad": 0.7525765238095238,
            "mae": 0.6062879776366055,
            "mse": 0.8286822149355081,
            "expert_lt_perturb_large": 0.5,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.5005,
            "same_context_pred_std": 5.462855929083633e-11,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7852767637595535
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8773262435466052
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0266736132964491
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1654150742878517
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9433226587096272,
            "spearman": 0.9896211065983275,
            "auroc_top30_worst": 0.9934723809523809,
            "pairwise_seed_ranking": 0.5001,
            "predicted_best_mean_error": 1.706448216855526,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 2.1332502364579398e-06,
            "gap_to_oracle": 0.08330169594287873,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5268648408055305
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7379590289592743
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0156697516202926
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2534298669974009
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6173952817916875,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.459251386973593,
                "rejected_mean_error": 3.8601599650382994,
                "gap_rejected_minus_accepted": 2.4009085780647066
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9524342715740204,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2534298669974009,
                "rejected_mean_error": 3.037079378128052,
                "gap_rejected_minus_accepted": 1.783649511130651
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4688377976417542,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0156697516202926,
                "rejected_mean_error": 2.3830147379398348,
                "gap_rejected_minus_accepted": 1.3673449863195422
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0220049023628235,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7379590289592743,
                "rejected_mean_error": 2.019803316720327,
                "gap_rejected_minus_accepted": 1.2818442877610525
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.617395281791687,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4615024289157657,
                "rejected_mean_error": 3.9109816408157347,
                "gap_rejected_minus_accepted": 2.449479211899969
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9524342715740204,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2532101177374522,
                "rejected_mean_error": 3.0661710472106933,
                "gap_rejected_minus_accepted": 1.8129609294732412
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4688377976417542,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0134078592061997,
                "rejected_mean_error": 2.3994928410053253,
                "gap_rejected_minus_accepted": 1.3860849817991256
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0220049023628235,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7272157430648803,
                "rejected_mean_error": 2.0328618857860565,
                "gap_rejected_minus_accepted": 1.305646142721176
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.3945455868597907,
            "spearman": 0.41133248889965723,
            "auroc_top30_bad": 0.7778209523809525,
            "mae": 0.6200629204809666,
            "mse": 0.6892870304412055,
            "expert_lt_perturb_large": 0.5,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.5,
            "same_context_pred_std": 0.0,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7979318807721139
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9558806789398193
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0765707785844802
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.219330137570699
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.8455909567817885,
            "spearman": 0.8640273564130869,
            "auroc_top30_worst": 0.9436800000000001,
            "pairwise_seed_ranking": 0.5,
            "predicted_best_mean_error": 1.7279956197738648,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.0,
            "gap_to_oracle": 0.07892336523532872,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.674226968050003
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.018838007767231
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.19561639046669
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.45115815477966
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.215467643737793,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6289412646028731,
                "rejected_mean_error": 2.6161690006256104,
                "gap_rejected_minus_accepted": 0.9872277360227373
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8968656063079834,
                "accepted_n": 940,
                "rejected_n": 310,
                "accepted_mean_error": 1.4511589663142854,
                "rejected_mean_error": 2.5660987723258235,
                "gap_rejected_minus_accepted": 1.114939806011538
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5252670049667358,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.19561639046669,
                "rejected_mean_error": 2.2597116859436035,
                "gap_rejected_minus_accepted": 1.0640952954769134
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2119752168655396,
                "accepted_n": 315,
                "rejected_n": 935,
                "accepted_mean_error": 1.0233649097737811,
                "rejected_mean_error": 1.964941284682024,
                "gap_rejected_minus_accepted": 0.9415763749082429
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.215467643737793,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6267253875732421,
                "rejected_mean_error": 2.6394277095794676,
                "gap_rejected_minus_accepted": 1.0127023220062255
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8959807455539703,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4420318265649723,
                "rejected_mean_error": 2.5768087837431164,
                "gap_rejected_minus_accepted": 1.134776957178144
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5252670049667358,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.179003430366516,
                "rejected_mean_error": 2.2769878091812132,
                "gap_rejected_minus_accepted": 1.0979843788146972
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2144046127796173,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9983800696948218,
                "rejected_mean_error": 1.9738019280892642,
                "gap_rejected_minus_accepted": 0.9754218583944424
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.3595880473159753,
            "spearman": 0.3092333152326011,
            "auroc_top30_bad": 0.7005379047619049,
            "mae": 0.6144567244946957,
            "mse": 0.6656083941104897,
            "expert_lt_perturb_large": 0.498,
            "expert_lt_other_task": 0.5,
            "expert_lt_simvla_seed0": 0.5,
            "same_context_pred_std": 1.430511474609375e-10,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8828704640865326
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.95502632791996
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0361926328539848
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0819920457919439
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.8186030502383137,
            "spearman": 0.8320499665202599,
            "auroc_top30_worst": 0.9258514285714287,
            "pairwise_seed_ranking": 0.5,
            "predicted_best_mean_error": 1.4820592087507247,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.0,
            "gap_to_oracle": 0.08060269248485552,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6388989989757538
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8309649692322963
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0333143747806548
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1275594960461293
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0109969139099144,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2869341519938575,
                "rejected_mean_error": 3.1265835876464845,
                "gap_rejected_minus_accepted": 1.839649435652627
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6997476816177368,
                "accepted_n": 940,
                "rejected_n": 310,
                "accepted_mean_error": 1.1294293488910858,
                "rejected_mean_error": 2.5063234886815473,
                "gap_rejected_minus_accepted": 1.3768941397904615
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3219881653785706,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0333143747806548,
                "rejected_mean_error": 1.9084838163375855,
                "gap_rejected_minus_accepted": 0.8751694415569307
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0816899538040161,
                "accepted_n": 315,
                "rejected_n": 935,
                "accepted_mean_error": 0.8326297484693073,
                "rejected_mean_error": 1.6859310146321587,
                "gap_rejected_minus_accepted": 0.8533012661628514
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.010996913909912,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2977276859018538,
                "rejected_mean_error": 3.141042914390564,
                "gap_rejected_minus_accepted": 1.84331522848871
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6991252601146698,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1297765943137081,
                "rejected_mean_error": 2.527723477000282,
                "gap_rejected_minus_accepted": 1.3979468826865737
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3219881653785706,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0373663265705109,
                "rejected_mean_error": 1.9267520909309388,
                "gap_rejected_minus_accepted": 0.8893857643604279
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0868065059185028,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8315533763832517,
                "rejected_mean_error": 1.701213580083082,
                "gap_rejected_minus_accepted": 0.8696602036998304
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
      "best_epoch": 95,
      "best_calib_loss": 0.0396035835146904,
      "train_time_sec": 17.85653018951416,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9981333838946105,
            "spearman": 0.9962700194488934,
            "auroc_top30_bad": 0.9988293809523809,
            "mae": 0.058240341808646914,
            "mse": 0.005707824301196271,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7900438116902349,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05614794596284628
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1869496274203062
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5936035344704985
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9741379238039255
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.99943402569315,
            "spearman": 0.9990379190654703,
            "auroc_top30_worst": 0.9993533333333334,
            "pairwise_seed_ranking": 0.9272,
            "predicted_best_mean_error": 1.6251388945281506,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08131145557761177,
            "gap_to_oracle": 0.0019923736155034177,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.516669069647789
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7319884321689606
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0110139793634414
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2504923304080964
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.043218469619751,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530939987632963,
                "rejected_mean_error": 3.9155764589309694,
                "gap_rejected_minus_accepted": 2.4624824601676734
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9512358605861664,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2504923304080964,
                "rejected_mean_error": 3.0458919878959656,
                "gap_rejected_minus_accepted": 1.7953996574878692
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4717227816581726,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0110139793634414,
                "rejected_mean_error": 2.3876705101966857,
                "gap_rejected_minus_accepted": 1.3766565308332444
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0458664894104004,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7319884321689606,
                "rejected_mean_error": 2.0217935156504314,
                "gap_rejected_minus_accepted": 1.289805083481471
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.0698333978652963,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4557022731171714,
                "rejected_mean_error": 3.9631830430030823,
                "gap_rejected_minus_accepted": 2.5074807698859107
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9460681676864624,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2494452146689097,
                "rejected_mean_error": 3.077465756416321,
                "gap_rejected_minus_accepted": 1.8280205417474111
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.470384955406189,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0080058027505874,
                "rejected_mean_error": 2.4048948974609377,
                "gap_rejected_minus_accepted": 1.3968890947103503
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0572718679904938,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7209875824451446,
                "rejected_mean_error": 2.0349379393259683,
                "gap_rejected_minus_accepted": 1.3139503568808237
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.919102121374509,
            "spearman": 0.9275788902096942,
            "auroc_top30_bad": 0.9595070476190475,
            "mae": 0.25121468672454356,
            "mse": 0.13446599646645327,
            "expert_lt_perturb_large": 0.992,
            "expert_lt_other_task": 0.968,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6060366307100077,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11790200501680374
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.29724438025951383
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6763317008852958
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0387202570517857
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9567794251593225,
            "spearman": 0.9541873206958853,
            "auroc_top30_worst": 0.993048380952381,
            "pairwise_seed_ranking": 0.8316,
            "predicted_best_mean_error": 1.6619375344514846,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.06605808532238022,
            "gap_to_oracle": 0.012865279912948502,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6719748358726502
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.912281583994627
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1816627180576325
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4161470248056118
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5172096490859985,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5893235468599531,
                "rejected_mean_error": 2.9727284603118895,
                "gap_rejected_minus_accepted": 1.3834049134519364
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1887989044189453,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4153963610164129,
                "rejected_mean_error": 2.6624717491503342,
                "gap_rejected_minus_accepted": 1.2470753881339214
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7873701453208923,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1816627180576325,
                "rejected_mean_error": 2.273665358352661,
                "gap_rejected_minus_accepted": 1.0920026402950287
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4460041224956512,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.912542782366847,
                "rejected_mean_error": 1.999951074573757,
                "gap_rejected_minus_accepted": 1.08740829220691
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5184071779251096,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.58653795560201,
                "rejected_mean_error": 3.001114597320557,
                "gap_rejected_minus_accepted": 1.4145766417185468
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.20622181892395,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4057974930115562,
                "rejected_mean_error": 2.684361488100082,
                "gap_rejected_minus_accepted": 1.278563995088526
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7794975638389587,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1656314878463745,
                "rejected_mean_error": 2.290359751701355,
                "gap_rejected_minus_accepted": 1.1247282638549805
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4582138061523438,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8970964333367726,
                "rejected_mean_error": 2.007924222691174,
                "gap_rejected_minus_accepted": 1.1108277893544014
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9354725996128442,
            "spearman": 0.917717652769476,
            "auroc_top30_bad": 0.9635759999999999,
            "mae": 0.22109952933639287,
            "mse": 0.0981372478280721,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.944,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6113735466532059,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11462244504690171
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2621053195476532
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6336797467708588
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9065150124311447
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.95124500635686,
            "spearman": 0.853106395332093,
            "auroc_top30_worst": 0.9925638095238095,
            "pairwise_seed_ranking": 0.8052,
            "predicted_best_mean_error": 1.417284241914749,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.06477496683597561,
            "gap_to_oracle": 0.01582772564887991,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6674274127483368
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8766844498996551
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.001599199438095
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1192133625242502
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.551742148399355,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2639896647400326,
                "rejected_mean_error": 3.333083972930908,
                "gap_rejected_minus_accepted": 2.0690943081908753
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8613656163215637,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1184973685247794,
                "rejected_mean_error": 2.525852508438281,
                "gap_rejected_minus_accepted": 1.4073551399135014
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4281039834022522,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.001599199438095,
                "rejected_mean_error": 1.9401989916801452,
                "gap_rejected_minus_accepted": 0.9385997922420501
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.159205436706543,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8778869832476107,
                "rejected_mean_error": 1.6689917221903927,
                "gap_rejected_minus_accepted": 0.791104738942782
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.555870413780212,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2739171005619896,
                "rejected_mean_error": 3.3553381824493407,
                "gap_rejected_minus_accepted": 2.081421081887351
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8797807693481445,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1221881746289564,
                "rejected_mean_error": 2.550247833842323,
                "gap_rejected_minus_accepted": 1.4280596592133665
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4464332461357117,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.99347460770607,
                "rejected_mean_error": 1.9706438097953796,
                "gap_rejected_minus_accepted": 0.9771692020893096
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.162960410118103,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.893929290866095,
                "rejected_mean_error": 1.6801992345621242,
                "gap_rejected_minus_accepted": 0.7862699436960292
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
      "best_epoch": 85,
      "best_calib_loss": 0.008704558946192265,
      "train_time_sec": 42.13012385368347,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997671384029105,
            "spearman": 0.9989489509703013,
            "auroc_top30_bad": 0.9997377619047619,
            "mae": 0.01791509231524542,
            "mse": 0.0005181290911018842,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8076535484378228,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00036276847869157793
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18629695763289927
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5934233591422439
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9736670843193929
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9998291085843263,
            "spearman": 0.9996939981877379,
            "auroc_top30_worst": 0.9999104761904761,
            "pairwise_seed_ranking": 0.9543,
            "predicted_best_mean_error": 1.6244461695849894,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08200418052077296,
            "gap_to_oracle": 0.001299648672342224,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5153749177455902
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7315447937488556
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0107524020433425
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2502547181924184
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.1761515140533447,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530428185065587,
                "rejected_mean_error": 3.916037081241608,
                "gap_rejected_minus_accepted": 2.462994262735049
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.017004430294037,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2502547181924184,
                "rejected_mean_error": 3.046604824542999,
                "gap_rejected_minus_accepted": 1.7963501063505807
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.516300916671753,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0107524020433425,
                "rejected_mean_error": 2.3879320875167847,
                "gap_rejected_minus_accepted": 1.3771796854734422
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0757119953632355,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7315447937488556,
                "rejected_mean_error": 2.0219413951237994,
                "gap_rejected_minus_accepted": 1.290396601374944
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.24649121761322,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4556599781910577,
                "rejected_mean_error": 3.9635636973381043,
                "gap_rejected_minus_accepted": 2.5079037191470466
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0185930132865906,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2494587520758311,
                "rejected_mean_error": 3.0774251441955567,
                "gap_rejected_minus_accepted": 1.8279663921197256
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.512335181236267,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0076083320379257,
                "rejected_mean_error": 2.4052923681735994,
                "gap_rejected_minus_accepted": 1.3976840361356737
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0852646827697754,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7209322793483735,
                "rejected_mean_error": 2.034956373691559,
                "gap_rejected_minus_accepted": 1.3140240943431853
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9881106878302547,
            "spearman": 0.9877307680880005,
            "auroc_top30_bad": 0.9939314285714286,
            "mae": 0.09296253021024167,
            "mse": 0.018823415713344425,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.972,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7345455222550341,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07471192574501037
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2040215149641037
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6424750812411308
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0261664516369502
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9840082026615484,
            "spearman": 0.9883866897834817,
            "auroc_top30_worst": 0.9948312380952382,
            "pairwise_seed_ranking": 0.8912,
            "predicted_best_mean_error": 1.6558340276479722,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07216159212589268,
            "gap_to_oracle": 0.006761773109436042,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.64134131026268
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8636397594251694
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1509770519733429
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4124921183151478
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6697041034698494,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5945944963296255,
                "rejected_mean_error": 2.925289915084839,
                "gap_rejected_minus_accepted": 1.3306954187552134
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1654670238494873,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4115709593418186,
                "rejected_mean_error": 2.6739235107129375,
                "gap_rejected_minus_accepted": 1.262352551371119
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6541801691055298,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1509770519733429,
                "rejected_mean_error": 2.3043510244369507,
                "gap_rejected_minus_accepted": 1.1533739724636078
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1818489134311676,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8644481669790067,
                "rejected_mean_error": 2.016016831901819,
                "gap_rejected_minus_accepted": 1.1515686649228123
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7047395229339597,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5940273337894015,
                "rejected_mean_error": 2.9337101936340333,
                "gap_rejected_minus_accepted": 1.3396828598446318
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.156789004802704,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4038814733372653,
                "rejected_mean_error": 2.690048721101549,
                "gap_rejected_minus_accepted": 1.2861672477642838
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6612354516983032,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1387074699401856,
                "rejected_mean_error": 2.317283769607544,
                "gap_rejected_minus_accepted": 1.1785762996673586
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1955620050430298,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8568840121466016,
                "rejected_mean_error": 2.021471722878237,
                "gap_rejected_minus_accepted": 1.1645877107316354
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9806641034940874,
            "spearman": 0.981356813514633,
            "auroc_top30_bad": 0.9954963809523809,
            "mae": 0.10716363364364952,
            "mse": 0.028471791739663514,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7099976525560896,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06251287472248078
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.247198885846138
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5662841534256935
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8897314898252487
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9818983750763788,
            "spearman": 0.9820031372820079,
            "auroc_top30_worst": 0.9981927619047619,
            "pairwise_seed_ranking": 0.8932,
            "predicted_best_mean_error": 1.40938512134552,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07267408740520476,
            "gap_to_oracle": 0.007928605079650763,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6340212624073028
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7894552639470651
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9406492720127105
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1147409330870806
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5454649209976195,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2639896647400326,
                "rejected_mean_error": 3.333083972930908,
                "gap_rejected_minus_accepted": 2.0690943081908753
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8500980138778687,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1140161770830286,
                "rejected_mean_error": 2.539267448952404,
                "gap_rejected_minus_accepted": 1.4252512718693753
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2622175216674805,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9406492720127105,
                "rejected_mean_error": 2.0011489191055296,
                "gap_rejected_minus_accepted": 1.060499647092819
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9191554188728333,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7899515614532434,
                "rejected_mean_error": 1.6983660946787993,
                "gap_rejected_minus_accepted": 0.9084145332255559
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5500531673431395,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.2739171005619896,
                "rejected_mean_error": 3.3553381824493407,
                "gap_rejected_minus_accepted": 2.081421081887351
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8875010907649994,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.118359643348398,
                "rejected_mean_error": 2.5616118870084246,
                "gap_rejected_minus_accepted": 1.4432522436600266
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2626129984855652,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.939013504743576,
                "rejected_mean_error": 2.0251049127578735,
                "gap_rejected_minus_accepted": 1.0860914080142976
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.9172378033399582,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7861301459017254,
                "rejected_mean_error": 1.7165165935608155,
                "gap_rejected_minus_accepted": 0.9303864476590902
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
      "best_calib_loss": 0.011610961519181728,
      "train_time_sec": 46.026206493377686,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997861920450302,
            "spearman": 0.9989122177287256,
            "auroc_top30_bad": 0.9998160476190476,
            "mae": 0.01605599354568386,
            "mse": 0.00046521676711600663,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8048374225637415,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0010518485829234124
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1862153424948454
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5933850518330932
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9736314021815856
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3900039018683135
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9998465828134002,
            "spearman": 0.9997048789721598,
            "auroc_top30_worst": 0.9997424761904762,
            "pairwise_seed_ranking": 0.9493,
            "predicted_best_mean_error": 1.6247383030951024,
            "seed0_mean_error": 1.7064503501057624,
            "random_seed_mean_error": 1.7013063016831875,
            "oracle_best_mean_error": 1.6231465209126472,
            "improvement_over_seed0": 0.08171204701066004,
            "gap_to_oracle": 0.0015917821824551481,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5151366485357285
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7316162534236907
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0107340880155564
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.250266405948003
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6993422447800637
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.161591386795044,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4530233759482702,
                "rejected_mean_error": 3.916212064266205,
                "gap_rejected_minus_accepted": 2.463188688317935
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.007182538509369,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.250266405948003,
                "rejected_mean_error": 3.046569761276245,
                "gap_rejected_minus_accepted": 1.796303355328242
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5093658566474915,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0107340880155564,
                "rejected_mean_error": 2.387950401544571,
                "gap_rejected_minus_accepted": 1.3772163135290145
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0782191455364227,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7316162534236907,
                "rejected_mean_error": 2.021917575232188,
                "gap_rejected_minus_accepted": 1.290301321808497
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.219655656814576,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.455667041738828,
                "rejected_mean_error": 3.9635001254081725,
                "gap_rejected_minus_accepted": 2.5078330836693445
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0114440321922302,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.249549975156784,
                "rejected_mean_error": 3.077151474952698,
                "gap_rejected_minus_accepted": 1.8276014997959138
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.508176326751709,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0076350976228714,
                "rejected_mean_error": 2.4052656025886536,
                "gap_rejected_minus_accepted": 1.3976305049657822
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0934145152568817,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7208234369754791,
                "rejected_mean_error": 2.0349926544825236,
                "gap_rejected_minus_accepted": 1.3141692175070445
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9842416464836222,
            "spearman": 0.9847991983200844,
            "auroc_top30_bad": 0.9922841904761904,
            "mae": 0.11122542342316469,
            "mse": 0.026168387936572366,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7131847012639371,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08890826272964478
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21164581820964815
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6412396459460259
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0273037934541702
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3786586558759213
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9822521499790914,
            "spearman": 0.9882775661296425,
            "auroc_top30_worst": 0.9956662857142857,
            "pairwise_seed_ranking": 0.89,
            "predicted_best_mean_error": 1.6536583777666092,
            "seed0_mean_error": 1.7279956197738648,
            "random_seed_mean_error": 1.7318815352916717,
            "oracle_best_mean_error": 1.6490722545385361,
            "improvement_over_seed0": 0.07433724200725567,
            "gap_to_oracle": 0.004586123228073058,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6549943611621857
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8620221657821765
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1519636627674104
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4130021635212624
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7276640382051467
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6169167757034306,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5934099236859216,
                "rejected_mean_error": 2.935951068878174,
                "gap_rejected_minus_accepted": 1.3425411451922524
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1135213971138,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4118661701424782,
                "rejected_mean_error": 2.673039764641954,
                "gap_rejected_minus_accepted": 1.2611735944994757
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6640011072158813,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1519636627674104,
                "rejected_mean_error": 2.3033644136428832,
                "gap_rejected_minus_accepted": 1.151400750875473
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1474206745624542,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8629842540517021,
                "rejected_mean_error": 2.0165058444378343,
                "gap_rejected_minus_accepted": 1.1535215903861322
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.652246046066284,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5940066570705838,
                "rejected_mean_error": 2.9338962841033935,
                "gap_rejected_minus_accepted": 1.3398896270328098
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1307180523872375,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4057186784591267,
                "rejected_mean_error": 2.684595429708087,
                "gap_rejected_minus_accepted": 1.2788767512489605
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6844271421432495,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.139200855255127,
                "rejected_mean_error": 2.3167903842926028,
                "gap_rejected_minus_accepted": 1.1775895290374758
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1774860322475433,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8539014638416351,
                "rejected_mean_error": 2.0224765386173433,
                "gap_rejected_minus_accepted": 1.1685750747757082
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9729482421567216,
            "spearman": 0.9698702048669353,
            "auroc_top30_bad": 0.9927497142857142,
            "mae": 0.14888352325596757,
            "mse": 0.04645085058094342,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6386598083527883,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07652842849493027
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2567265676736832
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.572300618994236
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8930185315529505
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2518879841387272
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9739427371779783,
            "spearman": 0.9487853834146455,
            "auroc_top30_worst": 0.9887299047619047,
            "pairwise_seed_ranking": 0.8968,
            "predicted_best_mean_error": 1.4093893489837646,
            "seed0_mean_error": 1.4820592087507247,
            "random_seed_mean_error": 1.4711955163478851,
            "oracle_best_mean_error": 1.4014565162658692,
            "improvement_over_seed0": 0.07266985976696017,
            "gap_to_oracle": 0.007932832717895355,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.671731730222702
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8062769314990594
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9579678675174713
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1179965038352937
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.4708990955591201
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2883743524551394,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.264079571644465,
                "rejected_mean_error": 3.3322748107910156,
                "gap_rejected_minus_accepted": 2.068195239146551
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6480055749416351,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.1173454654445771,
                "rejected_mean_error": 2.5293008572758198,
                "gap_rejected_minus_accepted": 1.4119553918312426
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2306227684020996,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 0.9579678675174713,
                "rejected_mean_error": 1.983830323600769,
                "gap_rejected_minus_accepted": 1.0258624560832978
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8785841763019562,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8075378477192534,
                "rejected_mean_error": 1.6924914867799081,
                "gap_rejected_minus_accepted": 0.8849536390606547
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2733171224594115,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.273069721725252,
                "rejected_mean_error": 3.3629645919799804,
                "gap_rejected_minus_accepted": 2.0898948702547284
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6773742735385895,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.1214395167037128,
                "rejected_mean_error": 2.5524700406997924,
                "gap_rejected_minus_accepted": 1.4310305239960797
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.2320325374603271,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 0.9578241374492645,
                "rejected_mean_error": 2.006294280052185,
                "gap_rejected_minus_accepted": 1.0484701426029206
              },
              {
                "reject_rate": 0.75,
                "threshold": 0.8683809787034988,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8093954244303325,
                "rejected_mean_error": 1.708678558548504,
                "gap_rejected_minus_accepted": 0.8992831341181715
              }
            ]
          }
        }
      }
    }
  ]
}
```
