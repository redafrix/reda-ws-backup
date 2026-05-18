# Stage 7 Multi-Expert Target Experiments: holdout_object_cabinet

```json
{
  "split": "holdout_object_cabinet",
  "by_target": {
    "target_chunk_l2_single_expert": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 41,
        "best_calib_loss": 0.06107345595955849,
        "train_time_sec": 11.150570154190063,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9655441698114771,
              "spearman": 0.9334536318463175,
              "auroc_top30_bad": 0.9986404523809523,
              "mae": 0.11846725728698075,
              "mse": 0.0446335307020609,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.963,
              "same_context_pred_std": 0.6664347394986557,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2911870816759765
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3111160518750548
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4463604797028005
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7573265863354007
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.108668715305254
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9968695530647188,
              "spearman": 0.9970583700421937,
              "auroc_top30_worst": 0.9978281904761904,
              "pairwise_seed_ranking": 0.8375,
              "predicted_best_mean_error": 1.460084577381611,
              "seed0_mean_error": 1.5254779134392737,
              "random_seed_mean_error": 1.5131405942738057,
              "oracle_best_mean_error": 1.4502590649425984,
              "improvement_over_seed0": 0.06539333605766284,
              "gap_to_oracle": 0.00982551243901253,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4982525430321693
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7059345484972
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9823939564347267
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.210574580804507
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5126614425718785
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3256874084472665,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3525095074507925,
                  "rejected_mean_error": 2.9540288586616517,
                  "gap_rejected_minus_accepted": 1.6015193512108592
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9116221070289612,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.210574580804507,
                  "rejected_mean_error": 2.418922027873993,
                  "gap_rejected_minus_accepted": 1.2083474470694862
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5049695372581482,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9823939564347267,
                  "rejected_mean_error": 2.04292892870903,
                  "gap_rejected_minus_accepted": 1.0605349722743034
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0452298820018768,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7059345484972,
                  "rejected_mean_error": 1.781570407263438,
                  "gap_rejected_minus_accepted": 1.0756358587662378
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.353176355361939,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3647398610247505,
                  "rejected_mean_error": 2.972120385169983,
                  "gap_rejected_minus_accepted": 1.6073805241452324
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9270905256271362,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.22123308634758,
                  "rejected_mean_error": 2.4382123947143555,
                  "gap_rejected_minus_accepted": 1.2169793083667755
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.519704818725586,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9887538908720016,
                  "rejected_mean_error": 2.062201936006546,
                  "gap_rejected_minus_accepted": 1.0734480451345445
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0752839148044586,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7082896716594697,
                  "rejected_mean_error": 1.7978739940325419,
                  "gap_rejected_minus_accepted": 1.0895843223730721
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8747227122629142,
              "spearman": 0.8314993579534454,
              "auroc_top30_bad": 0.9454041904761905,
              "mae": 0.34022592426538467,
              "mse": 0.21758780544439632,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 0.932,
              "same_context_pred_std": 0.610530006608184,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.41277903094887736
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.40039843641519546
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5859358720898629
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8876018331925074
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2122082696199417
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8729611699261945,
              "spearman": 0.7600808305157317,
              "auroc_top30_worst": 0.8479786666666668,
              "pairwise_seed_ranking": 0.6608,
              "predicted_best_mean_error": 1.654412266254425,
              "seed0_mean_error": 1.6927297905683518,
              "random_seed_mean_error": 1.6863511270284652,
              "oracle_best_mean_error": 1.6256710990667342,
              "improvement_over_seed0": 0.038317524313926876,
              "gap_to_oracle": 0.028741167187690708,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7045520210266113
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.031621739650384
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.239104712677002
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.40991235402093
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6859890789031982
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.949047350883484,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5273563441170586,
                  "rejected_mean_error": 3.1136836919784545,
                  "gap_rejected_minus_accepted": 1.586327347861396
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5958857536315918,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4095150262848926,
                  "rejected_mean_error": 2.513644629393142,
                  "gap_rejected_minus_accepted": 1.1041296031082493
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2892042398452759,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.239104712677002,
                  "rejected_mean_error": 2.1328734451293947,
                  "gap_rejected_minus_accepted": 0.8937687324523926
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9675138592720032,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0302262730872669,
                  "rejected_mean_error": 1.90504324989614,
                  "gap_rejected_minus_accepted": 0.8748169768088732
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9429510116577147,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.53695007469919,
                  "rejected_mean_error": 3.094747233390808,
                  "gap_rejected_minus_accepted": 1.557797158691618
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6157678961753845,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4081313053873135,
                  "rejected_mean_error": 2.5374903735660372,
                  "gap_rejected_minus_accepted": 1.1293590681787238
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3177752494812012,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.228458563566208,
                  "rejected_mean_error": 2.1570010175704954,
                  "gap_rejected_minus_accepted": 0.9285424540042875
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9899748712778091,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9572196049349648,
                  "rejected_mean_error": 1.9405219921453751,
                  "gap_rejected_minus_accepted": 0.9833023872104103
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8336527854836429,
              "spearman": 0.8328014002189461,
              "auroc_top30_bad": 0.9148575238095238,
              "mae": 0.38015527199804783,
              "mse": 0.3644449356983948,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.476,
              "expert_lt_simvla_seed0": 0.964,
              "same_context_pred_std": 0.6517770523639057,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.36839896988868714
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3810174337387085
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6114409655630588
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9529974901556969
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.339590658262372
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7044148530907344,
              "spearman": 0.6691800711552457,
              "auroc_top30_worst": 0.7593874285714286,
              "pairwise_seed_ranking": 0.7344,
              "predicted_best_mean_error": 1.9221783316135406,
              "seed0_mean_error": 1.9813467921018602,
              "random_seed_mean_error": 1.9611121064424515,
              "oracle_best_mean_error": 1.892046400785446,
              "improvement_over_seed0": 0.059168460488319585,
              "gap_to_oracle": 0.03013193082809451,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.264563093662262
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.329804295530686
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4990928312301637
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5866370853076357
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.958894820690155
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.409396529197693,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7718678282631768,
                  "rejected_mean_error": 3.642137752532959,
                  "gap_rejected_minus_accepted": 1.8702699242697822
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9265816807746887,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.58630792651894,
                  "rejected_mean_error": 3.0742747562761887,
                  "gap_rejected_minus_accepted": 1.4879668297572488
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5758128762245178,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4990928312301637,
                  "rejected_mean_error": 2.4186968101501467,
                  "gap_rejected_minus_accepted": 0.919603978919983
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2528428137302399,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.329066815086828,
                  "rejected_mean_error": 2.169285605913038,
                  "gap_rejected_minus_accepted": 0.84021879082621
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4417333364486695,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7898228675789303,
                  "rejected_mean_error": 3.7050621128082275,
                  "gap_rejected_minus_accepted": 1.9152392452292972
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9294098019599915,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5964305966614403,
                  "rejected_mean_error": 3.1238758166631064,
                  "gap_rejected_minus_accepted": 1.5274452200016662
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.605391502380371,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.496508411169052,
                  "rejected_mean_error": 2.4661851730346678,
                  "gap_rejected_minus_accepted": 0.9696767618656157
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2625126540660858,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.329749831604579,
                  "rejected_mean_error": 2.2008687627506767,
                  "gap_rejected_minus_accepted": 0.8711189311460976
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8957882261990774,
              "spearman": 0.8649316559133606,
              "auroc_top30_bad": 0.945768380952381,
              "mae": 0.2717883900254965,
              "mse": 0.15070777510194683,
              "expert_lt_perturb_large": 0.992,
              "expert_lt_other_task": 0.508,
              "expert_lt_simvla_seed0": 0.932,
              "same_context_pred_std": 0.695157885688956,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3517208230495453
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3590213034391403
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5321327986717224
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8989762903054556
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8925167185217422,
              "spearman": 0.8478752367841517,
              "auroc_top30_worst": 0.8941866666666667,
              "pairwise_seed_ranking": 0.7184,
              "predicted_best_mean_error": 1.6851827749013901,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.021407319784164436,
              "gap_to_oracle": 0.023333838939666895,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6984916665554046
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9931033694018156
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2757589273929595
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4706706927338642
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6011404037475594,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5632387244171566,
                  "rejected_mean_error": 3.120531632423401,
                  "gap_rejected_minus_accepted": 1.5572929080062443
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9720543324947357,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4698535152089762,
                  "rejected_mean_error": 2.4647197293016476,
                  "gap_rejected_minus_accepted": 0.9948662140926714
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6284267902374268,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2757589273929595,
                  "rejected_mean_error": 2.1621771030426027,
                  "gap_rejected_minus_accepted": 0.8864181756496432
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2410044372081757,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9936817325532626,
                  "rejected_mean_error": 1.9612461437919477,
                  "gap_rejected_minus_accepted": 0.9675644112386851
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5118813514709473,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.550790280368593,
                  "rejected_mean_error": 3.108788423538208,
                  "gap_rejected_minus_accepted": 1.5579981431696153
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9448287189006805,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4599143644386434,
                  "rejected_mean_error": 2.438786309862894,
                  "gap_rejected_minus_accepted": 0.9788719454242505
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6377081274986267,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2612094023227691,
                  "rejected_mean_error": 2.1519707870483398,
                  "gap_rejected_minus_accepted": 0.8907613847255706
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2190446853637695,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9745284493953462,
                  "rejected_mean_error": 1.9532204885533786,
                  "gap_rejected_minus_accepted": 0.9786920391580324
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
        "best_epoch": 69,
        "best_calib_loss": 0.00602965010330081,
        "train_time_sec": 35.74726414680481,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9993902093949596,
              "spearman": 0.998506849897153,
              "auroc_top30_bad": 0.9999424761904763,
              "mae": 0.014672690004622563,
              "mse": 0.000842341305413735,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6799628058118258,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0013575539328157902
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16598914880007506
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4373610896252096
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7566042778268457
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.108668715305254
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9995124073641565,
              "spearman": 0.9992687108746957,
              "auroc_top30_worst": 0.9998154285714286,
              "pairwise_seed_ranking": 0.9579,
              "predicted_best_mean_error": 1.4510605703890325,
              "seed0_mean_error": 1.5254779134392737,
              "random_seed_mean_error": 1.5131405942738057,
              "oracle_best_mean_error": 1.4502590649425984,
              "improvement_over_seed0": 0.07441734305024128,
              "gap_to_oracle": 0.000801505446434092,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4949932110905647
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7045413004636765
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9822589476943016
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.209967329541842
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5126614425718785
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.319807267189026,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.352005375021034,
                  "rejected_mean_error": 2.95856605052948,
                  "gap_rejected_minus_accepted": 1.606560675508446
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8776686787605286,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.209967329541842,
                  "rejected_mean_error": 2.4207437816619874,
                  "gap_rejected_minus_accepted": 1.2107764521201454
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.482354462146759,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9822589476943016,
                  "rejected_mean_error": 2.0430639374494555,
                  "gap_rejected_minus_accepted": 1.060804989755154
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0310012102127075,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7045413004636765,
                  "rejected_mean_error": 1.7820348232746124,
                  "gap_rejected_minus_accepted": 1.077493522810936
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.370732808113098,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3641424635383819,
                  "rejected_mean_error": 2.9774969625473022,
                  "gap_rejected_minus_accepted": 1.6133544990089204
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8910337388515472,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.22112633395195,
                  "rejected_mean_error": 2.438532651901245,
                  "gap_rejected_minus_accepted": 1.2174063179492949
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4913585186004639,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9892242842912674,
                  "rejected_mean_error": 2.0617315425872804,
                  "gap_rejected_minus_accepted": 1.072507258296013
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0457215905189514,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7068721859455108,
                  "rejected_mean_error": 1.798346489270528,
                  "gap_rejected_minus_accepted": 1.0914743033250174
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9920767943513338,
              "spearman": 0.9890897223589531,
              "auroc_top30_bad": 0.9959649523809524,
              "mae": 0.07548345658648759,
              "mse": 0.013003694614667827,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.968,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.712315947253903,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06529925087094307
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17498614132404328
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4936032104969025
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8529061056454976
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2122082696199417
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9895794040561574,
              "spearman": 0.9918720664781228,
              "auroc_top30_worst": 0.9931184761904762,
              "pairwise_seed_ranking": 0.9056,
              "predicted_best_mean_error": 1.6291015750169755,
              "seed0_mean_error": 1.6927297905683518,
              "random_seed_mean_error": 1.6863511270284652,
              "oracle_best_mean_error": 1.6256710990667342,
              "improvement_over_seed0": 0.06362821555137632,
              "gap_to_oracle": 0.003430475950241263,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5213642015457153
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8287956095658816
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.148484449195862
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3724141964780243
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6859890789031982
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.364485859870911,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.49973386976454,
                  "rejected_mean_error": 3.362285961151123,
                  "gap_rejected_minus_accepted": 1.8625520913865832
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9159742593765259,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3717768244453274,
                  "rejected_mean_error": 2.626618096241936,
                  "gap_rejected_minus_accepted": 1.2548412717966084
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6359920501708984,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.148484449195862,
                  "rejected_mean_error": 2.2234937086105346,
                  "gap_rejected_minus_accepted": 1.0750092594146727
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2632327675819397,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.829880054004657,
                  "rejected_mean_error": 1.97196786736984,
                  "gap_rejected_minus_accepted": 1.1420878133651828
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3644858598709106,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5075401209460364,
                  "rejected_mean_error": 3.3594368171691893,
                  "gap_rejected_minus_accepted": 1.851896696223153
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9333317875862122,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.375802266884615,
                  "rejected_mean_error": 2.6334511703915067,
                  "gap_rejected_minus_accepted": 1.2576489035068916
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6353932619094849,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.146499217748642,
                  "rejected_mean_error": 2.2389603633880615,
                  "gap_rejected_minus_accepted": 1.0924611456394195
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2910215258598328,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8258805629752931,
                  "rejected_mean_error": 1.9847699046772431,
                  "gap_rejected_minus_accepted": 1.1588893417019501
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9739894426421802,
              "spearman": 0.9836987467690445,
              "auroc_top30_bad": 0.9914087619047619,
              "mae": 0.14160761891566218,
              "mse": 0.07369682274304265,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7488383408590287,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.06761345580220222
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17640654410123824
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5106332279741764
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9050934835155805
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.339590658262372
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.957502257168163,
              "spearman": 0.9912757663204906,
              "auroc_top30_worst": 0.9949074285714286,
              "pairwise_seed_ranking": 0.9176,
              "predicted_best_mean_error": 1.8935185712575913,
              "seed0_mean_error": 1.9813467921018602,
              "random_seed_mean_error": 1.9611121064424515,
              "oracle_best_mean_error": 1.892046400785446,
              "improvement_over_seed0": 0.08782822084426889,
              "gap_to_oracle": 0.0014721704721452067,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6500728101730346
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9857045943156267
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3006803939819336
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.525566545757912
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.958894820690155
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8903083086013797,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7559517558415731,
                  "rejected_mean_error": 3.7853824043273927,
                  "gap_rejected_minus_accepted": 2.0294306484858193
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.192691445350647,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5249606113932557,
                  "rejected_mean_error": 3.257924706029435,
                  "gap_rejected_minus_accepted": 1.7329640946361793
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8198292255401611,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3006803939819336,
                  "rejected_mean_error": 2.6171092473983766,
                  "gap_rejected_minus_accepted": 1.316428853416443
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4549764096736908,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9867006532681255,
                  "rejected_mean_error": 2.283651250149168,
                  "gap_rejected_minus_accepted": 1.2969505968810424
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.905450391769409,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7708185523086124,
                  "rejected_mean_error": 3.876100950241089,
                  "gap_rejected_minus_accepted": 2.1052823979324766
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1948379278182983,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5415915038815156,
                  "rejected_mean_error": 3.2866521714225647,
                  "gap_rejected_minus_accepted": 1.7450606675410492
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.843245506286621,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3137580506801605,
                  "rejected_mean_error": 2.6489355335235594,
                  "gap_rejected_minus_accepted": 1.3351774828433989
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4784134924411774,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.994089241538729,
                  "rejected_mean_error": 2.3139522770509364,
                  "gap_rejected_minus_accepted": 1.3198630355122074
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9893708936039505,
              "spearman": 0.9877123858199055,
              "auroc_top30_bad": 0.9896304761904762,
              "mae": 0.08598678721245379,
              "mse": 0.017686554175189974,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.968,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7569582033990475,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.026790398478507997
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18027839548587798
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5004127078652382
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8643923000733058
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9755916343408472,
              "spearman": 0.9737676222512783,
              "auroc_top30_worst": 0.9636358095238096,
              "pairwise_seed_ranking": 0.9228,
              "predicted_best_mean_error": 1.6658804377317429,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.04070965695381168,
              "gap_to_oracle": 0.004031501770019652,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6295122301578522
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9507159186670413
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2237420486927033
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4280862583598095
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5917467594146766,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.558882494105233,
                  "rejected_mean_error": 3.1597377052307127,
                  "gap_rejected_minus_accepted": 1.6008552111254797
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.021910607814789,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.427471209901883,
                  "rejected_mean_error": 2.5915958317704857,
                  "gap_rejected_minus_accepted": 1.1641246218686028
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7159706354141235,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2237420486927033,
                  "rejected_mean_error": 2.214193981742859,
                  "gap_rejected_minus_accepted": 0.9904519330501556
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3565047085285187,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9522253443448307,
                  "rejected_mean_error": 1.9750944356908158,
                  "gap_rejected_minus_accepted": 1.022869091345985
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5479414224624635,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5499693193700579,
                  "rejected_mean_error": 3.1161770725250246,
                  "gap_rejected_minus_accepted": 1.5662077531549667
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0029337406158447,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4167511216140687,
                  "rejected_mean_error": 2.5669057766596475,
                  "gap_rejected_minus_accepted": 1.1501546550455788
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7040278911590576,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2120357296466828,
                  "rejected_mean_error": 2.2011444597244263,
                  "gap_rejected_minus_accepted": 0.9891087300777435
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3568540811538696,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9284738306961362,
                  "rejected_mean_error": 1.9687362157087276,
                  "gap_rejected_minus_accepted": 1.0402623850125914
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
        "best_epoch": 46,
        "best_calib_loss": 0.008553095161914825,
        "train_time_sec": 41.715940713882446,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.999178248875359,
              "spearman": 0.9979509305585895,
              "auroc_top30_bad": 0.9994179047619048,
              "mae": 0.026227717427871538,
              "mse": 0.0012178235056548826,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6852324561767357,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0034400227479636667
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16626664499491453
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.43716600091680885
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7567866850470503
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.108668715305254
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9991690126850663,
              "spearman": 0.9987439277176667,
              "auroc_top30_worst": 0.9995464761904762,
              "pairwise_seed_ranking": 0.9605,
              "predicted_best_mean_error": 1.4510396426916123,
              "seed0_mean_error": 1.5254779134392737,
              "random_seed_mean_error": 1.5131405942738057,
              "oracle_best_mean_error": 1.4502590649425984,
              "improvement_over_seed0": 0.0744382707476614,
              "gap_to_oracle": 0.0007805777490139665,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.49540258783102037
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7047414143323898
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.981696534216404
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2102099817991256
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5126614425718785
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.344938182830812,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3520982105003463,
                  "rejected_mean_error": 2.9577305312156676,
                  "gap_rejected_minus_accepted": 1.6056323207153214
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8987208306789398,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2102099817991256,
                  "rejected_mean_error": 2.420015824890137,
                  "gap_rejected_minus_accepted": 1.2098058430910112
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4889215230941772,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.981696534216404,
                  "rejected_mean_error": 2.043626350927353,
                  "gap_rejected_minus_accepted": 1.0619298167109492
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0368508994579315,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7047414143323898,
                  "rejected_mean_error": 1.781968118651708,
                  "gap_rejected_minus_accepted": 1.0772267043193182
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3886669158935545,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3642047596640057,
                  "rejected_mean_error": 2.976936297416687,
                  "gap_rejected_minus_accepted": 1.6127315377526814
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9091793298721313,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2212447216510773,
                  "rejected_mean_error": 2.4381774888038636,
                  "gap_rejected_minus_accepted": 1.2169327671527863
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.504731297492981,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9886550022363663,
                  "rejected_mean_error": 2.0623008246421812,
                  "gap_rejected_minus_accepted": 1.073645822405815
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0505863726139069,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7073411734104157,
                  "rejected_mean_error": 1.7981901601155599,
                  "gap_rejected_minus_accepted": 1.090848986705144
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9889502328701636,
              "spearman": 0.9810924429518392,
              "auroc_top30_bad": 0.9940906666666667,
              "mae": 0.09496951386689616,
              "mse": 0.018145964691286237,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7017675406598975,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.08627534431219101
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19781573133468627
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4951916018009186
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8532738638877868
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2122082696199417
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9919640194258106,
              "spearman": 0.9850254818493075,
              "auroc_top30_worst": 0.9886232380952381,
              "pairwise_seed_ranking": 0.8852,
              "predicted_best_mean_error": 1.6292429193258287,
              "seed0_mean_error": 1.6927297905683518,
              "random_seed_mean_error": 1.6863511270284652,
              "oracle_best_mean_error": 1.6256710990667342,
              "improvement_over_seed0": 0.06348687124252317,
              "gap_to_oracle": 0.003571820259094416,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5225369887351989
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8343104364780279
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1514852947235108
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.373083687286133
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6859890789031982
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.403466439247132,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4986022078196208,
                  "rejected_mean_error": 3.3724709186553956,
                  "gap_rejected_minus_accepted": 1.8738687108357748
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9206097424030304,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3726234492013905,
                  "rejected_mean_error": 2.624083631716597,
                  "gap_rejected_minus_accepted": 1.2514601825152065
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6049792766571045,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1514852947235108,
                  "rejected_mean_error": 2.2204928630828857,
                  "gap_rejected_minus_accepted": 1.069007568359375
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1590561270713806,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8353203950217738,
                  "rejected_mean_error": 1.9701505496127882,
                  "gap_rejected_minus_accepted": 1.1348301545910144
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3991612672805784,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5051499376032087,
                  "rejected_mean_error": 3.3809484672546386,
                  "gap_rejected_minus_accepted": 1.87579852965143
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9383893609046936,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3766225517433595,
                  "rejected_mean_error": 2.63101635660444,
                  "gap_rejected_minus_accepted": 1.2543938048610805
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6104711294174194,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.149655657529831,
                  "rejected_mean_error": 2.2358039236068725,
                  "gap_rejected_minus_accepted": 1.0861482660770416
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1789390444755554,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8322734809111035,
                  "rejected_mean_error": 1.9826161408806866,
                  "gap_rejected_minus_accepted": 1.1503426599695832
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9764577290765588,
              "spearman": 0.9748232030262584,
              "auroc_top30_bad": 0.9911512380952381,
              "mae": 0.1455855048813748,
              "mse": 0.05969910418784068,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7499669253471539,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09970624271035194
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19508494185209274
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5116244468271732
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9043306569139162
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.339590658262372
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9751900386743075,
              "spearman": 0.9902860164390507,
              "auroc_top30_worst": 0.9980007619047618,
              "pairwise_seed_ranking": 0.9128,
              "predicted_best_mean_error": 1.8936692630052567,
              "seed0_mean_error": 1.9813467921018602,
              "random_seed_mean_error": 1.9611121064424515,
              "oracle_best_mean_error": 1.892046400785446,
              "improvement_over_seed0": 0.08767752909660342,
              "gap_to_oracle": 0.0016228622198106724,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6519065399169922
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9819811678085572
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3041553518295288
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5233138554385985
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.958894820690155
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.0503508329391495,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7396052408218383,
                  "rejected_mean_error": 3.932501039505005,
                  "gap_rejected_minus_accepted": 2.1928957986831668
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.280968487262726,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5225180298439849,
                  "rejected_mean_error": 3.265236843127412,
                  "gap_rejected_minus_accepted": 1.7427188132834273
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8292299509048462,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3041553518295288,
                  "rejected_mean_error": 2.6136342895507814,
                  "gap_rejected_minus_accepted": 1.3094789377212526
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3539444506168365,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9833134340402037,
                  "rejected_mean_error": 2.2847827331996906,
                  "gap_rejected_minus_accepted": 1.301469299159487
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.138592004776001,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.758899153470993,
                  "rejected_mean_error": 3.9833755397796633,
                  "gap_rejected_minus_accepted": 2.2244763863086705
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3716883063316345,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5403320418003408,
                  "rejected_mean_error": 3.290390574742877,
                  "gap_rejected_minus_accepted": 1.7500585329425364
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8653064370155334,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3170936152935029,
                  "rejected_mean_error": 2.645599968910217,
                  "gap_rejected_minus_accepted": 1.3285063536167143
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.394177258014679,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9897650513384078,
                  "rejected_mean_error": 2.315409089792221,
                  "gap_rejected_minus_accepted": 1.3256440384538133
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9878851157699392,
              "spearman": 0.9841508587814248,
              "auroc_top30_bad": 0.9916601904761905,
              "mae": 0.09462975759031396,
              "mse": 0.017844350429460667,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7356025733366545,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09764212989807129
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18833961260318757
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.501995425760746
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8624197508255641
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9830801141155164,
              "spearman": 0.9750330413011465,
              "auroc_top30_worst": 0.9720716190476191,
              "pairwise_seed_ranking": 0.9212,
              "predicted_best_mean_error": 1.66351500916481,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.04307508552074446,
              "gap_to_oracle": 0.0016660732030868708,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6295322353839874
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9561875184568075
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2238688677310943
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4255089888504064
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.488709902763369,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5594402202235327,
                  "rejected_mean_error": 3.1547181701660154,
                  "gap_rejected_minus_accepted": 1.5952779499424827
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9609858095645905,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4251113568006228,
                  "rejected_mean_error": 2.5986603121407117,
                  "gap_rejected_minus_accepted": 1.1735489553400889
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6491799354553223,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2238688677310943,
                  "rejected_mean_error": 2.2140671627044677,
                  "gap_rejected_minus_accepted": 0.9901982949733734
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3145310282707214,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9569262042403602,
                  "rejected_mean_error": 1.9735241377748063,
                  "gap_rejected_minus_accepted": 1.0165979335344462
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4397711038589476,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5499383069409265,
                  "rejected_mean_error": 3.116456184387207,
                  "gap_rejected_minus_accepted": 1.5665178774462807
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9307336807250977,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.414888372555136,
                  "rejected_mean_error": 2.5724348889456854,
                  "gap_rejected_minus_accepted": 1.1575465163905494
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6444621682167053,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2121625196933747,
                  "rejected_mean_error": 2.2010176696777344,
                  "gap_rejected_minus_accepted": 0.9888551499843596
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.306675523519516,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9350845345429012,
                  "rejected_mean_error": 1.9665090801881597,
                  "gap_rejected_minus_accepted": 1.0314245456452587
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
        "best_epoch": 69,
        "best_calib_loss": 0.007193773053586483,
        "train_time_sec": 29.274470329284668,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9994627727217064,
              "spearman": 0.998482255947859,
              "auroc_top30_bad": 0.9997358095238095,
              "mae": 0.023723357173471685,
              "mse": 0.0010666569181604086,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6914566006090497,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.001830370008945465
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.16615360919684172
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4370690615795553
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7566705855146051
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.108668715305254
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9994634414365309,
              "spearman": 0.9992398246655383,
              "auroc_top30_worst": 0.9996247619047619,
              "pairwise_seed_ranking": 0.9602,
              "predicted_best_mean_error": 1.4508195583224297,
              "seed0_mean_error": 1.5254779134392737,
              "random_seed_mean_error": 1.5131405942738057,
              "oracle_best_mean_error": 1.4502590649425984,
              "improvement_over_seed0": 0.07465835511684404,
              "gap_to_oracle": 0.0005604933798313283,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.49519911938905714
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7048939823389053
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.981642017185688
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.210040677968661
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5126614425718785
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3362403869628907,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3520952534741826,
                  "rejected_mean_error": 2.9577571444511412,
                  "gap_rejected_minus_accepted": 1.6056618909769587
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9094562530517578,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.210040677968661,
                  "rejected_mean_error": 2.4205237363815306,
                  "gap_rejected_minus_accepted": 1.2104830584128696
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.504689633846283,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.981642017185688,
                  "rejected_mean_error": 2.0436808679580687,
                  "gap_rejected_minus_accepted": 1.0620388507723808
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0370937585830688,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7048939823389053,
                  "rejected_mean_error": 1.781917262649536,
                  "gap_rejected_minus_accepted": 1.0770232803106308
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.366582751274109,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3641605330175823,
                  "rejected_mean_error": 2.977334337234497,
                  "gap_rejected_minus_accepted": 1.6131738042169148
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9379757940769196,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2211036072572072,
                  "rejected_mean_error": 2.4386008319854735,
                  "gap_rejected_minus_accepted": 1.2174972247282663
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5147823691368103,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9886076678037643,
                  "rejected_mean_error": 2.062348159074783,
                  "gap_rejected_minus_accepted": 1.073740491271019
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0563485026359558,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7069693987369537,
                  "rejected_mean_error": 1.7983140850067139,
                  "gap_rejected_minus_accepted": 1.09134468626976
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9904664417254029,
              "spearman": 0.985122015028092,
              "auroc_top30_bad": 0.9943260952380952,
              "mae": 0.08902731083001736,
              "mse": 0.015169025543425233,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7091254007348757,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05076154989004135
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18494177205562592
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4959655601024628
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8531023632367452
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2122082696199417
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9902076596064142,
              "spearman": 0.9828055441955483,
              "auroc_top30_worst": 0.9872396190476191,
              "pairwise_seed_ranking": 0.9268,
              "predicted_best_mean_error": 1.6270681248903274,
              "seed0_mean_error": 1.6927297905683518,
              "random_seed_mean_error": 1.6863511270284652,
              "oracle_best_mean_error": 1.6256710990667342,
              "improvement_over_seed0": 0.06566166567802445,
              "gap_to_oracle": 0.0013970258235931343,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.523640027999878
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8391744796282206
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1533276788711548
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3742865304957066
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6859890789031982
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.37904748916626,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4988424294789633,
                  "rejected_mean_error": 3.3703089237213133,
                  "gap_rejected_minus_accepted": 1.87146649424235
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9533239901065826,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3736736422032914,
                  "rejected_mean_error": 2.6209397632093094,
                  "gap_rejected_minus_accepted": 1.247266121006018
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6153098344802856,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1533276788711548,
                  "rejected_mean_error": 2.218650478935242,
                  "gap_rejected_minus_accepted": 1.065322800064087
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1851199567317963,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8407624586702536,
                  "rejected_mean_error": 1.9683326564196462,
                  "gap_rejected_minus_accepted": 1.1275701977493926
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3810227394104,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5060743786229027,
                  "rejected_mean_error": 3.3726284980773924,
                  "gap_rejected_minus_accepted": 1.8665541194544897
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.962188333272934,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3794229774870337,
                  "rejected_mean_error": 2.6227039817779785,
                  "gap_rejected_minus_accepted": 1.2432810042909448
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6328417658805847,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1515657613277435,
                  "rejected_mean_error": 2.23389381980896,
                  "gap_rejected_minus_accepted": 1.0823280584812165
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1755059957504272,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8414527948886629,
                  "rejected_mean_error": 1.979523644727819,
                  "gap_rejected_minus_accepted": 1.1380708498391563
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9703184678992276,
              "spearman": 0.977471504233299,
              "auroc_top30_bad": 0.9903207619047619,
              "mae": 0.14769430524027644,
              "mse": 0.07211050450229076,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7626146071949627,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07877533510327339
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1840027372956276
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5138888661921024
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9054634865164757
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.339590658262372
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9633379613205765,
              "spearman": 0.9888444042352837,
              "auroc_top30_worst": 0.9965500952380952,
              "pairwise_seed_ranking": 0.9268,
              "predicted_best_mean_error": 1.8930916365385055,
              "seed0_mean_error": 1.9813467921018602,
              "random_seed_mean_error": 1.9611121064424515,
              "oracle_best_mean_error": 1.892046400785446,
              "improvement_over_seed0": 0.08825515556335461,
              "gap_to_oracle": 0.0010452357530594814,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6555566115379333
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.982701865144265
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3049652807235719
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5236426704982196
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.958894820690155
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9328073501586918,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7409849384095935,
                  "rejected_mean_error": 3.92008376121521,
                  "gap_rejected_minus_accepted": 2.1790988228056163
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.312181293964386,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.522818684069044,
                  "rejected_mean_error": 3.264336801565493,
                  "gap_rejected_minus_accepted": 1.7415181174964491
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.870387077331543,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3049652807235719,
                  "rejected_mean_error": 2.612824360656738,
                  "gap_rejected_minus_accepted": 1.3078590799331662
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4167017340660095,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9840743678827255,
                  "rejected_mean_error": 2.2845285471882613,
                  "gap_rejected_minus_accepted": 1.3004541793055358
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9666051626205445,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7591472476058536,
                  "rejected_mean_error": 3.981142692565918,
                  "gap_rejected_minus_accepted": 2.2219954449600645
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.37595272064209,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5410935277926092,
                  "rejected_mean_error": 3.2881302909245567,
                  "gap_rejected_minus_accepted": 1.7470367631319474
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8884127736091614,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3199588220119476,
                  "rejected_mean_error": 2.6427347621917723,
                  "gap_rejected_minus_accepted": 1.3227759401798247
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4348128736019135,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9908966010525113,
                  "rejected_mean_error": 2.31502787250886,
                  "gap_rejected_minus_accepted": 1.3241312714563487
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9895198255728959,
              "spearman": 0.9872157624574858,
              "auroc_top30_bad": 0.9910346666666666,
              "mae": 0.08772091851561341,
              "mse": 0.015543574281392906,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7374429937233756,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04489074337482452
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1839532152891159
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5018247160553932
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.86072478120327
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9796683728775752,
              "spearman": 0.9744723517903053,
              "auroc_top30_worst": 0.9759512380952381,
              "pairwise_seed_ranking": 0.9108,
              "predicted_best_mean_error": 1.6638276340961455,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.042762460589409024,
              "gap_to_oracle": 0.0019786981344223076,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6326845095157624
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9559593537870126
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2222055082798005
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.427846589099878
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.479163646697998,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.559591796371672,
                  "rejected_mean_error": 3.153353984832764,
                  "gap_rejected_minus_accepted": 1.593762188461092
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0027076601982117,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4272961779681443,
                  "rejected_mean_error": 2.5921198091567894,
                  "gap_rejected_minus_accepted": 1.164823631188645
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6876301765441895,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2222055082798005,
                  "rejected_mean_error": 2.215730522155762,
                  "gap_rejected_minus_accepted": 0.9935250138759615
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3195410370826721,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9572366096150761,
                  "rejected_mean_error": 1.97342044846607,
                  "gap_rejected_minus_accepted": 1.0161838388509938
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4418595790863034,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5504927371607886,
                  "rejected_mean_error": 3.111466312408447,
                  "gap_rejected_minus_accepted": 1.5609735752476586
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.969581812620163,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.418116564578551,
                  "rejected_mean_error": 2.562852795161898,
                  "gap_rejected_minus_accepted": 1.144736230583347
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7053776383399963,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2096183531284332,
                  "rejected_mean_error": 2.2035618362426757,
                  "gap_rejected_minus_accepted": 0.9939434831142424
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3176631927490234,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9323594991176848,
                  "rejected_mean_error": 1.9674271402512005,
                  "gap_rejected_minus_accepted": 1.0350676411335158
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
        "best_epoch": 5,
        "best_calib_loss": 0.05957847833633423,
        "train_time_sec": 10.740931510925293,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9576840435535938,
              "spearman": 0.9065497862861288,
              "auroc_top30_bad": 0.9922492142857143,
              "mae": 0.16253074463318334,
              "mse": 0.05449107533210986,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.486,
              "expert_lt_simvla_seed0": 0.982,
              "same_context_pred_std": 0.6409412981386019,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.32748299187328667
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.34686756225707943
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.437884266763716
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7400826391635928
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.090024156752124
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9866832700941981,
              "spearman": 0.9811671163986846,
              "auroc_top30_worst": 0.989575238095238,
              "pairwise_seed_ranking": 0.7146,
              "predicted_best_mean_error": 1.451751834332943,
              "seed0_mean_error": 1.501893677175045,
              "random_seed_mean_error": 1.490140748888254,
              "oracle_best_mean_error": 1.428934212654829,
              "improvement_over_seed0": 0.0501418428421021,
              "gap_to_oracle": 0.022817621678113964,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.48252060264348984
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6832317237854004
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9608033079624176
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1851613127072653
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4895446684122085
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.328577899932862,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3283286680645412,
                  "rejected_mean_error": 2.940488671541214,
                  "gap_rejected_minus_accepted": 1.6121600034766728
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8811067938804626,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1851613127072653,
                  "rejected_mean_error": 2.4026947355270387,
                  "gap_rejected_minus_accepted": 1.2175334228197734
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4369944334030151,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9608033079624176,
                  "rejected_mean_error": 2.0182860288619997,
                  "gap_rejected_minus_accepted": 1.057482720899582
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9767145663499832,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6832317237854004,
                  "rejected_mean_error": 1.7583156499544779,
                  "gap_rejected_minus_accepted": 1.0750839261690774
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.380087685585022,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3394944465822645,
                  "rejected_mean_error": 2.9634867525100708,
                  "gap_rejected_minus_accepted": 1.6239923059278063
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9008372724056244,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1958918494383495,
                  "rejected_mean_error": 2.419899160385132,
                  "gap_rejected_minus_accepted": 1.2240073109467824
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4794620871543884,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9665919064283371,
                  "rejected_mean_error": 2.037195447921753,
                  "gap_rejected_minus_accepted": 1.070603541493416
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0273437201976776,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6840862953662872,
                  "rejected_mean_error": 1.7744961377779642,
                  "gap_rejected_minus_accepted": 1.090409842411677
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8818062657568069,
              "spearman": 0.8347570878260986,
              "auroc_top30_bad": 0.9451748571428572,
              "mae": 0.33795971113443374,
              "mse": 0.20189671538961823,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.54,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5939045388404078,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.389707277983427
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3967339246869087
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5816593652009964
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9062548688968023
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2215371421217918
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9059440124554482,
              "spearman": 0.8067226566776264,
              "auroc_top30_worst": 0.8881020952380951,
              "pairwise_seed_ranking": 0.6252,
              "predicted_best_mean_error": 1.678589517235756,
              "seed0_mean_error": 1.7044727271795272,
              "random_seed_mean_error": 1.6981746295690536,
              "oracle_best_mean_error": 1.637618626475334,
              "improvement_over_seed0": 0.025883209943771357,
              "gap_to_oracle": 0.04097089076042182,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8863113903999329
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9783140206948305
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2342978394508362
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4224617701730748
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6977653141498565
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8431177854537968,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5356953477329678,
                  "rejected_mean_error": 3.1563950119018553,
                  "gap_rejected_minus_accepted": 1.6206996641688876
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.529354751110077,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4217906023038744,
                  "rejected_mean_error": 2.5239260329986912,
                  "gap_rejected_minus_accepted": 1.1021354306948168
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3359946012496948,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2342978394508362,
                  "rejected_mean_error": 2.161232788848877,
                  "gap_rejected_minus_accepted": 0.9269349493980408
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.96507728099823,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9788115032183857,
                  "rejected_mean_error": 1.9379281133190671,
                  "gap_rejected_minus_accepted": 0.9591166101006814
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8236960411071776,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5477437404791514,
                  "rejected_mean_error": 3.11503360748291,
                  "gap_rejected_minus_accepted": 1.5672898670037587
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.566730797290802,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4342289817205724,
                  "rejected_mean_error": 2.506624797033885,
                  "gap_rejected_minus_accepted": 1.0723958153133126
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3579867482185364,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.239870983839035,
                  "rejected_mean_error": 2.1690744705200196,
                  "gap_rejected_minus_accepted": 0.9292034866809846
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9898623079061508,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9371610931933873,
                  "rejected_mean_error": 1.9629787856882268,
                  "gap_rejected_minus_accepted": 1.0258176924948397
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8027855859266281,
              "spearman": 0.8378631741820387,
              "auroc_top30_bad": 0.9178544761904762,
              "mae": 0.4226943086743355,
              "mse": 0.45211309382166476,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.488,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.634400851632652,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.37946576964855194
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.38461886465549466
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6730685564756393
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0137688802719116
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.384413278055191
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6233941837204282,
              "spearman": 0.6757217334539095,
              "auroc_top30_worst": 0.7771306666666666,
              "pairwise_seed_ranking": 0.6792,
              "predicted_best_mean_error": 1.9939467381238938,
              "seed0_mean_error": 2.049862780690193,
              "random_seed_mean_error": 2.0296543596982954,
              "oracle_best_mean_error": 1.9612690694332122,
              "improvement_over_seed0": 0.05591604256629923,
              "gap_to_oracle": 0.03267766869068156,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4569593739509583
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4939080897050026
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6276541913986207
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6799376778511097
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.0277799105644227
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4233221054077148,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8544454641342163,
                  "rejected_mean_error": 3.5877899284362793,
                  "gap_rejected_minus_accepted": 1.733344464302063
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9884338080883026,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6798082746589196,
                  "rejected_mean_error": 3.069471357348628,
                  "gap_rejected_minus_accepted": 1.3896630826897085
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5869536399841309,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.6276541913986207,
                  "rejected_mean_error": 2.4279056297302244,
                  "gap_rejected_minus_accepted": 0.8002514383316037
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1816355288028717,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.4941753522275736,
                  "rejected_mean_error": 2.2060277512895388,
                  "gap_rejected_minus_accepted": 0.7118523990619652
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.452855706214905,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8764807183212704,
                  "rejected_mean_error": 3.610301342010498,
                  "gap_rejected_minus_accepted": 1.7338206236892275
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.99120032787323,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6898861219857466,
                  "rejected_mean_error": 3.118364926368471,
                  "gap_rejected_minus_accepted": 1.4284788043827243
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.606545090675354,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6234862167835236,
                  "rejected_mean_error": 2.4762393445968627,
                  "gap_rejected_minus_accepted": 0.8527531278133391
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2304872870445251,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.5049356425565386,
                  "rejected_mean_error": 2.2334478593127614,
                  "gap_rejected_minus_accepted": 0.7285122167562228
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8870105389620426,
              "spearman": 0.8573491403235773,
              "auroc_top30_bad": 0.9352777142857144,
              "mae": 0.32841498221457005,
              "mse": 0.17215920085901354,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.492,
              "expert_lt_simvla_seed0": 0.976,
              "same_context_pred_std": 0.6942004292375193,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3568403136730194
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.38747184467315676
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5581995248556137
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8957118265708287
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8582216118840766,
              "spearman": 0.798473371694958,
              "auroc_top30_worst": 0.8754986666666666,
              "pairwise_seed_ranking": 0.6444,
              "predicted_best_mean_error": 1.6993591538667678,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.007230940818786724,
              "gap_to_oracle": 0.03751021790504461,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7261714260578156
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0193213374377825
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2971996670246124
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4721914584766318
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.889017534255982,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5651137875715893,
                  "rejected_mean_error": 3.1036560640335082,
                  "gap_rejected_minus_accepted": 1.538542276461919
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.025303602218628,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.471001185023543,
                  "rejected_mean_error": 2.461284053211395,
                  "gap_rejected_minus_accepted": 0.9902828681878519
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5578481554985046,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2971996670246124,
                  "rejected_mean_error": 2.1407363634109497,
                  "gap_rejected_minus_accepted": 0.8435366963863373
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9857287406921387,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.021730645110432,
                  "rejected_mean_error": 1.951876549736031,
                  "gap_rejected_minus_accepted": 0.9301459046255991
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7686964750289915,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5576096175776588,
                  "rejected_mean_error": 3.047414388656616,
                  "gap_rejected_minus_accepted": 1.4898047710789573
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9899068474769592,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4588814516437245,
                  "rejected_mean_error": 2.441852257365272,
                  "gap_rejected_minus_accepted": 0.9829708057215476
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5413255095481873,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2811684944629669,
                  "rejected_mean_error": 2.132011694908142,
                  "gap_rejected_minus_accepted": 0.8508432004451751
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0369375944137573,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.001792508931387,
                  "rejected_mean_error": 1.9440352706348194,
                  "gap_rejected_minus_accepted": 0.9422427617034324
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
        "best_epoch": 52,
        "best_calib_loss": 0.007830895483493805,
        "train_time_sec": 35.17217302322388,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995476251109665,
              "spearman": 0.9989801677227729,
              "auroc_top30_bad": 0.9998417142857143,
              "mae": 0.02606237367951544,
              "mse": 0.0010066358383334553,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6742959739897953,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05733501711382996
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1837700984116178
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4194733651933959
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7353739399471475
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.090024156752124
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997028124818887,
              "spearman": 0.9997388067415521,
              "auroc_top30_worst": 0.999752380952381,
              "pairwise_seed_ranking": 0.9412,
              "predicted_best_mean_error": 1.4302200067937374,
              "seed0_mean_error": 1.501893677175045,
              "random_seed_mean_error": 1.490140748888254,
              "oracle_best_mean_error": 1.428934212654829,
              "improvement_over_seed0": 0.07167367038130767,
              "gap_to_oracle": 0.0012857941389083916,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46922957694530487
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.669784662437439
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9499314237594605
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.182826130549113
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4895446684122085
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3465235710144046,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3273187824090322,
                  "rejected_mean_error": 2.949577642440796,
                  "gap_rejected_minus_accepted": 1.6222588600317636
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8918872475624084,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.182826130549113,
                  "rejected_mean_error": 2.4097002820014954,
                  "gap_rejected_minus_accepted": 1.2268741514523824
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.488548457622528,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9499314237594605,
                  "rejected_mean_error": 2.0291579130649566,
                  "gap_rejected_minus_accepted": 1.0792264893054961
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.022963672876358,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.669784662437439,
                  "rejected_mean_error": 1.7627980037371318,
                  "gap_rejected_minus_accepted": 1.093013341299693
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.390411424636841,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3389617365598678,
                  "rejected_mean_error": 2.9682811427116396,
                  "gap_rejected_minus_accepted": 1.6293194061517717
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9002063572406769,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1932503589789072,
                  "rejected_mean_error": 2.427823631763458,
                  "gap_rejected_minus_accepted": 1.2345732727845509
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4936820268630981,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9560524505376816,
                  "rejected_mean_error": 2.0477349038124086,
                  "gap_rejected_minus_accepted": 1.0916824532747271
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.03080153465271,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6709009535312652,
                  "rejected_mean_error": 1.7788912517229716,
                  "gap_rejected_minus_accepted": 1.1079902981917065
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9900370643187422,
              "spearman": 0.9825591571070774,
              "auroc_top30_bad": 0.995767619047619,
              "mae": 0.09297075006067752,
              "mse": 0.01647098048436826,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7088970010464909,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10911523723602295
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2023037896156311
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5062509106397629
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8647326096057892
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2215371421217918
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9916106282548107,
              "spearman": 0.9890821603085826,
              "auroc_top30_worst": 0.9949135238095238,
              "pairwise_seed_ranking": 0.888,
              "predicted_best_mean_error": 1.6403429914712906,
              "seed0_mean_error": 1.7044727271795272,
              "random_seed_mean_error": 1.6981746295690536,
              "oracle_best_mean_error": 1.637618626475334,
              "improvement_over_seed0": 0.06412973570823666,
              "gap_to_oracle": 0.0027243649959565186,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5289007806777954
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8555952912339797
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1743904509544372
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3872490677116776
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6977653141498565
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3436762332916268,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5116592049598694,
                  "rejected_mean_error": 3.3727202968597414,
                  "gap_rejected_minus_accepted": 1.861061091899872
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9174250364303589,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3865887043061353,
                  "rejected_mean_error": 2.629306794736332,
                  "gap_rejected_minus_accepted": 1.2427180904301967
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6427320837974548,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1743904509544372,
                  "rejected_mean_error": 2.221140177345276,
                  "gap_rejected_minus_accepted": 1.0467497263908387
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2604971826076508,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8567733427587028,
                  "rejected_mean_error": 1.9786943291396444,
                  "gap_rejected_minus_accepted": 1.1219209863809416
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.342149090766907,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5181976449489594,
                  "rejected_mean_error": 3.3809484672546386,
                  "gap_rejected_minus_accepted": 1.8627508223056792
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9370089769363403,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.390716417428644,
                  "rejected_mean_error": 2.635781138662308,
                  "gap_rejected_minus_accepted": 1.245064721233664
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6427145600318909,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1729008729457855,
                  "rejected_mean_error": 2.2360445814132692,
                  "gap_rejected_minus_accepted": 1.0631437084674837
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2665968835353851,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.847817868940414,
                  "rejected_mean_error": 1.9930783746076777,
                  "gap_rejected_minus_accepted": 1.1452605056672636
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9662819169197641,
              "spearman": 0.9807090159428608,
              "auroc_top30_bad": 0.9896586666666667,
              "mae": 0.17853100898191332,
              "mse": 0.09341511143624935,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7715966192673052,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09837939846515656
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2124219659805298
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5589064410686493
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9343393056233724
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.384413278055191
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9431509005396984,
              "spearman": 0.9821306376516084,
              "auroc_top30_worst": 0.9974735238095238,
              "pairwise_seed_ranking": 0.892,
              "predicted_best_mean_error": 1.964769205570221,
              "seed0_mean_error": 2.049862780690193,
              "random_seed_mean_error": 2.0296543596982954,
              "oracle_best_mean_error": 1.9612690694332122,
              "improvement_over_seed0": 0.08509357511997195,
              "gap_to_oracle": 0.0035001361370088357,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7207781939506531
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0838302064400454
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.349082519721985
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5556702612559679
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.0277799105644227
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9098419666290285,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8270401764975654,
                  "rejected_mean_error": 3.834437517166138,
                  "gap_rejected_minus_accepted": 2.0073973406685726
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.269511878490448,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5548876368757756,
                  "rejected_mean_error": 3.443435055760149,
                  "gap_rejected_minus_accepted": 1.8885474188843734
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8639829754829407,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.349082519721985,
                  "rejected_mean_error": 2.7064773014068604,
                  "gap_rejected_minus_accepted": 1.3573947816848755
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4743127226829529,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.084991548769771,
                  "rejected_mean_error": 2.342713482860822,
                  "gap_rejected_minus_accepted": 1.2577219340910508
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9255543470382688,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8423859883679283,
                  "rejected_mean_error": 3.9171539115905762,
                  "gap_rejected_minus_accepted": 2.074767923222648
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3004382252693176,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5723671353755788,
                  "rejected_mean_error": 3.4671911247192866,
                  "gap_rejected_minus_accepted": 1.8948239893437078
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9010503888130188,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3605458071231842,
                  "rejected_mean_error": 2.739179754257202,
                  "gap_rejected_minus_accepted": 1.3786339471340179
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.506976455450058,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0890832141278282,
                  "rejected_mean_error": 2.3735478753074606,
                  "gap_rejected_minus_accepted": 1.2844646611796324
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9864392130389782,
              "spearman": 0.9839201840196018,
              "auroc_top30_bad": 0.9874346666666667,
              "mae": 0.10409459051452577,
              "mse": 0.021844940054093105,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7485766265274474,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05677169567346573
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18374565854072572
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5001045199990273
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8659919877767562
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9731545146791698,
              "spearman": 0.9680689603001347,
              "auroc_top30_worst": 0.9571139047619047,
              "pairwise_seed_ranking": 0.9028,
              "predicted_best_mean_error": 1.6637501819133758,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.0428399127721788,
              "gap_to_oracle": 0.0019012459516525304,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6308010013103486
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9520768107703099
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2238520531177521
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4316083325315385
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6075023412704468,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5592579556836021,
                  "rejected_mean_error": 3.1563585510253906,
                  "gap_rejected_minus_accepted": 1.5971005953417885
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.020707130432129,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4307692931644944,
                  "rejected_mean_error": 2.5817226559971087,
                  "gap_rejected_minus_accepted": 1.1509533628326143
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7238249778747559,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2238520531177521,
                  "rejected_mean_error": 2.2140839773178103,
                  "gap_rejected_minus_accepted": 0.9902319242000581
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3360666036605835,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.953532091059243,
                  "rejected_mean_error": 1.97465792371471,
                  "gap_rejected_minus_accepted": 1.0211258326554669
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.52800703048706,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5499693193700579,
                  "rejected_mean_error": 3.1161770725250246,
                  "gap_rejected_minus_accepted": 1.5662077531549667
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0140907764434814,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4207932294052552,
                  "rejected_mean_error": 2.5549077741683477,
                  "gap_rejected_minus_accepted": 1.1341145447630925
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7108479142189026,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2124752247333526,
                  "rejected_mean_error": 2.2007049646377563,
                  "gap_rejected_minus_accepted": 0.9882297399044038
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3249785900115967,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9298581268106189,
                  "rejected_mean_error": 1.9682698485685541,
                  "gap_rejected_minus_accepted": 1.0384117217579352
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
        "best_epoch": 67,
        "best_calib_loss": 0.009627925232052803,
        "train_time_sec": 41.62012076377869,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9989380129015399,
              "spearman": 0.9979221471370502,
              "auroc_top30_bad": 0.9995132857142857,
              "mae": 0.029371254748490172,
              "mse": 0.0014275354805834818,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.998,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6738365756096996,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0588600646693958
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1845687686796766
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.41979063600876837
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7357308492698862
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.090024156752124
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9989891714132281,
              "spearman": 0.9987173578926635,
              "auroc_top30_worst": 0.999243619047619,
              "pairwise_seed_ranking": 0.9578,
              "predicted_best_mean_error": 1.4297780726253986,
              "seed0_mean_error": 1.501893677175045,
              "random_seed_mean_error": 1.490140748888254,
              "oracle_best_mean_error": 1.428934212654829,
              "improvement_over_seed0": 0.0721156045496465,
              "gap_to_oracle": 0.0008438599705695715,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47026687479019164
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6702167203426361
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9503617456912994
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1831031379063923
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4895446684122085
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3068197965621966,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3274626087877486,
                  "rejected_mean_error": 2.9482832050323484,
                  "gap_rejected_minus_accepted": 1.6208205962445998
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8748691380023956,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1831031379063923,
                  "rejected_mean_error": 2.408869259929657,
                  "gap_rejected_minus_accepted": 1.2257661220232647
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4741306900978088,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9503617456912994,
                  "rejected_mean_error": 2.0287275911331175,
                  "gap_rejected_minus_accepted": 1.0783658454418181
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.016074776649475,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6702167203426361,
                  "rejected_mean_error": 1.7626539844353994,
                  "gap_rejected_minus_accepted": 1.0924372640927633
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.349789023399353,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.339062842991617,
                  "rejected_mean_error": 2.9673711848258972,
                  "gap_rejected_minus_accepted": 1.6283083418342803
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8969316482543945,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.193530480782191,
                  "rejected_mean_error": 2.426983266353607,
                  "gap_rejected_minus_accepted": 1.2334527855714161
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4846519231796265,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9563410478830338,
                  "rejected_mean_error": 2.047446306467056,
                  "gap_rejected_minus_accepted": 1.0911052585840224
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.027332067489624,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6714477469921112,
                  "rejected_mean_error": 1.7787089872360229,
                  "gap_rejected_minus_accepted": 1.1072612402439117
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9881966591171867,
              "spearman": 0.9772001499357316,
              "auroc_top30_bad": 0.9935695238095239,
              "mae": 0.10943473586570472,
              "mse": 0.020321690221728795,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.702439281566725,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.14201950615644454
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21578095116615295
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5068023517370224
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8652892466068268
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2215371421217918
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9933301389054147,
              "spearman": 0.9860341383898488,
              "auroc_top30_worst": 0.9927222857142857,
              "pairwise_seed_ranking": 0.9044,
              "predicted_best_mean_error": 1.6409348635673522,
              "seed0_mean_error": 1.7044727271795272,
              "random_seed_mean_error": 1.6981746295690536,
              "oracle_best_mean_error": 1.637618626475334,
              "improvement_over_seed0": 0.06353786361217506,
              "gap_to_oracle": 0.003316237092018115,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5237360606193543
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8549276687777959
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1764219954490662
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3879068863036028
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6977653141498565
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3641973733901978,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.510192168182797,
                  "rejected_mean_error": 3.3859236278533937,
                  "gap_rejected_minus_accepted": 1.8757314596705967
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8974249064922333,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.387222103718887,
                  "rejected_mean_error": 2.6274106437786697,
                  "gap_rejected_minus_accepted": 1.2401885400597827
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6357437372207642,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1764219954490662,
                  "rejected_mean_error": 2.219108632850647,
                  "gap_rejected_minus_accepted": 1.0426866374015806
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2000206410884857,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8560114582887473,
                  "rejected_mean_error": 1.9789488327032474,
                  "gap_rejected_minus_accepted": 1.1229373744145001
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3630316257476807,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5146056306362152,
                  "rejected_mean_error": 3.413276596069336,
                  "gap_rejected_minus_accepted": 1.8986709654331206
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.923562377691269,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3917186284128995,
                  "rejected_mean_error": 2.632806321931264,
                  "gap_rejected_minus_accepted": 1.2410876935183643
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6401053071022034,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.175354816198349,
                  "rejected_mean_error": 2.2335906381607056,
                  "gap_rejected_minus_accepted": 1.0582358219623567
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.22085303068161,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8536095746925899,
                  "rejected_mean_error": 1.9911271582312762,
                  "gap_rejected_minus_accepted": 1.1375175835386862
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.975957190750737,
              "spearman": 0.9779046124563602,
              "auroc_top30_bad": 0.9951634285714286,
              "mae": 0.16827982868626715,
              "mse": 0.07475025037294568,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7652068893666166,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.12668847012519838
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2281160147666931
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5630940422534942
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9324051523844401
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.384413278055191
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9711936827065334,
              "spearman": 0.9855154492898877,
              "auroc_top30_worst": 0.998104380952381,
              "pairwise_seed_ranking": 0.906,
              "predicted_best_mean_error": 1.9640383310317993,
              "seed0_mean_error": 2.049862780690193,
              "random_seed_mean_error": 2.0296543596982954,
              "oracle_best_mean_error": 1.9612690694332122,
              "improvement_over_seed0": 0.08582444965839375,
              "gap_to_oracle": 0.002769261598587036,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7182471785545349
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0813264052073162
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3497553289413453
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5559250272667484
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.0277799105644227
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9764317989349367,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.816565276781718,
                  "rejected_mean_error": 3.9287116146087646,
                  "gap_rejected_minus_accepted": 2.1121463378270464
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.267536997795105,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5550003129364713,
                  "rejected_mean_error": 3.44309774755289,
                  "gap_rejected_minus_accepted": 1.8880974346164188
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7830175757408142,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3497553289413453,
                  "rejected_mean_error": 2.7058044921875,
                  "gap_rejected_minus_accepted": 1.3560491632461549
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.376223623752594,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0822988550503032,
                  "rejected_mean_error": 2.343612963260174,
                  "gap_rejected_minus_accepted": 1.2613141082098709
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.037899541854858,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8347142740090687,
                  "rejected_mean_error": 3.9861993408203125,
                  "gap_rejected_minus_accepted": 2.1514850668112437
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.336015999317169,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5723671353755788,
                  "rejected_mean_error": 3.4671911247192866,
                  "gap_rejected_minus_accepted": 1.8948239893437078
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.831863284111023,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3607988770008088,
                  "rejected_mean_error": 2.7389266843795776,
                  "gap_rejected_minus_accepted": 1.3781278073787688
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4112849831581116,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.086794023002897,
                  "rejected_mean_error": 2.374319100124951,
                  "gap_rejected_minus_accepted": 1.2875250771220539
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9901178050221653,
              "spearman": 0.9866574562684208,
              "auroc_top30_bad": 0.9953219047619047,
              "mae": 0.10306628384613432,
              "mse": 0.017250695213290423,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7142314688860213,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07674496465921402
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19353191306591033
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5014387246727944
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8577509053309759
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9900586046189895,
              "spearman": 0.988206602884226,
              "auroc_top30_worst": 0.9893150476190475,
              "pairwise_seed_ranking": 0.9088,
              "predicted_best_mean_error": 1.6641467862129211,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.042443308472633445,
              "gap_to_oracle": 0.002297850251197886,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6299682395458222
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9504367778889644
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2190211222171783
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4212734840635552
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.398250246047974,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.558841324408849,
                  "rejected_mean_error": 3.160108232498169,
                  "gap_rejected_minus_accepted": 1.6012669080893198
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9142752885818481,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.420660905834196,
                  "rejected_mean_error": 2.6119832276536252,
                  "gap_rejected_minus_accepted": 1.1913223218194293
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6071385145187378,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2190211222171783,
                  "rejected_mean_error": 2.218914908218384,
                  "gap_rejected_minus_accepted": 0.9998937860012056
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2616680562496185,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9515256585594946,
                  "rejected_mean_error": 1.975328162105768,
                  "gap_rejected_minus_accepted": 1.0238025035462734
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3295346975326536,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5504927371607886,
                  "rejected_mean_error": 3.111466312408447,
                  "gap_rejected_minus_accepted": 1.5609735752476586
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.876723736524582,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4081207387906345,
                  "rejected_mean_error": 2.5925229447228566,
                  "gap_rejected_minus_accepted": 1.1844022059322221
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5996559262275696,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2073043406009674,
                  "rejected_mean_error": 2.2058758487701415,
                  "gap_rejected_minus_accepted": 0.9985715081691742
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.244374543428421,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.927021503921539,
                  "rejected_mean_error": 1.9692255022691534,
                  "gap_rejected_minus_accepted": 1.0422039983476143
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
        "best_epoch": 78,
        "best_calib_loss": 0.008388334885239601,
        "train_time_sec": 29.266164541244507,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9994204041076722,
              "spearman": 0.9988502053630803,
              "auroc_top30_bad": 0.9998086190476191,
              "mae": 0.024443359350657556,
              "mse": 0.001008283221363197,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.999,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6856034006096421,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05770195105567109
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1836096151824575
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.41946076481917405
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7354444508114053
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.090024156752124
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9992552256663844,
              "spearman": 0.9992742645949356,
              "auroc_top30_worst": 0.9993565714285715,
              "pairwise_seed_ranking": 0.9619,
              "predicted_best_mean_error": 1.429543952524662,
              "seed0_mean_error": 1.501893677175045,
              "random_seed_mean_error": 1.490140748888254,
              "oracle_best_mean_error": 1.428934212654829,
              "improvement_over_seed0": 0.07234972465038303,
              "gap_to_oracle": 0.000609739869833037,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46926903223991395
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6698349451541901
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9500780524730682
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1830269901593526
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4895446684122085
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.315650343894959,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3275259503523509,
                  "rejected_mean_error": 2.9477131309509277,
                  "gap_rejected_minus_accepted": 1.6201871805985768
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8744298815727234,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1830269901593526,
                  "rejected_mean_error": 2.4090977031707763,
                  "gap_rejected_minus_accepted": 1.2260707130114237
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4662209749221802,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9500780524730682,
                  "rejected_mean_error": 2.029011284351349,
                  "gap_rejected_minus_accepted": 1.0789332318782807
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0188346803188324,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6698349451541901,
                  "rejected_mean_error": 1.7627812428315481,
                  "gap_rejected_minus_accepted": 1.092946297677358
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3603153944015505,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.339229833483696,
                  "rejected_mean_error": 2.9658682703971864,
                  "gap_rejected_minus_accepted": 1.6266384369134903
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.889841914176941,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1935626431306203,
                  "rejected_mean_error": 2.4268867793083193,
                  "gap_rejected_minus_accepted": 1.233324136177699
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4641323685646057,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9560792795419693,
                  "rejected_mean_error": 2.0477080748081207,
                  "gap_rejected_minus_accepted": 1.0916287952661514
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0220800936222076,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6708937606811524,
                  "rejected_mean_error": 1.7788936493396759,
                  "gap_rejected_minus_accepted": 1.1079998886585236
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9897508214265447,
              "spearman": 0.9822436780436075,
              "auroc_top30_bad": 0.9953904761904762,
              "mae": 0.09916529144905507,
              "mse": 0.01778767004380951,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7086474614552238,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.09879966056346894
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20538457934856416
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5056664403676987
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8650425847848257
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2215371421217918
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9930235838372341,
              "spearman": 0.9877467303339076,
              "auroc_top30_worst": 0.9911679999999999,
              "pairwise_seed_ranking": 0.9056,
              "predicted_best_mean_error": 1.640640801668167,
              "seed0_mean_error": 1.7044727271795272,
              "random_seed_mean_error": 1.6981746295690536,
              "oracle_best_mean_error": 1.637618626475334,
              "improvement_over_seed0": 0.06383192551136019,
              "gap_to_oracle": 0.0030221751928329876,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5251120247840881
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.851271958114245
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1760987492561341
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3880666267516009
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6977653141498565
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3917773008346557,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.510434845023685,
                  "rejected_mean_error": 3.3837395362854004,
                  "gap_rejected_minus_accepted": 1.8733046912617153
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9296923577785492,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3875420153967981,
                  "rejected_mean_error": 2.6264529529090126,
                  "gap_rejected_minus_accepted": 1.2389109375122145
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5858145356178284,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1760987492561341,
                  "rejected_mean_error": 2.219431879043579,
                  "gap_rejected_minus_accepted": 1.0433331297874449
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1920023262500763,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8529376402830544,
                  "rejected_mean_error": 1.9799756256976784,
                  "gap_rejected_minus_accepted": 1.127037985414624
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.398349952697754,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5147001620133718,
                  "rejected_mean_error": 3.412425813674927,
                  "gap_rejected_minus_accepted": 1.897725651661555
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.955730140209198,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3924299572559602,
                  "rejected_mean_error": 2.6306949172701155,
                  "gap_rejected_minus_accepted": 1.2382649600141553
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5858736038208008,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.174508389234543,
                  "rejected_mean_error": 2.234437065124512,
                  "gap_rejected_minus_accepted": 1.0599286758899689
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2044314742088318,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8486822233313606,
                  "rejected_mean_error": 1.9927871750000326,
                  "gap_rejected_minus_accepted": 1.1441049516686719
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9696036732799934,
              "spearman": 0.9797970061805291,
              "auroc_top30_bad": 0.9932464761904761,
              "mae": 0.17225878354730084,
              "mse": 0.0859635056200389,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7681186000021674,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.12020847141742706
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21706641464233398
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5643402971744538
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9333444266637166
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.384413278055191
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9561407607719413,
              "spearman": 0.9827939013080969,
              "auroc_top30_worst": 0.9965287619047619,
              "pairwise_seed_ranking": 0.9164,
              "predicted_best_mean_error": 1.9635537086725234,
              "seed0_mean_error": 2.049862780690193,
              "random_seed_mean_error": 2.0296543596982954,
              "oracle_best_mean_error": 1.9612690694332122,
              "improvement_over_seed0": 0.08630907201766957,
              "gap_to_oracle": 0.0022846392393112147,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7120591878890992
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0787605570677
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3510623165130615
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5562882203537265
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.0277799105644227
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.902297115325928,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8162524048487345,
                  "rejected_mean_error": 3.931527462005615,
                  "gap_rejected_minus_accepted": 2.1152750571568806
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.312922418117523,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.555588040942189,
                  "rejected_mean_error": 3.441338318986253,
                  "gap_rejected_minus_accepted": 1.885750278044064
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8317577242851257,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3510623165130615,
                  "rejected_mean_error": 2.7044975046157838,
                  "gap_rejected_minus_accepted": 1.3534351881027222
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3970943093299866,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0796074890100156,
                  "rejected_mean_error": 2.344512000155169,
                  "gap_rejected_minus_accepted": 1.2649045111451536
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9307316303253175,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8357026376989152,
                  "rejected_mean_error": 3.977304067611694,
                  "gap_rejected_minus_accepted": 2.141601429912779
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.39767986536026,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5726856982962971,
                  "rejected_mean_error": 3.466245549065726,
                  "gap_rejected_minus_accepted": 1.893559850769429
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8640710711479187,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3631628420352935,
                  "rejected_mean_error": 2.736562719345093,
                  "gap_rejected_minus_accepted": 1.3733998773097995
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4229205548763275,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0856026037344857,
                  "rejected_mean_error": 2.374720487365111,
                  "gap_rejected_minus_accepted": 1.2891178836306252
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.987529900045361,
              "spearman": 0.9860659793087035,
              "auroc_top30_bad": 0.9912830476190476,
              "mae": 0.10050752471848391,
              "mse": 0.01984390709516486,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7404927003283518,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07451478731632233
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.18803329541683197
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.500904100382328
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8609393614212671
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9771296727352816,
              "spearman": 0.9761436744599518,
              "auroc_top30_worst": 0.9792975238095238,
              "pairwise_seed_ranking": 0.9236,
              "predicted_best_mean_error": 1.6634000909328461,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.04319000375270843,
              "gap_to_oracle": 0.0015511549711229033,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6305467851161957
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9512805351271079
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2217925449848175
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4226846988839128
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.437680697441101,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5603654877609676,
                  "rejected_mean_error": 3.1463907623291014,
                  "gap_rejected_minus_accepted": 1.5860252745681338
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0019879937171936,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4220714256437763,
                  "rejected_mean_error": 2.6077606811310154,
                  "gap_rejected_minus_accepted": 1.1856892554872391
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6518658995628357,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2217925449848175,
                  "rejected_mean_error": 2.2161434854507447,
                  "gap_rejected_minus_accepted": 0.9943509404659272
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3195466995239258,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9523106052662237,
                  "rejected_mean_error": 1.975065954721343,
                  "gap_rejected_minus_accepted": 1.0227553494551191
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.399108576774597,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5512216420968374,
                  "rejected_mean_error": 3.1049061679840086,
                  "gap_rejected_minus_accepted": 1.5536845258871712
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9728679955005646,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4094532022182955,
                  "rejected_mean_error": 2.588567854866149,
                  "gap_rejected_minus_accepted": 1.1791146526478533
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6520605087280273,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2095598051548004,
                  "rejected_mean_error": 2.2036203842163085,
                  "gap_rejected_minus_accepted": 0.994060579061508
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3134889602661133,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9281982055732182,
                  "rejected_mean_error": 1.9688290733704592,
                  "gap_rejected_minus_accepted": 1.040630867797241
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
        "best_epoch": 66,
        "best_calib_loss": 0.05847380310297012,
        "train_time_sec": 10.778150081634521,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9788397593600402,
              "spearman": 0.939282811261902,
              "auroc_top30_bad": 0.9995258571428571,
              "mae": 0.09696525114272954,
              "mse": 0.02803319794640491,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.525,
              "expert_lt_simvla_seed0": 0.991,
              "same_context_pred_std": 0.6776650314897493,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.27002088171744254
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.28629188453848475
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.39412537953814025
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7112969358640258
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0711428765801596
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.998071343161212,
              "spearman": 0.9982493991299759,
              "auroc_top30_worst": 0.9986300952380953,
              "pairwise_seed_ranking": 0.8681,
              "predicted_best_mean_error": 1.4308499933481216,
              "seed0_mean_error": 1.4972091338038445,
              "random_seed_mean_error": 1.4855629888772965,
              "oracle_best_mean_error": 1.42489939853549,
              "improvement_over_seed0": 0.06635914045572289,
              "gap_to_oracle": 0.005950594812631493,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4626096314191818
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6619022846221924
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9432285037040711
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1775316296259561
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4849701192378997
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.339921259880066,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3228152985572814,
                  "rejected_mean_error": 2.9443635053634645,
                  "gap_rejected_minus_accepted": 1.621548206806183
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.876017987728119,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1775316296259561,
                  "rejected_mean_error": 2.4072855880737305,
                  "gap_rejected_minus_accepted": 1.2297539584477744
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4662431478500366,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9432285037040711,
                  "rejected_mean_error": 2.0267117347717285,
                  "gap_rejected_minus_accepted": 1.0834832310676574
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0157409608364105,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6619022846221924,
                  "rejected_mean_error": 1.7593260641098023,
                  "gap_rejected_minus_accepted": 1.09742377948761
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3783249616622926,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3339051381084654,
                  "rejected_mean_error": 2.966945095062256,
                  "gap_rejected_minus_accepted": 1.6330399569537903
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8832961022853851,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1876864230632782,
                  "rejected_mean_error": 2.425777266025543,
                  "gap_rejected_minus_accepted": 1.2380908429622648
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4722548127174377,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9488794795274734,
                  "rejected_mean_error": 2.0455387880802154,
                  "gap_rejected_minus_accepted": 1.0966593085527419
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0388244688510895,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6626008193492889,
                  "rejected_mean_error": 1.7754119052886963,
                  "gap_rejected_minus_accepted": 1.1128110859394074
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8966262993268856,
              "spearman": 0.8507301698188874,
              "auroc_top30_bad": 0.9530278095238095,
              "mae": 0.33236910659223795,
              "mse": 0.19278187622726456,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6206115365984326,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.41053445109725
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4089137315094471
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.562984569093585
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8854648204227289
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2199731270357967
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9001077753398378,
              "spearman": 0.7868636188567162,
              "auroc_top30_worst": 0.8819382857142856,
              "pairwise_seed_ranking": 0.7,
              "predicted_best_mean_error": 1.65759115087986,
              "seed0_mean_error": 1.7036175681352614,
              "random_seed_mean_error": 1.697212252020836,
              "oracle_best_mean_error": 1.6369523051977157,
              "improvement_over_seed0": 0.046026417255401464,
              "gap_to_oracle": 0.020638845682144247,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6425150275230408
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9786510224907826
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2698854278564453
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4152560000861887
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6968660296916962
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.957161450386048,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5278926270272997,
                  "rejected_mean_error": 3.2176266536712648,
                  "gap_rejected_minus_accepted": 1.689734026643965
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6241660714149475,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.414659613160975,
                  "rejected_mean_error": 2.5416820433954843,
                  "gap_rejected_minus_accepted": 1.1270224302345093
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3210996389389038,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2698854278564453,
                  "rejected_mean_error": 2.123846631526947,
                  "gap_rejected_minus_accepted": 0.8539612036705018
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0342068076133728,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9810985907579002,
                  "rejected_mean_error": 1.9359644377880443,
                  "gap_rejected_minus_accepted": 0.9548658470301441
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9394478797912598,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5340742017163171,
                  "rejected_mean_error": 3.2295078659057617,
                  "gap_rejected_minus_accepted": 1.6954336641894445
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6315501630306244,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4202588052354395,
                  "rejected_mean_error": 2.544698340552194,
                  "gap_rejected_minus_accepted": 1.1244395353167544
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3531591892242432,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2645336725711822,
                  "rejected_mean_error": 2.142701463699341,
                  "gap_rejected_minus_accepted": 0.8781677911281587
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0821599662303925,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9679009701524462,
                  "rejected_mean_error": 1.9514793097016645,
                  "gap_rejected_minus_accepted": 0.9835783395492183
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.795281358770854,
              "spearman": 0.8380245231670443,
              "auroc_top30_bad": 0.9198354285714285,
              "mae": 0.4165129489660263,
              "mse": 0.47010061456307506,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.48,
              "expert_lt_simvla_seed0": 0.992,
              "same_context_pred_std": 0.6529164517763038,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4130787822008133
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3970012983083725
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6693985832333564
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0126956626415253
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3824614222288132
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.5874376404730366,
              "spearman": 0.6422221541261788,
              "auroc_top30_worst": 0.7616304761904762,
              "pairwise_seed_ranking": 0.7344,
              "predicted_best_mean_error": 1.9881492899656297,
              "seed0_mean_error": 2.0495302921533582,
              "random_seed_mean_error": 2.02936255300045,
              "oracle_best_mean_error": 1.9609006407260894,
              "improvement_over_seed0": 0.06138100218772857,
              "gap_to_oracle": 0.02724864923954029,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.4260584406852723
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.5219337158860304
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.633832540512085
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6786636316191668
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.027466819000244
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3738800048828126,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8848017871644762,
                  "rejected_mean_error": 3.311452105522156,
                  "gap_rejected_minus_accepted": 1.4266503183576797
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.946575939655304,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6784156508735812,
                  "rejected_mean_error": 3.0723899644784654,
                  "gap_rejected_minus_accepted": 1.393974313604884
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5448944568634033,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.633832540512085,
                  "rejected_mean_error": 2.4211010974884033,
                  "gap_rejected_minus_accepted": 0.7872685569763183
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2132502794265747,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.5221739837917656,
                  "rejected_mean_error": 2.196257275158466,
                  "gap_rejected_minus_accepted": 0.6740832913667003
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4403899669647218,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.9204762094550663,
                  "rejected_mean_error": 3.211017036437988,
                  "gap_rejected_minus_accepted": 1.290540826982922
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9395785331726074,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6885787683693483,
                  "rejected_mean_error": 3.120926084972563,
                  "gap_rejected_minus_accepted": 1.4323473166032148
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5696980357170105,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6371451952457428,
                  "rejected_mean_error": 2.461915389060974,
                  "gap_rejected_minus_accepted": 0.8247701938152312
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2223565578460693,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.5166596973699236,
                  "rejected_mean_error": 2.2290535406632856,
                  "gap_rejected_minus_accepted": 0.7123938432933621
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.898942961287321,
              "spearman": 0.8657464778571313,
              "auroc_top30_bad": 0.9438346666666666,
              "mae": 0.29375121069550514,
              "mse": 0.15161148785319864,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.714951209459872,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.38787955534458163
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4022031854867935
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5347557995438575
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8909141281525293
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8541631145441994,
              "spearman": 0.8054197702526531,
              "auroc_top30_worst": 0.8768030476190477,
              "pairwise_seed_ranking": 0.6928,
              "predicted_best_mean_error": 1.691433776140213,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.015156318545341607,
              "gap_to_oracle": 0.029584840178489724,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7575998122692108
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9996464230502263
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2888496864795684
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4961184887553074
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.760639309883118,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5633715752760569,
                  "rejected_mean_error": 3.1193359746932985,
                  "gap_rejected_minus_accepted": 1.5559643994172416
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9963527619838715,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.496186641039945,
                  "rejected_mean_error": 2.3858886145936036,
                  "gap_rejected_minus_accepted": 0.8897019735536587
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6329590678215027,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2888496864795684,
                  "rejected_mean_error": 2.1490863439559935,
                  "gap_rejected_minus_accepted": 0.8602366574764251
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1279102265834808,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0025268691225935,
                  "rejected_mean_error": 1.9582914717042204,
                  "gap_rejected_minus_accepted": 0.9557646025816269
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6798209905624386,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.550790280368593,
                  "rejected_mean_error": 3.108788423538208,
                  "gap_rejected_minus_accepted": 1.5579981431696153
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9390241503715515,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4855907207185572,
                  "rejected_mean_error": 2.362572363444737,
                  "gap_rejected_minus_accepted": 0.8769816427261798
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6411844491958618,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.282013118982315,
                  "rejected_mean_error": 2.131167070388794,
                  "gap_rejected_minus_accepted": 0.849153951406479
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.153476893901825,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9733943130288806,
                  "rejected_mean_error": 1.9536025772757708,
                  "gap_rejected_minus_accepted": 0.9802082642468902
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
        "best_epoch": 78,
        "best_calib_loss": 0.010423065163195133,
        "train_time_sec": 35.128870248794556,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9997211648494257,
              "spearman": 0.9991027425800236,
              "auroc_top30_bad": 0.9999222857142858,
              "mae": 0.015123881340038498,
              "mse": 0.0004263498655859604,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6769342359710071,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05574655126582365
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17299822114626878
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3885018595393514
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7108518028773212
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0711428765801596
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9998326044377447,
              "spearman": 0.9997798933031955,
              "auroc_top30_worst": 0.9998291428571429,
              "pairwise_seed_ranking": 0.9449,
              "predicted_best_mean_error": 1.4261854983568192,
              "seed0_mean_error": 1.4972091338038445,
              "random_seed_mean_error": 1.4855629888772965,
              "oracle_best_mean_error": 1.42489939853549,
              "improvement_over_seed0": 0.07102363544702528,
              "gap_to_oracle": 0.0012860998213291008,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.45962922942638396
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6611027307510376
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9426321373462677
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1772153586069742
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4849701192378997
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.302635598182679,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3223505148887633,
                  "rejected_mean_error": 2.948546558380127,
                  "gap_rejected_minus_accepted": 1.6261960434913636
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8639525473117828,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1772153586069742,
                  "rejected_mean_error": 2.4082344011306764,
                  "gap_rejected_minus_accepted": 1.2310190425237022
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4563924670219421,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9426321373462677,
                  "rejected_mean_error": 2.027308101129532,
                  "gap_rejected_minus_accepted": 1.0846759637832641
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9965457320213318,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6611027307510376,
                  "rejected_mean_error": 1.7595925820668539,
                  "gap_rejected_minus_accepted": 1.0984898513158163
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.352367877960205,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3338129355510076,
                  "rejected_mean_error": 2.9677749180793764,
                  "gap_rejected_minus_accepted": 1.6339619825283689
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8688103556632996,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.187431634346644,
                  "rejected_mean_error": 2.4265416321754456,
                  "gap_rejected_minus_accepted": 1.2391099978288016
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4656954407691956,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9484251183271408,
                  "rejected_mean_error": 2.045993149280548,
                  "gap_rejected_minus_accepted": 1.0975680309534073
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0058387517929077,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6621475293636322,
                  "rejected_mean_error": 1.775563001950582,
                  "gap_rejected_minus_accepted": 1.1134154725869498
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9878379885844517,
              "spearman": 0.9804222155251113,
              "auroc_top30_bad": 0.994879238095238,
              "mae": 0.11182037494555115,
              "mse": 0.022298985312537746,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7088447981485081,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11242482267320156
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1956914955317974
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5069259327024221
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8635658856769403
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2199731270357967
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9900548181077928,
              "spearman": 0.9867471193261566,
              "auroc_top30_worst": 0.9910948571428572,
              "pairwise_seed_ranking": 0.8996,
              "predicted_best_mean_error": 1.6396467617750168,
              "seed0_mean_error": 1.7036175681352614,
              "random_seed_mean_error": 1.697212252020836,
              "oracle_best_mean_error": 1.6369523051977157,
              "improvement_over_seed0": 0.06397080636024466,
              "gap_to_oracle": 0.002694456577301052,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5259112105369568
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8505834117531776
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1724957522392272
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.38713571391126
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6968660296916962
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.364198350906373,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5105141240755717,
                  "rejected_mean_error": 3.3740331802368164,
                  "gap_rejected_minus_accepted": 1.8635190561612447
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8854758143424988,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3865156161619734,
                  "rejected_mean_error": 2.62593420054585,
                  "gap_rejected_minus_accepted": 1.2394185843838768
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5993902683258057,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1724957522392272,
                  "rejected_mean_error": 2.221236307144165,
                  "gap_rejected_minus_accepted": 1.0487405549049378
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2363060414791107,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8517757515176035,
                  "rejected_mean_error": 1.9791640628491038,
                  "gap_rejected_minus_accepted": 1.1273883113315004
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.33175675868988,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5172474682331085,
                  "rejected_mean_error": 3.3809484672546386,
                  "gap_rejected_minus_accepted": 1.86370099902153
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9153203964233398,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.389583091844212,
                  "rejected_mean_error": 2.6357516485547263,
                  "gap_rejected_minus_accepted": 1.2461685567105143
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6017391085624695,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1705521957874299,
                  "rejected_mean_error": 2.2366829404830932,
                  "gap_rejected_minus_accepted": 1.0661307446956634
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2469797134399414,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8457130198440854,
                  "rejected_mean_error": 1.9926442341371016,
                  "gap_rejected_minus_accepted": 1.1469312142930161
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9612076169909792,
              "spearman": 0.9789821202195585,
              "auroc_top30_bad": 0.9918003809523811,
              "mae": 0.19947325721532105,
              "mse": 0.11975701719263257,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7418031963829635,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1061373228430748
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22187683329582214
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.553843669128418
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9317768283526102
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3824614222288132
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9320311096257177,
              "spearman": 0.9803515552969956,
              "auroc_top30_worst": 0.9974247619047618,
              "pairwise_seed_ranking": 0.8876,
              "predicted_best_mean_error": 1.9651989402770995,
              "seed0_mean_error": 2.0495302921533582,
              "random_seed_mean_error": 2.02936255300045,
              "oracle_best_mean_error": 1.9609006407260894,
              "improvement_over_seed0": 0.08433135187625873,
              "gap_to_oracle": 0.004298299551010132,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7236321020126343
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0834721361215298
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3485458641052246
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5558239656216555
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.027466819000244
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7731498003005983,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8331264735327826,
                  "rejected_mean_error": 3.7765299282073976,
                  "gap_rejected_minus_accepted": 1.943403454674615
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.223803162574768,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5551946440526745,
                  "rejected_mean_error": 3.4412656302650135,
                  "gap_rejected_minus_accepted": 1.886070986212339
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8238676190376282,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3485458641052246,
                  "rejected_mean_error": 2.7063877738952637,
                  "gap_rejected_minus_accepted": 1.3578419097900392
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.424115926027298,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0847270991474676,
                  "rejected_mean_error": 2.342384142707735,
                  "gap_rejected_minus_accepted": 1.2576570435602674
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8039495944976807,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8519327731927235,
                  "rejected_mean_error": 3.827907962799072,
                  "gap_rejected_minus_accepted": 1.9759751896063487
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.27858430147171,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.571662890879228,
                  "rejected_mean_error": 3.467962102284507,
                  "gap_rejected_minus_accepted": 1.896299211405279
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8726598620414734,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3601851923465729,
                  "rejected_mean_error": 2.738875391960144,
                  "gap_rejected_minus_accepted": 1.3786901996135712
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.440434455871582,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0864533682664235,
                  "rejected_mean_error": 2.3739893627676736,
                  "gap_rejected_minus_accepted": 1.2875359945012501
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.982555569970817,
              "spearman": 0.9818736659168276,
              "auroc_top30_bad": 0.9891702857142858,
              "mae": 0.11898210923820735,
              "mse": 0.027801503544136314,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7502185677015311,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05647710460424423
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19764117033481599
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5004095596909524
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8646616293986639
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9702163941178256,
              "spearman": 0.9709950606048389,
              "auroc_top30_worst": 0.9677043809523809,
              "pairwise_seed_ranking": 0.8984,
              "predicted_best_mean_error": 1.6639218242168428,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.0426682704687118,
              "gap_to_oracle": 0.0020728882551195316,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.631416951417923
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9529735034283919
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.220747168970108
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4291257730234406
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.672043800354005,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5593921005725861,
                  "rejected_mean_error": 3.155151247024536,
                  "gap_rejected_minus_accepted": 1.5957591464519498
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9954619407653809,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4285494365521658,
                  "rejected_mean_error": 2.5883680414467953,
                  "gap_rejected_minus_accepted": 1.1598186048946295
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6943174600601196,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.220747168970108,
                  "rejected_mean_error": 2.2171888614654542,
                  "gap_rejected_minus_accepted": 0.9964416924953463
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2957299649715424,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9544168730703787,
                  "rejected_mean_error": 1.974362366863605,
                  "gap_rejected_minus_accepted": 1.0199454937932262
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.653421640396118,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5509547860092587,
                  "rejected_mean_error": 3.1073078727722168,
                  "gap_rejected_minus_accepted": 1.556353086762958
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9797543585300446,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4189551604941566,
                  "rejected_mean_error": 2.56036362950764,
                  "gap_rejected_minus_accepted": 1.1414084690134834
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6900261044502258,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.209100062608719,
                  "rejected_mean_error": 2.20408012676239,
                  "gap_rejected_minus_accepted": 0.9949800641536712
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2826997935771942,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9284738306961362,
                  "rejected_mean_error": 1.9687362157087276,
                  "gap_rejected_minus_accepted": 1.0402623850125914
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
        "best_epoch": 56,
        "best_calib_loss": 0.010297456756234169,
        "train_time_sec": 42.76903057098389,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9990480938949511,
              "spearman": 0.9976836100324142,
              "auroc_top30_bad": 0.9997518095238095,
              "mae": 0.06434639255284565,
              "mse": 0.005895406872511689,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.997,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7069336340960272,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05847980600397568
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17435657145897857
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3888292508776998
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7110626300213082
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0711428765801596
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9991064013818313,
              "spearman": 0.998922723572857,
              "auroc_top30_worst": 0.9993796190476191,
              "pairwise_seed_ranking": 0.9515,
              "predicted_best_mean_error": 1.425759786784649,
              "seed0_mean_error": 1.4972091338038445,
              "random_seed_mean_error": 1.4855629888772965,
              "oracle_best_mean_error": 1.42489939853549,
              "improvement_over_seed0": 0.07144934701919547,
              "gap_to_oracle": 0.0008603882491589054,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4617456840276718
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6615789695262909
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9430214704036712
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1773709308624267
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4849701192378997
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4209849596023565,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.322415911939409,
                  "rejected_mean_error": 2.9479579849243165,
                  "gap_rejected_minus_accepted": 1.6255420729849075
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9427413940429688,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1773709308624267,
                  "rejected_mean_error": 2.4077676843643188,
                  "gap_rejected_minus_accepted": 1.230396753501892
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5109753608703613,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9430214704036712,
                  "rejected_mean_error": 2.0269187680721283,
                  "gap_rejected_minus_accepted": 1.083897297668457
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0450634360313416,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6615789695262909,
                  "rejected_mean_error": 1.759433835808436,
                  "gap_rejected_minus_accepted": 1.097854866282145
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.463443732261658,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3339328508244621,
                  "rejected_mean_error": 2.9666956806182863,
                  "gap_rejected_minus_accepted": 1.6327628297938241
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9565470218658447,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1876987863381703,
                  "rejected_mean_error": 2.4257401762008666,
                  "gap_rejected_minus_accepted": 1.2380413898626963
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.515955626964569,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9484986935853958,
                  "rejected_mean_error": 2.0459195740222933,
                  "gap_rejected_minus_accepted": 1.0974208804368975
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.060278445482254,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.662540456533432,
                  "rejected_mean_error": 1.7754320262273153,
                  "gap_rejected_minus_accepted": 1.1128915696938835
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9871444472245804,
              "spearman": 0.9763905076427433,
              "auroc_top30_bad": 0.9938544761904762,
              "mae": 0.11095628400109708,
              "mse": 0.021782484245821798,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.984,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7374962609712357,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1396751648634672
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2111772595345974
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5043122483342886
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8637685808241368
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2199731270357967
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9919190702388265,
              "spearman": 0.9842650031776022,
              "auroc_top30_worst": 0.9901257142857143,
              "pairwise_seed_ranking": 0.8916,
              "predicted_best_mean_error": 1.6403949579000474,
              "seed0_mean_error": 1.7036175681352614,
              "random_seed_mean_error": 1.697212252020836,
              "oracle_best_mean_error": 1.6369523051977157,
              "improvement_over_seed0": 0.06322261023521403,
              "gap_to_oracle": 0.0034426527023316833,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5237738327980042
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8509315536954464
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.173029294681549
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3881067325438519
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6968660296916962
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.405658721923828,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5104374096658495,
                  "rejected_mean_error": 3.3747236099243163,
                  "gap_rejected_minus_accepted": 1.8642862002584668
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.965437263250351,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3875135692868188,
                  "rejected_mean_error": 2.6229467178685977,
                  "gap_rejected_minus_accepted": 1.2354331485817789
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6524217128753662,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.173029294681549,
                  "rejected_mean_error": 2.2207027647018434,
                  "gap_rejected_minus_accepted": 1.0476734700202943
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1873091757297516,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8523025320360835,
                  "rejected_mean_error": 1.978988094543571,
                  "gap_rejected_minus_accepted": 1.1266855625074874
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.407362174987793,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.516010104417801,
                  "rejected_mean_error": 3.392084741592407,
                  "gap_rejected_minus_accepted": 1.8760746371746062
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9861361384391785,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3913111822171644,
                  "rejected_mean_error": 2.6306222374477084,
                  "gap_rejected_minus_accepted": 1.239311055230544
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.654110610485077,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.171108237504959,
                  "rejected_mean_error": 2.236126898765564,
                  "gap_rejected_minus_accepted": 1.0650186612606047
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.203790307044983,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8423892623848386,
                  "rejected_mean_error": 1.9937640026928907,
                  "gap_rejected_minus_accepted": 1.151374740308052
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.971797214756598,
              "spearman": 0.9766931057577687,
              "auroc_top30_bad": 0.9934902857142858,
              "mae": 0.170218686237745,
              "mse": 0.07019950330084619,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.806257351021759,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.12602740705013274
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22544962408542632
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5578002970933914
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9305146744092305
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3824614222288132
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9634293863931056,
              "spearman": 0.9818088761656808,
              "auroc_top30_worst": 0.9973272380952382,
              "pairwise_seed_ranking": 0.9048,
              "predicted_best_mean_error": 1.9628489761352539,
              "seed0_mean_error": 2.0495302921533582,
              "random_seed_mean_error": 2.02936255300045,
              "oracle_best_mean_error": 1.9609006407260894,
              "improvement_over_seed0": 0.08668131601810436,
              "gap_to_oracle": 0.0019483354091645033,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7262874584197998
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0783089193013997
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3515114179611205
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5562760695211415
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.027466819000244
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.0651861429214486,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8172826506296793,
                  "rejected_mean_error": 3.919124334335327,
                  "gap_rejected_minus_accepted": 2.101841683705648
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.348807156085968,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5555191019683154,
                  "rejected_mean_error": 3.4402943297316093,
                  "gap_rejected_minus_accepted": 1.8847752277632939
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8461827635765076,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3515114179611205,
                  "rejected_mean_error": 2.703422220039368,
                  "gap_rejected_minus_accepted": 1.3519108020782473
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4194017052650452,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0792890093958796,
                  "rejected_mean_error": 2.34420070844119,
                  "gap_rejected_minus_accepted": 1.2649116990453104
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.079885935783386,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8353332059913212,
                  "rejected_mean_error": 3.977304067611694,
                  "gap_rejected_minus_accepted": 2.141970861620373
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.419355571269989,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5721729816918704,
                  "rejected_mean_error": 3.4664480232057118,
                  "gap_rejected_minus_accepted": 1.8942750415138414
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8683432340621948,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3619993212223054,
                  "rejected_mean_error": 2.7370612630844118,
                  "gap_rejected_minus_accepted": 1.3750619418621064
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4368072152137756,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.082688911093606,
                  "rejected_mean_error": 2.3752576023499596,
                  "gap_rejected_minus_accepted": 1.2925686912563537
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9880584045387842,
              "spearman": 0.985099669067631,
              "auroc_top30_bad": 0.9934544761904762,
              "mae": 0.10035755363609641,
              "mse": 0.018591323305611782,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.742760596035074,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07399341720342636
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1958483249425888
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5012515566468239
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8599055253744126
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9838131741402713,
              "spearman": 0.9808975975024624,
              "auroc_top30_worst": 0.9833813333333333,
              "pairwise_seed_ranking": 0.912,
              "predicted_best_mean_error": 1.663629163980484,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.042960930705070455,
              "gap_to_oracle": 0.0017802280187608766,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6300003125667571
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9503676559871588
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2220632229328157
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4233976552036525
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5037749052047733,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5602156409422556,
                  "rejected_mean_error": 3.14773938369751,
                  "gap_rejected_minus_accepted": 1.5875237427552542
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.022352457046509,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.422590527774939,
                  "rejected_mean_error": 2.6062066916840525,
                  "gap_rejected_minus_accepted": 1.1836161639091134
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6718337535858154,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2220632229328157,
                  "rejected_mean_error": 2.2158728075027465,
                  "gap_rejected_minus_accepted": 0.9938095845699308
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.290237933397293,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9517285280143872,
                  "rejected_mean_error": 1.9752603946144325,
                  "gap_rejected_minus_accepted": 1.0235318666000452
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4341349840164184,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5509547860092587,
                  "rejected_mean_error": 3.1073078727722168,
                  "gap_rejected_minus_accepted": 1.556353086762958
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9892187118530273,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4094667767777163,
                  "rejected_mean_error": 2.5885275621262807,
                  "gap_rejected_minus_accepted": 1.1790607853485644
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6645580530166626,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2093269245624543,
                  "rejected_mean_error": 2.2038532648086546,
                  "gap_rejected_minus_accepted": 0.9945263402462003
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.284736692905426,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9268753249493856,
                  "rejected_mean_error": 1.96927474973036,
                  "gap_rejected_minus_accepted": 1.0423994247809745
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
        "best_epoch": 54,
        "best_calib_loss": 0.009612731635570526,
        "train_time_sec": 29.24747586250305,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995232460332926,
              "spearman": 0.9983850880720361,
              "auroc_top30_bad": 0.9998692380952381,
              "mae": 0.019538502483966293,
              "mse": 0.0006961735693411571,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6869656452999057,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.05802629835705739
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17305187714020723
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3885278280909872
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7108913481908384
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0711428765801596
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9997082272224544,
              "spearman": 0.9996354028813983,
              "auroc_top30_worst": 0.9997535238095238,
              "pairwise_seed_ranking": 0.9535,
              "predicted_best_mean_error": 1.4256289302110672,
              "seed0_mean_error": 1.4972091338038445,
              "random_seed_mean_error": 1.4855629888772965,
              "oracle_best_mean_error": 1.42489939853549,
              "improvement_over_seed0": 0.07158020359277728,
              "gap_to_oracle": 0.0007295316755770997,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.459523765206337
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6611103766441345
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9427217827796937
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.177213679854075
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4849701192378997
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3241286754608157,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.322353292412228,
                  "rejected_mean_error": 2.9485215606689454,
                  "gap_rejected_minus_accepted": 1.6261682682567173
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8628164529800415,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.177213679854075,
                  "rejected_mean_error": 2.4082394373893736,
                  "gap_rejected_minus_accepted": 1.2310257575352985
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4607667326927185,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9427217827796937,
                  "rejected_mean_error": 2.027218455696106,
                  "gap_rejected_minus_accepted": 1.0844966729164125
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.001211166381836,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6611103766441345,
                  "rejected_mean_error": 1.7595900334358214,
                  "gap_rejected_minus_accepted": 1.098479656791687
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3689780235290527,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3339463217390908,
                  "rejected_mean_error": 2.9665744423866274,
                  "gap_rejected_minus_accepted": 1.6326281206475366
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8747167885303497,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1875565265814463,
                  "rejected_mean_error": 2.426166955471039,
                  "gap_rejected_minus_accepted": 1.2386104288895927
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4669857025146484,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9484022687673569,
                  "rejected_mean_error": 2.046015998840332,
                  "gap_rejected_minus_accepted": 1.097613730072975
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.003939539194107,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6621656312942504,
                  "rejected_mean_error": 1.775556967973709,
                  "gap_rejected_minus_accepted": 1.1133913366794586
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.988386601036491,
              "spearman": 0.9807190802331939,
              "auroc_top30_bad": 0.9952190476190477,
              "mae": 0.10257976276306435,
              "mse": 0.021273294932833912,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.988,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7243455134836763,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10493503892421722
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20803055414557456
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5040490721791983
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8635384820997715
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2199731270357967
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9936059585022144,
              "spearman": 0.9875061557159397,
              "auroc_top30_worst": 0.9903116190476191,
              "pairwise_seed_ranking": 0.9152,
              "predicted_best_mean_error": 1.6396431505680085,
              "seed0_mean_error": 1.7036175681352614,
              "random_seed_mean_error": 1.697212252020836,
              "oracle_best_mean_error": 1.6369523051977157,
              "improvement_over_seed0": 0.06397441756725297,
              "gap_to_oracle": 0.002690845370292738,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5229151725769043
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8502375817833803
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1715915778160095
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3859040258662787
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6968660296916962
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4085027456283576,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.510175707022349,
                  "rejected_mean_error": 3.3770789337158202,
                  "gap_rejected_minus_accepted": 1.8669032266934713
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9395181238651276,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3853018699231754,
                  "rejected_mean_error": 2.6295676836952233,
                  "gap_rejected_minus_accepted": 1.244265813772048
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.606239140033722,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1715915778160095,
                  "rejected_mean_error": 2.222140481567383,
                  "gap_rejected_minus_accepted": 1.0505489037513733
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1954463124275208,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8520483869714097,
                  "rejected_mean_error": 1.9790729903869466,
                  "gap_rejected_minus_accepted": 1.127024603415537
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.431052899360657,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5164467442035674,
                  "rejected_mean_error": 3.388154983520508,
                  "gap_rejected_minus_accepted": 1.8717082393169404
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9578923881053925,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3894561696498788,
                  "rejected_mean_error": 2.636128385861715,
                  "gap_rejected_minus_accepted": 1.246672216211836
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6046888828277588,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1693728926181792,
                  "rejected_mean_error": 2.237862243652344,
                  "gap_rejected_minus_accepted": 1.0684893510341646
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1885903775691986,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8457338871463896,
                  "rejected_mean_error": 1.9926372039764322,
                  "gap_rejected_minus_accepted": 1.1469033168300427
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9711850832452151,
              "spearman": 0.978735783342434,
              "auroc_top30_bad": 0.9916899047619048,
              "mae": 0.17772642597500235,
              "mse": 0.08390306142860136,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7842914471108626,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11574744433164597
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21601977033615113
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.55489647128582
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9320124228477478
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3824614222288132
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.960002091058262,
              "spearman": 0.9824218941580124,
              "auroc_top30_worst": 0.9959283809523809,
              "pairwise_seed_ranking": 0.9096,
              "predicted_best_mean_error": 1.9624924998283386,
              "seed0_mean_error": 2.0495302921533582,
              "random_seed_mean_error": 2.02936255300045,
              "oracle_best_mean_error": 1.9609006407260894,
              "improvement_over_seed0": 0.08703779232501963,
              "gap_to_oracle": 0.0015918591022492379,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7188226690292359
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.082238447589752
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3516778551101685
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5553709512580431
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.027466819000244
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9130030870437627,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8158579088846842,
                  "rejected_mean_error": 3.9319470100402834,
                  "gap_rejected_minus_accepted": 2.116089101155599
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2637410759925842,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5545808263878431,
                  "rejected_mean_error": 3.443103161101905,
                  "gap_rejected_minus_accepted": 1.8885223347140618
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8539766073226929,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3516778551101685,
                  "rejected_mean_error": 2.7032557828903196,
                  "gap_rejected_minus_accepted": 1.3515779277801512
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4128021001815796,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.083454218916238,
                  "rejected_mean_error": 2.3428093417604297,
                  "gap_rejected_minus_accepted": 1.2593551228441917
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9381643533706665,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8347086340851253,
                  "rejected_mean_error": 3.982925214767456,
                  "gap_rejected_minus_accepted": 2.148216580682331
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3127707839012146,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5717300586203202,
                  "rejected_mean_error": 3.4677627313704718,
                  "gap_rejected_minus_accepted": 1.8960326727501515
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.887586772441864,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3641647589206696,
                  "rejected_mean_error": 2.7348958253860474,
                  "gap_rejected_minus_accepted": 1.3707310664653778
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4282182157039642,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0862426478711387,
                  "rejected_mean_error": 2.374060354130791,
                  "gap_rejected_minus_accepted": 1.2878177062596523
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9892152151967671,
              "spearman": 0.987259275682254,
              "auroc_top30_bad": 0.9929988571428572,
              "mae": 0.10364618504690007,
              "mse": 0.01948970080822317,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7178122449310904,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.058949395835399626
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19145744836330414
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5003864172577858
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8600724811315537
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9839513318427315,
              "spearman": 0.9817514973129584,
              "auroc_top30_worst": 0.9828327619047619,
              "pairwise_seed_ranking": 0.9156,
              "predicted_best_mean_error": 1.6630694932937622,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.04352060139179237,
              "gap_to_oracle": 0.0012205573320389629,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6299049770832061
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9512230491217895
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.220829166841507
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4236375949085394
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3493829727172852,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5598354752063752,
                  "rejected_mean_error": 3.1511608753204348,
                  "gap_rejected_minus_accepted": 1.5913254001140595
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9200671017169952,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4232341833849982,
                  "rejected_mean_error": 2.604279837669275,
                  "gap_rejected_minus_accepted": 1.1810456542842767
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6112071871757507,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.220829166841507,
                  "rejected_mean_error": 2.217106863594055,
                  "gap_rejected_minus_accepted": 0.9962776967525482
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.275989979505539,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9522396624088287,
                  "rejected_mean_error": 1.9750896528156487,
                  "gap_rejected_minus_accepted": 1.02284999040682
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.328088617324829,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5507218987411924,
                  "rejected_mean_error": 3.1094038581848142,
                  "gap_rejected_minus_accepted": 1.5586819594436219
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9012527465820312,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.410695092085211,
                  "rejected_mean_error": 2.5848816103405423,
                  "gap_rejected_minus_accepted": 1.1741865182553313
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6119552850723267,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2096579954624176,
                  "rejected_mean_error": 2.2035221939086913,
                  "gap_rejected_minus_accepted": 0.9938641984462737
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2690831124782562,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9296789325418926,
                  "rejected_mean_error": 1.9683302188302105,
                  "gap_rejected_minus_accepted": 1.038651286288318
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
        "best_epoch": 45,
        "best_calib_loss": 0.061781782656908035,
        "train_time_sec": 10.641635417938232,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9826160783185369,
              "spearman": 0.9542635301188837,
              "auroc_top30_bad": 0.9991592857142857,
              "mae": 0.09233948700568871,
              "mse": 0.0265149278000101,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.518,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.74625137458408,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11126876036345493
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1747495441052597
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3010564919823548
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6488760833974773
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0237238207039308
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.997945223298542,
              "spearman": 0.9973756740070268,
              "auroc_top30_worst": 0.9978851428571428,
              "pairwise_seed_ranking": 0.8608,
              "predicted_best_mean_error": 1.4313127516806126,
              "seed0_mean_error": 1.4966771293878556,
              "random_seed_mean_error": 1.4850968795716764,
              "oracle_best_mean_error": 1.42449176928401,
              "improvement_over_seed0": 0.06536437770724302,
              "gap_to_oracle": 0.0068209823966025596,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.46233486831188203
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6615389019966126
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9425220395088196
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1772227100054422
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4844832009077071
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3212804794311523,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3221277408864762,
                  "rejected_mean_error": 2.9456823410987854,
                  "gap_rejected_minus_accepted": 1.6235546002123091
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8853890299797058,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1772227100054422,
                  "rejected_mean_error": 2.406264673614502,
                  "gap_rejected_minus_accepted": 1.22904196360906
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4765501022338867,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9425220395088196,
                  "rejected_mean_error": 2.0264443623065946,
                  "gap_rejected_minus_accepted": 1.083922322797775
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.013658881187439,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6615389019966126,
                  "rejected_mean_error": 1.7587979672114054,
                  "gap_rejected_minus_accepted": 1.0972590652147929
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3536150217056275,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3333807215425704,
                  "rejected_mean_error": 2.966344799995422,
                  "gap_rejected_minus_accepted": 1.6329640784528519
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.896024763584137,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.187252243677775,
                  "rejected_mean_error": 2.424951786518097,
                  "gap_rejected_minus_accepted": 1.237699542840322
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4913976788520813,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9482171061038971,
                  "rejected_mean_error": 2.045137152671814,
                  "gap_rejected_minus_accepted": 1.0969200465679168
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0395605862140656,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6618686702251434,
                  "rejected_mean_error": 1.7749466157754263,
                  "gap_rejected_minus_accepted": 1.113077945550283
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8943277485650203,
              "spearman": 0.8461209534834158,
              "auroc_top30_bad": 0.9574674285714286,
              "mae": 0.35028225244879724,
              "mse": 0.21825532013183738,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.512,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6923543492268667,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.43939566251635553
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.43775813530683516
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5603500173807144
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8923051912705103
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.219241336542368
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9045241795377711,
              "spearman": 0.8212358986469751,
              "auroc_top30_worst": 0.9087360000000001,
              "pairwise_seed_ranking": 0.7196,
              "predicted_best_mean_error": 1.658424010515213,
              "seed0_mean_error": 1.7036175681352614,
              "random_seed_mean_error": 1.697212252020836,
              "oracle_best_mean_error": 1.6369523051977157,
              "improvement_over_seed0": 0.0451935576200484,
              "gap_to_oracle": 0.021471705317497314,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7490599150657654
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9586253838661389
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2361446568489074
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4184797037003645
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6968660296916962
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0848607778549195,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5263027753300138,
                  "rejected_mean_error": 3.2319353189468383,
                  "gap_rejected_minus_accepted": 1.7056325436168245
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6336434185504913,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4176524813299882,
                  "rejected_mean_error": 2.5327225626467134,
                  "gap_rejected_minus_accepted": 1.1150700813167251
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3650099635124207,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2361446568489074,
                  "rejected_mean_error": 2.1575874025344848,
                  "gap_rejected_minus_accepted": 0.9214427456855774
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0457413494586945,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9591801890169089,
                  "rejected_mean_error": 1.9432861664379164,
                  "gap_rejected_minus_accepted": 0.9841059774210075
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0367827892303465,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.533532469669978,
                  "rejected_mean_error": 3.234383454322815,
                  "gap_rejected_minus_accepted": 1.7008509846528372
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.649210274219513,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4287731833955184,
                  "rejected_mean_error": 2.5194255037913247,
                  "gap_rejected_minus_accepted": 1.0906523203958063
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.382336437702179,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2332826941013335,
                  "rejected_mean_error": 2.1739524421691896,
                  "gap_rejected_minus_accepted": 0.9406697480678561
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.07874196767807,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.932078455648725,
                  "rejected_mean_error": 1.9635478573686935,
                  "gap_rejected_minus_accepted": 1.0314694017199684
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.805823920245681,
              "spearman": 0.831273088345391,
              "auroc_top30_bad": 0.9282514285714285,
              "mae": 0.43155294680297374,
              "mse": 0.47906190098429136,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.516,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7211591252966527,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4648591302037239
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.44063279366493224
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6512548349261283
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0118840501626332
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3812216915369033
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6165616343828813,
              "spearman": 0.6720862464551979,
              "auroc_top30_worst": 0.7813363809523809,
              "pairwise_seed_ranking": 0.762,
              "predicted_best_mean_error": 1.9899691398143768,
              "seed0_mean_error": 2.0495302921533582,
              "random_seed_mean_error": 2.02936255300045,
              "oracle_best_mean_error": 1.9609006407260894,
              "improvement_over_seed0": 0.059561152338981405,
              "gap_to_oracle": 0.02906849908828746,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3346305856704712
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4768824571600327
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.6244614753723146
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6779362762660615
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.027466819000244
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3937879085540774,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8762526763280232,
                  "rejected_mean_error": 3.388394103050232,
                  "gap_rejected_minus_accepted": 1.5121414267222086
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9155099391937256,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6777385818029544,
                  "rejected_mean_error": 3.0744168453704055,
                  "gap_rejected_minus_accepted": 1.396678263567451
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5356048941612244,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.6244614753723146,
                  "rejected_mean_error": 2.430472162628174,
                  "gap_rejected_minus_accepted": 0.8060106872558594
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2710968255996704,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.4766596523336708,
                  "rejected_mean_error": 2.2114611019955883,
                  "gap_rejected_minus_accepted": 0.7348014496619175
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4293197631835937,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.9151837397946252,
                  "rejected_mean_error": 3.258649263381958,
                  "gap_rejected_minus_accepted": 1.343465523587333
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9053311944007874,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6914776622611571,
                  "rejected_mean_error": 3.1123214316746544,
                  "gap_rejected_minus_accepted": 1.4208437694134972
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5548444986343384,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6387815210819245,
                  "rejected_mean_error": 2.4602790632247924,
                  "gap_rejected_minus_accepted": 0.8214975421428679
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2670595347881317,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.4874828159809113,
                  "rejected_mean_error": 2.2388831851954127,
                  "gap_rejected_minus_accepted": 0.7514003692145015
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9059970424554387,
              "spearman": 0.85456913899053,
              "auroc_top30_bad": 0.9424251428571429,
              "mae": 0.30546086588799953,
              "mse": 0.16628564071428337,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.484,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7881781100498122,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5074111333489418
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4242841233253479
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.525338530242443
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.895314087176323
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8654887465588026,
              "spearman": 0.8062096864061994,
              "auroc_top30_worst": 0.8619855238095238,
              "pairwise_seed_ranking": 0.718,
              "predicted_best_mean_error": 1.68699806702137,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.019592027664184553,
              "gap_to_oracle": 0.02514913105964678,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6800668613910675
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9921738204474633
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.290406242799759
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.495509592486597
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.797821593284608,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5603081871933406,
                  "rejected_mean_error": 3.146906467437744,
                  "gap_rejected_minus_accepted": 1.5865982802444034
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9518344700336456,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4955770949353022,
                  "rejected_mean_error": 2.3877133580442433,
                  "gap_rejected_minus_accepted": 0.8921362631089411
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6654555797576904,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.290406242799759,
                  "rejected_mean_error": 2.1475297876358033,
                  "gap_rejected_minus_accepted": 0.8571235448360444
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1954990029335022,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9932117265062972,
                  "rejected_mean_error": 1.9614031468791413,
                  "gap_rejected_minus_accepted": 0.9681914203728441
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.740313458442688,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.550790280368593,
                  "rejected_mean_error": 3.108788423538208,
                  "gap_rejected_minus_accepted": 1.5579981431696153
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8958097696304321,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4930450682015342,
                  "rejected_mean_error": 2.3404459669476463,
                  "gap_rejected_minus_accepted": 0.8474008987461121
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6439767479896545,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2810348570346832,
                  "rejected_mean_error": 2.132145332336426,
                  "gap_rejected_minus_accepted": 0.8511104753017427
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1825243830680847,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9708663494814009,
                  "rejected_mean_error": 1.9544542441393602,
                  "gap_rejected_minus_accepted": 0.9835878946579593
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
        "best_epoch": 52,
        "best_calib_loss": 0.015841513872146606,
        "train_time_sec": 35.15504598617554,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.999050630932188,
              "spearman": 0.995604948298612,
              "auroc_top30_bad": 0.999874761904762,
              "mae": 0.023009154273674358,
              "mse": 0.0013975780312344,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.956,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7207554897952113,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.012833254746627063
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.08148883367064409
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.29738981163443534
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6481609658952647
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0237238207039308
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9996774217355471,
              "spearman": 0.9996213455528538,
              "auroc_top30_worst": 0.9996979047619048,
              "pairwise_seed_ranking": 0.9334,
              "predicted_best_mean_error": 1.426280879944563,
              "seed0_mean_error": 1.4966771293878556,
              "random_seed_mean_error": 1.4850968795716764,
              "oracle_best_mean_error": 1.42449176928401,
              "improvement_over_seed0": 0.07039624944329259,
              "gap_to_oracle": 0.0017891106605529838,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4594513365030289
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.660495525932312
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9420807276725769
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1767617387135823
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4844832009077071
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3123699426651,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3218763434886933,
                  "rejected_mean_error": 2.947944917678833,
                  "gap_rejected_minus_accepted": 1.6260685741901397
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8507803976535797,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1767617387135823,
                  "rejected_mean_error": 2.407647587490082,
                  "gap_rejected_minus_accepted": 1.2308858487764995
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.451203167438507,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9420807276725769,
                  "rejected_mean_error": 2.0268856741428376,
                  "gap_rejected_minus_accepted": 1.0848049464702607
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9941776543855667,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.660495525932312,
                  "rejected_mean_error": 1.759145759232839,
                  "gap_rejected_minus_accepted": 1.098650233300527
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.351854944229126,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3333855725659265,
                  "rejected_mean_error": 2.9663011407852173,
                  "gap_rejected_minus_accepted": 1.6329155682192908
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8650230169296265,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1869922231038412,
                  "rejected_mean_error": 2.4257318482398986,
                  "gap_rejected_minus_accepted": 1.2387396251360574
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4540055990219116,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9477719979286194,
                  "rejected_mean_error": 2.0455822608470915,
                  "gap_rejected_minus_accepted": 1.097810262918472
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0039271116256714,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6613619859218598,
                  "rejected_mean_error": 1.7751155105431875,
                  "gap_rejected_minus_accepted": 1.1137535246213277
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9787684767535778,
              "spearman": 0.9639191503673681,
              "auroc_top30_bad": 0.995376,
              "mae": 0.13123889118731022,
              "mse": 0.04106739124521205,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.904,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7480510510352383,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2258713381290436
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24705125944614412
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5055891538739204
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8624057149966557
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.219241336542368
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9913351229317608,
              "spearman": 0.9910488866872875,
              "auroc_top30_worst": 0.9941760000000001,
              "pairwise_seed_ranking": 0.8812,
              "predicted_best_mean_error": 1.6422109287977218,
              "seed0_mean_error": 1.7036175681352614,
              "random_seed_mean_error": 1.697212252020836,
              "oracle_best_mean_error": 1.6369523051977157,
              "improvement_over_seed0": 0.06140663933753965,
              "gap_to_oracle": 0.005258623600006063,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5238884978294372
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8497466255839055
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1721886408805846
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3858685497917347
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6968660296916962
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4058186292648314,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5101625147395663,
                  "rejected_mean_error": 3.3771976642608643,
                  "gap_rejected_minus_accepted": 1.867035149521298
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9250687658786774,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3852591717510365,
                  "rejected_mean_error": 2.629695505379869,
                  "gap_rejected_minus_accepted": 1.2444363336288324
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6283860802650452,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1721886408805846,
                  "rejected_mean_error": 2.2215434185028076,
                  "gap_rejected_minus_accepted": 1.049354777622223
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2076743245124817,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8513920667072454,
                  "rejected_mean_error": 1.9792922307740153,
                  "gap_rejected_minus_accepted": 1.1279001640667699
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4187111854553223,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5159807524416182,
                  "rejected_mean_error": 3.3923489093780517,
                  "gap_rejected_minus_accepted": 1.8763681569364334
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9469906389713287,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3886853043727059,
                  "rejected_mean_error": 2.6384165097796726,
                  "gap_rejected_minus_accepted": 1.2497312054069667
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6303812861442566,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1709086153507233,
                  "rejected_mean_error": 2.2363265209197998,
                  "gap_rejected_minus_accepted": 1.0654179055690765
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.226018875837326,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8482114800385067,
                  "rejected_mean_error": 1.991802506905826,
                  "gap_rejected_minus_accepted": 1.1435910268673193
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9530027819736548,
              "spearman": 0.9553795261479593,
              "auroc_top30_bad": 0.9915085714285715,
              "mae": 0.22459931503161787,
              "mse": 0.1337702174467355,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.948,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7933817144196814,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.279070478618145
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.27277742340564726
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5507981228351593
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9304116514523824
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3812216915369033
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9330411967785837,
              "spearman": 0.9793137347287904,
              "auroc_top30_worst": 0.9959954285714285,
              "pairwise_seed_ranking": 0.8728,
              "predicted_best_mean_error": 1.9669439442157746,
              "seed0_mean_error": 2.0495302921533582,
              "random_seed_mean_error": 2.02936255300045,
              "oracle_best_mean_error": 1.9609006407260894,
              "improvement_over_seed0": 0.08258634793758368,
              "gap_to_oracle": 0.006043303489685181,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7316989717483521
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0826869114087179
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3485813974380494
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.556169320525391
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.027466819000244
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.796671795845032,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.83101032977634,
                  "rejected_mean_error": 3.7955752220153807,
                  "gap_rejected_minus_accepted": 1.9645648922390406
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1812100410461426,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5553800477035018,
                  "rejected_mean_error": 3.440710604000396,
                  "gap_rejected_minus_accepted": 1.8853305562968943
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8347597122192383,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3485813974380494,
                  "rejected_mean_error": 2.706352240562439,
                  "gap_rejected_minus_accepted": 1.3577708431243898
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4397253096103668,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0836974340505874,
                  "rejected_mean_error": 2.3427280970037048,
                  "gap_rejected_minus_accepted": 1.2590306629531174
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8026750564575194,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8468317144446902,
                  "rejected_mean_error": 3.873817491531372,
                  "gap_rejected_minus_accepted": 2.026985777086682
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2115655541419983,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5721385703686086,
                  "rejected_mean_error": 3.4665501647525363,
                  "gap_rejected_minus_accepted": 1.8944115943839277
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8736160397529602,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3603744223117828,
                  "rejected_mean_error": 2.738686161994934,
                  "gap_rejected_minus_accepted": 1.378311739683151
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4495160281658173,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.08850691668571,
                  "rejected_mean_error": 2.3732975255996784,
                  "gap_rejected_minus_accepted": 1.2847906089139685
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9741912771717167,
              "spearman": 0.9571517977883705,
              "auroc_top30_bad": 0.9874285714285714,
              "mae": 0.13789294635616242,
              "mse": 0.0438041125230673,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.896,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7726795281249624,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.24129283052682876
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24711063611507417
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5003079702973365
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8668913334290187
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9727543733801234,
              "spearman": 0.9675731944788445,
              "auroc_top30_worst": 0.9587108571428572,
              "pairwise_seed_ranking": 0.8896,
              "predicted_best_mean_error": 1.6669973421096802,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.03959275257587436,
              "gap_to_oracle": 0.005148406147956974,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6304194691181183
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9515584245897256
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.222009592485428
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4299412112055556
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.605460572242737,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.557425257285436,
                  "rejected_mean_error": 3.172852836608887,
                  "gap_rejected_minus_accepted": 1.615427579323451
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0122793912887573,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4293583130569316,
                  "rejected_mean_error": 2.5859465804724646,
                  "gap_rejected_minus_accepted": 1.156588267415533
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6907240748405457,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.222009592485428,
                  "rejected_mean_error": 2.2159264379501344,
                  "gap_rejected_minus_accepted": 0.9939168454647065
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3032159209251404,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9527776417450402,
                  "rejected_mean_error": 1.9749099436030189,
                  "gap_rejected_minus_accepted": 1.0221323018579787
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.567812919616699,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5484711288081274,
                  "rejected_mean_error": 3.1296607875823974,
                  "gap_rejected_minus_accepted": 1.58118965877427
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9909426867961884,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.421185797070437,
                  "rejected_mean_error": 2.553742533638364,
                  "gap_rejected_minus_accepted": 1.132556736567927
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6680321097373962,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2118004925251007,
                  "rejected_mean_error": 2.201379696846008,
                  "gap_rejected_minus_accepted": 0.9895792043209075
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2965834140777588,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9283837898383065,
                  "rejected_mean_error": 1.9687665503292797,
                  "gap_rejected_minus_accepted": 1.0403827604909732
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
        "best_epoch": 66,
        "best_calib_loss": 0.02073136903345585,
        "train_time_sec": 41.69432020187378,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9989476717420792,
              "spearman": 0.9950901609800366,
              "auroc_top30_bad": 0.9996400476190476,
              "mae": 0.027230233913182748,
              "mse": 0.0015399399104014647,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.968,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7256197622798002,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.015945649217697793
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.08101289152982645
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.297494455730333
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6482534771518006
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0237238207039308
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9992380529558493,
              "spearman": 0.9989577927583115,
              "auroc_top30_worst": 0.9992598095238096,
              "pairwise_seed_ranking": 0.9601,
              "predicted_best_mean_error": 1.425331406801939,
              "seed0_mean_error": 1.4966771293878556,
              "random_seed_mean_error": 1.4850968795716764,
              "oracle_best_mean_error": 1.42449176928401,
              "improvement_over_seed0": 0.07134572258591665,
              "gap_to_oracle": 0.0008396375179289262,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4602173867225647
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6607334613800049
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9422881784915924
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.176906129137675
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4844832009077071
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2951679944992067,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3220147106117672,
                  "rejected_mean_error": 2.946699613571167,
                  "gap_rejected_minus_accepted": 1.6246849029593997
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8507049679756165,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.176906129137675,
                  "rejected_mean_error": 2.407214416217804,
                  "gap_rejected_minus_accepted": 1.230308287080129
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4536666870117188,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9422881784915924,
                  "rejected_mean_error": 2.026678223323822,
                  "gap_rejected_minus_accepted": 1.0843900448322297
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9930074363946915,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6607334613800049,
                  "rejected_mean_error": 1.7590664474169413,
                  "gap_rejected_minus_accepted": 1.0983329860369364
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.331822228431702,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3334037477440304,
                  "rejected_mean_error": 2.9661375641822816,
                  "gap_rejected_minus_accepted": 1.6327338164382512
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8828707933425903,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1870013387997944,
                  "rejected_mean_error": 2.4257045011520386,
                  "gap_rejected_minus_accepted": 1.2387031623522442
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.46562659740448,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9478875439167023,
                  "rejected_mean_error": 2.0454667148590087,
                  "gap_rejected_minus_accepted": 1.0975791709423064
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0033565163612366,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6616293456554413,
                  "rejected_mean_error": 1.7750263906319936,
                  "gap_rejected_minus_accepted": 1.1133970449765522
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9701870038254954,
              "spearman": 0.9469058365286712,
              "auroc_top30_bad": 0.9955733333333334,
              "mae": 0.15948976185289213,
              "mse": 0.06425594829387694,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.928,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7596780834837994,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.32860294526815415
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.300362566280365
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5056350445866585
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8622114107847214
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.219241336542368
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9928759978044104,
              "spearman": 0.9892362826472211,
              "auroc_top30_worst": 0.994328380952381,
              "pairwise_seed_ranking": 0.9032,
              "predicted_best_mean_error": 1.640037900209427,
              "seed0_mean_error": 1.7036175681352614,
              "random_seed_mean_error": 1.697212252020836,
              "oracle_best_mean_error": 1.6369523051977157,
              "improvement_over_seed0": 0.06357966792583447,
              "gap_to_oracle": 0.0030855950117112396,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5249021620750427
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8512567417361797
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.172148985004425
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3859612418771552
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6968660296916962
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3629468679428105,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5099624573919508,
                  "rejected_mean_error": 3.3789981803894045,
                  "gap_rejected_minus_accepted": 1.8690357229974537
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9015636146068573,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.38535409885893,
                  "rejected_mean_error": 2.6294113306191784,
                  "gap_rejected_minus_accepted": 1.2440572317602485
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5720521807670593,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.172148985004425,
                  "rejected_mean_error": 2.2215830743789673,
                  "gap_rejected_minus_accepted": 1.0494340893745422
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1658330261707306,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8529224725196156,
                  "rejected_mean_error": 1.9787810066339173,
                  "gap_rejected_minus_accepted": 1.1258585341143017
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.381777286529541,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5150418378247155,
                  "rejected_mean_error": 3.4007991409301757,
                  "gap_rejected_minus_accepted": 1.8857573031054602
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9267667531967163,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3899586036562281,
                  "rejected_mean_error": 2.6346370341285827,
                  "gap_rejected_minus_accepted": 1.2446784304723546
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5733473896980286,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1710061361789703,
                  "rejected_mean_error": 2.236229000091553,
                  "gap_rejected_minus_accepted": 1.0652228639125825
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1800962686538696,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8462608016672588,
                  "rejected_mean_error": 1.992459687319669,
                  "gap_rejected_minus_accepted": 1.1461988856524101
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9653741746371691,
              "spearman": 0.9603746437578443,
              "auroc_top30_bad": 0.9947161904761905,
              "mae": 0.20888039308437145,
              "mse": 0.10777754265127915,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.948,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.810069154407375,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2815617919564247
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.27795935323238374
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5481007562160491
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9283637476285299
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3812216915369033
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9650020727957723,
              "spearman": 0.9865647407134341,
              "auroc_top30_worst": 0.9972114285714285,
              "pairwise_seed_ranking": 0.9104,
              "predicted_best_mean_error": 1.9637903583049774,
              "seed0_mean_error": 2.0495302921533582,
              "random_seed_mean_error": 2.02936255300045,
              "oracle_best_mean_error": 1.9609006407260894,
              "improvement_over_seed0": 0.08573993384838086,
              "gap_to_oracle": 0.002889717578888007,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7169030680656433
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0767607975464601
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.350587783241272
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5553709512580431
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.027466819000244
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.901611256599426,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8162417822943793,
                  "rejected_mean_error": 3.928492149353027,
                  "gap_rejected_minus_accepted": 2.112250367058648
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.200566589832306,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5545808263878431,
                  "rejected_mean_error": 3.443103161101905,
                  "gap_rejected_minus_accepted": 1.8885223347140618
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8058778047561646,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.350587783241272,
                  "rejected_mean_error": 2.7043458547592163,
                  "gap_rejected_minus_accepted": 1.3537580715179443
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3413230776786804,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0777349757691161,
                  "rejected_mean_error": 2.3447198253303863,
                  "gap_rejected_minus_accepted": 1.26698484956127
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9281365156173704,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8343660954634349,
                  "rejected_mean_error": 3.986008062362671,
                  "gap_rejected_minus_accepted": 2.151641966899236
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.267064094543457,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5721729816918704,
                  "rejected_mean_error": 3.4664480232057118,
                  "gap_rejected_minus_accepted": 1.8942750415138414
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8337832689285278,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3604948103427887,
                  "rejected_mean_error": 2.7385657739639284,
                  "gap_rejected_minus_accepted": 1.3780709636211397
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3861263394355774,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.081970722429336,
                  "rejected_mean_error": 2.375499558958778,
                  "gap_rejected_minus_accepted": 1.293528836529442
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9754238415283076,
              "spearman": 0.9581135668775985,
              "auroc_top30_bad": 0.991704380952381,
              "mae": 0.15557600317928008,
              "mse": 0.050310198638610956,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.912,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7555290248513272,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2698574423789978
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2675716370344162
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.500694048178196
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8618974890152613
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9827013301754159,
              "spearman": 0.9773135235286552,
              "auroc_top30_worst": 0.977398857142857,
              "pairwise_seed_ranking": 0.9164,
              "predicted_best_mean_error": 1.663619591474533,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.04297050321102147,
              "gap_to_oracle": 0.00177065551280986,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6301752898693085
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9523394425901083
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2219094465732574
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4245199440702447
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4330289840698245,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5594857153627608,
                  "rejected_mean_error": 3.1543087139129637,
                  "gap_rejected_minus_accepted": 1.594822998550203
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9023333489894867,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4236535128114571,
                  "rejected_mean_error": 2.603024528811153,
                  "gap_rejected_minus_accepted": 1.179371015999696
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5704662203788757,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2219094465732574,
                  "rejected_mean_error": 2.2160265838623046,
                  "gap_rejected_minus_accepted": 0.9941171372890472
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2359547913074493,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9537069143388218,
                  "rejected_mean_error": 1.9745995249030683,
                  "gap_rejected_minus_accepted": 1.0208926105642466
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3691262006759644,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5499383069409265,
                  "rejected_mean_error": 3.116456184387207,
                  "gap_rejected_minus_accepted": 1.5665178774462807
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8814173340797424,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.411354307981736,
                  "rejected_mean_error": 2.582924890139746,
                  "gap_rejected_minus_accepted": 1.1715705821580102
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5897453427314758,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.206633498430252,
                  "rejected_mean_error": 2.206546690940857,
                  "gap_rejected_minus_accepted": 0.9999131925106048
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2198593318462372,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9284014309209491,
                  "rejected_mean_error": 1.9687606070768386,
                  "gap_rejected_minus_accepted": 1.0403591761558895
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
        "best_epoch": 41,
        "best_calib_loss": 0.01755034551024437,
        "train_time_sec": 29.23209834098816,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9991336556279625,
              "spearman": 0.9932299779455337,
              "auroc_top30_bad": 0.999808,
              "mae": 0.033437563593662345,
              "mse": 0.0021020672555051496,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.979,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7452220489752517,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.023922030063346027
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.08059074683669024
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.2973175986641785
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6481398996587687
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0237238207039308
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9995388458786871,
              "spearman": 0.9994994189239766,
              "auroc_top30_worst": 0.9996689523809523,
              "pairwise_seed_ranking": 0.941,
              "predicted_best_mean_error": 1.4254654721617699,
              "seed0_mean_error": 1.4966771293878556,
              "random_seed_mean_error": 1.4850968795716764,
              "oracle_best_mean_error": 1.42449176928401,
              "improvement_over_seed0": 0.07121165722608569,
              "gap_to_oracle": 0.0009737028777598855,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.45943061375617983
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6604447115898132
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9420403017520904
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1768090370814006
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4844832009077071
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3591981410980227,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3219294628302256,
                  "rejected_mean_error": 2.9474668436050413,
                  "gap_rejected_minus_accepted": 1.6255373807748157
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8842532336711884,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1768090370814006,
                  "rejected_mean_error": 2.407505692386627,
                  "gap_rejected_minus_accepted": 1.2306966553052265
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4884684085845947,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9420403017520904,
                  "rejected_mean_error": 2.026926100063324,
                  "gap_rejected_minus_accepted": 1.0848857983112334
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0086736381053925,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6604447115898132,
                  "rejected_mean_error": 1.7591626973470051,
                  "gap_rejected_minus_accepted": 1.098717985757192
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4031516313552856,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3333696446153853,
                  "rejected_mean_error": 2.966444492340088,
                  "gap_rejected_minus_accepted": 1.6330748477247026
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9053348898887634,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1870993785858155,
                  "rejected_mean_error": 2.425410381793976,
                  "gap_rejected_minus_accepted": 1.2383110032081603
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4901628494262695,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9478040363788605,
                  "rejected_mean_error": 2.0455502223968507,
                  "gap_rejected_minus_accepted": 1.0977461860179902
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0191533267498016,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6613022232055664,
                  "rejected_mean_error": 1.7751354314486185,
                  "gap_rejected_minus_accepted": 1.1138332082430522
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9747296925402749,
              "spearman": 0.9599537171706681,
              "auroc_top30_bad": 0.995104,
              "mae": 0.14067520570422057,
              "mse": 0.052488363137985446,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.964,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7680733233095682,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.20663167560100557
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2665781690835953
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.505193011868
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8625168225685755
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.219241336542368
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9923363576503414,
              "spearman": 0.9871288831544853,
              "auroc_top30_worst": 0.9912289523809523,
              "pairwise_seed_ranking": 0.9016,
              "predicted_best_mean_error": 1.6389132957458497,
              "seed0_mean_error": 1.7036175681352614,
              "random_seed_mean_error": 1.697212252020836,
              "oracle_best_mean_error": 1.6369523051977157,
              "improvement_over_seed0": 0.06470427238941179,
              "gap_to_oracle": 0.001960990548133923,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5246461105346679
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8502771046299201
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1719021958351135
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3870229097698796
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6968660296916962
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3506381988525393,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5103842086262174,
                  "rejected_mean_error": 3.3752024192810057,
                  "gap_rejected_minus_accepted": 1.8648182106547884
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9376499950885773,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3863924925584294,
                  "rejected_mean_error": 2.6263027846241913,
                  "gap_rejected_minus_accepted": 1.2399102920657619
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5965152382850647,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1719021958351135,
                  "rejected_mean_error": 2.2218298635482787,
                  "gap_rejected_minus_accepted": 1.0499276677131653
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.199610710144043,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8521793637031945,
                  "rejected_mean_error": 1.9790292382876418,
                  "gap_rejected_minus_accepted": 1.1268498745844473
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3585695028305054,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5154084069199032,
                  "rejected_mean_error": 3.3975000190734863,
                  "gap_rejected_minus_accepted": 1.8820916121535831
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9557990729808807,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3890920247942369,
                  "rejected_mean_error": 2.6372092602744934,
                  "gap_rejected_minus_accepted": 1.2481172354802565
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.607535183429718,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1706003839969634,
                  "rejected_mean_error": 2.2366347522735595,
                  "gap_rejected_minus_accepted": 1.066034368276596
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2198962569236755,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8479464494046711,
                  "rejected_mean_error": 1.9918917953011823,
                  "gap_rejected_minus_accepted": 1.1439453458965112
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9596122092954713,
              "spearman": 0.9641925761047083,
              "auroc_top30_bad": 0.9903740952380952,
              "mae": 0.20503899659567978,
              "mse": 0.11067077507527988,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.968,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8190461793144964,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2067212148308754
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2672767595052719
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5481497983455658
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9300688892682394
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3812216915369033
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9486337673299752,
              "spearman": 0.9813864636073368,
              "auroc_top30_worst": 0.9936944761904762,
              "pairwise_seed_ranking": 0.904,
              "predicted_best_mean_error": 1.9635061688423157,
              "seed0_mean_error": 2.0495302921533582,
              "random_seed_mean_error": 2.02936255300045,
              "oracle_best_mean_error": 1.9609006407260894,
              "improvement_over_seed0": 0.08602412331104259,
              "gap_to_oracle": 0.0026055281162262744,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7136566367149353
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.078926493342106
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3545933933258056
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5567006706428934
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.027466819000244
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.858406591415405,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8183837295108372,
                  "rejected_mean_error": 3.9092146244049073,
                  "gap_rejected_minus_accepted": 2.0908308948940704
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3062158823013306,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5559619406880285,
                  "rejected_mean_error": 3.4389686432128515,
                  "gap_rejected_minus_accepted": 1.883006702524823
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8666792511940002,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3545933933258056,
                  "rejected_mean_error": 2.7003402446746825,
                  "gap_rejected_minus_accepted": 1.3457468513488768
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4077246189117432,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0799403476258056,
                  "rejected_mean_error": 2.343983132276871,
                  "gap_rejected_minus_accepted": 1.2640427846510653
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.887064218521118,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8297707585493723,
                  "rejected_mean_error": 4.027366094589233,
                  "gap_rejected_minus_accepted": 2.1975953360398606
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.365500271320343,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5724587881947583,
                  "rejected_mean_error": 3.465599676919362,
                  "gap_rejected_minus_accepted": 1.8931408887246037
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8894917368888855,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.368623297929764,
                  "rejected_mean_error": 2.730437286376953,
                  "gap_rejected_minus_accepted": 1.3618139884471891
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4153706729412079,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0826025297717443,
                  "rejected_mean_error": 2.375286704078715,
                  "gap_rejected_minus_accepted": 1.2926841743069706
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.977923818424814,
              "spearman": 0.9680459980119265,
              "auroc_top30_bad": 0.9898956190476191,
              "mae": 0.12776761628082023,
              "mse": 0.03644726539064335,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.98,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7563017324447927,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1458077586889267
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.24490825781822204
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5010879920601845
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8623699778000514
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.977910487988086,
              "spearman": 0.9715566840042777,
              "auroc_top30_worst": 0.9703009523809524,
              "pairwise_seed_ranking": 0.8936,
              "predicted_best_mean_error": 1.664057432293892,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.042532662391662646,
              "gap_to_oracle": 0.0022084963321686857,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6326179001331329
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9542457095514505
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.221959836626053
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.429957143946497
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4493358135223393,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.559523860639996,
                  "rejected_mean_error": 3.153965406417847,
                  "gap_rejected_minus_accepted": 1.594441545777851
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0102603435516357,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.429376846984458,
                  "rejected_mean_error": 2.585891097117537,
                  "gap_rejected_minus_accepted": 1.1565142501330787
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6633428931236267,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.221959836626053,
                  "rejected_mean_error": 2.2159761938095093,
                  "gap_rejected_minus_accepted": 0.9940163571834564
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3153665363788605,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9551055527533205,
                  "rejected_mean_error": 1.974132316980189,
                  "gap_rejected_minus_accepted": 1.0190267642268684
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4421541690826416,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.55052374958992,
                  "rejected_mean_error": 3.1111872005462646,
                  "gap_rejected_minus_accepted": 1.5606634509563446
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9708150029182434,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4212943062106556,
                  "rejected_mean_error": 2.553420450952318,
                  "gap_rejected_minus_accepted": 1.1321261447416626
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6828444600105286,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.208868767976761,
                  "rejected_mean_error": 2.204311421394348,
                  "gap_rejected_minus_accepted": 0.9954426534175871
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3203837275505066,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9305010698144398,
                  "rejected_mean_error": 1.9680532421020263,
                  "gap_rejected_minus_accepted": 1.0375521722875864
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
        "best_epoch": 5,
        "best_calib_loss": 0.12348035722970963,
        "train_time_sec": 10.606531620025635,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9513068306282655,
              "spearman": 0.8888517025134354,
              "auroc_top30_bad": 0.9889271666666667,
              "mae": 0.185086838362598,
              "mse": 0.06722491111926554,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5934003553176397,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.15304251161217688
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.1409345763862133
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.0686816844522953
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.2247966069718202
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.5718854881331324
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9728639897719075,
              "spearman": 0.9638521342412179,
              "auroc_top30_worst": 0.985862666666667,
              "pairwise_seed_ranking": 0.7309,
              "predicted_best_mean_error": 0.9374339309632778,
              "seed0_mean_error": 0.9900609410107136,
              "random_seed_mean_error": 0.978739710867405,
              "oracle_best_mean_error": 0.9180251259803772,
              "improvement_over_seed0": 0.05262701004743586,
              "gap_to_oracle": 0.01940880498290054,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0637929453253746
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20034129447937013
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.45165263506174086
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6772025614500046
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.9780684807360173
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.7812842845916748,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.8182834235628446,
                  "rejected_mean_error": 2.416133995294571,
                  "gap_rejected_minus_accepted": 1.5978505717317266
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3876019418239594,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.6772025614500046,
                  "rejected_mean_error": 1.8806662385940551,
                  "gap_rejected_minus_accepted": 1.2034636771440506
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9700947999954224,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.45165263506174086,
                  "rejected_mean_error": 1.5044843264102936,
                  "gap_rejected_minus_accepted": 1.0528316913485527
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.525750920176506,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.20034129447937013,
                  "rejected_mean_error": 1.2373108761548997,
                  "gap_rejected_minus_accepted": 1.0369695816755296
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.847927737236023,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8297584910194079,
                  "rejected_mean_error": 2.4327829909324645,
                  "gap_rejected_minus_accepted": 1.6030244999130567
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4052604734897614,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.686833577354749,
                  "rejected_mean_error": 1.8997430319786073,
                  "gap_rejected_minus_accepted": 1.2129094546238584
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9873870015144348,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.45560857027769086,
                  "rejected_mean_error": 1.5245133117437362,
                  "gap_rejected_minus_accepted": 1.0689047414660453
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5432086735963821,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.1961833026409149,
                  "rejected_mean_error": 1.2546868204673132,
                  "gap_rejected_minus_accepted": 1.0585035178263982
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8385631330154365,
              "spearman": 0.7748626568139086,
              "auroc_top30_bad": 0.933623619047619,
              "mae": 0.6039365179188335,
              "mse": 0.5262248102724923,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5828940726700896,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3814139823615551
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.49817948600053785
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5459460391759873
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8525434924840927
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1788091871500015
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8168883067287577,
              "spearman": 0.7323707460932776,
              "auroc_top30_worst": 0.8833066666666666,
              "pairwise_seed_ranking": 0.6228,
              "predicted_best_mean_error": 1.6330545630455018,
              "seed0_mean_error": 1.6623953195810317,
              "random_seed_mean_error": 1.6560072766542435,
              "oracle_best_mean_error": 1.595594585776329,
              "improvement_over_seed0": 0.02934075653552992,
              "gap_to_oracle": 0.03745997726917283,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9444529378414154
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9910793678882794
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2417994331359863
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3616700744959338
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6556154248714448
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5470898985862733,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.480417825433943,
                  "rejected_mean_error": 3.23239381980896,
                  "gap_rejected_minus_accepted": 1.7519759943750168
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.1759306490421295,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3611422815979355,
                  "rejected_mean_error": 2.5371532371630683,
                  "gap_rejected_minus_accepted": 1.1760109555651328
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9838716685771942,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2417994331359863,
                  "rejected_mean_error": 2.069431416606903,
                  "gap_rejected_minus_accepted": 0.8276319834709167
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5477458834648132,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9920908102212241,
                  "rejected_mean_error": 1.8772623879296293,
                  "gap_rejected_minus_accepted": 0.8851715777084052
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.5256560087203979,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4860197524229686,
                  "rejected_mean_error": 3.249775424003601,
                  "gap_rejected_minus_accepted": 1.7637556715806326
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.1907102167606354,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3615854272549166,
                  "rejected_mean_error": 2.5552754761680725,
                  "gap_rejected_minus_accepted": 1.1936900489131559
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9896981716156006,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2386550080776215,
                  "rejected_mean_error": 2.086135631084442,
                  "gap_rejected_minus_accepted": 0.8474806230068206
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5775700509548187,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9724469170683906,
                  "rejected_mean_error": 1.8948378295184456,
                  "gap_rejected_minus_accepted": 0.922390912450055
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.7810485655836464,
              "spearman": 0.8065726426748123,
              "auroc_top30_bad": 0.9044327619047619,
              "mae": 0.6463071901504797,
              "mse": 0.8044611213226659,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.472,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.582786568566521,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3569796888232231
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.36339238657951356
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5892137740254402
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9259890940904617
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3014900189995766
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.5983376869346141,
              "spearman": 0.6390044040988188,
              "auroc_top30_worst": 0.7348662857142857,
              "pairwise_seed_ranking": 0.6712,
              "predicted_best_mean_error": 1.9232308744192124,
              "seed0_mean_error": 1.9666107931137085,
              "random_seed_mean_error": 1.9462949228286743,
              "oracle_best_mean_error": 1.8785797675848008,
              "improvement_over_seed0": 0.04337991869449609,
              "gap_to_oracle": 0.044651106834411536,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.2545170240402221
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.292028152789825
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.4784527048110963
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6157786921143278
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9445513899803162
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8606534957885743,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8065773293177287,
                  "rejected_mean_error": 3.1863179359436034,
                  "gap_rejected_minus_accepted": 1.3797406066258746
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5663060545921326,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.6151808853973828,
                  "rejected_mean_error": 2.9305582998659663,
                  "gap_rejected_minus_accepted": 1.3153774144685835
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1011723279953003,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.4784527048110963,
                  "rejected_mean_error": 2.4106500751495363,
                  "gap_rejected_minus_accepted": 0.9321973703384401
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6761743277311325,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.2910269413131494,
                  "rejected_mean_error": 2.16285784935366,
                  "gap_rejected_minus_accepted": 0.8718309080405107
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9004988074302673,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.817152738041348,
                  "rejected_mean_error": 3.3117332887649535,
                  "gap_rejected_minus_accepted": 1.4945805507236056
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5793738961219788,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6201675830677869,
                  "rejected_mean_error": 2.9949422261071583,
                  "gap_rejected_minus_accepted": 1.3747746430393715
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1200759410858154,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.47476655292511,
                  "rejected_mean_error": 2.458455033302307,
                  "gap_rejected_minus_accepted": 0.983688480377197
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6870756894350052,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.2920779595299372,
                  "rejected_mean_error": 2.1938598226098454,
                  "gap_rejected_minus_accepted": 0.9017818630799082
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8791272182071956,
              "spearman": 0.8475193363535387,
              "auroc_top30_bad": 0.9304784761904762,
              "mae": 0.5259088433299606,
              "mse": 0.40302380303449775,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6578794278848477,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.42398127645254136
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.42242498726844785
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5453145342946053
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9000175438245137
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8477967916416091,
              "spearman": 0.7809690676282034,
              "auroc_top30_worst": 0.8538544761904762,
              "pairwise_seed_ranking": 0.6152,
              "predicted_best_mean_error": 1.6964983946084977,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.010091700077056842,
              "gap_to_oracle": 0.03464945864677449,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7334303290843963
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0526128962444954
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2964161072254181
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4852191962476478
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3433617115020766,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.56540660405159,
                  "rejected_mean_error": 3.101020715713501,
                  "gap_rejected_minus_accepted": 1.535614111661911
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.546562910079956,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4846908407824526,
                  "rejected_mean_error": 2.420302559773381,
                  "gap_rejected_minus_accepted": 0.9356117189909283
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1965031027793884,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2964161072254181,
                  "rejected_mean_error": 2.141519923210144,
                  "gap_rejected_minus_accepted": 0.845103815984726
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.4867027476429939,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0540060712316166,
                  "rejected_mean_error": 1.9410951107008863,
                  "gap_rejected_minus_accepted": 0.8870890394692696
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.294564437866211,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5576096175776588,
                  "rejected_mean_error": 3.047414388656616,
                  "gap_rejected_minus_accepted": 1.4898047710789573
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5066563487052917,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4877799145359407,
                  "rejected_mean_error": 2.3560742802090116,
                  "gap_rejected_minus_accepted": 0.8682943656730708
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2320004105567932,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2838961107730866,
                  "rejected_mean_error": 2.1292840785980225,
                  "gap_rejected_minus_accepted": 0.8453879678249359
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5120957791805267,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.014628244297845,
                  "rejected_mean_error": 1.9397109319819485,
                  "gap_rejected_minus_accepted": 0.9250826876841036
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
        "best_epoch": 70,
        "best_calib_loss": 0.07580261677503586,
        "train_time_sec": 35.30931758880615,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9890357606994851,
              "spearman": 0.9819430463725638,
              "auroc_top30_bad": 0.9998721904761905,
              "mae": 0.10987064914817893,
              "mse": 0.029515311395812302,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.928,
              "expert_lt_simvla_seed0": 0.995,
              "same_context_pred_std": 0.5771135943333897,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.3037542953938246
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.3040938158452511
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.09582493056356907
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.2205955127298832
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.5718854881331324
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9985546065820841,
              "spearman": 0.9994371309774447,
              "auroc_top30_worst": 0.999551142857143,
              "pairwise_seed_ranking": 0.9332,
              "predicted_best_mean_error": 0.9198446012437343,
              "seed0_mean_error": 0.9900609410107136,
              "random_seed_mean_error": 0.978739710867405,
              "oracle_best_mean_error": 0.9180251259803772,
              "improvement_over_seed0": 0.07021633976697927,
              "gap_to_oracle": 0.0018194752633571287,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.06073542159795761
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.15644456820487976
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4414939898610115
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6744590631246566
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.9780684807360173
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8220395803451543,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.8172164400219917,
                  "rejected_mean_error": 2.4257368471622467,
                  "gap_rejected_minus_accepted": 1.608520407140255
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3825987875461578,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.6744590631246566,
                  "rejected_mean_error": 1.8888967335700988,
                  "gap_rejected_minus_accepted": 1.214437670445442
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9720228314399719,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.4414939898610115,
                  "rejected_mean_error": 1.514642971611023,
                  "gap_rejected_minus_accepted": 1.0731489817500115
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5184021294116974,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.15644456820487976,
                  "rejected_mean_error": 1.2519431182463965,
                  "gap_rejected_minus_accepted": 1.0954985500415166
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.874934196472168,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8282464283373621,
                  "rejected_mean_error": 2.446391555070877,
                  "gap_rejected_minus_accepted": 1.618145126733515
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.400398999452591,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.6843204999367396,
                  "rejected_mean_error": 1.9072822642326355,
                  "gap_rejected_minus_accepted": 1.2229617642958959
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9792302548885345,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.44757111138105393,
                  "rejected_mean_error": 1.5325507706403732,
                  "gap_rejected_minus_accepted": 1.0849796592593193
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5266249775886536,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.15795882833004,
                  "rejected_mean_error": 1.2674283119042715,
                  "gap_rejected_minus_accepted": 1.1094694835742316
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.971850174785003,
              "spearman": 0.9638908709638149,
              "auroc_top30_bad": 0.9872731428571428,
              "mae": 0.41292471487126314,
              "mse": 0.21521956071744144,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.908,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.61969380473385,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15226305755972863
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.14377612109184265
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.44887720313072205
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8145693516731263
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1788091871500015
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9812466045644141,
              "spearman": 0.9789642392091131,
              "auroc_top30_worst": 0.9901775238095237,
              "pairwise_seed_ranking": 0.8896,
              "predicted_best_mean_error": 1.5992776478528976,
              "seed0_mean_error": 1.6623953195810317,
              "random_seed_mean_error": 1.6560072766542435,
              "oracle_best_mean_error": 1.595594585776329,
              "improvement_over_seed0": 0.0631176717281341,
              "gap_to_oracle": 0.003683062076568655,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.47217795372009275
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7473799697099588
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.091740500164032
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3343300499768653
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6556154248714448
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8392973303794862,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4655284700923497,
                  "rejected_mean_error": 3.366398017883301,
                  "gap_rejected_minus_accepted": 1.9008695477909512
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4434950947761536,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3337153345823543,
                  "rejected_mean_error": 2.6192588261522043,
                  "gap_rejected_minus_accepted": 1.28554349156985
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.17509126663208,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.091740500164032,
                  "rejected_mean_error": 2.2194903495788574,
                  "gap_rejected_minus_accepted": 1.1277498494148255
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7401136755943298,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7479011768731065,
                  "rejected_mean_error": 1.9588326710010924,
                  "gap_rejected_minus_accepted": 1.2109314941279858
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8507502555847168,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.471998416715198,
                  "rejected_mean_error": 3.375967445373535,
                  "gap_rejected_minus_accepted": 1.903969028658337
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4631039798259735,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3352935832133268,
                  "rejected_mean_error": 2.6333163465772356,
                  "gap_rejected_minus_accepted": 1.2980227633639088
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1791173219680786,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0907723467350006,
                  "rejected_mean_error": 2.234018292427063,
                  "gap_rejected_minus_accepted": 1.1432459456920623
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7474058270454407,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7531562821259574,
                  "rejected_mean_error": 1.9687164926273937,
                  "gap_rejected_minus_accepted": 1.2155602105014363
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9449140125460503,
              "spearman": 0.9553341850530743,
              "auroc_top30_bad": 0.9883260952380952,
              "mae": 0.4503830149479792,
              "mse": 0.3245951672669597,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.952,
              "expert_lt_simvla_seed0": 0.988,
              "same_context_pred_std": 0.681753436299374,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.14744961476325988
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.17609393813610077
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4550969197511673
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8570745066483816
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3014900189995766
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9082078454819896,
              "spearman": 0.9752126612561034,
              "auroc_top30_worst": 0.9962666666666666,
              "pairwise_seed_ranking": 0.8864,
              "predicted_best_mean_error": 1.8835023703575133,
              "seed0_mean_error": 1.9666107931137085,
              "random_seed_mean_error": 1.9462949228286743,
              "oracle_best_mean_error": 1.8785797675848008,
              "improvement_over_seed0": 0.08310842275619512,
              "gap_to_oracle": 0.004922602772712503,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5500788307189941
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9241178058660947
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2678342575073243
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5018208889818903
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9445513899803162
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.379240202903748,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7983399193021987,
                  "rejected_mean_error": 3.260454626083374,
                  "gap_rejected_minus_accepted": 1.4621147067811755
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7250783443450928,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5010235893560957,
                  "rejected_mean_error": 3.27230074839851,
                  "gap_rejected_minus_accepted": 1.7712771590424141
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.376029133796692,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2678342575073243,
                  "rejected_mean_error": 2.6212685224533083,
                  "gap_rejected_minus_accepted": 1.353434264945984
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0197782516479492,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9262054846309625,
                  "rejected_mean_error": 2.284724568608222,
                  "gap_rejected_minus_accepted": 1.3585190839772596
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3914122343063355,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.816983224021064,
                  "rejected_mean_error": 3.3132589149475096,
                  "gap_rejected_minus_accepted": 1.4962756909264456
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7535064220428467,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5176362927584726,
                  "rejected_mean_error": 3.2992811354379805,
                  "gap_rejected_minus_accepted": 1.781644842679508
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4213237166404724,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2799052543640137,
                  "rejected_mean_error": 2.653316331863403,
                  "gap_rejected_minus_accepted": 1.3734110774993895
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0375069975852966,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9295908685714479,
                  "rejected_mean_error": 2.315981142023668,
                  "gap_rejected_minus_accepted": 1.38639027345222
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9677272439279658,
              "spearman": 0.9769142294210931,
              "auroc_top30_bad": 0.9898308571428571,
              "mae": 0.41459391892902203,
              "mse": 0.2095363316500826,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.936,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.6551037215644108,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15203600573539733
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19997733271121979
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5002363155007362
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8652215675115585
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9714165159711521,
              "spearman": 0.9755770928493396,
              "auroc_top30_worst": 0.9655527619047619,
              "pairwise_seed_ranking": 0.894,
              "predicted_best_mean_error": 1.6659857680797576,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.04060432660579694,
              "gap_to_oracle": 0.004136832118034395,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.629839236497879
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9503894074796102
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.220556422472
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4271818132860574
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.054682850837708,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5596854855484432,
                  "rejected_mean_error": 3.1525107822418215,
                  "gap_rejected_minus_accepted": 1.5928252966933782
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5016624331474304,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4267795831760195,
                  "rejected_mean_error": 2.5936662926079745,
                  "gap_rejected_minus_accepted": 1.166886709431955
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2133391499519348,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.220556422472,
                  "rejected_mean_error": 2.217379607963562,
                  "gap_rejected_minus_accepted": 0.9968231854915619
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8346292972564697,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9518018958096306,
                  "rejected_mean_error": 1.97523588648219,
                  "gap_rejected_minus_accepted": 1.0234339906725594
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9942176222801207,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5507535596688589,
                  "rejected_mean_error": 3.1091189098358156,
                  "gap_rejected_minus_accepted": 1.5583653501669568
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4852731823921204,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4185612126786442,
                  "rejected_mean_error": 2.5615329666743203,
                  "gap_rejected_minus_accepted": 1.142971753995676
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.209640383720398,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2082301790714265,
                  "rejected_mean_error": 2.2049500102996826,
                  "gap_rejected_minus_accepted": 0.9967198312282561
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8324947953224182,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9286559787061479,
                  "rejected_mean_error": 1.9686748503363707,
                  "gap_rejected_minus_accepted": 1.0400188716302228
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
        "best_epoch": 68,
        "best_calib_loss": 0.08402515202760696,
        "train_time_sec": 41.50220799446106,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9720171302188726,
              "spearman": 0.9046552684609783,
              "auroc_top30_bad": 0.9991455238095238,
              "mae": 0.1399821059273854,
              "mse": 0.04182997108206804,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.477,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6062291919786896,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.1288289872407913
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.135464437687397
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.08948164152801037
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.22101910524964333
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.5718854881331324
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9970675913922875,
              "spearman": 0.9978106636083215,
              "auroc_top30_worst": 0.9981969523809523,
              "pairwise_seed_ranking": 0.9488,
              "predicted_best_mean_error": 0.9193983665406704,
              "seed0_mean_error": 0.9900609410107136,
              "random_seed_mean_error": 0.978739710867405,
              "oracle_best_mean_error": 0.9180251259803772,
              "improvement_over_seed0": 0.0706625744700432,
              "gap_to_oracle": 0.0013732405602931985,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.058600629210472106
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.15711131525039673
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.44210657857656477
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6750462546428044
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.9780684807360173
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.862228584289551,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.8173059976432059,
                  "rejected_mean_error": 2.4249308285713194,
                  "gap_rejected_minus_accepted": 1.6076248309281134
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.409343272447586,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.6750462546428044,
                  "rejected_mean_error": 1.8871351590156555,
                  "gap_rejected_minus_accepted": 1.212088904372851
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9713970422744751,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.44210657857656477,
                  "rejected_mean_error": 1.5140303828954698,
                  "gap_rejected_minus_accepted": 1.071923804318905
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.50405652821064,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.15711131525039673,
                  "rejected_mean_error": 1.251720869231224,
                  "gap_rejected_minus_accepted": 1.0946095539808274
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9097533345222475,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8282557399074236,
                  "rejected_mean_error": 2.446307750940323,
                  "gap_rejected_minus_accepted": 1.618052011032899
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4376544952392578,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.684668372352918,
                  "rejected_mean_error": 1.9062386469841004,
                  "gap_rejected_minus_accepted": 1.2215702746311825
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9902443587779999,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.4479015365242958,
                  "rejected_mean_error": 1.5322203454971313,
                  "gap_rejected_minus_accepted": 1.0843188089728355
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5194454044103622,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.15867553544044494,
                  "rejected_mean_error": 1.2671894095341365,
                  "gap_rejected_minus_accepted": 1.1085138740936915
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9424967398099829,
              "spearman": 0.8928663410792946,
              "auroc_top30_bad": 0.985288380952381,
              "mae": 0.445692859970873,
              "mse": 0.28189157700726764,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.588,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6663603738259528,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3077649345099926
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.35935014872550963
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4606532245159149
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8162641641934713
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1788091871500015
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.981627747331923,
              "spearman": 0.9684426078992692,
              "auroc_top30_worst": 0.9704106666666666,
              "pairwise_seed_ranking": 0.8804,
              "predicted_best_mean_error": 1.599526353120804,
              "seed0_mean_error": 1.6623953195810317,
              "random_seed_mean_error": 1.6560072766542435,
              "oracle_best_mean_error": 1.595594585776329,
              "improvement_over_seed0": 0.06286896646022777,
              "gap_to_oracle": 0.003931767344474979,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4703224310874939
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.757824624578158
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0935520966529846
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3349488293057057
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6556154248714448
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9596744060516365,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4625649544927808,
                  "rejected_mean_error": 3.393069658279419,
                  "gap_rejected_minus_accepted": 1.9305047037866383
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4886353313922882,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3342913879656104,
                  "rejected_mean_error": 2.617534346854725,
                  "gap_rejected_minus_accepted": 1.2832429588891145
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1934847235679626,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0935520966529846,
                  "rejected_mean_error": 2.217678753089905,
                  "gap_rejected_minus_accepted": 1.1241266564369203
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7420187294483185,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7579163156759244,
                  "rejected_mean_error": 1.9554871657233102,
                  "gap_rejected_minus_accepted": 1.1975708500473856
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.002083492279053,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4683541389306387,
                  "rejected_mean_error": 3.4087659454345705,
                  "gap_rejected_minus_accepted": 1.9404118065039317
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5145543813705444,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3382354479103802,
                  "rejected_mean_error": 2.6245841450161405,
                  "gap_rejected_minus_accepted": 1.2863486971057603
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.204286813735962,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.092512681245804,
                  "rejected_mean_error": 2.23227795791626,
                  "gap_rejected_minus_accepted": 1.139765276670456
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7561284750699997,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7605311988838135,
                  "rejected_mean_error": 1.9662318950030893,
                  "gap_rejected_minus_accepted": 1.2057006961192758
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9555946168161475,
              "spearman": 0.9119513156379888,
              "auroc_top30_bad": 0.9871314285714285,
              "mae": 0.45419902611421314,
              "mse": 0.30883984332162917,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.572,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7445885369153715,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.33064167350530627
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3431146491765976
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4522082367181778
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8585467462062836
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3014900189995766
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9608026914141167,
              "spearman": 0.9823484118709838,
              "auroc_top30_worst": 0.9915977142857143,
              "pairwise_seed_ranking": 0.902,
              "predicted_best_mean_error": 1.8815573459863664,
              "seed0_mean_error": 1.9666107931137085,
              "random_seed_mean_error": 1.9462949228286743,
              "oracle_best_mean_error": 1.8785797675848008,
              "improvement_over_seed0": 0.08505344712734209,
              "gap_to_oracle": 0.0029775784015655393,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5519465699195861
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9247681708672107
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2698656009674072
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5017322857242656
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9445513899803162
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5813128471374513,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7281246769163343,
                  "rejected_mean_error": 3.8923918075561525,
                  "gap_rejected_minus_accepted": 2.1642671306398182
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.815420150756836,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5008849157467723,
                  "rejected_mean_error": 3.2727158831331296,
                  "gap_rejected_minus_accepted": 1.7718309673863573
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3897305130958557,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2698656009674072,
                  "rejected_mean_error": 2.619237178993225,
                  "gap_rejected_minus_accepted": 1.349371578025818
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9242575913667679,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9260957865669324,
                  "rejected_mean_error": 2.2847612126787036,
                  "gap_rejected_minus_accepted": 1.3586654261117712
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.61359281539917,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7470823478698732,
                  "rejected_mean_error": 3.9423668003082275,
                  "gap_rejected_minus_accepted": 2.1952844524383544
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.853154867887497,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.517160613269092,
                  "rejected_mean_error": 3.3006930729699513,
                  "gap_rejected_minus_accepted": 1.7835324597008593
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4200103282928467,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2839727325439454,
                  "rejected_mean_error": 2.6492488536834715,
                  "gap_rejected_minus_accepted": 1.3652761211395261
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9402429014444351,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9324979365818085,
                  "rejected_mean_error": 2.315001755474723,
                  "gap_rejected_minus_accepted": 1.3825038188929144
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9616191307931925,
              "spearman": 0.9112383347091458,
              "auroc_top30_bad": 0.9925081904761903,
              "mae": 0.47870804991708954,
              "mse": 0.285290172327358,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.592,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6528616795879856,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.41706081229448316
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4261215655326843
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5006716379761695
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8599143841187159
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9852491309608242,
              "spearman": 0.9794229321106767,
              "auroc_top30_worst": 0.9880807619047619,
              "pairwise_seed_ranking": 0.9048,
              "predicted_best_mean_error": 1.6646251678466797,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.04196492683887487,
              "gap_to_oracle": 0.0027762318849564593,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6298239200115204
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9545214517185321
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.221225964975357
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4204830681400766
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8922538995742801,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5593470985889435,
                  "rejected_mean_error": 3.1555562648773194,
                  "gap_rejected_minus_accepted": 1.596209166288376
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4520998001098633,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4199331432994426,
                  "rejected_mean_error": 2.6141618650180463,
                  "gap_rejected_minus_accepted": 1.1942287217186036
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1579335927963257,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.221225964975357,
                  "rejected_mean_error": 2.216710065460205,
                  "gap_rejected_minus_accepted": 0.9954841004848483
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7786787003278732,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9557018810377335,
                  "rejected_mean_error": 1.973933116603432,
                  "gap_rejected_minus_accepted": 1.0182312355656986
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8419944524765013,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.551137354241477,
                  "rejected_mean_error": 3.105664758682251,
                  "gap_rejected_minus_accepted": 1.5545274044407738
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.435658574104309,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4094567243109413,
                  "rejected_mean_error": 2.5885574004006764,
                  "gap_rejected_minus_accepted": 1.1791006760897351
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1570903658866882,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2084738819599152,
                  "rejected_mean_error": 2.2047063074111937,
                  "gap_rejected_minus_accepted": 0.9962324254512784
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7739531248807907,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.930276933643553,
                  "rejected_mean_error": 1.9681287532184213,
                  "gap_rejected_minus_accepted": 1.0378518195748683
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
        "best_epoch": 63,
        "best_calib_loss": 0.08732505887746811,
        "train_time_sec": 29.133174657821655,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.971787439093126,
              "spearman": 0.8977719281251859,
              "auroc_top30_bad": 0.9994279523809524,
              "mae": 0.1409460521276749,
              "mse": 0.04238338790126535,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.394,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6100824599713471,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.09711763453483581
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.11087756366729737
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": -0.08953552586734295
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.220712334305048
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.5718854881331324
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9976568574530225,
              "spearman": 0.9990673655786501,
              "auroc_top30_worst": 0.9993295238095238,
              "pairwise_seed_ranking": 0.9508,
              "predicted_best_mean_error": 0.9188427065014839,
              "seed0_mean_error": 0.9900609410107136,
              "random_seed_mean_error": 0.978739710867405,
              "oracle_best_mean_error": 0.9180251259803772,
              "improvement_over_seed0": 0.0712182345092297,
              "gap_to_oracle": 0.0008175805211066978,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.06084756624698639
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.1565891134738922
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.44177168825864793
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6745638441801071
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.9780684807360173
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8899280548095707,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.8172559633056323,
                  "rejected_mean_error": 2.425381137609482,
                  "gap_rejected_minus_accepted": 1.6081251743038494
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.414793312549591,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.6745638441801071,
                  "rejected_mean_error": 1.8885823904037475,
                  "gap_rejected_minus_accepted": 1.2140185462236404
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9751784205436707,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.44177168825864793,
                  "rejected_mean_error": 1.5143652732133865,
                  "gap_rejected_minus_accepted": 1.0725935849547386
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5136451423168182,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.1565891134738922,
                  "rejected_mean_error": 1.251894936490059,
                  "gap_rejected_minus_accepted": 1.0953058230161667
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.904153394699097,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8281634164187643,
                  "rejected_mean_error": 2.447138662338257,
                  "gap_rejected_minus_accepted": 1.6189752459194926
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4407108128070831,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.6843492160240809,
                  "rejected_mean_error": 1.9071961159706117,
                  "gap_rejected_minus_accepted": 1.2228468999465307
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9799663126468658,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.44800468295812607,
                  "rejected_mean_error": 1.5321171990633011,
                  "gap_rejected_minus_accepted": 1.084112516105175
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5316103398799896,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.15837035942077637,
                  "rejected_mean_error": 1.267291134874026,
                  "gap_rejected_minus_accepted": 1.1089207754532495
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9401111170736852,
              "spearman": 0.8672656097472347,
              "auroc_top30_bad": 0.9892064761904762,
              "mae": 0.45740692827927704,
              "mse": 0.2960732945260296,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.436,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6590758161695706,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5378494535684586
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.45249452879428864
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.460366597366333
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8145714174588521
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1788091871500015
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9770303565545679,
              "spearman": 0.9759905581650788,
              "auroc_top30_worst": 0.9862918095238096,
              "pairwise_seed_ranking": 0.8792,
              "predicted_best_mean_error": 1.6005436547994614,
              "seed0_mean_error": 1.6623953195810317,
              "random_seed_mean_error": 1.6560072766542435,
              "oracle_best_mean_error": 1.595594585776329,
              "improvement_over_seed0": 0.06185166478157034,
              "gap_to_oracle": 0.004949069023132413,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.48982107448577883
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.756703315828091
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0918097401618958
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3338178947154902
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6556154248714448
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8392641425132754,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.465477711836497,
                  "rejected_mean_error": 3.3668548421859743,
                  "gap_rejected_minus_accepted": 1.9013771303494773
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4708017706871033,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3330400963984788,
                  "rejected_mean_error": 2.6212802260828476,
                  "gap_rejected_minus_accepted": 1.2882401296843689
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1566567420959473,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.0918097401618958,
                  "rejected_mean_error": 2.2194211095809937,
                  "gap_rejected_minus_accepted": 1.127611369419098
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7779825627803802,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7586611400777921,
                  "rejected_mean_error": 1.9552383609871473,
                  "gap_rejected_minus_accepted": 1.1965772209093553
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8595680594444275,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4709064077006446,
                  "rejected_mean_error": 3.3857955265045168,
                  "gap_rejected_minus_accepted": 1.9148891188038721
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.486128568649292,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.33782252350593,
                  "rejected_mean_error": 2.625809809518239,
                  "gap_rejected_minus_accepted": 1.287987286012309
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.1672141551971436,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0877497026920318,
                  "rejected_mean_error": 2.2370409364700317,
                  "gap_rejected_minus_accepted": 1.149291233778
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7826004326343536,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7562392406047337,
                  "rejected_mean_error": 1.9676778488618167,
                  "gap_rejected_minus_accepted": 1.2114386082570832
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9466181885017486,
              "spearman": 0.9004498922894368,
              "auroc_top30_bad": 0.9854598095238095,
              "mae": 0.46265109149017863,
              "mse": 0.34164819877627844,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.388,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7319039837306325,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.42279241448640825
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.36698528809547426
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.4527469701051712
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8602422819932302
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3014900189995766
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9435320998051686,
              "spearman": 0.9784265835690136,
              "auroc_top30_worst": 0.9899062857142857,
              "pairwise_seed_ranking": 0.8988,
              "predicted_best_mean_error": 1.8813241047859193,
              "seed0_mean_error": 1.9666107931137085,
              "random_seed_mean_error": 1.9462949228286743,
              "oracle_best_mean_error": 1.8785797675848008,
              "improvement_over_seed0": 0.08528668832778918,
              "gap_to_oracle": 0.002744337201118441,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5577039737701416
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9296741974659455
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2707161060333252
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.503113764308409
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.9445513899803162
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.373976039886475,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7313777981864082,
                  "rejected_mean_error": 3.8631137161254885,
                  "gap_rejected_minus_accepted": 2.1317359179390802
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.843278557062149,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.502604878063263,
                  "rejected_mean_error": 3.267566986358204,
                  "gap_rejected_minus_accepted": 1.764962108294941
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4200403690338135,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2707161060333252,
                  "rejected_mean_error": 2.618386673927307,
                  "gap_rejected_minus_accepted": 1.3476705678939818
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.039613425731659,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9315214888356365,
                  "rejected_mean_error": 2.2829487849197876,
                  "gap_rejected_minus_accepted": 1.3514272960841511
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3804041147232056,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7450003200107151,
                  "rejected_mean_error": 3.9611050510406494,
                  "gap_rejected_minus_accepted": 2.216104731029934
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8743560910224915,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5210483431178619,
                  "rejected_mean_error": 3.2891533034188405,
                  "gap_rejected_minus_accepted": 1.7681049603009786
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4510709643363953,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2819517068862916,
                  "rejected_mean_error": 2.6512698793411253,
                  "gap_rejected_minus_accepted": 1.3693181724548338
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0567674040794373,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9398734228951591,
                  "rejected_mean_error": 2.312516965968086,
                  "gap_rejected_minus_accepted": 1.372643543072927
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9598893259221153,
              "spearman": 0.9021527014354426,
              "auroc_top30_bad": 0.9896190476190476,
              "mae": 0.4516302523785683,
              "mse": 0.26176165048927796,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.524,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6710839053852976,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.522855322778225
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.41995944819450376
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5002630528092384
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8633875812292099
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9792785490616304,
              "spearman": 0.9756788252664483,
              "auroc_top30_worst": 0.9758933333333334,
              "pairwise_seed_ranking": 0.9048,
              "predicted_best_mean_error": 1.6639796825647355,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.04261041212081906,
              "gap_to_oracle": 0.002130746603012268,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6293242318630219
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9510780982673168
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2205514261722565
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.426230310154622
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.002872014045716,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5603114154868656,
                  "rejected_mean_error": 3.1468774127960204,
                  "gap_rejected_minus_accepted": 1.5865659973091548
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.522354394197464,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.425659088244942,
                  "rejected_mean_error": 2.5970206176891875,
                  "gap_rejected_minus_accepted": 1.1713615294442454
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2145652770996094,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2205514261722565,
                  "rejected_mean_error": 2.2173846042633056,
                  "gap_rejected_minus_accepted": 0.9968331780910491
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8759857267141342,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9525103017735405,
                  "rejected_mean_error": 1.9749992471367217,
                  "gap_rejected_minus_accepted": 1.0224889453631811
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.9863346457481383,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5507242988215553,
                  "rejected_mean_error": 3.1093822574615477,
                  "gap_rejected_minus_accepted": 1.5586579586399925
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4870631694793701,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4176886000416495,
                  "rejected_mean_error": 2.564123102596828,
                  "gap_rejected_minus_accepted": 1.1464345025551783
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2244390845298767,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2087557632923127,
                  "rejected_mean_error": 2.204424426078796,
                  "gap_rejected_minus_accepted": 0.9956686627864835
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8771175742149353,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9275534460468898,
                  "rejected_mean_error": 1.9690462918205058,
                  "gap_rejected_minus_accepted": 1.041492845773616
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
        "best_epoch": 55,
        "best_calib_loss": 0.061181336641311646,
        "train_time_sec": 10.6789870262146,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9832604521726618,
              "spearman": 0.9525067558711418,
              "auroc_top30_bad": 0.9993430476190476,
              "mae": 0.08899655129718594,
              "mse": 0.023640830337918965,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.507,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7055222598150083,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15997952869301663
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.21211287917364388
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.32696042710030454
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6688693121955419
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0404698042665144
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9979819295313437,
              "spearman": 0.9977273872529862,
              "auroc_top30_worst": 0.9986264761904763,
              "pairwise_seed_ranking": 0.8738,
              "predicted_best_mean_error": 1.4384935944974422,
              "seed0_mean_error": 1.5044371087253094,
              "random_seed_mean_error": 1.4930715757012367,
              "oracle_best_mean_error": 1.4327080482244492,
              "improvement_over_seed0": 0.06594351422786726,
              "gap_to_oracle": 0.005785546272992992,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4685572643876076
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6695333444833755
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9515610036969185
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1857049916346867
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4924227940618993
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2947934865951556,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3302013435429998,
                  "rejected_mean_error": 2.9524158487319947,
                  "gap_rejected_minus_accepted": 1.622214505188995
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8674357533454895,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1857049916346867,
                  "rejected_mean_error": 2.4125762013435366,
                  "gap_rejected_minus_accepted": 1.2268712097088499
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4661758542060852,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9515610036969185,
                  "rejected_mean_error": 2.03328458442688,
                  "gap_rejected_minus_accepted": 1.0817235807299612
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.021540343761444,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6695333444833755,
                  "rejected_mean_error": 1.7667192772547404,
                  "gap_rejected_minus_accepted": 1.097185932771365
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.348842477798462,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3412967628571721,
                  "rejected_mean_error": 2.9727002215385436,
                  "gap_rejected_minus_accepted": 1.6314034586813715
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8776087760925293,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1957164299885432,
                  "rejected_mean_error": 2.430599144935608,
                  "gap_rejected_minus_accepted": 1.2348827149470647
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4712821245193481,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9565720805525779,
                  "rejected_mean_error": 2.052302136898041,
                  "gap_rejected_minus_accepted": 1.095730056345463
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0348762273788452,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6704531325101852,
                  "rejected_mean_error": 1.782431767463684,
                  "gap_rejected_minus_accepted": 1.1119786349534988
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8824686344142858,
              "spearman": 0.8411275290696325,
              "auroc_top30_bad": 0.9537668571428572,
              "mae": 0.3434802280671895,
              "mse": 0.21615126879733798,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6545519240609347,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4518832811638713
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.44088501280248166
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5664284516379238
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8951846043537061
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2198312164030969
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8790137836214263,
              "spearman": 0.8102212970376302,
              "auroc_top30_worst": 0.9045973333333335,
              "pairwise_seed_ranking": 0.722,
              "predicted_best_mean_error": 1.6556336447000504,
              "seed0_mean_error": 1.7040709828138352,
              "random_seed_mean_error": 1.6976370857954026,
              "oracle_best_mean_error": 1.637361989378929,
              "improvement_over_seed0": 0.04843733811378481,
              "gap_to_oracle": 0.018271655321121294,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7405185079574585
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9718122224395092
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2392837941169739
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4170137569467143
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6973068408489227
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.0313396930694583,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5321085298856099,
                  "rejected_mean_error": 3.184091639518738,
                  "gap_rejected_minus_accepted": 1.651983109633128
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.616031527519226,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.416204481712655,
                  "rejected_mean_error": 2.5388177370491882,
                  "gap_rejected_minus_accepted": 1.1226132553365333
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3232826590538025,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2392837941169739,
                  "rejected_mean_error": 2.1553298875808715,
                  "gap_rejected_minus_accepted": 0.9160460934638976
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0774270594120026,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9727173820852091,
                  "rejected_mean_error": 1.9393521990058515,
                  "gap_rejected_minus_accepted": 0.9666348169206425
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.00979061126709,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5419224509927962,
                  "rejected_mean_error": 3.163407769203186,
                  "gap_rejected_minus_accepted": 1.6214853182103897
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.6260158121585846,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4226862904540996,
                  "rejected_mean_error": 2.5392922125165422,
                  "gap_rejected_minus_accepted": 1.1166059220624427
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3401058912277222,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.24123841547966,
                  "rejected_mean_error": 2.1669035501480103,
                  "gap_rejected_minus_accepted": 0.9256651346683502
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0538018941879272,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9402071185528286,
                  "rejected_mean_error": 1.9614154932333185,
                  "gap_rejected_minus_accepted": 1.0212083746804899
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.8092900682323788,
              "spearman": 0.8304730086775151,
              "auroc_top30_bad": 0.9292594285714285,
              "mae": 0.41745435457527635,
              "mse": 0.4570839708219977,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.5,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6847044517988964,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4402189836502075
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.47027227272987365
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6594009550213814
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.011244240172704
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3827605006814003
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6351731801316958,
              "spearman": 0.6709132025044496,
              "auroc_top30_worst": 0.7812266666666667,
              "pairwise_seed_ranking": 0.7748,
              "predicted_best_mean_error": 1.9834023206233977,
              "seed0_mean_error": 2.0505429774522783,
              "random_seed_mean_error": 2.030431843161583,
              "oracle_best_mean_error": 1.9620424230098725,
              "improvement_over_seed0": 0.0671406568288806,
              "gap_to_oracle": 0.02135989761352519,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.3075953860282898
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.4859523612719316
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.634185813331604
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.6805052856392444
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.0285268756866457
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3990533590316776,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.865289736641778,
                  "rejected_mean_error": 3.497661127090454,
                  "gap_rejected_minus_accepted": 1.632371390448676
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9570359587669373,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.680150215246634,
                  "rejected_mean_error": 3.071430808058181,
                  "gap_rejected_minus_accepted": 1.391280592811547
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5433821082115173,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.634185813331604,
                  "rejected_mean_error": 2.422867938041687,
                  "gap_rejected_minus_accepted": 0.788682124710083
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2585528492927551,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.486245041457228,
                  "rejected_mean_error": 2.209673315509279,
                  "gap_rejected_minus_accepted": 0.7234282740520512
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.459663414955139,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.9048197631041208,
                  "rejected_mean_error": 3.3620519065856933,
                  "gap_rejected_minus_accepted": 1.4572321434815725
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9620184302330017,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.6936806837186456,
                  "rejected_mean_error": 3.109800896947346,
                  "gap_rejected_minus_accepted": 1.4161202132287005
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.562783122062683,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6329887793064117,
                  "rejected_mean_error": 2.4680971755981447,
                  "gap_rejected_minus_accepted": 0.835108396291733
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.262518733739853,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.4892372995141954,
                  "rejected_mean_error": 2.2396459598592258,
                  "gap_rejected_minus_accepted": 0.7504086603450304
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.890663109508216,
              "spearman": 0.8528482166112681,
              "auroc_top30_bad": 0.9389942857142857,
              "mae": 0.30739515722990035,
              "mse": 0.1769735459049404,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.476,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7534871674621024,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.42143033266067503
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4078734889984131
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5317483035683632
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8933440948963165
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.8489062125347406,
              "spearman": 0.8021742861915433,
              "auroc_top30_worst": 0.868888380952381,
              "pairwise_seed_ranking": 0.7272,
              "predicted_best_mean_error": 1.6836883591413498,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.022901735544204715,
              "gap_to_oracle": 0.021839423179626616,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6569847996234894
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0000314144178843
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2913522106647493
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4964772498747434
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9438753843307497,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5636732062498728,
                  "rejected_mean_error": 3.116621295928955,
                  "gap_rejected_minus_accepted": 1.5529480896790822
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0293304324150085,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.495972945856819,
                  "rejected_mean_error": 2.386528334678552,
                  "gap_rejected_minus_accepted": 0.8905553888217332
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6493101716041565,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2913522106647493,
                  "rejected_mean_error": 2.146583819770813,
                  "gap_rejected_minus_accepted": 0.8552316091060639
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.20852530002594,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0006972399953835,
                  "rejected_mean_error": 1.9589026498438327,
                  "gap_rejected_minus_accepted": 0.9582054098484492
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8698672771453855,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5574765206707848,
                  "rejected_mean_error": 3.0486122608184814,
                  "gap_rejected_minus_accepted": 1.4911357401476966
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9663223326206207,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4903134306803107,
                  "rejected_mean_error": 2.34855416085985,
                  "gap_rejected_minus_accepted": 0.8582407301795392
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6620385646820068,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2759117834568023,
                  "rejected_mean_error": 2.137268405914307,
                  "gap_rejected_minus_accepted": 0.8613566224575044
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2065633833408356,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9702963682394179,
                  "rejected_mean_error": 1.954646269905376,
                  "gap_rejected_minus_accepted": 0.984349901665958
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
        "best_epoch": 46,
        "best_calib_loss": 0.01508072204887867,
        "train_time_sec": 35.10100317001343,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9992401176760656,
              "spearman": 0.9974018844678006,
              "auroc_top30_bad": 0.9997854761904762,
              "mae": 0.024813681470928713,
              "mse": 0.001264353177099516,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.986,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7118117416530464,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04446968092862517
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.11575840820837766
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3233430085727014
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6685449982052669
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0404698042665144
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9994519800447874,
              "spearman": 0.9992777153390566,
              "auroc_top30_worst": 0.9993220952380952,
              "pairwise_seed_ranking": 0.9405,
              "predicted_best_mean_error": 1.434140829205513,
              "seed0_mean_error": 1.5044371087253094,
              "random_seed_mean_error": 1.4930715757012367,
              "oracle_best_mean_error": 1.4327080482244492,
              "improvement_over_seed0": 0.07029627951979656,
              "gap_to_oracle": 0.0014327809810636971,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4647035047411919
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6687135520219802
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9508565228104592
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1854150731801987
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4924227940618993
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3219911098480233,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3300428301559555,
                  "rejected_mean_error": 2.953842469215393,
                  "gap_rejected_minus_accepted": 1.6237996390594376
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8618873953819275,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1854150731801987,
                  "rejected_mean_error": 2.4134459567070006,
                  "gap_rejected_minus_accepted": 1.228030883526802
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4572351574897766,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9508565228104592,
                  "rejected_mean_error": 2.0339890653133392,
                  "gap_rejected_minus_accepted": 1.08313254250288
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0035859048366547,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6687135520219802,
                  "rejected_mean_error": 1.7669925414085388,
                  "gap_rejected_minus_accepted": 1.0982789893865585
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.366497969627381,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3412351536419655,
                  "rejected_mean_error": 2.9732547044754027,
                  "gap_rejected_minus_accepted": 1.6320195508334372
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8771862089633942,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.1953216681083043,
                  "rejected_mean_error": 2.4317834305763246,
                  "gap_rejected_minus_accepted": 1.2364617624680203
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4564270377159119,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9562188388705254,
                  "rejected_mean_error": 2.052655378580093,
                  "gap_rejected_minus_accepted": 1.096436539709568
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0173508524894714,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6695006116628647,
                  "rejected_mean_error": 1.7827492744127909,
                  "gap_rejected_minus_accepted": 1.113248662749926
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9768896091708617,
              "spearman": 0.9650237353026435,
              "auroc_top30_bad": 0.9930125714285715,
              "mae": 0.13196182456985117,
              "mse": 0.03929779912315355,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.964,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7346703211267492,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.16432875230163335
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23892988921105862
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.506881507961452
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8647821200321119
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2198312164030969
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9881083661735247,
              "spearman": 0.9799067847083422,
              "auroc_top30_worst": 0.9868556190476191,
              "pairwise_seed_ranking": 0.8968,
              "predicted_best_mean_error": 1.6391573005914688,
              "seed0_mean_error": 1.7040709828138352,
              "random_seed_mean_error": 1.6976370857954026,
              "oracle_best_mean_error": 1.637361989378929,
              "improvement_over_seed0": 0.06491368222236638,
              "gap_to_oracle": 0.0017953112125397297,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5278198676109314
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8536320514021776
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.175339492893219
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3894990573941008
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6973068408489227
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.432045984268189,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5114901152186924,
                  "rejected_mean_error": 3.3696573715209963,
                  "gap_rejected_minus_accepted": 1.858167256302304
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9098846018314362,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3887403994130731,
                  "rejected_mean_error": 2.6210344946041655,
                  "gap_rejected_minus_accepted": 1.2322940951910923
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.639136552810669,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.175339492893219,
                  "rejected_mean_error": 2.2192741888046266,
                  "gap_rejected_minus_accepted": 1.0439346959114075
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.236928015947342,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8550631689568298,
                  "rejected_mean_error": 1.9786539799121299,
                  "gap_rejected_minus_accepted": 1.1235908109553001
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.44297993183136,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5195420730113982,
                  "rejected_mean_error": 3.3648311710357666,
                  "gap_rejected_minus_accepted": 1.8452890980243684
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9267578423023224,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3927015351420418,
                  "rejected_mean_error": 2.628294581458682,
                  "gap_rejected_minus_accepted": 1.2355930463166402
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6366956233978271,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1729947078227996,
                  "rejected_mean_error": 2.235147257804871,
                  "gap_rejected_minus_accepted": 1.0621525499820712
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2396635711193085,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8466836644543542,
                  "rejected_mean_error": 1.9929233948814677,
                  "gap_rejected_minus_accepted": 1.1462397304271135
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9578357626112148,
              "spearman": 0.960963423445418,
              "auroc_top30_bad": 0.9931878095238097,
              "mae": 0.21447033683657646,
              "mse": 0.11533595917624494,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.976,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7902532725051021,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.22611812382936478
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.27922002286911013
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5536919967889786
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9317768043041229
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3827605006814003
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9436194843977497,
              "spearman": 0.9816303805634436,
              "auroc_top30_worst": 0.9965958095238094,
              "pairwise_seed_ranking": 0.894,
              "predicted_best_mean_error": 1.9651865808963775,
              "seed0_mean_error": 2.0505429774522783,
              "random_seed_mean_error": 2.030431843161583,
              "oracle_best_mean_error": 1.9620424230098725,
              "improvement_over_seed0": 0.08535639655590077,
              "gap_to_oracle": 0.003144157886505017,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7281655316352844
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0869421462217967
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3505906597137451
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5569206697346052
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.0285268756866457
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.8557733297348022,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8243668840196399,
                  "rejected_mean_error": 3.8659668006896974,
                  "gap_rejected_minus_accepted": 2.041599916670058
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2117088437080383,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5563130681517285,
                  "rejected_mean_error": 3.4421509576681704,
                  "gap_rejected_minus_accepted": 1.8858378895164418
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.845936119556427,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3505906597137451,
                  "rejected_mean_error": 2.706463091659546,
                  "gap_rejected_minus_accepted": 1.3558724319458009
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4603615403175354,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0878837961739245,
                  "rejected_mean_error": 2.3427438275409482,
                  "gap_rejected_minus_accepted": 1.2548600313670237
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.87674195766449,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8419794359472064,
                  "rejected_mean_error": 3.9276148509979247,
                  "gap_rejected_minus_accepted": 2.085635415050718
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.2531915307044983,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5726953765606497,
                  "rejected_mean_error": 3.4689160150194924,
                  "gap_rejected_minus_accepted": 1.8962206384588427
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8711442351341248,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3623535740375519,
                  "rejected_mean_error": 2.7387323808670043,
                  "gap_rejected_minus_accepted": 1.3763788068294525
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4959977865219116,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0911266770627763,
                  "rejected_mean_error": 2.373768789882966,
                  "gap_rejected_minus_accepted": 1.2826421128201895
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9785102895149135,
              "spearman": 0.9701990983315845,
              "auroc_top30_bad": 0.9859359999999999,
              "mae": 0.13634750998616219,
              "mse": 0.034900989665827276,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.968,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7636194698399048,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10746437245607376
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22612848944664002
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5008805039048195
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8631723157644272
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9738310228346551,
              "spearman": 0.9640854277666739,
              "auroc_top30_worst": 0.9632152380952381,
              "pairwise_seed_ranking": 0.9024,
              "predicted_best_mean_error": 1.6629727244377137,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.04361737024784085,
              "gap_to_oracle": 0.0011237884759904837,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.629263133764267
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9529293528160988
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2263718870639801
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.431260947130128
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.564122557640076,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5591188849608104,
                  "rejected_mean_error": 3.1576101875305174,
                  "gap_rejected_minus_accepted": 1.598491302569707
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.025206446647644,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4308931161207221,
                  "rejected_mean_error": 2.581351978329424,
                  "gap_rejected_minus_accepted": 1.1504588622087017
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7051066756248474,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2263718870639801,
                  "rejected_mean_error": 2.2115641433715822,
                  "gap_rejected_minus_accepted": 0.9851922563076021
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2892987132072449,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9542893179879782,
                  "rejected_mean_error": 1.9744049759786437,
                  "gap_rejected_minus_accepted": 1.0201156579906656
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5031127691268917,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5499693193700579,
                  "rejected_mean_error": 3.1161770725250246,
                  "gap_rejected_minus_accepted": 1.5662077531549667
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.005167067050934,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4223991589431457,
                  "rejected_mean_error": 2.550140967444768,
                  "gap_rejected_minus_accepted": 1.1277418085016224
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.700686514377594,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2130059797763824,
                  "rejected_mean_error": 2.2001742095947265,
                  "gap_rejected_minus_accepted": 0.9871682298183442
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2729796767234802,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9277790713877905,
                  "rejected_mean_error": 1.968970279005122,
                  "gap_rejected_minus_accepted": 1.0411912076173315
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
        "best_calib_loss": 0.018189873546361923,
        "train_time_sec": 41.82031440734863,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9988342317570141,
              "spearman": 0.9964598819888697,
              "auroc_top30_bad": 0.9996629523809524,
              "mae": 0.0356192112149205,
              "mse": 0.0022645598047383777,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.968,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7287888462275769,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0465268260226585
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.11626444504726678
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.32349031894886865
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.668731845796667
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0404698042665144
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9988047861047056,
              "spearman": 0.9986019676880113,
              "auroc_top30_worst": 0.9991874285714286,
              "pairwise_seed_ranking": 0.9568,
              "predicted_best_mean_error": 1.4336511045396327,
              "seed0_mean_error": 1.5044371087253094,
              "random_seed_mean_error": 1.4930715757012367,
              "oracle_best_mean_error": 1.4327080482244492,
              "improvement_over_seed0": 0.07078600418567671,
              "gap_to_oracle": 0.0009430563151835436,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4651448585391045
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6695181000471115
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9513579761624337
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1855848951101302
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4924227940618993
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.35191764831543,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.330305202861627,
                  "rejected_mean_error": 2.9514811148643494,
                  "gap_rejected_minus_accepted": 1.6211759120027225
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9188291728496552,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1855848951101302,
                  "rejected_mean_error": 2.4129364909172057,
                  "gap_rejected_minus_accepted": 1.2273515958070755
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4952395558357239,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9513579761624337,
                  "rejected_mean_error": 2.0334876119613647,
                  "gap_rejected_minus_accepted": 1.082129635798931
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0180193185806274,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.6695181000471115,
                  "rejected_mean_error": 1.766724358733495,
                  "gap_rejected_minus_accepted": 1.0972062586863836
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3854089498519904,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3417059360278978,
                  "rejected_mean_error": 2.969017663002014,
                  "gap_rejected_minus_accepted": 1.6273117269741164
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9358840882778168,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.195494976321856,
                  "rejected_mean_error": 2.431263505935669,
                  "gap_rejected_minus_accepted": 1.2357685296138128
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5024487972259521,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9565165254473686,
                  "rejected_mean_error": 2.05235769200325,
                  "gap_rejected_minus_accepted": 1.0958411665558814
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0282211601734161,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6703812831640243,
                  "rejected_mean_error": 1.7824557172457378,
                  "gap_rejected_minus_accepted": 1.1120744340817135
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9721156076913609,
              "spearman": 0.9498963130378403,
              "auroc_top30_bad": 0.9942217142857143,
              "mae": 0.14775437452457846,
              "mse": 0.052388948233333725,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.916,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7488041929690952,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.24584308022260665
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3019955152601004
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5057861445829273
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8634203853875398
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2198312164030969
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.991438679789636,
              "spearman": 0.9828278039217947,
              "auroc_top30_worst": 0.9935268571428572,
              "pairwise_seed_ranking": 0.8968,
              "predicted_best_mean_error": 1.6416079910993575,
              "seed0_mean_error": 1.7040709828138352,
              "random_seed_mean_error": 1.6976370857954026,
              "oracle_best_mean_error": 1.637361989378929,
              "improvement_over_seed0": 0.06246299171447767,
              "gap_to_oracle": 0.004246001720428438,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5239100022315979
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8521092558900515
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.174760387134552
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3882023931693421
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6973068408489227
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5086642503738403,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5095991598235237,
                  "rejected_mean_error": 3.3866759700775146,
                  "gap_rejected_minus_accepted": 1.877076810253991
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9349472522735596,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3875771336647083,
                  "rejected_mean_error": 2.6245168588412837,
                  "gap_rejected_minus_accepted": 1.2369397251765755
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6248284578323364,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.174760387134552,
                  "rejected_mean_error": 2.2198532945632934,
                  "gap_rejected_minus_accepted": 1.0450929074287414
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.175685852766037,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8535462475051514,
                  "rejected_mean_error": 1.9791606996713351,
                  "gap_rejected_minus_accepted": 1.1256144521661837
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.5399366140365602,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5144916829797956,
                  "rejected_mean_error": 3.4102846813201904,
                  "gap_rejected_minus_accepted": 1.8957929983403947
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.950395554304123,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3925778526354602,
                  "rejected_mean_error": 2.6286617025496466,
                  "gap_rejected_minus_accepted": 1.2360838499141864
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6195905208587646,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1746398780345917,
                  "rejected_mean_error": 2.2335020875930787,
                  "gap_rejected_minus_accepted": 1.058862209558487
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1829921007156372,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8461585853781018,
                  "rejected_mean_error": 1.9931002931798842,
                  "gap_rejected_minus_accepted": 1.1469417078017825
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9606639374433257,
              "spearman": 0.9481620792934905,
              "auroc_top30_bad": 0.9937691428571429,
              "mae": 0.20393531990125777,
              "mse": 0.10076923644632549,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.96,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8080289065806366,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.2803396350741386
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3342843100786209
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5527826938390732
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9308593591213227
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3827605006814003
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9609918956685799,
              "spearman": 0.983462387367928,
              "auroc_top30_worst": 0.9988662857142858,
              "pairwise_seed_ranking": 0.8872,
              "predicted_best_mean_error": 1.966503065943718,
              "seed0_mean_error": 2.0505429774522783,
              "random_seed_mean_error": 2.030431843161583,
              "oracle_best_mean_error": 1.9620424230098725,
              "improvement_over_seed0": 0.08403991150856038,
              "gap_to_oracle": 0.0044606429338454046,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7291646327972412
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0809538203936357
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3535422946929931
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5563104200973186
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.0285268756866457
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9960112810134887,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8162446284823948,
                  "rejected_mean_error": 3.9390671005249023,
                  "gap_rejected_minus_accepted": 2.1228224720425075
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3085867166519165,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5555731288396943,
                  "rejected_mean_error": 3.4443660475575504,
                  "gap_rejected_minus_accepted": 1.888792918717856
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8581039309501648,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3535422946929931,
                  "rejected_mean_error": 2.703511456680298,
                  "gap_rejected_minus_accepted": 1.3499691619873047
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3834370970726013,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0817495854898764,
                  "rejected_mean_error": 2.3447929288687037,
                  "gap_rejected_minus_accepted": 1.2630433433788273
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 3.0121477842330933,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8355850740273794,
                  "rejected_mean_error": 3.985164108276367,
                  "gap_rejected_minus_accepted": 2.1495790342489878
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.3733959794044495,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5732707736645153,
                  "rejected_mean_error": 3.4672080902826217,
                  "gap_rejected_minus_accepted": 1.8939373166181064
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.8927379250526428,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3640449430942536,
                  "rejected_mean_error": 2.7370410118103026,
                  "gap_rejected_minus_accepted": 1.372996068716049
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4187580049037933,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0848545995023515,
                  "rejected_mean_error": 2.3758818427509163,
                  "gap_rejected_minus_accepted": 1.2910272432485648
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9775083346517752,
              "spearman": 0.960422818276419,
              "auroc_top30_bad": 0.994464761904762,
              "mae": 0.12682283089086413,
              "mse": 0.03733815222112536,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.88,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.747689741182975,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.21817605608701707
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.27668152492046355
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5003650198578835
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8589206799586614
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9898568225955751,
              "spearman": 0.9871967068138924,
              "auroc_top30_worst": 0.9890834285714285,
              "pairwise_seed_ranking": 0.9076,
              "predicted_best_mean_error": 1.6648779487609864,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.04171214592456818,
              "gap_to_oracle": 0.0030290127992631533,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6305150368213653
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9495572016980404
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2183046492099763
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.420190275128462
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.447507619857788,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5586828682422638,
                  "rejected_mean_error": 3.1615343379974363,
                  "gap_rejected_minus_accepted": 1.6028514697551726
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9821307957172394,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4194336156644078,
                  "rejected_mean_error": 2.6156572560532787,
                  "gap_rejected_minus_accepted": 1.1962236403888709
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.617981195449829,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2183046492099763,
                  "rejected_mean_error": 2.219631381225586,
                  "gap_rejected_minus_accepted": 1.0013267320156096
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.28291717171669,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9506527460611667,
                  "rejected_mean_error": 1.9756197540075573,
                  "gap_rejected_minus_accepted": 1.0249670079463906
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.385961604118347,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5499383069409265,
                  "rejected_mean_error": 3.116456184387207,
                  "gap_rejected_minus_accepted": 1.5665178774462807
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9728808403015137,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4097573542021176,
                  "rejected_mean_error": 2.5876650545332165,
                  "gap_rejected_minus_accepted": 1.177907700331099
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6128032803535461,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2055457413196564,
                  "rejected_mean_error": 2.2076344480514525,
                  "gap_rejected_minus_accepted": 1.002088706731796
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.274550586938858,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9272036519315507,
                  "rejected_mean_error": 1.9691641368967965,
                  "gap_rejected_minus_accepted": 1.0419604849652457
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
        "best_epoch": 27,
        "best_calib_loss": 0.015910452231764793,
        "train_time_sec": 29.552871704101562,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9983925183835092,
              "spearman": 0.9940710144852308,
              "auroc_top30_bad": 0.9996646666666666,
              "mae": 0.03780541764828377,
              "mse": 0.002814240691978027,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.987,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7262098850174291,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.054548236932838334
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.11683751501906663
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.3235596959182061
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6689014321372534
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0404698042665144
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9986914647654679,
              "spearman": 0.9984317242091935,
              "auroc_top30_worst": 0.9987647619047618,
              "pairwise_seed_ranking": 0.9397,
              "predicted_best_mean_error": 1.4341311567425727,
              "seed0_mean_error": 1.5044371087253094,
              "random_seed_mean_error": 1.4930715757012367,
              "oracle_best_mean_error": 1.4327080482244492,
              "improvement_over_seed0": 0.0703059519827367,
              "gap_to_oracle": 0.0014231085181235503,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4649175487160683
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.669624527335167
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9511743596196175
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1857435473839442
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4924227940618993
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.370695400238038,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3303021096189818,
                  "rejected_mean_error": 2.951508954048157,
                  "gap_rejected_minus_accepted": 1.6212068444291752
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8915170729160309,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1857435473839442,
                  "rejected_mean_error": 2.4124605340957643,
                  "gap_rejected_minus_accepted": 1.2267169867118202
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.496933400630951,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9511743596196175,
                  "rejected_mean_error": 2.033671228504181,
                  "gap_rejected_minus_accepted": 1.0824968688845633
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.018843412399292,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.669624527335167,
                  "rejected_mean_error": 1.7666888829708098,
                  "gap_rejected_minus_accepted": 1.0970643556356428
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4049257278442386,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3414108567436536,
                  "rejected_mean_error": 2.971673376560211,
                  "gap_rejected_minus_accepted": 1.6302625198165575
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8998128473758698,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.195631563782692,
                  "rejected_mean_error": 2.4308537435531616,
                  "gap_rejected_minus_accepted": 1.2352221797704697
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4978886246681213,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9562676994204521,
                  "rejected_mean_error": 2.0526065180301667,
                  "gap_rejected_minus_accepted": 1.0963388186097145
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0325742363929749,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.6705833777189255,
                  "rejected_mean_error": 1.782388352394104,
                  "gap_rejected_minus_accepted": 1.1118049746751786
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9747020731024518,
              "spearman": 0.9617138754039262,
              "auroc_top30_bad": 0.9938133333333334,
              "mae": 0.13361163219846786,
              "mse": 0.04568927615823289,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.968,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7579603822396699,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.15280591544508934
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.27376809290349485
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5091554061815142
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8638127352029085
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2198312164030969
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9914390770781181,
              "spearman": 0.9846439899161538,
              "auroc_top30_worst": 0.9872548571428571,
              "pairwise_seed_ranking": 0.9076,
              "predicted_best_mean_error": 1.6401998574733734,
              "seed0_mean_error": 1.7040709828138352,
              "random_seed_mean_error": 1.6976370857954026,
              "oracle_best_mean_error": 1.637361989378929,
              "improvement_over_seed0": 0.0638711253404618,
              "gap_to_oracle": 0.002837868094444307,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5230269703865051
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8565673375358949
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1755566111564637
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3876461885504123
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6973068408489227
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4249410867691044,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.509687030315399,
                  "rejected_mean_error": 3.3858851356506348,
                  "gap_rejected_minus_accepted": 1.8761981053352357
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.969860553741455,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3870700204003454,
                  "rejected_mean_error": 2.6260349582940243,
                  "gap_rejected_minus_accepted": 1.238964937893679
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6559106707572937,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1755566111564637,
                  "rejected_mean_error": 2.219057070541382,
                  "gap_rejected_minus_accepted": 1.0435004593849182
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.214840054512024,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8583728137869424,
                  "rejected_mean_error": 1.9775484101876633,
                  "gap_rejected_minus_accepted": 1.1191755964007208
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4429484844207763,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.514788847896788,
                  "rejected_mean_error": 3.4076101970672608,
                  "gap_rejected_minus_accepted": 1.8928213491704728
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9970354735851288,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3899836519503976,
                  "rejected_mean_error": 2.6363619490275307,
                  "gap_rejected_minus_accepted": 1.246378297077133
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6713343262672424,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1732198808193206,
                  "rejected_mean_error": 2.2349220848083498,
                  "gap_rejected_minus_accepted": 1.0617022039890291
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2170127630233765,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.850731347761457,
                  "rejected_mean_error": 1.9915597368689144,
                  "gap_rejected_minus_accepted": 1.1408283891074573
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9624544854294863,
              "spearman": 0.9656232583389367,
              "auroc_top30_bad": 0.990360380952381,
              "mae": 0.20619290849640964,
              "mse": 0.09524910781823401,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.8251514350194468,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.18228024584054947
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2632063579559326
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5549104418039322
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9334691268444061
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3827605006814003
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9527407000645408,
              "spearman": 0.9823605094147261,
              "auroc_top30_worst": 0.9926918095238095,
              "pairwise_seed_ranking": 0.9168,
              "predicted_best_mean_error": 1.964016139984131,
              "seed0_mean_error": 2.0505429774522783,
              "random_seed_mean_error": 2.030431843161583,
              "oracle_best_mean_error": 1.9620424230098725,
              "improvement_over_seed0": 0.08652683746814738,
              "gap_to_oracle": 0.0019737169742584104,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7221334571838379
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0820463643624232
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3530111795425415
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.5569983270885086
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 2.0285268756866457
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.949168157577515,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8157214289771186,
                  "rejected_mean_error": 3.943775896072388,
                  "gap_rejected_minus_accepted": 2.1280544670952692
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.369743525981903,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.5561791547716237,
                  "rejected_mean_error": 3.4425518421319348,
                  "gap_rejected_minus_accepted": 1.886372687360311
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.9265727996826172,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3530111795425415,
                  "rejected_mean_error": 2.7040425718307497,
                  "gap_rejected_minus_accepted": 1.3510313922882082
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4313757717609406,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.082887089290558,
                  "rejected_mean_error": 2.3444129516119125,
                  "gap_rejected_minus_accepted": 1.2615258623213546
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.9821600914001465,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.8337392723560333,
                  "rejected_mean_error": 4.001776323318482,
                  "gap_rejected_minus_accepted": 2.1680370509624485
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.4059934616088867,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.5730483508046298,
                  "rejected_mean_error": 3.4678682978191073,
                  "gap_rejected_minus_accepted": 1.8948199470144775
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.95846426486969,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3647610008716584,
                  "rejected_mean_error": 2.7363249540328978,
                  "gap_rejected_minus_accepted": 1.3715639531612394
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.4398422539234161,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0845857257880862,
                  "rejected_mean_error": 2.375972425873904,
                  "gap_rejected_minus_accepted": 1.291386700085818
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9771160805866617,
              "spearman": 0.9691895779933919,
              "auroc_top30_bad": 0.9893996190476191,
              "mae": 0.13666598284728826,
              "mse": 0.03929969445485814,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.976,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7560498448113671,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.11798915266990662
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.25081314549446104
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5014999415040016
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.862715114569664
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2155965617477893
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9747077231803928,
              "spearman": 0.971515457737893,
              "auroc_top30_worst": 0.9750796190476191,
              "pairwise_seed_ranking": 0.892,
              "predicted_best_mean_error": 1.664091989517212,
              "seed0_mean_error": 1.7065900946855546,
              "random_seed_mean_error": 1.7170267285108567,
              "oracle_best_mean_error": 1.6618489359617232,
              "improvement_over_seed0": 0.042498105168342626,
              "gap_to_oracle": 0.0022430535554887054,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6311186459064484
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9526188183480349
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2225031757831573
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.429037762635044
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.718968015217781
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.427583909034729,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5611538962523142,
                  "rejected_mean_error": 3.1392950859069826,
                  "gap_rejected_minus_accepted": 1.5781411896546684
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0026974081993103,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.42844993152766,
                  "rejected_mean_error": 2.58866592070546,
                  "gap_rejected_minus_accepted": 1.1602159891778001
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6437872052192688,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2225031757831573,
                  "rejected_mean_error": 2.2154328546524047,
                  "gap_rejected_minus_accepted": 0.9929296788692474
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.300516277551651,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9538904086659892,
                  "rejected_mean_error": 1.974538229572862,
                  "gap_rejected_minus_accepted": 1.0206478209068728
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.3759038925170897,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5521082699298858,
                  "rejected_mean_error": 3.096926517486572,
                  "gap_rejected_minus_accepted": 1.5448182475566863
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.993347018957138,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.418478954443957,
                  "rejected_mean_error": 2.5617771300058516,
                  "gap_rejected_minus_accepted": 1.1432981755618945
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6374980807304382,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2091896259784698,
                  "rejected_mean_error": 2.2039905633926393,
                  "gap_rejected_minus_accepted": 0.9948009374141695
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2890495359897614,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9278811750903962,
                  "rejected_mean_error": 1.968935880431517,
                  "gap_rejected_minus_accepted": 1.0410547053411205
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
