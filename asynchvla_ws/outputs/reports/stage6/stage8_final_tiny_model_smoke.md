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
      "best_epoch": 27,
      "best_calib_loss": 0.09649370610713959,
      "train_time_sec": 7.98074746131897,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.8964581114801701,
            "spearman": 0.8008206098829342,
            "auroc_top30_bad": 0.8711816666666666,
            "mae": 0.22012239133641123,
            "mse": 0.23384366219733765,
            "expert_lt_perturb_large": 0.976,
            "expert_lt_other_task": 0.522,
            "expert_lt_simvla_seed0": 0.98,
            "same_context_pred_std": 0.7832207865543359,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5911985927075147
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.5694584212511777
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7196958574384451
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0188813716868559
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
            "pearson": 0.9978899395221155,
            "spearman": 0.9943178506125777,
            "auroc_top30_worst": 0.9982040000000001,
            "pairwise_seed_ranking": 0.8176,
            "predicted_best_mean_error": 1.715743146687746,
            "seed0_mean_error": 1.7944243976175784,
            "random_seed_mean_error": 1.78608657553792,
            "oracle_best_mean_error": 1.7015940477252007,
            "improvement_over_seed0": 0.07868125092983247,
            "gap_to_oracle": 0.014149098962545237,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7318946895003319
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8835607054948806
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.085894537103176
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3061828931728998
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7850980784833432
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 3.082015371322633,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4902199259797733,
                "rejected_mean_error": 4.439001451015472,
                "gap_rejected_minus_accepted": 2.948781525035699
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0262240767478943,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.3061828931728998,
                "rejected_mean_error": 3.221843634414673,
                "gap_rejected_minus_accepted": 1.9156607412417732
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4987149834632874,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.085894537103176,
                "rejected_mean_error": 2.48430161986351,
                "gap_rejected_minus_accepted": 1.398407082760334
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0764766931533813,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8835607054948806,
                "rejected_mean_error": 2.085610536146164,
                "gap_rejected_minus_accepted": 1.2020498306512832
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 3.151158475875855,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4917173154155414,
                "rejected_mean_error": 4.518788137435913,
                "gap_rejected_minus_accepted": 3.027070822020372
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0253250002861023,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.302976931452751,
                "rejected_mean_error": 3.2687667961120606,
                "gap_rejected_minus_accepted": 1.9657898646593095
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.504427433013916,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0793999856114387,
                "rejected_mean_error": 2.509448809623718,
                "gap_rejected_minus_accepted": 1.4300488240122795
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.077721655368805,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8719973784685134,
                "rejected_mean_error": 2.101900070667267,
                "gap_rejected_minus_accepted": 1.2299026921987535
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8019582018882007,
            "spearman": 0.6768313537407994,
            "auroc_top30_bad": 0.746983619047619,
            "mae": 0.48718627539277076,
            "mse": 0.5244718230313228,
            "expert_lt_perturb_large": 0.988,
            "expert_lt_other_task": 0.516,
            "expert_lt_simvla_seed0": 0.952,
            "same_context_pred_std": 0.8777292620093419,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8387329439520836
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7048796426534653
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.828180061841011
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1290051131169
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
            "pearson": 0.8297430033706596,
            "spearman": 0.7531590448377888,
            "auroc_top30_worst": 0.8453485714285713,
            "pairwise_seed_ranking": 0.7336,
            "predicted_best_mean_error": 2.015247105836868,
            "seed0_mean_error": 2.104481004714966,
            "random_seed_mean_error": 2.077451464056969,
            "oracle_best_mean_error": 1.9888952296972275,
            "improvement_over_seed0": 0.08923389887809785,
            "gap_to_oracle": 0.02635187613964063,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0420703332424164
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1618966379035742
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.5247043677806855
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5975240600833507
              },
              {
                "coverage": 1.0,
                "mean_true_error": 2.079898323702812
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 4.283467102050782,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.84313370013237,
                "rejected_mean_error": 4.210779935836792,
                "gap_rejected_minus_accepted": 2.367646235704422
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7298038601875305,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5972984983101726,
                "rejected_mean_error": 3.5246140949261453,
                "gap_rejected_minus_accepted": 1.9273155966159727
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7186463475227356,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.5247043677806855,
                "rejected_mean_error": 2.635092279624939,
                "gap_rejected_minus_accepted": 1.1103879118442535
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2071031033992767,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1643447223753214,
                "rejected_mean_error": 2.3857342652348343,
                "gap_rejected_minus_accepted": 1.221389542859513
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 4.30448317527771,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.8663247532314724,
                "rejected_mean_error": 4.247887268066406,
                "gap_rejected_minus_accepted": 2.3815625148349335
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.7740204334259033,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6134029703344253,
                "rejected_mean_error": 3.562125328987364,
                "gap_rejected_minus_accepted": 1.9487223586529387
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7249369621276855,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.540343476295471,
                "rejected_mean_error": 2.6686185331344605,
                "gap_rejected_minus_accepted": 1.1282750568389894
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.216706544160843,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1035639880195496,
                "rejected_mean_error": 2.4416883418904267,
                "gap_rejected_minus_accepted": 1.3381243538708771
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6176109392284639,
            "spearman": 0.5027452855921036,
            "auroc_top30_bad": 0.6226841904761904,
            "mae": 0.5229785592913627,
            "mse": 0.6833955534805806,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.484,
            "expert_lt_simvla_seed0": 0.98,
            "same_context_pred_std": 0.6634052395835207,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8979920814037323
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8793459839344024
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9163446705460548
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1383534228404364
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
            "pearson": 0.815129563482506,
            "spearman": 0.7512028861458473,
            "auroc_top30_worst": 0.8090179047619046,
            "pairwise_seed_ranking": 0.7804,
            "predicted_best_mean_error": 1.595315260052681,
            "seed0_mean_error": 1.6571431424617766,
            "random_seed_mean_error": 1.6510543216466904,
            "oracle_best_mean_error": 1.579897521495819,
            "improvement_over_seed0": 0.06182788240909565,
            "gap_to_oracle": 0.015417738556861904,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5774824521541595
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8667409719947057
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1358186751365662
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3628612684923957
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6469764708042145
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.145747327804566,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.484204523563385,
                "rejected_mean_error": 3.11192399597168,
                "gap_rejected_minus_accepted": 1.6277194724082948
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8492732048034668,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.36250702911151,
                "rejected_mean_error": 2.4985670997692755,
                "gap_rejected_minus_accepted": 1.1360600706577655
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4980410933494568,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1358186751365662,
                "rejected_mean_error": 2.158134266471863,
                "gap_rejected_minus_accepted": 1.0223155913352966
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0363807678222656,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8673304736423797,
                "rejected_mean_error": 1.9074131806352221,
                "gap_rejected_minus_accepted": 1.0400827069928424
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.196552562713623,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4845463585853578,
                "rejected_mean_error": 3.210514197349548,
                "gap_rejected_minus_accepted": 1.7259678387641904
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8668277859687805,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3545245362475593,
                "rejected_mean_error": 2.555392021224612,
                "gap_rejected_minus_accepted": 1.2008674849770529
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5191113352775574,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1093984923362732,
                "rejected_mean_error": 2.20488779258728,
                "gap_rejected_minus_accepted": 1.0954893002510069
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0373027920722961,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8354359117765275,
                "rejected_mean_error": 1.933974990232743,
                "gap_rejected_minus_accepted": 1.0985390784562155
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.4989782887816522,
            "spearman": 0.38368052571975536,
            "auroc_top30_bad": 0.5614228571428572,
            "mae": 0.481569468075037,
            "mse": 0.6382217743071785,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.512,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6140502223492884,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9086607466936112
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.05840808968544
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0487631207227708
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2534437890370687
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
            "pearson": 0.6758668987122313,
            "spearman": 0.545259364133993,
            "auroc_top30_worst": 0.6762605714285714,
            "pairwise_seed_ranking": 0.7152,
            "predicted_best_mean_error": 1.6154919165372847,
            "seed0_mean_error": 1.6617511279582977,
            "random_seed_mean_error": 1.6605152992010117,
            "oracle_best_mean_error": 1.592023931980133,
            "improvement_over_seed0": 0.04625921142101297,
            "gap_to_oracle": 0.02346798455715171,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9350114877223968
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.3261276729022846
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.47365281624794
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5762387628812018
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6598132968187331
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.862747323513031,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6336044743061067,
                "rejected_mean_error": 1.895692699432373,
                "gap_rejected_minus_accepted": 0.2620882251262664
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7653515040874481,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.575817216835765,
                "rejected_mean_error": 1.9112648206016125,
                "gap_rejected_minus_accepted": 0.3354476037658476
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5351597666740417,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.47365281624794,
                "rejected_mean_error": 1.8459737773895264,
                "gap_rejected_minus_accepted": 0.3723209611415863
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3371322453022003,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.3270366981197088,
                "rejected_mean_error": 1.7709755971312142,
                "gap_rejected_minus_accepted": 0.4439388990115054
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.866475522518158,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.636297643714481,
                "rejected_mean_error": 1.8908324861526489,
                "gap_rejected_minus_accepted": 0.25453484243816793
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.759272575378418,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5730137700703055,
                "rejected_mean_error": 1.9251461426417034,
                "gap_rejected_minus_accepted": 0.35213237257139784
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5451796054840088,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4700405201911926,
                "rejected_mean_error": 1.8534617357254028,
                "gap_rejected_minus_accepted": 0.38342121553421027
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3583537340164185,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.3189961560188779,
                "rejected_mean_error": 1.7772247281304017,
                "gap_rejected_minus_accepted": 0.4582285721115238
              }
            ]
          }
        }
      }
    }
  ]
}
```
