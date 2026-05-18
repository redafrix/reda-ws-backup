# Stage 7 Multi-Expert Target Experiments: holdout_object_bowl

```json
{
  "split": "holdout_object_bowl",
  "by_target": {
    "target_chunk_l2_single_expert": [
      {
        "variant": "action_only_baseline",
        "feature_mode": "A0_action_flat",
        "model_kind": "mlp",
        "train_setting": "mixed",
        "train_rows": 10000,
        "input_dim": 70,
        "best_epoch": 75,
        "best_calib_loss": 0.0932208001613617,
        "train_time_sec": 16.999208688735962,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8734355308614724,
              "spearman": 0.8231822234273738,
              "auroc_top30_bad": 0.9045283333333333,
              "mae": 0.19858561774194242,
              "mse": 0.19941780146817734,
              "expert_lt_perturb_large": 0.979,
              "expert_lt_other_task": 0.549,
              "expert_lt_simvla_seed0": 0.969,
              "same_context_pred_std": 0.7055249075005547,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4734501058906317
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5027802829444409
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6764765583962202
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9551890594343344
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
              "pearson": 0.9977239673799343,
              "spearman": 0.9963308445971458,
              "auroc_top30_worst": 0.9987857142857145,
              "pairwise_seed_ranking": 0.8666,
              "predicted_best_mean_error": 1.537045886963606,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.0785624410510064,
              "gap_to_oracle": 0.008186652779579084,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6719624220728874
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8103123641729355
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0112142556071282
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2420035685141881
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.736993384361268,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.4059055191344685,
                  "rejected_mean_error": 3.4546381998062134,
                  "gap_rejected_minus_accepted": 2.048732680671745
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9708035290241241,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.2420035685141881,
                  "rejected_mean_error": 2.7171044432640077,
                  "gap_rejected_minus_accepted": 1.4751008747498195
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.393418788909912,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0112142556071282,
                  "rejected_mean_error": 2.210343318796158,
                  "gap_rejected_minus_accepted": 1.1991290631890297
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0313027799129486,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8103123641729355,
                  "rejected_mean_error": 1.877600928211212,
                  "gap_rejected_minus_accepted": 1.0672885640382765
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.739956545829773,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.410888303551409,
                  "rejected_mean_error": 3.4580885481834414,
                  "gap_rejected_minus_accepted": 2.047200244632032
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.978387862443924,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2441429787079492,
                  "rejected_mean_error": 2.730004375934601,
                  "gap_rejected_minus_accepted": 1.4858613972266517
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4085545539855957,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.0049754138588904,
                  "rejected_mean_error": 2.226241242170334,
                  "gap_rejected_minus_accepted": 1.2212658283114435
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0268226861953735,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.8019680796861649,
                  "rejected_mean_error": 1.8868217441240946,
                  "gap_rejected_minus_accepted": 1.0848536644379299
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5252454365548905,
              "spearman": 0.48884133788647605,
              "auroc_top30_bad": 0.658703619047619,
              "mae": 0.47511287047863004,
              "mse": 0.5347785276694298,
              "expert_lt_perturb_large": 0.984,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.964,
              "same_context_pred_std": 0.6303231559009198,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5537240207791329
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8072762405633926
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9433583812117576
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1685785418113073
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
              "pearson": 0.44067028483768717,
              "spearman": 0.49449217849099425,
              "auroc_top30_worst": 0.7179062857142858,
              "pairwise_seed_ranking": 0.7528,
              "predicted_best_mean_error": 1.4878753623962402,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.04091846132278443,
              "gap_to_oracle": 0.025032340288162258,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9497413229942322
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.167943815008188
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3493060023307801
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.472074140427209
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1437737464904787,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.5213851115438672,
                  "rejected_mean_error": 1.6725176129341126,
                  "gap_rejected_minus_accepted": 0.15113250139024537
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8019827604293823,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.471748977168011,
                  "rejected_mean_error": 1.7303327811411775,
                  "gap_rejected_minus_accepted": 0.2585838039731665
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4998561143875122,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3493060023307801,
                  "rejected_mean_error": 1.7236907210350036,
                  "gap_rejected_minus_accepted": 0.3743847187042235
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2032258808612823,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1690835446214523,
                  "rejected_mean_error": 1.6592313795486662,
                  "gap_rejected_minus_accepted": 0.4901478349272139
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.130565619468689,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.512621046702067,
                  "rejected_mean_error": 1.6743488168716432,
                  "gap_rejected_minus_accepted": 0.16172777016957607
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8012565672397614,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4637558772602184,
                  "rejected_mean_error": 1.7218429663824657,
                  "gap_rejected_minus_accepted": 0.2580870891222473
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5312625169754028,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3516084470748901,
                  "rejected_mean_error": 1.705979200363159,
                  "gap_rejected_minus_accepted": 0.35437075328826895
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1722899675369263,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1247613997686476,
                  "rejected_mean_error": 1.6649116991675474,
                  "gap_rejected_minus_accepted": 0.5401502993988998
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.4029108104106395,
              "spearman": 0.3509770593315149,
              "auroc_top30_bad": 0.5676860952380952,
              "mae": 0.6667994446516037,
              "mse": 0.8824646197297678,
              "expert_lt_perturb_large": 0.896,
              "expert_lt_other_task": 0.496,
              "expert_lt_simvla_seed0": 0.776,
              "same_context_pred_std": 0.6468122272671981,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4996906145811081
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5976900774717331
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2230549555420875
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3448890811681748
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
              "pearson": 0.07863054514215523,
              "spearman": -0.052974016623370646,
              "auroc_top30_worst": 0.3312822857142857,
              "pairwise_seed_ranking": 0.706,
              "predicted_best_mean_error": 1.759639916062355,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.04750866532325748,
              "gap_to_oracle": 0.03575311589241026,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.7967546327114106
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 2.0747296696481032
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8735621514797212
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.8035763350885305
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7832838773727415,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.751741767141554,
                  "rejected_mean_error": 2.25891997051239,
                  "gap_rejected_minus_accepted": 0.5071782033708361
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8365787863731384,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.804427753136023,
                  "rejected_mean_error": 1.7965676666448673,
                  "gap_rejected_minus_accepted": -0.007860086491155771
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3872936367988586,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.8735621514797212,
                  "rejected_mean_error": 1.7313570234775544,
                  "gap_rejected_minus_accepted": -0.14220512800216678
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0646658837795258,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 2.0712787980279224,
                  "rejected_mean_error": 1.7126619216281296,
                  "gap_rejected_minus_accepted": -0.3586168763997928
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7256886720657345,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.7536148991849687,
                  "rejected_mean_error": 2.288951721191406,
                  "gap_rejected_minus_accepted": 0.5353368220064374
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8376303315162659,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.80322749394784,
                  "rejected_mean_error": 1.8187873647326516,
                  "gap_rejected_minus_accepted": 0.01555987078481147
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3901353478431702,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8654540622234344,
                  "rejected_mean_error": 1.7488431005477905,
                  "gap_rejected_minus_accepted": -0.11661096167564389
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0521530210971832,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 2.077511838977299,
                  "rejected_mean_error": 1.7160636336408197,
                  "gap_rejected_minus_accepted": -0.36144820533647937
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6235840332421945,
              "spearman": 0.5853479818761104,
              "auroc_top30_bad": 0.8034502857142858,
              "mae": 0.49021766790747645,
              "mse": 0.49000910032313866,
              "expert_lt_perturb_large": 0.936,
              "expert_lt_other_task": 0.52,
              "expert_lt_simvla_seed0": 0.884,
              "same_context_pred_std": 0.6887938270176085,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6746134932041168
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.607119726395607
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8655497940540313
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0653443666299185
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
              "pearson": 0.7017859365980551,
              "spearman": 0.5877106711748296,
              "auroc_top30_worst": 0.8685988571428571,
              "pairwise_seed_ranking": 0.7444,
              "predicted_best_mean_error": 1.5700134875774383,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.049308790683746384,
              "gap_to_oracle": 0.018870227336883483,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.822072360754013
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.141971864283849
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2867803395748139
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4028673815384094
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.402023983001709,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.509897500594457,
                  "rejected_mean_error": 2.6410258407592773,
                  "gap_rejected_minus_accepted": 1.1311283401648202
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0479584336280823,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4024140782964396,
                  "rejected_mean_error": 2.283389542811214,
                  "gap_rejected_minus_accepted": 0.8809754645147743
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.7039052844047546,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2867803395748139,
                  "rejected_mean_error": 1.9592403296470642,
                  "gap_rejected_minus_accepted": 0.6724599900722503
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2734820544719696,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.142285143129361,
                  "rejected_mean_error": 1.7835940965466208,
                  "gap_rejected_minus_accepted": 0.6413089534172598
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4596474170684814,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.5045595955848694,
                  "rejected_mean_error": 2.6521864223480223,
                  "gap_rejected_minus_accepted": 1.1476268267631529
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.1067469120025635,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3932588922786202,
                  "rejected_mean_error": 2.29033582078086,
                  "gap_rejected_minus_accepted": 0.8970769285022397
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.723401963710785,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2622097101211547,
                  "rejected_mean_error": 1.9764348464012147,
                  "gap_rejected_minus_accepted": 0.71422513628006
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2517659962177277,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0851741073623535,
                  "rejected_mean_error": 1.7992759401148015,
                  "gap_rejected_minus_accepted": 0.714101832752448
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
        "best_epoch": 79,
        "best_calib_loss": 0.0064374906942248344,
        "train_time_sec": 64.31426525115967,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9996435349160301,
              "spearman": 0.9987518649067227,
              "auroc_top30_bad": 0.9995864523809522,
              "mae": 0.01965750449341722,
              "mse": 0.0006914885151745431,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7396661825437487,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.00029336635768413544
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19785668466091155
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5739950283527374
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9268403259754181
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
              "pearson": 0.9995670893215236,
              "spearman": 0.999353610302129,
              "auroc_top30_worst": 0.9997379047619048,
              "pairwise_seed_ranking": 0.9557,
              "predicted_best_mean_error": 1.5304070627093316,
              "seed0_mean_error": 1.6156083280146123,
              "random_seed_mean_error": 1.6104893134832383,
              "oracle_best_mean_error": 1.5288592341840268,
              "improvement_over_seed0": 0.08520126530528072,
              "gap_to_oracle": 0.001547828525304773,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6661467599272728
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8071454864740372
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.0101435073256493
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.241384118771553
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.610778787201643
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.768628883361817,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.405770457075702,
                  "rejected_mean_error": 3.4558537583351137,
                  "gap_rejected_minus_accepted": 2.050083301259412
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9770774245262146,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.241384118771553,
                  "rejected_mean_error": 2.718962792491913,
                  "gap_rejected_minus_accepted": 1.4775786737203598
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4056655168533325,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 1.0101435073256493,
                  "rejected_mean_error": 2.2114140670776368,
                  "gap_rejected_minus_accepted": 1.2012705597519875
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.017314225435257,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.8071454864740372,
                  "rejected_mean_error": 1.8786565541108449,
                  "gap_rejected_minus_accepted": 1.0715110676368078
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7896839141845704,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.410662989517053,
                  "rejected_mean_error": 3.460116374492645,
                  "gap_rejected_minus_accepted": 2.049453384975592
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.995783120393753,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2430234499375026,
                  "rejected_mean_error": 2.733362962245941,
                  "gap_rejected_minus_accepted": 1.4903395123084386
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4159854054450989,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.003812305510044,
                  "rejected_mean_error": 2.2274043505191803,
                  "gap_rejected_minus_accepted": 1.2235920450091362
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.0130718350410461,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7989224928617478,
                  "rejected_mean_error": 1.8878369397322337,
                  "gap_rejected_minus_accepted": 1.0889144468704859
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9882596863363486,
              "spearman": 0.9833276933905132,
              "auroc_top30_bad": 0.9840860952380952,
              "mae": 0.0817394666519016,
              "mse": 0.013859416424007042,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7078581175870826,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.04394069415330887
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22673268702030183
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6787698642134666
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0358739339431127
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
              "pearson": 0.975401493415528,
              "spearman": 0.9751309398598016,
              "auroc_top30_worst": 0.9832899047619048,
              "pairwise_seed_ranking": 0.8784,
              "predicted_best_mean_error": 1.4695677785873413,
              "seed0_mean_error": 1.5287938237190246,
              "random_seed_mean_error": 1.537072078704834,
              "oracle_best_mean_error": 1.462843022108078,
              "improvement_over_seed0": 0.05922604513168328,
              "gap_to_oracle": 0.006724756479263405,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.885671429157257
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9771482971234199
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1693442682266235
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3602955839527187
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.5364983616828918
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1075648069381714,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4613377315733167,
                  "rejected_mean_error": 2.2129440326690673,
                  "gap_rejected_minus_accepted": 0.7516063010957506
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9105488955974579,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.359773945528517,
                  "rejected_mean_error": 2.0655423806498225,
                  "gap_rejected_minus_accepted": 0.7057684351213056
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.537225067615509,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1693442682266235,
                  "rejected_mean_error": 1.9036524551391603,
                  "gap_rejected_minus_accepted": 0.7343081869125367
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.157136857509613,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9775446973288783,
                  "rejected_mean_error": 1.7232139400636883,
                  "gap_rejected_minus_accepted": 0.7456692427348101
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.126835060119629,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4588153245713975,
                  "rejected_mean_error": 2.1586003160476683,
                  "gap_rejected_minus_accepted": 0.6997849914762708
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9029149115085602,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3511868230799302,
                  "rejected_mean_error": 2.0559765081557018,
                  "gap_rejected_minus_accepted": 0.7047896850757716
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5316779017448425,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.157432424545288,
                  "rejected_mean_error": 1.9001552228927612,
                  "gap_rejected_minus_accepted": 0.7427227983474731
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.194704383611679,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.959388776431008,
                  "rejected_mean_error": 1.7206254706663244,
                  "gap_rejected_minus_accepted": 0.7612366942353165
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9744890967057203,
              "spearman": 0.9790537664388043,
              "auroc_top30_bad": 0.9878445714285714,
              "mae": 0.14725383697841316,
              "mse": 0.0500415684081007,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.996,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7215679651888554,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.07894187742471695
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.2055211198568344
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.696005794608593
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0484175980170567
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
              "pearson": 0.941818149244487,
              "spearman": 0.9589314317641163,
              "auroc_top30_worst": 0.9852251428571428,
              "pairwise_seed_ranking": 0.916,
              "predicted_best_mean_error": 1.7263385998010636,
              "seed0_mean_error": 1.8071485813856125,
              "random_seed_mean_error": 1.8040734711885453,
              "oracle_best_mean_error": 1.7238868001699448,
              "improvement_over_seed0": 0.08080998158454888,
              "gap_to_oracle": 0.002451799631118856,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.9451340675354004
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.1149325653528557
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3032109434127808
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.458162155232704
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.8024595874786378
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.277874875068665,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6498511640760634,
                  "rejected_mean_error": 3.1759353981018066,
                  "gap_rejected_minus_accepted": 1.5260842340257432
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.921307384967804,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4572002350838742,
                  "rejected_mean_error": 2.8360315146156774,
                  "gap_rejected_minus_accepted": 1.3788312795318032
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6474165320396423,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3032109434127808,
                  "rejected_mean_error": 2.3017082315444948,
                  "gap_rejected_minus_accepted": 0.998497288131714
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3785969614982605,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.1156349951466813,
                  "rejected_mean_error": 2.0318897874785335,
                  "gap_rejected_minus_accepted": 0.9162547923318523
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2728360652923585,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6511795032024383,
                  "rejected_mean_error": 3.2108702850341797,
                  "gap_rejected_minus_accepted": 1.5596907818317414
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9731732308864594,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4557659382169896,
                  "rejected_mean_error": 2.850141506346445,
                  "gap_rejected_minus_accepted": 1.3943755681294554
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6429614424705505,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.301734883069992,
                  "rejected_mean_error": 2.312562279701233,
                  "gap_rejected_minus_accepted": 1.010827396631241
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3860463201999664,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.1160512155010587,
                  "rejected_mean_error": 2.0399781752397668,
                  "gap_rejected_minus_accepted": 0.9239269597387081
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9890102016593316,
              "spearman": 0.9873719168185984,
              "auroc_top30_bad": 0.9955108571428571,
              "mae": 0.08900539226550609,
              "mse": 0.017721686618985297,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.972,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7523743191486357,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0608820081949234
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.19982503340244293
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5893028330802917
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9336234129587809
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
              "pearson": 0.9821113857140722,
              "spearman": 0.98324592182139,
              "auroc_top30_worst": 0.995303619047619,
              "pairwise_seed_ranking": 0.922,
              "predicted_best_mean_error": 1.5545262722969055,
              "seed0_mean_error": 1.6193222782611847,
              "random_seed_mean_error": 1.626927037715912,
              "oracle_best_mean_error": 1.5511432602405548,
              "improvement_over_seed0": 0.06479600596427915,
              "gap_to_oracle": 0.0033830120563507204,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5682093913555145
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8710222122951959
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.117453287744522
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3112913647503741
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.623010334610939
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6986613750457793,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4771300409369998,
                  "rejected_mean_error": 2.9359329776763916,
                  "gap_rejected_minus_accepted": 1.4588029367393918
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.057875633239746,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3104713342551106,
                  "rejected_mean_error": 2.5586302813630515,
                  "gap_rejected_minus_accepted": 1.2481589471079408
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5563428401947021,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.117453287744522,
                  "rejected_mean_error": 2.128567381477356,
                  "gap_rejected_minus_accepted": 1.0111140937328338
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2780839800834656,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8719636838847455,
                  "rejected_mean_error": 1.873893580798024,
                  "gap_rejected_minus_accepted": 1.0019298969132784
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6798009395599363,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4691338721911114,
                  "rejected_mean_error": 2.971017932891846,
                  "gap_rejected_minus_accepted": 1.5018840607007344
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0654982924461365,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2984497531212587,
                  "rejected_mean_error": 2.5717534243114413,
                  "gap_rejected_minus_accepted": 1.2733036711901826
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5694173574447632,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.104301305294037,
                  "rejected_mean_error": 2.1343432512283327,
                  "gap_rejected_minus_accepted": 1.0300419459342958
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2817714512348175,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.851890091858213,
                  "rejected_mean_error": 1.8778689506857154,
                  "gap_rejected_minus_accepted": 1.0259788588275023
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_l2_single_expert"
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
        "best_epoch": 68,
        "best_calib_loss": 0.08259732276201248,
        "train_time_sec": 14.086798667907715,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.899375484054364,
              "spearman": 0.8479277958541337,
              "auroc_top30_bad": 0.9195945714285714,
              "mae": 0.18219589696764016,
              "mse": 0.15162867618607312,
              "expert_lt_perturb_large": 0.988,
              "expert_lt_other_task": 0.532,
              "expert_lt_simvla_seed0": 0.968,
              "same_context_pred_std": 0.6596231051365261,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.41165005273371935
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.48754118687007575
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6333002368655987
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9071115630207583
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2657154838076328
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9979546886222476,
              "spearman": 0.9968244163048241,
              "auroc_top30_worst": 0.9993330476190476,
              "pairwise_seed_ranking": 0.8595,
              "predicted_best_mean_error": 1.5067566586136818,
              "seed0_mean_error": 1.5817216905951499,
              "random_seed_mean_error": 1.5773716281354426,
              "oracle_best_mean_error": 1.4989939597547055,
              "improvement_over_seed0": 0.07496503198146809,
              "gap_to_oracle": 0.007762698858976291,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.6432335110902786
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7696861782073975
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9660167855024338
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1998156134446463
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.576842271912098
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.65668306350708,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.3688835129340489,
                  "rejected_mean_error": 3.4484711027145387,
                  "gap_rejected_minus_accepted": 2.07958758978049
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.914398044347763,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.1998156134446463,
                  "rejected_mean_error": 2.7079222473144533,
                  "gap_rejected_minus_accepted": 1.508106633869807
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3182048201560974,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9660167855024338,
                  "rejected_mean_error": 2.187667758321762,
                  "gap_rejected_minus_accepted": 1.2216509728193283
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9638355821371078,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7696861782073975,
                  "rejected_mean_error": 1.845894303146998,
                  "gap_rejected_minus_accepted": 1.0762081249396007
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.658662247657776,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3738150421116087,
                  "rejected_mean_error": 3.4528815269470217,
                  "gap_rejected_minus_accepted": 2.079066484835413
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9225127696990967,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.201289805014928,
                  "rejected_mean_error": 2.7230173473358152,
                  "gap_rejected_minus_accepted": 1.5217275423208871
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.333403468132019,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9586193100214004,
                  "rejected_mean_error": 2.2048240711688996,
                  "gap_rejected_minus_accepted": 1.2462047611474991
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.948003962635994,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7614750576019287,
                  "rejected_mean_error": 1.8551372349262238,
                  "gap_rejected_minus_accepted": 1.0936621773242952
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.5761889978741599,
              "spearman": 0.5524600489954118,
              "auroc_top30_bad": 0.7021946666666667,
              "mae": 0.43669681433215735,
              "mse": 0.41818943862901486,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.468,
              "expert_lt_simvla_seed0": 0.968,
              "same_context_pred_std": 0.5739534142651992,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.48394177699834107
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7546122050076723
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8796485632851719
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.1181912576427062
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2786651423238218
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.506000040872643,
              "spearman": 0.54049587487736,
              "auroc_top30_worst": 0.7470049523809524,
              "pairwise_seed_ranking": 0.766,
              "predicted_best_mean_error": 1.4407761282920837,
              "seed0_mean_error": 1.490642247915268,
              "random_seed_mean_error": 1.4961941375732422,
              "oracle_best_mean_error": 1.421916245698929,
              "improvement_over_seed0": 0.04986611962318421,
              "gap_to_oracle": 0.018859882593154742,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.915339515209198
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0905360107620556
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3053705526351929
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.4278694538673613
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4952853263378143
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1158098697662355,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4706980068418716,
                  "rejected_mean_error": 1.7165712018013,
                  "gap_rejected_minus_accepted": 0.2458731949594284
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7752538919448853,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4275448106014614,
                  "rejected_mean_error": 1.698074026800954,
                  "gap_rejected_minus_accepted": 0.27052921619949255
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4866897463798523,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3053705526351929,
                  "rejected_mean_error": 1.6852001000404357,
                  "gap_rejected_minus_accepted": 0.3798295474052429
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1743967533111572,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.089112208293269,
                  "rejected_mean_error": 1.6309653540303892,
                  "gap_rejected_minus_accepted": 0.5418531457371203
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1329386949539186,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4689607808325025,
                  "rejected_mean_error": 1.6857754516601562,
                  "gap_rejected_minus_accepted": 0.2168146708276537
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.7693791389465332,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.4161770863329026,
                  "rejected_mean_error": 1.711673759278797,
                  "gap_rejected_minus_accepted": 0.2954966729458943
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.490100622177124,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.296406741142273,
                  "rejected_mean_error": 1.684877754688263,
                  "gap_rejected_minus_accepted": 0.3884710135459899
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.163257509469986,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0804531347183954,
                  "rejected_mean_error": 1.6288343020938933,
                  "gap_rejected_minus_accepted": 0.5483811673754979
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.4663928075388273,
              "spearman": 0.4208304724501681,
              "auroc_top30_bad": 0.5889093333333333,
              "mae": 0.614749657677859,
              "mse": 0.7167947698849814,
              "expert_lt_perturb_large": 0.944,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.864,
              "same_context_pred_std": 0.5863456493624468,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4451948598176241
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6041231289625167
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1457613032221794
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2530035587300856
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3897421671397985
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.10652897743120689,
              "spearman": -0.08002767566571244,
              "auroc_top30_worst": 0.32989561904761905,
              "pairwise_seed_ranking": 0.6976,
              "predicted_best_mean_error": 1.739369027853012,
              "seed0_mean_error": 1.783529419183731,
              "random_seed_mean_error": 1.7815439200401306,
              "oracle_best_mean_error": 1.7024154713153838,
              "improvement_over_seed0": 0.04416039133071892,
              "gap_to_oracle": 0.03695355653762822,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.8597119312286376
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 2.0708955262716
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.8542239868164063
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.775109612611311
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7780467000961304
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6631947755813603,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.7189847928153144,
                  "rejected_mean_error": 2.3096038656234743,
                  "gap_rejected_minus_accepted": 0.59061907280816
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8251304626464844,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.7759556295777588,
                  "rejected_mean_error": 1.784306550178284,
                  "gap_rejected_minus_accepted": 0.008350920600525225
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4164262413978577,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.8542239868164063,
                  "rejected_mean_error": 1.7018694133758545,
                  "gap_rejected_minus_accepted": -0.1523545734405518
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1767473220825195,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 2.0686134663633644,
                  "rejected_mean_error": 1.6809843758254321,
                  "gap_rejected_minus_accepted": -0.38762909053793226
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6162945985794064,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.722900108496348,
                  "rejected_mean_error": 2.329193215370178,
                  "gap_rejected_minus_accepted": 0.6062931068738302
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.8309325575828552,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.773905867880041,
                  "rejected_mean_error": 1.8120945635296049,
                  "gap_rejected_minus_accepted": 0.03818869564956384
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4083269238471985,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.8519095921516417,
                  "rejected_mean_error": 1.7151492462158202,
                  "gap_rejected_minus_accepted": -0.13676034593582154
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1866819560527802,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 2.145295138396914,
                  "rejected_mean_error": 1.6616511287536213,
                  "gap_rejected_minus_accepted": -0.48364400964329257
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.6890589478099262,
              "spearman": 0.6600226569829598,
              "auroc_top30_bad": 0.8098236190476191,
              "mae": 0.4365585033215582,
              "mse": 0.3771896896162653,
              "expert_lt_perturb_large": 0.98,
              "expert_lt_other_task": 0.492,
              "expert_lt_simvla_seed0": 0.936,
              "same_context_pred_std": 0.6255150600976651,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.4607969300448895
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.6786972011089325
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7705684122160077
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.0088919094711541
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2675651958428322
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.7272457736034932,
              "spearman": 0.6207391876025355,
              "auroc_top30_worst": 0.8609889523809523,
              "pairwise_seed_ranking": 0.7388,
              "predicted_best_mean_error": 1.5509782671928405,
              "seed0_mean_error": 1.6055929944515228,
              "random_seed_mean_error": 1.610197425842285,
              "oracle_best_mean_error": 1.537134670495987,
              "improvement_over_seed0": 0.05461472725868233,
              "gap_to_oracle": 0.013843596696853533,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.7340310981273651
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.052743187508522
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2679835438728333
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.39722435891247
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6093601160049438
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4156179189682008,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4945260505146452,
                  "rejected_mean_error": 2.642866705417633,
                  "gap_rejected_minus_accepted": 1.1483406549029878
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9398025870323181,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.396217747202805,
                  "rejected_mean_error": 2.247425290342337,
                  "gap_rejected_minus_accepted": 0.8512075431395321
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6405465602874756,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2679835438728333,
                  "rejected_mean_error": 1.9507366881370545,
                  "gap_rejected_minus_accepted": 0.6827531442642212
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3088719844818115,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0534668991360039,
                  "rejected_mean_error": 1.795053367744515,
                  "gap_rejected_minus_accepted": 0.7415864686085112
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.4453364849090575,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4891585026846992,
                  "rejected_mean_error": 2.6535034203529357,
                  "gap_rejected_minus_accepted": 1.1643449176682366
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9676168262958527,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3823758070481653,
                  "rejected_mean_error": 2.2681582967440286,
                  "gap_rejected_minus_accepted": 0.8857824896958633
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.6547816395759583,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2586847367286682,
                  "rejected_mean_error": 1.9525012521743774,
                  "gap_rejected_minus_accepted": 0.6938165154457092
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2524497509002686,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0105413699906969,
                  "rejected_mean_error": 1.8060649321041005,
                  "gap_rejected_minus_accepted": 0.7955235621134036
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
        "best_epoch": 61,
        "best_calib_loss": 0.008188355714082718,
        "train_time_sec": 42.32956099510193,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9995425910688039,
              "spearman": 0.9990129977816885,
              "auroc_top30_bad": 0.9997572380952381,
              "mae": 0.024852519425330684,
              "mse": 0.0010494198622059009,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.993,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7047230831863125,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.0857228856892325
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.23048470495585352
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5478809210521169
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.885603111679169
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2657154838076328
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9996455890205984,
              "spearman": 0.9993273836530628,
              "auroc_top30_worst": 0.9999251428571428,
              "pairwise_seed_ranking": 0.94,
              "predicted_best_mean_error": 1.5012617136836053,
              "seed0_mean_error": 1.5817216905951499,
              "random_seed_mean_error": 1.5773716281354426,
              "oracle_best_mean_error": 1.4989939597547055,
              "improvement_over_seed0": 0.0804599769115446,
              "gap_to_oracle": 0.002267753928899774,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.636254191994667
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7672115557670593
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.9652296553373336
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.19929495622317
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.576842271912098
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.7400292396545414,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 1.36872844962279,
                  "rejected_mean_error": 3.4498666725158693,
                  "gap_rejected_minus_accepted": 2.0811382228930793
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9475346207618713,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 1.19929495622317,
                  "rejected_mean_error": 2.709484218978882,
                  "gap_rejected_minus_accepted": 1.5101892627557119
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3415942788124084,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.9652296553373336,
                  "rejected_mean_error": 2.188454888486862,
                  "gap_rejected_minus_accepted": 1.2232252331495284
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9529950171709061,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.7672115557670593,
                  "rejected_mean_error": 1.8467191772937774,
                  "gap_rejected_minus_accepted": 1.079507621526718
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.781074643135071,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 1.3736375609371396,
                  "rejected_mean_error": 3.4544788575172425,
                  "gap_rejected_minus_accepted": 2.080841296580103
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9673320353031158,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 1.2007426658471425,
                  "rejected_mean_error": 2.7246587648391722,
                  "gap_rejected_minus_accepted": 1.5239160989920297
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3527423739433289,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.9573958677053451,
                  "rejected_mean_error": 2.206047513484955,
                  "gap_rejected_minus_accepted": 1.2486516457796097
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9465733468532562,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.7593255181312561,
                  "rejected_mean_error": 1.8558537480831145,
                  "gap_rejected_minus_accepted": 1.0965282299518584
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9836448686481951,
              "spearman": 0.9779547628551799,
              "auroc_top30_bad": 0.984736761904762,
              "mae": 0.09648563048578798,
              "mse": 0.01777352651297966,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6731217366435037,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.13356339062005282
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.25131116853654384
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6568595475241542
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9985665525148312
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2786651423238218
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9714019990724572,
              "spearman": 0.9705828593810301,
              "auroc_top30_worst": 0.9843413333333333,
              "pairwise_seed_ranking": 0.8888,
              "predicted_best_mean_error": 1.4275708785057069,
              "seed0_mean_error": 1.490642247915268,
              "random_seed_mean_error": 1.4961941375732422,
              "oracle_best_mean_error": 1.421916245698929,
              "improvement_over_seed0": 0.06307136940956104,
              "gap_to_oracle": 0.005654632806777915,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8261544280052185
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.9461692044368157
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1307641856193542
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.3148679686888958
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.4952853263378143
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1110862970352176,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.4180530919498868,
                  "rejected_mean_error": 2.1903754358291625,
                  "gap_rejected_minus_accepted": 0.7723223438792757
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.894730269908905,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.3142675536037636,
                  "rejected_mean_error": 2.037181981455404,
                  "gap_rejected_minus_accepted": 0.7229144278516404
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4468634128570557,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1307641856193542,
                  "rejected_mean_error": 1.8598064670562744,
                  "gap_rejected_minus_accepted": 0.7290422814369202
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.172732025384903,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.9464379293850055,
                  "rejected_mean_error": 1.6786249584042274,
                  "gap_rejected_minus_accepted": 0.732187029019222
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.1121959686279297,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.414765867392222,
                  "rejected_mean_error": 2.1735296726226805,
                  "gap_rejected_minus_accepted": 0.7587638052304584
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.890834629535675,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.3074476148355454,
                  "rejected_mean_error": 2.0344104445169844,
                  "gap_rejected_minus_accepted": 0.726962829681439
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4490662217140198,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1284743638038635,
                  "rejected_mean_error": 1.8528101320266723,
                  "gap_rejected_minus_accepted": 0.7243357682228089
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.1824660897254944,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.9345665309164259,
                  "rejected_mean_error": 1.6779832648720971,
                  "gap_rejected_minus_accepted": 0.7434167339556712
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9684013616081382,
              "spearman": 0.9679026507027223,
              "auroc_top30_bad": 0.972136380952381,
              "mae": 0.16623483137413858,
              "mse": 0.06479827350192505,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.992,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6877334749036941,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.12384183849394322
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22325276689827442
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.672022409440577
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.033748658117652
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.3897421671397985
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9318223331959783,
              "spearman": 0.9513325829968532,
              "auroc_top30_worst": 0.973464380952381,
              "pairwise_seed_ranking": 0.888,
              "predicted_best_mean_error": 1.7054206858873366,
              "seed0_mean_error": 1.783529419183731,
              "random_seed_mean_error": 1.7815439200401306,
              "oracle_best_mean_error": 1.7024154713153838,
              "improvement_over_seed0": 0.07810873329639434,
              "gap_to_oracle": 0.0030052145719527967,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.8927718181610107
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.0700611900060604
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.2723024900436402
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.443520717910612
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.7780467000961304
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2185064554214478,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.6295331734551324,
                  "rejected_mean_error": 3.1146684398651123,
                  "gap_rejected_minus_accepted": 1.48513526640998
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.907771646976471,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.4420743526745758,
                  "rejected_mean_error": 2.7838169541983557,
                  "gap_rejected_minus_accepted": 1.3417426015237799
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5646981000900269,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.2723024900436402,
                  "rejected_mean_error": 2.2837909101486207,
                  "gap_rejected_minus_accepted": 1.0114884201049805
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3277921080589294,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.0708275686818571,
                  "rejected_mean_error": 2.0142895903124245,
                  "gap_rejected_minus_accepted": 0.9434620216305674
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2248040437698364,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.6343433086077372,
                  "rejected_mean_error": 3.1262044143676757,
                  "gap_rejected_minus_accepted": 1.4918611057599385
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.9043143093585968,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.436453405867286,
                  "rejected_mean_error": 2.8137391729960366,
                  "gap_rejected_minus_accepted": 1.3772857671287506
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5870444178581238,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.270094801425934,
                  "rejected_mean_error": 2.2969640369415285,
                  "gap_rejected_minus_accepted": 1.0268692355155946
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.3409163653850555,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.0765473871004014,
                  "rejected_mean_error": 2.0217105315968316,
                  "gap_rejected_minus_accepted": 0.9451631444964301
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9865902230801404,
              "spearman": 0.9833893553842558,
              "auroc_top30_bad": 0.9938003809523809,
              "mae": 0.10450683980099856,
              "mse": 0.019816969936766758,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 1.0,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.7303600140967902,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.12112362015992403
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.22775678455531598
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5753809404298663
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9166803443223238
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.2675651958428322
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9790177356449954,
              "spearman": 0.9721016510090568,
              "auroc_top30_worst": 0.9938712380952381,
              "pairwise_seed_ranking": 0.9128,
              "predicted_best_mean_error": 1.5402172971963883,
              "seed0_mean_error": 1.6055929944515228,
              "random_seed_mean_error": 1.610197425842285,
              "oracle_best_mean_error": 1.537134670495987,
              "improvement_over_seed0": 0.06537569725513448,
              "gap_to_oracle": 0.0030826267004013808,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5661690182685852
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.8606103188716449
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.1097666328430176
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2976871904279632
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.6093601160049438
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.650137495994569,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.463088411755032,
                  "rejected_mean_error": 2.9258054542541503,
                  "gap_rejected_minus_accepted": 1.4627170424991183
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.0691603422164917,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2968626024883356,
                  "rejected_mean_error": 2.5448558673310204,
                  "gap_rejected_minus_accepted": 1.2479932648426848
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.5259936451911926,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.1097666328430176,
                  "rejected_mean_error": 2.10895359916687,
                  "gap_rejected_minus_accepted": 0.9991869663238524
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2557246387004852,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.8616665441768999,
                  "rejected_mean_error": 1.859123283541953,
                  "gap_rejected_minus_accepted": 0.9974567393650532
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.6138062238693234,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.4543786279360453,
                  "rejected_mean_error": 2.9665222930908204,
                  "gap_rejected_minus_accepted": 1.512143665154775
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 2.057637095451355,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.285386837421254,
                  "rejected_mean_error": 2.5560461907159713,
                  "gap_rejected_minus_accepted": 1.2706593532947172
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.4962294101715088,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1015664744377136,
                  "rejected_mean_error": 2.109619514465332,
                  "gap_rejected_minus_accepted": 1.0080530400276184
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 1.2577772438526154,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.8459971244373019,
                  "rejected_mean_error": 1.8614996244563138,
                  "gap_rejected_minus_accepted": 1.0155025000190119
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_min_l2_K10"
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
        "best_epoch": 13,
        "best_calib_loss": 0.089607834815979,
        "train_time_sec": 13.857841968536377,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.8549167034876181,
              "spearman": 0.7558646156820994,
              "auroc_top30_bad": 0.8549635476190476,
              "mae": 0.2376198542829773,
              "mse": 0.20500368122367232,
              "expert_lt_perturb_large": 0.996,
              "expert_lt_other_task": 0.515,
              "expert_lt_simvla_seed0": 0.996,
              "same_context_pred_std": 0.6120227794440419,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1753882880359888
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.20263282113075257
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.2298314838975668
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.4489424115876357
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7900858353823423
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9955176939491214,
              "spearman": 0.9937027420599585,
              "auroc_top30_worst": 0.9978893333333334,
              "pairwise_seed_ranking": 0.7959,
              "predicted_best_mean_error": 1.0325070311427116,
              "seed0_mean_error": 1.1003441655039787,
              "random_seed_mean_error": 1.0959886793792248,
              "oracle_best_mean_error": 1.0204971807599068,
              "improvement_over_seed0": 0.06783713436126715,
              "gap_to_oracle": 0.012009850382804776,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.17888692253828048
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3204539456129074
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5122749498128891
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7316991292476654
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0952668563961983
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.153415393829347,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.893526428659757,
                  "rejected_mean_error": 2.91093070602417,
                  "gap_rejected_minus_accepted": 2.0174042773644127
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4443534314632416,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.7316991292476654,
                  "rejected_mean_error": 2.185970037841797,
                  "gap_rejected_minus_accepted": 1.4542709085941317
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.8809590339660645,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5122749498128891,
                  "rejected_mean_error": 1.6782587629795074,
                  "gap_rejected_minus_accepted": 1.1659838131666183
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5277682393789291,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.3204539456129074,
                  "rejected_mean_error": 1.3535378266572953,
                  "gap_rejected_minus_accepted": 1.0330838810443879
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.159871125221253,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8988065430190828,
                  "rejected_mean_error": 2.914182767868042,
                  "gap_rejected_minus_accepted": 2.015376224848959
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4500606060028076,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7330974722703298,
                  "rejected_mean_error": 2.2020842452049254,
                  "gap_rejected_minus_accepted": 1.4689867729345956
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.8724252581596375,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5057485067844391,
                  "rejected_mean_error": 1.6949398242235183,
                  "gap_rejected_minus_accepted": 1.1891913174390791
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5294170528650284,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.31226894903182983,
                  "rejected_mean_error": 1.3630359043280285,
                  "gap_rejected_minus_accepted": 1.0507669552961987
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.4957213482499578,
              "spearman": 0.43319229430653716,
              "auroc_top30_bad": 0.6165470476190477,
              "mae": 0.4646425369165925,
              "mse": 0.46607487912469825,
              "expert_lt_perturb_large": 0.98,
              "expert_lt_other_task": 0.504,
              "expert_lt_simvla_seed0": 0.98,
              "same_context_pred_std": 0.5671065093852007,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.48988156896829604
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3512553535938263
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.46234012131690977
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.6690570449352264
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8104393946766854
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.3886317482017983,
              "spearman": 0.42888579794291076,
              "auroc_top30_worst": 0.7011291428571428,
              "pairwise_seed_ranking": 0.7336,
              "predicted_best_mean_error": 0.9715473263263702,
              "seed0_mean_error": 1.0164055445194244,
              "random_seed_mean_error": 1.022320342183113,
              "oracle_best_mean_error": 0.9497344499826431,
              "improvement_over_seed0": 0.044858218193054245,
              "gap_to_oracle": 0.021812876343727083,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.5619737334251403
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.7114442365291791
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8865450479030609
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.970822649310901
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0215300606012345
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6006671786308289,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0093878920608097,
                  "rejected_mean_error": 1.1308095774650573,
                  "gap_rejected_minus_accepted": 0.12142168540424758
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.347182422876358,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 0.9703556957914073,
                  "rejected_mean_error": 1.174726162284327,
                  "gap_rejected_minus_accepted": 0.20437046649291968
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.090911090373993,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.8865450479030609,
                  "rejected_mean_error": 1.156515073299408,
                  "gap_rejected_minus_accepted": 0.2699700253963472
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8021324276924133,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.7126324054913018,
                  "rejected_mean_error": 1.1247157234074339,
                  "gap_rejected_minus_accepted": 0.41208331791613206
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.6094123005867005,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.0038076565000746,
                  "rejected_mean_error": 1.129786536693573,
                  "gap_rejected_minus_accepted": 0.12597888019349845
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3482994139194489,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 0.961684346517777,
                  "rejected_mean_error": 1.1788319576354254,
                  "gap_rejected_minus_accepted": 0.21714761111764835
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0907856225967407,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.8782351326942444,
                  "rejected_mean_error": 1.1545759563446045,
                  "gap_rejected_minus_accepted": 0.27634082365036017
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7857499569654465,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.7414157792689309,
                  "rejected_mean_error": 1.1090491552722646,
                  "gap_rejected_minus_accepted": 0.3676333760033337
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.45977888429772323,
              "spearman": 0.44307406011746253,
              "auroc_top30_bad": 0.5699245714285714,
              "mae": 0.6090619057119601,
              "mse": 0.7394027644465845,
              "expert_lt_perturb_large": 0.972,
              "expert_lt_other_task": 0.484,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5818782519244776,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.18629761624336244
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.208285551571846
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6020442818760872
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7566327441374461
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8894869814991951
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.10179317278209066,
              "spearman": -0.05780675494832317,
              "auroc_top30_worst": 0.349528380952381,
              "pairwise_seed_ranking": 0.7068,
              "predicted_best_mean_error": 1.2296566483974456,
              "seed0_mean_error": 1.2755211631059646,
              "random_seed_mean_error": 1.2729036058187484,
              "oracle_best_mean_error": 1.194955771803856,
              "improvement_over_seed0": 0.045864514708519044,
              "gap_to_oracle": 0.03470087659358967,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 1.0893349139690398
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 1.5866615909796495
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 1.3052169381141663
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 1.2630074171305719
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.270014890742302
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.129591321945192,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.2111234641340043,
                  "rejected_mean_error": 1.8000377302169799,
                  "gap_rejected_minus_accepted": 0.5889142660829756
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3657943904399872,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 1.2634685471129137,
                  "rejected_mean_error": 1.2896120919587133,
                  "gap_rejected_minus_accepted": 0.026143544845799616
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9257461130619049,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 1.3052169381141663,
                  "rejected_mean_error": 1.2348128433704377,
                  "gap_rejected_minus_accepted": -0.07040409474372855
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.47935035824775696,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 1.5859684449034377,
                  "rejected_mean_error": 1.1644722413800441,
                  "gap_rejected_minus_accepted": -0.42149620352339356
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.031682133674621,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.2145918611685436,
                  "rejected_mean_error": 1.8238848805427552,
                  "gap_rejected_minus_accepted": 0.6092930193742117
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3606527149677277,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 1.2684767579331118,
                  "rejected_mean_error": 1.2964307467142742,
                  "gap_rejected_minus_accepted": 0.027953988781162398
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.912466436624527,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.3164533953666686,
                  "rejected_mean_error": 1.2345889308452607,
                  "gap_rejected_minus_accepted": -0.08186446452140794
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.49896153062582016,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 1.652533850499562,
                  "rejected_mean_error": 1.1485061935562502,
                  "gap_rejected_minus_accepted": -0.5040276569433118
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.7179933310870256,
              "spearman": 0.6980335435032424,
              "auroc_top30_bad": 0.8083253333333335,
              "mae": 0.40914772440425334,
              "mse": 0.3323463193340203,
              "expert_lt_perturb_large": 0.976,
              "expert_lt_other_task": 0.488,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.6426813768315476,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.041182150185108186
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.019628409934043883
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.2458305639743805
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.5267686516682307
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7668621683597565
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.6603254788989044,
              "spearman": 0.5779647818014604,
              "auroc_top30_worst": 0.8253836190476191,
              "pairwise_seed_ranking": 0.7436,
              "predicted_best_mean_error": 1.0492731535434723,
              "seed0_mean_error": 1.0999449586868286,
              "random_seed_mean_error": 1.1049399985671042,
              "oracle_best_mean_error": 1.0338721013069152,
              "improvement_over_seed0": 0.05067180514335634,
              "gap_to_oracle": 0.015401052236557078,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.20570927941799164
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.5689732836893736
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.8124923045396805
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9066205850319822
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1033425257325173
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8468709111213684,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.0082932079765532,
                  "rejected_mean_error": 1.9587863855361938,
                  "gap_rejected_minus_accepted": 0.9504931775596406
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4923720359802246,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 0.9060583460197378,
                  "rejected_mean_error": 1.6939344630835536,
                  "gap_rejected_minus_accepted": 0.7878761170638158
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.2811573147773743,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.8124923045396805,
                  "rejected_mean_error": 1.394192746925354,
                  "gap_rejected_minus_accepted": 0.5817004423856736
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.9410047233104706,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.5701553171720749,
                  "rejected_mean_error": 1.2814509529250664,
                  "gap_rejected_minus_accepted": 0.7112956357529915
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.8690016627311707,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.0175759585698445,
                  "rejected_mean_error": 1.841265959739685,
                  "gap_rejected_minus_accepted": 0.8236900011698405
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4981505274772644,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 0.9047170938017534,
                  "rejected_mean_error": 1.6794308433457026,
                  "gap_rejected_minus_accepted": 0.7747137495439492
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.3069090843200684,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.8182758264541626,
                  "rejected_mean_error": 1.3816140909194947,
                  "gap_rejected_minus_accepted": 0.5633382644653321
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8939263969659805,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.5104754340080988,
                  "rejected_mean_error": 1.2985362958780584,
                  "gap_rejected_minus_accepted": 0.7880608618699596
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
        "best_epoch": 56,
        "best_calib_loss": 0.013226645067334175,
        "train_time_sec": 45.2065372467041,
        "metrics": {
          "train": {
            "all_candidate": {
              "n": 10000,
              "pearson": 0.9896447744821715,
              "spearman": 0.9926011160269889,
              "auroc_top30_bad": 0.9997520952380953,
              "mae": 0.08940422754021711,
              "mse": 0.021675313762231144,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.956,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5924453893660491,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.30444636595249175
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.23167666901946068
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.0959198865711689
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.4236745035290718
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7900858353823423
                }
              ]
            },
            "simvla_only": {
              "n": 5000,
              "contexts": 1000,
              "pearson": 0.9990267665358467,
              "spearman": 0.9993664045826561,
              "auroc_top30_worst": 0.9997826666666666,
              "pairwise_seed_ranking": 0.9434,
              "predicted_best_mean_error": 1.0219699176251889,
              "seed0_mean_error": 1.1003441655039787,
              "random_seed_mean_error": 1.0959886793792248,
              "oracle_best_mean_error": 1.0204971807599068,
              "improvement_over_seed0": 0.07837424787878988,
              "gap_to_oracle": 0.0014727368652820427,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.1716088119149208
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.31531457872390745
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.5102995235204697
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.730223304828008
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0952668563961983
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.192669272422791,
                  "accepted_n": 4500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.8927855356666777,
                  "rejected_mean_error": 2.9175987429618835,
                  "gap_rejected_minus_accepted": 2.024813207295206
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4023739695549011,
                  "accepted_n": 3750,
                  "rejected_n": 1250,
                  "accepted_mean_error": 0.730223304828008,
                  "rejected_mean_error": 2.190397511100769,
                  "gap_rejected_minus_accepted": 1.4601742062727612
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.8626508414745331,
                  "accepted_n": 2500,
                  "rejected_n": 2500,
                  "accepted_mean_error": 0.5102995235204697,
                  "rejected_mean_error": 1.6802341892719268,
                  "gap_rejected_minus_accepted": 1.169934665751457
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5065640062093735,
                  "accepted_n": 1250,
                  "rejected_n": 3750,
                  "accepted_mean_error": 0.31531457872390745,
                  "rejected_mean_error": 1.3552509489536286,
                  "gap_rejected_minus_accepted": 1.039936370229721
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.2181557416915894,
                  "accepted_n": 900,
                  "rejected_n": 100,
                  "accepted_mean_error": 0.8981294045845668,
                  "rejected_mean_error": 2.9202770137786866,
                  "gap_rejected_minus_accepted": 2.02214760919412
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4089549779891968,
                  "accepted_n": 750,
                  "rejected_n": 250,
                  "accepted_mean_error": 0.7311140269438425,
                  "rejected_mean_error": 2.2080345811843873,
                  "gap_rejected_minus_accepted": 1.4769205542405448
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.8601741790771484,
                  "accepted_n": 500,
                  "rejected_n": 500,
                  "accepted_mean_error": 0.5041247000694274,
                  "rejected_mean_error": 1.69656363093853,
                  "gap_rejected_minus_accepted": 1.1924389308691024
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.5114017724990845,
                  "accepted_n": 250,
                  "rejected_n": 750,
                  "accepted_mean_error": 0.31004141664505,
                  "rejected_mean_error": 1.3637784151236216,
                  "gap_rejected_minus_accepted": 1.0537369984785716
                }
              ]
            }
          },
          "calib": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9802362201653556,
              "spearman": 0.9786072782411647,
              "auroc_top30_bad": 0.9848266666666667,
              "mae": 0.12653856782593065,
              "mse": 0.028467248938184947,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.968,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5628328947669302,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.290617795586586
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.19566390528678895
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.20701776654720305
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.5390562779267629
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8104393946766854
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9725766250839154,
              "spearman": 0.9761640602649987,
              "auroc_top30_worst": 0.9829912380952381,
              "pairwise_seed_ranking": 0.8992,
              "predicted_best_mean_error": 0.9531491988897324,
              "seed0_mean_error": 1.0164055445194244,
              "random_seed_mean_error": 1.022320342183113,
              "oracle_best_mean_error": 0.9497344499826431,
              "improvement_over_seed0": 0.06325634562969207,
              "gap_to_oracle": 0.00341474890708926,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3862924945354462
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.4795210230617951
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6647576381206513
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.8445307971127252
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.0215300606012345
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.566398572921753,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.9435711086326175,
                  "rejected_mean_error": 1.7231606283187866,
                  "gap_rejected_minus_accepted": 0.7795895196861691
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4048745334148407,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 0.843963205655331,
                  "rejected_mean_error": 1.5530960129472775,
                  "gap_rejected_minus_accepted": 0.7091328072919465
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9860798418521881,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.6647576381206513,
                  "rejected_mean_error": 1.3783024830818176,
                  "gap_rejected_minus_accepted": 0.7135448449611663
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6685745716094971,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.48043100473979794,
                  "rejected_mean_error": 1.202281399432216,
                  "gap_rejected_minus_accepted": 0.721850394692418
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.587650465965271,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 0.9412780112690395,
                  "rejected_mean_error": 1.6925533437728881,
                  "gap_rejected_minus_accepted": 0.7512753325038486
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.4152210354804993,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 0.8393983805880827,
                  "rejected_mean_error": 1.5418077612680101,
                  "gap_rejected_minus_accepted": 0.7024093806799274
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 0.9858428537845612,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.659059416770935,
                  "rejected_mean_error": 1.3737516722679137,
                  "gap_rejected_minus_accepted": 0.7146922554969787
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.6877962052822113,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.46899196552851846,
                  "rejected_mean_error": 1.200828301077858,
                  "gap_rejected_minus_accepted": 0.7318363355493396
                }
              ]
            }
          },
          "test_id": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9565652663268279,
              "spearman": 0.9630041453766633,
              "auroc_top30_bad": 0.9773120000000001,
              "mae": 0.21425938690707552,
              "mse": 0.10038211735920459,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.976,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5744982812077174,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.3546723212003708
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.26102247104644777
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.1950518658876419
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.5446386881669363
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.8894869814991951
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9005601542079812,
              "spearman": 0.9471390115449675,
              "auroc_top30_worst": 0.9716845714285715,
              "pairwise_seed_ranking": 0.8972,
              "predicted_best_mean_error": 1.1972816108465194,
              "seed0_mean_error": 1.2755211631059646,
              "random_seed_mean_error": 1.2729036058187484,
              "oracle_best_mean_error": 1.194955771803856,
              "improvement_over_seed0": 0.07823955225944523,
              "gap_to_oracle": 0.00232583904266348,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.3996545717716217
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.595020088343284
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.7937116825580597
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.9496959671219275
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.270014890742302
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.4743002891540529,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 1.1335871169567109,
                  "rejected_mean_error": 2.497864854812622,
                  "gap_rejected_minus_accepted": 1.364277737855911
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3193376064300537,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 0.9483515755407583,
                  "rejected_mean_error": 2.2329494797002774,
                  "gap_rejected_minus_accepted": 1.284597904159519
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0503551959991455,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.7937116825580597,
                  "rejected_mean_error": 1.746318098926544,
                  "gap_rejected_minus_accepted": 0.9526064163684844
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8306949883699417,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.5959099827292628,
                  "rejected_mean_error": 1.495196146033744,
                  "gap_rejected_minus_accepted": 0.8992861633044812
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 1.465937578678131,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 1.141068117486106,
                  "rejected_mean_error": 2.485598573684692,
                  "gap_rejected_minus_accepted": 1.3445304561985862
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.3331193029880524,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 0.9477200924075223,
                  "rejected_mean_error": 2.2485179920045155,
                  "gap_rejected_minus_accepted": 1.300797899596993
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0523605942726135,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.7920496757030487,
                  "rejected_mean_error": 1.7589926505088807,
                  "gap_rejected_minus_accepted": 0.9669429748058319
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.8289775997400284,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.6011525340496547,
                  "rejected_mean_error": 1.5027148723602295,
                  "gap_rejected_minus_accepted": 0.9015623383105748
                }
              ]
            }
          },
          "test_ood": {
            "all_candidate": {
              "n": 2500,
              "pearson": 0.9779416182658636,
              "spearman": 0.978300086640014,
              "auroc_top30_bad": 0.9925767619047619,
              "mae": 0.14763773297989974,
              "mse": 0.03780814120683908,
              "expert_lt_perturb_large": 1.0,
              "expert_lt_other_task": 0.932,
              "expert_lt_simvla_seed0": 1.0,
              "same_context_pred_std": 0.5949766602855221,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": -0.2966769703030586
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": -0.2552930459737778
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.09306883988380432
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.4245431166966756
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 0.7668621683597565
                }
              ]
            },
            "simvla_only": {
              "n": 1250,
              "contexts": 250,
              "pearson": 0.9754589259242272,
              "spearman": 0.9738407297540671,
              "auroc_top30_worst": 0.9894979047619048,
              "pairwise_seed_ranking": 0.9192,
              "predicted_best_mean_error": 1.035615171790123,
              "seed0_mean_error": 1.0999449586868286,
              "random_seed_mean_error": 1.1049399985671042,
              "oracle_best_mean_error": 1.0338721013069152,
              "improvement_over_seed0": 0.06432978689670565,
              "gap_to_oracle": 0.0017430704832077648,
              "risk_coverage": [
                {
                  "coverage": 0.1,
                  "mean_true_error": 0.10226350259780884
                },
                {
                  "coverage": 0.25,
                  "mean_true_error": 0.3683046481261651
                },
                {
                  "coverage": 0.5,
                  "mean_true_error": 0.6081441825151443
                },
                {
                  "coverage": 0.75,
                  "mean_true_error": 0.7993915872310778
                },
                {
                  "coverage": 1.0,
                  "mean_true_error": 1.1033425257325173
                }
              ],
              "switch_proxy_all_simvla": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.15164749622345,
                  "accepted_n": 1125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.9613569579256905,
                  "rejected_mean_error": 2.3812126359939576,
                  "gap_rejected_minus_accepted": 1.419855678068267
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5443664491176605,
                  "accepted_n": 937,
                  "rejected_n": 313,
                  "accepted_mean_error": 0.798531543690087,
                  "rejected_mean_error": 2.015827797853147,
                  "gap_rejected_minus_accepted": 1.2172962541630599
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0156220197677612,
                  "accepted_n": 625,
                  "rejected_n": 625,
                  "accepted_mean_error": 0.6081441825151443,
                  "rejected_mean_error": 1.5985408689498901,
                  "gap_rejected_minus_accepted": 0.9903966864347458
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7073223888874054,
                  "accepted_n": 313,
                  "rejected_n": 937,
                  "accepted_mean_error": 0.3693780591027043,
                  "rejected_mean_error": 1.3485195567411954,
                  "gap_rejected_minus_accepted": 0.9791414976384911
                }
              ],
              "switch_proxy_seed0": [
                {
                  "reject_rate": 0.1,
                  "threshold": 2.107324838638305,
                  "accepted_n": 225,
                  "rejected_n": 25,
                  "accepted_mean_error": 0.95327796459198,
                  "rejected_mean_error": 2.4199479055404662,
                  "gap_rejected_minus_accepted": 1.4666699409484862
                },
                {
                  "reject_rate": 0.25,
                  "threshold": 1.5583494305610657,
                  "accepted_n": 187,
                  "rejected_n": 63,
                  "accepted_mean_error": 0.7863875378899395,
                  "rejected_mean_error": 2.030663017242674,
                  "gap_rejected_minus_accepted": 1.2442754793527344
                },
                {
                  "reject_rate": 0.5,
                  "threshold": 1.0302570462226868,
                  "accepted_n": 125,
                  "rejected_n": 125,
                  "accepted_mean_error": 0.6001357197761535,
                  "rejected_mean_error": 1.5997541975975036,
                  "gap_rejected_minus_accepted": 0.99961847782135
                },
                {
                  "reject_rate": 0.75,
                  "threshold": 0.7109344750642776,
                  "accepted_n": 63,
                  "rejected_n": 187,
                  "accepted_mean_error": 0.35492193036609226,
                  "rejected_mean_error": 1.3509420217039751,
                  "gap_rejected_minus_accepted": 0.9960200913378829
                }
              ]
            }
          }
        },
        "target_column": "target_chunk_softmin_l2_K10"
      }
    ]
  }
}
```
